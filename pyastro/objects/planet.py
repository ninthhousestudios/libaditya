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

from pyastro import constants as const
from pyastro import utils

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
        self.context = context
        self.pnumber = pnumber
        self.planet_name = context.planet_names[self.pnumber]
        self.jd = self.timeJD.jd
        self.ayanamsa = context.ayanamsa
        self.system = context.sysflg
        self.sysflg = self.system | swe.FLG_SPEED
        self.sysflgstr = const.sysflgstr(context.sysflg)
        self.long, self.lat, self.dist, self.long_speed, self.lat_speed, self.dist_speed = self.init_coords()

    def __str__(self):
        ayanamsa = ""
        if self.system == swe.FLG_SIDEREAL:
            ayanamsa = f" with {const.ayanamsa_name(self.ayanamsa)} ayanamsa"
        return f"{self.planet_name}{self.retrostr()} at {self.longitude()} degrees {self.system_name()} longitude{ayanamsa}\n" + super().__str__()

    def table_row(self):
        return [self.name()+self.retrostr()] + [self.longitude()] + [self.longitude_speed()] + [self.latitude()] + [self.latitude_speed()] + [self.distance()] + [self.distance_speed()] 

    def init_coords(self):
        loc = self.context.location.swe_location()
        if self.system == const.SID:
            # will need to add custom ayanamsas here
            if self.ayanamsa == 98:
                self.ayanamsa = 36
            swe.set_sid_mode(self.ayanamsa)
        if self.system == const.TOPO:
            swe.set_topo(loc[0],loc[1],loc[2])
        if self.system == (const.SID | const.TOPO):
            swe.set_sid_mode(self.ayanamsa)
            swe.set_topo(loc[0],loc[1],loc[2])
        return swe.calc_ut(self.jd,self.pnumber,self.sysflg)[0]

    def name(self):
        return self.planet_name

    def system_name(self):
        return self.sysflgstr

    def longitude(self):
        if self.context.signize:
            return utils.signize(self.long,self.context.toround,self.context.sign_names)
        else:
            return self.long

    def latitude(self):
        if self.context.toround[0]:
            return round(self.lat,self.context.toround[1])
        else:
            return self.lat
    
    def distance(self):
        if self.context.toround[0]:
            return round(self.dist,self.context.toround[1])
        else:
            return self.dist
    
    def longitude_speed(self):
        if self.context.toround[0]:
            return round(self.long_speed,self.context.toround[1])
        else:
            return self.long_speed

    def latitude_speed(self):
        if self.context.toround[0]:
            return round(self.lat_speed,self.context.toround[1])
        else:
            return self.lat_speed

    def distance_speed(self):
        if self.context.toround[0]:
            return round(self.dist_speed,self.context.toround[1])
        else:
            return self.dist_speed

    def ayanamsa(self):
        return self.ayanamsa

    def retrograde(self):
        if self.longitude_speed() < 0:
            return True
        else:
            return False

    def retrostr(self):
        if self.retrograde():
            return " (R)"
        else:
            return ""

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
                location.swe_location(),
            )[1][0]
        )

class Sun(Planet):

    def __init__(self, context):
        super().__init__(swe.SUN, context)

    def sunrise_yamakoti(self):
        return self.riseset(swe.CALC_RISE, Yamakoti)


class Moon(Planet):

    def __init__(self, context):
        super().__init__(swe.MOON, context)


class Mars(Planet):

    def __init__(self, context):
        super().__init__(swe.MARS, context)


class Mercury(Planet):

    def __init__(self, context):
        super().__init__(swe.MERCURY, context)

class Venus(Planet):

    def __init__(self, context):
        super().__init__(swe.VENUS, context)


class Jupiter(Planet):

    def __init__(self, context):
        super().__init__(swe.JUPITER, context)


class Saturn(Planet):

    def __init__(self, context):
        super().__init__(swe.SATURN, context)


class Rahu(Planet):

    def __init__(self, context):
        super().__init__(swe.TRUE_NODE, context)
        self.planet_name = context.planet_names[10]

class Ketu(Planet):

    def __init__(self, context):
        super().__init__(swe.TRUE_NODE, context)

    def longitude(self):
        self.long = (self.long-180)%360
        if self.context.signize:
            return utils.signize(self.long,self.context.toround,self.context.sign_names)
        else:
            return self.long

class Uranus(Planet):

    def __init__(self, context):
        super().__init__(swe.URANUS, context)

class Neptune(Planet):

    def __init__(self, context):
        super().__init__(swe.NEPTUNE, context)

class Pluto(Planet):

    def __init__(self, context):
        super().__init__(swe.PLUTO, context)

class Earth(Planet):

    def __init__(self, context):
        super().__init__(swe.EARTH, context)

class Chiron(Planet):

    def __init__(self, context):
        self.planet_name = "Chiron"
        super().__init__(swe.CHIRON, context)
