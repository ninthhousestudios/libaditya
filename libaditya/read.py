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

import codecs
import configparser
import toml

from libaditya import constants as const
from libaditya.objects import JulianDay, Location, EphContext, Circle


def read_pyph(infile):
    input = open(infile, "r")
    for line in input:
        if not "=" in line:
            continue
        field, value = line.split("=")
        field = field.strip()
        value = value.strip()
        if field.startswith("Na") or field.startswith("na"):
            name = value
        if field.startswith("Pla") or field.startswith("pla"):
            placename = value
        if field.startswith("Da") or field.startswith("da"):
            month, day, year = intize_date(value)
        if field.startswith("Ti") or field.startswith("ti"):
            ephclock = intize_time(value)
        if field.startswith("La") or field.startswith("la"):
            lat = float(value)
        if field.startswith("Lo") or field.startswith("lo"):
            long = float(value)
    return name, placename, month, day, year, ephclock, lat, long


def _read_chtk_lines(infile):
    """Read a .chtk file, handling both UTF-16 LE (BOM) and ASCII/UTF-8."""
    with open(infile, "rb") as f:
        raw = f.read()
    if raw[:2] == b'\xff\xfe':
        text = raw.decode("utf-16-le").lstrip("﻿")
        return [line.encode("latin-1", errors="replace") for line in text.splitlines()]
    else:
        return raw.splitlines()


def read_chtk(infile):
    lines = _read_chtk_lines(infile)
    linenum = 0
    for line in lines:
        # print(f"{n}: {line.decode(errors='ignore')}")
        match linenum:
            case 0:
                name = clean_line(line)
            case 1:
                year = intize_line(codecs.decode(line))
            case 2:
                month = intize_line(codecs.decode(line))
            case 3:
                day = intize_line(codecs.decode(line))
            case 4:
                hour = intize_line(codecs.decode(line))
            case 5:
                min = intize_line(codecs.decode(line))
            case 6:
                sec = intize_line(codecs.decode(line))
            case 7:
                sexstr = codecs.decode(line).strip().replace("\x00", "").replace("\r", "").replace("\n", "")
                if sexstr in ("m", "M", "1"):
                    sex = 1
                elif sexstr in ("f", "F", "0", "2"):
                    sex = 2
                else:
                    sex = 0
            case 8:
                country = clean_line(line)
            case 9:
                city = clean_line(line)
            case 10:
                long = long_to_float(clean_line(line))
            case 11:
                lat = lat_to_float(clean_line(line))
            case 12:
                # this is the utc offset
                # usually this line is HH:MM:SS
                # someimtes it is just HH:MM
                # sometimes it is just H, so deal with all of those
                line = clean_line(line).split(":")
                sign = 1
                if line[0] == "UTC":
                    utcoff = 0
                    continue
                elif len(line) == 1:
                    h = int(line[0])
                    m = s = 0
                elif len(line) == 2:
                    h = int(line[0])
                    m = int(line[1])
                    s = 0
                else:
                    h = int(line[0])
                    m = int(line[1])
                    s = int(line[2])
                if h < 0:
                    sign = -1
                    h = abs(h)
                utcoff = sign*(int(h) + (int(m) / 60) + (int(s) / 3600))
            case 13:  # dst value
                dst = intize_line(codecs.decode(line))
        linenum += 1
    placename = city + ", " + country
    ephclock = hour + min / 60 + sec / 3600
    return (
        name,
        placename,
        month,
        day,
        year,
        # below is the precise decimal hour needed to turn this into the proper JulianDay
        ephclock + utcoff - dst,
        lat,
        long,
        -(utcoff - dst),
    )


def read_chtk_location(infile):
    _, placename, _, _, _, _, lat, long, utcoff = read_chtk(infile)
    return placename, lat, long, utcoff

def chtk_to_Location(infile):
    context=chtk_to_context(infile)
    return context.location

def read_toml(infile):
    con=toml_to_context(infile)
    return con.name,con.location.placename(),con.timeJD.month(),con.timeJD.day(),con.timeJD.year(),con.timeJD.hour(tz="utc"),con.location.lat,con.location.long,con.location.utcoffset

def read_toml_location(infile):
    con=toml_to_context(infile)
    return con.location.placename, con.location.lat, con.location.long, con.timeJD.utcoffset

def toml_to_Location(infile):
    context=toml_to_context(infile)
    return context.location

# note: argument "toround" takes a tuple (bool,int) = (if toround; ifso, how much)
def chtk_to_context(infile, sysflg=const.TROP,ayanamsa=98,hsys='C',circle=Circle.ADITYA,signize=True,toround=(True,3),print_nakshatras=True,print_outer_planets=True,names_type="mixed",sign_names="adityas"):
    name, placename, month, day,year, timedec, lat, long, utcoffset = read_chtk(infile)
    timeJD = JulianDay((year,month,day,timedec),utcoffset)
    location = Location(lat, long, 0, placename, timeJD.utcoffset)
    return EphContext(name=name,timeJD=timeJD,location=location,sysflg=sysflg,amsha=1,ayanamsa=ayanamsa,hsys=hsys,circle=circle,toround=toround,print_nakshatras=print_nakshatras, print_outer_planets=print_outer_planets, names_type=names_type,sign_names=sign_names)

def context_to_chtk(context=EphContext(),outfile=None):
    """
    turn context into a list of strings

    out = []
    out.append(str(name)+"\n")
    out.append(str(year)+"\n")
    out.append(str(month)+"\n")
    out.append(str(day)+"\n")
    out.append(str(hour)+"\n")
    out.append(str(min)+"\n")
    out.append(str(sec)+"\n")
    out.append(str(sex)+"\n")
    out.append(str(country)+"\n")
    out.append(str(city)+"\n")
    out.append(float_to_long(long)+"\n")
    out.append(float_to_lat(lat)+"\n")
    out.append(f"{h:02d}:{m:02d}:{s:02d}\n")
    out.append(str(dst)+"\n")
    return out
#   put below into a different function
#    fout = open(foutname+"-test"+".chtk","w")
#    fout.writelines(out)
#    fout.close()
    """
    out = []
    out.append(str(context.name)+"\n")
    out.append(str(context.timeJD.year())+"\n")
    out.append(str(context.timeJD.month())+"\n")
    out.append(str(context.timeJD.day())+"\n")
    out.append(str(context.timeJD.hour())+"\n")
    out.append(str(context.timeJD.min())+"\n")
    out.append(str(context.timeJD.sec())+"\n")

def chtk_to_toml(infile):
    """
    encodes with the least information needed
    outputs into an equivalent file, replacing .chtk by .toml

    [timeJD]
    jd = float
    utcoffset = float

    [location]
    # N,E are positive
    lat = float
    long = float
    # alt in meters
    alt = float
    # optional placename
    placename = ""
    timezone = timeJD.mktimezone()
    """
    name, placename, month, day,year, timedec, lat, long, utcoffset = read_chtk(infile)
    timeJD = JulianDay((year,month,day,timedec),utcoffset)
    location = Location(lat, long, 0, placename, utcoffset)
    d=dict()
    d["name"] = name
    d["timeJD"] = dict()
    d["timeJD"]["jd"]=timeJD.jd_number()
    d["timeJD"]["utcoffset"]=timeJD.utcoffset
    d["location"]=location.__dict__
    with open(f"{infile.split('.')[0]}.toml", "w") as fd:
        toml.dump(d,fd)
    return

def toml_to_context(infile) -> EphContext:
    with open(infile, "r") as fd:
        d = toml.load(fd)
    name = d["name"]
    timeJD = JulianDay(d["timeJD"]["jd"],d["timeJD"]["utcoffset"])
    # use unpacking of the dictionary values
    location = Location(*d["location"].values())
    # all other options are defaults
    return EphContext(name=name,timeJD=timeJD,location=location)

def lat_to_float(lat):
    """
    change kalas lat representation into a float
    """
    # string is like this 38N37'38 or short form 23n02
    if lat[2:3] in ("N", "n"):
        sign = 1
    else:
        sign = -1
    degs = float(lat[:2])
    mins = float(lat[3:5]) if len(lat) > 3 else 0.0
    secs_str = lat[6:8] if len(lat) > 6 else ""
    secs = float(secs_str) if secs_str else 0.0
    return sign*(degs + (mins / 60) + (secs / 3600))


def float_to_lat(lat):
    if lat >= 0:
        dir = "N"
    else:
        dir = "S"

    latstr = dec2dms(lat)
    d, m, s = latstr.split(":")

    return d + dir + m + "'" + s


def long_to_float(long):
    """
    change kalas long representation into a float
    """
    # long form: 090W11'52 (3-digit degrees)
    # short form: 72e39 (2-digit degrees, no seconds)
    if long[3:4] in ("E", "e", "W", "w"):
        sign = 1 if long[3:4] in ("E", "e") else -1
        degs = float(long[:3])
        mins = float(long[4:6]) if len(long) > 4 else 0.0
        secs_str = long[7:9] if len(long) > 7 else ""
        secs = float(secs_str) if secs_str else 0.0
    elif long[2:3] in ("E", "e", "W", "w"):
        sign = 1 if long[2:3] in ("E", "e") else -1
        degs = float(long[:2])
        mins = float(long[3:5]) if len(long) > 3 else 0.0
        secs_str = long[6:8] if len(long) > 6 else ""
        secs = float(secs_str) if secs_str else 0.0
    else:
        sign = 1
        degs = float(long[:3])
        mins = secs = 0.0
    return sign*(degs + (mins / 60) + (secs / 3600))


def float_to_long(long):
    if long >= 0:
        dir = "E"
    else:
        dir = "W"

    longstr = dec2dms(long)
    d, m, s = longstr.split(":")

    return "0" + d + dir + m + "'" + s


def intize_line(line):
    """
    line is a string (of decoded bytes)
    we remove all the space, etc. characters, then
    can return the integer of the string
    """
    nochars = ["\x00", "\r", "\n"]
    count = 0
    line = list(line)
    while count < len(line):
        if line[count] in nochars:
            del line[count]
            continue
        count += 1
    s = "".join(line)
    return int(float(s))


def clean_line(line):
    """
    line is a line of bytes
    we remove all the space, carriage return, and newline characters, then
    can return the string as only a string
    """
    line = line.decode(errors="ignore")
    nochars = ["\x00", "\r", "\n"]
    count = 0
    line = list(line)
    while count < len(line):
        if line[count] in nochars:
            del line[count]
            continue
        count += 1
    retval = "".join(line)
    #    print(retval)
    return retval


def dec2dms(dd):
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
    if len(time) == 2:
        # no seconds
        return float(time[0]) + float(time[1]) / 60
    else:
        return float(time[0]) + float(time[1]) / 60 + float(time[2]) / 3600


def parse_position_argument(position):
    """
    i think this basically works now

    parse command line position argument
    position is one position, either latitude or longitude
    either can be:
        float
        DD:MM(:SS)
       (D)DD(N/E/S/W)MM('SS)
    return a float
    N and E are positive
    S and W are negative
    """

    # given as a decimal
    if "." in position and not any(char.isalpha() for char in position):
        return float(position)

    # given in the form DD:MM(:SS)
    if not isinstance(position, float):
        if ":" in position:
            positiontmp = position.split(":")
            # if len == 2, HH:MM, otherwise, HH:MM:SS
            sign = 1
            if "-" in positiontmp[0]:
                sign = -1
            if len(positiontmp) == 2:
                position = sign * (abs(float(positiontmp[0])) + float(positiontmp[1]) / 60)
            else:
                position = sign * (abs(float(positiontmp[0])) + float(positiontmp[1]) / 60 + float(positiontmp[2]) / 3600)
        return position

    # given in Kala format DDD(DIR)MM('SS)
    # longtiude is DDD, latitude it DD
    if not isinstance(position, float):
        if "N" in position or "S" in position or "W" in position or "E" in position:
            if "N" in position:
                positionsign = 1
                positiontmp = position.split("N")
            elif "E" in position:
                positionsign = 1
                positiontmp = position.split("E")
            elif "S" in position:
                positionsign = -1
                positiontmp = position.split("S")
            elif "W" in position:
                positionsign = -1
                positiontmp = position.split("W")
            if "'" in positiontmp[1]:
                min, sec = positiontmp[1].split("'")
                position = positionsign * (int(positiontmp[0]) + int(min) / 60 + float(sec) / 3600)
            else:
                position = positionsign * (int(positiontmp[0]) + int(positiontmp[1]) / 60)
        return position




#def init_names(langfile=const.base_path + "/dict/dict.mixed"):
#    names = configparser.ConfigParser()
#    if "/" not in langfile:
#        langfile = const.base_path + f"/dict/{langfile}"
#    names.read(langfile)
#
#    # because of importing and such things
#    planets = []
#    zodiac = []
#    tithis = []
#    karanas = []
#    nakshatras = []
#    nakshatraeq = []
#    varas = []
#    yogas = []
#    adityas = []
#
#    # because of needing these names in pyphclasses i called init_names()
#    # there, which when i run the whole program thus initializes them twice
#    # which causes the karana especially to not work right
#    # so if planets is not an empty list, then we have already done the names
#    # if planets != []:
#    #    return
#
#    pnames = names["PLANETS"]
#    znames = names["RASIS"]
#    tnames = names["TITHI"]
#    knames = names["KARANA"]
#    nnames = names["NAKSHATRA"]
#    neqnames = names["NAKSHATRAEQ"]
#    vnames = names["VARA"]
#    ynames = names["YOGAS"]
#    anames = names["ADITYAS"]
#
#    planets.append(pnames["Sun"])
#    planets.append(pnames["Moon"])
#    planets.append(pnames["Mercury"])
#    planets.append(pnames["Venus"])
#    planets.append(pnames["Mars"])
#    planets.append(pnames["Jupiter"])
#    planets.append(pnames["Saturn"])
#    planets.append(pnames["Uranus"])
#    planets.append(pnames["Neptune"])
#    planets.append(pnames["Pluto"])
#    planets.append(pnames["Rahu"])  # index 10
#    planets.append(pnames["Ketu"])  # index 11
#    planets.append([])
#    planets.append([])
#    planets.append(pnames["Earth"])  # so we can use swe.EARTH
#    planets.append("Chiron")
#
#    zodiac.append(znames["Aries"])
#    zodiac.append(znames["Taurus"])
#    zodiac.append(znames["Gemini"])
#    zodiac.append(znames["Cancer"])
#    zodiac.append(znames["Leo"])
#    zodiac.append(znames["Virgo"])
#    zodiac.append(znames["Libra"])
#    zodiac.append(znames["Scorpio"])
#    zodiac.append(znames["Sagittarius"])
#    zodiac.append(znames["Capricorn"])
#    zodiac.append(znames["Aquarius"])
#    zodiac.append(znames["Pisces"])
#
#    tithis.append(tnames["Nanda"])
#    tithis.append(tnames["Bhadra"])
#    tithis.append(tnames["Jaya"])
#    tithis.append(tnames["Rkta"])
#    tithis.append(tnames["Purna"])
#
#    karanas.append(knames["Kimtughna"])
#    karanas.append(knames["Bava"])
#    karanas.append(knames["Balava"])
#    karanas.append(knames["Kaulava"])
#    karanas.append(knames["Taitula"])
#    karanas.append(knames["Garija"])
#    karanas.append(knames["Vanija"])
#    karanas.append(knames["Vishti"])
#    karanas.append(knames["Shakuni"])
#    karanas.append(knames["Chatushpada"])
#    karanas.append(knames["Naga"])
#    karanas = organize_karana(karanas)
#
#    nakshatras.append(nnames["Ashvini"])
#    nakshatras.append(nnames["Bharani"])
#    nakshatras.append(nnames["Krittika"])
#    nakshatras.append(nnames["Rohini"])
#    nakshatras.append(nnames["Mrigashira"])
#    nakshatras.append(nnames["Ardra"])
#    nakshatras.append(nnames["Punarvasu"])
#    nakshatras.append(nnames["Pushya"])
#    nakshatras.append(nnames["Ashlesha"])
#    nakshatras.append(nnames["Magha"])
#    nakshatras.append(nnames["Purva Phalguni"])
#    nakshatras.append(nnames["Uttara Phalguni"])
#    nakshatras.append(nnames["Hasta"])
#    nakshatras.append(nnames["Chitra"])
#    nakshatras.append(nnames["Svati"])
#    nakshatras.append(nnames["Vishakha"])
#    nakshatras.append(nnames["Anuradha"])
#    nakshatras.append(nnames["Jyeshtha"])
#    nakshatras.append(nnames["Mula"])
#    nakshatras.append(nnames["Purva Ashadha"])
#    nakshatras.append(nnames["Uttara Ashadha"])
#    nakshatras.append(nnames["Shravana"])
#    nakshatras.append(nnames["Danishtha"])
#    nakshatras.append(nnames["Shatabhisha"])
#    nakshatras.append(nnames["Purva Bhadrapada"])
#    nakshatras.append(nnames["Uttara Bhadrapada"])
#    nakshatras.append(nnames["Revati"])
#
#    varas.append(vnames["Ravivara"])
#    varas.append(vnames["Somavara"])
#    varas.append(vnames["Mangalavara"])
#    varas.append(vnames["Budhavara"])
#    varas.append(vnames["Guruvara"])
#    varas.append(vnames["Shukravara"])
#    varas.append(vnames["Shanivara"])
#
#    yogas.append(ynames["Vishkambha"])
#    yogas.append(ynames["Priti"])
#    yogas.append(ynames["Ayushman"])
#    yogas.append(ynames["Saubhagya"])
#    yogas.append(ynames["Shobana"])
#    yogas.append(ynames["Atiganda"])
#    yogas.append(ynames["Sukarma"])
#    yogas.append(ynames["Dhriti"])
#    yogas.append(ynames["Shoola"])
#    yogas.append(ynames["Ganda"])
#    yogas.append(ynames["Vriddhi"])
#    yogas.append(ynames["Dhruva"])
#    yogas.append(ynames["Vyaghata"])
#    yogas.append(ynames["Harshana"])
#    yogas.append(ynames["Vajra"])
#    yogas.append(ynames["Siddhi"])
#    yogas.append(ynames["Vyatipata"])
#    yogas.append(ynames["Variyan"])
#    yogas.append(ynames["Parigha"])
#    yogas.append(ynames["Shiva"])
#    yogas.append(ynames["Siddha"])
#    yogas.append(ynames["Sadhya"])
#    yogas.append(ynames["Shubha"])
#    yogas.append(ynames["Shukla"])
#    yogas.append(ynames["Brahma"])
#    yogas.append(ynames["Indra"])
#    yogas.append(ynames["Vaidhriti"])
#
#    adityas.append(anames["Dhata"])
#    adityas.append(anames["Aryama"])
#    adityas.append(anames["Mitra"])
#    adityas.append(anames["Varuna"])
#    adityas.append(anames["Indra"])
#    adityas.append(anames["Vivasvan"])
#    adityas.append(anames["Tvashta"])
#    adityas.append(anames["Vishnu"])
#    adityas.append(anames["Amshu"])
#    adityas.append(anames["Bhaga"])
#    adityas.append(anames["Pusha"])
#    adityas.append(anames["Parjanya"])
#
#    # sidereal_adityas = [adityas[11]] + adityas[:11]
#
#    nakshatraeq.append(neqnames["Krittika"])
#    nakshatraeq.append(neqnames["Rohini"])
#    nakshatraeq.append(neqnames["Mrigashira"])
#    nakshatraeq.append(neqnames["Ardra"])
#    nakshatraeq.append(neqnames["Punarvasu"])
#    nakshatraeq.append(neqnames["Pushya"])
#    nakshatraeq.append(neqnames["Ashlesha"])
#    nakshatraeq.append(neqnames["Magha"])
#    nakshatraeq.append(neqnames["Purva Phalguni"])
#    nakshatraeq.append(neqnames["Uttara Phalguni"])
#    nakshatraeq.append(neqnames["Hasta"])
#    nakshatraeq.append(neqnames["Chitra"])
#    nakshatraeq.append(neqnames["Svati"])
#    nakshatraeq.append(neqnames["Vishakha"])
#    nakshatraeq.append(neqnames["Anuradha"])
#    nakshatraeq.append(neqnames["Jyeshtha"])
#    nakshatraeq.append(neqnames["Mula"])
#    nakshatraeq.append(neqnames["Purva Ashadha"])
#    nakshatraeq.append(neqnames["Uttara Ashadha"])
#    nakshatraeq.append(neqnames["Abhijit"])
#    nakshatraeq.append(neqnames["Shravana"])
#    nakshatraeq.append(neqnames["Danishtha"])
#    nakshatraeq.append(neqnames["Shatabhisha"])
#    nakshatraeq.append(neqnames["Purva Bhadrapada"])
#    nakshatraeq.append(neqnames["Uttara Bhadrapada"])
#    nakshatraeq.append(neqnames["Revati"])
#    nakshatraeq.append(neqnames["Ashvini"])
#    nakshatraeq.append(neqnames["Bharani"])
#
#    return (
#        planets,
#        zodiac,
#        tithis,
#        karanas,
#        nakshatras,
#        varas,
#        yogas,
#        adityas,
#    )


# there are 11 karanas
# 4 happen once a lunar month
# the other 7 happen 8 times each a lunar month,
# repeating in a fixed pattern
# so the config just has 11 names
# and the function below is to organize them as
# as list of pairs in order that can easily be indexed when we know the tithi
def organize_karana(karana):
    # lets do them in order
    ret = []  # our return list or organized karana
    tmp = []  # build a list of two in tmp, then append to ret
    # then the 7 repeat in order eight times
    tmp.append(karana[0])
    for i in range(8):
        for n in range(7):
            # n+1 because, e.g., bava is at [1]
            if (
                i % 2 == 1
            ):  # i is odd, so we need to start a new pair first, if n is even
                if n % 2 == 0:
                    tmp.append(karana[n + 1])
                else:
                    tmp.append(karana[n + 1])
                    ret.append(tmp)
                    tmp = []
            else:
                if n % 2 == 0:  # n is even; append this karana to its first of the pair
                    tmp.append(karana[n + 1])
                    # this pair is done, so it can be added to ret
                    ret.append(tmp)
                    tmp = []
                else:  # n is odd; start a new pair list
                    tmp.append(karana[n + 1])
    tmp.append(karana[8])
    ret.append(tmp)
    ret.append([karana[9], karana[10]])
    return ret
