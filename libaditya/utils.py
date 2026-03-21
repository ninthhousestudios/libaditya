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
import time as tmod
import os

from libaditya import constants as const

def dms2dec(dms):
    """
    dms is a tuple (hour,minutes,seconds) that wants to be turned into a float
    """
    return dms[0] + (dms[1] / 60) + (dms[2] / 3600)

def sign_degree_to_longitude(sd: float, context):
    """
    sd is a float of the 10.28, i.e., 10th sign, 28th degree
    now change to an ecliptic longitude based on which Circle we are using
    """
    from libaditya.objects import Circle
    sign=int(sd[0])
    degrees=float(sd[1])
    if context.circle == Circle.ZODIAC:
        return ((sign-1)*30) + degrees
    else:
        return (((sign-2)%12)*30) + degrees


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

def even(n):
    return n%2 == 0 

def odd(n):
    return n%2 == 1 

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

def mktimezone(offset,timezone="UTC"):
    sign = ""
    appendix = ""
    if offset > 0:
        sign = "+"
    if offset == 0 or timezone != "UTC":
        appendix = ""
    else:
        appendix = sign + f"{round(offset, 2)}"
    return timezone + appendix

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



def dec2ymd(age: float) -> str:
    """
    take a floating point age (=number of years) and return a string
    "x years, y months, z days, a hours, b minutes, c seconds"
    the days isnt precise, since i didnt just now feel like
    programming the details of that
    if any of these are zero, it does not print that
    """
#    import pdb; pdb.set_trace()
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
        dpart = rem*24
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

# make a string for dasha lords including subdashas
def mk_dasha_lord(dlist):
    """
    make a string of dashas lords
    """
    lordstr = ""
    for lord in range(0,len(dlist)):
        if lord == len(dlist)-1:
            lordstr += const.vimshottari_dashas[dlist[lord]][0]
        else:
            lordstr += const.vimshottari_dashas[dlist[lord]][0] + "/"
    return lordstr

DIGNITY_RANK = {"EX": 9, "MT": 8, "OH": 7, "GF": 6, "F": 5, "N": 4, "E": 3, "GE": 2, "DB": 1}

def compare_signs_dignities(sign1,sign2,dignities: [str]) -> int:
    """
    compare which sign has stronger dignities among its occupying planets
    dignities is the list of planetary dignities returned by Planets.dignities()

    if different planet counts, more planets wins
    if same count, sort each sign's planets by dignity descending,
    compare element by element; first difference determines the winner

    0 means equal
    1 means sign1 has stronger dignities
    2 means sign2 has stronger dignities
    """
    s1digs = sorted([DIGNITY_RANK.get(dignities[p.list_index()], 0) for p in sign1.karakas()], reverse=True)
    s2digs = sorted([DIGNITY_RANK.get(dignities[p.list_index()], 0) for p in sign2.karakas()], reverse=True)
    if not s1digs and not s2digs:
        return 0
    if len(s1digs) != len(s2digs):
        return 1 if len(s1digs) > len(s2digs) else 2
    for d1, d2 in zip(s1digs, s2digs):
        if d1 > d2: return 1
        if d1 < d2: return 2
    return 0

def compare_planets_dignities(planet1,planet2) -> int:
    """
    compare the dignities of these two planets
    0 for equal
    1 for planet1 has higher dignity
    2 for planet2 has higher dignity
    """
    match planet1,planet2:
        case "EX", "EX":
            return 0
        case "EX", _:
            return 1
        case _, "EX":
            return 2
        case "MT", "MT":
            return 0
        case "MT", _:
            return 1
        case _, "MT":
            return 2
        case "GF", "GF":
            return 0
        case "GF", _:
            return 1
        case _, "GF":
            return 2
        case "F", "F":
            return 0
        case "F", _:
            return 1
        case _, "F":
            return 2
        case "E", "E":
            return 0
        case "E", _:
            return 1
        case _, "E":
            return 2
        case "N", "N":
            return 0
        case "N", _:
            return 1
        case _, "N":
            return 2
        case "GE", "GE":
            return 0
        case "GE", _:
            return 1
        case _, "GE":
            return 2
        case "DB", "DB":
            return 0
        case "DB", _:
            return 1
        case _, "DB":
            return 2



def compare_signs_modalities(sign1,sign2) -> int:
    """
    compare the modalities of sign1 and sign2, both Sign classes
    return which is stronger
    0 means equal strength
    1 means sign1 is stronger
    2 means sign2 is stronger
    """
    if sign1.modality() == sign2.modality():
        return 0
    match (sign1.modality(),sign2.modality()):
        case ("Dual", "Fixed"):
            return 1
        case ("Dual", "Moveable"):
            return 1
        case ("Fixed", "Dual"):
            return 2
        case ("Fixed", "Moveable"):
            return 1
        case ("Moveable", "Dual"):
            return 2
        case ("Moveable", "Fixed"):
            return 2

def copy_collect_charts(root,outdir="all-charts"):
    """
    will copy all .chtk files in root and down to outdir/*.chtk
    will give errors if run again because the file is already there, but it works
    """
    import subprocess
    ret = []
    for root, sub, files in os.walk(root):
        for file in files:
            this_path = os.path.join(root, file)
            res = subprocess.call(["cp", f"{this_path}", f"{outdir}/{file}"])
            if res != 0:
                print("cp command failed")

    return ret

def toJD(ls,context):
    """
    take a list ls of julianday floats
    return a list of JulianDay classes
    """
    from libaditya.objects import JulianDay
    return [JulianDay(jd_number,context.timeJD.utcoffset) for jd_number in ls]

def is_stellarium_id(swe_id):
    """
    find if swe_id is actually a stellarium id 
    """
    if isinstance(swe_id, int):
        return False
    return "HIP" in swe_id or " " in swe_id


def set_swe_true_sidereal_ayanamsa():
    """
    this is used by calling TheStars.set_true_sidereal_hd_ayanamsa()
    this sets the swe ayanamsa to the true sidereal ayanamsa, so that when we intialize
    our stars they have the appropriate coordinates for what we are doing

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


def mkheader(obj):
    header = ""
    header += f"{obj.context.name}\n"
    header += f"Varga {obj.context.amsha} {obj.varga_name()}\n"
    header += f"{obj.sysflgstr} coordinates\n"
    header += f"{const.circle_name(obj.context.circle)}\n"
    header += f"House system {swe.house_name(obj.context.hsys.encode())}\n"
    digplace = "rashi" if obj.context.rashi_temporary_friendships else "varga"
    header += f"Dignities based on {digplace}\n"
    header += f"{obj.context.rashi_aspects} rashi aspects\n"
    if obj.context.sysflg == swe.FLG_SIDEREAL:
        # for sidereal signs we actually use swisseph 36
        # dhruva equatorial is only for nakshatras
        if obj.context.ayanamsa == 98:
            header += f"{const.ayanamsa_name(36)} ayanamsa for signs\n"
            header += f"{const.ayanamsa_name(98)} ayanamsa for nakshatras\n"
        else:
            header += f"{const.ayanamsa_name(obj.context.ayanamsa)} ayanamsa\n"
    elif obj.context.sysflg == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
        if obj.context.ayanamsa == 98:
            header += f"{const.ayanamsa_name(36)} ayanamsa for signs\n"
            header += f"{const.ayanamsa_name(98)} ayanamsa for nakshatras\n"
        header += f"{obj.context.location.placename()} ({obj.context.location.latitude()} lat, {obj.context.location.longitude()} long)\n"
        header += f"{const.ayanamsa_name(obj.context.ayanamsa)} ayanamsa\n"
    else:
        header += f"{const.ayanamsa_name(obj.context.ayanamsa)} ayanamsa\n"
    header += f"{obj.context.location.placename()} ({obj.context.location.latitude()} lat, {obj.context.location.longitude()} long)\n"
    header += f"{obj.context.timeJD}\n"
    return header
