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

    timezone=""
    if args.location:
        lat, long, placename, utcoffset, timezone = parse_position(args.location)
        original_timezone = utils.mktimezone(utcoffset)
        if isinstance(args.timezone_string,str):
            timezone = args.timezone_string
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

        # midnight on the first day of the month
        this_timeJD = JulianDay((year,month,1,0),utcoffset,timezone)
        context = EphContext(timeJD=this_timeJD,location=this_location,ayanamsa=ayanamsa,names=names)
        panch = Panchanga(context)

        panch_str = make_table(args,panch)

        print(f"Panchanga for {month}/{year}")
        print(f"{this_location}")
        print(f"Using {const.ayanamsa_name(ayanamsa)} ayanamsa")
        if args.utc:
            print("All times UTC")
        else:
            print(f"All times {original_timezone}")
        if args.midnight:
            print("Times at midnight")
        else:
            print("All panchanga times at sunrise")

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

    # so we can keep track of when the month ends
    _, this_month, day, _ = swe.revjul(panch.timeJD.jd_number())

    utc = False
    if args.utc:
        utc = True

    if utc:
        tz = "utc"
    else:
        tz = "usr"

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

        today_sunrise = Panchanga(replace(panch.context,timeJD=sunrise))
        if args.midnight:
            panch = today_midnight
        else:
            panch = today_sunrise
        # build row for this day
        row = []
        row.append(day)
        row.append(f"{sunrise.time(tz)}")
        row.append(f"{sunset.time(tz)}")
        # take care of moonrise and moonset
        if tz == "utc":
            if moonrise.day(tz) != day:
                row.append("N/A")
            else:
                row.append(f"{moonrise.time(tz)}")
            if moonset.day(tz) != day:
                row.append("N/A")
            else:
                row.append(f"{moonset.time(tz)}")
        else:
            if moonrise.usrday() != today_midnight.timeJD.day():
                # we have to go forward a day to make the calendar days line up between local and utc
                moonrise = Panchanga(replace(today_midnight.context,timeJD=today_midnight.timeJD.shift('f','day',1))).moonrise()
                row.append(f"{moonrise.usrtime()}")
            else:
                row.append(f"{moonrise.usrtime()}")
            if moonset.usrday() != today_midnight.timeJD.day():
                moonset = Panchanga(replace(today_midnight.context,timeJD=today_midnight.timeJD.shift('f','day',1))).moonset()
                if moonset.day() == moonset.usrday():
                    row.append("N/A")
                else:
                    row.append(f"{moonset.usrtime()}")
            else:
                row.append(f"{moonset.usrtime()}")
        # now do the rest
        ptimes = []
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
        # now check all to make sure that are the right calendar day, otherwise print N/A
        # .time
        for n,t in enumerate(ptimes):
            if not isinstance(t,JulianDay):
                # not a time, so skip
                row.append(t)
                continue
            if t.day(tz) != day:
                row.append("N/A")
                continue
            if args.midnight:
                if t.time(tz) < panch.timeJD.time():
                    row.append("N/A")
                    continue
            else:
                if t.time(tz) < panch.timeJD.time(tz):
                    row.append("N/A")
                    continue
            row.append(t.time(tz))

        output.add_row(row)
        output.add_divider()
        # go forward one day
        panch = Panchanga(replace(today_midnight.context,timeJD=today_midnight.timeJD.shift('f','day',1)))
        month = panch.timeJD.month(tz)

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
        "--timezone-string",
        help="set a timezone-string to make local time output more readable; e.g., using -z EST will make the table more readable, rather than having it print \"UTC-5.0\""
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
