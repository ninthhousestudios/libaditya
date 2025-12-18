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
from dataclasses import replace


from libaditya import constants as const
from libaditya import utils
from libaditya import read
import defaults
from libaditya.objects import JulianDay, Planets, Cusps, EphContext, Location, Names
from libaditya.calc import Panchanga


def main():
    args = get_args()

    if args.edir:
        ephe_path = args.edir
    else:
        ephe_path = defaults.edir

    if os.path.exists(ephe_path):
        swe.set_ephe_path(ephe_path)
    else:
        # swe recommends calling this even if using builtin ephemeris
        swe.set_ephe_path()

    if args.lang:
        lang_file = defaults.dict_path + args.lang
    else:
        lang_file = defaults.lang_file

    (
        planet_names,
        zodiac,
        tithis,
        karanas,
        nakshatras,
        varas,
        yogas,
        adityas,
        sidereal_adityas,
    ) = read.init_names(lang_file)
    planet_names.append("Chiron")


    if args.zodiac:
        sign_names = zodiac
    elif defaults.signs == "zodiac":
        sign_names = zodiac
    else:
        sign_names = adityas

    names = Names(planet_names,sign_names,nakshatras,tithis,karanas,varas,yogas)

    if args.timezone:
        timezone = args.timezone
    else:
        timezone = defaults.timezone

    signize = defaults.signize
    if args.signize:
        signize = not (defaults.signize)

    toround = defaults.toround
    if args.round:
        toround[0] = not (defaults.toround[0])
    else:
        toround = defaults.toround

    ayanamsa = 98
    if args.ayanamsa:
        ayanamsa = int(args.ayanamsa)

    if args.house_system:
        hsys = args.house_system[0]
    else:
        hsys = defaults.hsys

    timezone = "UTC"
    name = ""
    if args.input:  # user passed a .pyph or .chtk file
        name, placename, month, day, year, timedec, lat, long, utcoffset = (
            parse_input_file(args.input)
        )
    else:
        name = ""
        placename = ""
        utcoffset = defaults.utcoffset
        month, day, year, timedec = parse_date_time(args.date, args.time)

    if args.position:
        lat, long, placename, utcoffset, timezone = parse_position(
            args.position, args.placename, args.timezone
        )
    
    # use defaults for position if not given by input file or args.position
    if not args.position and not args.input:
        lat, long, placename, utcoffset = (
            defaults.lat,
            defaults.long,
            defaults.placename,
            defaults.utcoffset,
        )

    # the time and place for our computations for this ephemeris
    timeJD = JulianDay((year, month, day, timedec), utcoffset, timezone)
    location = Location(lat, long, 0, placename, timeJD.mktimezone())

    if args.julian:
        # user entered a julian day
        timeJD = JulianDay(float(args.julian))

    # decide which coordinates system the user wants displayed
    to_show = [const.ECL]
    show_sidereal = 0
    if args.equatorial:
        show_equ = not (defaults.show_equ)
        if show_equ:
            to_show.append(const.EQU)
    if args.helios:
        show_helios = not (defaults.show_helios)
        if show_helios:
            to_show.append(const.HELIO)
    if args.baryos:
        show_baryos = not (defaults.show_baryos)
        if show_baryos:
            to_show.append(const.BARY)
    if args.topo:
        show_topo = not (defaults.show_topo)
        if show_topo:
            to_show.append(const.TOPO)
    if args.draconic:
        show_drac = not (defaults.show_drac)
        if show_drac:
            to_show.append(const.DRAC)
    if args.sidereal:
        show_sidereal = not (defaults.show_sidereal)
        if show_sidereal:
            to_show.append(const.SID)
            if args.topo:
                if show_topo:
                    to_show.append(const.SID | const.TOPO)
            if args.ayanamsa:
                ayanamsa = int(args.ayanamsa)
            else:
                ayanamsa = 27


    ########################################################
    #                                                      #
    #                                                      #
    #         start acutally printing stuff                #
    #                                                      #
    #                                                      #
    ########################################################

    # @dataclass
    # class EphContext:
    #     timeJD: JulianDay = JulianDay()
    #     location: Location = Location()
    #     sysflg: int = const.ECL
    #     ayanamsa: int = 98
    #     signize: bool = True
    #     toround: (bool,int) = (True,3)
    #     hsys: str = 'C'
    #     names = Names = Names()
    #
    # @dataclass(frozen=True)
    # class Names:
    #     planet_names: str = tuple(const.planet_names)
    #     sign_names: str = tuple(const.adityas)
    #     nakshatras: str = tuple(const.nakshatras)
    #     tithis: str =  tuple(const.tithis)
    #     karanas: str = tuple(const.karanas)
    #     varas: str = tuple(const.varas)
    #     yogas: str = tuple(const.yogas)

    context = EphContext(timeJD,location,const.ECL,ayanamsa,hsys,signize,toround,names)

    print(f"\nEphemeris for {name}\n")

    print(f"Date: {timeJD.date()}\t{timeJD.usrdate()}")
    print(f"Time: {timeJD.time()}\t{timeJD.usrtime()}\n")

    # print planetary positions in all coordinates and types the users wants


    for sys in to_show:
        if sys == const.SID and sign_names == adityas:
            if context.ayanamsa == -1:
                # tropical ayanamsa, so set sys=const.ECL
                print(Planets(replace(context,sysflg=const.ECL)))
            # if sign_names == zodiac, then we are using the zodiac
            print(Planets(replace(context,sysflg=sys,names=Names(planet_names,sidereal_adityas,nakshatras,tithis,karanas,varas,yogas))))
            print("\n")
            continue
        if sys == const.DRAC:
            dracon = replace(context,sysflg=sys,names=Names(planet_names,zodiac,nakshatras,tithis,karanas,varas,yogas))
            print(Planets(dracon))
            print("\n")
            print(Cusps(dracon))
            print("\n")
            continue
        print(Planets(replace(context,sysflg=sys)))
        print("\n")

    print(Planets(context).nakshatras())

    # now for house cusps
    print("\n")
    for sys in to_show:
        if sys == const.SID and sign_names == adityas:
            # if sign_names == zodiac, then we are using the zodiac
            context = EphContext(timeJD,location,sys,ayanamsa,hsys,signize,toround,Names(planet_names,sidereal_adityas,nakshatras,tithis,karanas,varas,yogas))
            print(Cusps(context))
            print("\n")
        if sys == const.ECL:
            print(Cusps(EphContext(timeJD,location,sys,ayanamsa,hsys,signize,toround,names)))
            print("\n")


    print(Cusps(context).nakshatras())

    p=Panchanga(context)
    print(p)
    p.print_addendum()
    p.print_next_new_moon()
    p.print_next_full_moon()



# end main function
def parse_input_file(input):
    if ".pyph" in input:
        name, placename, month, day, year, ephclock, lat, long = read.read_pyph(input)
    elif ".chtk" in input:
        name, placename, month, day, year, ephclock, lat, long, utcoffset = (
            read.read_chtk(input)
        )
        utcoffset = round(utcoffset, 1)
    else:
        print("invalid file type")
        exit
    return name, placename, month, day, year, ephclock, lat, long, utcoffset


def parse_date_time(date, time):
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
        rettime = nowtime[3] + nowtime[4] / 60 + nowtime[5] / 3600
    return month, day, year, rettime


def parse_position(position, placname, timezone):
    if ".chtk" in position:
        placename, lat, long, utcoffset = read.read_chtk_location(position)
        timezone = "UTC"
    else:
        lat, long = read.parse_position_argument(position)
        lat = lat
        long = long
        placename = placename
        utcoffset = 0
        timezone = timezone
    return lat, long, placename, utcoffset, timezone


def get_args():
    parser = argparse.ArgumentParser(
        prog="pyphemeris",
        usage="%(prog)s [options]",
        description="get ephemeris for -dMM/DD/YYYY -tHH:MM:SS (utc)",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="use date, time and position from input file; can be a .pyph or .chtk file",
    )
    parser.add_argument(
        "-d",
        "--date",
        help="date specified as MM/DD/YYYY; if not present will use day at runtime",
    )
    parser.add_argument(
        "-t",
        "--time",
        help="time specified as HH:MM(:SS); must be UTC ; if not present will use time at runtime",
    )
    parser.add_argument(
        "-a",
        "--ayanamsa",
        help="integer value for desired ayanamsa; use any valid swisseph value; 98 for dhruva gc mid-mula (default); 99 for ecliptic vedanga jyotisha; 100 for equatorial vedanga jyotisha; -8 for tropical, i.e., put ashvini at the equinox",
    )
    parser.add_argument(
        "-p",
        "--position",
        help="latitude and longitutde in the form NN,EE; north and east are positive; don't pass directional letters; if latitude is negative, pass argument as -p=-30,40, for example; if you pass a .chtk file, it will read and use the position in that file; use -z and -P to set strings for timezone and placename, if desired",
    )
    parser.add_argument(
        "-H",
        "--house-system",
        help="house system, default: C for Campanus; try R for Regiomantus",
    )
    parser.add_argument(
        "-Z",
        "--zodiac",
        action="store_true",
        help="toggle use of zodiac signs; can set default variable 'signs' in defaults.py",
    )
    parser.add_argument(
        "-S",
        "--sidereal",
        action="store_true",
        help="print positions in sidereal longitude; pass an ayanamsa value with the -a/--ayanamsa option; if none is passed, will default to number 27, True Chitra ayanamsa",
    )
    parser.add_argument(
        "-helio",
        "--helios",
        action="store_true",
        help="toggle heliocentric coordinates",
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
        "-D",
        "--draconic",
        action="store_true",
        help="print positions for a tropical draconic chart, where Rahu = 0 Aries",
    )
    parser.add_argument(
        "-T",
        "--topo",
        action="store_true",
        help="toggle topocentric positions of planets; can use -p to specify lat/long; if passing an input file, -p argument will override that location information",
    )
    parser.add_argument(
        "-l",
        "--lang",
        help="language file; current options: dict.eng, dict.iast, dict.deva, dict.mixed",
    )
    parser.add_argument("-j", "--julian", help="time specificed as a julian day")
    parser.add_argument(
        "-e",
        "--edir",
        help="path to swiss ephemeris files; default can be set in constants.py",
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
    parser.add_argument(
        "-z", "--timezone", help="a string showing the timezone; e.g., CDT; note: this is just a string pyphemeris will print; pyphemeris does not deal wiht timezones!"
    )
    parser.add_argument(
        "-P", "--placename", help="a string showing the placename; e.g., CDT"
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
