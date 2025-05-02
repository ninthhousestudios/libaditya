import swisseph as swe
import time
import pyphglobals as pglob
import pyphutils as putil

nowtime = time.gmtime()
nowjdfloat = putil.tmod_to_jd(nowtime)

"""
classes take the present as a default
other defaults come directly from pyphglobals
e.g., latitude,longitude,place name,etc.
change them there if you want to change them
most values can also be toggled from being displayed

for boolean values, the flag by itself toggles the display on that usage
the default can be changed in pyphglobals

for non-boolean values, the flag can have a value, which changes the value
of that variable for that usage

if .t or .T is passed to a non-boolean flag, it will toggle the display of that
variable for that run
...maybe, if i decide to implement it; not really hard, probably, just tedious

"""


class JulianDay:
    """
    takes a float representing a julian day
    or (year,month,day,hour)
    any arguments not given are filled by the current time
    """

    def __init__(self, jd=nowjdfloat):
        if isinstance(jd, float):
            self.jd = jd
        elif isinstance(jd, tuple):
            self.jd = swe.julday(jd[0], jd[1], jd[2], jd[3])
        self.datetime = swe.revjul(self.jd)
        self.usrdatetime = self.usrdt()

    def __str__(self):
        return f"{self.date()} at {self.time()}\n{self.usrdate()} at {self.usrtime()}\n{self.jd}"

    def __lt__(self, jd2):
        return self.jd < jd2.jd

    def date(self):
        return f"{putil.date2str(self.datetime)}"

    def time(self):
        return f"{putil.time2str(putil.dec2dms(self.datetime[3]))} utc"

    def timedate(self):
        return f"{putil.time2str(putil.dec2dms(self.datetime[3]))} utc on {putil.date2str(self.datetime)}"

    def year(self):
        return int(self.datetime[0])

    def hour(self):
        return float(self.datetime[3])

    def usrdate(self):
        return f"{putil.date2str(self.usrdatetime)}"

    def usrtime(self):
        return f"{putil.time2str(putil.dec2dms(self.usrdatetime[3]))} {pglob.timezone}"

    def usrtimedate(self):
        return f"{putil.time2str(putil.dec2dms(self.usrdatetime[3]))} {pglob.timezone} on {putil.date2str(self.usrdatetime)}"

    def midnightjd(self):
        """return the jd that is at midnight of this JulianDay's calendar day"""
        return swe.julday(self.datetime[0], self.datetime[1], self.datetime[2], 0)

    def shift(self, dir, unit, number):
        """
        shift the julianday in 'dir'ection 'f'orward or 'b'ackward
        by number units, 'second','minute','hour','day','month','year'
        """
        sf = 1
        if dir == "b":
            sf = -1
        elif unit == "second":
            sf = sf * pglob.onesecjd
        elif unit == "minute":
            sf = sf * pglob.oneminjd
        elif unit == "hour":
            sf = sf * pglob.onehrjd
        elif unit == "day":
            sf = sf * pglob.onedayjd
        elif unit == "year":
            sf = sf * pglob.oneyearjd
        else:
            print("given unit not recognized")
        return JulianDay(self.jd + (number * sf))

    def usrdt(self):
        """
        transform utc time into user specified time with pglob.utcoffset and timezone string
        return a tuple (year,month,day,hour)
        an annoying function because i just had to brute force check everything by hand
        not sure else how to do it?
        probably there are some edge cases that will be wrong with this function
        """
        usrhr = self.datetime[3] + pglob.utcoffset
        usrday = self.datetime[2]
        usrmonth = self.datetime[1]
        usryear = self.datetime[0]
        # check what other fields we need to change
        # fix hour first
        if usrhr < 0:  # the day before
            usrday = usrday - 1
            usrhr = usrhr % 24
        if usrhr >= 24:  # the day after
            usrday = self.datetime[2] + 1
            usrhr = usrhr % 24

        # now check the day to make sure the month didn't change
        usrmonth = self.datetime[1]
        if usrday > 31:  # day is more than 31, so increase month by one
            usrday = 1
            usrmonth += 1
            if usrmonth > 12:
                usrmonth = 1
                usryear += 1
        if usrday < 1:
            usrmonth = self.datetime[1] - 1
            if usrmonth in [1, 3, 5, 7, 8, 10, 12]:  # in a month with 31 days
                usrday = 31
            elif usrmonth == 2:  # february
                if self.datetime[0] % 4 == 0:  # a leap year
                    usrday = 29
                else:
                    usrday = 28
            elif usrmonth < 1:
                usrday = 31
                usryear -= 1
                usrmonth = 12
            else:
                usrday == 30
        # now check the month to make sure the year didn't change
        if self.datetime[1] > 12:
            # month should have been changed above, lets change year
            usryear = self.datetime[0] + 1
        if self.datetime[1] < 1:
            usryear = self.datetime[0] - 1

        return (usryear, usrmonth, usrday, usrhr)


class Location:
    def __init__(
        self,
        lat=pglob.lat,
        long=pglob.long,
        alt=pglob.alt,
        placename=pglob.placename,
        timezone=pglob.timezone,
    ):
        self.lat = lat
        self.long = long
        self.alt = alt
        self.placename = placename
        self.timezone = timezone

    def __str__(self):
        return f"{self.placename} at ({self.lat},{self.long})\nelevation {self.alt} m\ntimezone: {self.timezone}"

    def place(self):
        return f"{self.placename} ({self.lat},{self.long})"

    def risetrans_location(self):
        return (self.long, self.lat, self.alt)


Yamakoti = Location(0, 165.76666666666668, 0, "Yamakoti", "ykt")


class Planet:
    """
    this class has information and functions related to planets
    each Planet takes a planet number and a JulianDay class
    """

    def __init__(self, pnumber, julianday=JulianDay()):
        self.pnumber = pnumber
        self.planet_name = swe.get_planet_name(pnumber)
        self.julianday = julianday  # the JulianDay class of this planet
        self.jd = self.julianday.jd
        self.coords = self.get_coords()

    def __str__(self):
        return f"{self.planet_name} on {self.julianday}"

    def get_coords(self, sysflg=pglob.ECL):
        """
        return swe.calc_ut tuple for coords of Planet at time self.jd
        sysflg tells what kind of coordinates: ECL,EQU,HELIO,BARY
        """
        return list(swe.calc_ut(self.jd, self.pnumber, swe.FLG_SPEED | sysflg)[0])

    def longitude(self):
        return self.coords[0]

    # rising time of this planet on the calendar day of self.julianday
    # rs is the swe flag that indicates rise or set
    def riseset(self, rs, location=Location()):
        return JulianDay(
            swe.rise_trans(
                self.julianday.jd,
                self.pnumber,
                rs | swe.BIT_HINDU_RISING,
                location.risetrans_location(),
            )[1][0]
        )

    def daily_motion(self, sysflag=pglob.ECL):
        """
        return daily motion in degress that the planet traverses
        in the next 24 hours from self.julianday
        """
        return (
            (swe.calc_ut(self.jd + 1, self.pnumber, sysflag)[0][0])
            - (swe.calc_ut(self.jd, self.pnumber, sysflag)[0][0])
        )

    def init_nakshatra(self, ayanamsa=pglob.ayanamsa):
        if ayanamsa == 98:
            return self.init_dhruvequ()
        swe.set_sid_mode(ayanamsa)
        sidlong = swe.calc_ut(self.julianday.jd, self.pnumber, swe.FLG_SIDEREAL)[0][0]
        return sidlong, putil.nakshatra_index(sidlong)

    def init_dhruvequ(self):
        swe.set_sid_mode(36)
        aval = swe.get_ayanamsa(self.jd)
        equlong = swe.calc_ut(self.jd, self.pnumber, swe.FLG_EQUATORIAL)[0][0]
        sidlong = (equlong - aval) % 360
        return sidlong, putil.nakshatra_index(sidlong)

    def nakshatra_table_list(self, ayanamsa=pglob.ayanamsa):
        sidlong, nindex = self.init_nakshatra(ayanamsa)
        pname = self.planet_name
        nname = pglob.nakshatra[nindex]
        in_nak_long = round(sidlong - (nindex * pglob.nak), 1)
        percent_elapsed = round((in_nak_long / pglob.nak) * 100, 2)
        elapsed = f"{in_nak_long} deg ({percent_elapsed} %)"
        return list((pname, nname, elapsed))

    def nakshatra(self, ayanamsa=pglob.ayanamsa):
        sidlong, nindex = self.init_nakshatra(ayanamsa)
        return pglob.nakshatra[nindex]

    def table_list(self, sysflg=pglob.ECL):
        """
        add planet name to self.get_coords(sysflg)
        and return a list 7 elements long, name first, values after
        """
        coord_list = list(self.get_coords(sysflg))
        coord_list[0] = pglob.sign_func(coord_list[0])  # signize longitude if desired
        # round other values if desired
        for i in range(5):
            coord_list[i + 1] = pglob.round_func(float(coord_list[i + 1]))
        return [self.planet_name] + coord_list


class Cusps:
    """
    calculate house cusps for a certain place lat,long (NE both positive)
    with a certain house system hsys at a time JulianDay
    hsys is a letter; swisseph actually needs it as a byte, so it is encoded
    with utf-8...you cant just pass a python string 'R';

    however, the argument for this function should be a python string; so is the
    default in pyphglobals; __init__ takes care of the encoding

    Campanus is the default house system, 'C'
    """

    def __init__(self, hsys=pglob.hsys, location=Location(), julianday=JulianDay()):
        self.hsys = hsys.encode()
        self.location = location
        self.julianday = julianday
        self.jd = self.julianday.jd
        self.hname = swe.house_name(self.hsys)
        self.cusps = self.init_cusps()  # a 12 tuple of cusp points

    def __str__(self):
        """
        the function swe.houses(time,lat,long,hsys) take lat first
        """
        return f"Getting cusps for {self.location.placename} ({self.location.lat},{self.location.long}) on {self.julianday} using house system {self.hname}\n{self.cusps}"

    def init_cusps(self):
        """
        find our house cusps
        cusps will be a 12-tuple with cusps 1-12
        """
        self.cusps = swe.houses(
            self.julianday.jd, self.location.lat, self.location.long, self.hsys
        )[0]

    def house_name(self):
        return self.hname

    def cusps_nakshatras(self, ayanamsa=pglob.ayanamsa):
        if ayanamsa == 98:
            return self.cusps_dhruvequ()
        swe.set_sid_mode(ayanamsa)
        aval = swe.get_ayanamsa(self.jd)
        sidcusps = []
        for cusp in self.cusps:
            sidcusps.append(cusp - aval)
        cusps_nakshatras = []
        for sidcusp in sidcusps:
            cusps_nakshatras.append(pglob.nakshatra[putil.nakshatra_index(sidcusp)])
        return cusps_nakshatras

    def cusps_dhruvequ(self):
        swe.set_sid_mode(36)
        aval = swe.get_ayanamsa(self.jd)
        equcusps = []  # get equatorial coordinates of cusps from ecliptic ones in self.cusps
        for cusp in self.cusps:
            equcusps.append(
                swe.cotrans(
                    (cusp, 0, 1), putil.ecliptic_obliquity(self.julianday.year())
                )[0]
            )
        sidcusps = []  # longitude of cusps that will be passed to nakshatra_index
        for i in range(len(equcusps)):
            sidcusps.append((equcusps[i] - aval) % 360)
        cusps_nakshatras = []
        for sidcusp in sidcusps:
            cusps_nakshatras.append(pglob.nakshatra[putil.nakshatra_index(sidcusp)])
        return cusps_nakshatras
