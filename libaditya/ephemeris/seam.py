# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
#
#    This file is part of libaditya.
#
#    libaditya is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    libaditya is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with libaditya.  If not, see <https://www.gnu.org/licenses/>.

"""The swisseph_rs seam: the single native surface every cutover routes through.

Phase 2 of the pyswisseph -> swisseph_rs migration (see libaditya/3) replaces
every ``import swisseph as swe`` / ``swe.calc_ut`` in the domain modules with
calls into this seam. Concentrating the native surface here means:

* **one importer.** Alongside :mod:`libaditya.ephemeris.config` (the distiller),
  this module is the only place that imports ``swisseph_rs``. Domain modules ask
  the seam for body ids, calc flags, name strings, and typed errors -- they never
  touch ``swisseph_rs`` directly.
* **one return shape.** :func:`calc_ut` unwraps ``CalcResult`` into the
  ``(data, retflags)`` pair pyswisseph's ``swe.calc_ut(...)`` returns, so cutover
  sites keep their existing ``[0]`` / ``[1]`` indexing.
* **the 3 API gaps in one place.** ``swisseph_rs`` has no name functions and no
  ``FLG_TROPICAL``: :func:`house_name` and :func:`get_ayanamsa_name` are
  hand-rolled name tables (the enum ``.name()`` gives wrong casing), and
  :data:`FLG_TROPICAL` is the ``0`` flag.

VALIDATION MODEL (whole arc): the seam imports ``swisseph_rs`` DIRECTLY, so a
cut-over subsystem hits ``swisseph_rs`` regardless of ``LIBADITYA_SWE_BACKEND``.
Running ``python -m libaditya.tests.golden`` on the DEFAULT (pyswisseph) backend
therefore tests each cut-over subsystem's ``swisseph_rs`` output against the
pyswisseph-frozen golden. Green = faithful.

This module stands up the seam and nothing else: it cuts over NO subsystem's
function calls. Only :mod:`libaditya.constants` sources its body/flag aliases and
``ayanamsa_name`` from here (value-identical), dropping its ``import swisseph``.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING, Iterator

from swisseph_rs import (
    Body,
    CalcFlags,
    Ephemeris,
    errors,
)

from libaditya.ephemeris.config import distill_config

if TYPE_CHECKING:
    from libaditya.objects.context import EphContext


# --------------------------------------------------------------------------- #
# coordinate-system flag surface (value-identical to pyswisseph FLG_*)
# --------------------------------------------------------------------------- #
# swisseph_rs.CalcFlags carries the same bit values as pyswisseph's FLG_* ints
# (config.py already asserts int(CalcFlags.SIDEREAL) == 65536 == const.SID).
# These are exposed as plain ``int`` -- not CalcFlags objects -- because
# libaditya threads them through bitwise composition (``system | FLG_SPEED``)
# and equality tests (``system == FLG_SIDEREAL``); a CalcFlags does NOT compare
# equal to its own int, so an int is the faithful drop-in for ``swe.FLG_*``.
FLG_TROPICAL: int = (
    0  # GAP: CalcFlags has no TROPICAL member; the 0 flag == swe.FLG_TROPICAL
)
FLG_SIDEREAL: int = int(CalcFlags.SIDEREAL)  # 65536
FLG_TOPOCTR: int = int(CalcFlags.TOPOCTR)  # 32768
FLG_EQUATORIAL: int = int(CalcFlags.EQUATORIAL)  # 2048
FLG_HELCTR: int = int(CalcFlags.HELCTR)  # 8
FLG_BARYCTR: int = int(CalcFlags.BARYCTR)  # 16384
FLG_SPEED: int = int(CalcFlags.SPEED)  # 256
FLG_SWIEPH: int = int(CalcFlags.SWIEPH)  # 2


# --------------------------------------------------------------------------- #
# body-id surface (pnumber ints, value-identical to pyswisseph)
# --------------------------------------------------------------------------- #
# ``int(Body.SUN) == swe.SUN == 0`` and so on down the table -- swisseph_rs
# keeps the raw Swiss-Ephemeris ipl ids, so these are exact drop-ins for the
# ``swe.SUN`` / ``swe.MOON`` ... ints the domain modules currently pass as
# ``pnumber``. Sourced from the enum so a future id shift is caught here, not in
# 49 call sites.
SUN: int = int(Body.SUN)  # 0
MOON: int = int(Body.MOON)  # 1
MERCURY: int = int(Body.MERCURY)  # 2
VENUS: int = int(Body.VENUS)  # 3
MARS: int = int(Body.MARS)  # 4
JUPITER: int = int(Body.JUPITER)  # 5
SATURN: int = int(Body.SATURN)  # 6
URANUS: int = int(Body.URANUS)  # 7
NEPTUNE: int = int(Body.NEPTUNE)  # 8
PLUTO: int = int(Body.PLUTO)  # 9
MEAN_NODE: int = int(Body.MEAN_NODE)  # 10
TRUE_NODE: int = int(Body.TRUE_NODE)  # 11
EARTH: int = int(Body.EARTH)  # 14
CHIRON: int = int(Body.CHIRON)  # 15


def to_body(pnumber: int) -> Body:
    """Map a libaditya body id (``swe.SUN`` .. ``swe.CHIRON``) to a swisseph_rs Body.

    ``swisseph_rs.Body(n)`` reconstructs from the raw Swiss ipl id, so this is a
    total inverse of the ``int(Body.X)`` aliases above.
    """
    return Body(pnumber)


def to_flags(flags: int) -> CalcFlags:
    """Wrap a libaditya calc-flag int (``FLG_*`` bit union) as a swisseph_rs CalcFlags."""
    return CalcFlags(flags)


# --------------------------------------------------------------------------- #
# engine wrapper
# --------------------------------------------------------------------------- #
# DECISION (libaditya/23): one Ephemeris PER DISTINCT CONFIG, memoized for the
# process lifetime -- NOT one per object. Each Ephemeris is ~4.63MB resident, and
# an Ephemeris depends only on its EphemerisConfig (system, ayanamsa, and -- for
# topocentric -- location); jd/body/flags are calc_ut ARGS, not construction
# inputs. A heavy chart builds ~2,700 Planet/Cusp objects that collapse to a
# handful of distinct configs, so caching turns ~12.5GB resident into a few MB.
# The Ephemeris is immutable/stateless (calc_ut mutates nothing; 20k calls =
# +0.1MB), so sharing one across every object with an identical config is safe.
# This SUPERSEDES the seam foundation's "Ephemeris per object" decision
# (edf7ef2), which predated knowing the 4.63MB/instance cost.
#
# KEY = repr(config), not the config object: EphemerisConfig is unhashable and
# compares by identity (two value-equal configs are ``!=``), so it cannot key a
# dict directly. Its repr is a deterministic, total serialization of every field
# the Ephemeris derives from -- so value-equal configs share a cache slot, the
# 98->36 ayanamsa remap folds two codes into one entry, and non-topo configs
# (``topographic=None`` regardless of location) collapse across locations without
# the seam having to re-derive which inputs matter. Distilling on a cache hit is
# cheap (pure config construction, no ephemeris-file I/O); only Ephemeris(...) is.
_EPHEMERIS_CACHE: dict[str, Ephemeris] = {}


def build_ephemeris(context: EphContext, system: int, ayanamsa: int) -> Ephemeris:
    """Return the process-shared ``Ephemeris`` for this object's distilled config.

    ``system`` and ``ayanamsa`` are the PER-OBJECT resolved values
    (``Planet.system`` / ``Planet.ayanamsa()``, ``Cusps.system`` /
    ``Cusps.ayanamsa``); the distiller collapses them into a frozen
    ``EphemerisConfig`` (Swiss engine, bundled ``ephe/``, sidereal/topo knobs).
    Objects that distill to the same config share one cached Ephemeris (see the
    DECISION note above) rather than each opening their own ~4.63MB instance.
    """
    config = distill_config(context, system, ayanamsa)
    key = repr(config)
    eph = _EPHEMERIS_CACHE.get(key)
    if eph is None:
        eph = Ephemeris(config)
        _EPHEMERIS_CACHE[key] = eph
    return eph


def calc_ut(
    eph: Ephemeris,
    jd: float,
    body: int,
    flags: int,
) -> tuple[tuple[float, ...], int]:
    """Position of ``body`` at ``jd`` (UT), in pyswisseph's return shape.

    Mirrors ``swe.calc_ut(jd, body, flags) -> (xx, retflags)``: the result's
    ``.data`` 6-tuple is element ``[0]``, the ``.flags_used`` int is element
    ``[1]``, so cutover sites keep the ``[0]`` / ``[1]`` indexing they use today.
    ``body`` and ``flags`` are libaditya ints; the conversion to ``Body`` /
    ``CalcFlags`` happens here so callers never see the enums.
    """
    result = eph.calc_ut(jd, to_body(body), to_flags(flags))
    return result.data, int(result.flags_used)


# --------------------------------------------------------------------------- #
# API gap: house-system names (hand-rolled; enum .name() gives wrong casing)
# --------------------------------------------------------------------------- #
# Verified value-identical to pyswisseph 2.10.03 ``swe.house_name(letter)`` for
# the full Swiss house-system set. Keys are the single-letter codes; 'I' and 'i'
# are DISTINCT (Sunshine vs Sunshine/alt.). An unknown letter returns '' -- the
# same empty string pyswisseph yields for an unnamed code.
_HOUSE_NAMES: dict[str, str] = {
    "A": "equal",
    "B": "Alcabitius",
    "C": "Campanus",
    "D": "equal (MC)",
    "E": "equal",
    "F": "Carter poli-equ.",
    "G": "Gauquelin sectors",
    "H": "horizon/azimut",
    "I": "Sunshine",
    "J": "Savard-A",
    "K": "Koch",
    "L": "Pullen SD",
    "M": "Morinus",
    "N": "equal/1=Aries",
    "O": "Porphyry",
    "P": "Placidus",
    "Q": "Pullen SR",
    "R": "Regiomontanus",
    "S": "Sripati",
    "T": "Polich/Page",
    "U": "Krusinski-Pisa-Goelzer",
    "V": "equal/Vehlow",
    "W": "equal/ whole sign",
    "X": "axial rotation system/Meridian houses",
    "Y": "APC houses",
    "i": "Sunshine/alt.",
}


def house_name(hsys: str | bytes) -> str:
    """House-system name for a code letter, as ``swe.house_name`` returns it.

    Accepts the letter as ``str`` or ``bytes`` (call sites pass
    ``context.hsys.encode()``). Unknown codes return ``''``, mirroring
    pyswisseph.
    """
    if isinstance(hsys, (bytes, bytearray)):
        hsys = hsys.decode("ascii", "ignore")
    return _HOUSE_NAMES.get(hsys[:1], "")


# --------------------------------------------------------------------------- #
# API gap: ayanamsa names (hand-rolled; swisseph_rs has no name function)
# --------------------------------------------------------------------------- #
# Verified value-identical to pyswisseph 2.10.03 ``swe.get_ayanamsa_name(code)``
# for the full Swiss sidereal-mode table (0..46; 47 is the empty boundary).
# libaditya's own codes (97 true-sidereal, 98 aditya, 99/100/101 Vedanga) are
# NOT here -- constants.ayanamsa_name resolves those before reaching the seam.
_AYANAMSA_NAMES: tuple[str, ...] = (
    "Fagan/Bradley",  # 0
    "Lahiri",  # 1
    "De Luce",  # 2
    "Raman",  # 3
    "Usha/Shashi",  # 4
    "Krishnamurti",  # 5
    "Djwhal Khul",  # 6
    "Yukteshwar",  # 7
    "J.N. Bhasin",  # 8
    "Babylonian/Kugler 1",  # 9
    "Babylonian/Kugler 2",  # 10
    "Babylonian/Kugler 3",  # 11
    "Babylonian/Huber",  # 12
    "Babylonian/Eta Piscium",  # 13
    "Babylonian/Aldebaran = 15 Tau",  # 14
    "Hipparchos",  # 15
    "Sassanian",  # 16
    "Galact. Center = 0 Sag",  # 17
    "J2000",  # 18
    "J1900",  # 19
    "B1950",  # 20
    "Suryasiddhanta",  # 21
    "Suryasiddhanta, mean Sun",  # 22
    "Aryabhata",  # 23
    "Aryabhata, mean Sun",  # 24
    "SS Revati",  # 25
    "SS Citra",  # 26
    "True Citra",  # 27
    "True Revati",  # 28
    "True Pushya (PVRN Rao)",  # 29
    "Galactic Center (Gil Brand)",  # 30
    "Galactic Equator (IAU1958)",  # 31
    "Galactic Equator",  # 32
    "Galactic Equator mid-Mula",  # 33
    "Skydram (Mardyks)",  # 34
    "True Mula (Chandra Hari)",  # 35
    "Dhruva/Gal.Center/Mula (Wilhelm)",  # 36
    "Aryabhata 522",  # 37
    "Babylonian/Britton",  # 38
    '"Vedic"/Sheoran',  # 39
    "Cochrane (Gal.Center = 0 Cap)",  # 40
    "Galactic Equator (Fiorenza)",  # 41
    "Vettius Valens",  # 42
    "Lahiri 1940",  # 43
    "Lahiri VP285",  # 44
    "Krishnamurti-Senthilathiban",  # 45
    "Lahiri ICRC",  # 46
    "",  # 47 (empty boundary)
)


def get_ayanamsa_name(code: int) -> str:
    """Ayanamsa name for a Swiss sidereal-mode code, as ``swe.get_ayanamsa_name``.

    Out-of-range codes return ``''`` -- the empty string pyswisseph yields for an
    unnamed mode.
    """
    if 0 <= code < len(_AYANAMSA_NAMES):
        return _AYANAMSA_NAMES[code]
    return ""


# --------------------------------------------------------------------------- #
# typed exceptions
# --------------------------------------------------------------------------- #
# The seam is the sole importer of swisseph_rs, so it must also be the single
# source of the backend's typed-error vocabulary: re-export the error classes so
# cutover sites catch (e.g.) ``seam.NoConvergence`` around ``mooncross_node_ut``
# without importing swisseph_rs.errors themselves. Every one is a SwissephError
# subclass, hence an ``Exception`` -- so an UNcaught rejection propagates to the
# golden harness's ``capture()`` and freezes as a visible ``{"__error__": ...}``
# leaf rather than being swallowed. That is the contract :func:`surfacing_errors`
# makes explicit and greppable.
SwissephError = errors.SwissephError
NoConvergence = errors.NoConvergence
InvalidHouseSystem = errors.InvalidHouseSystem
InvalidSiderealMode = errors.InvalidSiderealMode
InvalidBody = errors.InvalidBody
CircumpolarBody = errors.CircumpolarBody
BeyondEphemerisLimits = errors.BeyondEphemerisLimits


@contextmanager
def surfacing_errors() -> Iterator[None]:
    """Wrap a backend call so its typed rejection SURFACES rather than is swallowed.

    ``swisseph_rs`` raises ``SwissephError`` subclasses (``NoConvergence``,
    ``InvalidHouseSystem``, ``InvalidSiderealMode``, ...) where pyswisseph raised
    ``swe.Error``. They are ``Exception`` subclasses, so the golden harness's
    ``capture()`` already freezes each as a visible ``{"__error__": ...}`` leaf.
    This context manager is the single seam idiom cutover code wraps backend
    calls in: it re-raises the typed error unchanged, making the "do not swallow"
    contract explicit and greppable instead of a bare ``try``/``except`` that
    might quietly discard it.
    """
    try:
        yield
    except SwissephError:
        # Deliberately re-raised, never swallowed: the harness freezes it.
        raise
