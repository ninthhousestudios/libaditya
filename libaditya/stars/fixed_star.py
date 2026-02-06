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
from libaditya import utils

from libaditya.objects import Longitude, CelestialObject, EphContext

from libaditya.stars.stellarium import Stellarium


class FixedStar(Longitude,CelestialObject):

    def __init__(self, swe_id: str, context: EphContext = EphContext(), rc: Stellarium = None):
        self.context = context
        self.system = self.context.sysflg
        self.sysflg = self.system | swe.FLG_SPEED
        self._other_names = ""
        # swe_id is the nomenclature name of the star
        # can pass it with or without comma
        self._stellarium = False
        if "st:" in swe_id:
            # swe_id = "st:Omi Tau"
            # or "st: HIP 19500"
            # indicates this is a stellarium star
            self._swe_id = swe_id.split(":")[1].strip()
            self._stellarium = True
            # called "rc", but is not a stellarium.remote_control.RemoteControl object
            # it is a Stellarium object initialized by someone else to get this information
            # initialized by the TheStars()
            self.rc = rc
            # now initialize all of the information
            self.init_Stellarium()
            super().__init__(self.long,1,context)
            # done with this __init__
            return
        self._swe_id = self.correct_nomen_name(swe_id)
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
        self.dist_ly = 0 # convert self.dist in AUs to LYs
        self._name, self.returned_swe_id = self._name.split(",")
        (self._right_ascension, self._declination, self._equatorial_distance,_,_,_) = swe.fixstar2_ut(self.swe_id(),self.context.timeJD.jd_number(),swe.FLG_EQUATORIAL)[0]
        if "%" in self._swe_id:
            self._swe_id = self.returned_swe_id
        # now that we know which star this is, make sure it has the right swe_id()
        super().__init__(self.long,1,context)

    def init_coords(self):
        loc = self.context.location.swe_location()
        # the if statements are returnless statements that initialize swe
        # sysflg is definited in __init__; it is self.system + swe.FLG_SPEED
        # so that we always get the speed
        if self.system == const.SID:
            # will need to add custom ayanamsas here
            if self.ayanamsa() == 98:
                self._ayanamsa = 36
            if self.ayanamsa() == 97:
                utils.set_swe_true_sidereal_ayanamsa()
        if self.system == const.TOPO:
            swe.set_topo(loc[0], loc[1], loc[2])
        if self.system == (const.SID | const.TOPO):
            swe.set_sid_mode(self.ayanamsa())
            swe.set_topo(loc[0], loc[1], loc[2])
        return swe.fixstar2_ut(self.swe_id(), self.context.timeJD.jd_number(), self.sysflg if self.sysflg >= 0 else 0)

    def correct_nomen_name(self, swe_id):
        # take care of cases like ,And14
        # the proper nomen name is ,14And
        if "," in swe_id:
            # remove initial comma if there
            swe_id = swe_id.split(",")[1]
        if swe_id[-3:].isnumeric():
            return ","+swe_id[-3:]+swe_id[:-3]
        if swe_id[-2:].isnumeric():
            if swe_id[-2:] == "00":
                # for GCRS00
                return ","+swe_id
            return ","+swe_id[-2:]+swe_id[:-2]
        if swe_id[-1:].isnumeric():
            return ","+swe_id[-1:]+swe_id[:-1]
        return ","+swe_id

    def __eq__(self, fs2):
        """
        are these the same kind of object?
        they could both be Aldebaran but 4000 years apart; they would still be == with this function
        """
        return self.swe_id() == fs2.swe_id()

    def other_names(self):
        return self._other_names

    # longitude is taken care of by inheritor, Longitude

    def name(self):
        return self._name

    def stellarium(self):
        return self._stellarium

    def swe_id(self):
        return self._swe_id

    def identity(self):
        return self.swe_id()
        
    def magnitude(self):
        return swe.fixstar2_mag(self.swe_id())[0]

    def init_Stellarium(self):
        """
        self.swe_id() should be a valid stellarium object, probably HIP

        need to deal with sidereal in here, so we only get the ecliptic longitude
        """
        try:
            self.rc.change_context(self.context)
            info = self.rc.info(self.swe_id())        
        except:
            print("Stellarium not available...")
            return
        self.long = info["elong"]
        self.lat = info["elat"]
        try:
            self.dist = info["distance-ly"]
        except:
            self.dist = 0
        self.dist_ly = self.dist
        self.long_speed = self.lat_speed = self.dist_speed = 0
        self._name = info["name"]
        self._right_ascension = info["ra"] 
        self._declination = info["dec"]
        self._equatorial_distance = self.dist
        self._altitude = info["altitude"]
        self._azimuth = info["azimuth"]
        # these will be in local time, so think about time switching?
        # make FixedStar.rise() which will catch Stellarium stars, if not, send them to CelestialObject.rise()
        self._rise = info["rise"]
        self._set = info["set"]
        self._info = info
        return

    def info(self):
        return self._info
