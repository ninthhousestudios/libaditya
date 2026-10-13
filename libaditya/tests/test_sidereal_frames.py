# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
"""Planets and house cusps of one chart must share one sidereal frame.

The offset tropical - sidereal is the ayanamsa, and it is the same for every
point of the chart. A cusp path that sets its own Swiss sidereal mode can drift
from the planet path: ayanamsa 97 (true sidereal) used to compute cusps in
Fagan-Bradley while planets used the true-sidereal SVP, and the topocentric
flag used to decide whether cusps were sidereal at all.
"""

from dataclasses import replace

import pytest

from libaditya import constants as const
from libaditya.charts.chart import Chart
from libaditya.custom_ayanamsa import CUSTOM_AYANAMSA_ID
from libaditya.objects.context import EphContext
from libaditya.objects.julian_day import JulianDay

JD = 2448057.0  # 1990-06-15 12:00 UT


def _chart():
    return Chart(context=replace(EphContext(), timeJD=JulianDay(JD)))


def _offsets(tropical, sidereal):
    sun = (
        tropical.rashi().planets()["Sun"].ecliptic_longitude()
        - sidereal.rashi().planets()["Sun"].ecliptic_longitude()
    ) % 360
    asc = (
        tropical.rashi().cusps().ascendant().ecliptic_longitude()
        - sidereal.rashi().cusps().ascendant().ecliptic_longitude()
    ) % 360
    return sun, asc


@pytest.mark.parametrize("ayanamsa", [1, 27, 97, CUSTOM_AYANAMSA_ID])
def test_cusps_use_the_planets_ayanamsa(ayanamsa):
    chart = _chart()
    sun, asc = _offsets(chart.tropical(), chart.sidereal(ayanamsa=ayanamsa))
    assert asc == pytest.approx(sun, abs=1e-6)


def test_true_sidereal_cusps_are_not_fagan_bradley():
    chart = _chart()
    _, true_sid = _offsets(chart.tropical(), chart.sidereal(ayanamsa=97))
    _, fagan = _offsets(chart.tropical(), chart.sidereal(ayanamsa=0))
    assert abs(true_sid - fagan) > 1


def test_pure_topocentric_cusps_are_tropical():
    chart = _chart()
    topo = Chart(context=replace(chart.tropical().context, sysflg=const.TOPO))
    assert topo.rashi().cusps().ascendant().ecliptic_longitude() == pytest.approx(
        chart.tropical().rashi().cusps().ascendant().ecliptic_longitude(), abs=1e-9
    )


def test_sidereal_topocentric_cusps_are_sidereal():
    chart = _chart()
    sid = chart.sidereal(ayanamsa=1)
    sid_topo = Chart(context=replace(sid.context, sysflg=const.SID | const.TOPO))
    assert sid_topo.rashi().cusps().ascendant().ecliptic_longitude() == pytest.approx(
        sid.rashi().cusps().ascendant().ecliptic_longitude(), abs=1e-9
    )
