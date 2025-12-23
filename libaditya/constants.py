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

from libaditya import utils

base_path = os.path.dirname(os.path.realpath(__file__))

ECL = swe.FLG_TROPICAL
TROP = swe.FLG_TROPICAL
EQU = swe.FLG_EQUATORIAL
HELIO = swe.FLG_HELCTR
BARY = swe.FLG_BARYCTR
SID = swe.FLG_SIDEREAL
TOPO = swe.FLG_TOPOCTR
DRAC = -8


def sysflgstr(sflg):
    if sflg == swe.FLG_TROPICAL:
        return "Tropical"
    if sflg == swe.FLG_EQUATORIAL:
        return "Equatorial"
    if sflg == swe.FLG_HELCTR:
        return "Heliocentric"
    if sflg == swe.FLG_BARYCTR:
        return "Barycentric"
    if sflg == swe.FLG_SIDEREAL:
        return "Sidereal"
    if sflg == swe.FLG_TOPOCTR:
        return "Topocentric"
    if sflg == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
        return "Sidereal Topocentric"
    if sflg == DRAC:
        return "Draconic"


def ayanamsa_name(ayanamsa):
    if ayanamsa == -1:
        return "Tropical"
    if ayanamsa == 98:
        return "Dhruva GC mid-Mula Equatorial"
    if ayanamsa == 99:
        return "Eclitpic Vedanga Jyotisha"
    if ayanamsa == 100:
        return "Equatorial Vedanga Jyotisha"
    swe.set_sid_mode(ayanamsa)
    return swe.get_ayanamsa_name(ayanamsa)

def circle_name(circle) -> str:
    from libaditya.objects import Circle
    if circle == Circle.ADITYA:
        return "Aditya Circle"
    if circle == Circle.ZODIAC:
        return "Zodiac Circle"


# constant constants

lords = {
    1: "Mars",
    2: "Venus",
    3: "Mercury",
    4: "Moon",
    5: "Sun",
    6: "Mercury",
    7: "Venus",
    8: "Mars",
    9: "Jupiter",
    10: "Saturn",
    11: "Saturn",
    12: "Jupiter"
}


karaka_glyphs = ["⨀","☾","♂","☿","♃","♀","♄"]

glyphs = {
    "Sun": "⨀",
    "Moon": "☾",
    "ercury": "☿",
    "Venus": "♀",
    "Mars": "♂",
    "Jupiter": "♃",
    "Saturn": "♄",
    "Uranus": "⛢",
    "Neptune": "♆",
    "Pluto": "⯓",
    "Rahu": "☊",
    "Ketu": "☋",
    "Earth": "⨁"
}

vimshottari_dashas = [("Ketu",7),("Venus",20),("Sun",6),("Moon",10),("Mars",7),("Rahu",18),("Jupiter",16),("Saturn",19),("Mercury",17)]

dasha_years = [
    ("saura", 365.2422),
    ("nakshatra", 359.0167),
    ("savana", 360),
    ("sidereal", 365.2564),
    ("chandra", 364.2888),
    ("lunar", 354.36708),
]

nak = 13 + (1 / 3)
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


planet_names = [
    "Sun",
    "Moon",
    "Mercury",
    "Venus",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
    "Rahu",
    "Ketu",
    [],
    [],
    "Earth",
    "Chiron",
]

zodiac = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
]

tithis = ["nanda", "bhadra", "jāya", "ṛkta", "pūrṇa"]

karanas = [
    ["kiṃtughna", "bava"],
    ["balava", "kaulava"],
    ["taitila", "garija"],
    ["vaṇija", "viṣṭi"],
    ["bava", "balava"],
    ["kaulava", "taitila"],
    ["garija", "vaṇija"],
    ["viṣṭi", "bava"],
    ["balava", "kaulava"],
    ["taitila", "garija"],
    ["vaṇija", "viṣṭi"],
    ["bava", "balava"],
    ["kaulava", "taitila"],
    ["garija", "vaṇija"],
    ["viṣṭi", "bava"],
    ["balava", "kaulava"],
    ["taitila", "garija"],
    ["vaṇija", "viṣṭi"],
    ["bava", "balava"],
    ["kaulava", "taitila"],
    ["garija", "vaṇija"],
    ["viṣṭi", "bava"],
    ["balava", "kaulava"],
    ["taitila", "garija"],
    ["vaṇija", "viṣṭi"],
    ["bava", "balava"],
    ["kaulava", "taitila"],
    ["garija", "vaṇija"],
    ["viṣṭi", "śakuni"],
    ["catuṣpada", "nāga"],
]

nakshatras = [
    "aśvinī",
    "bharaṇī",
    "kṛttikā",
    "rohiṇī",
    "mṛgaśīrṣa",
    "ārdrā",
    "punarvasu",
    "puṣya",
    "āśleṣā",
    "maghā",
    "pūrvā phalgunī",
    "uttarā phalgunī",
    "hasta",
    "citrā",
    "svāti",
    "viśākhā",
    "anurādhā",
    "jyeṣṭhā",
    "mūla",
    "pūrvāṣāḍhā",
    "uttarāṣāḍhā",
    "śravaṇa",
    "dhaniṣṭhā",
    "śatabhiṣa",
    "pūrvabhādrapadā",
    "uttarabhādrapadā",
    "revatī",
]

varas = [
    "ravivāra",
    "somavāra",
    "maṅgalavāra",
    "budhavāra",
    "guruvāra",
    "śukravāra",
    "śanivāra",
]

yogas = [
    "viṣkambha",
    "prīti",
    "āyuṣmān",
    "saubhāgya",
    "śobhana",
    "atigaṇḍa",
    "sukarma",
    "dhṛti",
    "śula",
    "gaṇḍa",
    "vṛddhi",
    "dhruva",
    "vyāghāta",
    "harṣaṇa",
    "vajra",
    "siddhi",
    "vyātipata",
    "varīyas",
    "parighā",
    "śiva",
    "siddha",
    "sādhya",
    "śubha",
    "śukla",
    "brahmā",
    "indra",
    "vaidhṛti",
]

adityas = [
    "dhātā",
    "aryamā",
    "mitra",
    "varuṇa",
    "indra",
    "vivasvān",
    "tvaṣṭā",
    "viṣṇu",
    "aṃśu",
    "bhaga",
    "pūṣā",
    "parjanya",
]


# template comment box

########################################################
#                                                      #
#                                                      #
#                                                      #
#                                                      #
#                                                      #
########################################################
