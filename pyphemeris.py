#!/usr/bin/python

import swisseph as swe
import argparse
import time
import codecs
import pyphglobals as pglob
import pyphutils as putil
from pyphprint import *
from pyphclasses import *
from pyphobjs import *

global ephtime  # a JulianDay that we are working on


def main():
    global ephtime
    args = get_args()

    if args.lang:
        pglob.init_names(args.lang)
    else:
        pglob.init_names(pglob.langfile)

    if args.edir:
        swe.set_ephe_path(args.edir)
    else:
        swe.set_ephe_path(pglob.edir)

    if args.timezone:
        pglob.timezone = args.timezone

    if args.signize:
        pglob.sign_long = not (pglob.sign_long)

    if not (pglob.sign_long):  # means they want raw longitudes
        pglob.sign_func = putil.nosignize

    if args.round:
        pglob.flground = not (pglob.flground)
    if pglob.flground:
        pglob.round_func = putil.yesround
    else:
        pglob.round_func = putil.noround

    if args.julian:
        # user entered a julian day
        ephtime = JulianDay(float(args.julian))

    if args.input: # user passed a .pyph or .chtk file
        if ".pyph" in args.input:
            name, placename, month, day, year, ephclock, lat, long = read_pyph(args.input)
        elif ".chtk" in args.input:
            name, placename, month, day, year, ephclock, lat, long = read_chtk(args.input)
        else:
            print("invalid file type")
            exit
        ephtime = JulianDay(swe.julday(year, month, day, ephclock))
        print(f"Ephemeris for {name}")
    else:
        if args.date:
            month, day, year = putil.intize_date(args.date)
        if args.time:
            ephclock = putil.intize_time(args.time)
        if args.date:
            if args.time:
                ephtime = JulianDay(swe.julday(year, month, day, ephclock))
            else:
                nowtime = time.gmtime()
                ephtime = JulianDay(
                    swe.julday(
                        year, month, day, nowtime[3] + nowtime[4] / 60 + nowtime[5] / 3600
                    )
                )
        else:
            if args.time:
                nowtime = time.gmtime()
                ephtime = JulianDay((nowtime[0], nowtime[1], nowtime[2], ephclock))
            else:
                ephtime = JulianDay()

    if args.equatorial:
        pglob.show_equ = not (pglob.show_equ)
    if args.helios:
        pglob.show_helios = not (pglob.show_helios)
    if args.baryos:
        pglob.show_baryos = not (pglob.show_baryos)
    if args.adityas:
        pglob.show_adityas = not (pglob.show_adityas)

    # always print with signs first
    # later we will check adityas and go through again if wanted
    pglob.signs = pglob.rasis

    print(f"\nDate: {ephtime.date()}\t{ephtime.usrdate()}")
    print(f"Time: {ephtime.time()}\t{ephtime.usrtime()}")

    if pglob.show_adityas:
        pglob.signs = pglob.adityas
    print_planets(ephtime, 0)
    if pglob.show_equ:
        print_planets(ephtime, pglob.EQU)
    if pglob.show_helios:
        print_planets(ephtime, pglob.HELIO)
    if pglob.show_baryos:
        print_planets(ephtime, pglob.BARY)

    if args.ayanamsa:
        pglob.ayanamsa = int(args.ayanamsa)
    print_planets_nakshatras(ephtime, pglob.ayanamsa)

    # houses

    if pglob.show_houses:
        if args.position:
            lat, long = args.position.split(",")
            pglob.lat = float(lat)
            pglob.long = long = float(long)
            pglob.placename = ""
        if args.input:
            pglob.lat = lat
            pglob.long = long
            pglob.placename = placename
        if args.house:
            pglob.hsys = args.house
        print_Cusps(
            Location(lat=pglob.lat, long=pglob.long, placename=pglob.placename), ephtime
        )
        print_Cusps_nakshatras(
            pglob.ayanamsa,
            Location(lat=pglob.lat, long=pglob.long, placename=pglob.placename),
            ephtime,
        )

    panch = Panchanga(ephtime, pglob.ayanamsa)
    print_panchanga(panch)
    if args.position:
        lat, long = args.position.split(",")
        lat = float(lat)
        long = float(long)
        if args.placename:
            placename = args.placename
        else:
            placename = ""
        print_panchanga_addendum(
            panch, Location(lat=lat, long=long, placename=placename)
        )
    else:
        print_panchanga_addendum(panch)
    print_next_new_moon(panch)
    print_next_full_moon(panch)

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
            month, day, year = putil.intize_date(value)
        if field.startswith("Ti") or field.startswith("ti"):
            ephclock = putil.intize_time(value)
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
        #print(f"{n}: {line.decode(errors='ignore')}")
        match linenum:
            case 0: # the functions used on the lines are all in chtk2pyph
                    # which i *-imported because im lazy
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
                # usually this line is HH:MM:SS
                # someimtes it is just HH:MM
                # sometimes it is just H, so deal with all of those
                line = clean_line(line).split(":")
                if(len(line)==1):
                    h = int(line[0])
                    m = s = 0
                elif(len(line)==2):
                    h = int(line[0])
                    m = int(line[1])
                    s = 0
                else:
                    h = int(line[0])
                    m = int(line[1])
                    s = int(line[2])
                utcoff = int(h)+(int(m)/60) + (int(s)/3600)
        linenum+=1
    input.close() 
    placename = city + " " + country
    ephclock = hour + min/60 + sec/3600
    return name, placename, month, day, year, ephclock+utcoff, lat, long 

def lat_to_float(lat):
    """
    change kalas lat representation into a float
    """
    # string is like this 030E44'00
    if(lat[2:3] == 'N'):
        degs = int(lat[:2])
    else:
        degs = -int(lat[:2])
    mins = int(lat[3:5])
    secs = int(lat[6:8])
    return degs + (mins / 60) + (secs / 3600)

def long_to_float(lat):
    """
    change kalas long representation into a float
    """
    # string is usually like this 030E44'00
    if(lat[3:4] == 'e'):
        degs = int(lat[:3])
    else:
        degs = -int(lat[:3])
    mins = int(lat[4:6])
    secs = int(lat[7:9])
    return degs + (mins / 60) + (secs / 3600)

def intize_line(line):
    """
    line is a string (of decoded bytes)
    we remove all the space, etc. characters, then
    can return the integer of the string
    """
    nochars = ["\x00","\r","\n"]
    count = 0
    line=list(line)
    while count < len(line):
        if(line[count] in nochars):
            del line[count]
            continue
        count+=1
    retval = int(''.join(line))
#    print(retval)
    return retval

def clean_line(line):
    """
    line is a line of bytes
    we remove all the space, carriage return, and newline characters, then
    can return the string as only a string
    """
    line=line.decode(errors='ignore')
    nochars = ["\x00","\r","\n"]
    count = 0
    line=list(line)
    while count < len(line):
        if(line[count] in nochars):
            del line[count]
            continue
        count+=1
    retval = ''.join(line)
#    print(retval)
    return retval

def get_args():
    parser = argparse.ArgumentParser(
        prog="pyphemeris",
        usage="%(prog)s [options]",
        description="get ephemeris for -dMM/DD/YYYY -tHH:MM:SS (utc)",
    )
    parser.add_argument(
        "-d",
        "--date",
        help="date specified as MM/DD/YYYY; if not present will give the current day",
    )
    parser.add_argument(
        "-t",
        "--time",
        help="time specified as HH:MM:SS, (utc); if not present will use midnight utc",
    )
    parser.add_argument("-j", "--julian", help="time specificed as the julian day")
    parser.add_argument(
        "-i", "--input", help="use date, time and position in input file; can be a .pyph or .chtk file"
    )
    parser.add_argument("-e", "--edir", help="path to swiss ephemeris files")
    parser.add_argument(
        "-a", "--ayanamsa", help="pass swisseph value for desired ayanamsa; 98 for dhruva gc mid-mula equatorial; 99 for dhruva gc mid-mula ecliptic; 100 for 28 equal nakshatras with Krittika on the ascending equinox"
    )
    parser.add_argument(
        "-u",
        "--utcoffset",
        help="utc offset in hours, positive is east; default is currently -4 (EDT)",
    )
    parser.add_argument(
        "-H",
        "--house",
        help="house system, default: C for Campanus; try R for Regiomantus",
    )
    parser.add_argument(
        "-p",
        "--position",
        help="latitude and longitutde in the form NN,EE; north and east are positive; don't pass directional letters; if latitude is negative, pass argument as -p=-30,40, for example",
    )
    parser.add_argument(
        "-P",
        "--placename",
        help="a string that describes the place given by the position argument",
    )
    parser.add_argument(
        "-s", "--helios", action="store_true", help="toggle heliocentric coordinates"
    )
    parser.add_argument(
        "-B",
        "--baryos",
        action="store_true",
        help="toggle default of barycentric coordinates - i.e., with the solar system's barycenter as the center of the coordinate system",
    )
    parser.add_argument(
        "-n",
        "--newmoon",
        action="store_true",
        help="find next new moon after date -d and time -t or -j",
    )
    parser.add_argument(
        "-f",
        "--fullmoon",
        action="store_true",
        help="find next full moon after date -d and time -t or -j",
    )
    parser.add_argument(
        "-r",
        "--rawlongn",
        action="store_true",
        help="show n planets with their longitudes not rounded",
    )
    parser.add_argument(
        "-A",
        "--adityas",
        action="store_true",
        help="toggle printing adityas from the default behavior",
    )
    parser.add_argument(
        "-E",
        "--equatorial",
        action="store_true",
        help="toggle priting equatorial coordinates from default behavior",
    )
    parser.add_argument(
        "-T",
        "--topo",
        action="store_true",
        help="toggle topocentric positions of planets; use -p to specify lat/long",
    )
    parser.add_argument("-l", "--lang", help="language file; current options: dict.eng, dict.iast, dict.deva, dict.mixed")
    parser.add_argument(
        "-z", "--timezone", help="a string showing the timezone; e.g., CDT"
    )
    parser.add_argument(
        "-S",
        "--signize",
        action="store_true",
        help="toggle longitude presentation; default is in-sign longitude; other option is raw longitude",
    )
    parser.add_argument(
        "-R",
        "--round",
        action="store_true",
        help="toggle whether output is rounded or not",
    )
    args = parser.parse_args()
    return args


main()
