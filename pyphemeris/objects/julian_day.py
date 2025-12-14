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

import constants as const
import utils

nowtime = time.gmtime()
nowjdfloat = utils.tmod_to_jd(nowtime)

class JulianDay:
    """
    takes a float representing a julian day
    or (year,month,day,hour)
    any arguments not given are filled by the current time
    """
    # time units in julian days
    onedayjd = 1
    oneyearjd = onedayjd * 360
    onemonthjd = onedayjd * 30
    onehrjd = onedayjd / 24
    oneminjd = onehrjd / 60
    onesecjd = oneminjd / 60

    def __init__(self, jd=nowjdfloat, utcoffset=const.utcoffset, timezone=const.timezone):
        """
        initialize JulianDay class
        :jd - can be a float or a tuple(year, month, day, decimal_time)
        :utcoffset - an integer
        :timezone - a string representing the timezone
        """
        if isinstance(jd, float):
            self.jd = jd
        elif isinstance(jd, tuple):
            self.jd = swe.julday(jd[0], jd[1], jd[2], jd[3])
        self.datetime = swe.revjul(self.jd)
        self.utcoffset = utcoffset
        self.timezone = timezone
        self.usrdatetime = self.usrdt()

    def __str__(self):
        return f"{self.date()} at {self.time()}\n{self.usrdate()} at {self.usrtime()}\n{self.jd}"

    def __lt__(self, jd2):
        return self.jd < jd2.jd

    def indent_print(self, n=1):
        """
        print like with __str__, but indenting each line n times
        """
        tab = utils.mktab(n)
        print(f"{tab}{self.date()} at {self.time()}\n{tab}{self.usrdate()} at {self.usrtime()}\n{tab}{self.jd}")

    def date(self):
        return f"{utils.date2str(self.datetime)}"

    def time(self):
        return f"{utils.time2str(utils.dec2dms(self.datetime[3]))} UTC"

    def timedate(self):
        return f"{utils.time2str(utils.dec2dms(self.datetime[3]))} UTC on {utils.date2str(self.datetime)}"

    def year(self):
        return int(self.datetime[0])

    def hour(self):
        return float(self.datetime[3])

    def usrdate(self):
        return f"{utils.date2str(self.usrdatetime)}"

    def usrtime(self):
        return f"{utils.time2str(utils.dec2dms(self.usrdatetime[3]))} {self.timezone}"

    def usrtimedate(self):
        return f"{utils.time2str(utils.dec2dms(self.usrdatetime[3]))} {self.timezone} on {utils.date2str(self.usrdatetime)}"

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
            sf = sf * self.onesecjd
        elif unit.startswith("m"):
            sf = sf * self.oneminjd
        elif unit.startswith("h"):
            sf = sf * self.onehrjd
        elif unit.startswith("d"):
            sf = sf * self.onedayjd
        elif unit.startswith("y"):
            sf = sf * self.oneyearjd
        else:
            print("given unit not recognized")
        return JulianDay(self.jd + (number * sf))

    def usrdt(self):
        """
        transform utc time into user specified time with self.utcoffset and timezone string
        return a tuple (year,month,day,hour)
        an annoying function because i just had to brute force check everything by hand
        not sure else how to do it?
        probably there are some edge cases that will be wrong with this function
        """
        usrhr = self.datetime[3] + self.utcoffset
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
