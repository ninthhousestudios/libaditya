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
    nomen_name = ",noMen"
    for n,line in enumerate(lines):
        if n > 28:
            # find HIP id so we can return it first as well
            for n in range(28,50):
                if n >= len(lines):
                    break
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
    try:
        return [hipid,name],trad_name,nomen_name,ra_hour,ra_minute,ra_sec,dec_degree,dec_minute,dec_sec,pmra,pmde,rad_vel,parallax,magV
    except:
        return response


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

def swe_make_star(names=[""]) -> str:
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
        response = parse_simbad_ascii_response(ascii)
        try:
            ids,trad_name,nomen_name,ra_hour,ra_minute,ra_sec,dec_degree,dec_minute,dec_sec,pmra,pmde,rad_vel,parallax,magV = response
        except:
            print("Error: \n")
            print(response)
            return
        id_line = f"#0# {nomen_name.replace(",","")}, "
        id_line += str(ids[1]+", "+ids[0]+"\n")
        ret.append(id_line)
        ret.append(f"{nomen_to_long_form(nomen_name)}{nomen_name},ICRS,{ra_hour},{ra_minute},{ra_sec},{dec_degree},{dec_minute},{dec_sec},{pmra},{pmde},{rad_vel},{parallax},{magV}\n")
    return ret, ascii


def swe_write_stars(names=[""],outfile=""):
    lines=[]
    for name in names:
        returns, ascii=swe_make_star(name)
#        print(f"sws: {returns[0]=} {returns[1]=}")
        lines.append(returns[0])
        lines.append(returns[1])
#    print(f"{lines=}")
    with open(outfile,"a") as fd:
        fd.writelines(lines)
    return

def swe_star_to_python(swe_star: str) -> str:
    """
    take a star line from ephe/sefstars.txt and produce a python object that inherits from FixedStar
    this is written in a .py file that can then be loaded, and we can use any of these stars then by name
    e.g., stars.the_stars.Fomalhaut(context)

    swe_star is like this:

    #0# swe_id, Common Name, HIP ID
    Galactic Center,SgrA*,ICRS,17,45,40.03599,-29,00,28.1699,-2.755718425, -5.547,  0.0,0.125,999.99,  0,    0

    (traditional/common) name,(,noMen) nomenclature name, equinox, ra_hour, ra_minute, ra_second, dec_degree, dec_minute, dec_second,
    ra of proper motion, dec of proper motion, radial velocity in km/s, annual parallax in .0001"", magnitude_V
    an example of what this produces:

    class GalacticCenter(FixedStar): # ,SgrA*

        def __init__(self, context = EphContext()): 
            super().__init__(swe_id = ",SgrA*", context=context)

    for new stars, this is the template I am trying to use:

    #0# alfAur, Capella, HIP 24608
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
    # since swe_star[1] has a \n at the end, lines will have 3 elements, the last being ""
    names = lines[0]
    names_split = names.split(",")
    common_names = []
    hip_name = ""
    # the swe_id, aka ",nomen" name
    id_swe_id = ","+names_split[0].split()[1]
    # dont need the first one anymore
    names_split = names_split[1:]
    for name in names_split:
        name=name.strip()
        if "HIP" in name:
            hip_name = f"{name.strip()}"
        if not "Messier" in names and not name.startswith("VC") and not name.startswith("NGC") and not name.startswith("HR") and not name.startswith("HD"):
            # get all the common names
            common_names.append(f"{name.strip()}")
    other_names = common_names
    if hip_name:
        other_names = common_names + [hip_name]

    swe_line = lines[1]
    swe_split = lines[1].split(",")

    long_form_name = swe_split[0].replace(" ","")
    star_swe_id = ","+swe_split[1]

    if id_swe_id != star_swe_id:
        print(f"Error swe_ids do not match: {id_swe_id} != {star_swe_id}\nLines out of order")
        return

    other_classes=""
    for common_name in common_names:
        other_classes += f"{common_name.replace(" ","")} = {long_form_name}\n"
    other_classes += "\n\n"

    if other_names is not None:
        tmp = []
        for name in other_names:
            if name in tmp:
                continue
            if name == "" or name == '""':
                continue
            tmp.append(name.replace("'",""))
        other_names = tmp

    ret=[]
    ret.append(f"class {long_form_name}(FixedStar): # {id_swe_id}\n")
    ret.append("\n")
    ret.append(f"    def __init__(self, context = EphContext()):\n")
    ret.append(f"        super().__init__(swe_id = \"{star_swe_id}\", context=context, swe_string=\"{swe_line}\")\n")
    ret.append(f"        self._other_names = {other_names}\n\n")
    ret.append(other_classes)
    return "".join(ret)

def swe_stars_to_py(infile,outfile):
    """
    take an input
    """
    with open(infile, "r") as infd:
        swe_stars = infd.readlines()

    with open(outfile, "a") as outfd:
        n = 0
        while n < len(swe_stars):
            # if line is blank
            if not swe_stars[n]:
                n+=1
                continue
            # if line has info for the next line
            if "#" in swe_stars[n] and "#0#" not in swe_stars[n]:
                n+=1
                continue
            star = swe_stars[n]
            n+=1
            if "#0#" in star:
                star += swe_stars[n]
                n+=1
            outfd.write(swe_star_to_python(star))

def convert_sefstars(infile,outfile):
    """
    convert ephe/sefstars.txt to a different format
    i already manually changed all 2-letter greek abbreviations to 3-letter abbreviations manually
    so that is accounted for in this function
    """
    with open(infile, "r") as infd:
        inlines = infd.readlines()

    outlines = []
    for inline in inlines:
        if inline.startswith("#"):
            outlines.append(inline)
            continue
        star = inline.split(",")
        trad_name = star[0]
        nomen_name = star[1].replace("-","0")
        star[1] = nomen_name
        long_form_name = nomen_to_long_form(nomen_name)
        star[0]=long_form_name
        outlines.append(f"#0# {nomen_name}, {trad_name}\n")
        outlines.append(",".join(star).strip()+"\n")

    with open(outfile,"a") as outfd:
        outfd.writelines(outlines)


def nomen_to_long_form(nomen: str):
    """
    turn a nomenclature name into a long form version of itself
    nomenclature names, any of these designations:
    Bayer, Falmsteed, HIP, NGC, HD, HR, M (Messer Object)
    greek is lowercase greek letter, will use upper case in English
    Latin is genitive of Latin constellation name
    e.g., alfTau, Alpha Tauri, α Tauri
    """
    if nomen[0] == ",":
        nomen = nomen[1:]
    if nomen[0].isnumeric():
        # this means it is Flamsteed 
        # easiest to do this first
        number=""
        n=0
        while nomen[n].isnumeric():
            number+=nomen[n]
            n+=1
        constellation=""
        while n < len(nomen):
            constellation+=nomen[n]
            n+=1
        return const.star_names_short_to_long["constellations"][constellation]+number
    # check if this is a "special constellation"
    # not really constellations, but fill the same place in the nomen name, so are treated the same for this purpose
    special_constellations = ["VC","HD","HR","HIP","NGC"]
    # doesnt include "M" because that throws off other checks
    special = None
    for constellation in special_constellations:
        number=""
        if constellation in nomen.upper() or nomen.upper().startswith("M"):
            # if one of these special tags is here, special will show us that it is
            if nomen.upper().startswith("M"):
                special = "M"
                number = nomen[1:]
            else:
                special = constellation
                # the rest of the string except the "constellation" names
                number = nomen[(len(special)):]
            break
    if number != "":
        return const.star_names_short_to_long["constellations"][special]+f" {number.strip()}"
    if number == "":
        if special == "VC":
            return const.star_names_short_to_long["constellations"][special]
    # now assume it is a Bayer designation
    # some in the original sefstars.txt have a hyphen "-" in the name
    # replace that with 0
    # first three letters are the greek
    greek = nomen[:3]
    # last three are the Latin constellation
    latin = nomen[3:]
    # sometimes there are two stars with the same name basically, one is, e.g., gam01Sgr, the other, gam02Sgr
    # this will be Gamma Sagittarii 1 and Gamma Sagittarii 2
    number = ""
    if latin[:2].isnumeric():
        number = latin[:2]
        latin = latin[2:]
    if not greek.islower():
        return nomen
    if number:
        return const.star_names_short_to_long["greek"][greek]+" "+const.star_names_short_to_long["constellations"][latin]+f" {number}"
    return const.star_names_short_to_long["greek"][greek]+" "+const.star_names_short_to_long["constellations"][latin]
