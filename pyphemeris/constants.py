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

import utils

# defaults
pyph_path = os.path.dirname(os.path.realpath(__file__))
edir = pyph_path + "/ephe/"
utcoffset = -5
timezone = "EST"
ayanamsa = 101  # new code for dhruva equatorial
show_helios = 0
show_baryos = 0
show_topo = 0
show_adityas = 1
show_equ = 0
show_topo = 0
show_vdasha = 0
show_v2dasha = 0
dasha_levels = 1
# N and E are positive
lat = round(utils.dms2dec((39, 57, 22)), 3)
long = -round(utils.dms2dec((86, 0, 46)),3)
alt = 0  # swe requires meters
placename = ""
hsys = "C"
show_houses = 1
lang = "eng"
signs = []
sign_long = 1  # default to printing longitudes as "degrees Sign", e.g., 10.3 Capricorn
sign_func = utils.yessignize
dict_path = pyph_path + "/dict/"
eng = dict_path + "dict.eng"
iast = dict_path + "dict.iast"
deva = dict_path + "dict.deva"
mixed = dict_path + "dict.mixed"
lang_file = mixed
flground = 1  # 1 to round, 0 to not round, ndigs is how much to round to
ndigs = 3
round_func = utils.yesround  # like with the signs, the function used to round constant constants for program functions
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
    swe.set_sid_mode(ayanamsa)
    return swe.get_ayanamsa_name(ayanamsa)

# constant constants

pnames = {swe.SUN: "Sun",
          swe.MOON: "Moon",
          swe.MERCURY: "Mercury",
          swe.VENUS: "Venus",
          swe.MARS: "Mars",
          swe.JUPITER: "Jupiter",
          swe.SATURN: "Saturn",
          swe.URANUS: "Uranus",
          swe.NEPTUNE: "Neptune",
          swe.PLUTO: "Pluto",
          swe.EARTH: "Earth",
          swe.TRUE_NODE: "Rahu"}

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
