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

from libaditya import constants as const
from libaditya import read

import defaults

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


def coords_to_show(args):
    to_show=[const.TROP]
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
    return to_show
