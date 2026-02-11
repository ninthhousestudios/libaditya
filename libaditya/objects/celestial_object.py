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
from dataclasses import replace

from libaditya import utils

from libaditya.objects import JulianDay
from libaditya.hd.longitude import HDLongitude

class CelestialObject:
    """
    this inherits unto Planet and FixedStar
    but this is a Mixin

    has all the functions that these share, and that they dont share with Cusp
    all three inherit from Longitude, but only Planet and FixedStar from CelestialObject
    """

    def set_attribute(self,attrs):
        """
        attrs is a tuple ("attribute",value)
        add all of these to self.attributes
        attritube is a string that will be a dictionary key for value
        """
        key,value=attrs
        self.attributes[key] = value
    
    def hd(self):
        """
        each Planet and FixedStar has its own HDLongitude
        """
        return HDLongitude(self.ecliptic_longitude(),context=self.context)

    def constellation(self):
        """
        as in, the actual sky
        constellations according to "true sidereal", 13 sign astrology
        """
        if "constellation" not in self.attributes.keys():
            return "n/a"
        return self.attributes["constellation"]

    def __repr__(self):
        ret = f"{self.name()} {self.ecliptic_longitude()} {self.amsha()} {self.amsha_longitude()} {self.ayanamsa()}"
        return ret

    def latitude(self) -> float:
        if self.context.toround[0]:
            return round(self.lat, self.context.toround[1])
        else:
            return self.lat

    def right_ascension(self) -> float:
        """
        add declination so that is is always retrivable
        """
        if self.context.toround[0]:
            return round(self._right_ascension, self.context.toround[1])
        else:
            return self._right_ascension

    def ra(self) -> str:
        """
        return self.right_ascension() as hours,minutes,seconds
        """
        d,m,s = utils.dec2dms(self.right_ascension())
        return f"{int(d/15):02d}h{int(m):02d}m{int(s):02d}s"

    def declination(self) -> float:
        """
        add declination so that is is always retrivable
        """
        if self.context.toround[0]:
            return round(self._declination, self.context.toround[1])
        else:
            return self._declination

    def dec(self) -> str:
        """
        return self.declination() as degrees,minutes,seconds
        """
        d,m,s = utils.dec2dms(self.declination())
        return f"{int(d):02d}d{int(m):02d}m{int(s):02d}s"

    def equatorial_distance(self):
        """
        add equatorial_distance so that is is always retrivable
        """
        if self.context.toround[0]:
            return round(self._equatorial_distance, self.context.toround[1])
        else:
            return self._equatorial_distance

    def distance(self):
        if self.context.toround[0]:
            return round(self.dist, self.context.toround[1])
        else:
            return self.dist

    def speed(self):
        return self.longitude_speed()

    def longitude_speed(self):
        if self.context.toround[0]:
            return round(self.long_speed, self.context.toround[1])
        else:
            return self.long_speed

    def latitude_speed(self):
        if self.context.toround[0]:
            return round(self.lat_speed, self.context.toround[1])
        else:
            return self.lat_speed

    def distance_speed(self):
        if self.context.toround[0]:
            return round(self.dist_speed, self.context.toround[1])
        else:
            return self.dist_speed

    # SWE FUNCTIONS
    # that apply to planets and fixed stars; it uses Object.swe_id(), so the proper thing it gotten
    
    def rise_trans(self, bitflags=swe.BIT_HINDU_RISING,location=None) -> JulianDay:
        if location:
            self.context = replace(self.context,location=location)
        timeJD = JulianDay(
            swe.rise_trans(
                self.context.timeJD.jd_number(),  # midnightjd() if (rs == swe.CALC_RISE) else self.jd,
                self.swe_id(),
                bitflags,
                self.context.location.swe_location(),
            )[1][0],self.context.timeJD.utcoffset)
        return timeJD

    def rise(self, bitflags=swe.BIT_HINDU_RISING, location=None) -> JulianDay:
        """
        next rising time for this planet (can do stars...need to add something for that)
        """
        # an object instantied by using Stellarium. it will have this information from that
        if utils.is_stellarium_id(self.swe_id()):
            return self._rise
        return self.rise_trans(bitflags=bitflags|swe.CALC_RISE,location=location)

    def set(self, bitflags=swe.BIT_HINDU_RISING, location=None) -> JulianDay:
        """
        next setting time for this planet (can do stars...need to add something for that)
        """
        if utils.is_stellarium_id(self.swe_id()):
            return self._set
        return self.rise_trans(bitflags=bitflags|swe.CALC_SET,location=location)

    def next_heliacal_event(self, atmosphere,observer,event=None):
        """
        swe.heliacal_ut() returns 3 jd numbers
        start of visbility, optimum visbility, end of visbility

        there are options in this function to factor in place based considerations
        and observer considerations; here these are all set to some default as a general indication
        of when the event will occur
        """
        if self.identity() == "Moon":
            # Moon doesnt have these
            return
        return utils.toJD(swe.heliacal_ut(
            self.context.timeJD.jd_number(),
            self.context.location.swe_location(),
            # need to figure out how to get current information for the place
            # relative humdity can do with metpy, but it is a lot of dependcies for just one thing that
            # may not really be that important
            # the 4-tuple of 0 sets atmospheric information to general values
            atmosphere,
            # a 6-tuple of values relative to an observer and various observing situations
            observer,
            self.identity(),
            event,
            # this is the ephemeris flag, i think
            self.sysflg
       ), self.context)

    def next_heliacal_rising(self, atmosphere=(0,0,0,0),observer=(0,0,0,0,0,0)):
        return self.next_heliacal_event(atmosphere,observer,event=swe.HELIACAL_RISING)

    def next_heliacal_setting(self, atmosphere=(0,0,0,0),observer=(0,0,0,0,0,0)):
        return self.next_heliacal_event(atmosphere,observer,event=swe.HELIACAL_SETTING)

    def altitude(self):
        return self._altitude

    def azimuth(self):
        return self._azimuth
