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


    # make actual coordinates for the chakra image
    coords = sc.make_coords()
    # get planet information
    bplanets = init_Planets(bephtime)
    tplanets = init_Planets(transit_ephtime)

    bcusps = Cusps(sc.hsys,Location(lat=blat,long=blong,placename=bplace),bephtime)
    bcusps.init_cusps()
    tcusps = Cusps(sc.hsys,Location(lat=tlat,long=tlong,placename=tplace),transit_ephtime)
    tcusps.init_cusps()

    # display birth lagna and moon in the signs
    moon_rashi=get_rashi(bplanets[swe.MOON].longitude())
    my,mx=sc.rashis_coords[moon_rashi]
    d.append(draw.Text(sc.moon,font_size=15,x=coords[my][mx][0]+10,y=coords[my][mx][1]+15))
    lagna_rashi=get_rashi(bcusps.get_lagna())
    ly,lx=sc.rashis_coords[lagna_rashi]
    d.append(draw.Text(sc.lagna,font_size=10,x=coords[ly][lx][0]+10,y=coords[ly][lx][1]+15))

    # planets to print, sun-sa, rahuketu, not u,n,p
    to_print=[0,1,2,3,4,5,6,10,11]
    # get nakshatra coordinates
    # takes a list of coordinates, returns a list of indices
    bnaks = get_nakshatras(long_list(bplanets,to_print))

    for n in range(9):
        ny,nx = sc.nak_coords[bnaks[n]]
        print(f"ny,nx = {ny},{nx}")
        d.append(draw.Text(sc.plist[n],font_size=15,x=coords[ny][nx][0]+10,y=coords[ny][nx][1]+15))
    

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

def init_Planets(tjd=JulianDay()):
    """
    return a list of Planet classes, one for each
    Sun,Moon,Mercury,Venus,Mars,Jupiter,Saturn,Uranus,Neptune,Pluto (indexes 0-9)
    Rahu at index 11, Ketu at index 10
    Earth at index 12
    """
    planets = []
    for i in range(10):
        planets.append(Planet(i, tjd))  # Planet takes a JulianDay class, tjd
    planets.append(Rahu(tjd))
    planets.append(Ketu(tjd))
    # must use swe.EARTH=14, if changed will given wrong results
    # plgob.earth is 12 since it indexes
    planets.append(Planet(swe.EARTH, tjd))
    return planets

def get_rashi(long):
    """get the appropriate rashi index 0-11 with a long between 0-360"""
    return int(divmod(long,30)[0]) 

def get_nakshatras(longs):
    """
    get nakshatra index for longs
    this function gets nakshatras for 28 equal nakshatra with krittka starting
    at the ascending equinox
    """
    naks=[]
    nak=360/28
    for i in longs:
        naks.append(int(divmod(i,nak)[0]))
    return naks

def long_list(planets,to_print):
    """planets is a list of classes; this function returns a list of longitudes"""
    coords=[]
    for n in to_print:
        coords.append(planets[n].longitude())
    print(f"long_list {coords}")
    return coords

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
