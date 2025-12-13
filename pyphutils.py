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
import pyphglobals as pglob

"""
module of utility functions for pyphemeris
"""


def sign_index(long):
    return int(long / 30)


def nakshatra_index(sidlong, n=0):
    """
    sidlong is the sidereal longitude of a planet
    finds the proper index for the nakshatra array
    n is the index since this is a recursive function;
    needs to be called with n=0 the first time
    """
    if (n * pglob.nak) <= sidlong and sidlong <= ((n + 1) * pglob.nak):
        return n
    else:
        return nakshatra_index(sidlong, n + 1)

def nakshatra_tropkrt28_index(long):
    return int((long/(360/28))%28)


def dhruvecl_index(sidlong, jd, n=0):
    """
    generate the nakshatra index for dhruva ecliptic
    with dhruva eclitpic, the nakshatra boundaries have been projected
    onto the eclitpic from the equator, so dhruva nakshatras are not
    equal on the ecliptic, thus we cant index with nakshatra_index,
    we need to actually build the index of where the nakshatras are,
    then we can find the right index
    """
    ecl_points = build_dhruvecl_boundaries(jd)
    return dindex(sidlong, ecl_points, 0)


def dindex(sidlong, ecl_points, n=0):
    #print(f"{n=} {sidlong=} {ecl_points[n]=}")
    if ecl_points[(n+1)%27] < ecl_points[n]:
        if ecl_points[n] <= sidlong and sidlong <= ecl_points[(n+1)%27]+360:
            return n
    else:
        if ecl_points[n] <= sidlong and sidlong <= ecl_points[(n+1)%27]:
            return n
    return dindex(sidlong, ecl_points, n + 1)

def dhruvecl_naksize(ecl_points):
    """
    find the size of dhruva ecliptic nakshatras with boundaries given by ecl_points
    """
    sizes=[]
    for n in range(len(ecl_points)-1):
        sizes.append((ecl_points[n+1]-ecl_points[n])%360)
    return sizes


def build_dhruvecl_boundaries(jd):
    eo = ecliptic_obliquity(jd)
    nak = pglob.nak
    ecl_points = []
    for i in range(27):
        ecl_points.append(swe.cotrans((i * nak, 0, 1), eo)[0])
    ecl_points.append(360)
    return ecl_points

def build_my_dhruvequ_bounds(gcequ):
    """
    take the equatorial longitude of the galactic center
    and find the nakshatra boundaries along the equator
    list starts with ashvini
    """
    mula=gcequ-(pglob.nak/2)
    ashvini=mula-(18*pglob.nak)
    bounds = []
    for i in range(0,27):
        bounds.append((ashvini+i*pglob.nak)%360)
    return bounds

def build_my_dhruvecl_bounds(equbounds,eo):
    eclbounds = []
    for bound in equbounds:
        eclbounds.append(swe.cotrans((bound, 0, 1), eo)[0])
    return eclbounds


def ketuize(long):
    """
    take rahus longitude and make it ketus
    """
    return (long - 180) % 360


def ecliptic_obliquity(jd):
    return swe.calc(jd,swe.ECL_NUT)[0][0]


def yessignize(long):
    """
    return a string with 360degree longitude long given with
    long (sign), with long being in the sign
    signs contains the signs to be used, which might be adityas
    """
    rasi = int(
        (long % 360) / 30
    )  # mod 360 in case long=360...but it probably wouldnt with swe, right?
    inlong = pglob.round_func(long - (rasi * 30), 4)
    return f"{dec2deg(inlong)} {pglob.signs[rasi]}"


def nosignize(long):
    """
    return the long which was passed
    user wants longitudes raw, so this function
    helps do that
    """
    return long


def yesround(long, nd=3):
    return round(long, nd)


def noround(long, nd=3):
    return long


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


def dec2deg(dd):
    """
    take a decimal dd and return the equivalent DD:MM:SS as a string
    """
    dd = abs(dd)
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    return f"{round(degrees):02d}:{round(minutes):02d}:{round(seconds):02d}"


def dms2dec(dms):
    """
    dms is a tuple (hour,minutes,seconds) that wants to be turned into a float
    """
    return dms[0] + (dms[1] / 60) + (dms[2] / 3600)

def ra2dec(ra):
    return dms2dec(ra)*15

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
    return int(time[0]) + int(time[1]) / 60 + int(time[2]) / 3600

def parse_position_argument(position):
    """
    parse command line position argument
    form is "latitude,longitude"
    either can be:
        float
        DD:MM(:SS)
        DD(N/E/S/W)MM('SS)
    return a float
    N and E are positive
    S and W are negative
    """
    lat, long = position.split(",")

    # given as a decimal
    if "." in lat:
        lat = float(lat)
    if "." in long:
        long = float(long)

    # given in the form DD:MM(:SS)
    if not isinstance(lat,float):
        if ":" in lat:
            latsign = -1 if "-" in lat else 1
            lattmp = lat.split(':')
            # if len == 2, HH:MM, otherwise, HH:MM:SS
            if len(lattmp) == 2:
                lat = latsign*(int(lattmp[0]) + int(lattmp[1]) / 60)
            else:
                lat = latsign*(int(lattmp[0]) + int(lattmp[1]) / 60 + int(lattmp[2]) / 3600)

    if not isinstance(long,float):
        if ":" in long:
            longsign = -1 if "-" in long else 1
            longtmp = long.split(':')
            # if len == 2, HH:MM, otherwise, HH:MM:SS
            if len(longtmp) == 2:
                long = longsign*(int(longtmp[0]) + int(longtmp[1]) / 60)
            else:
                long = longsign*(int(longtmp[0]) + int(longtmp[1]) / 60 + int(longtmp[2]) / 3600)

    # given in Kala format DD(DIR)MM('SS)
    if not isinstance(lat,float):
        if "N" in lat or "S" in lat:
            if "N" in lat:
                latsign = 1
                lattmp = lat.split("N")
            if "S" in lat:
                latsign = -1
                lattmp = lat.split("S")
            if "'" in lattmp[1]:
                min, sec = lattmp[1].split("'")
                lat = latsign*(int(lattmp[0]) + int(min) / 60 + int(sec) / 3600)
            else:
                lat = latsign*(int(lattmp[0]) + int(lattmp[1]) / 60)

    if not isinstance(long,float):
        if "E" in long or "W" in long:
            if "E" in long:
                longsign = 1
                longtmp = long.split("E")
            if "W" in long:
                longsign = -1
                longtmp = long.split("W")
            if "'" in longtmp[1]:
                min, sec = longtmp[1].split("'")
                long = longsign*(int(longtmp[0]) + (int(min) / 60) + (int(sec) / 3600))
            else:
                long = longsign*(int(longtmp[0]) + int(longtmp[1]) / 60)

    return lat, long


def date2str(date):
    """date is a revjul-tuple (year,month,day,hour); return a string 'month/day/year'"""
    return f"{date[1]:02d}/{date[2]:02d}/{date[0]:02d}"

def time2str(time):
    """time is a dec2dms tupel (deg,min,sec); returns a string 'HH:MM:SS'"""
    return f"{str(int(time[0])).zfill(2)}:{str(int(time[1])).zfill(2)}:{str(int(time[2])).zfill(2)}"

def dhruvecl_boundaries_longtime(firstyear,lastyear):
    for yr in range(firstyear,lastyear+1):
        yrjd = swe.julday(yr,1,1,0)
        yreo = ecliptic_obliquity(yrjd)
        gcequ=swe.fixstar(",SgrA*",yrjd, swe.FLG_EQUATORIAL)[0][0]
        yrbnd = build_my_dhruvecl_bounds(build_my_dhruvequ_bounds(gcequ),yreo)
        yrbnd = [round(x,3) for x in yrbnd]
        yrnak = dhruvecl_naksize(yrbnd)
        yrnak = [round(x,3) for x in yrnak]
        print(f"\nFor January 1, {yr} at midnight:")
        print(f"ecliptic obliquity: {yreo}")
        print(f"nakshatra boundaries:")
        print(yrbnd)
        print(f"nakshatra sizes:")
        print(yrnak)
        return yrnak

def vedanga_jyotisha_boundaries_ecliptic():
    dhanishta = 270
    ashvini = dhanishta+5*pglob.nak
    bounds = []
    for i in range(0,27):
        bounds.append((ashvini+i*pglob.nak)%360)
    return bounds

def vedanga_jyotisha_boundaries_equatorial(jd):
    # equatorial longitude of the winter solstice, which i think will always be 270; do it anyway
    dhanishta = swe.cotrans((270,0,1),jd.ecliptic_obliquity())[0]
    ashvini = dhanishta+5*pglob.nak
    print(f"{dhanishta=} {ashvini=}")
    bounds = []
    for i in range(0,27):
        bounds.append((ashvini+i*pglob.nak)%360)
    return bounds

def vedanga_jyotisha_boundaries_dhruva_ecliptic(jd):
    # equatorial longitude of the winter solstice, which i think will always be 270; do it anyway
    dhanishta = swe.cotrans((270,0,1),jd.ecliptic_obliquity())[0]
    ashvini = dhanishta+5*pglob.nak
    print(f"{dhanishta=} {ashvini=}")
    bounds = []
    for i in range(0,27):
        bounds.append((ashvini+i*pglob.nak)%360)
    eclbounds = []
    for bound in bounds:
        eclbounds.append(swe.cotrans((bound,0,1),jd.ecliptic_obliquity())[0])
    return eclbounds

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
