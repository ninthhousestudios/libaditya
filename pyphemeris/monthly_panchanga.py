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
from prettytable import PrettyTable
from dataclasses import replace

import libaditya.read as read
from libaditya import constants as const

from libaditya.objects import JulianDay, EphContext, Location, Yamakoti
from libaditya.calc import Panchanga

def main():
    args = get_args()

    if args.location:
        lat, long, placename, utcoffset, timezone = parse_position(args.location)
        this_location = Location(lat,long,0,placename,timezone)
    else:
        utcoffset = 12
        timezone = "YKT"
        this_location = Yamakoti


    ayanamsa = 98
    if args.ayanamsa:
        ayanamsa = int(args.ayanamsa)


    for month in args.months:
        month, year = parse_date(month)

        # midnight on the first day of the month
        this_timeJD = JulianDay((year,month,1,0),utcoffset,timezone)
        context = EphContext(timeJD=this_timeJD,location=this_location,ayanamsa=ayanamsa)
        panch = Panchanga(context)

        panch_str = make_table(args,panch)

        print(f"Panchanga for {month}/{year}")
        print(f"{this_location}")
        print(f"Using {const.ayanamsa_name(ayanamsa)} ayanamsa")
        if args.midnight:
            print("Times at midnight")
        else:
            print("Times at sunrise")

        print(panch_str)


def make_table(args,panch):
    output = PrettyTable()
    output.field_names = ["Day", "Sunrise", "Sunset", "Moonrise", "Moonset", "Vara", "Next Vara", "Nakshatra", "Next Nakshatra", "Tithi", "Next Tithi", "Karana", "Next Karana", "Yoga", "Next Yoga"]

    # so we can keep track of when the month ends
    _, this_month, day, _ = swe.revjul(panch.timeJD.jd_number())

    utc = False
    if args.utc:
        utc = True

    format = "text"
    if args.format:
        format = args.format

    month = this_month
    while month == this_month:
        today_midnight = panch
        # this is so that we change change the Panchanga to be at sunrise if desired
        sunrise = panch.sunrise()
        sunset = panch.sunset()
        moonrise = panch.moonrise()
        moonset = panch.moonset()
        today_sunrise = Panchanga(replace(panch.context,timeJD=sunrise))
        if args.midnight:
            panch = today_midnight
        else:
            panch = today_sunrise
        # build row for this day
        row = []
        row.append(day)
        if utc:
            row.append(f"{sunrise.time()}")
            row.append(f"{sunset.time()}")
            row.append(f"{moonrise.time()}")
            row.append(f"{moonset.time()}")
            row.append(f"{panch.vara()}")
            row.append(f"{panch.next_vara().timeJD.time()}")
            row.append(f"{panch.nakshatra()}")
            row.append(f"{panch.next_nakshatra().timeJD.time()}")
            row.append(f"{panch.tithi()} ({panch.tithi_type()})")
            row.append(f"{panch.next_tithi().timeJD.time()}")
            row.append(f"{panch.karana()}")
            row.append(f"{panch.next_karana().timeJD.time()}")
            row.append(f"{panch.yoga_name()}")
            row.append(f"{panch.next_yoga().timeJD.time()}")
        else:
            row.append(f"{panch.sunrise().usrtime()}")
            row.append(f"{panch.sunset().usrtime()}")
            row.append(f"{panch.moonrise().usrtime()}")
            row.append(f"{panch.moonset().usrtime()}")
            row.append(f"{panch.vara()}")
            row.append(f"{panch.next_vara().timeJD.usrtime()}")
            row.append(f"{panch.nakshatra()}")
            row.append(f"{panch.next_nakshatra().timeJD.usrtime()}")
            row.append(f"{panch.tithi()} ({panch.tithi_type()})")
            row.append(f"{panch.next_tithi().timeJD.usrtime()}")
            row.append(f"{panch.karana()}")
            row.append(f"{panch.next_karana().timeJD.usrtime()}")
            row.append(f"{panch.yoga_name()}")
            row.append(f"{panch.next_yoga().timeJD.usrtime()}")

        output.add_row(row)
        output.add_divider()
        # go forward one day
        panch = Panchanga(replace(today_midnight.context,timeJD=today_midnight.timeJD.shift('f','day',1)))
        _, month, day, _ = swe.revjul(panch.timeJD.jd_number())

    return output.get_formatted_string(out_format=format,fields=["Day", "Sunrise", "Sunset", "Moonrise", "Moonset", "Vara", "Next Vara", "Nakshatra", "Next Nakshatra", "Tithi", "Next Tithi", "Karana", "Next Karana", "Yoga", "Next Yoga"])



def parse_date(date):
    return [int(x) for x in date.split('/')]

def parse_position(position, placname="", timezone=""):
    if ".chtk" in position:
        placename, lat, long, utcoffset = read.read_chtk_location(position)
        timezone = "UTC"
    else:
        print(f"cant interpret that position information at this time; pass a .chtk file")
        exit()
    return lat, long, placename, utcoffset, timezone

def get_args():
    parser = argparse.ArgumentParser(
        prog="monthly_panchanga",
        usage="%(prog)s [options]",
        description="get panchanga for month MM/YYYY",
    )
    parser.add_argument(
        "-l",
        "--location",
        help="enter location by providing a .chtk file; default location is Yamakoti",
    )
    parser.add_argument(
        "-a",
        "--ayanamsa",
        help="swiss epehemeris code for the ayanamsa you want; lahiri = 1; true citra = 27; dhruva gc equatorial = 98, ecliptic vedanga jyotisha = 99, equatorial vedanga jyotisha = 100",
    )
    parser.add_argument(
        "-u",
        "--utc",
        action="store_true",
        help="display times as utc; default is local timezone specified in .chtk file",
    )
    parser.add_argument(
        "-m",
        "--midnight",
        action="store_true",
        help="display elements as they are as midnight; default is to display at the time of sunrise",
    )
    parser.add_argument(
        "-f",
        "--format",
        help="output format; defaul is text; options: text, html, json, csv, latex, mediawiki"
    )
    parser.add_argument("months", nargs='*', help="enter months for which to calculate panchanga; multiple can be entered; MM/YYYY") 
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
