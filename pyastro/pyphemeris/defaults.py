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

from pyastro import utils

# defaults
pyph_path = os.path.dirname(pathlib.Path(__file__).parent)
edir = pyph_path + "/ephe/"
dict_path = pyph_path + "/dict/"
utcoffset = -5.0
timezone = "EST"
ayanamsa = 98  # dhruva equatorial
show_helios = 0
show_baryos = 0
show_topo = 0
show_adityas = 1
show_equ = 0
show_topo = 0
show_vdasha = 0
show_v2dasha = 0
dasha_levels = 1
signs = "adityas" # adityas, or zodiac
# N and E are positive
lat = round(utils.dms2dec((39, 57, 22)), 3)
long = -round(utils.dms2dec((86, 0, 46)),3)
alt = 0  # swe requires meters
placename = ""
hsys = "C"
show_houses = 1
lang = "eng"
signs = []
signize = 1  # default to printing longitudes as "degrees Sign", e.g., 10.3 Capricorn
toround = [True,3] # whether to round longitudes, and if so, to how many decimals
eng = dict_path + "dict.eng"
iast = dict_path + "dict.iast"
deva = dict_path + "dict.deva"
mixed = dict_path + "dict.mixed"
lang_file = mixed
flground = 1  # 1 to round, 0 to not round, ndigs is how much to round to
ndigs = 3
