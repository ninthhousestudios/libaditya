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

# House-system letters swept for the high-latitude subject.  A wide, well-known
# spread: quadrant systems that degrade toward the poles (P, K, R, C, O) next to
# robust equal/whole variants (A, V, W) plus the space-division oddballs
# (X meridian, H horizon, T Polich-Page, B Alcabitius, M Morinus, G Gauquelin).
# Each is computed inside per-system error capture, so an engine that rejects a
# letter freezes that rejection rather than crashing the run.
HOUSE_SYSTEMS = [
    "P",
    "K",
    "O",
    "R",
    "C",
    "A",
    "V",
    "W",
    "X",
    "H",
    "T",
    "B",
    "M",
    "G",
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
    """One frozen computation: a subject rendered under one configuration."""

    id: str
    subject: Subject
    config: str  # Chart method: "aditya" | "tropical" | "sidereal"
    config_kwargs: dict = field(default_factory=dict)  # e.g. {"ayanamsa": 1}
    extra_views: tuple = ()  # e.g. ("houses_by_system",)


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
    """The ordered case matrix frozen by the harness."""
    s = SUBJECTS
    return [
        Case("nyc-aditya", s["nyc"], "aditya"),
        Case("nyc-tropical", s["nyc"], "tropical"),
        Case("nyc-sidereal-lahiri", s["nyc"], "sidereal", {"ayanamsa": 1}),
        Case("nyc-sidereal-truecitra", s["nyc"], "sidereal", {"ayanamsa": 27}),
        Case("sydney-aditya", s["sydney"], "aditya"),
        Case(
            "reykjavik-aditya",
            s["reykjavik"],
            "aditya",
            extra_views=("houses_by_system",),
        ),
        Case("equator-aditya", s["equator"], "aditya"),
        Case("equator-sidereal-lahiri", s["equator"], "sidereal", {"ayanamsa": 1}),
        Case("yamakoti-aditya", s["yamakoti"], "aditya"),
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
    return configure(**case.config_kwargs)
