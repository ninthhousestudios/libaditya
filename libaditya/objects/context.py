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

from dataclasses import dataclass
from enum import Enum

from .julian_day import JulianDay
from .location import Location
from libaditya import constants as const
from libaditya.hd import constants as hdc


class Circle(Enum):
    ADITYA = 1
    ZODIAC = 2


@dataclass
class EphContext:
    """
    this is the base configuration device
    this includes chart information, calculation options and display options

    every object in libaditya has default values, so you can instantiate anything by, e.g.:
    >>> e = EphContext()
    >>> c = Chart()
    >>> c
    ...

    here is the definition direct from libaditya/objects/context.py:

    # basic chart information
    name: str = ""
    timeJD: JulianDay = JulianDay()
    location: Location = Location()

    # calculation options

    sysflg: int = const.ECL # | swe.SWEIPH there is supposed to be an option about which ephemeris to use; not sure where it is here
    amsha: int = 1 # amsha is the varga; default is 1
    ayanamsa: int = 98
    hsys: str = "C"
    circle: Circle = Circle.ADITYA
    rashi_temporary_friendships: bool = True # other option is to base temporary friendships on the varga under consideration
    rashi_aspects: str = "quadrant" # options are "quadrant", "element", "conventional"

    # display options
    names_type: str = "mixed" # mixed, eng, iast, deva; possible to create your own
    sign_names: str = "adityas" # other option is zodiac
    signize: bool = True
    toround: (bool, int) = (True, 3)
    print_nakshatras: bool = True
    print_outer_planets: bool = True

    # hd options
    # i dont acutally know if hd_gate_one works to change the gate
    # Chart.bodygraph().draw_svg() can draw a bodygraph, not sure if hd_print_hexagrams works?
    hd_gate_one: float = hdc.gate_one
    hd_print_hexagrams: bool = False

    # cot options
    # ew teaches that the card changes at the time of sunrise on the equator
    # i.e., at sunrise on the equator, the savana day changes for the whole 180 degrees of line of longitude
    # if cot_savana_day is False, will use calendar days, so card changes at midnight local
    cot_savana_day: bool = True # False option not yet implemented
    cot_planet_order: str = "vedic" # other option is "solar_system"

    """
    # basic chart information
    name: str = ""
    timeJD: JulianDay = JulianDay()
    location: Location = Location()

    # calculation options

    sysflg: int = const.ECL # | swe.SWEIPH there is supposed to be an option about which ephemeris to use; not sure where it is here
    amsha: int = 1 # amsha is the varga; default is 1
    ayanamsa: int = 98
    hsys: str = "C"
    circle: Circle = Circle.ADITYA
    rashi_temporary_friendships: bool = True # other option is to base temporary friendships on the varga under consideration
    rashi_aspects: str = "quadrant" # options are "quadrant", "element", "conventional"

    # display options
    names_type: str = "mixed" # mixed, eng, iast, deva; possible to create your own
    sign_names: str = "adityas" # other option is zodiac
    signize: bool = True
    toround: (bool, int) = (True, 3)
    print_nakshatras: bool = True
    print_outer_planets: bool = True

    # hd options
    # i dont acutally know if hd_gate_one works to change the gate
    # Chart.bodygraph().draw_svg() can draw a bodygraph, not sure if hd_print_hexagrams works?
    hd_gate_one: float = hdc.gate_one
    hd_print_hexagrams: bool = False

    # cot options
    # ew teaches that the card changes at the time of sunrise on the equator
    # i.e., at sunrise on the equator, the savana day changes for the whole 180 degrees of line of longitude
    # if cot_savana_day is False, will use calendar days, so card changes at midnight local
    cot_savana_day: bool = True # False option not yet implemented
    cot_planet_order: str = "vedic" # other option is "solar_system"

    # this is mostly used for pyhd
    # need to change the xx business
    def get_info_str_hd(self):
        istr=""
        istr+=self.name+"\n"
        # for __str__ of JulianDay
        istr+=f"{self.timeJD}"
        # 223.25 is what hd_gate_one "should" be; if not, print what it is to show that it is not what is expected
        if self.hd_gate_one != 223.25:
            istr+="\ngate 1 = {self.hd_gate_one}"
        if self.ayanamsa:
            istr+=f"\n{self.ayanamsa}"
        return istr


