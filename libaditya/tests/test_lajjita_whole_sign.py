# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
"""Lajjita (shamed) reads the whole-sign 5th house, never the 5th cusp.

The 5th is the 5th sign from the lagna's sign whatever the house system. In a
quadrant system at high latitude the 5th cusp can fall in another sign; a
planet there with Sun/Mars/Saturn used to be shamed through "conjunct 5th
cusp".
"""

from dataclasses import replace

import pytest

from libaditya.charts.chart import Chart
from libaditya.objects.context import EphContext
from libaditya.objects.julian_day import JulianDay
from libaditya.objects.location import Location

# Reykjavik, Lahiri: in Placidus the 5th cusp is in sign 3 while the whole-sign
# 5th is sign 5. Jupiter sits in sign 3 conjunct a cruel planet, no node.
JD = 2448059.59
REYKJAVIK = Location(lat=64.13, long=-21.9, placename="Reykjavik", utcoffset="0")


def _rashi(hsys):
    context = replace(EphContext(), timeJD=JulianDay(JD), location=REYKJAVIK, hsys=hsys)
    return Chart(context=context).sidereal(ayanamsa=1).rashi()


def test_fifth_cusp_and_fifth_sign_disagree():
    rashi = _rashi("P")
    assert rashi.signs().lagna().astrological_signs_forward(5) == 5
    assert rashi.cusps()[5].sign() == 3
    assert rashi.planets()["Jupiter"].sign() == 3


def test_planet_on_the_fifth_cusp_is_not_shamed():
    assert "shamed" not in _rashi("P").lajjitaadi_avasthas()["Jupiter"]


@pytest.mark.parametrize("hsys", ["P", "K", "W"])
def test_shamed_does_not_depend_on_house_system(hsys):
    def shamed(rashi):
        return {
            name: states.get("shamed")
            for name, states in rashi.lajjitaadi_avasthas().items()
        }

    assert shamed(_rashi(hsys)) == shamed(_rashi("C"))
