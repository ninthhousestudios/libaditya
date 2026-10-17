# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
"""A planet just past its station is retrograde, even when its rounded speed is -0.0."""

from dataclasses import replace

import swisseph as swe

from libaditya.objects import planets as P
from libaditya.objects.context import EphContext
from libaditya.objects.julian_day import JulianDay

# 2024-04-01 22:18 UT, a few minutes after Mercury's station retrograde.
# Swiss Ephemeris gives a speed of about -0.00028 deg/day: negative, but it
# rounds to -0.0 at the default three decimals.
JUST_AFTER_STATION = 2460402.4291666667


def test_reference_speed_is_negative_but_rounds_to_zero():
    speed = swe.calc_ut(JUST_AFTER_STATION, swe.MERCURY, swe.FLG_SWIEPH | swe.FLG_SPEED)[0][3]
    assert -0.0005 < speed < 0
    assert round(speed, 3) == 0


def test_mercury_is_retrograde_just_after_station():
    ctx = replace(EphContext(), timeJD=JulianDay(JUST_AFTER_STATION))
    mercury = P.Planets(ctx)._planets["Mercury"]
    assert mercury.longitude_speed() == 0  # the rounded display value
    assert mercury.retrograde()
