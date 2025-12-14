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
import time
import pyphglobals as pglob
import pyphutils as putil
import pyphread as pread
from pyphprint import *
from pyphclasses import *
from pyphobjs import *


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


    if args.input: # user passed a .pyph or .chtk file
        if ".pyph" in args.input:
            name, placename, month, day, year, ephclock, lat, long = pread.read_pyph(args.input)
        elif ".chtk" in args.input:
            name, placename, month, day, year, ephclock, lat, long = pread.read_chtk(args.input)
            pglob.placename, pglob.lat, pglob.long, pglob.utcoffset = pread.read_chtk_location(args.input)
            sign = ""
            if pglob.utcoffset > 0:
                sign = "+"
            pglob.timezone = "UTC" + sign + str(pglob.utcoffset)
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

    if args.julian:
        # user entered a julian day
        ephtime = JulianDay(float(args.julian))

    if args.equatorial:
        pglob.show_equ = not (pglob.show_equ)
    if args.helios:
        pglob.show_helios = not (pglob.show_helios)
    if args.baryos:
        pglob.show_baryos = not (pglob.show_baryos)
    if args.adityas:
        pglob.show_adityas = not (pglob.show_adityas)
    if args.vdasha:
        pglob.show_vdasha = not (pglob.show_vdasha)


    print(f"\nDate: {ephtime.date()}\t{ephtime.usrdate()}")
    print(f"Time: {ephtime.time()}\t{ephtime.usrtime()}")

    if not pglob.show_adityas:
        pglob.signs = pglob.rasis
    print_planets(ephtime)
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
    if args.position:
        if ".chtk" in args.position:
            pglob.placename, pglob.lat, pglob.long, pglob.utcoffset = pread.read_chtk_location(args.position)
            sign = ""
            if pglob.utcoffset > 0:
                sign = "+"
            pglob.timezone = "UTC" + sign + str(pglob.utcoffset)
        else:
            lat, long = putil.parse_position_argument(args.position)
            pglob.lat = lat
            pglob.long = long
            if args.placename:
                pglob.placename = args.placename
            else:
                pglob.placename = ""

    if pglob.show_houses:
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
    print_panchanga_addendum(
        panch, Location(lat=pglob.lat, long=pglob.long, placename=pglob.placename)
    )
    print_next_new_moon(panch)
    print_next_full_moon(panch)

    if args.dasha_levels:
        pglob.dasha_levels = int(args.dasha_levels)

    if args.dasha_year_length:
        for opt in pglob.dasha_years:
            if opt[0][:3] in args.dasha_year_length.lower():
                yrlen = opt[1]
        if yrlen == 0:
            # the option was not recognized
            print(f"year length not recognized, using saura year")
            yrlen = pglob.saura_year
    else:
        yrlen = pglob.saura_year

    if pglob.show_vdasha:
        # print_vimshottari_dasha takes a Panchanga
        # since we need the Moon and the ayanamsha
        # so all the information is there
        yrlen=pglob.saura_year
        print_vimshottari_dasha(panch,pglob.dasha_levels,yrlen)

    if args.v2dasha:
        pglob.show_v2dasha = not pglob.show_v2dasha

    if pglob.show_v2dasha:
        # print_vimshottari_dasha takes a Panchanga
        # since we need the Moon and the ayanamsha
        # so all the information is there
        yrlen=pglob.saura_year
        vdasha = calculate_vimshottari_dasha(ephtime,pglob.dasha_levels,yrlen)
        print("\n\nVimshottari Dasha\n")

        for opt in pglob.dasha_years:
            if yrlen == opt[1]:
                yrstr = opt[0].capitalize()

        print(f"Using {yrstr} year length")
        print_dasha(vdasha)

    if args.current_dasha: 
        if not args.dasha_levels:
           # if user didnt pass a level argument, change default to 3
           pglob.dasha_levels = 3

        # what time to show current dasha for?
        # assume user inputs a file with -i
        # then -d and -t can be used to find dasha at time specified by -d/-t
        if args.date:
            month, day, year = putil.intize_date(args.date)
        if args.time:
            nowclock = putil.intize_time(args.time)
        if args.date:
            if args.time:
                nowtime = JulianDay(swe.julday(year, month, day, nowclock))
            else:
                nowtime = time.gmtime()
                nowtime = JulianDay(
                    swe.julday(
                        year, month, day, nowtime[3] + nowtime[4] / 60 + nowtime[5] / 3600
                    )
                )
        else:
            if args.time:
                nowtime = time.gmtime()
                nowtime = JulianDay((nowtime[0], nowtime[1], nowtime[2], nowclock))
            else:
                nowtime = JulianDay()

        print_current_dasha(ephtime,nowtime,pglob.dasha_levels)


def get_args():
    parser = argparse.ArgumentParser(
        prog="pyphemeris",
        usage="%(prog)s [options]",
        description="get ephemeris for -dMM/DD/YYYY -tHH:MM:SS (utc)",
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
    parser.add_argument("-j", "--julian", help="time specificed as a julian day")
    parser.add_argument(
        "-i", "--input", help="use date, time and position from input file; can be a .pyph or .chtk file"
    )
    parser.add_argument("-e", "--edir", help="path to swiss ephemeris files; default can be set in pyphglobals.py")
    parser.add_argument(
            "-a", "--ayanamsa", help="pass swisseph value for desired ayanamsa; 101 for dhruva gc mid-mula equatorial; 98 for dhruva gc mid-mula equatorial (NOT A CORRECT IMPLEMENTATION); 99 for dhruva gc mid-mula ecliptic (based on 98, so NOT A CORRECT IMPLEMENTATION); 100 for 28 equal nakshatras with Krittika on the ascending equinox; 102 is ecliptic vedanga jyotisha: 27 equal tropical nakshatras with dhanishta starting at the southern solstice; 103 is equatorial vedanga jyotisha"
    )
    parser.add_argument(
        "-u",
        "--utcoffset",
        help="utc offset in hours, positive is east; note: this is only for printing purposes; for computing the ephemeris pyphemeris only understands time in UTC or julian days; default set in pyphglobals.py",
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
        "-V",
        "--vdasha",
        action="store_true",
        help="toggle printing vimshottari dasha from default",
    )
    parser.add_argument(
        "-V2",
        "--v2dasha",
        action="store_true",
        help="toggle printing vimshottari dasha from default",
    )
    parser.add_argument(
        "-C",
        "--current-dasha",
        action="store_true",
        help="print current dasha; use -L to specify how many levels; default is 3",
    )
    parser.add_argument(
        "-L",
        "--dasha-levels",
        help="how many dasha levels to print; if not given uses default in pyphglobals",
    )
    parser.add_argument(
        "-Y",
        "--dasha-year-length",
        help="which year length to use for dashas; default is Saura; options: Nakshatra = 359.0167 standard days; Savana = 360 standard days; Saura = 365.2422; Sidereal = 365.2564; Chandra = 364.2888; Lunar = 354.36708",
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

if __name__ == "__main__":
    main()
