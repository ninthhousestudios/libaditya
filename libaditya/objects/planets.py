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
from prettytable import PrettyTable
from dataclasses import replace
from typing import Self

from libaditya import constants as const
from libaditya.hd import HDLongitude

from .julian_day import JulianDay
from .location import Location, Yamakoti
from .context import EphContext
from .longitude import Longitude
from .cusps import Cusp
from .nakshatras import Nakshatra, Nakshatras


class Planet(Longitude):
    """
    this class has information and functions related to planets
    each Planet takes a planet number and a JulianDay class
    """

    def __init__(self, pnumber, context=EphContext(),master=None):
        self.timeJD = context.timeJD
        self._context = context
        self._amsha = self._context.amsha
        self.master = master
        self.pnumber = pnumber
        self.planet_name = self._context.names.planet_names[self.pnumber]
        self.jd = self.timeJD.jd
        self._ayanamsa = context.ayanamsa
        self.system = context.sysflg
        self.sysflg = self.system | swe.FLG_SPEED
        self.sysflgstr = const.sysflgstr(context.sysflg)
        # if a longitude is passed, we are in a varga not equal to 1
        self.long, self.lat, self.dist, self.long_speed, self.lat_speed, self.dist_speed = self.init_coords()
        # deal with Ketu; i tried to put this in Ketu's class, but it didnt work comletely
        self.long = self.long if not isinstance(self,Ketu) else (self.long-180)%360
        if isinstance(self,Ketu):
            self.pnumber = 8
        # so that we only need only longitude() function with all the signizing and rounding or not
        # this instantiates all the functions in Longitude
        # this is for all the calculations that require *only* longitude
        # thus it is used for both Planet and Cusp
        super().__init__(self.long,self._amsha,self._context)
        if self._amsha != 1:
            self.lat = self.dist = self.long_speed = self.lat_speed = self.dist_speed = 0
        self._hd = HDLongitude(self.ecliptic_longitude(),context=self._context.hdcontext)
        # below is the default for the outer planets, since they dont have dignity
        # the others are set post-instantiation, since we need all the planets to fully determine
        # dignity, so then these are added later
        self.attributes = {"dignity": "NA"} # will hold attributes to be set post-init; dictionary, where "attribute" is the key, e.g., "dignity"
        from .nakshatras import Nakshatra
        self._nakshatra = Nakshatra(self)

    # this < is specialized to jaimini_karakas since it uses in_sign_longitude, not ecliptic longitude
    def __lt__(self,p2: Self):
        return self.real_in_sign_longitude() < p2.real_in_sign_longitude()

    def amsha(self):
        return self._amsha
    
    def hd(self):
        return self._hd

    def table_row(self):
        return (
            [self.name()]
            + [self.longitude()]
            + [self.nakshatra_name()]
            + [self.nakshatra().elapsed()]
            + [self.longitude_speed()]
            + [self.latitude()]
            + [self.latitude_speed()]
            + [self.distance()]
            + [self.distance_speed()]
        )

    def init_coords(self):
        loc = self._context.location.swe_location()
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
        # for draconic charts i choose -8 to indicate that system
        # but swe doesnt accept that, so replace it if necessary
        return swe.calc_ut(self.jd, self.pnumber, self.sysflg if self.sysflg >= 0 else 0)[0]

    def name(self) -> str:
        return self.planet_name + self.retrostr()

    def swe_id(self):
        return self.pnumber

    def set_attribute(self,attrs):
        """
        attrs is a tuple ("attribute",value)
        add all of these to self.attributes
        attritube is a string that will be a dictionary key for value
        """
        key,value=attrs
        self.attributes[key] = value

    def dignity(self):
        """
        return the dignity that has been set by Planets.
        """
        return self.attributes["dignity"]

    def list_index(self):
        match self.pnumber:
            case swe.SUN:
                return 0
            case swe.MOON:
                return 1
            case swe.MARS:
                return 2
            case swe.MERCURY:
                return 3
            case swe.JUPITER:
                return 4
            case swe.VENUS:
                return 5
            case swe.SATURN:
                return 6
            case swe.TRUE_NODE:
                return 7
            case swe.TRUE_NODE:
                return 8
            case swe.URANUS:
                return 9
            case swe.NEPTUNE:
                return 10
            case swe.PLUTO:
                return 11
            case swe.CHIRON:
                return 12

    def system_name(self) -> str:
        return self.sysflgstr

    def object_type(self) -> str:
        return "Planet"

    def identity(self) -> str:
        return self._id

    def key(self) -> str:
        return self.identity()

    def latitude(self) -> float:
        if self._context.toround[0]:
            return round(self.lat, self._context.toround[1])
        else:
            return self.lat

    def declination(self) -> float:
        """
        add declination so that is is always retrivable
        """
        declination = swe.calc_ut(self.timeJD.jd_number(),self.pnumber,swe.FLG_EQUATORIAL)[0][1]
        if self._context.toround[0]:
            return round(declination, self._context.toround[1])
        else:
            return declination

    def distance(self):
        if self._context.toround[0]:
            return round(self.dist, self._context.toround[1])
        else:
            return self.dist

    def speed(self):
        return self.longitude_speed()

    def longitude_speed(self):
        if self._context.toround[0]:
            return round(self.long_speed, self._context.toround[1])
        else:
            return self.long_speed

    def latitude_speed(self):
        if self._context.toround[0]:
            return round(self.lat_speed, self._context.toround[1])
        else:
            return self.lat_speed

    def distance_speed(self):
        if self._context.toround[0]:
            return round(self.dist_speed, self._context.toround[1])
        else:
            return self.dist_speed

    def ayanamsa(self):
        return self._ayanamsa

    def ayanamsa_name(self) -> str:
        return const.ayanamsa_name(self.ayanamsa())

    def retrograde(self) -> bool:
        if self.longitude_speed() < 0:
            return True
        else:
            return False

    def retrostr(self) -> str:
        if self.retrograde():
            return " (R)"
        else:
            return ""

    def daily_motion(self):
        """
        return daily motion in degress that the planet traverses
        in the next 24 hours from self.julianday
        """
        return (
            (swe.calc_ut(self.timeJD.jd + 1, self.pnumber, self.sysflg)[0][0])
            - (swe.calc_ut(self.timeJD.jd, self.pnumber, self.sysflg)[0][0])
        )

    def riseset(self, rs, location=Location()):
        """
        :rs flag for rise, set, or one of the two meridian transits
        swe.CALC_RISE, swe.CALC_SET, swe.MTRANSIT, swe.ITRANSIT
        :location a Location class for where this is for
        """
        return JulianDay(
            swe.rise_trans(
                self.timeJD.jd_number(),  # midnightjd() if (rs == swe.CALC_RISE) else self.jd,
                self.pnumber,
                rs | swe.BIT_HINDU_RISING,
                location.swe_location(),
            )[1][0],self.timeJD.utcoffset,self.timeJD.timezone()
        )

    def nakshatra(self) -> Nakshatra:
        return self._nakshatra

    def nakshatra_name(self) -> str:
        return self._nakshatra.nakshatra()

    def context(self):
        return self._context

    def ingress(self, next_long) -> Self:
        """
        return Planet for the JulianDay where Sun arrives at longitude next_long
        """
        # % 360 help in case we are looking for the equinox, next_long = 0
        if round(self.ecliptic_longitude(),3)%360 == round(next_long,3):
            # if we dont go forward one second the longitude we are are will be
            # for example, 269.99999769, and then the ephemeris will print "30:00:00 bhaga"
            # so by going forward one seconds, we get to 270.0000000343 and it will print "00:00:00 pusha"
            return Sun(replace(self.context,timeJD=self.timeJD.shift("f","seconds",1)))
        # difference between current longitude and desired longitude
        diff = self.degrees_apart(next_long)
        shift_factor = diff*self.lowest_daily_speed()
        # get Planet class for this planet
        planet = local_planets[self.identity()]
        return planet(replace(self.context,timeJD=self.timeJD.shift("f","days",shift_factor)))

    def _dignity(self, self_in_rashi, lord: Self) -> str:
        """
        return the dignity of a planet
        i.e, the combined relationship, so we need to know where the lord is
    
        this doesnt really work like you might expect, since we need information from Planets
        since a Planet cannot always determine its dignity on its own

        we need self_in_rashi to calculate temporary relationships based on the rashi chart
        so now we cant calculate temporary relationships based on the specific varga with this code
        """
        if self.is_ex():
            return "EX"
        if self.is_mt():
            return "MT"
        if self.is_oh():
            return "OH"
        if self.is_db():
            return "DB"
        natural_relationship = self.natural_relationship_from(lord)
        distance = self_in_rashi.signs_apart(lord.sign())
        match distance:
            case 1 | 2 | 3 | 9 | 10 | 11:
                temporary_relationship = "F"
            case _:
                temporary_relationship = "E"
        match (natural_relationship,temporary_relationship):
            case ("F","F"):
                return "GF"
            case ("N","F"):
                return "F"
            case ("E","F"):
                return "N"
            case ("F","E"):
                return "N"
            case ("N","E"):
                return "E"
            case ("E","E"):
                return "GE"
            case ("N","N"):
                return "N"

    def parashara_aspect_to(self, planet: Self | Cusp) -> float | str:
        """
        return the float of the precise parashara aspect between
        self and planet

        this function does aspects for Sun, Moon, Mercury and Venus
        the other karakas have their own special aspects that are defined in their own classes

        this is implemented according to the sutras from bphs as found in graha sutras by ew
        """
        if self.identity() == planet.identity():
            # a planet is not aspecting itself; so there is no value
            return ""
        if self.sign() == planet.sign():
            # Y for yuti, conjunction
            return "Y"
        diff = self.degrees_apart(planet.ecliptic_longitude())
        if diff <= 30 or diff >= 300:
            # within this orb planets do not aspect other planets
            return ""
        if diff > 180 and diff < 300:
            return (300 - diff)/2
        if diff > 150 and diff <= 180:
            return (diff - 150)*2
        if diff > 120 and diff <= 150:
            return (150 - diff)
        if diff > 90 and diff <= 120:
            return ((120-diff)/2) + 30
        if diff > 60 and diff <= 90:
            return (diff - 60) + 15
        if diff > 30 and diff <= 60:
            return (diff - 30)/2

    def parashara_aspect_from(self, planet: Self | Cusp) -> float | str:
        return planet.parashara_aspect_to(self)

    def lowest_hourly_speed(self) -> float:
        return self.lowest_daily_speed()/24

    def lowest_minutely_speed(self) -> float:
        return self.lowest_hourly_speed()/60

    def lowest_secondly_speed(self) -> float:
        return self.lowest_minutely_speed()/60

    def __repr__(self):
        ret = ""
        ayanamsa = ""
        if self.system == swe.FLG_SIDEREAL:
            ayanamsa = f"\nUsing {const.ayanamsa_name(self.ayanamsa())} ayanamsa"
        if self.amsha() != 1:
            ret = f"amsha {self.amsha()} {self.planet_name}{self.retrostr()} at {self.longitude()} degrees {self.system_name()} longitude{ayanamsa}\n"
        else:
            ret = f"amsha {self.amsha()} {self.planet_name}{self.retrostr()} at {self.longitude()} degrees {self.system_name()} longitude{ayanamsa}\n"
        return ret

    def __str__(self):
        ayanamsa = ""
        if self.system == swe.FLG_SIDEREAL:
            ayanamsa = f"\nUsing {const.ayanamsa_name(self.ayanamsa())} ayanamsa"
        return (
            f"amsha {self.amsha()}\n{self.planet_name}{self.retrostr()} {self.ecliptic_longitude()} degrees ({self.longitude()}) {self.system_name()} longitude{ayanamsa}\n"
            + f"{self.timeJD}\n"
        )



class Sun(Planet):
    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.SUN, context,master)
        self._id = "Sun"

    def glyph(self):
        return "⨀"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Su"

    def type(self):
        return Sun

    def sunrise_yamakoti(self) -> JulianDay:
        return self.riseset(swe.CALC_RISE, Yamakoti)

    def lowest_daily_speed(self) -> float:
        """
        return a speed lower than the lowest speed for this planet
        used in finding the time when a planet is at a certain longitude
        this is the daily motion
        i.e., x/24 hours = hours motion
        x/24/60 = minute motion
        """
        return .9


    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_graha(self):
        return True

    def nature(self) -> str:
        """
        nature means benefic or malefic
        """
        return "Malefic"


#    def ingress(self, next_long) -> Self:
#        """
#        return Sun for the JulianDay where Sun arrives at longitude next_long
#        """
#        # % 360 help in case we are looking for the equinox, next_long = 0
#        if round(self.ecliptic_longitude(),3)%360 == round(next_long,3):
#            # if we dont go forward one second the longitude we are are will be
#            # for example, 269.99999769, and then the ephemeris will print "30:00:00 bhaga"
#            # so by going forward one seconds, we get to 270.0000000343 and it will print "00:00:00 pusha"
#            return Sun(replace(self.context,timeJD=self.timeJD.shift("f","seconds",1)))
#        # difference between current longitude and desired longitude
#        diff = self.degrees_apart(next_long)
#        shift_factor = diff*self.lowest_daily_speed()
#        return Sun(replace(self.context,timeJD=self.timeJD.shift("f","days",shift_factor))).ingress(next_long)

    def next_equinox(self):
        """
        get the next equinox from the current timeJD
        """
        # between ascending and descending, so find descending
        if self.ecliptic_longitude() > 0 and self.ecliptic_longitude() < 180:
            return self.ingress(180)
        # otherwise, we are between descending and ascending, so find ascending
        else:
            return self.ingress(0)

    def next_solstice(self):
        """
        get the next solstice from the current timeJD
        """
        # between norther and southern, so find southern
        if self.ecliptic_longitude() > 90 and self.ecliptic_longitude() < 270:
            return self.ingress(270)
        # otherwise, we are between southern and northern, so find northern
        else:
            return self.ingress(90)

    def is_ex(self):
        if self.sign() == 1:
            return True
        else:
            return False

    def is_mt(self):
        if self.sign() == 5 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 20):
            return True
        else:
            return False

    def is_oh(self):
        if self.sign() == 5 and self.real_in_sign_longitude() > 20:
            return True
        else:
            return False


    def is_db(self):
        if self.sign() == 7:
            return True
        else:
            return False

    def natural_relationship_from(self, lord):
        match lord.identity():
            case "Moon":
                return "F"
            case "Mars":
                return "F"
            case "Mercury":
                return "N"
            case "Jupiter":
                return "F"
            case "Venus":
                return "E"
            case "Saturn":
                return "E"


class Moon(Planet):
    def __init__(self, context=EphContext(),master=None, nature=None):
        super().__init__(swe.MOON, context,master)
        self._id = "Moon"
        self.attributes = {"nature": nature}

    def glyph(self):
        return "☾"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Mo"

    def type(self):
        return Moon

    def nature(self):
        return  self.attributes["nature"]

    def lowest_daily_speed(self) -> float:
        """
        return a speed lower than the lowest speed for this planet
        used in finding the time when a planet is at a certain longitude
        this is the daily motion
        i.e., x/24 hours = hours motion
        x/24/60 = minute motion
        """
        return 11.0

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_graha(self):
        return True

    def is_ex(self):
        if self.sign() == 2 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 3):
            return True
        else:
            return False

    def is_mt(self):
        if self.sign() == 2 and self.real_in_sign_longitude() > 3:
            return True
        else:
            return False

    def is_oh(self):
        if self.sign() == 4:
            return True
        else:
            return False

    def is_db(self):
        if self.sign() == 8 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 3):
            return True
        else:
            return False

    def natural_relationship_from(self, lord):
        match lord.identity():
            case "Sun":
                return "F"
            case "Mars":
                return "N"
            case "Mercury":
                return "F"
            case "Jupiter":
                return "N"
            case "Venus":
                return "N"
            case "Saturn":
                return "N"

class Mars(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.MARS, context,master)
        self._id = "Mars"

    def glyph(self):
        return "♂"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ma"

    def type(self):
        return Mars

    def nature(self) -> str:
        """
        nature means benefic or malefic
        """
        return "Malefic"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_graha(self):
        return True

    def is_ex(self):
        if self.sign() == 10:
            return True
        else:
            return False

    def is_mt(self):
        if self.sign() == 1 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 12):
            return True
        else:
            return False

    def is_oh(self):
        if (self.sign() == 1 and self.real_in_sign_longitude() > 12) or self.sign() == 8:
            return True
        else:
            return False

    def is_db(self):
        if self.sign() == 4:
            return True
        else:
            return False

    def natural_relationship_from(self, lord):
        match lord.identity():
            case "Sun":
                return "F"
            case "Moon":
                return "F"
            case "Mercury":
                return "E"
            case "Jupiter":
                return "F"
            case "Venus":
                return "N"
            case "Saturn":
                return "N"

    def parashara_aspect_to(self, planet: Self | Cusp) -> float | str:
        """
        return the float of the precise parashara aspect between
        self and planet

        this function does aspects for Mars
        the other karakas have their own special aspects that are defined in their own classes

        this is implemented according to the sutras from bphs as found in graha sutras by ew
        """
        if self.identity() == planet.identity():
            # a planet is not aspecting itself; so there is no value
            return ""
        if self.sign() == planet.sign():
            # Y for yuti, conjunction
            return "Y"
        diff = self.degrees_apart(planet.ecliptic_longitude())
        if diff <= 30 or diff >= 300:
            # within this orb planets do not aspect other planets
            return ""
        if diff > 240 and diff < 300:
            return (300 - diff)/2
        if diff > 210 and diff <= 240:
            return 60 - (diff - 210)
        if diff > 180 and diff < 210:
            return 60
        if diff > 150 and diff <= 180:
            return (diff - 150)*2
        if diff > 120 and diff <= 150:
            return (150 - diff)
        if diff > 90 and diff <= 120:
            return 60 - (120 - diff)
        if diff > 60 and diff <= 90:
            return (diff - 60) + (diff - 60)/2 + 15
        if diff > 30 and diff <= 60:
            return (diff - 30)/2

class Mercury(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.MERCURY, context,master)
        self._id = "Mercury"

    def glyph(self):
        return "☿"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Me"

    def type(self):
        return Mercury

    def nature(self) -> str:
        """
        nature means benefic or malefic
        """
        return "Benefic"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_graha(self):
        return True

    def is_ex(self):
        if self.sign() == 6 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 15):
            return True
        else:
            return False

    def is_mt(self):
        if self.sign() == 6 and (self.real_in_sign_longitude() >= 15 and self.real_in_sign_longitude() < 20):
            return True
        else:
            return False

    def is_oh(self):
        if self.sign() == 3 or (self.sign() == 6 and self.real_in_sign_longitude() >= 20):
            return True
        else:
            return False

    def is_db(self):
        if self.sign() == 12 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 15):
            return True
        else:
            return False

    def natural_relationship_from(self, lord):
        match lord.identity():
            case "Sun":
                return "F"
            case "Moon":
                return "E"
            case "Mars":
                return "N"
            case "Jupiter":
                return "N"
            case "Venus":
                return "F"
            case "Saturn":
                return "N"

class Venus(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.VENUS, context,master)
        self._id = "Venus"

    def glyph(self):
        return "♀"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ve"

    def type(self):
        return Venus

    def nature(self) -> str:
        """
        nature means benefic or malefic
        """
        return "Benefic"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_graha(self):
        return True

    def is_ex(self):
        if self.sign() == 12:
            return True
        else:
            return False

    def is_mt(self):
        if self.sign() == 7 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 15):
            return True
        else:
            return False

    def is_oh(self):
        if self.sign() == 2 or (self.sign() == 7 and self.real_in_sign_longitude() > 15):
            return True
        else:
            return False

    def is_db(self):
        if self.sign() == 6:
            return True
        else:
            return False

    def natural_relationship_from(self, lord):
        match lord.identity():
            case "Sun":
                return "E"
            case "Moon":
                return "E"
            case "Mars":
                return "N"
            case "Mercury":
                return "F"
            case "Jupiter":
                return "N"
            case "Saturn":
                return "F"


class Jupiter(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.JUPITER, context,master)
        self._id = "Jupiter"

    def glyph(self):
        return "♃"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ju"

    def type(self):
        return Jupiter

    def nature(self) -> str:
        """
        nature means benefic or malefic
        """
        return "Benefic"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_graha(self):
        return True

    def is_ex(self):
        if self.sign() == 4:
            return True
        else:
            return False

    def is_mt(self):
        if self.sign() == 9 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 10):
            return True
        else:
            return False

    def is_oh(self):
        if self.sign() == 12 or (self.sign() == 9 and self.real_in_sign_longitude() > 10):
            return True
        else:
            return False

    def is_db(self):
        if self.sign() == 10:
            return True
        else:
            return False

    def natural_relationship_from(self, lord):
        match lord.identity():
            case "Sun":
                return "F"
            case "Moon":
                return "F"
            case "Mars":
                return "F"
            case "Mercury":
                return "E"
            case "Venus":
                return "E"
            case "Saturn":
                return "N"

    def parashara_aspect_to(self, planet: Self | Cusp) -> float | str:
        """
        return the float of the precise parashara aspect between
        self and planet

        this function does aspects for Jupiter 
        the other karakas have their own special aspects that are defined in their own classes

        this is implemented according to the sutras from bphs as found in graha sutras by ew
        """
        if self.identity() == planet.identity():
            # a planet is not aspecting itself; so there is no value
            return ""
        if self.sign() == planet.sign():
            # Y for yuti, conjunction
            return "Y"
        diff = self.degrees_apart(planet.ecliptic_longitude())
        if diff <= 30 or diff >= 300:
            # within this orb planets do not aspect other planets
            return ""
        if diff > 270 and diff < 300:
            return (300 - diff)/2
        if diff > 240 and diff <= 270:
            return ((30-(diff-240))*1.5) + 15
        if diff > 210 and diff <= 240:
            return ((diff-210)/2) + 45
        if diff > 180 and diff <= 210:
            return (300 - diff)/2
        if diff > 150 and diff <= 180:
            return (diff - 150)*2
        if diff > 120 and diff <= 150:
            return 60 - ((diff-120)*2)
        if diff > 90 and diff <= 120:
            return ((120-diff)/2) + 45
        if diff > 60 and diff <= 90:
            return (diff - 60) + 15
        if diff > 30 and diff <= 60:
            return (diff - 30)/2


class Saturn(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.SATURN, context,master)
        self._id = "Saturn"

    def glyph(self):
        return "♄"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Sa"

    def type(self):
        return Saturn

    def nature(self) -> str:
        """
        nature means benefic or malefic
        """
        return "Malefic"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_graha(self):
        return True

    def is_ex(self):
        if self.sign() == 7:
            return True
        else:
            return False

    def is_mt(self):
        if self.sign() == 11 and (self.real_in_sign_longitude() >= 0 and self.real_in_sign_longitude() < 20):
            return True
        else:
            return False

    def is_oh(self):
        if self.sign() == 10 or (self.sign() == 11 and self.real_in_sign_longitude() > 20):
            return True
        else:
            return False

    def is_db(self):
        if self.sign() == 1:
            return True
        else:
            return False

    def natural_relationship_from(self, lord):
        match lord.identity():
            case "Sun":
                return "E"
            case "Moon":
                return "E"
            case "Mars":
                return "E"
            case "Mercury":
                return "F"
            case "Jupiter":
                return "N"
            case "Venus":
                return "F"

    def parashara_aspect_to(self, planet: Self | Cusp) -> float | str:
        """
        return the float of the precise parashara aspect between
        self and planet

        this function does aspects for Saturn
        the other karakas have their own special aspects that are defined in their own classes

        this is implemented according to the sutras from bphs as found in graha sutras by ew
        """
        if self.identity() == planet.identity():
            # a planet is not aspecting itself; so there is no value
            return ""
        if self.sign() == planet.sign():
            # Y for yuti, conjunction
            return "Y"
        diff = self.degrees_apart(planet.ecliptic_longitude())
        if diff <= 30 or diff >= 300:
            # within this orb planets do not aspect other planets
            return ""
        if diff > 270 and diff < 300:
            return (300 - diff)*2
        if diff > 240 and diff <= 270:
            return (diff - 240) + 30
        if diff > 180 and diff <= 240:
            return (300 - diff)/2
        if diff > 150 and diff <= 180:
            return (diff - 150)*2
        if diff > 120 and diff <= 150:
            return (150 - diff)
        if diff > 90 and diff <= 120:
            return ((120-diff)/2) + 30
        if diff > 60 and diff <= 90:
            return 60 - ((diff - 60)/2)
        if diff > 30 and diff <= 60:
            return (diff - 30)*2


class Rahu(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.TRUE_NODE, context,master)
        self.planet_name = context.names.planet_names[10]
        self._id = "Rahu"

    def glyph(self):
        return "☊"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ra"

    def type(self):
        return Rahu

    def nature(self) -> str:
        """
        nature means benefic or malefic
        """
        return "Malefic"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return False

    def is_graha(self):
        return True


class Ketu(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.TRUE_NODE, context,master)
        self.planet_name = context.names.planet_names[11]
        self._id = "Ketu"
        
    def glyph(self):
        return "☋"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ke"

    def type(self):
        return Ketu

    def nature(self) -> str:
        """
        nature means benefic or malefic
        """
        return "Malefic"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return False

    def is_graha(self):
        return True


class Uranus(Planet):
    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.URANUS, context,master)
        self._id = "Uranus"

    def glyph(self):
        return "⛢"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ur"

    def type(self):
        return Uranus

    def is_outer_planet(self):
        return True

    def is_karaka(self):
        return False

    def is_graha(self):
        return False

class Neptune(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.NEPTUNE, context,master)
        self._id = "Neptune"

    def glyph(self):
        return "♆"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ne"

    def type(self):
        return Neptune

    def is_outer_planet(self):
        return True

    def is_karaka(self):
        return False

    def is_graha(self):
        return False


class Pluto(Planet):

    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.PLUTO, context,master)
        self._id = "Pluto"

    def glyph(self):
        return "♇"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Pu"

    def type(self):
        return Pluto

    def is_outer_planet(self):
        return True

    def is_karaka(self):
        return False

    def is_graha(self):
        return False

class Earth(Planet):
    def __init__(self, context=EphContext(),master=None):
        super().__init__(swe.EARTH, context,master)
        self._id = "Earth"

    def glyph(self):
        return "⨁"

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ea"

    def type(self):
        return Earth

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return False

    def is_graha(self):
        return False

class Chiron(Planet):

    def __init__(self, context=EphContext(),master=None):
        self.planet_name = "Chiron"
        super().__init__(swe.CHIRON, context,master)
        self._id = "Chiron"

    def type(self):
        return Chiron

    def abbreviation(self) -> str:
        """
        two letter representation of Planet's name
        """
        return "Ch"

    def is_outer_planet(self):
        return True

    def is_karaka(self):
        return False

    def is_graha(self):
        return False

local_planets = {
    "Sun": Sun,
    "Moon": Moon,
    "Mars": Mars,
    "Mercury": Mercury,
    "Jupiter": Jupiter,
    "Venus": Venus,
    "Saturn": Saturn,
    "Rahu": Rahu,
    "Ketu": Ketu,
    "Uranus": Uranus,
    "Neptune": Neptune,
    "Pluto": Pluto,
    "Chiron": Chiron
}

class Planets:

    def __init__(self, context=EphContext()):
        """
        initialize Planets
        planets default is for vargas > 1, which will pass
        a list of Planet classes and this will make a container for them
        the varga.__init__ function will make a dictionary of planets
        and pass that dictionary into this class
        """
        self.timeJD = context.timeJD  # the JulianDay class of this planet
        self.context = context
        self._amsha = self.context.amsha
        self.jd = self.timeJD.jd
        self.ayanamsa = context.ayanamsa
        self.system = context.sysflg
        self.sysflgstr = const.sysflgstr(context.sysflg)
        self._planets = self.init_Planets()
        self.set_attributes()
        from .nakshatras import Nakshatras
        self._nakshatras = Nakshatras(self,self.context)

    def __iter__(self):
        return iter(self._planets.values())

    def __getitem__(self,n):
        return self._planets[n]

    def planets(self):
        return self._planets

    def items(self):
        return self._planets.items()

    def karakas(self):
        return {"Sun": self.sun(),
                "Moon": self.moon(),
                "Mars": self.mars(),
                "Mercury": self.mercury(),
                "Jupiter": self.jupiter(),
                "Venus": self.venus(),
                "Saturn": self.saturn()
                }

    def grahas(self):
        return {"Sun": self.sun(),
                "Moon": self.moon(),
                "Mars": self.mars(),
                "Mercury": self.mercury(),
                "Jupiter": self.jupiter(),
                "Venus": self.venus(),
                "Saturn": self.saturn(),
                "Rahu": self.rahu(),
                "Ketu": self.ketu()
                }

    def init_Planets(self):
        ret = {}

        # chiron can only be computed in a certain time frame
        if self.timeJD.jd < 1967601.5 or self.timeJD.jd > 3419437.5:
            # swe can only compute Chiron between these two days
            # so if it is outside this range, get rid of Chiron
            local_planets.pop()

        # add Earth if using barycentric or heliocentric
        if self.system == const.BARY or self.system == const.HELIO:
            # add Earth to the planet_dict["planets"], after Pluto and before Chiron
            local_planets["Earth"] = Earth

        for planet,constructor in local_planets.items():
            ret[planet] = constructor(self.context,self)


        return ret

    def set_attributes(self):
        """
        there is some information i want each Planet to know, but that I have to use
        the other Planet-s to calculate first. so we init_Planets() above,
        then we can set_attributes() in __init__(), e.g., dignity
        """
        moon_nature = "Benefic" if self.sun().degrees_apart(self.moon().ecliptic_longitude()) <= 180 else "Malefic"
        self.moon().set_attribute(("nature",moon_nature))
        digs = self.dignities()
        # for the outer planets and miscellaneous_planets
        digs+=["NA","NA","NA","NA","NA","NA"]
        for planet in self:
            if isinstance(planet,Rahu) or isinstance(planet,Ketu):
                # these two will show the dignity of their lords in the complete list
                # need the list index of the Rahus lord
                # Rahu nows who is lord is, but does not have direct access to him
                # i.e., Rahu cannot return the Planet class of his Lord...is that possible?
                # more recursive structures?
                # right now, this gets the Planet class from self.planets, then gets its list_index
                planet.set_attribute(("dignity",digs[self.planets()[planet.lord()].list_index()]))
            else:
                planet.set_attribute(("dignity",digs[planet.list_index()]))


    def nakshatras(self) -> Nakshatras:
        return self._nakshatras

    def dignities(self, temp_planets=None) -> [str]:
        """
        return a list of dignities in the natural order
        Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn

        dignity is a combination of natural and temporary relationship
        we can use the temporary relationship from the varga itself, or from the rashi chart

        if Planets is in a varga and temp_planets=None, then it will use temporary relationships based on that varga
        so if, for instance, you want to determine dignity in the Navamsha based on temporary friends in the Rashi
        you must past d9Planets.dignites(temp_planets=d1Planets)
        """
        if temp_planets == None:
            temp_planets = self
        # else: temp_planets are the planets from the rashi chart
        dignities = []
        for planet in self.karakas().values():
            # _dignity() takes two arguments: 1) itself in the rashi chart or this varga, depending on the options
            #                                 2) its lord in rashi or in this varga, depending on the option
            #                                 set with EphContext.rashi_temporary_friends True or False
#            if planet.identity() == "Sun":
#                import pdb; pdb.set_trace()
            dignities.append(planet._dignity(temp_planets.karakas()[planet.identity()],temp_planets.karakas()[planet.lord()]))
        return dignities

    def parashara_aspects(self):
        """
        return a list of lists, each inner list being a row
        the first list is sun aspecting sun through ketu in order, etc.
        """
        ret = []

        for aspecting in self.karakas().values():
            this_row = []
            for aspected in self.grahas().values():
                value = aspecting.parashara_aspect_to(aspected)
                this_row.append(int(round(value,0)) if isinstance(value,float) else value)
            ret.append(this_row)

        return ret

    def parashara_aspects_cusps(self, cusps):
        """
        return a list of lists, each inner list being a row
        the first list is sun aspecting sun through ketu in order, etc.
        """
        ret = []

        for aspecting in self.karakas().values():
            this_row = []
            for aspected in cusps:
                value = aspecting.parashara_aspect_to(aspected)
                this_row.append(int(round(value,0)) if isinstance(value,float) else value)
            ret.append(this_row)

        return ret

    def jaimini_karakas(self) -> [Self]:
        """
        return a list of Planet classes where the first element is the ak, the second the amk, etc.
        """
        # we need to sort according to real in sign longitude
        longs = {}
        for karaka in self.karakas().values():
            # the longitude is the key, the Planet the value
            # the following doesnt work if two planets have the same longitude!
            # longs[karaka.in_sign_longitude()] = karaka
            # below is better, but still, what if two planets have same longitude? doesnt work then
            longs[karaka] = karaka.in_sign_longitude()
        ret = []
        # for long in sorted(longs.values())
        # sorted from least in sign longitude to to most
        # sorted returns a list of Planet classes
        karakas_reverse = sorted(longs.items())
        # karakas_reverse is a list of tuples (Planet,in_sign_longitude)
        ret = [karaka[0] for karaka in karakas_reverse]
        # sorted() gives from least to most, but karakas are from most to least
        return list(ret.__reversed__())

    def is_moon_benefic(self):
        return self.sun().degrees_apart(self.moon().ecliptic_longitude()) <= 180

    def is_moon_malefic(self):
        return self.sun().degrees_apart(self.moon().ecliptic_longitude()) > 180

    def sun(self):
        return self._planets["Sun"]

    def moon(self):
        return self._planets["Moon"]

    def mars(self):
        return self._planets["Mars"]

    def mercury(self):
        return self._planets["Mercury"]

    def jupiter(self):
        return self._planets["Jupiter"]

    def venus(self):
        return self._planets["Venus"]

    def saturn(self):
        return self._planets["Saturn"]

    def rahu(self):
        return self._planets["Rahu"]

    def ketu(self):
        return self._planets["Ketu"]

    def uranus(self):
        return self._planets["Uranus"]

    def neptune(self):
        return self._planets["Neptune"]

    def pluto(self):
        return self._planets["Pluto"]

    def chiron(self):
        return self._planets["Chiron"]

    def __str__(self):
        if self.context.print_nakshatras:
            return self.planets_with_nakshatras()
        else:
            return self.planets_complete_information()

    def planets_with_nakshatras(self):
        """
        return a PrettyTable string with coordinates for all planets on julianday
        using sysflag coordinates
        """
        output = PrettyTable()
        output.field_names = [
            "Planet",
            "Longitude",
            "Nakshatra",
            "Elapsed",
            "Speed",
            "Latitude",
            "Latitude Speed",
            "Distance",
            "Distance Speed",
        ]
        output.align["Planet"] = "l"
        output.align["Longitude"] = "l"
        output.align["Nakshatra"] = "r"
        output.align["Elapsed"] = "r"
        output.align["Speed"] = "r"
        output.align["Latitude"] = "r"
        output.align["Latitude Speed"] = "r"
        output.align["Distance"] = "r"
        output.align["Distance Speed"] = "r"

        for p in self._planets.values():
            # dont print earth unless it is heliocentric or barycentric
            if isinstance(p, Earth) and not (
                self.system == const.HELIO or self.system == const.BARY
            ):
                continue
            # dont print rahuketu if it is heliocentric or barycentric
            if (isinstance(p, Rahu) or isinstance(p, Ketu)) and (
                self.system == const.HELIO or self.system == const.BARY
            ):
                continue
            # dont print the Sun when printing heliocentric coordinates
            if isinstance(p, Sun) and self.system == const.HELIO:
                continue
            if not self.context.print_outer_planets and p.is_outer_planet():
                continue
            output.add_row(p.table_row())

        ret = output.get_string(
            fields=[
                "Planet",
                "Longitude",
                "Speed",
                "Nakshatra",
                "Elapsed",
                "Latitude",
            ]
        )

        return self.mkheader() + ret

    def planets_complete_information(self):
        """
        return a PrettyTable string with coordinates for all planets on julianday
        using sysflag coordinates
        """
        output = PrettyTable()
        output.field_names = [
            "Planet",
            "Longitude",
            "Speed",
            "Latitude",
            "Latitude Speed",
            "Distance",
            "Distance Speed",
        ]
        output.align["Planet"] = "l"
        output.align["Longitude"] = "l"
        output.align["Speed"] = "r"
        output.align["Latitude"] = "r"
        output.align["Latitude Speed"] = "r"
        output.align["Distance"] = "r"
        output.align["Distance Speed"] = "r"

        for p in self._planets.values():
            # dont print earth unless it is heliocentric or barycentric
            if isinstance(p, Earth) and not (
                self.system == const.HELIO or self.system == const.BARY
            ):
                continue
            # dont print rahuketu if it is heliocentric or barycentric
            if (isinstance(p, Rahu) or isinstance(p, Ketu)) and (
                self.system == const.HELIO or self.system == const.BARY
            ):
                continue
            # dont print the Sun when printing heliocentric coordinates
            if isinstance(p, Sun) and self.system == const.HELIO:
                continue
            if not self.context.print_outer_planets and p.is_outer_planet():
                continue
            output.add_row(p.table_row()[:2]+p.table_row()[4:])

        ret = output.get_string(
            fields=[
                "Planet",
                "Longitude",
                "Speed",
                "Latitude",
                "Latitude Speed",
                "Distance",
                "Distance Speed"
            ]
        )

        return self.mkheader() + ret

    def __repr__(self):
        return self.planets_complete_information()

    def hd_planets(self):
        definition = self.hd_planets_definition()
        state = self.hd_planets_state()
        return "Human Design Planets\n" + self.mkheader() + definition + "\n" + state

    def mkheader(self):
        header = f"{self.sysflgstr} coordinates\n"
        header += f"amsha {self._amsha}\n"
        header += f"{const.circle_name(self.context.circle)}\n"
        if self.system == swe.FLG_SIDEREAL:
            # for sidereal signs we actually use swisseph 36
            # dhruva equatorial is only for nakshatras
            if self.ayanamsa == 98:
                header += f"{const.ayanamsa_name(36)} ayanamsa for signs\n"
                header += f"{const.ayanamsa_name(98)} ayanamsa for nakshatras\n"
            else:
                header += f"{const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        elif self.system == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
            if self.ayanamsa == 98:
                self.ayanamsa = 36
            header += f"{self.context.location}\n"
            header += f"{const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        else:
            header += f"{const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        if self.system == swe.FLG_TOPOCTR:
            header += f"{self.context.location}"
        header += f"{self.timeJD}\n"
        return header

    def hd_planets_definition(self):
        output = PrettyTable()
        output.field_names = [
            "Planet",
            "Longitude",
            "Gate",
            "Line",
            "Color",
            "Tone",
            "Base",
            "Speed",
            "Sign"
        ]
        output.align["Planet"] = "l"
        output.align["Longitude"] = "l"
        output.align["Gate"] = "r"
        output.align["Line"] = "r"
        output.align["Color"] = "r"
        output.align["Tone"] = "r"
        output.align["Base"] = "r"
        output.align["Speed"] = "r"
        output.align["Sign"] = "r"

        for planet in self:
            output.add_row([planet.name()] + planet.hd().row_definition() + [planet.speed()] + [planet.signize()])

        ret = output.get_string(
            fields=[
            "Planet",
            "Longitude",
            "Gate",
            "Line",
            "Color",
            "Tone",
            "Base",
            "Speed",
            "Sign"
            ]
        )
        return ret

    def hd_planets_state(self):
        output = PrettyTable()
        output.field_names = [
            "Planet",
            "Longitude",
            "Gate Elapsed",
            "Line Elapsed",
            "Color Elapsed",
            "Tone Elapsed",
            "Base Elapsed",
            "Speed"
        ]
        output.align["Planet"] = "l"
        output.align["Longitude"] = "l"
        output.align["Gate Elapsed"] = "r"
        output.align["Line Elapsed"] = "r"
        output.align["Color Elapsed"] = "r"
        output.align["Tone Elapsed"] = "r"
        output.align["Base Elapsed"] = "r"
        output.align["Speed"] = "r"

        for planet in self:
            output.add_row([planet.name()] + planet.hd().row_state() + [planet.speed()])

        ret = output.get_string(
            fields=[
            "Planet",
            "Longitude",
            "Gate Elapsed",
            "Line Elapsed",
            "Color Elapsed",
            "Tone Elapsed",
            "Base Elapsed",
            "Speed",
            ]
        )

        return ret
    

planet_dict = {
    "planets": [Sun, Moon, Mars, Mercury, Venus, Jupiter, Saturn, Rahu, Ketu, Uranus, Neptune, Pluto, Chiron],
    "grahas": [Sun, Moon, Mars, Mercury, Venus, Jupiter, Saturn, Rahu, Ketu],
    "karakas": [Sun, Moon, Mars, Mercury, Venus, Jupiter, Saturn],
    "outer_planets": [Uranus, Neptune, Pluto],
    "miscellaneous_planets": [Chiron]
}

karakas = [Sun, Moon, Mars, Mercury, Venus, Jupiter, Saturn]
