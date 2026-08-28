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

"""Verify the EphContext -> EphemerisConfig distiller (libaditya/2, Phase 1).

Two layers, both offline (both engines ship in the dev env):

1. FIELD MAPPING -- ``distill_config`` yields an ``EphemerisConfig`` whose fields
   match the (system, ayanamsa) contract: ephe_path/source always; sidereal only
   for exactly SID or SID|TOPO; topo only for exactly TOPO or SID|TOPO; the
   98->36 remap, the 97->SVP override, and the 99/100/101 -> Fagan-Bradley clamp.

2. BIT-FOR-BIT -- for each coordinate system, ``Ephemeris(distill_config(...))``
   .calc_ut reproduces C ``pyswisseph`` (the "set a global, then call" path the
   distiller replaces) to within 1e-9. This is the accept-crit-2 evidence for the
   true-sidereal SVP path, plus standard/aditya/clamp/topo/mixed.

Run directly::

    python -m libaditya.tests.test_distiller

Exit code is 0 when every check passes, 1 otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

import swisseph as swe  # C pyswisseph -- the reference the distiller must match
import swisseph_rs as sr

import libaditya.constants as const
from libaditya.ephemeris import config as distiller
from libaditya.ephemeris.config import distill_config
from libaditya.objects.context import EphContext
from libaditya.objects.location import Location

# --- fixtures ---------------------------------------------------------------
# A pinned context; only context.location.swe_location() is read (topo paths).
_LOC = Location(lat=40.7484, long=-73.9857, alt=10.0, placename="NYC", icao=None)
_CTX = EphContext(name="distiller-test", location=_LOC)
_GEO = _LOC.swe_location()  # (longitude, latitude, altitude)

_JD = 2451545.0 + 9000.0  # arbitrary UT epoch
_BODIES = [("sun", swe.SUN, sr.Body.SUN), ("moon", swe.MOON, sr.Body.MOON)]

_TOL = 1e-9  # plan gate (observed residual is 0.0)

# System values (== the swe FLG_* the call site passes for these coordinates).
_TROP = 0
_SID = int(sr.CalcFlags.SIDEREAL)  # 65536
_TOPO = int(sr.CalcFlags.TOPOCTR)  # 32768
_SID_TOPO = _SID | _TOPO  # 98304
_DRAC = -8


def _check(label: str, condition: bool) -> bool:
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    return bool(condition)


# --- layer 1: field mapping -------------------------------------------------
def run_field_mapping() -> bool:
    print("distiller field mapping")
    ok = True

    # ephe_path is derived without importing constants, but must resolve to the
    # same bundled directory constants uses.
    ok &= _check(
        "_EPHE_PATH resolves to the bundled ephe/ (== constants.ephe_path)",
        Path(distiller._EPHE_PATH) == Path(const.ephe_path),
    )

    # Always: Swiss source + bundled ephe path, for every system.
    for name, system in [("tropical", _TROP), ("sidereal", _SID), ("draconic", _DRAC)]:
        cfg = distill_config(_CTX, system, ayanamsa=1)
        ok &= _check(
            f"{name}: ephemeris_source=SWISS, ephe_path=bundled",
            cfg.ephemeris_source == sr.EphemerisSource.SWISS
            and Path(cfg.ephe_path) == Path(const.ephe_path),
        )

    # Tropical: no sidereal, no topo.
    trop = distill_config(_CTX, _TROP, ayanamsa=1)
    ok &= _check(
        "tropical: sidereal_mode is None, topographic is None",
        trop.sidereal_mode is None and trop.topographic is None,
    )

    # Draconic (-8) is neither SID nor TOPO -> plain config (calc uses flags 0).
    drac = distill_config(_CTX, _DRAC, ayanamsa=1)
    ok &= _check(
        "draconic(-8): plain config, no sidereal/topo (does not test truthy)",
        drac.sidereal_mode is None and drac.topographic is None,
    )

    # Standard sidereal code passes straight through.
    lahiri = distill_config(_CTX, _SID, ayanamsa=1)
    ok &= _check(
        "sidereal(1): sidereal_mode=SiderealMode(1), no topo",
        lahiri.sidereal_mode == sr.SiderealMode(1) and lahiri.topographic is None,
    )

    # 98 (aditya) remaps to Swiss mode 36 (GAL_CENT_MULA_WILHELM).
    aditya = distill_config(_CTX, _SID, ayanamsa=98)
    ok &= _check(
        "sidereal(98): remapped to SiderealMode(36) == GAL_CENT_MULA_WILHELM",
        aditya.sidereal_mode == sr.SiderealMode.GAL_CENT_MULA_WILHELM,
    )

    # 97 (true sidereal) -> SVP USER_UT, t0/ayan_t0 carried, t0_is_ut auto-set.
    svp = distill_config(_CTX, _SID, ayanamsa=97)
    ok &= _check(
        "sidereal(97): USER + SVP t0/ayan_t0 + USER_UT bit",
        svp.sidereal_mode == sr.SiderealMode.USER
        and svp.sidereal_t0 == 2451545.0
        and svp.sidereal_ayan_t0 == 31.2836
        and svp.sidereal_bits == sr.SiderealBits.USER_UT
        and svp.sidereal_t0_is_ut is True,
    )

    # 99/100/101 (and any code SiderealMode rejects) clamp to Fagan-Bradley,
    # mirroring C swe_set_sid_mode; never raises.
    for code in (99, 100, 101):
        clamp = distill_config(_CTX, _SID, ayanamsa=code)
        ok &= _check(
            f"sidereal({code}): clamped to FAGAN_BRADLEY (no raise)",
            clamp.sidereal_mode == sr.SiderealMode.FAGAN_BRADLEY,
        )

    # Topo only: topographic set from swe_location(), no sidereal.
    topo = distill_config(_CTX, _TOPO, ayanamsa=1)
    tp = topo.topographic
    ok &= _check(
        "topo: TopoPosition == swe_location() (lon,lat,alt order), no sidereal",
        topo.sidereal_mode is None
        and tp is not None
        and (tp.longitude, tp.latitude, tp.altitude) == _GEO,
    )

    # Mixed SID|TOPO (accept-crit 4): both branches distill independently.
    mixed = distill_config(_CTX, _SID_TOPO, ayanamsa=97)
    mtp = mixed.topographic
    ok &= _check(
        "SID|TOPO(97): SVP sidereal AND topo both applied",
        mixed.sidereal_mode == sr.SiderealMode.USER
        and mixed.sidereal_bits == sr.SiderealBits.USER_UT
        and mtp is not None
        and (mtp.longitude, mtp.latitude, mtp.altitude) == _GEO,
    )

    return ok


# --- layer 2: bit-for-bit vs C pyswisseph -----------------------------------
def _c_positions(setup, flags):
    """Apply the C 'set globals then call' path and return {body: 6-tuple}."""
    swe.set_ephe_path(const.ephe_path)
    setup()
    return {name: swe.calc_ut(_JD, c_body, flags)[0] for name, c_body, _ in _BODIES}


def _rs_positions(system, ayanamsa, flags):
    """Distill a config, open one Ephemeris, and return {body: 6-tuple}."""
    eph = sr.Ephemeris(distill_config(_CTX, system, ayanamsa))
    return {
        name: eph.calc_ut(_JD, rs_body, sr.CalcFlags(flags)).data
        for name, _, rs_body in _BODIES
    }


def run_bit_for_bit() -> bool:
    print("distiller bit-for-bit vs pyswisseph 2.10.03")
    ok = True

    def svp_setup():
        swe.set_sid_mode(swe.SIDM_USER + swe.SIDBIT_USER_UT, 2451545.0, 31.2836)

    def topo_setup():
        swe.set_topo(_GEO[0], _GEO[1], _GEO[2])

    def sidtopo_setup():
        svp_setup()
        topo_setup()

    # (label, system, ayanamsa, C setup, calc flags)
    cases = [
        ("tropical", _TROP, 1, lambda: None, 0),
        ("sidereal Lahiri (1)", _SID, 1, lambda: swe.set_sid_mode(1), _SID),
        ("aditya 98->36", _SID, 98, lambda: swe.set_sid_mode(36), _SID),
        ("true-sidereal SVP (97)", _SID, 97, svp_setup, _SID),
        ("clamp 99->Fagan-Bradley", _SID, 99, lambda: swe.set_sid_mode(99), _SID),
        ("topocentric", _TOPO, 1, topo_setup, _TOPO),
        ("mixed SID|TOPO (97)", _SID_TOPO, 97, sidtopo_setup, _SID_TOPO),
    ]

    for label, system, ayanamsa, setup, flags in cases:
        c_pos = _c_positions(setup, flags)
        rs_pos = _rs_positions(system, ayanamsa, flags)
        worst = 0.0
        for name, _, _ in _BODIES:
            worst = max(
                worst, max(abs(a - b) for a, b in zip(c_pos[name], rs_pos[name]))
            )
        ok &= _check(
            f"{label}: max|C - Rust| = {worst:.2e} <= {_TOL:.0e}", worst <= _TOL
        )

    return ok


def run() -> bool:
    a = run_field_mapping()
    b = run_bit_for_bit()
    return a and b


def main() -> int:
    passed = run()
    print("OK" if passed else "FAILED")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
