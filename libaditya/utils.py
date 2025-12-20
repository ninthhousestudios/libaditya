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
import time as tmod


def dms2dec(dms):
    """
    dms is a tuple (hour,minutes,seconds) that wants to be turned into a float
    """
    return dms[0] + (dms[1] / 60) + (dms[2] / 3600)


def signize(long, toround, names):
    """
    return a string with 360degree longitude long given with
    long (sign), with long being in the sign
    signs contains the signs to be used, which might be adityas
    """
    index = int(
        (long % 360) / 30
    )  # mod 360 in case long=360...but it probably wouldnt with swe, right?
    if toround[0]:
        inlong = round(long % 30, toround[1])
    else:
        inlong = long % 30
    return f"{dec2dmsstr(inlong)} {names[index]}"


def intize_date(date):
    """
    take a string 'MM/DD/YYYY'
    and return a tuple of int (mm,dd,yyyy)
    """
    date = date.split("/")
    year = int(date[2])
    month = int(date[0])
    day = int(date[1])

    return (month, day, year)


def intize_time(time):
    """
    take a string 'HH:MM:SS'
    and return a float of that time
    """
    time = time.split(":")
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
    for i in range(0, n):
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


def define_true_sidereal_hd_ayanamsa():
    """
    define a custom ayanamsha
    this is from the faq at masteringthezodiac.com
    • Ayanamsa: User Defined SVP
    • Fixed Sidereal Vernal Point: 31.2836
    • Yearly Incremental SVP: 0.00
    • Reference Year: 2000
    reference year means January 1, 2000
    Then choose the true sidereal-M (Midpoint) setting
    """
    swe.set_sid_mode(swe.SIDM_USER + swe.SIDBIT_USER_UT, 2451545.0, 31.2836)

def dec2ymd(age):
    """
    take a floating point age and return a string
    "x years, y months, z days, a hours, b minutes, c seconds"
    the days isnt precise, since i didnt just now feel like
    programming the details of that
    if any of these are zero, it does not print that
    """
    sign = ""
    if age < 0:
        sign = "-" 
        age=-age
    strlist=[]
    # how many years is the integer part
    years = int(age)
    if not years == 0:
        strlist.append(f"{years} years")
    # get the decimal part of the float
    rem = age % 1
    # multiple by 12 to find numbers of months as a float
    md = rem*12
    # months is the decimal part
    months = int(md)
    if not months == 0:
        strlist.append(f"{months} months")
    rem = md % 1
    # days are approximatebecause to be precise we need to find
    # the precise monthetc. and i dont feel like it
    dpart = rem*31
    days = int(rem*31)
    if not days == 0:
        strlist.append(f"{days} days")
    if years == 0 and months == 0:
        # only compute hours and seconds if years and months are 0
        rem = dpart%1
        hours = int(dpart)
        if not hours == 0:
            strlist.append(f"{hours} hours")
        mpart = rem*60
        minutes = int(mpart)
        if not minutes == 0:
            strlist.append(f"{minutes} minutes")
        rem = mpart%1
        seconds = int(rem*60)
        if not seconds == 0:
            strlist.append(f"{seconds} seconds")
    if not strlist:
        return "Less than one second"
    strlist[0] = sign+strlist[0]
    return ", ".join(strlist)

def mktab(n):
    tab = ""
    for i in range(0,n):
        tab += "\t"
    return tab

def mksub(n):
    sub = ""
    for i in range(0,n):
        sub += "sub"
    return sub

def construct_varga_row(cusp):
    """
    construct a row where every column
    is "" except the one the corresponds to the sign
    the planet/cusp is in, then print its in_sign_longitude there
    e.g., if Sun is in Cancer, print nothing in the
    first, second column, third column, print longitude in fourth column, nothing in fifth,etc.
    """
    ret = []

    for n in range(0,12):
        if n == cusp.sign_index():
            ret.append(cusp.in_sign_longitude())
        else:
            ret.append("")
    return ret
