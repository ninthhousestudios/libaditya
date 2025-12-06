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
import time
import calendar
import datetime
import pyphglobals as pglob
import pyphutils as putil
from pyphclasses import *

nowtime = time.gmtime()
nowjdfloat = putil.tmod_to_jd(nowtime)


class Sun(Planet):
    def __init__(self, julianday=JulianDay()):
        super().__init__(swe.SUN, julianday)

    def riseset(self, rs, location=Location()):
        return JulianDay(
            swe.rise_trans(
                self.julianday.midnightjd() if (rs == swe.CALC_RISE) else self.jd,
                self.pnumber,
                rs | swe.BIT_HINDU_RISING,
                location.risetrans_location(),
            )[1][0]
        )

    def sunrise_yamakoti(self):
        return self.riseset(swe.CALC_RISE, Yamakoti)


class Moon(Planet):
    def __init__(self, julianday=JulianDay()):
        super().__init__(swe.MOON, julianday)


class Rahu(Planet):
    def __init__(self, julianday=JulianDay()):
        super().__init__(pglob.true_node, julianday)
        self.planet_name = pglob.planets[10]


class Ketu(Planet):
    def __init__(self, julianday=JulianDay()):
        super().__init__(pglob.true_node, julianday)
        self.planet_name = pglob.planets[11]
        self.coords = self.get_coords()

    def get_coords(self, sysflg=pglob.ECL):
        """
        return swe.calc_ut tuple for coords of Planet at time self.jd
        sysflg tells what kind of coordinates: ECL,EQU,HELIO,BARY
        """
        coords = list(swe.calc_ut(self.jd, self.pnumber, swe.FLG_SPEED | sysflg)[0])
        return [(coords[0] - 180) % 360] + coords[1:]

    def longitude(self, sysflg=pglob.ECL):
        long = swe.calc_ut(self.jd, self.pnumber, sysflg)[0][0]
        return (long - 180) % 360


class Panchanga(JulianDay):
    def __init__(self, julianday=JulianDay(), ayanamsa=pglob.ayanamsa):
        super().__init__(julianday.jd)
        self.julianday = julianday
        self.jd = self.julianday.jd
        self.sun = Sun(
            self
        )  # since Panchanga is a kind of Julian Day, we can pass it to Sun
        self.moon = Moon(self)  # and Moon which will be the sun and moon at the time jd
        self.tithi_raw, self.telapsed, self.tremaining = self.init_tithi()
        self.tithi_int = int(self.tithi_raw) + 1
        self.karana_index = (
            (self.tithi_int - 1, 0)
            if (self.tremaining > 6)
            else (self.tithi_int - 1, 1)
        )
        self.yoga_raw, self.yelapsed, self.yremaining = self.init_yoga()
        self.yoga_int = int(self.yoga_raw + 1)
        self.ayanamsa = ayanamsa

    def init_tithi(self):
        traw = ((self.moon.longitude() - self.sun.longitude()) % 360) / 12
        remainder = traw % 1  # remainder shows how much has elapsed
        elapsed = remainder * 12  # degrees elapsed
        remaining = 12 - elapsed  # degrees remaining
        return (traw, elapsed, remaining)

    def tithi(self):
        return self.tithi_int

    def karana(self):
        return pglob.karana[self.karana_index[0]][self.karana_index[1]]

#    def vara(self):
#        weekday = calendar.weekday(
#            self.julianday.datetime[0],
#            self.julianday.datetime[1],
#            self.julianday.datetime[2],
#        ) # 0 is Monday
#        sunriseyk = self.sun.sunrise_yamakoti()
#        if sunriseyk < self.julianday:
#            return pglob.vara[(weekday) % 7]
#        else:
#            return pglob.vara[weekday % 7]
    def vara(self):
        weekday = datetime.date(
            self.julianday.datetime[0],
            self.julianday.datetime[1],
            self.julianday.datetime[2],
        ).isoweekday()  # 1 is Monday
        sunriseyk = self.sun.sunrise_yamakoti()
        if sunriseyk < self.julianday:
            return pglob.vara[(weekday + 1) % 7]
        else:
            return pglob.vara[weekday % 7]

    def nakshatra(self):
        return self.moon.nakshatra(self.ayanamsa)

    def init_yoga(self):
        yraw = ((self.moon.longitude() + self.sun.longitude()) % 360) / (13 + (20 / 60))
        remainder = yraw % 1  # remainder shows how much has elapsed
        elapsed = remainder * 12  # degrees elapsed
        remaining = 12 - elapsed  # degrees remaining
        return (yraw, elapsed, remaining)

    def yoga(self):
        return f"{self.yoga_int} {pglob.yogas[self.yoga_int - 1]}"

    def tithi_type(self):
        return pglob.tithi[(self.tithi() - 1) % 5]

    # above is the basic panchanga
    # below is other interesting information from the panchanga

    def tithi_degrees_elapsed(self):
        return self.telapsed

    def tithi_degrees_remaining(self):
        return self.tremaining

    def yoga_degrees_elapsed(self):
        return self.yelapsed

    def yoga_degrees_remaining(self):
        return self.yremaining

    def ayanamsa_name(self):
        if self.ayanamsa == 98:
            return "Dhruva GC mid-Mula equatorial coordinates"
        if self.ayanamsa == 99:
            return "Dhruva GC mid-Mula eclitpic coordinates"
        if self.ayanamsa == 100:
            return "Tropical Krittika 28 equal nakshatras"
        if self.ayanamsa == 101:
            return "My Dhruva GC equatorial non-ayanamsha"
        return swe.get_ayanamsa_name(self.ayanamsa)

    # next next moon and next full moon
    # its not techincally panchanga
    # but i need the sun and the moon and the tithi
    # which is all in the panchanga already

    def next_new_moon(self):
        """
        return the JulianDay of the new moon that comes after
        self.julianday
        """
        if (
            self.tithi() != 30
        ):  # if the tithi isnt 30, it cant be a new moon, so go forward 8 hours
            return Panchanga(self.shift("f", "hour", 8),ayanamsa=self.ayanamsa).next_new_moon()
        if abs(round(self.sun.longitude() - self.moon.longitude(), 4)) <= 0.0001:
            return self
        elapsed = self.tithi_degrees_elapsed()
        remaining = self.tithi_degrees_remaining()
        # if there are more than x degrees remaining, check a time y forward
        if remaining > 6:
            return Panchanga(self.shift("f", "hour", 8),ayanamsa=self.ayanamsa).next_new_moon()
        elif remaining > 3:
            return Panchanga(self.shift("f", "hour", 4),ayanamsa=self.ayanamsa).next_new_moon()
        elif remaining > 1:
            return Panchanga(self.shift("f", "minute", 30),ayanamsa=self.ayanamsa).next_new_moon()
        elif remaining > 0.5:
            return Panchanga(self.shift("f", "minute", 15),ayanamsa=self.ayanamsa).next_new_moon()
        elif remaining > 0.1:
            return Panchanga(self.shift("f", "minute", 1),ayanamsa=self.ayanamsa).next_new_moon()
        elif remaining > 0.01:
            return Panchanga(self.shift("f", "second", 1),ayanamsa=self.ayanamsa).next_new_moon()
        elif remaining < 0.001:
            return Panchanga(self.shift("f", "second", 1 / 4),ayanamsa=self.ayanamsa).next_new_moon()
        else:
            return Panchanga(self.shift("f", "second", 1),ayanamsa=self.ayanamsa).next_new_moon()

    def next_full_moon_loop(self):
        test = self
        #n=0
        while True:
            #n+=1
            #print(f"loop {n}")
            #print(f"tithi = {test.tithi()}")
            target = (test.sun.longitude() + 180) % 360
            # full moon is at the end of the 15th tithi
            if test.tithi() != 15:
                test = Panchanga(test.shift("f", "hours", 8))
                continue
            diff = abs(test.moon.longitude() - target)
            if diff > 16:
                test = Panchanga(test.shift("f", "day", 1))
                continue
            elif diff > 5 and diff <= 16:
                test = Panchanga(test.shift("f", "hours", 4))
                continue
            elif diff > 1 and diff <= 5:
                test = Panchanga(test.shift("f", "hours", 1))
                continue
            elif diff > .5 and diff <= 1:
                test = Panchanga(test.shift("f", "hours", 1/2))
                continue
            elif diff > .25 and diff <= .5:
                test = Panchanga(test.shift("f", "hours", 1/8))
                continue
            elif diff > .1 and diff <= .25:
                test = Panchanga(test.shift("f", "mins", 5))
                continue
            elif diff > .01 and diff <= .1:
                test = Panchanga(test.shift("f", "mins", 1/4))
                continue
            elif diff > .001 and diff <= .01:
                test = Panchanga(test.shift("f", "secs", 1/2))
                continue
            elif diff <= .0001:
                return test
            else:
                test = Panchanga(test.shift("f", "secs", 1/8))
                continue

    def next_full_moon_recursive(self):
        #print("finding next full moon recursively")
        if self.tithi() != 15:
            return Panchanga(self.shift("f", "hours", 8)).next_full_moon()
        target = (self.sun.longitude() + 180) % 360
        diff = abs(self.moon.longitude() - target)
        if diff > 16:  # at least six more degrees until a full moon
            # moon moves about 1 degree/2 hours, so lets move it 5 degrees forward => 10 hours
            #print("going forward by 1 day")
            return Panchanga(self.shift("f", "days", 1)).next_full_moon()
        elif diff > 5 and diff <= 16:
            #print("going forward by 4 hours")
            return Panchanga(self.shift("f", "hours", 4)).next_full_moon()
        elif diff > 1 and diff <= 5:
            #print("going forward by .5 hour")
            return Panchanga(self.shift("f", "hours", 1)).next_full_moon()
        elif diff > .5 and diff <= 1:
            # moon is between 1 and 3 degrees from full, so move forward 1 degree
            #print("going forward by .5 hour")
            return Panchanga(self.shift("f", "hours", 1/2)).next_full_moon()
        elif diff > 0.25 and diff <= .5:
            # moon is between .1 and  1 degree from full, so move foward about .1 degrees
            #print("going forward by 1 minute")
            return Panchanga(self.shift("f", "hours", 1/8)).next_full_moon()
        elif diff > 0.1 and diff <= 0.25:
            # moon is between .01 and .1 degree from full, so move forward about .01 degrees
            #print("going forward by 5 seconds")
            return Panchanga(self.shift("f", "mins", 5)).next_full_moon()
        elif diff > 0.01 and diff <= 0.1:
            #print("going forward by 1/2 seconds")
            return Panchanga(self.shift("f", "mins", 1/4)).next_full_moon()
        elif diff > 0.001 and diff <= 0.01:
            #print("going forward by 1/2 seconds")
            return Panchanga(self.shift("f", "seconds", 1/2)).next_full_moon()
        elif diff <= .0001:
            return self
        else:
            #print("going forward by 1/4 seconds")
            return Panchanga(self.shift("f", "seconds", 1/8)).next_full_moon()

    next_full_moon = next_full_moon_loop
