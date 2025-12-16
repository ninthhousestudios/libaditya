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

from libaditya import constants as const

def dms2dec(dms):
    """
    dms is a tuple (hour,minutes,seconds) that wants to be turned into a float
    """
    return dms[0] + (dms[1] / 60) + (dms[2] / 3600)

def signize(long,toround,names):
    """
    return a string with 360degree longitude long given with
    long (sign), with long being in the sign
    signs contains the signs to be used, which might be adityas
    """
    index = int((long % 360) / 30)  # mod 360 in case long=360...but it probably wouldnt with swe, right?
    if toround[0]:
        inlong = round(long % 30, toround[1])
    else:
        inlong = (long % 30)
    return f"{dec2dmsstr(inlong)} {names[index]}"


def intize_date(date):
    """
    take a string 'MM/DD/YYYY'
    and return a tuple of int (mm,dd,yyyy)
    """
    date = date.split('/')
    year = int(date[2]) 
    month = int(date[0])
    day = int(date[1])

    return (month, day, year)

def intize_time(time):
    """
    take a string 'HH:MM:SS'
    and return a float of that time
    """
    time = time.split(':')
    # if len == 2, HH:MM, otherwise, HH:MM:SS
    if len(time) == 2:
        return int(time[0]) + int(time[1]) / 60
    else:
        return int(time[0]) + int(time[1]) / 60 + int(time[2]) / 3600

def tmod_to_jd(now):
    """
    time a struct from the time module
    and convert it to julian day float
    """
    return swe.julday(
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour + now.tm_min / 60 + now.tm_sec / 3600,
    )

def date2str(date):
    """date is a revjul-tuple (year,month,day,hour); return a string 'month/day/year'"""
    return f"{date[1]:02d}/{date[2]:02d}/{date[0]:02d}"

def time2str(time):
    """time is a dec2dms tupel (deg,min,sec); returns a string 'HH:MM:SS'"""
    return f"{str(int(time[0])).zfill(2)}:{str(int(time[1])).zfill(2)}:{str(int(time[2])).zfill(2)}"

def mktab(n):
    tab = ""
    for i in range(0,n):
        tab += "\t"
    return tab

def dec2dms(dd):
    """dd is a float that wants to be turned into degs,mins,secs; returns (deg,min,sec)"""
    dd = abs(dd)
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    return (degrees, minutes, seconds)

def dec2dmsstr(dd):
    """dd is a float that wants to be turned into degs,mins,secs; returns (deg,min,sec)"""
    dd = abs(dd)
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    return f"{int(degrees):02d}:{int(minutes):02d}:{int(seconds):02d}"
