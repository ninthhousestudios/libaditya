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

import time

from libaditya import utils

GREGORIAN_REFORM_JD = 2299160.5


def _cal_flag(jd_val):
    return swe.JUL_CAL if jd_val < GREGORIAN_REFORM_JD else swe.GREG_CAL


def _cal_flag_ymd(year, month, day):
    if year < 1582 or (year == 1582 and (month < 10 or (month == 10 and day < 15))):
        return swe.JUL_CAL
    return swe.GREG_CAL


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
    oneyearjd = onedayjd * 365.25
    onemonthjd = onedayjd * 30
    onehrjd = onedayjd / 24
    oneminjd = onehrjd / 60
    onesecjd = oneminjd / 60

    def __init__(self, jd=nowjdfloat, utcoffset=0, timezone="UTC"):
        """
        initialize JulianDay class
        :jd - can be a float or a tuple(year, month, day, decimal_time)
        :utcoffset - a float
        :timezone - a string representing the timezone
        """
        if isinstance(jd, float) or isinstance(jd, int):
            self.jd = jd
        elif isinstance(jd, tuple):
            self.jd = swe.julday(jd[0], jd[1], jd[2], jd[3], _cal_flag_ymd(jd[0], jd[1], jd[2]))
        elif jd == "now":
            nowtime = time.gmtime()
            jd = utils.tmod_to_jd(nowtime)
            self.jd = jd
        self.datetime = swe.revjul(self.jd, _cal_flag(self.jd))
        self.utcoffset = float(utcoffset)
        self._timezone = self.mktimezone(timezone)
        self.usrdatetime = self.usrdt()

    def __repr__(self):
        return str(self.jd)

    def __str__(self):
        if self.utcoffset == 0:
            return f"{self.date()} at {self.time()}\n{self.jd}"
        else:
            return f"{self.date()} at {self.time()}\n{self.usrdate()} at {self.usrtime()}\n{self.jd}"

    def __lt__(self, jd2):
        return self.jd < jd2.jd

    def __le__(self, jd2):
        return self.jd <= jd2.jd

    def __gt__(self, jd2):
        return self.jd > jd2.jd

    def __ge__(self, jd2):
        return self.jd >= jd2.jd

    def T(self):
        """
        T = (Julian Day - 2451545) / 36525
        for use in cheshta bala calculations
        """
        return (self.jd_number() - 2451545) / 36525

    def indent_print(self, n=1) -> None:
        """
        print like with __str__, but indenting each line n times
        """
        tab = utils.mktab(n)
        print(
            f"{tab}{self.date()} at {self.time()}\n{tab}{self.usrdate()} at {self.usrtime()}\n{tab}{self.jd}"
        )

    def indent_print_str(self, n=1) -> str:
        """
        print like with __str__, but indenting each line n times
        """
        tab = utils.mktab(n)
        return f"{tab}{self.date()} at {self.time()}\n{tab}{self.usrdate()} at {self.usrtime()}\n{tab}{self.jd}"

    def mktimezone(self, timezone="UTC") -> str:
        """
        this only kind of timezone libaditya uses is UTC and UTC +/- (f: float)
        """
        sign = ""
        appendix = ""
        if self.utcoffset > 0:
            sign = "+"
        if self.utcoffset == 0 or timezone != "UTC":
            appendix = ""
        else:
            appendix = sign + f"{round(self.utcoffset, 2)}"
        return timezone + appendix

    def timezone(self):
        return self._timezone

    def jd_number(self):
        return self.jd

    def date(self, tz="utc"):
        if tz != "utc":
            return f"{utils.date2str(self.usrdatetime)}"
        else:
            return f"{utils.date2str(self.datetime)}"

    def time(self, tz="utc", print_tz=True, debug=""):
        if debug:
            debug=f" ({self.day(tz)})"
        ptz = ""
        ret = ""
        if tz != "utc":
            if print_tz: 
                ptz = " " + self._timezone
            ret += f"{utils.time2str(utils.dec2dms(self.usrdatetime[3]))}{ptz}"
        else:
            if print_tz: 
                ptz = " UTC"
            ret += f"{utils.time2str(utils.dec2dms(self.datetime[3]))}{ptz}"
        return ret + debug

    def timedate(self):
        return f"{utils.time2str(utils.dec2dms(self.datetime[3]))} UTC on {utils.date2str(self.datetime)}"

    def year(self, tz="utc"):
        if tz != "utc:":
            return self.usryear()
        else:
            return int(self.datetime[0])

    def month(self, tz="utc"):
        if tz != "utc:":
            return self.usrmonth()
        else:
            return int(self.datetime[1])

    def day(self, tz="utc"):
        if tz != "utc":
            return self.usrday()
        else:
            return int(self.datetime[2])

    def hour(self, tz="utc"):
        if tz != "utc":
            return self.usrhour()
        else:
            return float(self.datetime[3])

    def age(self, datejd):
        """
        distance in years between self and date
        """
        return (datejd-self.jd)/365.24221

    def current_age(self):
        """
        distance in years between self and date
        """
        nowtime = time.gmtime()
        jd = utils.tmod_to_jd(nowtime)
        return (jd-self.jd)/self.oneyearjd

    def current_age_days(self):
        """
        distance in years between self and date
        """
        return self.current_age()*365.25

    def usrdate(self):
        return f"{utils.date2str(self.usrdatetime)}"

    def usryear(self):
        return int(self.usrdatetime[0])

    def usrmonth(self):
        return int(self.usrdatetime[1])

    def usrday(self):
        return int(self.usrdatetime[2])

    def usrhour(self):
        return float(self.usrdatetime[3])

    def usrtime(self):
        return f"{utils.time2str(utils.dec2dms(self.usrdatetime[3]))} {self._timezone}"

    def usrtimedate(self):
        return f"{utils.time2str(utils.dec2dms(self.usrdatetime[3]))} {self._timezone} on {utils.date2str(self.usrdatetime)}"

    def midnightjd(self):
        """return the jd that is at midnight of this JulianDay's calendar day"""
        return swe.julday(self.datetime[0], self.datetime[1], self.datetime[2], 0, _cal_flag(self.jd))

    def midnightJD(self):
        """return the jd that is at midnight of this JulianDay's calendar day"""
        return JulianDay(swe.julday(self.datetime[0], self.datetime[1], self.datetime[2], 0, _cal_flag(self.jd)),self.utcoffset)

    def usr_midnightJD(self):
        """return the jd at midnight of this JulianDay's LOCAL calendar day

        ``midnightJD`` anchors on ``self.datetime``, the UTC calendar day.
        Anything that ALSO reads ``usrday()``/``usrmonth()`` must anchor here
        instead, or the two disagree by a whole day whenever the local and UTC
        dates differ — which is every evening west of Greenwich and every
        early morning east of it. Added 2026-07-27 for SPEC-COT-001 E-6.
        """
        y, m, d = (int(self.usrdatetime[0]), int(self.usrdatetime[1]),
                   int(self.usrdatetime[2]))
        # julday() on the LOCAL Y/M/D gives local midnight expressed as though
        # it were UTC; subtracting the offset turns it back into a real instant
        # (usrdt() adds the offset going the other way).
        usr_midnight = swe.julday(y, m, d, 0, _cal_flag_ymd(y, m, d))
        return JulianDay(usr_midnight - self.utcoffset / 24,
                         self.utcoffset, self.timezone())

    def next_midnightjd(self):
        """return the jd that is at next_midnight of this JulianDay's calendar day"""
        return swe.julday(self.datetime[0], self.datetime[1], self.datetime[2], 0, _cal_flag(self.jd))+1

    def next_midnightJD(self):
        """return the jd that is at next_midnight of this JulianDay's calendar day"""
        return JulianDay(swe.julday(self.datetime[0], self.datetime[1], self.datetime[2], 0, _cal_flag(self.jd))+1,self.utcoffset,self.timezone())

    def ecliptic_obliquity(self):
        return swe.calc(self.jd, swe.ECL_NUT)[0][0]

    def shift(self, dir, unit, number):
        """
        shift the julianday in 'dir'ection 'f'orward or 'b'ackward
        by number units, 'second','minute','hour','day','month','year'
        """
        sf = 1  # scale factor
        if dir.startswith("b"):
            sf = -1
        if unit.startswith("s"):
            sf = sf * self.onesecjd
        elif unit.startswith("min"):
            sf = sf * self.oneminjd
        elif unit.startswith("mon"):
            sf = sf * self.onemonthjd
        elif unit.startswith("h"):
            sf = sf * self.onehrjd
        elif unit.startswith("d"):
            sf = sf * self.onedayjd
        elif unit.startswith("y"):
            sf = sf * self.oneyearjd
        else:
            print("given unit not recognized")
        return JulianDay(self.jd + (number * sf),self.utcoffset,self._timezone)

    def usrdt(self):
        """
        transform utc time into user specified time with self.utcoffset and timezone string
        return a tuple (year,month,day,hour)
        """
        usr_jd = self.jd + self.utcoffset / 24
        return swe.revjul(usr_jd, _cal_flag(usr_jd))
