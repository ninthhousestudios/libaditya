# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
"""An out-of-range chart must not strip Chiron from charts built after it."""

from dataclasses import replace

from libaditya.objects import planets as P
from libaditya.objects.context import EphContext
from libaditya.objects.julian_day import JulianDay


def _planets(jd):
    return P.Planets(replace(EphContext(), timeJD=JulianDay(jd)))


IN_RANGE = 2447936.4375     # 1990-02-13
OUT_OF_RANGE = 1900000.0    # ~490 CE, before Chiron's Swiss Ephemeris window


def test_out_of_range_chart_drops_chiron_for_itself_only():
    assert "Chiron" not in _planets(OUT_OF_RANGE)._planets
    assert "Chiron" in _planets(IN_RANGE)._planets


def test_in_range_chart_keeps_chiron_after_an_out_of_range_one():
    _planets(OUT_OF_RANGE)
    assert "Chiron" in _planets(IN_RANGE)._planets


def test_module_table_is_never_mutated():
    before = dict(P.natural_planets)
    _planets(OUT_OF_RANGE)
    assert P.natural_planets == before
