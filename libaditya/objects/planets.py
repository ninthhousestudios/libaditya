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
from prettytable import PrettyTable
from dataclasses import replace
from typing import Self

from libaditya import constants as const

from .julian_day import JulianDay
from .location import Location, Yamakoti
from .context import EphContext
from .longitude import Longitude
from .nakshatras import Nakshatra, Nakshatras


class Planet(Longitude):
    """
    this class has information and functions related to planets
    each Planet takes a planet number and a JulianDay class
    """

    def __init__(self, pnumber, context=EphContext(), longitude=None):
        self.timeJD = context.timeJD
        self._context = context
        self.pnumber = pnumber
        self.planet_name = context.names.planet_names[self.pnumber]
        self.jd = self.timeJD.jd
        self._ayanamsa = context.ayanamsa
        self.system = context.sysflg
        self.sysflg = self.system | swe.FLG_SPEED
        self.sysflgstr = const.sysflgstr(context.sysflg)
        # if a longitude is passed, we are in a varga not equal to 1
        if longitude is None:
            self.long, self.lat, self.dist, self.long_speed, self.lat_speed, self.dist_speed = self.init_coords()
            # deal with Ketu; i tried to put this in Ketu's class, but it didnt work comletely
            self.long = self.long if not isinstance(self,Ketu) else (self.long-180)%360
        else:
            self.long = longitude
            self.lat = self.dist = self.long_speed = self.lat_speed = self.dist_speed = 0
        # so that we only need only longitude() function with all the signizing and rounding or not
        # this instantiates all the functions in Longitude
        # this is for all the calculations that require *only* longitude
        # thus it is used for both Planet and Cusp
        super().__init__(self.long,self._context)
        from .nakshatras import Nakshatra
        self._nakshatra = Nakshatra(self)


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

    def system_name(self) -> str:
        return self.sysflgstr

    def object_type(self) -> str:
        return "Planet"

    def identity(self) -> str:
        return self._id

    def lord(self):
        return const.lords[self.sign()]

    def latitude(self) -> float:
        if self._context.toround[0]:
            return round(self.lat, self._context.toround[1])
        else:
            return self.lat

    def distance(self):
        if self._context.toround[0]:
            return round(self.dist, self._context.toround[1])
        else:
            return self.dist

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
                self.timeJD.midnightjd() if (rs == swe.CALC_RISE) else self.jd,
                self.pnumber,
                rs | swe.BIT_HINDU_RISING,
                location.swe_location(),
            )[1][0],self.timeJD.utcoffset,self.timeJD.timezone
        )

    def nakshatra(self) -> Nakshatra:
        return self._nakshatra

    def nakshatra_name(self) -> str:
        return self._nakshatra.nakshatra()

    def context(self):
        return self._context

    def __str__(self):
        ayanamsa = ""
        if self.system == swe.FLG_SIDEREAL:
            ayanamsa = f"\nUsing {const.ayanamsa_name(self.ayanamsa())} ayanamsa"
        return (
            f"{self.planet_name}{self.retrostr()} at {self.longitude()} degrees {self.system_name()} longitude{ayanamsa}\n"
            + f"{self.timeJD}\n"
        )

    def __repr__(self):
        print(f"{type(self)}")
        ayanamsa = ""
        if self.system == swe.FLG_SIDEREAL:
            ayanamsa = f" with {const.ayanamsa_name(self.ayanamsa())} ayanamsa"
        return (
            f"{self.planet_name}{self.retrostr()} at {self.raw_longitude()} degrees {self.system_name()} longitude{ayanamsa}\n"
            + f"{self.timeJD}"
        )


class Sun(Planet):
    def __init__(self, context=EphContext()):
        super().__init__(swe.SUN, context)
        self._id = "Sun"

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

    def lowest_hourly_speed(self) -> float:
        return self.lowest_daily_speed()/24

    def lowest_minutely_speed(self) -> float:
        return self.lowest_hourly_speed()/60

    def lowest_secondly_speed(self) -> float:
        return self.lowest_minutely_speed()/60

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_inner_planet(self):
        return True

    def ingress(self, next_long) -> Self:
        """
        return Sun for the JulianDay where Sun arrives at longitude next_long
        """
        # % 360 help in case we are looking for the equinox, next_long = 0
        if round(self.real_longitude(),6)%360 == next_long:
            # if we dont go forward one second the longitude we are are will be
            # for example, 269.99999769, and then the ephemeris will print "30:00:00 bhaga"
            # so by going forward one seconds, we get to 270.0000000343 and it will print "00:00:00 pusha"
            return Sun(replace(self.context,timeJD=self.timeJD.shift("f","seconds",1)))
        # difference between current longitude and desired longitude
        diff = self.degrees_apart(next_long)
        shift_factor = diff*self.lowest_daily_speed()
        return Sun(replace(self.context,timeJD=self.timeJD.shift("f","days",shift_factor))).ingress(next_long)

    def next_equinox(self):
        """
        get the next equinox from the current timeJD
        """
        # between ascending and descending, so find descending
        if self.real_longitude() > 0 and self.real_longitude() < 180:
            return self.ingress(180)
        # otherwise, we are between descending and ascending, so find ascending
        else:
            return self.ingress(0)

    def next_solstice(self):
        """
        get the next solstice from the current timeJD
        """
        # between norther and southern, so find southern
        if self.real_longitude() > 90 and self.real_longitude() < 270:
            return self.ingress(270)
        # otherwise, we are between southern and northern, so find northern
        else:
            return self.ingress(90)



class Moon(Planet):
    def __init__(self, context=EphContext()):
        super().__init__(swe.MOON, context)
        self._id = "Moon"

    def lowest_daily_speed(self) -> float:
        """
        return a speed lower than the lowest speed for this planet
        used in finding the time when a planet is at a certain longitude
        this is the daily motion
        i.e., x/24 hours = hours motion
        x/24/60 = minute motion
        """
        return 11.0

    def lowest_hourly_speed(self) -> float:
        return self.lowest_daily_speed()/24

    def lowest_minutely_speed(self) -> float:
        return self.lowest_hourly_speed()/60

    def lowest_secondly_speed(self) -> float:
        return self.lowest_minutely_speed()/60

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_inner_planet(self):
        return True

class Mars(Planet):

    def __init__(self, context=EphContext()):
        super().__init__(swe.MARS, context)
        self._id = "Mars"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_inner_planet(self):
        return True

class Mercury(Planet):

    def __init__(self, context=EphContext()):
        super().__init__(swe.MERCURY, context)
        self._id = "Mercury"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True

    def is_inner_planet(self):
        return True

class Venus(Planet):

    def __init__(self, context=EphContext()):
        super().__init__(swe.VENUS, context)
        self._id = "Venus"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True


class Jupiter(Planet):

    def __init__(self, context=EphContext()):
        super().__init__(swe.JUPITER, context)
        self._id = "Jupiter"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True


class Saturn(Planet):

    def __init__(self, context=EphContext()):
        super().__init__(swe.SATURN, context)
        self._id = "Saturn"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return True


class Rahu(Planet):

    def __init__(self, context=EphContext()):
        super().__init__(swe.TRUE_NODE, context)
        self.planet_name = context.names.planet_names[10]
        self._id = "Rahu"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return False

    def is_inner_planet(self):
        return True


class Ketu(Planet):

    def __init__(self, context=EphContext(), longitude=None):
        super().__init__(swe.TRUE_NODE, context)
        self.planet_name = context.names.planet_names[11]
        self._id = "Ketu"
        

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return False

    def is_inner_planet(self):
        return True


class Uranus(Planet):
    def __init__(self, context=EphContext()):
        super().__init__(swe.URANUS, context)
        self._id = "Uranus"

    def is_outer_planet(self):
        return True

    def is_karaka(self):
        return False

    def is_inner_planet(self):
        return False

class Neptune(Planet):

    def __init__(self, context=EphContext()):
        super().__init__(swe.NEPTUNE, context)
        self._id = "Neptune"

    def is_outer_planet(self):
        return True

    def is_karaka(self):
        return False

    def is_inner_planet(self):
        return False


class Pluto(Planet):

    def __init__(self, context=EphContext()):
        super().__init__(swe.PLUTO, context)
        self._id = "Pluto"

    def is_outer_planet(self):
        return True

    def is_karaka(self):
        return False

    def is_inner_planet(self):
        return False

class Earth(Planet):
    def __init__(self, context=EphContext()):
        super().__init__(swe.EARTH, context)
        self._id = "Earth"

    def is_outer_planet(self):
        return False

    def is_karaka(self):
        return False

    def is_inner_planet(self):
        return False

class Chiron(Planet):

    def __init__(self, context=EphContext()):
        self.planet_name = "Chiron"
        super().__init__(swe.CHIRON, context)
        self._id = "Chiron"

    def is_outer_planet(self):
        return True

    def is_karaka(self):
        return False

    def is_inner_planet(self):
        return False

planets = {
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
        self.timeJD = context.timeJD  # the JulianDay class of this planet
        self.context = context
        self.jd = self.timeJD.jd
        self.ayanamsa = context.ayanamsa
        self.system = context.sysflg
        self.sysflgstr = const.sysflgstr(context.sysflg)
        self.planets = self.init_Planets()
        from .nakshatras import Nakshatras
        self._nakshatras = Nakshatras(self,self.context)

    def __iter__(self):
        return iter(self.planets.values())

    def __getitem__(self,n):
        return self.planets[n]

    def init_Planets(self):
        ret = {}

        # chiron can only be computed in a certain time frame
        if self.timeJD.jd < 1967601.5 or self.timeJD.jd > 3419437.5:
            # swe can only compute Chiron between these two days
            # so if it is outside this range, get rid of Chiron
            planets.pop()

        # add Earth if using barycentric or heliocentric
        if self.system == const.BARY or self.system == const.HELIO:
            # add Earth to the planet_dict["planets"], after Pluto and before Chiron
            planets["Earth"] = Earth

        for p,v in planets.items():
            ret[p] = v(self.context)

        return ret

    def nakshatras(self) -> Nakshatras:
        return self._nakshatras

    def sun(self):
        return self.planets["Sun"]

    def moon(self):
        return self.planets["Moon"]

    def mars(self):
        return self.planets["Mars"]

    def mercury(self):
        return self.planets["Mercury"]

    def jupiter(self):
        return self.planets["Jupiter"]

    def venus(self):
        return self.planets["Venus"]

    def saturn(self):
        return self.planets["Saturn"]

    def rahu(self):
        return self.planets["Rahu"]

    def ketu(self):
        return self.planets["Ketu"]

    def uranus(self):
        return self.planets["Uranus"]

    def neptune(self):
        return self.planets["Neptune"]

    def pluto(self):
        return self.planets["Pluto"]

    def chiron(self):
        return self.planets["Chiron"]

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

        for p in self.planets.values():
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

        for p in self.planets.values():
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

    def mkheader(self):
        header = f"{self.sysflgstr} coordinates\n"
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
    

planet_dict = {
    "planets": [Sun, Moon, Mars, Mercury, Venus, Jupiter, Saturn, Rahu, Ketu, Uranus, Neptune, Pluto, Chiron],
    "inner_planets": [Sun, Moon, Mars, Mercury, Venus, Jupiter, Saturn, Rahu, Ketu],
    "karakas": [Sun, Moon, Mars, Mercury, Venus, Jupiter, Saturn],
    "outer_planets": [Uranus, Neptune, Pluto]
}
