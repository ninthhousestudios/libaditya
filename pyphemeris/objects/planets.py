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

import constants as const

from .julian_day import JulianDay
from .planet import *

class Planets(JulianDay):

    plist = [Sun,Moon,Mars,Mercury,Venus,Jupiter,Saturn,Rahu,Ketu,Uranus,Neptune,Pluto,Earth]

    def __init__(self, context):
        self.timeJD = context.timeJD  # the JulianDay class of this planet
        super().__init__(self.timeJD.jd)
        self.context = context
        self.jd = self.timeJD.jd
        self.ayanamsa = context.ayanamsa
        self.sysflg = context.sysflg
        self.sysflgstr = const.sysflgstr(self.sysflg,self.ayanamsa)
        self.planets = self.init_Planets()

    def __iter__(self):
        return iter(self.planets)

    def init_Planets(self):
        ret = []
        for p in self.plist:
            ret.append(p(self.context))
        return ret

