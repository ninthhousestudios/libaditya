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

import os
import pathlib

from libaditya import utils

# defaults
base_path = os.path.dirname(pathlib.Path(__file__).parent)
pyph_path = base_path + "/libaditya"
edir = pyph_path + "/ephe/"
dict_path = pyph_path + "/dict/"

default_mode = "epehemeris"

utcoffset = -5.0
timezone = "EST"
lat = round(utils.dms2dec((39, 57, 22)), 3)
long = -round(utils.dms2dec((86, 0, 46)), 3)
alt = 252  # swe requires meters
placename = "Default Place"

ayanamsa = 98  # dhruva equatorial

epehemeris_mode = False
chart_mode = True

eng = dict_path + "dict.eng"
iast = dict_path + "dict.iast"
deva = dict_path + "dict.deva"
mixed = dict_path + "dict.mixed"
abrev = dict_path + "dict.abrev"
lang_file = abrev

#epehemeris_mode = {
#    "zodiac": False,
#    "adityas": True,
#    "helios": False,
#    "baryos": False,
#    "topo": False,
#    "equatorial": False,
#    "sidereal": False,
#    "vimshottari dasha": False,
#    "current vimshottari dasha": True,
#    "house system": "C",
#    "language file": abrev,
#    "signize": True,
#    "toround": [True,3],
#    "complete planet info": False # if True, it prints all six values returned by swiss eph; nakshatras printed separately
#}                                 # if False, longitude, speed and latitude are printed in one table with nakshatras

#chart_mode = {
#    "zodiac": False,
#    "adityas": True,
#    "sidereal": False,
#    "vimshottari dasha": False,
#    "current vimshottari dasha": True,
#    "house system": "C",
#    "language file": abrev,
#    "signize": True,
#    "toround": [True,3]
#}

show_helios = 0
show_baryos = 0
show_topo = 0
show_adityas = 1
show_equ = 0
show_topo = 0
show_drac = 0
show_sidereal = 0
show_vdasha = 0
show_v2dasha = 0
dasha_levels = 1
signs = "adityas"  # adityas, or zodiac
print_nakshatras = True
print_outer_planets = True
# N and E are positive
hsys = "C"
show_houses = 1
lang = "eng"
signs = []
signize = 1  # default to printing longitudes as "degrees Sign", e.g., 10.3 Capricorn
toround = [True, 3]  # whether to round longitudes, and if so, to how many decimals

