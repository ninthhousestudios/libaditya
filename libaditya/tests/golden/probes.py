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
from .subjects import HOUSE_SYSTEMS, VARGA_AMSHAS, Case, build_chart

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


def _nak_pada(nak) -> int:
    """Quarter (1..4) of the nakshatra the body falls in.

    Derived from the raw ``ash_long`` rather than a display accessor (the library
    exposes no ``pada`` method); ``index()`` already carries the 27- vs 28-fold
    (ayanamsa 101) modulus, so ``within`` is the in-nakshatra arc in ``[0, size)``.
    """
    size = nak.naksize()
    within = nak.ash_long - nak.index() * size
    return int(within / (size / 4)) + 1


def reduce_nakshatra(nak, recurse):
    return recurse(
        {
            "name": nak.identity(),
            "index": nak.index(),
            "pada": _nak_pada(nak),
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
        # rise/set via swe.rise_trans (BIT_HINDU_RISING). Each returns a
        # JulianDay -> reduce_julianday freezes both the boundary jd and its
        # revjul calendar tuple. Reference time is the subject's pinned timeJD,
        # so these are reproducible; per-event capture freezes a rejection (e.g.
        # a high-latitude no-rise day) as a visible __error__ leaf.
        "sunrise": capture(pan.sunrise),
        "sunset": capture(pan.sunset),
        "moonrise": capture(pan.moonrise),
        "moonset": capture(pan.moonset),
    }


def _vimshottari_period(period) -> dict:
    start, length, subs = period
    # ``start`` is a JulianDay produced by JulianDay.shift (julday/revjul round
    # trips); passing it whole lets reduce_julianday freeze BOTH the boundary jd
    # and its revjul calendar tuple, which is the julday<->revjul path GM-3 is
    # meant to pin. A bare float (defensive, shouldn't occur) is wrapped alike.
    return {
        "start": start if hasattr(start, "jd") else {"jd": start},
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


# --------------------------------------------------------------------------- #
# derived Vedic views (GM-3): jaimini, avasthas, rashi yogas
#
# These compound the underlying sidereal positions, so they are sensitive
# regression detectors -- small positional drift changes karaka order, a sign's
# strength rank, an avastha state, or whether a yoga fires.  They are only
# astrologically meaningful on a Vedic chart, so subjects.cases() attaches the
# "vedic_derived" extra view to the aditya-default and sidereal-Lahiri cases
# only, not the tropical/heliocentric/etc. sweep.
# --------------------------------------------------------------------------- #
def probe_jaimini(rashi) -> dict:
    """Chara karakas, arudha padas, and the two ranked/classified strengths.

    Signs are frozen by their number (1..12) and karakas/planets by identity, so
    the record is a stable categorical projection: order IS the datum (karakas
    run AK..DK strongest-first, first_strength strongest-first).
    """
    karakas = [p.identity() for p in rashi.planets().jaimini_karakas()]
    return {
        "chara_karakas": karakas,  # ordered AK, AmK, ... DK (7 karakas)
        "atmakaraka": karakas[0],
        "darakaraka": karakas[-1],
        "arudha_lagna": rashi.pada().sign(),  # AL: pada of the lagna
        "upapada_lagna": rashi.upapada().sign(),  # UL: pada of the 12th
        "arudha_padas": {
            str(sign.sign()): pada.sign() for sign, pada in rashi.padas().items()
        },
        # jaimini_first_strength: all 12 signs strongest->weakest (8 tiebreakers)
        "first_strength": [s.sign() for s in rashi.jaimini_first_strength()],
        # jaimini_third_strength: {sign: (value, Kendra/Panapara/Apoklima)}
        "third_strength": {
            str(sign.sign()): list(cls)
            for sign, cls in rashi.jaimini_third_strength().items()
        },
    }


def probe_avasthas(rashi) -> dict:
    """All 5 Parashara avastha systems, read from the Rashi's precomputed dicts.

    Each is keyed by karaka name; Baladi/Jagradadi/Deeptadi/Shayanadi map to a
    single state string, Lajjitaadi to a dict of avastha -> contributing factors
    (source/planet/strength ...), whose strengths carry full-precision aspect
    values.  Shayanadi additionally depends on a rise_trans sunrise, so it
    doubles as a rise/set regression detector.
    """
    return {
        "lajjitaadi": rashi._lajjitaadi_avasthas,
        "baladi": rashi._baladi_avasthas,
        "jagradadi": rashi._jagradadi_avasthas,
        "deeptadi": rashi._deeptadi_avasthas,
        "shayanadi": rashi._shayanadi_avasthas,
    }


def probe_yogas(rashi) -> dict:
    """Nabhasa (+ akriti), Panchamahapurusha, Solar and Lunar yogas.

    Each method returns a list of dataclasses which canonicalize serialises by
    field; freezing the whole list (name, category, to_move / present, planets)
    captures both which yogas fire and every yoga's to_move distance metric.
    """
    return {
        "nabhasa": rashi.nabhasa_yogas(),
        "panchamahapurusha": rashi.panchamahapurusha_yogas(),
        "solar": rashi.solar_yogas(),
        "lunar": rashi.lunar_yogas(),
    }


def probe_vedic_derived(chart) -> dict:
    rashi = chart.rashi()
    return {
        "jaimini": capture(lambda: probe_jaimini(rashi)),
        "avasthas": capture(lambda: probe_avasthas(rashi)),
        "yogas": capture(lambda: probe_yogas(rashi)),
    }


def _houses_for(chart, hsys: str) -> dict:
    rashi = chart._new_chart(hsys=hsys).rashi()
    cusps = rashi.cusps()
    return {
        # house_system() returns swe.house_name(hsys) -- freezing it per system
        # locks the casing workaround GM-2 exists to guard.
        "house_system": cusps.house_system(),
        "cusps": [c._longitude for c in cusps],
        "ascmc": list(cusps.ascmc),
        "armc": cusps.armc(),
        # house_pos of every body under this system (swe.house_pos wrapper);
        # per-body capture so an engine that rejects one body freezes only that.
        "house_pos": {
            p.identity(): capture(lambda p=p: rashi.house_position(p.identity()))
            for p in rashi.planets()
        },
    }


def probe_houses_by_system(chart) -> dict:
    return {h: capture(lambda h=h: _houses_for(chart, h)) for h in HOUSE_SYSTEMS}


# Swiss-Ephemeris sidereal-mode codes 0..46 are the named ayanamsas (47 is the
# empty boundary, frozen to document it); the harness sweeps them at one pinned
# epoch to catch int -> SiderealMode mapping drift across the whole table.  The
# library's own custom codes (97 true-sidereal, 98 aditya-default, 99/100/101
# Vedanga variants) are swept through const.ayanamsa_name, which resolves them
# without touching swe.set_sid_mode.
AYANAMSA_SWE_CODES = list(range(0, 48))
AYANAMSA_LIB_CODES = [97, 98, 99, 100, 101]


def _ayanamsa_swe_entry(jd: float, code: int) -> dict:
    import swisseph as swe

    from libaditya import constants as const

    swe.set_sid_mode(code)
    return {
        "swe_value": swe.get_ayanamsa_ut(jd),
        "swe_name": swe.get_ayanamsa_name(code),
        "lib_name": const.ayanamsa_name(code),
    }


def _ayanamsa_lib_entry(code: int) -> dict:
    from libaditya import constants as const

    # 97..101 are libaditya-internal codes with no swe.set_sid_mode; only the
    # library's int -> name resolution is exercised here.
    return {"lib_name": const.ayanamsa_name(code)}


def probe_ayanamsa_sweep(chart) -> dict:
    """Freeze get_ayanamsa() across the full sidereal-mode table at one epoch."""
    jd = chart.context.timeJD.jd_number()
    swe_codes = {
        str(code): capture(lambda code=code: _ayanamsa_swe_entry(jd, code))
        for code in AYANAMSA_SWE_CODES
    }
    lib_codes = {
        str(code): capture(lambda code=code: _ayanamsa_lib_entry(code))
        for code in AYANAMSA_LIB_CODES
    }
    return {"epoch_jd": jd, "swe_modes": swe_codes, "lib_modes": lib_codes}


# --------------------------------------------------------------------------- #
# event / search views (GM-4): fixed stars, eclipses, rise/trans, heliacal,
# mooncross.
#
# These are the iterative-search surface -- the highest-risk part of the
# pyswisseph -> swisseph_rs migration, because the Rust port changes both their
# RETURN TYPES and their FAILURE behaviour (crossings raise NoConvergence).
# Every search here is seeded from the case's PINNED reference time/location, so
# a fixture is reproducible forever, and every call is wrapped in ``capture`` so
# a rejection (a high-latitude no-event day, an engine that refuses a body) is
# frozen as a visible ``__error__`` leaf that trips the diff like any other
# value rather than crashing the run.
#
# Where libaditya's own wrapper is lossy -- ``next_crossing_of_rahu`` formats a
# string, ``rise_trans`` discards the swe retflag -- the probe drops to the raw
# ``swe`` call (as ``ayanamsa_sweep`` already does) to preserve full precision
# AND the retflag/return-shape, which is exactly the return-type surface the
# migration is most likely to move.  Where the wrapper preserves everything (the
# eclipse ``SWERashi`` methods return the raw swe tuple; ``FixedStar`` exposes
# every coordinate; ``next_evening_first`` returns whole JulianDays) the probe
# rides the library API.
# --------------------------------------------------------------------------- #
def probe_fixed_star(fs) -> dict:
    """Full raw state of one FixedStar (raw attrs, never a rounding accessor)."""
    return {
        "long": fs.long,
        "lat": fs.lat,
        "dist": fs.dist,
        "long_speed": fs.long_speed,
        "lat_speed": fs.lat_speed,
        "dist_speed": fs.dist_speed,
        "right_ascension": fs._right_ascension,
        "declination": fs._declination,
        "equatorial_distance": fs._equatorial_distance,
        "name": fs._name,
        "returned_swe_id": fs.returned_swe_id,
        "swe_id": fs.swe_id(),
        "retflags": fs._retflags,
        "magnitude": fs.magnitude(),
    }


def probe_fixed_stars(chart) -> dict:
    """Freeze the STAR_SAMPLE in two configs: the case's own frame and the SVP path.

    ``base`` uses the chart's own ``sysflg`` (the ordinary fixstar2_ut path).
    ``true_sidereal_svp`` forces ``sysflg=SID, ayanamsa=97`` so FixedStar takes
    the ``utils.set_swe_true_sidereal_ayanamsa`` (USER_UT SVP) branch -- the
    verified-but-fiddly config the HD/stars code relies on.  Per-star + per-config
    capture keeps a single unresolvable name from sinking the whole view.
    """
    from dataclasses import replace

    from libaditya import constants as const
    from libaditya.stars.fixed_star import FixedStar
    from .subjects import STAR_SAMPLE

    ctx = chart.context
    svp_ctx = replace(ctx, sysflg=const.SID, ayanamsa=97)
    configs = {"base": ctx, "true_sidereal_svp": svp_ctx}
    return {
        cfg: {
            star: capture(lambda star=star, c=c: probe_fixed_star(FixedStar(star, c)))
            for star in STAR_SAMPLE
        }
        for cfg, c in configs.items()
    }


def probe_eclipses(rashi) -> dict:
    """Next & previous solar (loc + glob) and lunar eclipse, raw swe tuples.

    The ``SWERashi`` wrappers return the swe result verbatim -- ``(retflag, tret)``
    for the glob/lunar searches and ``(retflag, tret, attr)`` for the local solar
    search -- so freezing them locks the eclipse instants, the whole tret contact
    array, the local-circumstance ``attr`` array AND the retflag (the failure /
    return-shape surface).  All six seed from the case's pinned ``timeJD``.
    """
    return {
        "next_solar_loc": capture(rashi.next_solar_eclipse_here),
        "prev_solar_loc": capture(rashi.previous_solar_eclipse_here),
        "next_solar_glob": capture(rashi.next_solar_eclipse),
        "prev_solar_glob": capture(rashi.previous_solar_eclipse),
        "next_lunar": capture(rashi.next_lunar_eclipse),
        "prev_lunar": capture(rashi.previous_lunar_eclipse),
    }


def probe_rise_trans(chart) -> dict:
    """Raw swe.rise_trans for Sun & Moon over rise / set / mtransit / itransit.

    Frozen from the raw call (not the library ``rise_trans``, which returns only a
    JulianDay) to also pin the retflag and the full tret contact array -- the
    return shape most at risk in the migration.  All four events carry
    ``BIT_HINDU_RISING`` (the library default).  swe demands a registered
    geographic position for the meridian transits, so ``set_topo`` is asserted to
    the case's own location first, making the transits deterministic regardless of
    prior global swe state; rise/set take the geopos from the call itself.
    """
    import swisseph as swe

    jd = chart.context.timeJD.jd_number()
    geopos = chart.context.location.swe_location()
    swe.set_topo(*geopos)
    events = {
        "rise": swe.CALC_RISE,
        "set": swe.CALC_SET,
        "mtransit": swe.CALC_MTRANSIT,
        "itransit": swe.CALC_ITRANSIT,
    }
    bodies = {"sun": 0, "moon": 1}

    def _one(pnum: int, flag: int) -> dict:
        retflag, tret = swe.rise_trans(jd, pnum, flag | swe.BIT_HINDU_RISING, geopos)
        return {"retflag": retflag, "tret": list(tret)}

    return {
        body: {
            name: capture(lambda p=pnum, f=flag: _one(p, f))
            for name, flag in events.items()
        }
        for body, pnum in bodies.items()
    }


def probe_heliacal(rashi) -> dict:
    """next_evening_first / next_morning_last for Moon, Mercury, Venus.

    Each library method returns a list of whole JulianDays (start / optimum / end
    of the heliacal window from swe.heliacal_ut with its 4-tuple atmosphere and
    6-tuple observer defaults), so reduce_julianday freezes every window jd and
    its revjul calendar tuple.  Per body+method capture freezes an engine that
    refuses a body / date.
    """
    planets = rashi.planets()
    bodies = {
        "moon": planets.moon(),
        "mercury": planets.mercury(),
        "venus": planets.venus(),
    }
    return {
        name: {
            "evening_first": capture(body.next_evening_first),
            "morning_last": capture(body.next_morning_last),
        }
        for name, body in bodies.items()
    }


def probe_mooncross(chart) -> dict:
    """Raw swe.mooncross_node_ut (next Moon/true-node conjunction) from pinned jd.

    Frozen raw rather than through ``Moon.next_crossing_of_rahu`` (which formats a
    lossy string) so the crossing instant keeps full precision.  In swisseph_rs
    this is one of the calls that raises NoConvergence -- capture would freeze
    that as an __error__ leaf, tripping the diff.
    """
    import swisseph as swe

    jd_cross, moon_longitude, moon_latitude = swe.mooncross_node_ut(
        chart.context.timeJD.jd_number()
    )
    return {
        "jd_cross": jd_cross,
        "moon_longitude": moon_longitude,
        "moon_latitude": moon_latitude,
    }


def probe_events(chart) -> dict:
    """Assemble the GM-4 event/search view for one case.

    Fixed stars run LAST: the SVP path mutates the global swe sidereal mode, and
    the other event calls (eclipses, rise/trans, heliacal, mooncross) are all
    frame-geometric and seed their own args, so keeping the star probe last means
    no sub-view can observe the SVP global-state mutation.
    """
    rashi = chart.rashi()
    return {
        "eclipses": capture(lambda: probe_eclipses(rashi)),
        "rise_trans": capture(lambda: probe_rise_trans(chart)),
        "heliacal": capture(lambda: probe_heliacal(rashi)),
        "mooncross": capture(lambda: probe_mooncross(chart)),
        "fixed_stars": capture(lambda: probe_fixed_stars(chart)),
    }


# --------------------------------------------------------------------------- #
# snapshot assembly
# --------------------------------------------------------------------------- #
def build_snapshot(chart) -> dict:
    rashi = chart.rashi()
    jd = chart.context.timeJD
    snapshot = {
        "rashi": capture(lambda: probe_rashi(rashi)),
        "vargas": {
            str(amsha): capture(lambda amsha=amsha: probe_varga(chart, amsha))
            for amsha in VARGA_AMSHAS
        },
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
        "context_overrides": case.context_overrides,
        "context": chart.context,
    }


def produce_record(case: Case) -> dict:
    """Build the full canonical record (meta + snapshot) for ``case``."""
    chart = build_chart(case)
    snapshot = build_snapshot(chart)
    for view in case.extra_views:
        if view == "houses_by_system":
            snapshot[view] = capture(lambda: probe_houses_by_system(chart))
        elif view == "ayanamsa_sweep":
            snapshot[view] = capture(lambda: probe_ayanamsa_sweep(chart))
        elif view == "vedic_derived":
            snapshot[view] = capture(lambda: probe_vedic_derived(chart))
        elif view == "events":
            snapshot[view] = capture(lambda: probe_events(chart))
        else:  # a case named a view the probe layer does not implement
            snapshot[view] = {"__error__": f"unknown view: {view}"}
    record = {
        "schema": SCHEMA_VERSION,
        "meta": build_meta(case, chart),
        "snapshot": snapshot,
    }
    return canonicalize(record, reducers=reducers())
