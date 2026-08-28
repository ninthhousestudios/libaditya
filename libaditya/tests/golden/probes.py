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

"""Snapshot probes: walk a computed Chart and emit its numeric/categorical leaves.

Every value read here is a RAW instance attribute (``planet.long``,
``planet._declination``, ``cusps.ascmc`` ...) or an exact zero-argument method,
never a display accessor -- the public accessors (``longitude()``, ``speed()``,
``degrees_elapsed()`` ...) round to ``context.toround`` (3 dp) or a hardcoded 2-3
dp, which would throw away exactly the sub-arcsecond drift this harness exists
to catch.  See ``README.md`` for the full list of rounding traps that were
deliberately bypassed.

The probes build plain dicts/lists holding raw floats and a few domain objects
(``JulianDay``, ``Location``, ``EphContext``, ``Nakshatra``); ``canonical`` then
turns the whole record into a deterministic JSON-able tree, using the reducers
returned by ``reducers()`` for those domain objects.

Anything that can raise (a house system an engine rejects, a chart method that
is broken on some path) is wrapped in ``capture`` so the failure is frozen as a
visible ``{"__error__": ...}`` leaf rather than swallowed or crashing the run --
a backend that changes an error then trips the diff like any other value.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .canonical import canonicalize
from .subjects import HOUSE_SYSTEMS, Case, build_chart

SCHEMA_VERSION = 1


# --------------------------------------------------------------------------- #
# error capture
# --------------------------------------------------------------------------- #
def capture(fn: Callable[[], Any]) -> Any:
    try:
        return fn()
    except Exception as exc:  # noqa: BLE001 - freezing the failure IS the point
        return {"__error__": f"{type(exc).__name__}: {exc}"}


# --------------------------------------------------------------------------- #
# domain reducers (passed to canonicalize)
# --------------------------------------------------------------------------- #
def reduce_julianday(jd, recurse):
    return recurse(
        {
            "jd": jd.jd,
            "datetime": list(jd.datetime),
            "utcoffset": jd.utcoffset,
        }
    )


def reduce_location(loc, recurse):
    return recurse(
        {
            "lat": loc.lat,
            "long": loc.long,
            "alt": loc.alt,
            "placename": loc._placename,
            "utcoffset": loc.utcoffset,
            "planet": loc._planet,
        }
    )


def reduce_context(ctx, recurse):
    # only the calculation-affecting configuration is echoed; the pure-display
    # fields (names_type, signize, toround, print_*) do not touch the math.
    return recurse(
        {
            "name": ctx.name,
            "timeJD": ctx.timeJD,
            "location": ctx.location,
            "sysflg": ctx.sysflg,
            "amsha": ctx.amsha,
            "ayanamsa": ctx.ayanamsa,
            "hsys": ctx.hsys,
            "circle": ctx.circle,
            "rashi_temporary_friendships": ctx.rashi_temporary_friendships,
            "rashi_aspects": ctx.rashi_aspects,
            "sign_names": ctx.sign_names,
            "cot_savana_day": ctx.cot_savana_day,
            "cot_planet_order": ctx.cot_planet_order,
        }
    )


def reduce_nakshatra(nak, recurse):
    return recurse(
        {
            "name": nak.identity(),
            "index": nak.index(),
            "ashvini_longitude": nak.ash_long,
            "base_longitude": nak.base_long,
            "naksize": nak.naksize(),
            "ayanamsa": nak.ayanamsa,
        }
    )


def reducers() -> list[tuple[type, Callable]]:
    from libaditya.objects.context import EphContext
    from libaditya.objects.julian_day import JulianDay
    from libaditya.objects.location import Location
    from libaditya.objects.nakshatras import Nakshatra

    return [
        (JulianDay, reduce_julianday),
        (Location, reduce_location),
        (EphContext, reduce_context),
        (Nakshatra, reduce_nakshatra),
    ]


# --------------------------------------------------------------------------- #
# object probes (raw attributes only)
# --------------------------------------------------------------------------- #
def probe_planet(p) -> dict:
    """Full raw state of a rashi (amsha=1) planet."""
    return {
        "id": p._id,
        "pnumber": p.pnumber,
        "amsha": p._amsha,
        "sysflg": p.sysflg,
        "system": p.system,
        "ayanamsa_id": p._ayanamsa,
        "long": p.long,
        "lat": p.lat,
        "dist": p.dist,
        "long_speed": p.long_speed,
        "lat_speed": p.lat_speed,
        "dist_speed": p.dist_speed,
        "right_ascension": p._right_ascension,
        "declination": p._declination,
        "equatorial_distance": p._equatorial_distance,
        "ecliptic_longitude": p._longitude,
        "amsha_longitude": p._amsha_longitude,
        "ecliptic_index": p._ecliptic_index,
        "amsha_index": p._amsha_index,
        "sign": p.sign(),
        "sign_name": p.sign_name(),
        "retrograde": p.retrograde(),
        "nakshatra": p._nakshatra,
    }


def probe_varga_planet(p) -> dict:
    """Amsha-relevant state only (in a varga the speeds/lat/dist are zeroed)."""
    return {
        "amsha_longitude": p._amsha_longitude,
        "amsha_index": p._amsha_index,
    }


def probe_cusp(c) -> dict:
    return {
        "number": c._number,
        "ecliptic_longitude": c._longitude,
        "amsha_longitude": c._amsha_longitude,
        "ecliptic_index": c._ecliptic_index,
        "amsha_index": c._amsha_index,
        "daily_speed": c.daily_speed,
        "sign": c.sign(),
        "sign_name": c.sign_name(),
        "nakshatra": c._nakshatra,
    }


def probe_rashi(rashi) -> dict:
    cusps = rashi.cusps()
    return {
        "planets": {p._id: probe_planet(p) for p in rashi.planets()},
        "cusps": [probe_cusp(c) for c in cusps],
        "ascmc": list(cusps.ascmc),
        "ascmc_speed": list(cusps.ascmcspeed),
        "armc": cusps.armc(),
        "lagna_sign": rashi.lagna().sign(),
    }


def probe_varga(chart, amsha: int) -> dict:
    varga = chart.varga(amsha)
    return {
        "amsha": varga.amsha(),
        "planets": {p._id: probe_varga_planet(p) for p in varga.planets()},
        "lagna_sign": varga.lagna().sign(),
    }


def probe_panchanga(rashi) -> dict:
    pan = rashi.panchanga()
    return {
        "tithi_number": pan._tithi_number,
        "tithi_elapsed": pan._tithi_elapsed,
        "tithi_remaining": pan._tithi_remaining,
        "tithi": pan.tithi(),
        "tithi_type": pan.tithi_type(),
        "karana_number": pan._karana_number,
        "karana_elapsed": pan._karana_elapsed,
        "karana_remaining": pan._karana_remaining,
        "karana_index": list(pan._karana_index),
        "karana": pan.karana(),
        "yoga_raw": pan._yoga_raw,
        "yoga_elapsed": pan._yoga_elapsed,
        "yoga_remaining": pan._yoga_remaining,
        "yoga_index": pan.yoga_index(),
        "yoga_name": pan.yoga_name(),
        "nakshatra": pan.nakshatra(),
        "vara": pan.vara(),
    }


def _vimshottari_period(period) -> dict:
    start, length, subs = period
    start_jd = start.jd if hasattr(start, "jd") else start
    return {
        "start_jd": start_jd,
        # raw period length as the library expresses it (years * yrlen, i.e. days)
        "length": length,
        "sub": [_vimshottari_period(s) for s in subs],
    }


def probe_vimshottari(rashi) -> dict:
    from libaditya.calc.vimshottari import calculate_vimshottari_dasha

    moon = rashi.planets().moon()
    result = calculate_vimshottari_dasha(planet=moon, dlevels=2)
    *periods, first_lord, age = result
    return {
        "first_lord": first_lord,
        "age": age,
        "periods": [_vimshottari_period(p) for p in periods],
    }


def _houses_for(chart, hsys: str) -> dict:
    cusps = chart._new_chart(hsys=hsys).rashi().cusps()
    return {
        "house_system": cusps.house_system(),
        "cusps": [c._longitude for c in cusps],
        "ascmc": list(cusps.ascmc),
        "armc": cusps.armc(),
    }


def probe_houses_by_system(chart) -> dict:
    return {h: capture(lambda h=h: _houses_for(chart, h)) for h in HOUSE_SYSTEMS}


# --------------------------------------------------------------------------- #
# snapshot assembly
# --------------------------------------------------------------------------- #
def build_snapshot(chart) -> dict:
    rashi = chart.rashi()
    jd = chart.context.timeJD
    snapshot = {
        "rashi": capture(lambda: probe_rashi(rashi)),
        "navamsa": capture(lambda: probe_varga(chart, 9)),
        "shashtyamsha": capture(lambda: probe_varga(chart, 60)),
        "panchanga": capture(lambda: probe_panchanga(rashi)),
        "vimshottari": capture(lambda: probe_vimshottari(rashi)),
        "ephemeris": capture(lambda: {"obliquity": jd.ecliptic_obliquity()}),
    }
    return snapshot


def build_meta(case: Case, chart) -> dict:
    return {
        "case": case.id,
        "subject": case.subject.id,
        "config": case.config,
        "config_kwargs": case.config_kwargs,
        "context": chart.context,
    }


def produce_record(case: Case) -> dict:
    """Build the full canonical record (meta + snapshot) for ``case``."""
    chart = build_chart(case)
    snapshot = build_snapshot(chart)
    for view in case.extra_views:
        if view == "houses_by_system":
            snapshot[view] = capture(lambda: probe_houses_by_system(chart))
        else:  # a case named a view the probe layer does not implement
            snapshot[view] = {"__error__": f"unknown view: {view}"}
    record = {
        "schema": SCHEMA_VERSION,
        "meta": build_meta(case, chart),
        "snapshot": snapshot,
    }
    return canonicalize(record, reducers=reducers())
