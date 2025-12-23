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

"""
a variety of functions to return string forms of various information
that can be computed with libaditya
"""

from libaditya import constants as const


def dignity_table(dignities):
    """
    takes a list of dignites from Planets.dignities and output a string form
    """
    ret = ""
    for n in range(0,len(dignities)):
        ret += f"{const.karaka_glyphs[n]} :  {dignities[n]}\n"
    # slice removes last \n
    return ret[:-1]
