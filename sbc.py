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
import time
import os
import drawsvg as draw
import pyphglobals as pglob
import pyphutils as putil
import sbc_constants as sc
import sbc_config as sconf
from pyphclasses import *
from pyphobjs import *


# make actual coordinates for the chakra image
# here because i need them in a function definition below
coords = sc.make_coords()

def main():
    # set path to ephemeris file
    # set in sbc_constants
    swe.set_ephe_path(sc.ephepath)

    args = get_args()
    d = draw.Drawing(500, 500)

    # config is all of the values that are used to produce a chart
    # including birth data and transit info
    # first, we try to read that from a .sbc file. we just read as many of the
    # fields as are there, and then fill in all of the other ones from
    # sbc-config/charts/chart-base.sbc. put any .sbc files in $(path to your
    # pyphemeris dir)sbc-config/charts/, and then call "sbc" with -i
    # your-chart.sbc

    if args.input_file: # user passed a file
        # checks if it is in the sbc-config/charts/ directory
        if ".sbc" in args.input_file: # working with an sbc file
            if os.path.exists(sc.chartspath+args.input_file):
                config = sconf.init_chart_config(file=sc.chartspath+args.input_file)
            else: # assume it is in the current directory
                config = sconf.init_chart_config(file=args.input_file)
        elif ".chtk" in args.input_file: # working with a chtk file
            config = sconf.init_chtk_config(args.input_file)
        else:
            print("unrecognized input file type; input a .chtk or .sbc file")
            exit()
    else:
        config = sconf.init_chart_config(file=sc.default_chart)
    
    # soon to implement
    # call sbc with -D "field:value,field:value,..."
    # call sbc with -T which is a transfit file
    # or a string "field:value,etc.", filled in with defaults
    
    name = config["name"]
    bmonth, bday, byear = putil.intize_date(config["date"])
    bplace = config["place"]
    ephclock = putil.intize_time(config["time"])
    blat = float(config["lat"])
    blong = float(config["long"])
    tplace = config["tplace"]
    if config["tdate"] == "now": # transit date to current day
        nowtime = time.gmtime()
        tyear = nowtime[0]
        tmonth = nowtime[1] 
        tday = nowtime[2]
    elif config["tdate"] == "birth": # transit date to current day
        tyear=byear
        tmonth=bmonth
        tday=bday
    else:
        print(f"config[tdate]={config["tdate"]}")
        tmonth, tday, tyear = putil.intize_date(config["tdate"])
    if config["ttime"] == "now":
        nowtime = time.gmtime()
        transit_ephclock = nowtime[3] + nowtime[4] / 60 + nowtime[5] / 3600
    elif config["ttime"] == "birth":
        transit_ephclock = ephclock
    else:
        transit_ephclock = putil.intize_time(config["ttime"])
    tlat = float(config["tlat"])
    tlong = float(config["tlong"])

    bephtime = JulianDay(swe.julday(byear, bmonth, bday, ephclock))
    transit_ephtime = JulianDay(swe.julday(tyear, tmonth, tday, transit_ephclock))

    langfile=f"{sc.sbcpath}dict.{config["dict"]}"
    themefile=f"{sc.themepath}{config["theme"]}.sbc"
    zodiac = False if config["zodiac"] == "false" else True
    english_letters = False if config["english letters"] == "false" else True
    output_file = config["output"]

    # i want cmdline args to override these values if they are given
    if args.lang:
        langfile=f"{sc.sbcpath}{args.lang}"
    if args.theme:
        themefile=f"{sc.themepath}{args.theme}.sbc"
    if args.zodiac:
        zodiac = True
    if args.english_letters:
        english_letters = True
    if args.output_file:
        output_file = args.output_file
    output_file = output_file.replace(' ','-').lower() 


    d = sc.draw_chakra(d,zodiac=zodiac,langfile=langfile,themefile=themefile)

    if english_letters:
       d = draw_english_letters(d)

    # display panchangas
    # birth panchanga
    bpanch = Panchanga(bephtime)
    birth_panchanga = panchanga_string(bpanch)
    d.append(draw.Rectangle(395, 450, 70, 45, rx='1', ry='1', stroke='black', fill='yellow'))
    d.append(draw.Text(birth_panchanga,font_size=7.5,x=400,y=450))
    colors = sc.get_colors(themefile)
    purna_text_color = colors[3]
    #print(f"purna_text_color = {purna_text_color}")

    # draw tithi number in the appropriate box for the tithi type, in the center
    # [(self.tithi() - 1) % 5]
    # we need the tithi coordinates
    # nanda, bhddra, jaya, rikta, purna
    tcoords = [(4,3),(5,4),(4,5),(3,4),(4,4)]
    btithi = bpanch.tithi()
    ttype = ((btithi-1)%5)
    # kind of pointless since i ended up testing them individually
    thisx = tcoords[ttype][0]
    thisy = tcoords[ttype][1]
    if ttype == 0:
        d.append(draw.Text(str((btithi-15)%15),font_size=10,x=coords[4][3][0]+10,y=coords[4][3][1]+14))
    if ttype == 1:
        d.append(draw.Text(str((btithi-15)%15),font_size=10,x=coords[thisx][thisy][0]+10,y=coords[thisx][thisy][1]+14))
    if ttype == 2:
        d.append(draw.Text(str((btithi-15)%15),font_size=10,x=coords[thisx][thisy][0]+10,y=coords[thisx][thisy][1]+17))
    if ttype == 3:
        d.append(draw.Text(str((btithi-15)%15),font_size=10,x=coords[3][4][0]+10,y=coords[3][4][1]+17))
    if ttype == 4:
        d.append(draw.Text('15' if (btithi-15)%15==0 else str((btithi-15)%15),font_size=10,x=coords[4][4][0]+10,y=coords[4][4][1]+17,fill=purna_text_color))

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


    # get planet information
    bplanets = init_Planets(bephtime)
    # tplanets = init_Planets(transit_ephtime)
    # above is actually called below

    # cut cusps; originally i included the transit planets here
    # but then moved all the transit stuff to the same section later
    bcusps = Cusps(sc.hsys,Location(lat=blat,long=blong,placename=bplace),bephtime)
    bcusps.init_cusps()

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
    # also want to print lagna in its nakshatra; do that last
    bnaks.append(int(divmod(bcusps.get_lagna(),360/28)[0]))
    #for i in range(len(bnaks)):
     #   print(f"{i}th nakshatra is {bnaks[i]}")

    poffsets = {1: [15,[(10,15)]], 2: [12,[(2,15),(15,15)]], 3:
                [10,[(5,15),(20,25),(15,15)]], 4:
                [10,[(5,10),(20,25),(20,10),(11,19)]], 5:
                [10,[(5,10),(20,25),(20,10),(5,19),(15,19)]], 6:
                [7,[(5,8),(20,25),(20,8),(5,19),(12,19),(12.5,8)]], 7:
                [7,[(5,8),(20,25),(20,8),(5,19),(12,19),(12.5,8),(20,19)]], 8:
                [7,[(5,8),(20,25),(20,8),(5,19),(12,19),(12.5,8),(20,19),(24,15)]]}
    nakcount = [0 for i in range(28)] # count how many planets in each nakshatra

    # if there are multiple planets in a nakshatra, print them in different
    # places
    for n in range(len(bnaks)):
        num = bnaks.count(bnaks[n]) # how many planets are in nakshatra bnaks[n]
        ny,nx = sc.nak_coords[bnaks[n]]
        d.append(draw.Text(sc.pglyphs[n],font_size=poffsets[num][0],x=coords[ny][nx][0]+(poffsets[num][1][nakcount[bnaks[n]]][0]),y=coords[ny][nx][1]+(poffsets[num][1][nakcount[bnaks[n]]][1])))
        nakcount[bnaks[n]]+=1

    # display transit planets
    tplanets = init_Planets(transit_ephtime)
    tcusps = Cusps(sc.hsys,Location(lat=tlat,long=tlong,placename=tplace),transit_ephtime)
    tcusps.init_cusps()

    # planets to print, sun-sa, rahuketu, not u,n,p
    to_print=[0,1,2,3,4,5,6,10,11]
    # get nakshatra coordinates
    # takes a list of coordinates, returns a list of indices
    tnaks = get_nakshatras(long_list(tplanets,to_print))
    # also want to print lagna in its nakshatra; do that last
    tnaks.append(int(divmod(tcusps.get_lagna(),360/28)[0]))
    
    #for i in range(len(tnaks)):
        #print(f"{i}th nakshatra is {tnaks[i]}")
    # transits are on the outside, not in a box
    # so i can print all planets at 15pt
    # these are the offsets for a nakshatra box on the krittika row
    # there are ten coordinates, for 9 planets and the lagna...just in case
    tup=[(2,-2),(20,-2),(2,-15),(20,-15),(2,-30),(20,-30),(2,-45),(20,-45)]
    toffup = {n: tup[:n] for n in range(1,len(tup)+1)} # a quick way of writing it
    tright=[(35,13),(35,27),(50,13),(49,26),(65,13),(65,27),(80,13),(80,27)]
    toffright = {n: tright[:n] for n in range(1,len(tright)+1)} # a quick way of writing it
    tbot=[(2,42),(20,42),(2,57),(20,57),(2,72),(20,72),(2,87),(20,87)]
    toffbot = {n: tbot[:n] for n in range(1,len(tbot)+1)} # a quick way of writing it
    tleft=[(-18,13),(-18,27),(-30,13),(-30,26),(-45,13),(-45,27),(-60,13),(-60,27)]
    toffleft = {n: tleft[:n] for n in range(1,len(tleft)+1)} # a quick way of writing it
    # specific nakshatra box (x,y), increasing to the right and down
    nakcount = [0 for i in range(28)] # count how many planets in each nakshatra

    # if there are multiple planets in a nakshatra, print them in different
    # places
    for n in range(len(tnaks)):
        num = tnaks.count(tnaks[n]) # how many planets are in nakshatra tnaks[n]
        #ncol,nrow = sc.nak_coords[tnaks[n]]
        ncol,nrow = sc.nak_coords[tnaks[n]]
        #print(f"debug: num is {num}, tnaks[n]={tnaks[n]},nakcount[tnaks[n]]={nakcount[tnaks[n]]}")
        if nrow == 0: # the row of seven nakshatras, krtikkikadi
            d.append(draw.Text(sc.pglyphs[n],font_size=15,x=coords[ncol][nrow][0]+(toffup[num][nakcount[tnaks[n]]][0]),y=coords[ncol][nrow][1]+(toffup[num][nakcount[tnaks[n]]][1])))
        if nrow == 8: # the bottom of of seven nakshatras
            d.append(draw.Text(sc.pglyphs[n],font_size=15,x=coords[ncol][nrow][0]+(toffbot[num][nakcount[tnaks[n]]][0]),y=coords[ncol][nrow][1]+(toffbot[num][nakcount[tnaks[n]]][1])))
        if ncol == 0: # the first column of nakshatras, i.e., ending with bharani
            d.append(draw.Text(sc.pglyphs[n],font_size=15,x=coords[ncol][nrow][0]+(toffleft[num][nakcount[tnaks[n]]][0]),y=coords[ncol][nrow][1]+(toffleft[num][nakcount[tnaks[n]]][1])))
        if ncol == 8: # the rightmost column of nakshatras
            d.append(draw.Text(sc.pglyphs[n],font_size=15,x=coords[ncol][nrow][0]+(toffright[num][nakcount[tnaks[n]]][0]),y=coords[ncol][nrow][1]+(toffright[num][nakcount[tnaks[n]]][1])))
        nakcount[tnaks[n]]+=1


    # display to the correct output file 
    d.set_pixel_scale(2)
    d.save_svg(output_file)
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
    return coords

def draw_english_letters(d):
    """draw english letter equivalents on the sanskrit letter boxes"""

    d.append(draw.Text("a",font_size=5,x=coords[0][0][0]+2,y=coords[0][0][1]+28))
    d.append(draw.Text("A",font_size=5,x=coords[8][0][0]+2,y=coords[8][0][1]+28))
    d.append(draw.Text("i",font_size=5,x=coords[8][8][0]+2,y=coords[8][8][1]+28))
    d.append(draw.Text("I",font_size=5,x=coords[0][8][0]+2,y=coords[0][8][1]+28))
    eng_letters=["u","a","va","ka","ha","Da","U","m","Ta","pa","ra","ta","R","na","ya","bha","ja","kha","RR","ga","sa","da","ca","la"]
    elet=0
    for y in range(1,8):
        d.append(draw.Text(eng_letters[elet],font_size=5,x=coords[y][1][0]+2,y=coords[y][1][1]+28))
        elet+=1
    for y in range(2,8):
        d.append(draw.Text(eng_letters[elet],font_size=5,x=coords[7][y][0]+2,y=coords[7][y][1]+28))
        elet+=1
    for y in range(1,7).__reversed__():
        d.append(draw.Text(eng_letters[elet],font_size=5,x=coords[y][7][0]+2,y=coords[y][7][1]+28))
        elet+=1
    for y in range(2,7).__reversed__():
        d.append(draw.Text(eng_letters[elet],font_size=5,x=coords[1][y][0]+2,y=coords[1][y][1]+28))
        elet+=1
    d.append(draw.Text("lR",font_size=5,x=coords[2][2][0]+2,y=coords[2][2][1]+28))
    d.append(draw.Text("lRR",font_size=5,x=coords[6][2][0]+2,y=coords[6][2][1]+28))
    d.append(draw.Text("e",font_size=5,x=coords[6][6][0]+2,y=coords[6][6][1]+28))
    d.append(draw.Text("ai",font_size=5,x=coords[2][6][0]+2,y=coords[2][6][1]+28))

    d.append(draw.Text("o",font_size=5,x=coords[3][3][0]+2,y=coords[3][3][1]+28))
    d.append(draw.Text("au",font_size=5,x=coords[5][3][0]+2,y=coords[5][3][1]+28))
    d.append(draw.Text("aM",font_size=5,x=coords[5][5][0]+2,y=coords[5][5][1]+28))
    d.append(draw.Text("aH",font_size=5,x=coords[3][5][0]+2,y=coords[3][5][1]+28))
    return d

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
        help="input file with birth data and transit time and place data. will first look for this file in sbc-config/charts, then in the current directory",
    )
    parser.add_argument(
        "-Z",
        "--zodiac",
        action="store_true",
        help="use zodiac signs on the sbc. default is adityas",
    )
    parser.add_argument("-l", "--lang", help="language file; options: dict.eng, dict.iast, dict.deva, dict.mixed")
    parser.add_argument(
        "-o",
        "--output-file",
        help="name of output file",
    )
    parser.add_argument(
        "-t",
        "--theme",
        help="theme file to use. default directory is $pyphpath/sbc-config/sbc-themes",
    )
    parser.add_argument(
        "-e",
        "--english-letters",
        action="store_true",
        help="display kyoto-harvard letters in addition to sanskrit letters",
    )
    args = parser.parse_args()
    return args

main()
