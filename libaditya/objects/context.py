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
    """
    timeJD: the JulianDay for this situation
    location: the Location for this situation
    sysflg: const.TROP = const.ECL; const.SID; const.HELIO; const.BARY; const.EQU; const.DRAC; const.TOPO
    ayanamsa: any swisseph ayanamsa, plug 98 for dhruva gc midmula equatorial, 99 ecliptic vedanga jyotisha, 100 equatorial vedanga jyotisha
    hsys: any swisseph letter for a house system; treats the cusps of the system as independent points
    circle:  Circle.ADITYA or Circle.ZODIAC or Circle.SIDEREAL_ADITYA, which will print as Circle.ZODIAC since it is equivalent, but
    with sidereal coordinates. Aditya sequence is as which Ernsts system. If you passed for names Names(sign_names=sidereal_adityas) with sidereal_adityas
    being a [str], list of strings of the names in the proper order starting from sign 1, then it might print correctly, if you want to experiement
    with a difference Aditya order
    signize:  True or False, print in_sign_longitude or ecliptic longitude
    toround: (True/False,n), round output to n digits
    print_nakshatras: True or False
    print_outer_planets: True or False
    rashi_temporary_friendships: bool; calculate temporary friendships for dignity in Rashi, True, or not
    names: Names()
    """
    timeJD: JulianDay = JulianDay()
    location: Location = Location()
    sysflg: int = const.ECL
    ayanamsa: int = 98
    hsys: str = "C"
    circle: Circle = Circle.ADITYA
    signize: bool = True
    toround: (bool, int) = (True, 3)
    print_nakshatras: bool = True
    print_outer_planets: bool = True
    rashi_temporary_friendships: bool = True # other option is "Varga"
    rashi_aspects: str = "quadrant" # options are "quadrant", "element", "conventional"
    names: Names = Names()

