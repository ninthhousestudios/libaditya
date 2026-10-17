# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
"""Every entry point computes the same thing on any thread.

Swiss Ephemeris keeps its ephemeris path per thread. Before libaditya._swe set
it on every thread, a worker thread saw swisseph's default path: Bodygraph and
Planets raised on the missing asteroid file (Chiron), fixed stars raised on the
missing sefstars.txt, and the planets silently fell back to Moshier.
"""

from concurrent.futures import ThreadPoolExecutor

from libaditya.charts.bodygraph import Bodygraph
from libaditya.charts.chart import Chart
from libaditya.objects.context import EphContext
from libaditya.objects.planets import Planets, Sun
from libaditya.stars.fixed_star import FixedStar

CONTEXT = EphContext()


def _on_fresh_thread(compute):
    with ThreadPoolExecutor(max_workers=1) as pool:
        return pool.submit(compute).result()


def _bodygraph_gates():
    return Bodygraph(CONTEXT).all_gates()


def _planet_longitudes():
    return {name: planet.init_coords() for name, planet in Planets(CONTEXT).items()}


def _sun_coords():
    # bit-exact: Moshier lands within an arcsecond of the Swiss Ephemeris
    return Sun(CONTEXT).init_coords()


def _fixed_star_coords():
    return FixedStar("Regulus", CONTEXT).init_coords()


def _chart_bodygraph_gates():
    return Chart(CONTEXT).bodygraph().all_gates()


def test_bodygraph_off_the_main_thread():
    assert _on_fresh_thread(_bodygraph_gates) == _bodygraph_gates()


def test_planets_off_the_main_thread():
    assert _on_fresh_thread(_planet_longitudes) == _planet_longitudes()


def test_planets_use_the_swiss_ephemeris_off_the_main_thread():
    assert _on_fresh_thread(_sun_coords) == _sun_coords()


def test_fixed_stars_off_the_main_thread():
    assert _on_fresh_thread(_fixed_star_coords) == _fixed_star_coords()


def test_chart_off_the_main_thread():
    assert _on_fresh_thread(_chart_bodygraph_gates) == _chart_bodygraph_gates()
