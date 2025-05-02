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
                self.julianday.midnightjd(),
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
        self.coords[0] = (self.coords[0] - 180) % 360

    def get_coords(self, sysflg=pglob.ECL):
        """
        return swe.calc_ut tuple for coords of Planet at time self.jd
        sysflg tells what kind of coordinates: ECL,EQU,HELIO,BARY
        """
        coords = list(swe.calc_ut(self.jd, self.pnumber, swe.FLG_SPEED | sysflg)[0])
        return [(coords[0] - 180) % 360] + coords[1:]

    def init_nakshatra(self, ayanamsa=pglob.ayanamsa):
        if ayanamsa == 98:
            return self.init_dhruvequ()
        swe.set_sid_mode(ayanamsa)
        sidlong = swe.calc_ut(self.julianday.jd, self.pnumber, swe.FLG_SIDEREAL)[0][0]
        sidlong = (sidlong - 180) % 360
        return sidlong, putil.nakshatra_index(sidlong)

    def init_dhruvequ(self):
        swe.set_sid_mode(36)
        aval = swe.get_ayanamsa(self.jd)
        equlong = swe.calc_ut(self.jd, self.pnumber, swe.FLG_EQUATORIAL)[0][0]
        sidlong = (equlong - aval) % 360
        sidlong = (sidlong - 180) % 360
        return sidlong, putil.nakshatra_index(sidlong)


class Panchanga(JulianDay):
    def __init__(self, julianday=JulianDay()):
        super().__init__(julianday.jd)
        self.julianday = julianday
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
        return self.moon.nakshatra()

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
