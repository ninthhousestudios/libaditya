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

    def __init__(self, pnumber, julianday=JulianDay(), sysflg=const.ECL, ayanamsa=0):
        super().__init__(julianday.jd)
        self.pnumber = pnumber
        self.planet_name = const.pnames[self.pnumber]
        self.julianday = julianday  # the JulianDay class of this planet
        self.jd = self.julianday.jd
        self.ayanamsa = ayanamsa
        self.sysflg = sysflg
        self.sysflgstr = const.sysflgstr(self.sysflg,self.ayanamsa)
        self.long, self.latitude, self.distance, self.longitude_speed, self.latitude_speed, self.distance_speed = self.init_coords()

    def __str__(self):
        return f"{self.planet_name} at {self.longitude()} {self.sysflgstr}\n" + super().__str__()

    def init_coords(self):
        if self.ayanamsa != 0:
            # will need to add custom ayanamsas here
            swe.set_sid_mode(self.ayanamsa)
        return swe.calc_ut(self.jd,self.pnumber,self.sysflg)[0]

    def longitude(self):
        return self.long

    def riseset(self, rs, location=Location()):
        """
        :rs flag for rise, set, or one of the two meridian transits
        swe.CALC_RISE, swe.CALC_SET, swe.MTRANSIT, swe.ITRANSIT
        :location a Location class for where this is for
        """
        return JulianDay(
            swe.rise_trans(
                self.julianday.midnightjd() if (rs == swe.CALC_RISE) else self.jd,
                self.pnumber,
                rs | swe.BIT_HINDU_RISING,
                location.risetrans_location(),
            )[1][0]
        )

class Sun(Planet):

    def __init__(self, julianday=JulianDay(), sysflg=const.ECL, ayanamsa=0):
        super().__init__(swe.SUN, julianday, sysflg, ayanamsa)
        self.planet_name = "Sun"

    def sunrise_yamakoti(self):
        return self.riseset(swe.CALC_RISE, Yamakoti)

class Ketu(Planet):

    def __init__(self, julianday=JulianDay(), sysflg=const.ECL, ayanamsa=0):
        super().__init__(swe.TRUE_NODE, julianday, sysflg, ayanamsa)
        self.planet_name = "Ketu"

    def longitude(self):
        return (self.long-180)%360

#class Moon(Planet):
#
#    def __init__(self, julianday=JulianDay()):
#        super().__init__(swe.MOON, julianday)
#        self.planet_name = "Moon"
#
#    def __str__(self):
#        return f"{self.planet_name} at\n" + super().__str__()
#
#class Mars(Planet):
#
#    def __init__(self, julianday=JulianDay()):
#        super().__init__(swe.MARS, julianday)
#        self.planet_name = "Mars"
#
#    def __str__(self):
#        return f"{self.planet_name} at\n" + super().__str__()
#
#class Mercury(Planet):
#
#    def __init__(self, julianday=JulianDay()):
#        super().__init__(swe.MERCURY, julianday)
#        self.planet_name = "Mercury"
#
#    def __str__(self):
#        return f"{self.planet_name} at\n" + super().__str__()
#
#class Venus(Planet):
#
#    def __init__(self, julianday=JulianDay()):
#        super().__init__(swe.VENUS, julianday)
#        self.planet_name = "Venus"
#
#    def __str__(self):
#        return f"{self.planet_name} at\n" + super().__str__()
#
#class Jupiter(Planet):
#
#    def __init__(self, julianday=JulianDay()):
#        super().__init__(swe.JUPITER, julianday)
#        self.planet_name = "Jupiter"
#
#    def __str__(self):
#        return f"{self.planet_name} at\n" + super().__str__()
#
#class Saturn(Planet):
#
#    def __init__(self, julianday=JulianDay()):
#        super().__init__(swe.SATURN, julianday)
#        self.planet_name = "Saturn"
#
#    def __str__(self):
#        return f"{self.planet_name} at\n" + super().__str__()
#
#class Rahu(Planet):
#
#    def __init__(self, julianday=JulianDay()):
#        super().__init__(swe.TRUE_NODE, julianday)
#        self.planet_name = "Rahu"
#
#    def __str__(self):
#        return f"{self.planet_name} at\n" + super().__str__()

