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

from dataclasses import dataclass
from enum import Enum

from .julian_day import JulianDay
from .location import Location
from libaditya import constants as const

class Circle(Enum):
    ADITYA = 1
    ZODIAC = 2
    SIDEREAL_ADITYA = ZODIAC
        
@dataclass(frozen=True)
class Names:
    planet_names: str = tuple(const.planet_names)
    sign_names: str = tuple(const.adityas)
    nakshatras: str = tuple(const.nakshatras)
    tithis: str =  tuple(const.tithis)
    karanas: str = tuple(const.karanas)
    varas: str = tuple(const.varas)
    yogas: str = tuple(const.yogas)

@dataclass
class EphContext:
    timeJD: JulianDay = JulianDay()
    location: Location = Location()
    sysflg: int = const.ECL
    ayanamsa: int = 98
    hsys: str = "C"
    circle: Circle = Circle
    signize: bool = True
    toround: (bool, int) = (True, 3)
    print_nakshatras: bool = True
    print_outer_planets: bool = True
    names: Names = Names()

