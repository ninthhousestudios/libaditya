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

    if args.lang:
        if args.theme:
            d = sc.draw_chakra(d,langfile=args.lang,themefile=sc.themepath+args.theme)
        else:
            d = sc.draw_chakra(d,langfile=args.lang)
    else:
        if args.theme:
            d = sc.draw_chakra(d,langfile=sc.langfile,themefile=sc.themepath+args.theme)
        else:
            d = sc.draw_chakra(d,langfile=sc.langfile)

    # read birth data and transit data from file 
    if args.input_file:
        input = open(args.input_file, "r")
    else:
        input = open(sc.default_input, "r")
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
        if field.startswith("Pla") or field.startswith("pla"):
            bplace = value
        if field.startswith("Ti") or field.startswith("ti"):
            ephclock = putil.intize_time(value)
        if field.startswith("La") or field.startswith("la"):
            blat = float(value)
        if field.startswith("Lo") or field.startswith("lo"):
            blong = float(value)
        # get transit data; time and lat and long
        if field.startswith("TDa") or field.startswith("tda"):
            if value == "now":
                nowtime = time.gmtime()
                tyear = nowtime[0]
                tmonth = nowtime[1] 
                tday = nowtime[2]
            else:
                tmonth, tday, tyear = putil.intize_date(value)
        if field.startswith("TPla") or field.startswith("tpla"):
            tplace = value
            print(f"got transit place name {tplace}")
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
    bephtime = JulianDay(swe.julday(byear, bmonth, bday, ephclock))
    transit_ephtime = JulianDay(swe.julday(tyear, tmonth, tday, transit_ephclock))
    input.close()


    # display panchangas
    # birth panchanga
    birth_panchanga = panchanga_string(Panchanga(bephtime))
    d.append(draw.Rectangle(395, 450, 70, 45, rx='1', ry='1', stroke='black', fill='yellow'))
    d.append(draw.Text(birth_panchanga,font_size=7.5,x=400,y=450))

    # transit panchanga
    transit_panchanga = panchanga_string(Panchanga(transit_ephtime))
    d.append(draw.Rectangle(35, 450, 70, 45, rx='1', ry='1', stroke='black', fill='yellow'))
    d.append(draw.Text(transit_panchanga,font_size=7.5,x=38,y=450))



    # display time and place, birth and transit
    bntstr = name_time_string(name,blat,blong,bplace,bephtime)
    tntstr = name_time_string("",tlat,tlong,tplace,jd=transit_ephtime)

    d.append(draw.Rectangle(400, 0, 100, 45, rx='1', ry='1', stroke='black', fill='yellow'))
    d.append(draw.Text(bntstr,font_size=7.5,x=405,y=10))

    d.append(draw.Rectangle(0, 0, 100, 50, rx='1', ry='1', stroke='black', fill='yellow'))
    d.append(draw.Text(tntstr,font_size=7.5,x=5,y=10))


    # display to the correct output file 
    d.set_pixel_scale(2)
    if args.output_file:
        d.save_svg(args.output_file)
    elif args.zodiac:
        d.save_svg(f"zodiac-sbc-{name}")
    else:
        d.save_svg(f"sbc-{name}")
    d



# def: panchanga string
def panchanga_string(panch=Panchanga()):
    s=""
    s+=f"\nTithi: {panch.tithi()}"
    s+=f"\nKarana: {panch.karana()}"
    s+=f"\nVara: {panch.vara()}"
    s+=f"\nNakshatra: {panch.nakshatra()}"
    s+=f"\nYoga: {panch.yoga()}"
    return s

# def: name_time_string
def name_time_string(name,lat,long,placename="",jd=JulianDay()):
    """
    name is the persons name for a birth chart, or the place name for transit
    placename is for a birth chart, if someone includes it.
    """
    s=""
    s+=f"{name}\n"
    s+=f"Date: {jd.date()}\n"
    s+=f"Time: {jd.time()}\n"
    s+=f"(Lat,Long): {(round(lat,2),round(long,2))}\n"
    if placename != "" :
        s+=f"Place: {placename}\n"
    return s




# get_args function 
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
    parser.add_argument("-l", "--lang", help="language file; default is ./dict.eng")
    parser.add_argument(
        "-o",
        "--output-file",
        help="name of output file; default is images/sbc.svg, images/sbc-zodiac.svg if -Z is selected",
    )
    parser.add_argument(
        "-t",
        "--theme",
        help="theme file to use. default directory is $pyphpath/images/sbc-themes",
    )
 

    args = parser.parse_args()
    return args

main()
