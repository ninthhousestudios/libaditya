# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
"""Whole Sign cusps under the Vedanga Jyotisha ayanamsas (99, 100) sit on the
sign boundaries of the Vedanga frame, cusp 1 at 0 degrees of the Ascendant's sign.

Swiss Ephemeris has no sidereal mode for 99/100, so cusps are computed tropical
and shifted by ``vedanga_ecliptic_aval``. For Whole Sign that shift used to move
the tropical sign boundaries: cusp 1 landed 23.333 degrees into a sign, here in
sign 8 while the Ascendant is in sign 9 (varuna/57).
"""

from dataclasses import replace

import pytest

from libaditya.charts.chart import Chart
from libaditya.objects.context import EphContext
from libaditya.objects.julian_day import JulianDay
from libaditya.objects.location import Location

JD = 2460310.75
REYKJAVIK = Location(lat=64.1466, long=-21.9426, placename="Reykjavik", utcoffset="0")


def _rashi(hsys, ayanamsa):
    context = replace(EphContext(), timeJD=JulianDay(JD), location=REYKJAVIK, hsys=hsys)
    return Chart(context=context).sidereal(ayanamsa=ayanamsa).rashi()


@pytest.mark.parametrize("ayanamsa", [99, 100])
def test_whole_sign_cusp_one_is_in_the_ascendant_sign(ayanamsa):
    asc = _rashi("C", ayanamsa).cusps()[1]
    assert asc.sign() == 9  # 247.62 degrees
    cusps = _rashi("W", ayanamsa).cusps()
    assert cusps[1].sign() == asc.sign()
    assert cusps[1].ecliptic_longitude() == pytest.approx((asc.sign() - 1) * 30.0)


@pytest.mark.parametrize("ayanamsa", [99, 100])
def test_whole_sign_cusps_are_consecutive_signs(ayanamsa):
    cusps = _rashi("W", ayanamsa).cusps()
    first = cusps[1].sign()
    for n in range(1, 13):
        assert cusps[n].sign() == (first - 1 + n - 1) % 12 + 1
        assert cusps[n].ecliptic_longitude() % 30.0 == pytest.approx(0.0, abs=1e-9)


@pytest.mark.parametrize("ayanamsa", [99, 100])
def test_quadrant_cusps_still_shifted_and_ascendant_unchanged(ayanamsa):
    """Only Whole Sign is rebuilt: the Ascendant (ascmc) and Campanus cusp 1
    stay the shifted tropical Ascendant."""
    campanus = _rashi("C", ayanamsa).cusps()
    whole = _rashi("W", ayanamsa).cusps()
    assert campanus[1].ecliptic_longitude() == pytest.approx(247.62, abs=0.01)
    assert whole.ascendant().ecliptic_longitude() == pytest.approx(
        campanus[1].ecliptic_longitude()
    )
