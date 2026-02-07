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

def compare_signs_dignities(sign1,sign2,dignities: [str]) -> int:
    """
    find which sign has the highest dignity in it
    dignities of the list of planetary dignities returned by Planets.dignities()
    0 means they both have equal highest dignity
    1 means sign1 has the highest dignity
    2 means sign2 has the highest dignity
    """
    s1digs = []
    for planet in sign1.karakas():
        s1digs.append(dignities[planet.list_index()])
    s2digs = []
    for planet in sign2.karakas():
        s2digs.append(dignities[planet.list_index()])
    if s1digs == [] and s2digs == []:
        return 0
    if "EX" in s1digs and "EX" in s2digs:
        return 0
    if "EX" in s1digs and not "EX" in s2digs:
        return 1
    if not "EX" in s1digs and "EX" in s2digs:
        return 2
    if "MT" in s1digs and "MT" in s2digs:
        return 0
    if "MT" in s1digs and not "MT" in s2digs:
        return 1
    if not "MT" in s1digs and "MT" in s2digs:
        return 2
    if "OH" in s1digs and "OH" in s2digs:
        return 0
    if "OH" in s1digs and not "OH" in s2digs:
        return 1
    if not "OH" in s1digs and "OH" in s2digs:
        return 2
    if "GF" in s1digs and "GF" in s2digs:
        return 0
    if "GF" in s1digs and not "GF" in s2digs:
        return 1
    if not "GF" in s1digs and "GF" in s2digs:
        return 2
    if "F" in s1digs and "F" in s2digs:
        return 0
    if "F" in s1digs and not "F" in s2digs:
        return 1
    if not "F" in s1digs and "F" in s2digs:
        return 2
    if "E" in s1digs and "E" in s2digs:
        return 0
    if "E" in s1digs and not "E" in s2digs:
        return 1
    if not "E" in s1digs and "E" in s2digs:
        return 2
    if "GE" in s1digs and "GE" in s2digs:
        return 0
    if "GE" in s1digs and not "GE" in s2digs:
        return 1
    if not "GE" in s1digs and "GE" in s2digs:
        return 2
    if "DB" in s1digs and "DB" in s2digs:
        return 0
    if "DB" in s1digs and not "DB" in s2digs:
        return 1
    if not "DB" in s1digs and "DB" in s2digs:
        return 2

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

def parse_simbad_ascii_response(response: str):
    """
    response is the http_response itself
    """
    lines = response.split("\n")
    #import pdb; pdb.set_trace()
    magV = None
    parallax = None
    hipid = "no hip id"
    name = ""
    for n,line in enumerate(lines):
        if n > 28:
            # find HIP id so we can return it first as well
            for n in range(28,50):
                if "HIP" in lines[n]:
                    line = lines[n].split()
                    for i,element in enumerate(line):
                        if element == "HIP":
                            hipid = element+" "+line[i+1]
                if "NAME" in lines[n]:
                    line = lines[n].split()
                    for i,element in enumerate(line):
                        if element == "NAME":
                            name = line[i+1]
            break
        match n:
            case 2:
                trad_name = str(line)
            case 5:
                names = line.split(" ")
                # try to guess the ,noMen name
                nomen_name = ","+names[2]+names[3]
            case 7:
                # icrs coordinates
                icrs = line.split(" ")
                ra_hour = icrs[1]
                ra_minute = icrs[2]
                ra_sec = icrs[3]
                dec_degree = icrs[5]
                dec_minute = icrs[6]
                dec_sec = icrs[7]
            case 11:
                pm = line.split(" ")
                pmra = pm[2]
                pmde = pm[3]
            case 13:
                rad_vel = line.split(" ")
                rad_vel = rad_vel[2]
            case 12:
                para = line.split(" ")
                parallax = para[1]
        if "Flux V" in line:
            flux = line.split(" ")
            magV = flux[3]
    if not magV:
        magV = 0
    return [hipid,name],trad_name,nomen_name,ra_hour,ra_minute,ra_sec,dec_degree,dec_minute,dec_sec,pmra,pmde,rad_vel,parallax,magV


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

def make_swe_star(names=[""]) -> str:
    """
    make an entry for ephe/sefstars.txt to add star "name" to that file, and thus to swe
    returns a list [sefstars.txt_entry,simbad_response_str]
    """
    import urllib
    from string import Template
    simbad_query = Template("https://simbad.cds.unistra.fr/simbad/sim-id?Ident=$swe_id&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit%20id&output.format=ASCII")
    swe_star_entry = Template("$trad_name,$nomen_name,ICRS,$ra_hour,$ra_minute,$ra_sec,$dec_degree,$dec_minute,$dec_sec,$pmra,$pmde,$rad_vel,$parallax,$magnitude_V")
    if not isinstance(names,list):
        names=[names]
    ret = []
    for name in names:
        name = name.replace(" ","+")
        the_bytes = urllib.request.urlopen(simbad_query.substitute(swe_id=name))
        ascii = the_bytes.read().decode()
#            lines=the_bytes.read().decode().split("\n")
#            for n,line in enumerate(lines):
#                print(n,line)
        # now parse bytes into all the variables needs for swe_star_entry
        ids, trad_name,nomen_name,ra_hour,ra_minute,ra_sec,dec_degree,dec_minute,dec_sec,pmra,pmde,rad_vel,parallax,magV = parse_simbad_ascii_response(ascii)
        if ids[0] != "":
            # if simba returned a traditional name, use it
            trad_name = ids[0]
        else:
            trad_name = name.strip().replace("+"," ")
        ret.append(f"{trad_name}{nomen_name},ICRS,{ra_hour},{ra_minute},{ra_sec},{dec_degree},{dec_minute},{dec_sec},{pmra},{pmde},{rad_vel},{parallax},{magV}")
    return str(ids[1]+", "+ids[0]), ret, ascii


def write_swe_stars(names=[""],outfile=f"{const.base_path}/stars/new_sefstars.txt"):
    lines=[]
    for name in names:
        ret=make_swe_star(name)
        # comment line with name and hip id
        lines.append("# "+ret[0]+"\n")
        # swe star entry
        lines.append(ret[1][0]+"\n")
    with open(outfile,"a") as fd:
        fd.writelines(lines)
    return

def swe_star_to_python(swe_star: str) -> str:
    """
    take a star line from ephe/sefstars.txt and produce a python object that inherits from FixedStar
    this is written in a .py file that can then be loaded, and we can use any of these stars then by name
    e.g., stars.the_stars.Fomalhaut(context)

    swe_star is like this:

    # Common Name, HIP ID
    Galactic Center,SgrA*,ICRS,17,45,40.03599,-29,00,28.1699,-2.755718425, -5.547,  0.0,0.125,999.99,  0,    0

    (traditional/common) name,(,noMen) nomenclature name, equinox, ra_hour, ra_minute, ra_second, dec_degree, dec_minute, dec_second,
    ra of proper motion, dec of proper motion, radial velocity in km/s, annual parallax in .0001"", magnitude_V
    an example of what this produces:

    class GalacticCenter(FixedStar): # ,SgrA*

        def __init__(self, context = EphContext()): 
            super().__init__(swe_id = ",SgrA*", context=context)

    for new stars, this is the template I am trying to use:

    # Capella, HIP 24608
    Alpha Auriga,alfAur,ICRS,05,16,41.35871,+45,59,52.7693,75.25,-426.89,29.19,76.20,0.08

    class AlphaAuriga(FixedStar): # ,alfAur

        def __init__(self, context = EphContext()): 
            super().__init__(swe_id = ",alfAur", context=context, swe_string="Alpha Auriga,alfAur,ICRS,05,16,41.35871,+45,59,52.7693,75.25,-426.89,29.19,76.20,0.08")
            self._other_names = ["Capella", "HIP 24608"]

    Capella = AlphaAuriga

    now, TheStars(context)["alfAur"] will return AlphaAuriga()
    but you can also do stars.the_stars.Capella(context)
    
    """
    lines=swe_star.split("\n")
    common_name = ""
    if len(lines) == 1:
        swe_line = lines[0]
        swe_split = lines[0].split(",")
        hip_name = "" 
    if len(lines) == 2:
        # could "" if there is no common name
        # all expect last character because .split() catches a comma
        swe_line = lines[1]
        swe_split = lines[1].split(",")
        common_name = lines[0].split()[1][:-1]
        hip_name = lines[0].split()[2]+lines[0].split()[3]
    trad_name = swe_split[0].replace(" ","")
    swe_id = ","+swe_split[1]
    other_classes=""
    if common_name != trad_name:
        if common_name == "":
            common_name = trad_name
        else:
            other_classes = f"{common_name} = {trad_name}"
    ret=[]
    ret.append(f"class {trad_name}(FixedStar): # {swe_id}")
    ret.append(f"    def __init__(self, context = EphContext()):\n")
    ret.append(f"        super().__init__(swe_id = \"{swe_id}\", context=context, swe_string=\"{swe_line}\")")
    ret.append(f"        self._other_names = [\"{common_name}\", \"{hip_name if hip_name else ""}\"]\n")
    ret.append(other_classes)
    return ret

def swe_stars_to_py(stars,outfile=f"{const.base_path}/stars/new_stars.py"):
    """
    take an input
    """
    #with open(outfile, "a") as fd:
