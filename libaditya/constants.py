#    This file is part of libaditya.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
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

rashi_aspects = {
    "quadrant": {
        1: (2,5,8),
        2: (7,10,1),
        3: (6,9,12),
        4: (5,8,11),
        5: (10,1,4),
        6: (9,12,3),
        7: (8,11,2),
        8: (1,4,7),
        9: (12,3,6),
        10: (11,2,5),
        11: (4,7,10),
        12: (3,6,9)
    },

    "element": {
        1: (2,8,11),
        2: (7,4,1),
        3: (6,9,12),
        4: (5,2,11),
        5: (7,10,4),
        6: (9,12,3),
        7: (8,11,5),
        8: (1,10,7),
        9: (12,3,6),
        10: (11,2,8),
        11: (4,1,10),
        12: (3,6,9)
    },

    "conventional": {
        1: (5,8,11),
        2: (4,7,10),
        3: (6,9,12),
        4: (8,11,2),
        5: (7,10,1),
        6: (9,12,3),
        7: (11,2,5),
        8: (10,1,4),
        9: (12,3,6),
        10: (2,5,8),
        11: (1,4,7),
        12: (3,6,9)
    }
}

karaka_glyphs = ["⨀","☾","♂","☿","♃","♀","♄"]
grahas_glyphs = ["⨀","☾","♂","☿","♃","♀","♄","☊","☋"]

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

names = {
    "eng":
    {'planets': ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Rahu', 'Ketu', [], [], 'Earth', 'Chiron'], 'nakshatras': ['Ashvini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'P. Phalguni', 'U. Phalguni', 'Hasta', 'Chitra', 'Svati', 'Vishakha', 'Anuradha', 'Jyeshtha', 'Mula', 'P. Ashadha', 'U. Ashadha', 'Shravana', 'Danishtha', 'Shatabhisha', 'P. Bhadrapada', 'U. Bhadrapada', 'Revati'], 'tithis': ['nanda', 'bhadra', 'jaya', 'rikta', 'purna'], 'karanas': [['Kimtughna', 'Bava'], ['Balava', 'Kaulava'], ['Taitula', 'Garija'], ['Vanija', 'Vishti'], ['Bava', 'Balava'], ['Kaulava', 'Taitula'], ['Garija', 'Vanija'], ['Vishti', 'Bava'], ['Balava', 'Kaulava'], ['Taitula', 'Garija'], ['Vanija', 'Vishti'], ['Bava', 'Balava'], ['Kaulava', 'Taitula'], ['Garija', 'Vanija'], ['Vishti', 'Bava'], ['Balava', 'Kaulava'], ['Taitula', 'Garija'], ['Vanija', 'Vishti'], ['Bava', 'Balava'], ['Kaulava', 'Taitula'], ['Garija', 'Vanija'], ['Vishti', 'Bava'], ['Balava', 'Kaulava'], ['Taitula', 'Garija'], ['Vanija', 'Vishti'], ['Bava', 'Balava'], ['Kaulava', 'Taitula'], ['Garija', 'Vanija'], ['Vishti', 'Shakuni'], ['Chatushpada', 'Naga']], 'varas': ['Ravivara', 'Somavara', 'Mangalavara', 'Budhavara', 'Guruvara', 'Shukravara', 'Shanivara'], 'yogas': ['Vishkambha', 'Priti', 'Ayushman', 'Saubhagya', 'Shobana', 'Atiganda', 'Sukarma', 'Dhriti', 'Shoola', 'Ganda', 'Vriddhi', 'Dhruva', 'Vyaghata', 'Harshana', 'Vajra', 'Siddhi', 'Vyatipata', 'Variyan', 'Parigha', 'Shiva', 'Siddha', 'Sadhya', 'Shubha', 'Shukla', 'Brahma', 'Indra', 'Vaidhriti'], 'adityas': ['Dhata', 'Aryama', 'Mitra', 'Varuna', 'Indra', 'Vivasvan', 'Tvashta', 'Vishnu', 'Amshu', 'Bhaga', 'Pusha', 'Parjanya'], 'zodiac': ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']},
    "iast":
    {'planets': ['sūrya', 'candra', 'budha', 'śukra', 'maṅgala', 'guru', 'śani', 'brahmā', 'viṣṇu', 'śiva', 'rāhu', 'ketu', [], [], 'bhūmi', 'Chiron'], 'nakshatras': ['aśvinī', 'bharaṇī', 'kṛttikā', 'rohiṇī', 'mṛgaśīrṣa', 'ārdrā', 'punarvasu', 'puṣya', 'āśleṣā', 'maghā', 'pūrvā phalgunī', 'uttarā phalgunī', 'hasta', 'citrā', 'svāti', 'viśākhā', 'anurādhā', 'jyeṣṭhā', 'mūla', 'pūrvāṣāḍhā', 'uttarāṣāḍhā', 'śravaṇa', 'dhaniṣṭhā', 'śatabhiṣa', 'pūrvabhādrapadā', 'uttarabhādrapadā', 'revatī'], 'tithis': ['nanda', 'bhadra', 'jāya', 'ṛkta', 'pūrṇa'], 'karanas': [['kiṃtughna', 'bava'], ['balava', 'kaulava'], ['taitila', 'garija'], ['vaṇija', 'viṣṭi'], ['bava', 'balava'], ['kaulava', 'taitila'], ['garija', 'vaṇija'], ['viṣṭi', 'bava'], ['balava', 'kaulava'], ['taitila', 'garija'], ['vaṇija', 'viṣṭi'], ['bava', 'balava'], ['kaulava', 'taitila'], ['garija', 'vaṇija'], ['viṣṭi', 'bava'], ['balava', 'kaulava'], ['taitila', 'garija'], ['vaṇija', 'viṣṭi'], ['bava', 'balava'], ['kaulava', 'taitila'], ['garija', 'vaṇija'], ['viṣṭi', 'bava'], ['balava', 'kaulava'], ['taitila', 'garija'], ['vaṇija', 'viṣṭi'], ['bava', 'balava'], ['kaulava', 'taitila'], ['garija', 'vaṇija'], ['viṣṭi', 'śakuni'], ['catuṣpada', 'nāga']], 'varas': ['ravivāra', 'somavāra', 'maṅgalavāra', 'budhavāra', 'guruvāra', 'śukravāra', 'śanivāra'], 'yogas': ['viṣkambha', 'prīti', 'āyuṣmān', 'saubhāgya', 'śobhana', 'atigaṇḍa', 'sukarma', 'dhṛti', 'śula', 'gaṇḍa', 'vṛddhi', 'dhruva', 'vyāghāta', 'harṣaṇa', 'vajra', 'siddhi', 'vyātipata', 'varīyas', 'parighā', 'śiva', 'siddha', 'sādhya', 'śubha', 'śukla', 'brahmā', 'indra', 'vaidhṛti'], 'adityas': ['dhātā', 'aryamā', 'mitra', 'varuṇa', 'indra', 'vivasvān', 'tvaṣṭā', 'viṣṇu', 'aṃśu', 'bhaga', 'pūṣā', 'parjanya'], 'zodiac': ['meṣa', 'vṛṣabha', 'mithuna', 'karka', 'siṃha', 'kanyā', 'tulā', 'vṛścika', 'dhanus', 'nakra', 'kumbha', 'mīna']},
    "deva":
    {'planets': ['सूर्य', 'चन्द्र', 'बुध', 'शुक्र', 'मङ्गल', 'गुरु', 'शनि', 'ब्रह्मा', 'विष्णु', 'शिव', 'राहु', 'केतु', [], [], 'भूमि', 'Chiron'], 'nakshatras': ['अश्विनी', 'भरणी', 'कृत्तिका', 'रोहिणी', 'मृगशीर्ष', 'आर्द्रा', 'पुनर्वसु', 'पुष्य', 'आश्लेषा', 'मघा', 'पूर्वा फल्गुनी', 'उत्तरा फल्गुनी', 'हस्त', 'चित्रा', 'स्वाति', 'विशाखा', 'अनुराधा', 'ज्येष्ठा', 'मूल', 'पूर्वाषाढा', 'उत्तराषाढा', 'श्रवण', 'धनिष्ठा', 'शतभिष', 'पूर्वभाद्रपदा', 'उत्तरभाद्रपदा', 'रेवती'], 'tithis': ['नन्द', 'भद्र', 'जाय', 'ऋक्त', 'पूर्ण'], 'karanas': [['किंतुघ्न', 'बव'], ['बलव', 'कौलव'], ['तैतिल', 'गरिज'], ['वणिज', 'विष्टि'], ['बव', 'बलव'], ['कौलव', 'तैतिल'], ['गरिज', 'वणिज'], ['विष्टि', 'बव'], ['बलव', 'कौलव'], ['तैतिल', 'गरिज'], ['वणिज', 'विष्टि'], ['बव', 'बलव'], ['कौलव', 'तैतिल'], ['गरिज', 'वणिज'], ['विष्टि', 'बव'], ['बलव', 'कौलव'], ['तैतिल', 'गरिज'], ['वणिज', 'विष्टि'], ['बव', 'बलव'], ['कौलव', 'तैतिल'], ['गरिज', 'वणिज'], ['विष्टि', 'बव'], ['बलव', 'कौलव'], ['तैतिल', 'गरिज'], ['वणिज', 'विष्टि'], ['बव', 'बलव'], ['कौलव', 'तैतिल'], ['गरिज', 'वणिज'], ['विष्टि', 'शकुनि'], ['चतुष्पद', 'नाग']], 'varas': ['रविवार', 'सोमवार', 'मङ्गलवार', 'बुधवार', 'गुरुवार', 'शुक्रवार', 'शनिवार'], 'yogas': ['विष्कम्भ', 'प्रीति', 'आयुष्मान्', 'सौभाग्य', 'शोभन', 'अतिगण्ड', 'सुकर्म', 'धृति', 'शुल', 'गण्ड', 'वृद्धि', 'ध्रुव', 'व्याघात', 'हर्षण', 'वज्र', 'सिद्धि', 'व्यातिपत', 'वरीयस्', 'परिघा', 'शिव', 'सिद्ध', 'साध्य', 'शुभ', 'शुक्ल', 'ब्रह्मा', 'इन्द्र', 'वैधृति'], 'adityas': ['धाता', 'अर्यमा', 'मित्र', 'वरुण', 'इन्द्र', 'विवस्वान्', 'त्वष्टा', 'विष्णु', 'अंशु', 'भग', 'पूषा', 'पर्जन्य'], 'zodiac': ['मेष', 'वृषभ', 'मिथुन', 'कर्क', 'सिंह', 'कन्या', 'तुला', 'वृश्चिक', 'धनुस्', 'नक्र', 'कुम्भ', 'मीन']},
    "mixed":
    {'planets': ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Rahu', 'Ketu', [], [], 'Earth', 'Chiron'], 'nakshatras': ['aśvinī', 'bharaṇī', 'kṛttikā', 'rohiṇī', 'mṛgaśīrṣa', 'ārdrā', 'punarvasu', 'puṣya', 'āśleṣā', 'maghā', 'pūrvā phalgunī', 'uttarā phalgunī', 'hasta', 'citrā', 'svāti', 'viśākhā', 'anurādhā', 'jyeṣṭhā', 'mūla', 'pūrvāṣāḍhā', 'uttarāṣāḍhā', 'śravaṇa', 'dhaniṣṭhā', 'śatabhiṣa', 'pūrvabhādrapadā', 'uttarabhādrapadā', 'revatī'], 'tithis': ['nanda', 'bhadra', 'jāya', 'ṛkta', 'pūrṇa'], 'karanas': [['kiṃtughna', 'bava'], ['balava', 'kaulava'], ['taitila', 'garija'], ['vaṇija', 'viṣṭi'], ['bava', 'balava'], ['kaulava', 'taitila'], ['garija', 'vaṇija'], ['viṣṭi', 'bava'], ['balava', 'kaulava'], ['taitila', 'garija'], ['vaṇija', 'viṣṭi'], ['bava', 'balava'], ['kaulava', 'taitila'], ['garija', 'vaṇija'], ['viṣṭi', 'bava'], ['balava', 'kaulava'], ['taitila', 'garija'], ['vaṇija', 'viṣṭi'], ['bava', 'balava'], ['kaulava', 'taitila'], ['garija', 'vaṇija'], ['viṣṭi', 'bava'], ['balava', 'kaulava'], ['taitila', 'garija'], ['vaṇija', 'viṣṭi'], ['bava', 'balava'], ['kaulava', 'taitila'], ['garija', 'vaṇija'], ['viṣṭi', 'śakuni'], ['catuṣpada', 'nāga']], 'varas': ['ravivāra', 'somavāra', 'maṅgalavāra', 'budhavāra', 'guruvāra', 'śukravāra', 'śanivāra'], 'yogas': ['viṣkambha', 'prīti', 'āyuṣmān', 'saubhāgya', 'śobhana', 'atigaṇḍa', 'sukarma', 'dhṛti', 'śula', 'gaṇḍa', 'vṛddhi', 'dhruva', 'vyāghāta', 'harṣaṇa', 'vajra', 'siddhi', 'vyātipata', 'varīyas', 'parighā', 'śiva', 'siddha', 'sādhya', 'śubha', 'śukla', 'brahmā', 'indra', 'vaidhṛti'], 'adityas': ['dhātā', 'aryamā', 'mitra', 'varuṇa', 'indra', 'vivasvān', 'tvaṣṭā', 'viṣṇu', 'aṃśu', 'bhaga', 'pūṣā', 'parjanya'], 'zodiac': ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']},
    "abbrev":
    {'planets': ['Su', 'Mo', 'Me', 'Ve', 'Ma', 'Ju', 'Sa', 'Ur', 'Ne', 'Pl', 'Ra', 'Ke', [], [], 'Ea', 'Ch'], 'nakshatras': ['aśv', 'bha', 'kṛt', 'roh', 'mṛg', 'ārd', 'pun', 'puṣ', 'āśl', 'mag', 'pph', 'uph', 'has', 'cit', 'svā', 'viś', 'anu', 'jye', 'mūl', 'pāṣ', 'uāṣ', 'śra', 'dha', 'śat', 'pdā', 'udā', 'rev'], 'tithis': ['nan', 'bha', 'jāy', 'ṛkt', 'pūr'], 'karanas': [['kiṃ', 'bav'], ['bal', 'kau'], ['tai', 'gar'], ['vaṇ', 'viṣ'], ['bav', 'bal'], ['kau', 'tai'], ['gar', 'vaṇ'], ['viṣ', 'bav'], ['bal', 'kau'], ['tai', 'gar'], ['vaṇ', 'viṣ'], ['bav', 'bal'], ['kau', 'tai'], ['gar', 'vaṇ'], ['viṣ', 'bav'], ['bal', 'kau'], ['tai', 'gar'], ['vaṇ', 'viṣ'], ['bav', 'bal'], ['kau', 'tai'], ['gar', 'vaṇ'], ['viṣ', 'bav'], ['bal', 'kau'], ['tai', 'gar'], ['vaṇ', 'viṣ'], ['bav', 'bal'], ['kau', 'tai'], ['gar', 'vaṇ'], ['viṣ', 'śak'], ['cat', 'nāg']], 'varas': ['rav', 'som', 'maṅ', 'bud', 'gur', 'śuk', 'śan'], 'yogas': ['viṣ', 'prī', 'āyu', 'sau', 'śob', 'ati', 'suk', 'dhṛ', 'śul', 'gaṇ', 'vṛd', 'dhr', 'vyā', 'har', 'vaj', 'sid', 'vyā', 'var', 'par', 'śiv', 'sid', 'sād', 'śub', 'śuk', 'bra', 'ind', 'vai'], 'adityas': ['dhā', 'ary', 'mit', 'var', 'ind', 'viv', 'tva', 'viṣ', 'aṃś', 'bha', 'pūṣ', 'par'], 'zodiac': ['Ar', 'Ta', 'Ge', 'Ca', 'Le', 'Vi', 'Li', 'Sc', 'Sa', 'Ca', 'Aq', 'Pi']},
}

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

planet_names_abbreviated = [
    "Su",
    "Mo",
    "Me",
    "Ve",
    "Ma",
    "Ju",
    "Sa",
    "Ur",
    "Ne",
    "Pl",
    "Ra",
    "Ke",
    [],
    [],
    "Ea",
    "Ch",
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
zodiac_abbreviated = [
    "Ar",
    "Ta",
    "Ge",
    "Ca",
    "Le",
    "Vi",
    "Li",
    "Sc",
    "Sa",
    "Ca",
    "Aq",
    "Pi",
]

tithis = ["nanda", "bhadra", "jāya", "ṛkta", "pūrṇa"]

tithis_abbreviated = ["nan", "bha", "jāy", "ṛkt", "pūr"]

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

karanas_abbreviated = [
    ["kiṃ", "bav"],
    ["bal", "kau"],
    ["tai", "gar"],
    ["vaṇ", "viṣ"],
    ["bav", "bal"],
    ["kau", "tai"],
    ["gar", "vaṇ"],
    ["viṣ", "bav"],
    ["bal", "kau"],
    ["tai", "gar"],
    ["vaṇ", "viṣ"],
    ["bav", "bal"],
    ["kau", "tai"],
    ["gar", "vaṇ"],
    ["viṣ", "bav"],
    ["bal", "kau"],
    ["tai", "gar"],
    ["vaṇ", "viṣ"],
    ["bav", "bal"],
    ["kau", "tai"],
    ["gar", "vaṇ"],
    ["viṣ", "bav"],
    ["bal", "kau"],
    ["tai", "gar"],
    ["vaṇ", "viṣ"],
    ["bav", "bal"],
    ["kau", "tai"],
    ["gar", "vaṇ"],
    ["viṣ", "śak"],
    ["cat", "nāg"],
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

nakshatras_abbreviated = [
    "aśv",
    "bha",
    "kṛt",
    "roh",
    "mṛg",
    "ārd",
    "pun",
    "puṣ",
    "āśl",
    "mag",
    "pph",
    "uph",
    "has",
    "cit",
    "svā",
    "viś",
    "anu",
    "jye",
    "mūl",
    "pāṣ",
    "uāṣ",
    "śra",
    "dha",
    "śat",
    "pdā",
    "udā",
    "rev",
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

varas_abbreviated = [
    "rav",
    "som",
    "maṅ",
    "bud",
    "gur",
    "śuk",
    "śan",
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

yogas_abbreviated = [
    "viṣ",
    "prī",
    "āyu",
    "sau",
    "śob",
    "ati",
    "suk",
    "dhṛ",
    "śul",
    "gaṇ",
    "vṛd",
    "dhr",
    "vyā",
    "har",
    "vaj",
    "sid",
    "vyā",
    "var",
    "par",
    "śiv",
    "sid",
    "sād",
    "śub",
    "śuk",
    "bra",
    "ind",
    "vai",
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

adityas_abbreviated = [
    "dhā",
    "ary",
    "mit",
    "var",
    "ind",
    "viv",
    "tva",
    "viṣ",
    "aṃś",
    "bha",
    "pūṣ",
    "par",
]

sign_names = adityas
sign_names_abbreviated = adityas_abbreviated

abbreviated_names = planet_names_abbreviated,sign_names_abbreviated,nakshatras_abbreviated,tithis_abbreviated,karanas_abbreviated,varas_abbreviated,yogas_abbreviated



# template comment box

########################################################
#                                                      #
#                                                      #
#                                                      #
#                                                      #
#                                                      #
########################################################
