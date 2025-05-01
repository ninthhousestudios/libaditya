#!/usr/bin/python

import swisseph as swe
import argparse
import time
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
            nowtime - time.gmtime()
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

    print(f"\nDate: {ephtime.date()}\t\t{ephtime.usrdate()}")
    print(f"Time: {ephtime.time()}\t{ephtime.usrtime()}")

    print_planets(ephtime, 0)
    if pglob.show_equ:
        print_planets(ephtime, pglob.EQU)
    if pglob.show_helios:
        print_planets(ephtime, pglob.HELIO)
    if pglob.show_baryos:
        print_planets(ephtime, pglob.BARY)

    if pglob.show_adityas:
        pglob.signs = pglob.adityas
        print_planets(ephtime, pglob.ECL)
        if pglob.show_equ:
            print_planets(ephtime, pglob.EQU)
        if pglob.show_helios:
            print_planets(ephtime, pglob.HELIO)
        if pglob.show_baryos:
            print_planets(ephtime, pglob.BARY)

    # houses

    if pglob.show_houses:
        if args.position:
            lat, long = args.position.split(",")
            pglob.lat = float(lat)
            pglob.long = long = float(long)
        if args.house:
            pglob.hsys = args.house
        print_Cusps(Location(lat=pglob.lat, long=pglob.long), ephtime)


def get_args():
    parser = argparse.ArgumentParser(
        prog="ephemeris",
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
    parser.add_argument("-e", "--edir", help="path to swiss ephemeris files")
    parser.add_argument(
        "-a", "--ayanamsa", help="pass swisseph value for desired ayanamsa"
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
    parser.add_argument("-l", "--lang", help="language file; default is ./dict.eng")
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
