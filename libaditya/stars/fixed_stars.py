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

import swisseph as swe

from libaditya import constants as const

from libaditya.objects import Longitude, CelestialObject, EphContext

class FixedStar(Longitude,CelestialObject):

    def __init__(self, swe_id: str, context: EphContext = EphContext()):
        self.context = context
        self.system = self.context.sysflg
        self.sysflg = self.system | swe.FLG_SPEED
        # swe_id is the nomenclature name of the star
        # can pass it with or without comma
        self._swe_id = swe_id if "," in swe_id else ","+swe_id
        try:
            # if it works, the swe_id is valid
            swe.fixstar2_ut(self._swe_id,self.context.timeJD.jd_number())
        except:
            # if not, assume it is a search
            # so remove "," from beginning, add "%" to end for wildcard
            self._swe_id = self._swe_id[1:]+"%"
        # self._coords is a 6-tuple
        # will be unpacked into FixedStar.longitude(), etc., for each value in the tuple
        (self.long, self.lat, self.dist, self.long_speed, self.lat_speed, self.dist_speed), self._name, _ = self.init_coords()
        self._name, self._swe_id = self._name.split(",")
        (self._right_ascension, self._declination, _,_,_,_) = swe.fixstar2_ut(self.swe_id(),self.context.timeJD.jd_number(),swe.FLG_EQUATORIAL)[0]
        # now that we know which star this is, make sure it has the right swe_id()
        super().__init__(self.long,1)

    def init_coords(self):
        loc = self.context.location.swe_location()
        if self.system == const.SID:
            # will need to add custom ayanamsas here
            if self.ayanamsa() == 98:
                self._ayanamsa = 36
            swe.set_sid_mode(self.ayanamsa())
        if self.system == const.TOPO:
            swe.set_topo(loc[0], loc[1], loc[2])
        if self.system == (const.SID | const.TOPO):
            swe.set_sid_mode(self.ayanamsa())
            swe.set_topo(loc[0], loc[1], loc[2])
        return swe.fixstar2_ut(self._swe_id, self.context.timeJD.jd_number(), self.sysflg if self.sysflg >= 0 else 0)

    def __eq__(self, fs2):
        return self.swe_id() == fs2.swe_id()

    # longitude is taken care of by inheritor, Longitude

    def name(self):
        return self._name

    def swe_id(self):
        return ","+self._swe_id

    def identity(self):
        return self.swe_id()
        
    def magnitude(self):
        return swe.fixstar2_mag(self.swe_id())[0]

