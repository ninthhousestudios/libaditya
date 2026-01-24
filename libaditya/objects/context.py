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
    SIDEREAL_ADITYA = ZODIAC

@dataclass(frozen=True)
class HDContext:
    gate_one: float = hdc.gate_one
    print_hexagrams: int = 0 # 0 for numbers, 1 for hexagrams
    toround: (bool, int) = (True, 3)
        

@dataclass
class EphContext:
    """
    this is the base configuration device
    this includes chart information, calculation options and display options
    """
    # basic chart information
    timeJD: JulianDay = JulianDay()
    location: Location = Location()

    # calculation options
    sysflg: int = const.ECL
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
    hd_gate_one: float = hdc.gate_one
    hd_print_hexagrams: bool = False


# originally i passed the names around to every function and every object

#@dataclass(frozen=True)
#class Names:
#    planet_names: str = tuple(const.planet_names)
#    sign_names: str = tuple(const.adityas)
#    nakshatras: str = tuple(const.nakshatras)
#    tithis: str =  tuple(const.tithis)
#    karanas: str = tuple(const.karanas)
#    varas: str = tuple(const.varas)
#    yogas: str = tuple(const.yogas)
#    adityas: str = tuple(const.adityas)
#    zodiac: str = tuple(const.zodiac)
