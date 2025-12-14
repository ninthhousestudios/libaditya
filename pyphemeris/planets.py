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

from .planet import *

class Planets(JulianDay):

    plist = [Sun,Moon,Mars,Mercury,Venus,Jupiter,Saturn,Rahu,Ketu,Uranus,Neptune,Pluto,Earth]

    def __init__(self, timeJD=JulianDay(), sysflg=const.ECL, ayanamsa=0):
        super().__init__(timeJD.jd)
        self.timeJD = timeJD  # the JulianDay class of this planet
        self.jd = self.timeJD.jd
        self.ayanamsa = ayanamsa
        self.sysflg = sysflg
        self.sysflgstr = const.sysflgstr(self.sysflg,self.ayanamsa)
        self.planets = self.init_Planets()

    def init_Planets(self):
        ret = []
        for p in plist:
            ret.append(p(timeJD))
        return ret

