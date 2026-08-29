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

"""EphContext -> swisseph_rs.EphemerisConfig distiller.

The heart of the pyswisseph -> swisseph_rs migration: collapse libaditya's
C-style "set a global, then call" ephemeris state -- ``set_sid_mode`` /
``set_topo`` / ``set_ephe_path``, the 98->36 ayanamsa remap, the true-sidereal
SVP override, and C's silent clamp of out-of-range ayanamsa codes -- into one
frozen, per-call ``EphemerisConfig``.

Every mapping below was verified bit-for-bit against pyswisseph 2.10.03 during
the migration (the C values reproduced exactly at ``Ephemeris(cfg).calc_ut``).
That equivalence is now baked into the golden fixtures (frozen from pyswisseph);
the standalone distiller reference test was retired with pyswisseph in Phase 3.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import TYPE_CHECKING

from swisseph_rs import (
    CalcFlags,
    EphemerisConfig,
    EphemerisSource,
    SiderealBits,
    SiderealMode,
    TopoPosition,
)
from swisseph_rs.errors import InvalidSiderealMode

if TYPE_CHECKING:
    # Type-only import: the distiller reads ``context.location`` structurally at
    # runtime, so it need not (and must not) pull in libaditya.objects.context,
    # which transitively binds the pyswisseph-flavoured ``constants`` module.
    from libaditya.objects.context import EphContext


# --- libaditya ayanamsa sentinels (NOT real Swiss Ephemeris mode numbers) ----
ADITYA_AYANAMSA: int = 98  # aditya default; SIGNS are computed under Swiss mode 36
ADITYA_SIGNS_MODE: int = 36  # == SiderealMode.GAL_CENT_MULA_WILHELM
TRUE_SIDEREAL_AYANAMSA: int = (
    97  # -> SVP USER_UT at EVERY sidereal site (post libaditya/12)
)

# True-sidereal "User Defined SVP" (masteringthezodiac FAQ; reference year 2000).
# NOTE(dedup): utils.set_swe_true_sidereal_ayanamsa() hardcodes these same two
# literals against the C engine; the implement phase should collapse the C path
# and this one onto a single source of truth rather than carry both.
TRUE_SIDEREAL_T0: float = 2451545.0  # J2000 (JD)
TRUE_SIDEREAL_SVP: float = 31.2836  # fixed sidereal vernal point, degrees

# Coordinate-system bits sourced from swisseph_rs (verified bit-identical to the
# pyswisseph FLG_* values), so the distiller carries no pyswisseph dependency.
_SIDEREAL_BIT: int = int(CalcFlags.SIDEREAL)  # 65536 == const.SID
_TOPOCENTRIC_BIT: int = int(CalcFlags.TOPOCTR)  # 32768 == const.TOPO
_SID_TOPO: int = _SIDEREAL_BIT | _TOPOCENTRIC_BIT  # 98304 == const.SID | const.TOPO

# Bundled ephemeris directory, derived from this file's location instead of
# ``libaditya.constants.ephe_path`` -- importing constants would re-bind the
# pyswisseph-flavoured ``swisseph`` module the migration is removing. This
# resolves to the same ``.../libaditya/ephe/`` (constants.py lives one level up).
_EPHE_PATH: str = (
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    + os.sep
    + "ephe"
    + os.sep
)


@dataclass(frozen=True)
class _SiderealSettings:
    """Resolved sidereal knobs for one ``EphemerisConfig``.

    A single value models all three faithful outcomes, so callers never juggle a
    ``mode`` against an optional ``t0``/``ayan_t0``/``bits`` combination:

    - standard Swiss mode:     ``mode=SiderealMode(n)``
    - C silent-clamp fallback: ``mode=SiderealMode.FAGAN_BRADLEY``
    - true-sidereal SVP:       ``mode=USER`` with ``t0``/``ayan_t0`` and
      ``bits=SiderealBits.USER_UT``
    """

    mode: SiderealMode
    t0: float = 0.0
    ayan_t0: float = 0.0
    bits: SiderealBits | None = None


def base_config() -> EphemerisConfig:
    """The config-independent base ``EphemerisConfig`` (Swiss engine, bundled ``ephe/``).

    No sidereal or topocentric knobs -- the tropical baseline every distilled
    config starts from. Used for calcs that depend only on ``jd`` and the
    ephemeris data, not on the object's zodiac (e.g. ecliptic obliquity /
    nutation, which pyswisseph read off ``swe.calc(jd, ECL_NUT)`` with no sid
    mode in play).
    """
    return EphemerisConfig(
        ephemeris_source=EphemerisSource.SWISS,
        ephe_path=_EPHE_PATH,
    )


def distill_config(
    context: EphContext,
    system: int,
    ayanamsa: int,
) -> EphemerisConfig:
    """Map one object's ephemeris state to a frozen ``EphemerisConfig``.

    ``system`` and ``ayanamsa`` are the PER-OBJECT resolved values
    (``Planet.system`` / ``Planet.ayanamsa()``, ``Cusps.system`` /
    ``Cusps.ayanamsa``) so that mixed ``SID|TOPO`` systems and per-planet
    overrides distill independently.

    Sidereal settings are applied only when ``system`` is *exactly* ``SID`` or
    ``SID|TOPO``; topocentric only when *exactly* ``TOPO`` or ``SID|TOPO`` --
    equality, never bit-AND, because ``DRAC == -8`` would test truthy under
    ``&``. ``ephemeris_source`` and ``ephe_path`` are always set (Swiss engine,
    bundled ``ephe/``).

    Total: never raises for an out-of-range ``ayanamsa`` -- invalid Swiss codes
    are clamped to Fagan-Bradley inside :func:`_resolve_sidereal`, mirroring C's
    ``swe_set_sid_mode``.
    """
    kwargs: dict = {
        "ephemeris_source": EphemerisSource.SWISS,
        "ephe_path": _EPHE_PATH,
    }
    if system == _SIDEREAL_BIT or system == _SID_TOPO:
        sid = _resolve_sidereal(ayanamsa)
        kwargs["sidereal_mode"] = sid.mode
        kwargs["sidereal_t0"] = sid.t0
        kwargs["sidereal_ayan_t0"] = sid.ayan_t0
        if sid.bits is not None:
            kwargs["sidereal_bits"] = sid.bits
    if system == _TOPOCENTRIC_BIT or system == _SID_TOPO:
        kwargs["topographic"] = _topo_position(context)
    return EphemerisConfig(**kwargs)


def _resolve_sidereal(ayanamsa: int) -> _SiderealSettings:
    """Resolve a libaditya ayanamsa code to swisseph_rs sidereal settings.

    Faithful reproduction of ``utils.set_swe_sidereal_mode`` (the single C call
    site since libaditya/12 centralised the true-sidereal override):

    - ``98`` -> mode ``36`` (both ``planets.py`` and ``cusps.py`` remap in-code
      before calling ``swe``).
    - ``97`` -> SVP ``USER_UT`` at EVERY sidereal site (planets, cusps,
      nakshatras) -- the planet-vs-cusp fork is gone post libaditya/12.
    - ``99`` / ``100`` / ``101`` and any other code ``SiderealMode`` rejects ->
      ``FAGAN_BRADLEY``, because C's ``swe_set_sid_mode`` silently clamps every
      out-of-range code to mode 0.
    - otherwise -> ``SiderealMode(ayanamsa)``.

    Total: catches ``swisseph_rs.errors.InvalidSiderealMode`` internally and
    falls back to ``FAGAN_BRADLEY``; never propagates it.
    """
    # 98 (aditya) computes SIGNS under Swiss mode 36; both C sites remap in-code.
    if ayanamsa == ADITYA_AYANAMSA:
        ayanamsa = ADITYA_SIGNS_MODE
    # 97 true-sidereal -> SVP USER_UT (t0/ayan_t0 load-bearing; the USER_UT bit
    # alone still leaves a residual without them).
    if ayanamsa == TRUE_SIDEREAL_AYANAMSA:
        return _SiderealSettings(
            mode=SiderealMode.USER,
            t0=TRUE_SIDEREAL_T0,
            ayan_t0=TRUE_SIDEREAL_SVP,
            bits=SiderealBits.USER_UT,
        )
    # Standard Swiss code, or C's silent clamp of an out-of-range code to mode 0.
    try:
        return _SiderealSettings(mode=SiderealMode(ayanamsa))
    except InvalidSiderealMode:
        return _SiderealSettings(mode=SiderealMode.FAGAN_BRADLEY)


def _topo_position(context: EphContext) -> TopoPosition:
    """Build a ``TopoPosition`` from ``context.location.swe_location()``.

    ``swe_location()`` returns ``(longitude, latitude, altitude)`` -- the
    geographic-longitude-first order the C ``swe.set_topo`` expects; preserve it.
    """
    longitude, latitude, altitude = context.location.swe_location()
    return TopoPosition(longitude=longitude, latitude=latitude, altitude=altitude)
