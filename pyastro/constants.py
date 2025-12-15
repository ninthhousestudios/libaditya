#    This file is part of pyphemeris.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
#
#    pyphemeris is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyphemeris is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with pyphemeris.  If not, see <https://www.gnu.org/licenses/>.

import swisseph as swe

import os

from pyastro import utils

ECL = swe.FLG_TROPICAL
EQU = swe.FLG_EQUATORIAL
HELIO = swe.FLG_HELCTR
BARY = swe.FLG_BARYCTR
SID = swe.FLG_SIDEREAL
sysflg = ECL  # default

def sysflgstr(sflg,ayanamsa=0):
    if sflg == swe.FLG_TROPICAL:
        return "degrees ecliptic longitude"
    if sflg == swe.FLG_EQUATORIAL:
        return "degrees equatorial longitude"
    if sflg == swe.FLG_HELCTR:
        return "degrees heliocentric longitude"
    if sflg == swe.FLG_BARYCTR:
        return "degrees barycentric longitude"
    if sflg == swe.FLG_SIDEREAL:
        return f"degrees sidereal longitude with {ayanamsa_name(ayanamsa)} ayanamsa"

def ayanamsa_name(ayanamsa):
    if ayanamsa == 0:
        return "Tropical"
    if ayanamsa == 98:
        return "Dhruva GC mid-Mula Equatorial"
    if ayanamsa == 99:
        return "Eclitpic Vedanga Jyotisha"
    if ayanamsa == 100:
        return "Equatorial Vedanga Jyotisha"
    swe.set_sid_mode(ayanamsa)
    return swe.get_ayanamsa_name(ayanamsa)

# constant constants


dasha_years = [("saura",365.2422),("nakshatra",359.0167),("savana",360),("sidereal",365.2564),("chandra",364.2888),("lunar",354.36708)]

nak = 13+(1/3)
true_node = 11
rahu = 11
ketu = 10
earth = 12
calendardays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

signglyph = ["♈︎", "♉︎", "♊︎", "♋︎", "♌︎", "♍︎", "♎︎", "♏︎", "♐︎", "♑︎", "♒︎", "♓︎"]


planet_names = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Rahu", "Ketu", [], [], "Earth","Chiron"]
