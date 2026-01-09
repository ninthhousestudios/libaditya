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
import tracemalloc
tracemalloc.start()

import libaditya.read as read
from libaditya import constants as const
from libaditya import utils

from libaditya.objects import JulianDay, EphContext, Location, Yamakoti, Names
from libaditya.calc import Panchanga

def main():
    args = get_args()

    if args.location:
        lat, long, placename, utcoffset, timezone = parse_position(args.location)
        original_timezone = utils.mktimezone(utcoffset)
        this_location = Location(lat,long,0,placename,original_timezone)
    else:
        utcoffset = 12
        timezone = "YKT"
        this_location = Yamakoti


    ayanamsa = 98
    if args.ayanamsa:
        ayanamsa = int(args.ayanamsa)

    names = Names(*const.abbreviated_names)
    if args.long_names:
        names = Names(*const.names)


    # input multiple months as MM/YYYY,MM/YYYY,MM/YYY
    for month in args.months:
        month, year = parse_date(month.replace(",","")) #

        # midnight utc on the first day of the month
        day = 1
        if utcoffset < 0:
            # in this case, midnight minus utcoffset will be the day before
            # but we want to start on calendar day 1, regardless of timezone
            day = 2
        this_timeJD = JulianDay((year,month,day,0+utcoffset),utcoffset,timezone)
        context = EphContext(timeJD=this_timeJD,location=this_location,ayanamsa=ayanamsa,names=names)
        panch = Panchanga(context)

        panch_str = make_table(args,panch)

        print(f"Panchanga for {month}/{year}")
        print(f"{this_location}")
        print(f"Using {const.ayanamsa_name(ayanamsa)} ayanamsa")
        print("All times relative to midnight")
        if args.utc:
            print(f"All times UTC")
        else:
            print(f"All times: {panch.timeJD.timezone()}")

        print(panch_str)
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)


def make_table(args,panch):
    output = PrettyTable()
    if args.long_names:
        output.field_names = ["Day", "Sunrise", "Sunset", "Moonrise", "Moonset", "Vara", "Next Vara", "Nakshatra", "Next Nakshatra", "Tithi", "Next Tithi", "Karana", "Next Karana", "Yoga", "Next Yoga"]
    else:
        output.field_names = ["Day", "Sunrise", "Sunset", "Moonrise", "Moonset", "V", "N.V.", "N", "N.N.", "T", "N.T.", "K.", "N.K.", "Y", "N.Y."]


    utc = False
    if args.utc:
        utc = True

    if utc:
        tz = "utc"
    else:
        tz = "usr"

    # so we can keep track of when the month ends
    #_, this_month, day, _ = swe.revjul(panch.timeJD.jd_number())
    this_month = panch.timeJD.month()
    day = panch.timeJD.day(tz)

    ptz = False
    if args.print_timezone:
        ptz = True

    format = "text"
    if args.format:
        format = args.format

    month = this_month
    while month == this_month:
        # want every row to be a calendar day
        # all times should occur within that calendar day
        # if no such event happens during that calendar, replace with "N/A"
        today_midnight = panch
        day = today_midnight.timeJD.day()
        # this is so that we change change the Panchanga to be at sunrise if desired
        sunrise = panch.sunrise()
        sunset = panch.sunset()
        moonrise = panch.moonrise()
        moonset = panch.moonset()

        # build row for this day
        row = []
        row.append(day)
        row.append(f"{sunrise.time(tz,ptz)}")
        row.append(f"{sunset.time(tz,ptz)}")
        ptimes = []
        ptimes.append(moonrise)
        ptimes.append(moonset)
        ptimes.append(panch.vara())
        ptimes.append(panch.next_vara().timeJD)
        ptimes.append(panch.nakshatra())
        ptimes.append(panch.next_nakshatra().timeJD)
        ptimes.append(panch.tithi())
        ptimes.append(panch.next_tithi().timeJD)
        ptimes.append(panch.karana())
        ptimes.append(panch.next_karana().timeJD)
        ptimes.append(panch.yoga_name())
        ptimes.append(panch.next_yoga().timeJD)
        for t in ptimes:
            if not isinstance(t,JulianDay):
                # not a time, so skip
                row.append(t)
                continue
            row.append(t.time(tz,ptz))

        output.add_row(row)
        output.add_divider()
        # go forward one day
        panch = Panchanga(replace(today_midnight.context,timeJD=today_midnight.timeJD.shift('f','day',1)))
        month = panch.timeJD.month()

    if args.long_names:
        return output.get_formatted_string(out_format=format,fields=["Day", "Sunrise", "Sunset", "Moonrise", "Moonset", "Vara", "Next Vara", "Nakshatra", "Next Nakshatra", "Tithi", "Next Tithi", "Karana", "Next Karana", "Yoga", "Next Yoga"])
    else:
        return output.get_formatted_string(out_format=format, fields=["Day", "Sunrise", "Sunset", "Moonrise", "Moonset", "V", "N.V.", "N", "N.N.", "T", "N.T.", "K.", "N.K.", "Y", "N.Y."])


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
        description="get panchanga for month MM/YYYY; all rows are times that happen on the calendar \"Day\"; for all but sun/moonrise/set, all times times are related to midnight or sunrise; default is sunrise; use -m for midnight",
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
        "-m",
        "--midnight",
        action="store_true",
        help="display elements as they are as midnight; default is to display at the time of sunrise",
    )
    parser.add_argument(
        "-u",
        "--utc",
        action="store_true",
        help="display times as utc; default is local timezone specified in .chtk file",
    )
    parser.add_argument(
        "-z",
        "--print-timezone",
        action="store_true",
        help="print timezone in each box; default is to just print at the top"
    )
    parser.add_argument(
        "-L",
        "--long-names",
        action="store_true",
        help="default is to use 2-4 letter abbreviations of all names; use this flag to use the full name as given in libaditya/constants.py",
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
