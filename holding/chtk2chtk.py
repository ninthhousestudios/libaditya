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

import argparse
import os
import codecs
from pyphread import *


def main():
    args = get_args()

    for file in args.file:
        if len(file.split(".")) == 1:
            # not a chtk file
            continue
        if file.split(".")[1].strip().lower() != "chtk":
            # not a chtk file
            continue
        linenum = 0
        foutname = file.split(".")[0].strip().replace(" ", "-").replace(",", "").lower()
        input = open(file, "rb")
        print(f"converting {file}")
        lines = input.readlines()
        for line in lines:
            # print(f"{n}: {line.decode(errors='ignore')}")
            match linenum:
                case 0:
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
                    if len(line) == 1:
                        h = int(line[0])
                        m = s = 0
                    elif len(line) == 2:
                        h = int(line[0])
                        m = int(line[1])
                        s = 0
                    else:
                        h = int(line[0])
                        m = int(line[1])
                        s = int(line[2])
                    utcoff = int(h) + (int(m) / 60) + (int(s) / 3600)
                case 13:  # dst value
                    dst = intize_line(codecs.decode(line))
            linenum += 1
        input.close()
        #    print(name)
        #    print(f"{month:02d}/{day:02d}/{year}")
        #    print(f"{hour:02d}:{min:02d}:{sec:02d}")
        #    print(f"{"male" if sex==1 else "female"}")
        #    print(country)
        #    print(city)
        #    print(f"(lat,long): ({lat},{long})")
        #    print(utcoff)

        # time for config needs to be utc
        # so we take the time here and add utcoffset
        time = dms2dec((int(hour), int(min), int(sec)))  # turn into float
        time += utcoff - dst  # utcoff is already a float
        time = dec2dms(time)  # return the float as a string HH:MM:SS
        #    print(time)

        out = []
        out.append(str(name) + "\n")
        out.append(str(year) + "\n")
        out.append(str(month) + "\n")
        out.append(str(day) + "\n")
        out.append(str(hour) + "\n")
        out.append(str(min) + "\n")
        out.append(str(sec) + "\n")
        out.append(str(sex) + "\n")
        out.append(str(country) + "\n")
        out.append(str(city) + "\n")
        out.append(float_to_long(long) + "\n")
        out.append(float_to_lat(lat) + "\n")
        out.append(f"{h:02d}:{m:02d}:{s:02d}\n")
        out.append(str(dst) + "\n")
        fout = open(foutname + "-test" + ".chtk", "w")
        fout.writelines(out)
        fout.close()


def get_args():
    parser = argparse.ArgumentParser(
        prog="chtk2sbc",
        usage="%(prog)s [options]",
        description=f"convert .chtk file .sbc format",
    )
    parser.add_argument("file", nargs="*", help=".chtk file(s) to convert")
    args = parser.parse_args()
    return args


main()
