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

TYPES-FIRST SKELETON (arc libaditya/~2, implement phase): data types,
signatures, and error taxonomy only. Bodies are ``NotImplementedError`` pending
review of this contract; every mapping below is already verified bit-for-bit
against pyswisseph 2.10.03 (see the task's implementation_plan).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from swisseph_rs import (
    CalcFlags,
    EphemerisConfig,
    SiderealBits,
    SiderealMode,
    TopoPosition,
)

if TYPE_CHECKING:
    # Type-only import: the distiller reads ``context.location`` structurally at
    # runtime, so it need not (and must not) pull in libaditya.objects.context,
    # which transitively binds the pyswisseph-flavoured ``constants`` module.
    from libaditya.objects.context import EphContext


# --- libaditya ayanamsa sentinels (NOT real Swiss Ephemeris mode numbers) ----
ADITYA_AYANAMSA: int = 98  # aditya default; SIGNS are computed under Swiss mode 36
ADITYA_SIGNS_MODE: int = 36  # == SiderealMode.GAL_CENT_MULA_WILHELM
TRUE_SIDEREAL_AYANAMSA: int = 97  # -> SVP USER_UT, but only at planet/star sites

# True-sidereal "User Defined SVP" (masteringthezodiac FAQ; reference year 2000).
# NOTE(dedup): utils.set_swe_true_sidereal_ayanamsa() hardcodes these same two
# literals against the C engine; the implement phase should collapse the C path
# and this one onto a single source of truth rather than carry both.
TRUE_SIDEREAL_T0: float = 2451545.0  # J2000 (JD)
TRUE_SIDEREAL_SVP: float = 31.2836  # fixed sidereal vernal point, degrees

# Coordinate-system bits sourced from swisseph_rs (verified bit-identical to the
# pyswisseph FLG_* values), so the distiller carries no pyswisseph dependency.
_SIDEREAL_BIT: int = int(CalcFlags.SIDEREAL)  # 65536
_TOPOCENTRIC_BIT: int = int(CalcFlags.TOPOCTR)  # 32768


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


def distill_config(
    context: EphContext,
    system: int,
    ayanamsa: int,
    *,
    true_sidereal_override: bool,
) -> EphemerisConfig:
    """Map one object's ephemeris state to a frozen ``EphemerisConfig``.

    ``system`` and ``ayanamsa`` are the PER-OBJECT resolved values
    (``Planet.system`` / ``Planet.ayanamsa()``, ``Cusps.system`` /
    ``Cusps.ayanamsa``) so that mixed ``SID|TOPO`` systems and per-planet
    overrides distill independently.

    ``true_sidereal_override`` is ``True`` at planet / star / nakshatra sites
    (which apply the SVP override) and ``False`` at cusp sites (which do not).
    That boolean is the fork behind ayanamsa 97 -- see :func:`_resolve_sidereal`.

    Sidereal settings are applied only when ``system`` is *exactly* ``SID`` or
    ``SID|TOPO``; topocentric only when *exactly* ``TOPO`` or ``SID|TOPO`` --
    equality, never bit-AND, because ``DRAC == -8`` would test truthy under
    ``&``. ``ephemeris_source`` and ``ephe_path`` are always set (Swiss engine,
    bundled ``ephe/``).

    Total: never raises for an out-of-range ``ayanamsa`` -- invalid Swiss codes
    are clamped to Fagan-Bradley inside :func:`_resolve_sidereal`, mirroring C's
    ``swe_set_sid_mode``.
    """
    raise NotImplementedError


def _resolve_sidereal(
    ayanamsa: int,
    *,
    true_sidereal_override: bool,
) -> _SiderealSettings:
    """Resolve a libaditya ayanamsa code to swisseph_rs sidereal settings.

    Faithful reproduction of libaditya's two divergent C call sites:

    - ``98`` -> mode ``36`` (both ``planets.py`` and ``cusps.py`` remap in-code
      before calling ``swe``).
    - ``97`` **with** ``true_sidereal_override`` (planets / stars / nakshatras)
      -> SVP ``USER_UT``.
    - ``97`` **without** override (cusps), plus ``99`` / ``100`` / ``101`` and
      any other code ``SiderealMode`` rejects -> ``FAGAN_BRADLEY``, because C's
      ``swe_set_sid_mode`` silently clamps every out-of-range code to mode 0.
    - otherwise -> ``SiderealMode(ayanamsa)``.

    Total: catches ``swisseph_rs.errors.InvalidSiderealMode`` internally and
    falls back to ``FAGAN_BRADLEY``; never propagates it.
    """
    raise NotImplementedError


def _topo_position(context: EphContext) -> TopoPosition:
    """Build a ``TopoPosition`` from ``context.location.swe_location()``.

    ``swe_location()`` returns ``(longitude, latitude, altitude)`` -- the
    geographic-longitude-first order the C ``swe.set_topo`` expects; preserve it.
    """
    raise NotImplementedError
