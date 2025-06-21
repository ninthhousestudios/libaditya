#!/usr/bin/python

import swisseph as swe
import argparse
import time
import drawsvg as draw
import pyphglobals as pglob
import pyphutils as putil
import sbc_constants as sc
from pyphclasses import *
from pyphobjs import *




def main():
    args = get_args()
    d = draw.Drawing(500, 500)
    d = sc.draw_chakra(d)

    # read birth data and transit data from file {{{1
    if args.input_file:
        fromfile = True
        input = open(args.input_file, "r")
        for line in input:
            if not "=" in line:
                continue
            field, value = line.split("=")
            field = field.strip()
            value = value.strip()
            # get birth data
            if field.startswith("Na") or field.startswith("na"):
                name = value
            if field.startswith("Da") or field.startswith("da"):
                bmonth, bday, byear = putil.intize_date(value)
            if field.startswith("Ti") or field.startswith("ti"):
                ephclock = putil.intize_time(value)
            if field.startswith("La") or field.startswith("la"):
                lat = float(value)
            if field.startswith("Lo") or field.startswith("lo"):
                long = float(value)
            # get transit data; time and lat and long
            if field.startswith("TDa") or field.startswith("tda"):
                if value == "now":
                    nowtime = time.gmtime()
                    tyear = nowtime[0]
                    tmonth = nowtime[1] 
                    tday = nowtime[2]
                else:
                    tmonth, tday, tyear = putil.intize_date(value)
            if field.startswith("TTi") or field.startswith("tti"):
                if value == "now":
                    nowtime = time.gmtime()
                    transit_ephclock = nowtime[3] + nowtime[4] / 60 + nowtime[5] / 3600
                else:
                    transit_ephclock = putil.intize_time(value)
            if field.startswith("TLa") or field.startswith("tla"):
                tlat = float(value)
            if field.startswith("TLo") or field.startswith("tlo"):
                tlong = float(value)
        ephtime = JulianDay(swe.julday(byear, bmonth, bday, ephclock))
        transit_ephtime = JulianDay(swe.julday(tyear, tmonth, tday, transit_ephclock))
        input.close()

        print(f"Got birth time: {ephtime}")
        print(f"Got transit time: {transit_ephtime}")
                                                    #}}}

    d.set_pixel_scale(2)
    if args.output_file:
        d.save_svg(args.output_file)
    elif args.zodiac:
        d.save_svg(f"zodiac-sbc-{name}")
    else:
        d.save_svg(f"sbc-{name}")
    d



# get_args function {{{1
def get_args():
    parser = argparse.ArgumentParser(
        prog="sbc",
        usage="%(prog)s [options]", 
        description=f"draw a sarvatobhadra chakra",
    )
    parser.add_argument(
        "-i",
        "--input-file",
        help="input file with birth data and transit time and place data",
    )
    parser.add_argument(
        "-Z",
        "--zodiac",
        action="store_true",
        help="use zodiac signs on the sbc. default is adityas",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        help="name of output file; default is images/sbc.svg, images/sbc-zodiac.svg if -Z is selected",
    )


    args = parser.parse_args()
    return args
                       #}}}
main()
