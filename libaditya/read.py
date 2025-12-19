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

import codecs
import configparser

from libaditya import constants as const


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


def read_chtk(infile):
    input = open(infile, "rb")
    lines = input.readlines()
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
                sex = intize_line(codecs.decode(line))
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
                if len(line) == 1:
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
                utcoff = int(h) + (int(m) / 60) + (int(s) / 3600)
            case 13:  # dst value
                dst = intize_line(codecs.decode(line))
        linenum += 1
    input.close()
    placename = city + ", " + country
    ephclock = hour + min / 60 + sec / 3600
    return (
        name,
        placename,
        month,
        day,
        year,
        ephclock + utcoff - dst,
        lat,
        long,
        -(utcoff - dst),
    )


def read_chtk_location(infile):
    _, placename, _, _, _, _, lat, long, utcoff = read_chtk(infile)
    return placename, lat, long, utcoff


def lat_to_float(lat):
    """
    change kalas lat representation into a float
    """
    # string is like this 030E44'00
    if lat[2:3] == "N":
        degs = int(lat[:2])
    else:
        degs = -int(lat[:2])
    mins = int(lat[3:5])
    secs = int(lat[6:8])
    return degs + (mins / 60) + (secs / 3600)


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
    # string is usually like this 030E44'00
    if long[3:4] == "E":
        degs = int(long[:3])
    else:
        degs = -int(long[:3])
    mins = int(long[4:6])
    secs = int(long[7:9])
    return degs + (mins / 60) + (secs / 3600)


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
    retval = int("".join(line))
    #    print(retval)
    return retval


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
    if not isinstance(lat, float):
        if ":" in lat:
            latsign = -1 if "-" in lat else 1
            lattmp = lat.split(":")
            # if len == 2, HH:MM, otherwise, HH:MM:SS
            if len(lattmp) == 2:
                lat = latsign * (int(lattmp[0]) + int(lattmp[1]) / 60)
            else:
                lat = latsign * (
                    int(lattmp[0]) + int(lattmp[1]) / 60 + int(lattmp[2]) / 3600
                )

    if not isinstance(long, float):
        if ":" in long:
            longsign = -1 if "-" in long else 1
            longtmp = long.split(":")
            # if len == 2, HH:MM, otherwise, HH:MM:SS
            if len(longtmp) == 2:
                long = longsign * (int(longtmp[0]) + int(longtmp[1]) / 60)
            else:
                long = longsign * (
                    int(longtmp[0]) + int(longtmp[1]) / 60 + int(longtmp[2]) / 3600
                )

    # given in Kala format DD(DIR)MM('SS)
    if not isinstance(lat, float):
        if "N" in lat or "S" in lat:
            if "N" in lat:
                latsign = 1
                lattmp = lat.split("N")
            if "S" in lat:
                latsign = -1
                lattmp = lat.split("S")
            if "'" in lattmp[1]:
                min, sec = lattmp[1].split("'")
                lat = latsign * (int(lattmp[0]) + int(min) / 60 + int(sec) / 3600)
            else:
                lat = latsign * (int(lattmp[0]) + int(lattmp[1]) / 60)

    if not isinstance(long, float):
        if "E" in long or "W" in long:
            if "E" in long:
                longsign = 1
                longtmp = long.split("E")
            if "W" in long:
                longsign = -1
                longtmp = long.split("W")
            if "'" in longtmp[1]:
                min, sec = longtmp[1].split("'")
                long = longsign * (
                    int(longtmp[0]) + (int(min) / 60) + (int(sec) / 3600)
                )
            else:
                long = longsign * (int(longtmp[0]) + int(longtmp[1]) / 60)

    return lat, long


def init_names(langfile=const.base_path + "/dict/dict.mixed"):
    names = configparser.ConfigParser()
    names.read(langfile)

    # because of importing and such things
    planets = []
    zodiac = []
    tithis = []
    karanas = []
    nakshatras = []
    nakshatraeq = []
    varas = []
    yogas = []
    adityas = []

    # because of needing these names in pyphclasses i called init_names()
    # there, which when i run the whole program thus initializes them twice
    # which causes the karana especially to not work right
    # so if planets is not an empty list, then we have already done the names
    # if planets != []:
    #    return

    pnames = names["PLANETS"]
    znames = names["RASIS"]
    tnames = names["TITHI"]
    knames = names["KARANA"]
    nnames = names["NAKSHATRA"]
    neqnames = names["NAKSHATRAEQ"]
    vnames = names["VARA"]
    ynames = names["YOGAS"]
    anames = names["ADITYAS"]

    planets.append(pnames["Sun"])
    planets.append(pnames["Moon"])
    planets.append(pnames["Mercury"])
    planets.append(pnames["Venus"])
    planets.append(pnames["Mars"])
    planets.append(pnames["Jupiter"])
    planets.append(pnames["Saturn"])
    planets.append(pnames["Uranus"])
    planets.append(pnames["Neptune"])
    planets.append(pnames["Pluto"])
    planets.append(pnames["Rahu"])  # index 10
    planets.append(pnames["Ketu"])  # index 11
    planets.append([])
    planets.append([])
    planets.append(pnames["Earth"])  # so we can use swe.EARTH

    zodiac.append(znames["Aries"])
    zodiac.append(znames["Taurus"])
    zodiac.append(znames["Gemini"])
    zodiac.append(znames["Cancer"])
    zodiac.append(znames["Leo"])
    zodiac.append(znames["Virgo"])
    zodiac.append(znames["Libra"])
    zodiac.append(znames["Scorpio"])
    zodiac.append(znames["Sagittarius"])
    zodiac.append(znames["Capricorn"])
    zodiac.append(znames["Aquarius"])
    zodiac.append(znames["Pisces"])

    tithis.append(tnames["Nanda"])
    tithis.append(tnames["Bhadra"])
    tithis.append(tnames["Jaya"])
    tithis.append(tnames["Rkta"])
    tithis.append(tnames["Purna"])

    karanas.append(knames["Kimtughna"])
    karanas.append(knames["Bava"])
    karanas.append(knames["Balava"])
    karanas.append(knames["Kaulava"])
    karanas.append(knames["Taitula"])
    karanas.append(knames["Garija"])
    karanas.append(knames["Vanija"])
    karanas.append(knames["Vishti"])
    karanas.append(knames["Shakuni"])
    karanas.append(knames["Chatushpada"])
    karanas.append(knames["Naga"])
    karanas = organize_karana(karanas)

    nakshatras.append(nnames["Ashvini"])
    nakshatras.append(nnames["Bharani"])
    nakshatras.append(nnames["Krittika"])
    nakshatras.append(nnames["Rohini"])
    nakshatras.append(nnames["Mrigashira"])
    nakshatras.append(nnames["Ardra"])
    nakshatras.append(nnames["Punarvasu"])
    nakshatras.append(nnames["Pushya"])
    nakshatras.append(nnames["Ashlesha"])
    nakshatras.append(nnames["Magha"])
    nakshatras.append(nnames["Purva Phalguni"])
    nakshatras.append(nnames["Uttara Phalguni"])
    nakshatras.append(nnames["Hasta"])
    nakshatras.append(nnames["Chitra"])
    nakshatras.append(nnames["Svati"])
    nakshatras.append(nnames["Vishakha"])
    nakshatras.append(nnames["Anuradha"])
    nakshatras.append(nnames["Jyeshtha"])
    nakshatras.append(nnames["Mula"])
    nakshatras.append(nnames["Purva Ashadha"])
    nakshatras.append(nnames["Uttara Ashadha"])
    nakshatras.append(nnames["Shravana"])
    nakshatras.append(nnames["Danishtha"])
    nakshatras.append(nnames["Shatabhisha"])
    nakshatras.append(nnames["Purva Bhadrapada"])
    nakshatras.append(nnames["Uttara Bhadrapada"])
    nakshatras.append(nnames["Revati"])

    varas.append(vnames["Ravivara"])
    varas.append(vnames["Somavara"])
    varas.append(vnames["Mangalavara"])
    varas.append(vnames["Budhavara"])
    varas.append(vnames["Guruvara"])
    varas.append(vnames["Shukravara"])
    varas.append(vnames["Shanivara"])

    yogas.append(ynames["Vishkambha"])
    yogas.append(ynames["Priti"])
    yogas.append(ynames["Ayushman"])
    yogas.append(ynames["Saubhagya"])
    yogas.append(ynames["Shobana"])
    yogas.append(ynames["Atiganda"])
    yogas.append(ynames["Sukarma"])
    yogas.append(ynames["Dhriti"])
    yogas.append(ynames["Shoola"])
    yogas.append(ynames["Ganda"])
    yogas.append(ynames["Vriddhi"])
    yogas.append(ynames["Dhruva"])
    yogas.append(ynames["Vyaghata"])
    yogas.append(ynames["Harshana"])
    yogas.append(ynames["Vajra"])
    yogas.append(ynames["Siddhi"])
    yogas.append(ynames["Vyatipata"])
    yogas.append(ynames["Variyan"])
    yogas.append(ynames["Parigha"])
    yogas.append(ynames["Shiva"])
    yogas.append(ynames["Siddha"])
    yogas.append(ynames["Sadhya"])
    yogas.append(ynames["Shubha"])
    yogas.append(ynames["Shukla"])
    yogas.append(ynames["Brahma"])
    yogas.append(ynames["Indra"])
    yogas.append(ynames["Vaidhriti"])

    adityas.append(anames["Dhata"])
    adityas.append(anames["Aryama"])
    adityas.append(anames["Mitra"])
    adityas.append(anames["Varuna"])
    adityas.append(anames["Indra"])
    adityas.append(anames["Vivasvan"])
    adityas.append(anames["Tvashta"])
    adityas.append(anames["Vishnu"])
    adityas.append(anames["Amshu"])
    adityas.append(anames["Bhaga"])
    adityas.append(anames["Pusha"])
    adityas.append(anames["Parjanya"])

    # sidereal_adityas = [adityas[11]] + adityas[:11]

    nakshatraeq.append(neqnames["Krittika"])
    nakshatraeq.append(neqnames["Rohini"])
    nakshatraeq.append(neqnames["Mrigashira"])
    nakshatraeq.append(neqnames["Ardra"])
    nakshatraeq.append(neqnames["Punarvasu"])
    nakshatraeq.append(neqnames["Pushya"])
    nakshatraeq.append(neqnames["Ashlesha"])
    nakshatraeq.append(neqnames["Magha"])
    nakshatraeq.append(neqnames["Purva Phalguni"])
    nakshatraeq.append(neqnames["Uttara Phalguni"])
    nakshatraeq.append(neqnames["Hasta"])
    nakshatraeq.append(neqnames["Chitra"])
    nakshatraeq.append(neqnames["Svati"])
    nakshatraeq.append(neqnames["Vishakha"])
    nakshatraeq.append(neqnames["Anuradha"])
    nakshatraeq.append(neqnames["Jyeshtha"])
    nakshatraeq.append(neqnames["Mula"])
    nakshatraeq.append(neqnames["Purva Ashadha"])
    nakshatraeq.append(neqnames["Uttara Ashadha"])
    nakshatraeq.append(neqnames["Abhijit"])
    nakshatraeq.append(neqnames["Shravana"])
    nakshatraeq.append(neqnames["Danishtha"])
    nakshatraeq.append(neqnames["Shatabhisha"])
    nakshatraeq.append(neqnames["Purva Bhadrapada"])
    nakshatraeq.append(neqnames["Uttara Bhadrapada"])
    nakshatraeq.append(neqnames["Revati"])
    nakshatraeq.append(neqnames["Ashvini"])
    nakshatraeq.append(neqnames["Bharani"])

    return (
        planets,
        zodiac,
        tithis,
        karanas,
        nakshatras,
        varas,
        yogas,
        adityas,
    )


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
