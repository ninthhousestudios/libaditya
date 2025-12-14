#!/usr/bin/python

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
import argparse
import time as tmod
import os
from dataclasses import dataclass

import constants as const
import utils
import read
from objects import *


def main():
    args = get_args()

    if args.edir:
        ephe_path = args.edir
    else:
        ephe_path = const.edir

    if os.path.exists(ephe_path):
        swe.set_ephe_path(ephe_path)

    if args.lang:
        lang_file = const.dict_path + args.lang
    else:
        lang_file = const.lang_file

    if args.timezone:
        timezone = args.timezone
    else:
        timezone = const.timezone

    if args.signize:
        sign_long = not (const.sign_long)

    if not (const.sign_long):  # means they want raw longitudes
        sign_func = utils.nosignize

    if args.round:
        flground = not (const.flground)

    if const.flground:
        round_func = utils.yesround
    else:
        round_func = utils.noround


    if args.input: # user passed a .pyph or .chtk file
        name, placename, month, day, year, timedec, lat, long, utcoffset, timezone = parse_input_file(args.input)
    else:
        name = ""
        placename = ""
        utcoffset = const.utcoffset 
        timezone = const.timezone
        month, day, year, timedec = parse_date_time(args.date,args.time)

    lat, long, position, position_utcoffset = parse_position(args.position)
    timeJD = JulianDay((year,month,day,timedec),utcoffset,timezone)


    if args.julian:
        # user entered a julian day
        timeJD = JulianDay(float(args.julian))


    if args.equatorial:
        show_equ = not (const.show_equ)
    if args.helios:
        show_helios = not (const.show_helios)
    if args.baryos:
        show_baryos = not (const.show_baryos)
    if args.topo:
        show_topo = not (const.show_topo)


    ayanamsa = 0
    sysflg = const.ECL
    if args.equatorial:
        sysflg = const.EQU
    if args.helios:
        sysflg = const.HELIO
    if args.baryos:
        sysflg = const.BARY
    if args.sidereal:
        sysflg = const.SID
        if args.ayanamsa:
            ayanamsa = int(args.ayanamsa)
        else:
            ayanamsa = 1

    context = EphContext(timeJD,sysflg,ayanamsa)

    planets = Planets(context)
    print("print all planets")
    for p in planets:
        print(p)


# end main function
def parse_input_file(input):
    if ".pyph" in input:
        name, placename, month, day, year, ephclock, lat, long = read.read_pyph(input)
    elif ".chtk" in input:
        name, placename, month, day, year, ephclock, lat, long, utcoffset = read.read_chtk(input)
        utcoffset = round(utcoffset,1)
        sign = ""
        if utcoffset > 0:
            sign = "+"
        timezone = "UTC" + sign + str(utcoffset)
    else:
        print("invalid file type")
        exit
    return name, placename, month, day, year, ephclock, lat, long, utcoffset, timezone

def parse_date_time(date,time):
    nowtime = tmod.gmtime()
    if date:
        month, day, year = utils.intize_date(date)
    else:
        # get current date
        month = nowtime[1]
        day = nowtime[2]
        year = nowtime[0]
    if time:
        rettime = utils.intize_time(time)
    else:
        # get current time
        time = nowtime[3] + nowtime[4] / 60 + nowtime[5] / 3600
    return month, day, year, time

def parse_position(position):
    if not position:
        return const.lat, const.long, const.placename, const.utcoffset
    if ".chtk" in position:
        placename, lat, long, utcoffset = read.read_chtk_location(position)
        sign = ""
        if utcoffset > 0:
            sign = "+"
        timezone = "UTC" + sign + str(utcoffset)
    else:
        lat, long = read.parse_position_argument(position)
        lat = lat
        long = long
        placename = ""
        utcoffset = ""
    return lat, long, placename, utcoffset

def get_args():
    parser = argparse.ArgumentParser(
        prog="pyphemeris",
        usage="%(prog)s [options]",
        description="get ephemeris for -dMM/DD/YYYY -tHH:MM:SS (utc)",
    )
    parser.add_argument(
        "-i", "--input", help="use date, time and position from input file; can be a .pyph or .chtk file"
    )
    parser.add_argument(
        "-d",
        "--date",
        help="date specified as MM/DD/YYYY; if not present will use day at runtime",
    )
    parser.add_argument(
        "-t",
        "--time",
        help="time specified as HH:MM:SS, (utc); if not present will use time at runtime",
    )
    parser.add_argument(
        "-p",
        "--position",
        help="latitude and longitutde in the form NN,EE; north and east are positive; don't pass directional letters; if latitude is negative, pass argument as -p=-30,40, for example; if you pass a .chtk file, it will read and use the position in that file",
    )
    parser.add_argument(
        "-a", "--ayanamsa", help="integer value for desired ayanamsa; use any valid swisseph value; 98 for dhruva gc mid-mula (default); 99 for ecliptic vedanga jyotisha; 100 for equatorial vedanga jyotisha"
    )
    parser.add_argument("-l", "--lang", help="language file; current options: dict.eng, dict.iast, dict.deva, dict.mixed")
    parser.add_argument("-j", "--julian", help="time specificed as a julian day")
    parser.add_argument("-e", "--edir", help="path to swiss ephemeris files; default can be set in constants.py")
    parser.add_argument(
        "-z", "--timezone", help="a string showing the timezone; e.g., CDT"
    )
    parser.add_argument(
        "-H", "--helios", action="store_true", help="toggle heliocentric coordinates"
    )
    parser.add_argument(
        "-B",
        "--baryos",
        action="store_true",
        help="toggle default of barycentric coordinates - i.e., with the solar system's barycenter as the center of the coordinate system",
    )
    parser.add_argument(
        "-E",
        "--equatorial",
        action="store_true",
        help="toggle priting equatorial coordinates from default behavior",
    )
    parser.add_argument(
        "-S", "--sidereal", action="store_true", help="print positions in sidereal longitude; pass an ayanamsa value with the -a/--ayanamsa option; if none is passed, will default to number 1, Lahiri"
    )
    parser.add_argument(
        "-T",
        "--topo",
        action="store_true",
        help="toggle topocentric positions of planets; use -p to specify lat/long",
    )
    parser.add_argument(
        "-s",
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

if __name__ == "__main__":
    main()
