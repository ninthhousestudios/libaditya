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
    EclipseFlags,
    Ephemeris,
    HeliacalEventType,
    HeliacalFlags,
    HouseSystem,
    RiseSetFlags,
    date as _date,
    errors,
)
from swisseph_rs.houses import house_pos as _house_pos
from swisseph_rs.math import cotrans as _cotrans

from libaditya.ephemeris.config import base_config, distill_config

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

# ECL_NUT is not a body but pyswisseph's special ``swe.calc(jd, ECL_NUT)`` code
# that returns obliquity + nutation instead of a position. swisseph_rs models it
# as ``Body.ECLIPTIC_NUTATION`` (same raw ipl id, -1), so it rides ``calc`` like
# any body -- see :func:`ecliptic_obliquity`.
ECL_NUT: int = int(Body.ECLIPTIC_NUTATION)  # -1


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


# Config-independent baseline Ephemeris (tropical, bundled ``ephe/``), built once
# and shared for the process lifetime. Backs calcs that read only jd + ephemeris
# data -- ``ecliptic_obliquity`` -- where pyswisseph called ``swe.calc`` off the
# global engine with no sid mode in play, so no per-object config is needed.
_DEFAULT_EPHEMERIS: Ephemeris | None = None


def default_ephemeris() -> Ephemeris:
    """The process-shared tropical baseline ``Ephemeris`` (see the note above)."""
    global _DEFAULT_EPHEMERIS
    if _DEFAULT_EPHEMERIS is None:
        _DEFAULT_EPHEMERIS = Ephemeris(base_config())
    return _DEFAULT_EPHEMERIS


def ecliptic_obliquity(jd: float) -> float:
    """True obliquity of the ecliptic of date, as ``swe.calc(jd, ECL_NUT)[0][0]``.

    pyswisseph's ``swe.calc(jd, swe.ECL_NUT)`` returns ``(true_eps, mean_eps,
    d_psi, d_eps, ...)`` -- element ``[0]`` is the true (nutation-included)
    obliquity the nakshatra/rashi coordinate transforms feed into ``cotrans``.
    swisseph_rs returns the same 6-tuple from ``calc(jd, ECLIPTIC_NUTATION)``, so
    ``.data[0]`` is bit-identical to the pyswisseph value (verified 0.0 apart at
    the golden's frozen leaf). ET-frame ``calc`` (not ``calc_ut``) and the
    default ``FLG_SWIEPH`` flag reproduce pyswisseph's flagless call exactly.
    Obliquity depends only on ``jd``, so this rides the shared default Ephemeris
    rather than any object's per-config one.
    """
    result = default_ephemeris().calc(jd, Body.ECLIPTIC_NUTATION, to_flags(FLG_SWIEPH))
    return result.data[0]


def fixstar(
    eph: Ephemeris,
    star: str,
    jd: float,
    flags: int,
) -> tuple[tuple[float, ...], str, int]:
    """Position of a fixed star at ``jd`` (UT), in pyswisseph's ``fixstar`` shape.

    Mirrors ``swe.fixstar2_ut(star, jd, flags) -> (xx, retname, retflags)`` (the
    same shape ``swe.fixstar`` returns): the coordinate 6-tuple is element ``[0]``,
    the canonical ``"traditional,bayer"`` name is ``[1]``, the ``retflags`` int is
    ``[2]`` -- so the nakshatra dhruva path keeps its ``[0][0]`` indexing and the
    fixed-star code keeps splitting ``[1]`` on the comma. swisseph_rs exposes only
    the ``fixstar2`` catalog (``(name, CalcResult)``); against pyswisseph's own
    ``fixstar2_ut`` it is bit-identical, and its SgrA* longitude tracks the v1
    ``swe.fixstar`` to ~5e-8 deg (engine noise floor, under the golden tolerance).

    ``flags_used`` comes straight from the engine (pyswisseph-rs>=0.1.2, which
    fixed swisseph-rs/165 so ``fixstar2_ut`` reports the full retflag -- 258
    tropical, 65858 sidereal -- exactly as pyswisseph and its own ``calc_ut`` do).
    """
    with surfacing_errors():
        name, result = eph.fixstar2_ut(star, jd, to_flags(flags))
    return result.data, name, int(result.flags_used)


def fixstar_mag(eph: Ephemeris, star: str) -> float:
    """Visual magnitude of a fixed star, as ``swe.fixstar2_mag(star)[0]``.

    ``swisseph_rs`` returns ``(canonical_name, magnitude)`` -- the REVERSE of
    pyswisseph's ``(magnitude, retname)`` -- so the magnitude is element ``[1]``
    here. Callers read a bare float (``swe.fixstar2_mag(...)[0]``), so this hands
    back just the float. Catalog-only lookup (no jd / config dependence), but it
    rides the object's ``eph`` like every other seam call.
    """
    with surfacing_errors():
        _name, mag = eph.fixstar2_mag(star)
    return mag


def cotrans(
    coord: tuple[float, float, float], eps: float
) -> tuple[float, float, float]:
    """Rotate a ``(lon, lat, r)`` coordinate about ``eps``, as ``swe.cotrans``.

    Stateless coordinate transform (``swisseph_rs.math.cotrans``); ``eps`` is the
    ecliptic obliquity, ``-eps`` going ecliptic->equatorial and ``+eps`` the
    reverse, exactly as ``swe.cotrans`` used it. Accepts an int coord tuple
    (``(270, 0, 1)``) and returns floats.
    """
    return _cotrans(coord, eps)


# --------------------------------------------------------------------------- #
# eclipse searches (structured result -> pyswisseph (retflag, tret[, attr]))
# --------------------------------------------------------------------------- #
# swisseph_rs returns typed structs (SolarEclipseLocal/.time_maximum/.attr,
# SolarEclipseGlobal, LunarEclipseGlobal) where pyswisseph's
# ``swe.sol_eclipse_when_*`` / ``swe.lun_eclipse_when`` return the flat
# ``(retflag, tret[, attr])`` the SWERashi mixin freezes verbatim. These wrappers
# restore that shape field-for-field so the mixin keeps its ``[1][0]`` (max-eclipse
# jd) indexing and the golden freezes the whole 10-slot ``tret`` / 20-slot ``attr``:
#
# * TRET PADDING. pyswisseph's ``tret`` is always 10 floats; the struct carries
#   only the meaningful contacts, so the trailing slots (and the lunar slot 1,
#   which pyswisseph documents as unused ``?``) are padded 0.0 -- matching the
#   pyswisseph-frozen golden exactly.
# * RETFLAG. ``int(result.flags)`` is the ECL_* type/visibility bit union
#   pyswisseph returns as the first tuple element.
# * SIGNATURE. Mirrors ``swe.*`` (``flags``/``ecltype`` defaults, ``backwards``
#   keyword) with ``eph`` threaded first like every other seam call, so SWERashi
#   calls them exactly as it called ``swe`` -- no behaviour change. (The mixin's
#   glob/lunar calls pass their ``etype`` into the ``flags`` position, as they did
#   against pyswisseph; preserved here so the frozen golden stays bit-faithful.)
def sol_eclipse_when_loc(
    eph: Ephemeris,
    tjd_start: float,
    geopos: tuple[float, float, float],
    flags: int = FLG_SWIEPH,
    backwards: bool = False,
) -> tuple[int, tuple[float, ...], tuple[float, ...]]:
    """Local solar eclipse search, as ``swe.sol_eclipse_when_loc`` returns it.

    Mirrors ``swe.sol_eclipse_when_loc(tjd, geopos, flags, backwards) ->
    (retflag, tret, attr)``: ``tret`` is the 10-slot contact array (max / 1st-4th
    contact / sunrise / sunset, padded), ``attr`` the 20-slot local-circumstance
    array (magnitude / ratios / azimuth-altitude / saros, padded).
    """
    with surfacing_errors():
        r = eph.sol_eclipse_when_loc(tjd_start, to_flags(flags), geopos, backwards)
    tret = (
        r.time_maximum,
        r.time_first_contact,
        r.time_second_contact,
        r.time_third_contact,
        r.time_fourth_contact,
        r.time_sunrise,
        r.time_sunset,
        0.0,
        0.0,
        0.0,
    )
    a = r.attr
    attr = (
        a.magnitude,
        a.diameter_ratio,
        a.obscuration,
        a.core_diameter_km,
        a.azimuth,
        a.true_altitude,
        a.apparent_altitude,
        a.elongation,
        a.nasa_magnitude,
        a.saros_series,
        a.saros_member,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    )
    return int(r.flags), tret, attr


def sol_eclipse_when_glob(
    eph: Ephemeris,
    tjd_start: float,
    flags: int = FLG_SWIEPH,
    ecltype: int = 0,
    backwards: bool = False,
) -> tuple[int, tuple[float, ...]]:
    """Global solar eclipse search, as ``swe.sol_eclipse_when_glob`` returns it.

    Mirrors ``swe.sol_eclipse_when_glob(tjd, flags, ecltype, backwards) ->
    (retflag, tret)``: ``tret`` slots are max / local-noon (ra conjunction) /
    begin / end / totality begin-end / centerline begin-end, the last two
    (annular-total transition) padded 0.0.
    """
    with surfacing_errors():
        r = eph.sol_eclipse_when_glob(
            tjd_start, to_flags(flags), EclipseFlags(ecltype), backwards
        )
    tret = (
        r.time_maximum,
        r.time_ra_conjunction,
        r.time_begin,
        r.time_end,
        r.time_totality_begin,
        r.time_totality_end,
        r.time_centerline_begin,
        r.time_centerline_end,
        0.0,
        0.0,
    )
    return int(r.flags), tret


def lun_eclipse_when(
    eph: Ephemeris,
    tjd_start: float,
    flags: int = FLG_SWIEPH,
    ecltype: int = 0,
    backwards: bool = False,
) -> tuple[int, tuple[float, ...]]:
    """Global lunar eclipse search, as ``swe.lun_eclipse_when`` returns it.

    Mirrors ``swe.lun_eclipse_when(tjd, flags, ecltype, backwards) ->
    (retflag, tret)``: ``tret`` slots are max / (unused) / partial begin-end /
    totality begin-end / penumbral begin-end, trailing slots padded 0.0. Slot 1 is
    the ``?`` pyswisseph documents as unused, held 0.0 to match its return.
    """
    with surfacing_errors():
        r = eph.lun_eclipse_when(
            tjd_start, to_flags(flags), EclipseFlags(ecltype), backwards
        )
    tret = (
        r.time_maximum,
        0.0,
        r.time_partial_begin,
        r.time_partial_end,
        r.time_totality_begin,
        r.time_totality_end,
        r.time_penumbral_begin,
        r.time_penumbral_end,
        0.0,
        0.0,
    )
    return int(r.flags), tret


# --------------------------------------------------------------------------- #
# rise / set / meridian-transit + heliacal + node crossings (search surface)
# --------------------------------------------------------------------------- #
# The last iterative-search family. swisseph_rs replaces pyswisseph's flat return
# tuples with typed structs (RiseSetResult/.time, HeliacalEvent/.start_visible..,
# MoonCrossing/.jd/.longitude/.latitude) and raises SwissephError subclasses where
# pyswisseph returned a sentinel retflag. These wrappers restore the shape each
# call site already consumes, and the rsmi / event-type flag ints below are the
# value-identical drop-ins for swe.CALC_*/BIT_HINDU_RISING and the heliacal event
# codes (verified int-equal to pyswisseph 2.10.03; sourced from the enums so a
# future value shift is caught here, not at the call sites).
CALC_RISE: int = int(RiseSetFlags.RISE)  # 1
CALC_SET: int = int(RiseSetFlags.SET)  # 2
CALC_MTRANSIT: int = int(RiseSetFlags.MTRANSIT)  # 4
CALC_ITRANSIT: int = int(RiseSetFlags.ITRANSIT)  # 8
BIT_HINDU_RISING: int = int(RiseSetFlags.HINDU_RISING)  # 896

HELIACAL_RISING: int = int(HeliacalEventType.MORNING_FIRST)  # 1
HELIACAL_SETTING: int = int(HeliacalEventType.EVENING_LAST)  # 2
EVENING_FIRST: int = int(HeliacalEventType.EVENING_FIRST)  # 3
MORNING_LAST: int = int(HeliacalEventType.MORNING_LAST)  # 4


def rise_trans(
    eph: Ephemeris,
    tjd_ut: float,
    body: int | str,
    rsmi: int,
    geopos: tuple[float, float, float],
    flags: int = FLG_SWIEPH,
    atpress: float = 0.0,
    attemp: float = 0.0,
) -> float:
    """Rise / set / meridian-transit instant, as ``swe.rise_trans(...)[1][0]``.

    Mirrors ``swe.rise_trans(tjdut, body, rsmi, geopos, atpress, attemp, flags)``,
    whose ``(retflag, tret)`` return the call sites index ``[1][0]`` for the event
    jd. swisseph_rs collapses that to ``RiseSetResult.time`` (the meaningful tret[0];
    pyswisseph left tret[1..9] zero) and RAISES on a no-event / circumpolar body
    rather than returning the ``retflag == -2`` sentinel -- so a found event is
    exactly ``.time`` and a miss surfaces through :func:`surfacing_errors` as the
    golden ``__error__`` leaf. ``rsmi`` is the ``CALC_*`` | ``BIT_HINDU_RISING`` int
    the call sites already build. ``body`` is a libaditya body id (int) or, for the
    fixed-star path, a catalog name (str) routed through the ``starname`` slot.
    """
    if isinstance(body, str):
        target, starname = Body.SUN, body
    else:
        target, starname = to_body(body), None
    with surfacing_errors():
        r = eph.rise_trans(
            tjd_ut,
            target,
            starname,
            to_flags(flags),
            RiseSetFlags(rsmi),
            geopos,
            atpress,
            attemp,
        )
    return r.time


def heliacal_ut(
    eph: Ephemeris,
    tjd_start: float,
    geopos: tuple[float, ...],
    atmo: tuple[float, ...],
    observer: tuple[float, ...],
    object_name: str,
    event: int,
    flags: int,
    helflag: int = 0,
) -> tuple[float, float, float]:
    """Heliacal window jds, as ``swe.heliacal_ut(...) -> (start, optimum, end)``.

    Mirrors ``swe.heliacal_ut(tjdut, geopos, atmo, observer, objname, eventtype,
    flags)``: three Julian days -- start of visibility, optimum visibility, end of
    visibility -- which the SWEFirstLast / CelestialObject mixins hand straight to
    ``utils.toJD``. swisseph_rs returns a ``HeliacalEvent`` struct and splits the
    single pyswisseph ``flags`` int into ``epheflag`` (the ordinary ephemeris bits
    the call sites pass as ``sysflg``) and a separate ``HeliacalFlags`` (``helflag``,
    the ``HELFLAG_*`` bits -- none are set by libaditya, so it defaults to 0). The
    ``atmo`` 4-tuple / ``observer`` 6-tuple are passed through as lists.
    """
    with surfacing_errors():
        r = eph.heliacal_ut(
            tjd_start,
            list(geopos),
            list(atmo),
            list(observer),
            object_name,
            HeliacalEventType(event),
            to_flags(flags),
            HeliacalFlags(helflag),
        )
    return r.start_visible, r.optimum_visibility, r.end_visible


def mooncross_node_ut(
    eph: Ephemeris,
    tjd_ut: float,
    flags: int = FLG_SWIEPH,
) -> tuple[float, float, float]:
    """Next Moon/node conjunction, as ``swe.mooncross_node_ut(tjdut, flags)``.

    Mirrors ``swe.mooncross_node_ut -> (jd_cross, xlon, xlat)``, which the Moon
    wrapper unpacks and the golden freezes whole. swisseph_rs returns a
    ``MoonCrossing`` struct (``.jd`` / ``.longitude`` / ``.latitude``).

    DECISION (libaditya/25): this calls swisseph_rs's true-UT ``mooncross_node_ut``,
    which is PHYSICALLY CORRECT and DELIBERATELY BREAKS bit-parity with pyswisseph.
    pyswisseph's ``swe.mooncross_node_ut`` is buggy: it converts the UT start to ET
    for the search but does NOT convert the found jd back to UT, so its "UT" result
    is actually the ET/TT-frame instant -- ~delta-T (~69 s, ~8e-4 JD in 2026) late.
    That bug matches swisseph_rs's ET-frame ``mooncross_node`` bit-for-bit, and the
    seam originally reproduced it (see pyswisseph-rs/32); we now trade that parity
    for correctness. The ~69 s shift is astrologically null (the crossing is ~13.6
    days out), and the affected ``events.mooncross.jd_cross`` golden leaf was
    surgically re-blessed from this corrected value. A no-convergence surfaces
    through :func:`surfacing_errors` as the golden ``__error__`` leaf.
    """
    with surfacing_errors():
        r = eph.mooncross_node_ut(tjd_ut, to_flags(flags))
    return r.jd, r.longitude, r.latitude


# --------------------------------------------------------------------------- #
# calendar surface (engine-independent date math: julday / revjul / day_of_week)
# --------------------------------------------------------------------------- #
# ``swisseph_rs.date`` carries the same Swiss ``swe_julday`` / ``swe_revjul`` /
# ``swe_day_of_week`` implementations, VERIFIED bit-for-bit against pyswisseph
# 2.10.03 (2000-01-01 12h UT -> 2451545.0 and back, DOW 5). This is the pure
# time/calendar math -- no Ephemeris, no engine config -- so it is a total,
# engine-independent inverse pair the vimshottari/panchanga goldens freeze as
# ``JulianDay(start).revjul`` tuples.
#
# GAP: unlike ``swe.julday``/``swe.revjul``, the swisseph_rs functions take NO
# default args -- ``hour`` and ``cal`` are required positionals. The seam
# restores pyswisseph's defaults so cutover call sites keep their arg-omitting
# shape: ``hour`` defaults to 12.0 (Swiss noon, matching ``swe.julday(y,m,d)``)
# and ``cal`` defaults to GREG_CAL (proleptic Gregorian throughout libaditya).
GREG_CAL: int = 1  # swe.GREG_CAL
JUL_CAL: int = 0  # swe.JUL_CAL


def julday(
    year: int,
    month: int,
    day: int,
    hour: float = 12.0,
    cal: int = GREG_CAL,
) -> float:
    """Calendar date -> Julian Day, as ``swe.julday(year, month, day, hour, cal)``.

    ``hour`` and ``cal`` default to pyswisseph's values (Swiss noon, Gregorian)
    so call sites that pass only ``(year, month, day)`` land on the same JD.
    """
    return _date.julday(year, month, day, hour, cal)


def revjul(jd: float, cal: int = GREG_CAL) -> tuple[int, int, int, float]:
    """Julian Day -> ``(year, month, day, decimal_hour)``, as ``swe.revjul(jd, cal)``.

    Total inverse of :func:`julday` on the shared ``cal`` -- the round-trip the
    vimshottari boundary and panchanga instant goldens freeze bit-for-bit.
    """
    return _date.revjul(jd, cal)


def day_of_week(jd: float) -> int:
    """Weekday for a Julian Day (0=Monday .. 6=Sunday), as ``swe.day_of_week(jd)``."""
    return _date.day_of_week(jd)


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


def _hsys_letter(hsys: str | bytes) -> str:
    """Normalise a house-system code to its single ``str`` letter.

    Call sites pass ``context.hsys.encode()`` (``bytes``) or a bare ``str``; both
    the name table and the ``HouseSystem`` construction key off one letter.
    """
    if isinstance(hsys, (bytes, bytearray)):
        hsys = hsys.decode("ascii", "ignore")
    return hsys[:1]


def house_name(hsys: str | bytes) -> str:
    """House-system name for a code letter, as ``swe.house_name`` returns it.

    Accepts the letter as ``str`` or ``bytes`` (call sites pass
    ``context.hsys.encode()``). Unknown codes return ``''``, mirroring
    pyswisseph.
    """
    return _HOUSE_NAMES.get(_hsys_letter(hsys), "")


# --------------------------------------------------------------------------- #
# house cusps + positions
# --------------------------------------------------------------------------- #
# swisseph_rs returns a structured ``HouseResult`` (``.cusps`` / ``.cusp_speeds``
# raw 1-based C arrays, ``.ascmc`` / ``.ascmc_speeds`` as ``AscMc`` objects with
# ``.as_array()``), where pyswisseph's ``swe.houses_ex2`` returns the flat
# ``(cusps, ascmc, cusp_speeds, ascmc_speeds)`` tuples cusps.py already unpacks.
# These wrappers restore the pyswisseph shape:
#
# * CUSP INDEXING. The swisseph_rs cusp array is the raw Swiss C layout -- index
#   0 a dummy, the valid cusps at 1.., trailing slots zero-padded to length 37
#   (Gauquelin's 36-sector maximum). pyswisseph's binding drops the dummy and
#   trims to the live count: 36 cusps for Gauquelin ('G'), 12 otherwise. Slicing
#   ``[1 : 1 + n]`` reproduces that exactly (verified bit-identical, incl. G).
# * HOUSE SYSTEM. ``HouseSystem(ord(letter))`` reconstructs from the code letter
#   ('I'/'i' distinct: Sunshine vs Sunshine/alt.).
_GAUQUELIN_LETTER: str = "G"


def houses_ex2(
    eph: Ephemeris,
    jd: float,
    lat: float,
    lon: float,
    hsys: str | bytes,
    flags: int,
) -> tuple[tuple[float, ...], tuple[float, ...], tuple[float, ...], tuple[float, ...]]:
    """House cusps + speeds at ``jd`` (UT), in pyswisseph's return shape.

    Mirrors ``swe.houses_ex2(jd, lat, lon, hsys, flags) ->
    (cusps, ascmc, cusp_speeds, ascmc_speeds)``. ``eph`` carries the sidereal
    knobs (the distiller folds ``set_sid_mode`` into its config, incl. the aditya
    98->36 remap); the ``flags`` int still carries the ``FLG_SIDEREAL`` bit so the
    backend applies the ayanamsa shift, exactly as pyswisseph did off its global.
    ``cusps``/``cusp_speeds`` are trimmed to the live 1-based cusps (36 for
    Gauquelin, 12 otherwise); ``ascmc``/``ascmc_speeds`` are the 8-element angle
    arrays.
    """
    letter = _hsys_letter(hsys)
    with surfacing_errors():
        result = eph.houses_ex2(jd, to_flags(flags), lat, lon, HouseSystem(ord(letter)))
    n = 36 if letter == _GAUQUELIN_LETTER else 12
    cusps = tuple(result.cusps[1 : 1 + n])
    cusp_speeds = tuple(result.cusp_speeds[1 : 1 + n])
    return (
        cusps,
        tuple(result.ascmc.as_array()),
        cusp_speeds,
        tuple(result.ascmc_speeds.as_array()),
    )


def house_pos(
    armc: float,
    geolat: float,
    eps: float,
    xpin: tuple[float, float],
    hsys: str | bytes,
    sundec: float | None = None,
) -> float:
    """Continuous house position (1.0..13.0; Gauquelin 1.0..37.0) of a body.

    Mirrors ``swe.house_pos(armc, geolat, eps, xpin, hsys)``. ``xpin`` is the
    body's ``(ecliptic_longitude, ecliptic_latitude)``. swisseph_rs is stateless,
    so the Sunshine systems ('I'/'i') -- which pyswisseph served off the Sun
    declination its last houses call cached -- need ``sundec`` passed explicitly
    (the Sun's equatorial declination); every other system ignores it.
    """
    letter = _hsys_letter(hsys)
    try:
        return _house_pos(armc, geolat, eps, HouseSystem(ord(letter)), xpin, sundec)
    except CError:
        # GAP: pyswisseph's swe.house_pos ignores the C ``serr`` out-param and
        # returns the (zero) hpos the engine bails to -- notably Koch ('K') in
        # circumpolar areas (high latitudes). swisseph_rs surfaces that serr as a
        # CError instead of returning 0. Reproduce pyswisseph's sentinel 0.0 so
        # the high-latitude Koch house_pos stays faithful; typed rejections other
        # than CError (InvalidHouseSystem, ...) still propagate.
        return 0.0


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
CError = errors.CError
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
