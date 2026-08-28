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

"""Pinned test subjects and the case matrix.

Everything here is a fixed constant: birth data is given as an explicit
``(year, month, day, decimal_hour_UTC)`` tuple and never ``.now()`` or the
library default clock, so a case computes the same numbers forever.  Longitudes
are East-positive (swisseph convention): New York is ``-74.006``.

The subjects deliberately span the coordinate/era edges a backend swap is most
likely to diverge on:

* ``nyc``       -- mid-latitude northern, modern era.
* ``sydney``    -- southern hemisphere, older era (1935).
* ``reykjavik`` -- high latitude, where house systems strain (swept over the
                   full ``HOUSE_SYSTEMS`` set via the ``houses_by_system`` view).
* ``equator``   -- 0 degN / 0 degE ("Null Island"), the savana-day / equatorial edge.
* ``yamakoti``  -- the library's *default* location, at a pinned time, so the
                   zero-argument default code path is itself frozen.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# House-system letters swept per the GM-2 decision: the FULL Swiss-Ephemeris
# house-system set, not just the letters libaditya drives through its API.  This
# is cheap insurance that catches ``house_name``/``house_pos`` gaps across every
# ``hsys`` blanket-wide -- the casing of the frozen ``house_name`` strings is the
# workaround GM-2 exists to lock.  The set is the whole uppercase ``A``..``Y``
# range that ``swe.house_name`` names, plus lowercase ``i`` (Sunshine / alt.),
# the one letter whose calculation genuinely differs from its uppercase form.
# Each system is computed inside per-system error capture, so an engine that
# rejects a letter freezes that rejection rather than crashing the run.
HOUSE_SYSTEMS = [
    "A",  # equal
    "B",  # Alcabitius
    "C",  # Campanus
    "D",  # equal (MC)
    "E",  # equal
    "F",  # Carter poli-equ.
    "G",  # Gauquelin sectors
    "H",  # horizon/azimut
    "I",  # Sunshine
    "J",  # Savard-A
    "K",  # Koch
    "L",  # Pullen SD
    "M",  # Morinus
    "N",  # equal / 1=Aries
    "O",  # Porphyry
    "P",  # Placidus
    "Q",  # Pullen SR
    "R",  # Regiomontanus
    "S",  # Sripati
    "T",  # Polich/Page
    "U",  # Krusinski-Pisa-Goelzer
    "V",  # equal/Vehlow
    "W",  # equal / whole sign
    "X",  # axial rotation / Meridian
    "Y",  # APC houses
    "i",  # Sunshine / alt. (distinct from uppercase 'I')
]

# Vargas frozen for every case.  The positive parivritti D-series saptavargas
# (D1 = rashi is already fully covered by the ``rashi`` view, so it is omitted
# here) plus the full set of special negative-amsha "deity" vargas enumerated in
# ``Chart.varga()``'s docstring.  A varga projection depends on the underlying
# rashi longitudes and the circle, so it is legitimate per-config coverage.
VARGA_AMSHAS = [
    # positive parivritti D-series
    2,
    3,
    7,
    9,
    12,
    30,
    60,
    # special negative-amsha (deity) vargas
    -2,
    -3,
    -4,
    -10,
    -12,
    -16,
    -20,
    -24,
    -27,
    -40,
    -45,
    -60,
    -100,
    -240,
]


@dataclass(frozen=True)
class Subject:
    """A pinned birth datum + location."""

    id: str
    jd: tuple  # (year, month, day, decimal_hour_UTC) -> swe.julday
    utcoffset: float  # display only; the jd above is already UTC
    timezone: str
    lat: float
    long: float  # East-positive
    alt: float
    placename: str
    use_default_location: bool = False  # True -> Location() (Yamakoti) code path


@dataclass(frozen=True)
class Case:
    """One frozen computation: a subject rendered under one configuration.

    ``config`` names the ``Chart`` builder method invoked with ``config_kwargs``
    (``aditya`` / ``tropical`` / ``sidereal`` / ``heliocentric`` / ``barycentric``
    / ``draconic``).  ``context_overrides`` is applied *after* that method via
    ``Chart._new_chart(**overrides)``, for knobs the builders set themselves and
    so cannot take as a keyword without a duplicate-argument clash -- the raw
    ``sysflg`` (equatorial ``const.EQU``, topocentric ``const.TOPO`` /
    ``const.SID | const.TOPO``) and the ``circle`` (an Aditya chart forced onto
    ``Circle.ZODIAC``).
    """

    id: str
    subject: Subject
    config: str  # Chart method: "aditya" | "tropical" | "sidereal" | ...
    config_kwargs: dict = field(default_factory=dict)  # e.g. {"ayanamsa": 1}
    context_overrides: dict = field(default_factory=dict)  # applied via _new_chart
    extra_views: tuple = ()  # e.g. ("houses_by_system", "ayanamsa_sweep")


SUBJECTS = {
    "nyc": Subject(
        id="nyc",
        jd=(1990, 2, 13, 22.5),
        utcoffset=-5.0,
        timezone="America/New_York",
        lat=40.7128,
        long=-74.0060,
        alt=10.0,
        placename="New York",
    ),
    "sydney": Subject(
        id="sydney",
        jd=(1935, 6, 21, 4.0),
        utcoffset=10.0,
        timezone="Australia/Sydney",
        lat=-33.8688,
        long=151.2093,
        alt=58.0,
        placename="Sydney",
    ),
    "reykjavik": Subject(
        id="reykjavik",
        jd=(1975, 12, 1, 9.0),
        utcoffset=0.0,
        timezone="Atlantic/Reykjavik",
        lat=64.1466,
        long=-21.9426,
        alt=40.0,
        placename="Reykjavik",
    ),
    "equator": Subject(
        id="equator",
        jd=(2000, 1, 1, 12.0),
        utcoffset=0.0,
        timezone="UTC",
        lat=0.0,
        long=0.0,
        alt=0.0,
        placename="Null Island",
    ),
    "yamakoti": Subject(
        id="yamakoti",
        jd=(2024, 3, 20, 6.1),
        utcoffset=12.0,
        timezone="UTC+12",
        lat=0.0,
        long=165.76666666666668,
        alt=0.0,
        placename="Yamakoti",
        use_default_location=True,
    ),
}


def cases() -> list[Case]:
    """The ordered case matrix frozen by the harness.

    Constants (``const.*`` sysflag values, the ``Circle`` enum) are imported
    lazily here rather than at module top: the harness selects the ephemeris
    backend *before* it first imports ``libaditya``, and ``cases()`` only ever
    runs after that (it is reached through ``harness``).
    """
    from libaditya import constants as const
    from libaditya.objects import Circle

    s = SUBJECTS
    return [
        # --- nyc: the full zodiac/system sweep on one modern mid-latitude subject
        Case(
            "nyc-aditya",
            s["nyc"],
            "aditya",
            extra_views=("houses_by_system", "vedic_derived"),
        ),
        Case(
            "nyc-aditya-zodiac",
            s["nyc"],
            "aditya",
            context_overrides={"circle": Circle.ZODIAC},
        ),
        Case("nyc-tropical", s["nyc"], "tropical"),
        Case("nyc-heliocentric", s["nyc"], "heliocentric"),
        Case("nyc-barycentric", s["nyc"], "barycentric"),
        Case("nyc-draconic", s["nyc"], "draconic"),
        Case(
            "nyc-equatorial",
            s["nyc"],
            "aditya",
            context_overrides={"sysflg": const.EQU},
        ),
        Case(
            "nyc-topocentric",  # tropical topocentric (FLG_TOPOCTR alone; TROP == 0)
            s["nyc"],
            "tropical",
            context_overrides={"sysflg": const.TOPO},
        ),
        # representative ayanamsa set: 1 Lahiri, 3 Raman, 5 Krishnamurti,
        # 27 True Citra (sidereal() default), 36 GAL_CENT_MULA_WILHELM (the code
        # aditya's 98 internally maps signs to), 97 true-sidereal, 98 aditya-default.
        Case(
            "nyc-sidereal-lahiri",
            s["nyc"],
            "sidereal",
            {"ayanamsa": 1},
            extra_views=("vedic_derived",),
        ),
        Case("nyc-sidereal-raman", s["nyc"], "sidereal", {"ayanamsa": 3}),
        Case("nyc-sidereal-krishnamurti", s["nyc"], "sidereal", {"ayanamsa": 5}),
        Case("nyc-sidereal-truecitra", s["nyc"], "sidereal", {"ayanamsa": 27}),
        Case("nyc-sidereal-galcentmula", s["nyc"], "sidereal", {"ayanamsa": 36}),
        Case("nyc-sidereal-truesidereal", s["nyc"], "sidereal", {"ayanamsa": 97}),
        Case("nyc-sidereal-adityadefault", s["nyc"], "sidereal", {"ayanamsa": 98}),
        # --- other subjects: spread the remaining coordinate/era edges.
        # Every subject carries the "vedic_derived" view under BOTH aditya-default
        # and sidereal-Lahiri (the GM-3 subset), so the panchanga/vimshottari/
        # jaimini/avastha/yoga layer is frozen against two ayanamsas per geometry.
        Case("sydney-aditya", s["sydney"], "aditya", extra_views=("vedic_derived",)),
        Case(
            "sydney-sidereal-lahiri",
            s["sydney"],
            "sidereal",
            {"ayanamsa": 1},
            extra_views=("vedic_derived",),
        ),
        Case(
            "sydney-topocentric-sidereal",  # the SID | TOPO topocentric branch
            s["sydney"],
            "sidereal",
            {"ayanamsa": 1},
            context_overrides={"sysflg": const.SID | const.TOPO},
        ),
        Case(
            "reykjavik-aditya",
            s["reykjavik"],
            "aditya",
            extra_views=("houses_by_system", "vedic_derived"),
        ),
        Case(
            "reykjavik-sidereal-lahiri",
            s["reykjavik"],
            "sidereal",
            {"ayanamsa": 1},
            extra_views=("vedic_derived",),
        ),
        Case(
            "equator-aditya",
            s["equator"],
            "aditya",
            # J2000 epoch: freeze the full get_ayanamsa() code sweep here.
            extra_views=("ayanamsa_sweep", "vedic_derived"),
        ),
        Case(
            "equator-sidereal-lahiri",
            s["equator"],
            "sidereal",
            {"ayanamsa": 1},
            extra_views=("vedic_derived",),
        ),
        Case(
            "yamakoti-aditya", s["yamakoti"], "aditya", extra_views=("vedic_derived",)
        ),
        Case(
            "yamakoti-sidereal-lahiri",
            s["yamakoti"],
            "sidereal",
            {"ayanamsa": 1},
            extra_views=("vedic_derived",),
        ),
    ]


def build_chart(case: Case):
    """Construct the configured Chart for ``case`` (imports libaditya lazily)."""
    from libaditya import Chart, EphContext, JulianDay, Location

    s = case.subject
    jd = JulianDay(s.jd, utcoffset=s.utcoffset, timezone=s.timezone)
    if s.use_default_location:
        location = Location()
    else:
        location = Location(
            lat=s.lat,
            long=s.long,
            alt=s.alt,
            placename=s.placename,
            utcoffset=s.utcoffset,
            icao=None,
        )
    base = Chart(EphContext(name=s.id, timeJD=jd, location=location))
    configure = getattr(base, case.config)
    chart = configure(**case.config_kwargs)
    if case.context_overrides:
        chart = chart._new_chart(**case.context_overrides)
    return chart
