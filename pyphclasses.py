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
import pyphglobals as pglob
import pyphutils as putil

nowtime = time.gmtime()
nowjdfloat = putil.tmod_to_jd(nowtime)

pglob.init_names()

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

    def indent_print(self, n=1):
        """
        print like with __str__, but indenting each line n times
        """
        tab = ""
        for i in range(0,n):
            tab += "\t"
        print(f"{tab}{self.date()} at {self.time()}\n{tab}{self.usrdate()} at {self.usrtime()}\n{tab}{self.jd}")

    def date(self):
        return f"{putil.date2str(self.datetime)}"

    def time(self):
        return f"{putil.time2str(putil.dec2dms(self.datetime[3]))} UTC"

    def timedate(self):
        return f"{putil.time2str(putil.dec2dms(self.datetime[3]))} UTC on {putil.date2str(self.datetime)}"

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

    def ecliptic_obliquity(self):
        return swe.calc(self.jd,swe.ECL_NUT)[0][0]

    def shift(self, dir, unit, number):
        """
        shift the julianday in 'dir'ection 'f'orward or 'b'ackward
        by number units, 'second','minute','hour','day','month','year'
        """
        sf = 1 # scale factor
        if dir.startswith("b"):
            sf = -1
        if unit.startswith("s"):
            sf = sf * pglob.onesecjd
        elif unit.startswith("m"):
            sf = sf * pglob.oneminjd
        elif unit.startswith("h"):
            sf = sf * pglob.onehrjd
        elif unit.startswith("d"):
            sf = sf * pglob.onedayjd
        elif unit.startswith("y"):
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
        self.lat = float(lat)
        self.long = float(long)
        self.alt = float(alt)
        self.placename = placename
        self.timezone = timezone

    def __str__(self):
        return f"{self.placename} at ({self.lat},{self.long})\nelevation {self.alt} m\ntimezone: {self.timezone}"

    def place(self):
        return f"{self.placename} ({pglob.round_func(self.lat)},{pglob.round_func(self.long)})"

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
        self.planet_name = pglob.planets[pnumber]
        self.julianday = julianday  # the JulianDay class of this planet
        self.jd = self.julianday.jd
        self.coords = self.get_coords()
        self.varga_long = 0 # for longitude in a varga if calculating

    def __str__(self):
        return f"{self.planet_name} on {self.julianday}"

    def get_coords(self, sysflg=pglob.ECL):
        """
        return swe.calc_ut tuple for coords of Planet at time self.jd
        sysflg tells what kind of coordinates: ECL,EQU,HELIO,BARY
        """
        return list(swe.calc_ut(self.jd, self.pnumber, swe.FLG_SPEED | sysflg)[0])

    def longitude(self, sysflg=pglob.ECL):
        return swe.calc_ut(self.jd, self.pnumber, sysflg)[0][0]

    def set_varga_long(self,long):
        self.varga_long = long

    def get_varga_long(self):
        return self.varga_long

    def sign_index(self, sysflg=pglob.ECL):
        return int(self.longitude(sysflg) / 30)

    def sign(self):
        return pglob.signs[self.sign_index()]

    def signize(self):
        return putil.yessignize(self.longitude())

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
        if ayanamsa == 99:
            return self.init_dhruvecl()
        if ayanamsa == 100:
            #print(f"returning {self.longitude(), int((self.longitude()/(360/28))%28)}")
            # second arg indexes into 28 equal tropical nakshatras, krittika at
            # ascending equinox
            return [self.longitude(), putil.nakshatra_tropkrt28_index(self.longitude())]
        if ayanamsa == 101:
            return self.init_my_dhruvequ()
        if ayanamsa == 102:
            return self.init_vedanga_jyotisha_ecliptic()
        if ayanamsa == 103:
            return self.init_vedanga_jyotisha_equatorial()
        if ayanamsa == 104:
            return self.init_my_dhruvecl()
        swe.set_sid_mode(ayanamsa)
        sidlong = swe.calc_ut(self.julianday.jd, self.pnumber, swe.FLG_SIDEREAL)[0][0]
        if self.planet_name == "Ketu":
            sidlong = (sidlong - 180) % 360
        return sidlong, putil.nakshatra_index(sidlong)

    def init_dhruvequ(self):
        swe.set_sid_mode(36)
        aval = swe.get_ayanamsa(self.jd)
        equlong = swe.calc_ut(self.jd, self.pnumber, swe.FLG_EQUATORIAL)[0][0]
        sidlong = (equlong - aval) % 360
        if self.planet_name == "Ketu":
            sidlong = (sidlong - 180) % 360
        return sidlong, putil.nakshatra_index(sidlong)

    def init_my_dhruvequ(self):
        gcequ=swe.fixstar(",SgrA*",self.jd, swe.FLG_EQUATORIAL)[0][0]
        mula=gcequ-(pglob.nak/2)
        ashvini=mula-(18*pglob.nak)
        equlong = swe.calc_ut(self.jd, self.pnumber, swe.FLG_EQUATORIAL)[0][0]
        if self.planet_name == "Ketu":
            equlong = (equlong - 180) % 360
        if equlong < ashvini:
            equlong+=360
        nindex=int((equlong-ashvini)/pglob.nak)
        return equlong-ashvini, nindex

    def init_my_dhruvecl(self):
        """
        use dhruva ecliptic nakshatra positions
        so find nakshatra boundaries on equator,
        translate them onto ecliptic,
        then index planets ecliptic longitude into that
        """
        gcequ=swe.fixstar(",SgrA*",self.jd, swe.FLG_EQUATORIAL)[0][0]
        mula=gcequ-(pglob.nak/2)
        ashvini=mula-(18*pglob.nak)
        long = self.longitude()
        # boundaries of nakhsatras along equator
        equbounds = putil.build_my_dhruvequ_bounds(gcequ)
        # translate these onto the ecliptic
        eo = self.julianday.ecliptic_obliquity()
        eclbounds = []
        for bound in equbounds:
            eclbounds.append(swe.cotrans((bound, 0, 1), eo)[0])
        # now index planets ecliptic longitude into this
        nindex = putil.dindex(long, eclbounds)
        return long, nindex

    def init_vedanga_jyotisha_ecliptic(self):
        """
        dhanishta begins at the winter solstice, i.e., 270 degrees ecliptic longitude
        this puts ashivini to start at 336+2/3 ecliptic longitude
        so our "ayanamsa" is 23+1/3, in order to line up with our nakshatra list
        but we have to added this; so that ashvini+ayanamsa=0
        """
        # aval = 23+1/3
        # this is how it is calculated
        aval = 360 - (270+5*pglob.nak)
        long = swe.calc_ut(self.jd, self.pnumber)[0][0]
        if self.planet_name == "Ketu":
            long = (long - 180) % 360
        nindex = int(((long+aval)%360)/pglob.nak)
        return (long+aval)%360, nindex

    def init_vedanga_jyotisha_equatorial(self):
        """
        dhanishta at the winter solstice, but equatorial nakshatras
        so find the equatorial longitude of the solstice, then
        determine nakshatras from there with equatorial planet longitudes
        """
        # equatorial longitude of the winter solstice, which i think will always be 270; do it anyway
        solequ = swe.cotrans((270,0,1),-self.julianday.ecliptic_obliquity())[0]
        aval = 360 - (solequ+5*pglob.nak)
        # equatorial longitude of this planet
        equlong = swe.calc_ut(self.jd, self.pnumber, swe.FLG_EQUATORIAL)[0][0]
        if self.planet_name == "Ketu":
            equlong = (equlong - 180) % 360
        nindex = int(((equlong+aval)%360)/pglob.nak)
        return (equlong+aval)%360, nindex


    def init_dhruvecl(self):
        swe.set_sid_mode(36)
        aval = swe.get_ayanamsa(self.jd)
        equlong = swe.calc_ut(self.jd, self.pnumber, swe.FLG_EQUATORIAL)[0][0]
        sidlong = (equlong - aval) % 360
        # now transform this equatorial (sidereal) longitude into ecliptic longitude
        eclsidlong = swe.cotrans(
            (sidlong, 0, 1), putil.ecliptic_obliquity(self.jd)
        )[0]
        if self.planet_name == "Ketu":
            eclsidlong = (eclsidlong - 180) % 360
        return eclsidlong, putil.dhruvecl_index(eclsidlong,self.jd)



    def nakshatra_table_list(self, ayanamsa=pglob.ayanamsa):
        sidlong, nindex = self.init_nakshatra(ayanamsa)
        pname = self.planet_name
        if ayanamsa == 100:
            nname = pglob.nakshatraeq[nindex]
            this_nak_length = 360/28
            in_nak_long = round(sidlong - (nindex * this_nak_length),1)
        elif ayanamsa == 99:
            eclbnds = putil.build_dhruvecl_boundaries(self.jd)
            nname = pglob.nakshatra[nindex]
            in_nak_long = round(sidlong - eclbnds[nindex], 1)
            this_nak_length = (
                eclbnds[nindex + 1]
                - eclbnds[nindex]
            )
        elif ayanamsa == 104:
            gcequ=swe.fixstar(",SgrA*",self.jd, swe.FLG_EQUATORIAL)[0][0]
            mula=gcequ-(pglob.nak/2)
            ashvini=mula-(18*pglob.nak)
            long = self.longitude()
            if self.planet_name == "Ketu":
                long = (long - 180) % 360
            # boundaries of nakhsatras along equator
            equbounds = putil.build_my_dhruvequ_bounds(gcequ)
            # translate these onto the ecliptic
            eo = self.julianday.ecliptic_obliquity()
            eclbnds = []
            for bound in equbounds:
                eclbnds.append(swe.cotrans((bound, 0, 1), eo)[0])
            nname = pglob.nakshatra[nindex]
            in_nak_long = round(sidlong - eclbnds[nindex], 1)
            this_nak_length = (
                eclbnds[(nindex + 1)%27]
                - eclbnds[nindex]
            )%360
        else:
            nname = pglob.nakshatra[nindex]
            in_nak_long = round(sidlong - (nindex * pglob.nak), 1)
            this_nak_length = pglob.nak
        percent_elapsed = round((in_nak_long / this_nak_length) * 100, 2)
        elapsed = f"{in_nak_long} deg ({percent_elapsed} %)"
        return list((pname, nname, elapsed))

    def nakshatra(self, ayanamsa=pglob.ayanamsa):
        sidlong, nindex = self.init_nakshatra(ayanamsa)
        if ayanamsa == 100:
            return pglob.nakshatraeq[nindex]
        else:
            return pglob.nakshatra[nindex]

    def table_list(self, sysflg=pglob.ECL):
        """
        add planet name to self.get_coords(sysflg)
        and return a list 7 elements long, name first, values after
        """
        coord_list = list(self.get_coords(sysflg))
        coord_list[0] = pglob.sign_func(coord_list[0])  # signize longitude if desired
        # added an indication to the planet name for retrograde
        if coord_list[3] < 0:
            self.planet_name += " (R)"
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

    def get_lagna(self):
        """returns ecliptic longitude of lagna"""
        return self.cusps[0]

    def cusps_nakshatras(self, ayanamsa=pglob.ayanamsa):
        if ayanamsa == 98:
            return self.cusps_dhruvequ()
        elif ayanamsa == 101:
            return self.my_dhruvequ_cusps()
        elif ayanamsa == 102:
            return self.vedanga_jyotisha_ecliptic_cusps()
        elif ayanamsa == 103:
            return self.vedanga_jyotisha_equatorial_cusps()
        elif ayanamsa == 104:
            # 104 is dhruva eclitpic, but havent implemented it yet, so use dhruva equatorial
            pglob.ayanamsa = 101
            return self.my_dhruvequ_cusps()
        else:
            swe.set_sid_mode(ayanamsa)
            aval = swe.get_ayanamsa(self.jd)
            sidcusps = []
            for cusp in self.cusps:
                sidcusps.append((cusp - aval) % 360)
            cusps_nakshatras = []
            for sidcusp in sidcusps:
                if ayanamsa == 99:
                    nindex = putil.dhruvecl_index(sidcusp, self.jd)
                elif ayanamsa == 100:
                    nindex = putil.nakshatra_tropkrt28_index(sidcusp)
                else:
                    nindex = putil.nakshatra_index(sidcusp)
                if ayanamsa == 100:
                    cusps_nakshatras.append(pglob.nakshatraeq[nindex])
                else:
                    cusps_nakshatras.append(pglob.nakshatra[nindex])
        return sidcusps, cusps_nakshatras

    def vedanga_jyotisha_ecliptic_cusps(self):
        """
        dhanishta begins at the winter solstice, i.e., 270 degrees ecliptic longitude
        this puts ashivini to start at 336+2/3 ecliptic longitude
        so our "ayanamsa" is 23+1/3, in order to line up with our nakshatra list
        """
        aval = 23+1/3
        cusps_nakshatras = []
        # cusp values to return in order to find in-cusp longitude
        retcusps = []
        for cusp in self.cusps:
            nindex = int(((cusp+aval)%360)/pglob.nak)
            cusps_nakshatras.append(pglob.nakshatra[nindex])
            retcusps.append((cusp+aval)%360)
        return retcusps, cusps_nakshatras

    def vedanga_jyotisha_equatorial_cusps(self):
        """
        dhanishta begins at the winter solstice, i.e., 270 degrees ecliptic longitude
        this puts ashivini to start at 336+2/3 ecliptic longitude
        so our "ayanamsa" is 23+1/3, in order to line up with our nakshatra list
        """
        # equatorial longitude of the winter solstice
        solequ = swe.cotrans((270,0,1),-self.julianday.ecliptic_obliquity())[0]
        aval = 23+1/3
        cusps_nakshatras = []
        retcusps = []
        for cusp in self.cusps:
            # equatorial longitude of this cusp
            equlong = swe.cotrans((cusp, 0, 1), -self.julianday.ecliptic_obliquity())[0]
            nindex = int(((equlong+aval)%360)/pglob.nak)
            cusps_nakshatras.append(pglob.nakshatra[nindex])
            retcusps.append((equlong+aval)%360)
        return retcusps, cusps_nakshatras

    def my_dhruvequ_cusps(self):
        gcequ=swe.fixstar(",SgrA*",self.jd, swe.FLG_EQUATORIAL)[0][0]
        mula=gcequ-(pglob.nak/2)
        ashvini=mula-(18*pglob.nak)
        equcusps = []  # get equatorial coordinates of cusps from ecliptic ones in self.cusps
        for cusp in self.cusps:
            equcusps.append(
                swe.cotrans(
                    (cusp, 0, 1), -putil.ecliptic_obliquity(self.jd)
                )[0]
            )
        cusps_nakshatras = []
        for cusp in equcusps:
            if cusp < ashvini:
                cusp+=360
            cusps_nakshatras.append(pglob.nakshatra[int((cusp-ashvini)/pglob.nak)])
        equcusps = [(cusp-ashvini)%360 for cusp in equcusps]
        return equcusps, cusps_nakshatras

    def cusps_dhruvequ(self):
        swe.set_sid_mode(36)
        aval = swe.get_ayanamsa(self.jd)
        equcusps = []  # get equatorial coordinates of cusps from ecliptic ones in self.cusps
        for cusp in self.cusps:
            equcusps.append(
                swe.cotrans(
                    (cusp, 0, 1), -putil.ecliptic_obliquity(self.jd)
                )[0]
            )
        sidcusps = []  # longitude of cusps that will be passed to nakshatra_index
        for i in range(len(equcusps)):
            sidcusps.append((equcusps[i] - aval) % 360)
        cusps_nakshatras = []
        for sidcusp in sidcusps:
            cusps_nakshatras.append(pglob.nakshatra[putil.nakshatra_index(sidcusp)])
        return cusps_nakshatras
