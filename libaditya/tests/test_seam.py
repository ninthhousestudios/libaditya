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

"""Verify the swisseph_rs seam (libaditya/13, Phase 2 foundation).

The seam is the single native surface every cutover routes through, so this
locks the properties the cutovers rely on -- all offline, both engines ship in
the dev env:

1. FLAG/BODY SURFACE -- ``seam.FLG_*`` and the body ints are value-identical to
   the ``swe.FLG_*`` / ``swe.SUN`` ... ints they replace, and ``to_body`` is the
   inverse of the ``int(Body.X)`` aliases.

2. ENGINE WRAPPER -- ``seam.calc_ut(build_ephemeris(...), ...)`` reproduces C
   ``swe.calc_ut(...)`` bit-for-bit and returns the ``(data-tuple, retflags-int)``
   shape pyswisseph returns, so cutover sites keep their ``[0]`` / ``[1]``.

2b. CALENDAR SURFACE -- ``seam.julday`` / ``seam.revjul`` / ``seam.day_of_week``
   reproduce the C functions bit-for-bit, form a total julday<->revjul inverse
   pair, and restore pyswisseph's default args (``hour=12.0``, ``cal=GREG_CAL``)
   the swisseph_rs functions drop.

3. THE 3 API GAPS -- ``house_name`` and ``get_ayanamsa_name`` reproduce
   ``swe.house_name`` / ``swe.get_ayanamsa_name`` across the full tables (str and
   bytes inputs), and ``FLG_TROPICAL == swe.FLG_TROPICAL == 0``.

3b. HOUSES SURFACE -- ``houses_ex2`` unwraps swisseph_rs's structured
   ``HouseResult`` to pyswisseph's ``(cusps, ascmc, cusp_speeds, ascmc_speeds)``
   shape (live cusp count 36 for Gauquelin, 12 otherwise), and ``house_pos``
   matches ``swe.house_pos`` across the letter set -- including the Sunshine
   sundec pass-through and the Koch circumpolar 0.0 sentinel pyswisseph returns
   where swisseph_rs raises a CError.

4. TYPED EXCEPTIONS -- ``surfacing_errors`` re-raises swisseph_rs SwissephError
   (so the golden's ``capture()`` freezes it) and lets non-backend errors pass.

Run directly::

    python -m libaditya.tests.test_seam

Exit code is 0 when every check passes, 1 otherwise.
"""

from __future__ import annotations

import sys

import swisseph as swe  # C pyswisseph -- the reference the seam must match

from libaditya import constants as const
from libaditya.ephemeris import seam
from libaditya.objects.context import EphContext
from libaditya.objects.location import Location

# --- fixtures ---------------------------------------------------------------
_LOC = Location(lat=40.7484, long=-73.9857, alt=10.0, placename="NYC", icao=None)
_CTX = EphContext(name="seam-test", location=_LOC)
_JD = 2451545.0 + 9000.0  # arbitrary UT epoch
_TOL = 1e-9  # observed residual is 0.0

# Body ids the domain modules pass as ``pnumber`` (== the swe.* ints).
_BODY_IDS = [
    ("SUN", seam.SUN, swe.SUN),
    ("MOON", seam.MOON, swe.MOON),
    ("MERCURY", seam.MERCURY, swe.MERCURY),
    ("VENUS", seam.VENUS, swe.VENUS),
    ("MARS", seam.MARS, swe.MARS),
    ("JUPITER", seam.JUPITER, swe.JUPITER),
    ("SATURN", seam.SATURN, swe.SATURN),
    ("URANUS", seam.URANUS, swe.URANUS),
    ("NEPTUNE", seam.NEPTUNE, swe.NEPTUNE),
    ("PLUTO", seam.PLUTO, swe.PLUTO),
    ("MEAN_NODE", seam.MEAN_NODE, swe.MEAN_NODE),
    ("TRUE_NODE", seam.TRUE_NODE, swe.TRUE_NODE),
    ("EARTH", seam.EARTH, swe.EARTH),
    ("CHIRON", seam.CHIRON, swe.CHIRON),
]

_FLAGS = [
    ("FLG_TROPICAL", seam.FLG_TROPICAL, swe.FLG_TROPICAL),
    ("FLG_SIDEREAL", seam.FLG_SIDEREAL, swe.FLG_SIDEREAL),
    ("FLG_TOPOCTR", seam.FLG_TOPOCTR, swe.FLG_TOPOCTR),
    ("FLG_EQUATORIAL", seam.FLG_EQUATORIAL, swe.FLG_EQUATORIAL),
    ("FLG_HELCTR", seam.FLG_HELCTR, swe.FLG_HELCTR),
    ("FLG_BARYCTR", seam.FLG_BARYCTR, swe.FLG_BARYCTR),
    ("FLG_SPEED", seam.FLG_SPEED, swe.FLG_SPEED),
    ("FLG_SWIEPH", seam.FLG_SWIEPH, swe.FLG_SWIEPH),
]

# Full Swiss house-system letter set (uppercase A..Y plus lowercase 'i').
_HOUSE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYi"


def _check(label: str, condition: bool) -> bool:
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    return bool(condition)


# --- 1: flag / body surface -------------------------------------------------
def run_surface() -> bool:
    print("seam flag/body surface (value-identical to pyswisseph)")
    ok = True

    for name, got, want in _FLAGS:
        ok &= _check(f"{name} == swe.{name} == {want}", got == want)

    # The one gap: swisseph_rs has no TROPICAL flag member; the seam pins it to 0.
    ok &= _check("FLG_TROPICAL is the 0 flag", seam.FLG_TROPICAL == 0)

    for name, got, want in _BODY_IDS:
        ok &= _check(f"{name} == swe.{name} == {want}", got == want)

    # to_body is the inverse of the int(Body.X) aliases (round-trips every id).
    round_trips = all(int(seam.to_body(bid)) == bid for _, bid, _ in _BODY_IDS)
    ok &= _check("to_body(int) round-trips every body id", round_trips)

    # to_flags wraps an int union without changing its bits.
    combo = seam.FLG_SIDEREAL | seam.FLG_TOPOCTR
    ok &= _check("to_flags preserves the bit union", int(seam.to_flags(combo)) == combo)
    return ok


# --- 2: engine wrapper bit-for-bit + return shape ---------------------------
def run_engine() -> bool:
    print("seam.calc_ut bit-for-bit vs pyswisseph + return shape")
    ok = True
    swe.set_ephe_path(const.ephe_path)

    # Tropical, sidereal-Lahiri, topocentric -- one Ephemeris per (system, ayan).
    cases = [
        ("tropical", seam.FLG_TROPICAL, 1, lambda: None, 0),
        (
            "sidereal Lahiri",
            seam.FLG_SIDEREAL,
            1,
            lambda: swe.set_sid_mode(1),
            seam.FLG_SIDEREAL,
        ),
        (
            "topocentric",
            seam.FLG_TOPOCTR,
            1,
            lambda: swe.set_topo(*_LOC.swe_location()),
            seam.FLG_TOPOCTR,
        ),
    ]
    for label, system, ayan, c_setup, flags in cases:
        eph = seam.build_ephemeris(_CTX, system, ayan)
        c_setup()
        worst = 0.0
        shape_ok = True
        for _, bid, c_body in _BODY_IDS:
            data, retflags = seam.calc_ut(eph, _JD, bid, flags)
            c_data, c_ret = swe.calc_ut(_JD, c_body, flags)
            shape_ok &= isinstance(data, tuple) and isinstance(retflags, int)
            shape_ok &= retflags == c_ret
            worst = max(worst, max(abs(a - b) for a, b in zip(data, c_data)))
        ok &= _check(
            f"{label}: max|C - Rust| = {worst:.2e} <= {_TOL:.0e}", worst <= _TOL
        )
        ok &= _check(
            f"{label}: (tuple data, int retflags) matching swe retflags", shape_ok
        )
    return ok


# --- 2b: calendar surface bit-for-bit + defaults + round-trip ---------------
def run_calendar() -> bool:
    print("seam calendar surface: julday / revjul / day_of_week vs pyswisseph")
    ok = True

    # A grid of dates spanning the Julian/Gregorian divide and modern epochs; all
    # left at the GREG_CAL default the library computes in (proleptic Gregorian).
    dates = [
        (1500, 2, 29, 6.0),  # proleptic-Gregorian leap day (pre-1582)
        (1899, 12, 31, 23.5),
        (2000, 1, 1, 12.0),
        (1987, 6, 17, 0.0),
        (2026, 8, 28, 18.25),
        (2200, 11, 5, 9.75),
    ]
    jd_ok = all(
        seam.julday(y, m, d, h) == swe.julday(y, m, d, h) for y, m, d, h in dates
    )
    ok &= _check("julday matches swe.julday across the date grid", jd_ok)

    # revjul is the inverse, and matches swe.revjul on the same JDs.
    rev_ok = True
    roundtrip_ok = True
    for y, m, d, h in dates:
        jd = seam.julday(y, m, d, h)
        rev_ok &= seam.revjul(jd) == swe.revjul(jd)
        roundtrip_ok &= seam.julday(*seam.revjul(jd)) == jd
    ok &= _check("revjul matches swe.revjul on the same JDs", rev_ok)
    ok &= _check("julday(revjul(jd)) == jd (total inverse pair)", roundtrip_ok)

    dow_ok = all(
        seam.day_of_week(seam.julday(y, m, d, h))
        == swe.day_of_week(swe.julday(y, m, d, h))
        for y, m, d, h in dates
    )
    ok &= _check("day_of_week matches swe.day_of_week (0=Mon..6=Sun)", dow_ok)

    # Defaults the swisseph_rs functions drop but call sites depend on: julday
    # omitting hour lands on Swiss noon; revjul defaults to GREG_CAL.
    ok &= _check(
        "julday(y,m,d) default hour==12.0 matches swe",
        seam.julday(1999, 1, 1) == swe.julday(1999, 1, 1),
    )
    ok &= _check(
        "revjul(jd) default cal==GREG_CAL matches swe",
        seam.revjul(2451545.0) == swe.revjul(2451545.0),
    )
    ok &= _check("GREG_CAL == swe.GREG_CAL", seam.GREG_CAL == swe.GREG_CAL)
    ok &= _check("JUL_CAL == swe.JUL_CAL", seam.JUL_CAL == swe.JUL_CAL)
    return ok


# --- 3: the 3 API gaps ------------------------------------------------------
def run_gaps() -> bool:
    print("seam API gaps: house_name, get_ayanamsa_name (hand-rolled tables)")
    ok = True

    # house_name across the full letter set, str AND bytes inputs.
    mismatched = [
        c
        for c in _HOUSE_LETTERS
        if seam.house_name(c) != swe.house_name(c.encode())
        or seam.house_name(c.encode()) != swe.house_name(c.encode())
    ]
    ok &= _check(
        f"house_name matches swe.house_name for all {len(_HOUSE_LETTERS)} letters (str+bytes)",
        not mismatched,
    )
    ok &= _check("house_name('') / unknown letter -> ''", seam.house_name("Z") == "")

    # get_ayanamsa_name across the full Swiss table (0..47).
    bad = [
        code
        for code in range(0, 48)
        if seam.get_ayanamsa_name(code) != swe.get_ayanamsa_name(code)
    ]
    ok &= _check("get_ayanamsa_name matches swe for codes 0..47", not bad)
    ok &= _check(
        "get_ayanamsa_name(-1) / out-of-range -> ''", seam.get_ayanamsa_name(-1) == ""
    )
    return ok


# --- 3b: house cusps + positions --------------------------------------------
# Arbitrary ecliptic (longitude, latitude) for the house_pos sweep, and a high
# ecliptic latitude at a high geo-latitude that pushes Koch ('K') into its
# circumpolar-failure branch.
_HP_XPIN = (137.246, 1.284)
_CIRCUMPOLAR_LAT = 64.15  # Reykjavik-ish; Koch fails circumpolar here
_CIRCUMPOLAR_XPIN = (90.0, 66.0)  # declination beyond 90 - lat -> Koch bails


def run_houses() -> bool:
    print("seam houses: houses_ex2 + house_pos vs pyswisseph (full letter set)")
    ok = True
    swe.set_ephe_path(const.ephe_path)
    lat, lon = _LOC.lat, _LOC.long
    eph = seam.build_ephemeris(_CTX, seam.FLG_TROPICAL, 0)

    # The Sun's equatorial declination -- what the Sunshine ('I'/'i') systems need
    # passed explicitly (pyswisseph serves it off the global its last houses call
    # cached; the swe.houses_ex2 in the loop below refreshes that global to match).
    sundec = seam.calc_ut(eph, _JD, seam.SUN, seam.FLG_EQUATORIAL)[0][1]
    eps = swe.calc_ut(_JD, swe.ECL_NUT, 0)[0][0]

    worst_cusp = worst_ascmc = worst_speed = hp_worst = 0.0
    count_ok = True
    for c in _HOUSE_LETTERS:
        cusps, ascmc, speeds, ascmcspeeds = seam.houses_ex2(eph, _JD, lat, lon, c, 0)
        c_cusps, c_ascmc, c_speeds, c_ascmcspeeds = swe.houses_ex2(
            _JD, lat, lon, c.encode(), 0
        )
        # Live cusp count: 36 for Gauquelin ('G'), 12 otherwise -- as pyswisseph.
        count_ok &= len(cusps) == len(c_cusps)
        worst_cusp = max(worst_cusp, max(abs(a - b) for a, b in zip(cusps, c_cusps)))
        worst_ascmc = max(worst_ascmc, max(abs(a - b) for a, b in zip(ascmc, c_ascmc)))
        worst_speed = max(
            worst_speed, max(abs(a - b) for a, b in zip(speeds, c_speeds))
        )
        # house_pos: seam takes sundec explicitly; pyswisseph reads it off the
        # global the swe.houses_ex2 above just cached, so both see one Sun decl.
        armc = ascmc[2]
        hp = seam.house_pos(armc, lat, eps, _HP_XPIN, c, sundec)
        c_hp = swe.house_pos(armc, lat, eps, _HP_XPIN, c.encode())
        hp_worst = max(hp_worst, abs(hp - c_hp))

    ok &= _check(f"houses_ex2 cusps match (worst {worst_cusp:.2e})", worst_cusp <= _TOL)
    ok &= _check(
        f"houses_ex2 ascmc match (worst {worst_ascmc:.2e})", worst_ascmc <= _TOL
    )
    # cusp speeds carry the intrinsic finite-difference engine noise (~1e-7).
    ok &= _check(
        f"houses_ex2 cusp speeds match (worst {worst_speed:.2e})", worst_speed <= 1e-7
    )
    ok &= _check("cusp count 36 for 'G', 12 otherwise (matches pyswisseph)", count_ok)
    ok &= _check(
        f"house_pos matches for all letters (worst {hp_worst:.2e})", hp_worst <= _TOL
    )

    # GAP: Koch circumpolar. pyswisseph's swe.house_pos ignores the C serr and
    # returns 0.0; swisseph_rs raises CError. The seam reproduces the 0.0 sentinel.
    kc, kascmc, *_ = swe.houses_ex2(_JD, _CIRCUMPOLAR_LAT, lon, b"K", 0)
    seam_koch = seam.house_pos(kascmc[2], _CIRCUMPOLAR_LAT, eps, _CIRCUMPOLAR_XPIN, "K")
    swe_koch = swe.house_pos(kascmc[2], _CIRCUMPOLAR_LAT, eps, _CIRCUMPOLAR_XPIN, b"K")
    ok &= _check(
        "Koch circumpolar house_pos -> 0.0 sentinel (matches swe, not a CError)",
        seam_koch == swe_koch == 0.0,
    )
    return ok


# --- 4: typed exceptions ----------------------------------------------------
def run_errors() -> bool:
    print("seam.surfacing_errors: typed rejections surface, others pass through")
    ok = True

    raised = False
    try:
        with seam.surfacing_errors():
            raise seam.NoConvergence("no convergence")
    except seam.SwissephError as exc:
        raised = type(exc).__name__ == "NoConvergence"
    ok &= _check(
        "SwissephError subclass is re-raised (frozen by capture, not swallowed)", raised
    )

    passed_through = False
    try:
        with seam.surfacing_errors():
            raise ValueError("unrelated")
    except ValueError:
        passed_through = True
    ok &= _check("non-backend exception propagates unchanged", passed_through)

    ok &= _check(
        "error classes are all SwissephError subclasses",
        all(
            issubclass(cls, seam.SwissephError)
            for cls in (
                seam.NoConvergence,
                seam.InvalidHouseSystem,
                seam.InvalidSiderealMode,
                seam.InvalidBody,
                seam.CircumpolarBody,
                seam.BeyondEphemerisLimits,
            )
        ),
    )
    return ok


def run() -> bool:
    return all(
        [
            run_surface(),
            run_engine(),
            run_calendar(),
            run_gaps(),
            run_houses(),
            run_errors(),
        ]
    )


def main() -> int:
    passed = run()
    print("OK" if passed else "FAILED")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
