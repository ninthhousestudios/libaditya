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
import os
from dataclasses import replace


from libaditya import constants as const
from libaditya import utils
from libaditya import read
from libaditya import print_functions as printf

from libaditya.objects import JulianDay, Planets, Cusps, EphContext, Location, Names, Circle, Sun, Moon
from libaditya.calc import Panchanga, print_vimshottari_dasha, calculate_vimshottari_dasha
from libaditya.calc import print_calculated_vimshottari_dasha, lunar_new_year, print_cardinal_points, current_vimshottari_dasha
from libaditya.calc import next_dasha_lords
from libaditya.charts import Chart

import defaults
import parse

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

    planet_names, zodiac, tithis, karanas, nakshatras, varas, yogas, adityas = read.init_names(lang_file)


    if args.zodiac:
        sign_names = zodiac
        circle = Circle.ZODIAC
    elif defaults.signs == "zodiac":
        sign_names = zodiac
        circle = Circle.ZODIAC
    else:
        sign_names = adityas
        circle = Circle.ADITYA

    names = Names(planet_names,sign_names,nakshatras,tithis,karanas,varas,yogas)

    print_nakshatras = defaults.print_nakshatras
    if args.nakshatras:
        print_nakshatras = not (print_nakshatras)

    print_outer_planets = defaults.print_outer_planets
    if args.outer_planets:
        print_outer_planets = not (print_outer_planets)

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
        name, placename, month, day, year, timedec, lat, long, utcoffset = (parse.parse_input_file(args.input))
    else:
        name = ""
        placename = ""
        utcoffset = defaults.utcoffset
        month, day, year, timedec = parse.parse_date_time(args.date, args.time)

    if args.position:
        lat, long, placename, utcoffset, timezone = parse.parse_position(
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

    to_show = parse.coords_to_show(args)

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
    #     hsys: str = 'C'
    #     circle: Circle = Circle
    #     signize: bool = True
    #     toround: (bool,int) = (True,3)
    #     print_nakshatras: bool = True
    #     print_outer_planets: bool = True
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

    context = EphContext(timeJD,location,const.TROP,ayanamsa,hsys,circle,signize,toround,print_nakshatras,print_outer_planets,names)
    # print kala information and exit
    if args.kala:
        print_kala(context)
        exit()

    ephemeris_mode = defaults.epehemeris_mode
    if args.ephemeris_mode:
        ephemeris_mode = not (ephemeris_mode)

    chart_mode = defaults.chart_mode
    if args.chart_mode:
        chart_mode = not(chart_mode)

    if ephemeris_mode:

        print(f"\nEphemeris for {name}\n")

        print(f"Date: {timeJD.date()}\t{timeJD.usrdate()}")
        print(f"Time: {timeJD.time()}\t{timeJD.usrtime()}\n")

        # print planetary positions in all coordinates and types the users wants

        print_ephemeris(context,to_show)

    if chart_mode and not ephemeris_mode:
        if args.helio_chart:
            context = replace(context,sysflg=const.HELIO)
            print_chart(name,args,context)
            exit()
        if args.baryos_chart:
            context = replace(context,sysflg=const.BARY)
            print_chart(name,args,context)
            exit()
        if args.sidereal_chart:
            if not args.aditya:
                # use zodiac circle and signs
                context = replace(context,sysflg=const.SID,circle=circle.ZODIAC,names=replace(names,sign_names=zodiac))
                chart = print_chart(name,args,context)
                print_planetary_aspects(args,chart)
                print_vargas(args,chart)
            else:
                # use sidereal aditya circle and signs
                context = replace(context,sysflg=const.SID,circle=circle.SIDEREAL_ADITYA,names=replace(names,sign_names=adityas))
                chart = print_chart(name,args,context)
                print_planetary_aspects(args,chart)
                print_vargas(args,chart)
        else:
            # default sysflg in context is const.TROP, set above
            chart = print_chart(name,args,replace(context))
            print_planetary_aspects(args,chart)
            print_vargas(args,chart)

    # do vimshottari dasha
    # this function takes care of deciding to print them
    # so if there is nothing to print, it will not print anything
    print_dashas(args,context)
# end main function

def print_chart(name,args,context):
    print(f"\nChart for {name}\n")
    chart = Chart(context)
    print(chart)
    return chart

def print_planetary_aspects(args,chart):
    planetary_aspects = defaults.planetary_aspects
    if args.planetary_aspects:
        planetary_aspects = not (planetary_aspects)
    planetary_cusps_aspects = defaults.planetary_cusps_aspects
    if args.planetary_cusps_aspects:
        planetary_cusps_aspects = not (planetary_cusps_aspects)
    if planetary_aspects:
        print(f"\nPlanetary Aspect Table")
        print(printf.parashara_aspect_table_planets(chart.rashi().planets().parashara_aspects()))
    if planetary_cusps_aspects:
        print(f"\nCusp Aspect Table")
        print(printf.parashara_aspect_table_cusps(chart.rashi().planets().parashara_aspects_cusps(chart.rashi().cusps())))

def print_vargas(args,chart):
    if not args.vargas:
        return
    vargas = [int(varga) for varga in args.vargas.split(',')]

    for varga in vargas:
        print(chart.get_varga(varga))

def print_ephemeris(context,to_show):
    for sys in to_show:
        if sys == const.SID:
            if context.ayanamsa == -1:
                # tropical ayanamsa, so set sys=const.ECL
                print(Planets(replace(context,sysflg=const.ECL)))
                continue
            if context.circle == Circle.ADITYA:
                print(Planets(replace(context,sysflg=sys,circle=Circle.SIDEREAL_ADITYA)))
                print("\n")
                continue
        if sys == const.DRAC:
            dracon = replace(context,sysflg=sys,names=replace(names,sign_names=zodiac))
            print(Planets(dracon))
            print("\n")
            print(Cusps(dracon))
            print("\n")
            continue
        if sys == const.BARY or sys == const.HELIO:
            print(repr(Planets(replace(context,sysflg=sys))))
            print("\n")
            continue
        print(Planets(replace(context,sysflg=sys)))
        print("\n")

    # now for house cusps
    for sys in to_show:
        if sys == const.SID and context.ayanamsa == -1:
                # tropical ayanamsa, so set sys=const.ECL
            print(Cusps(replace(context,sysflg=const.ECL)))
        if sys == const.ECL:
            print(Cusps(context))
            print("\n")
        if sys == const.SID:
            print(Cusps(replace(context,sysflg=const.SID)))
            print("\n")

    p=Panchanga(context)
    print(p)
    p.print_addendum()
    p.print_next_new_moon()
    p.print_next_full_moon()

def print_kala(context):
    """
    print time related information
    """
    print_cardinal_points(context.timeJD)

    print("Lunar new year:\n")
    print(lunar_new_year(context.timeJD).moon())

    p=Panchanga(context)
    print(p)
    p.print_addendum()
    p.print_next_new_moon()
    p.print_next_full_moon()

def print_dashas(args,context):
    if args.dasha_levels:
        dasha_levels = int(args.dasha_levels)
    else:
        if args.current_vdasha:
            dasha_levels = 3
        else:
            dasha_levels = defaults.dasha_levels

    if args.dasha_year_length:
        for opt in const.dasha_years:
            if opt[0][:3] in args.dasha_year_length.lower():
                yrlen = opt[1]
        if yrlen == 0:
            # the option was not recognized
            print(f"year length not recognized, using saura year")
            yrlen = const.dasha_years[0][1] # i.e., 365.2422 days per saura year
    else:
        yrlen = const.dasha_years[0][1] # i.e., 365.2422 days per saura year

    # get default, toggle if -V is present
    show_vdasha = defaults.show_vdasha
    if args.vdasha:
        show_vdasha = not show_vdasha

    if show_vdasha:
        print_vimshottari_dasha(Moon(context),dasha_levels,yrlen)

    # get default, toggle if -V2 is present
    show_v2dasha = defaults.show_v2dasha
    if args.v2dasha:
        show_v2dasha = not show_v2dasha

    if show_v2dasha:

        print("\n\nVimshottari Dasha\n")

        # this is for the year length
        for opt in const.dasha_years:
            if yrlen == opt[1]:
                yrstr = opt[0].capitalize()

        planet = Moon(context)
        print(f"Based on the position of {planet.name()}")
        print(f"Using {planet.ayanamsa_name()}")
        print(f"Using {yrstr} year length")
        vdasha = calculate_vimshottari_dasha(planet,dasha_levels,yrlen)
        print_calculated_vimshottari_dasha(vdasha)

    if args.dasha_levels:
        # if the user wants only a specific level, print that
        levels = [args.dasha_levels]
    else:
        # otherwise, print levels 1-5
        levels = [1,2,3,4,5]

    if args.current_vdasha:
        print_current_vdasha(context,yrlen,levels)

def print_current_vdasha(context,yrlen,levels: [int]):
    """
    print information on current vimshottari dasha
    levels is a list of levels, e.g., [1,2,3]
    it will print the information for all these levels
    """
    print("\n\nCurrent Vimshottari Dasha\n")

    # this is for the year length
    for opt in const.dasha_years:
        if yrlen == opt[1]:
            yrstr = opt[0].capitalize()

    planet = Moon(context)
    now = JulianDay("now")

    print(f"Based on the position of {planet.name()}")
    print(f"Using {planet.ayanamsa_name()}")
    print(f"Using {yrstr} year length\n")
    
    for level in levels:
        current_dasha = current_vimshottari_dasha(planet,now,level,yrlen)
        next_dasha_startsJD = current_dasha.pop()

        print(f"Current dasha: {utils.mk_dasha_lord(current_dasha)}")
        print(f"Next dasha: {utils.mk_dasha_lord(next_dasha_lords(current_dasha))}, starts at:")
        print(f"{next_dasha_startsJD}")
        print(f"in {utils.dec2ymd((next_dasha_startsJD.jd_number()-now.jd_number())/365.2422)}\n")


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
        "-e",
        "--ephemeris-mode",
        action="store_true",
        help="toggle printing of information in ephemeris mode",
    )
    parser.add_argument(
        "-c",
        "--chart-mode",
        action="store_true",
        help="toggle printing of information in chart mode",
    )
    parser.add_argument(
        "-k",
        "--kala",
        action="store_true",
        help="display a set of time related information",
    )
    parser.add_argument(
        "-Z",
        "--zodiac",
        action="store_true",
        help="toggle use of zodiac signs; can set default variable 'signs' in defaults.py",
    )
    parser.add_argument(
        "-A",
        "--aditya",
        action="store_true",
        help="use this is you want to use sidereal adityas, otherwise sidereal defautls to using zodiac signs",
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
        "-Q",
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
        "-C",
        "--current-vdasha",
        action="store_true",
        help="toggle printing of current vimshottari dashas; use -L to determine how many levels; default for printing current is 3",
    )
    parser.add_argument(
        "-V",
        "--vdasha",
        action="store_true",
        help="toggle printing vimshottari dasha from default; this option prints as it calculates, so it can print to however many levels you want easily",
    )
    parser.add_argument(
        "-V2",
        "--v2dasha",
        action="store_true",
        help="toggle printing vimshottari dasha from default; this option calculates everything, then prints",
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
        "-l",
        "--lang",
        help="language file; current options: dict.eng, dict.iast, dict.deva, dict.mixed",
    )
    parser.add_argument("-j", "--julian", help="time specificed as a julian day")
    parser.add_argument(
        "-E",
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
        "-N",
        "--nakshatras",
        action="store_true",
        help="toggle printing of nakshtras",
    )
    parser.add_argument(
        "-O",
        "--outer_planets",
        action="store_true",
        help="toggle printing of outer planets",
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
    parser.add_argument(
        "-Sc",
        "--sidereal-chart",
        action="store_true",
        help="in chart mode, print sidereal chart",
    )
    parser.add_argument(
        "-Hc",
        "--helio-chart",
        action="store_true",
        help="in chart mode, print heliocentric chart",
    )
    parser.add_argument(
        "-Bc",
        "--baryos-chart",
        action="store_true",
        help="in chart mode, print barycentric chart",
    )
    parser.add_argument(
        "-PA",
        "--planetary-aspects",
        action="store_true",
        help="toggle printing planetary aspects in chart mode",
    )
    parser.add_argument(
        "-PC",
        "--planetary-cusps-aspects",
        action="store_true",
        help="toggle printing planetary cusp aspects in chart mode",
    )
    parser.add_argument(
        "-v",
        "--vargas",
        help="vargas to print; any integer number will print the corresponding parivritti varga; multiple vargas can be printed at once, e.g., -v 4,5,9",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
