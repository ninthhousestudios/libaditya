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
from .location import Location, Yamakoti


class Planet(JulianDay):
    """
    this class has information and functions related to planets
    each Planet takes a planet number and a JulianDay class
    """

    def __init__(self, pnumber, context):
        self.timeJD = context.timeJD
        super().__init__(self.timeJD.jd)
        self.pnumber = pnumber
        self.planet_name = const.pnames[self.pnumber]
        self.jd = self.timeJD.jd
        self.ayanamsa = context.ayanamsa
        self.sysflg = context.sysflg
        self.sysflgstr = const.sysflgstr(self.sysflg,self.ayanamsa)
        self.long, self.lat, self.dist, self.long_speed, self.lat_speed, self.dist_speed = self.init_coords()

    def __str__(self):
        return f"{self.planet_name} at {self.longitude()} {self.sysflgstr}\n" + super().__str__()

    def init_coords(self):
        if self.ayanamsa != 0:
            # will need to add custom ayanamsas here
            swe.set_sid_mode(self.ayanamsa)
        return swe.calc_ut(self.jd,self.pnumber,self.sysflg)[0]

    def longitude(self):
        return self.long

    def latitude(self):
        return self.lat
    
    def distance(self):
        return self.dist
    
    def longitude_speed(self):
        return self.long_speed

    def latitude_speed(self):
        return self.lat_speed

    def distance_speed(self):
        return self.dist_speed

    def ayanamsa(self):
        return self.ayanamsa

    def riseset(self, rs, location=Location()):
        """
        :rs flag for rise, set, or one of the two meridian transits
        swe.CALC_RISE, swe.CALC_SET, swe.MTRANSIT, swe.ITRANSIT
        :location a Location class for where this is for
        """
        return timeJD(
            swe.rise_trans(
                self.timeJD.midnightjd() if (rs == swe.CALC_RISE) else self.jd,
                self.pnumber,
                rs | swe.BIT_HINDU_RISING,
                location.risetrans_location(),
            )[1][0]
        )

class Sun(Planet):

    def __init__(self, context):
        super().__init__(swe.SUN, context)
        self.planet_name = "Sun"

    def sunrise_yamakoti(self):
        return self.riseset(swe.CALC_RISE, Yamakoti)

class Ketu(Planet):

    def __init__(self, context):
        super().__init__(swe.TRUE_NODE, context)
        self.planet_name = "Ketu"

    def longitude(self):
        return (self.long-180)%360

class Moon(Planet):

    def __init__(self, context):
        super().__init__(swe.MOON, context)
        self.planet_name = "Moon"


class Mars(Planet):

    def __init__(self, context):
        super().__init__(swe.MARS, context)
        self.planet_name = "Mars"


class Mercury(Planet):

    def __init__(self, context):
        super().__init__(swe.MERCURY, context)
        self.planet_name = "Mercury"

    def __str__(self):
        return f"{self.planet_name} at\n" + super().__str__()

class Venus(Planet):

    def __init__(self, context):
        super().__init__(swe.VENUS, context)
        self.planet_name = "Venus"


class Jupiter(Planet):

    def __init__(self, context):
        super().__init__(swe.JUPITER, context)
        self.planet_name = "Jupiter"


class Saturn(Planet):

    def __init__(self, context):
        super().__init__(swe.SATURN, context)
        self.planet_name = "Saturn"


class Rahu(Planet):

    def __init__(self, context):
        super().__init__(swe.TRUE_NODE, context)
        self.planet_name = "Rahu"

class Uranus(Planet):

    def __init__(self, context):
        super().__init__(swe.URANUS, context)
        self.planet_name = "Uranus"

class Neptune(Planet):

    def __init__(self, context):
        super().__init__(swe.NEPTUNE, context)
        self.planet_name = "Neptune"

class Pluto(Planet):

    def __init__(self, context):
        super().__init__(swe.PLUTO, context)
        self.planet_name = "Pluto"

class Earth(Planet):

    def __init__(self, context):
        super().__init__(swe.EARTH, context)
        self.planet_name = "Earth"
