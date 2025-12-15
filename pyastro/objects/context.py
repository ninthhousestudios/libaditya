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

from dataclasses import dataclass, field
from typing import ClassVar

from .julian_day import JulianDay
from pyastro import constants as const

@dataclass
class EphContext:
    timeJD: JulianDay = JulianDay()
    sysflg: int = const.ECL
    ayanamsa: int = 98
    planet_names: (str) = tuple(const.planet_names)
    signize: bool = True
    toround: (bool,int) = (True,3)
