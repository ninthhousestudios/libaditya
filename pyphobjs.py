import swisseph as swe
import time
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
        self.planet_name = "Rahu"


class Ketu(Planet):
    def __init__(self, julianday=JulianDay()):
        super().__init__(pglob.true_node, julianday)
        self.planet_name = "Ketu"
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
    def __init__(self, julianday=JulianDay(), ayanamsa=98):
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
            return Panchanga(self.shift("f", "hour", 8)).next_new_moon()
        if abs(round(self.sun.longitude() - self.moon.longitude(), 4)) <= 0.0001:
            return self
        elapsed = self.tithi_degrees_elapsed()
        remaining = self.tithi_degrees_remaining()
        # if there are more than x degrees remaining, check a time y forward
        if remaining > 6:
            return Panchanga(self.shift("f", "hour", 8)).next_new_moon()
        elif remaining > 3:
            return Panchanga(self.shift("f", "hour", 4)).next_new_moon()
        elif remaining > 1:
            return Panchanga(self.shift("f", "minute", 30)).next_new_moon()
        elif remaining > 0.5:
            return Panchanga(self.shift("f", "minute", 15)).next_new_moon()
        elif remaining > 0.1:
            return Panchanga(self.shift("f", "minute", 1)).next_new_moon()
        elif remaining > 0.01:
            return Panchanga(self.shift("f", "second", 1)).next_new_moon()
        elif remaining < 0.001:
            return Panchanga(self.shift("f", "second", 1 / 4)).next_new_moon()
        else:
            return Panchanga(self.shift("f", "second", 1)).next_new_moon()

    def next_full_moon(self):
        if self.tithi() != 15:  # if the tithi is not 15 it cant be a full moon
            return Panchanga(self.shift("f", "hours", 12)).next_full_moon()
        # now tithi = 15, so we can possibly be at the full moon
        # full moon is when (lsun+180)%360==lmoon
        test = (round(self.sun.longitude(), 3) - 180) % 360
        if test == round(self.moon.longitude(), 3):
            return self
        remainder = abs(self.moon.longitude() - test)
        if remainder > 6:  # at least six more degrees until a full moon
            # moon moves about 1 degree/2 hours, so lets move it 5 degrees forward => 10 hours
            return Panchanga(self.shift("f", "hours", 4)).next_full_moon()
        elif remainder > 3:
            # so moon is between 3 and 6 degrees from full, so lets move it 2 degrees
            return Panchanga(self.shift("f", "hours", 1)).next_full_moon()
        elif remainder > 1:
            # moon is between 1 and 3 degrees from full, so move forward 1 degree
            return Panchanga(self.shift("f", "hours", 0.5)).next_full_moon()
        elif remainder > 0.1:
            # moon is between .1 and  1 degree from full, so move foward about .1 degrees
            return Panchanga(self.shift("f", "minutes", 1)).next_full_moon()
        elif remainder > 0.01:
            # moon is between .01 and .1 degree from full, so move forward about .01 degrees
            return Panchanga(self.shift("f", "seconds", 5)).next_full_moon()
        elif remainder > 0.001:
            return Panchanga(self.shift("f", "seconds", 1 / 2)).next_full_moon()
        else:
            return Panchanga(self.shift("f", "seconds", 1)).next_full_moon()
