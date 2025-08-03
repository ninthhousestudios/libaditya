#!/usr/bin/python
"""
this file contains and early version of drawing the chakra
below that it contains comments and test code from all the other files
i wanted to clean up those files but keep the comments and examples, so they are
all stored here
"""
import drawsvg as draw
import argparse
import sbcnames

def main():

    args = get_args()

    d = draw.Drawing(500, 500)

    d.append(draw.Circle(250,250,250,fill='khaki'))

    # makes coordinate system that that
    # coords[c][r] gives the coordinates for the square in the
    # cth column and rth row
    coords=sbcnames.make_coords()

    # draw the 81 squares of the chakra
    for i in range(9):
        for n in range(9):
            d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30, 30, rx='1', ry='1', stroke='black', fill='yellow'))

    # initalize all the names to write
    nakshatra,adityas,tithi,vara,signs = sbcnames.init_sbc_names()
    if args.zodiac:
        adityas=signs

    # draw names of nakshatras {{{1
    # init names
    # nnames = init_sbc_nakshatra_names()
    nak = 0 # 0 is krittika, and so on

    ## first seven{{{2
    for y in range(1,8):
        # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
        # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
        # first row
        if(len(nakshatra[nak]) > 9):
            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[y][0][0],y=coords[y][0][1]+25))
        else:
            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[y][0][0]+10,y=coords[y][0][1]+25))
        nak+=1

    ## second seven, along the side{{{2
    for y in range(1,8):
        # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
        # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
        # first row
        if(len(nakshatra[nak]) > 9):
            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[8][y][0],y=coords[8][y][1]+25))
        else:
            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[8][y][0]+10,y=coords[8][y][1]+25))
        nak+=1

    ## third seven, along the bottom, need to count backwards this time{{{2
    for y in range(1,8).__reversed__():
        # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
        # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
        # first row
        if(len(nakshatra[nak]) > 9):
            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[y][8][0],y=coords[y][8][1]+25))
        else:
            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[y][8][0]+10,y=coords[y][8][1]+25))
        nak+=1

    ## fourth seven, along the left, need to count backwards this time{{{2
    for y in range(1,8).__reversed__():
        # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
        # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
        # first row
        if(len(nakshatra[nak]) > 9):
            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[0][y][0],y=coords[0][y][1]+25))
        else:
            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[0][y][0]+10,y=coords[0][y][1]+25))
        nak+=1

    # draw sanskrit letters {{{1

    ## outermost; a,A,i,I {{{2
    d.append(draw.Text("अ",font_size=20,x=coords[0][0][0]+5,y=coords[0][0][1]+22))
    d.append(draw.Text("आ",font_size=20,x=coords[8][0][0]+3,y=coords[8][0][1]+22))
    d.append(draw.Text("इ",font_size=20,x=coords[8][8][0]+8,y=coords[8][8][1]+22))
    d.append(draw.Text("ई",font_size=20,x=coords[0][8][0]+8,y=coords[0][8][1]+24))

    ## inner square of 28 letters {{{2
    letters=["उ","अ","व","क","ह","ड","ऊ","म","ट","प","र","त","ऋ","न","य","भ","ज","ख","ॠ","ग","स","द","च","ल"]
    let=0

    ## first seven{{{3
    for y in range(1,8):
        # first column is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
        # coords[y][x] is a tuple (a,b), so need to do coords[col][row][a]
        # first row
        d.append(draw.Text(letters[let],font_size=20,x=coords[y][1][0]+8,y=coords[y][1][1]+22))
        let+=1

    ## second seven, along the side
    for y in range(2,8):
        d.append(draw.Text(letters[let],font_size=20,x=coords[7][y][0]+8,y=coords[7][y][1]+22))
        let+=1

    ## third seven, along the bottom, need to count backwards this time
    for y in range(1,7).__reversed__():
        d.append(draw.Text(letters[let],font_size=20,x=coords[y][7][0]+8,y=coords[y][7][1]+22))
        let+=1

    ## fourth seven, along the left, need to count backwards this time
    for y in range(2,7).__reversed__():
        d.append(draw.Text(letters[let],font_size=20,x=coords[1][y][0]+8,y=coords[1][y][1]+22))
        let+=1

    ## middle square of four letters; lR,lRR,e,ai {{{2
    d.append(draw.Text("ऌ",font_size=20,x=coords[2][2][0]+7,y=coords[2][2][1]+22))
    d.append(draw.Text("ॡ",font_size=20,x=coords[6][2][0]+7,y=coords[6][2][1]+22))
    d.append(draw.Text("ए",font_size=20,x=coords[6][6][0]+8,y=coords[6][6][1]+21))
    d.append(draw.Text("ऐ",font_size=20,x=coords[2][6][0]+8,y=coords[2][6][1]+23))
                                                     

    ## inner square of four letters; o,au,aM,aH {{{2
    d.append(draw.Text("ओ",font_size=20,x=coords[3][3][0]+5,y=coords[3][3][1]+22))
    d.append(draw.Text("औ",font_size=20,x=coords[5][3][0]+3,y=coords[5][3][1]+22))
    d.append(draw.Text("अं",font_size=20,x=coords[5][5][0]+8,y=coords[5][5][1]+22))
    d.append(draw.Text("अः",font_size=20,x=coords[3][5][0]+5,y=coords[3][5][1]+24))
                                                   

    # draw aditya names {{{1
    # adityas = init_sbc_aditya_names()
    adit_coords=[(2,3),(3,2),(4,2),(5,2),(6,3),(6,4),(6,5),(5,6),(4,6),(3,6),(2,5),(2,4)]

    for n in range(12):
        thisx=adit_coords[n][0]
        thisy=adit_coords[n][1]
        d.append(draw.Text(adityas[n],font_size=5,x=coords[thisx][thisy][0]+5,y=coords[thisx][thisy][1]+25))


    # draw tithi names {{{1
        # nanda, bhadra, jaya, rikta, purna
        d.append(draw.Text(tithi[0],font_size=5,x=coords[4][3][0]+7,y=coords[4][3][1]+5))
        d.append(draw.Text(tithi[1],font_size=5,x=coords[5][4][0]+7,y=coords[5][4][1]+5))
        d.append(draw.Text(tithi[2],font_size=5,x=coords[4][5][0]+10,y=coords[4][5][1]+5))
        d.append(draw.Text(tithi[3],font_size=5,x=coords[3][4][0]+9,y=coords[3][4][1]+5))
        d.append(draw.Text(tithi[4],font_size=5,x=coords[4][4][0]+7,y=coords[4][4][1]+5))
    #}}}                      

    # Display
    d.set_pixel_scale(2)
    d.save_svg('sbc-algo.svg')
    d


def get_args():

    parser = argparse.ArgumentParser(
        prog="make-sbc-image",
        usage="%(prog)s [options]",
        description="make an image of the sarvatobhadra charka, an svg image",
    )
    parser.add_argument(
        "-Z",
        "--zodiac",
        action="store_true",
        help="use zodiac signs on the sbc. default is adityas",
    )

    args = parser.parse_args()
    return args

 # sbc.py
# original parsing of arguments
#    langfile=sc.langfile # default
#    themefile = sc.default_theme
#    zodiac = False
#
#        # read birth data and transit data from file 
#    if args.input_file:
#        input = open(sc.chartspath+args.input_file, "r")
#    else:
#        input = open(sc.default_input, "r")
#    for line in input:
#        if not "=" in line:
#            continue
#        field, value = line.split("=")
#        field = field.strip()
#        value = value.strip()
#        # get birth data
#        if field.startswith("Na") or field.startswith("na"):
#            name = value
#        if field.startswith("Da") or field.startswith("da"):
#            bmonth, bday, byear = putil.intize_date(value)
#        if field.startswith("Pla") or field.startswith("pla"):
#            bplace = value
#        if field.startswith("Ti") or field.startswith("ti"):
#            ephclock = putil.intize_time(value)
#        if field.startswith("La") or field.startswith("la"):
#            blat = float(value)
#        if field.startswith("Lo") or field.startswith("lo"):
#            blong = float(value)
#        # get transit data; time and lat and long
#        if field.startswith("TDa") or field.startswith("tda"):
#            if value == "now":
#                nowtime = time.gmtime()
#                tyear = nowtime[0]
#                tmonth = nowtime[1] 
#                tday = nowtime[2]
#            else:
#                tmonth, tday, tyear = putil.intize_date(value)
#        if field.startswith("TPla") or field.startswith("tpla"):
#            tplace = value
#        if field.startswith("TTi") or field.startswith("tti"):
#            if value == "now":
#                nowtime = time.gmtime()
#                transit_ephclock = nowtime[3] + nowtime[4] / 60 + nowtime[5] / 3600
#            else:
#                transit_ephclock = putil.intize_time(value)
#        if field.startswith("TLa") or field.startswith("tla"):
#            tlat = float(value)
#        if field.startswith("TLo") or field.startswith("tlo"):
#            tlong = float(value)
#    bephtime = JulianDay(swe.julday(byear, bmonth, bday, ephclock))
#    transit_ephtime = JulianDay(swe.julday(tyear, tmonth, tday, transit_ephclock))
#    input.close()

#   sbc.py
#    this was to test where glyphs were placed
#    nakcount[27]=0
#    for i in range(8):
#        num = 8
#        ny,nx = sc.nak_coords[27]
#        d.append(draw.Text(sc.pglyphs[i],font_size=poffsets[num][0],x=coords[ny][nx][0]+(poffsets[num][1][nakcount[27]][0]),y=coords[ny][nx][1]+(poffsets[num][1][nakcount[27]][1])))
#        nakcount[27]+=1

# sbc.py
# this was used to test positions of nakshatras
#    nakcount = [0 for i in range(28)] # count how many planets in each nakshatra
#    for i in range(8):
#        num = 8
#        wnak = 24 
#        ny,nx = sc.nak_coords[wnak]
#        d.append(draw.Text(sc.pglyphs[i],font_size=15,x=coords[ny][nx][0]+(toffleft[num][nakcount[wnak]][0]),y=coords[ny][nx][1]+(toffleft[num][nakcount[wnak]][1])))
#        nakcount[wnak]+=1
#    nakcount = [0 for i in range(28)] # count how many planets in each nakshatra
#    for i in range(8):
#        num = 8
#        wnak = 14 
#        ny,nx = sc.nak_coords[wnak]
#        d.append(draw.Text(sc.pglyphs[i],font_size=15,x=coords[ny][nx][0]+(toffbot[num][nakcount[wnak]][0]),y=coords[ny][nx][1]+(toffbot[num][nakcount[wnak]][1])))
#        nakcount[wnak]+=1
#    nakcount = [0 for i in range(28)] # count how many planets in each nakshatra
#    for i in range(8):
#        num = 8
#        wnak = 9
#        ny,nx = sc.nak_coords[wnak]
#        d.append(draw.Text(sc.pglyphs[i],font_size=15,x=coords[ny][nx][0]+(toffright[num][nakcount[wnak]][0]),y=coords[ny][nx][1]+(toffright[num][nakcount[wnak]][1])))
#        nakcount[wnak]+=1
#    nakcount = [0 for i in range(28)] # count how many planets in each nakshatra
#    for i in range(8):
#        num = 8
#        wnak = 3
#        ny,nx = sc.nak_coords[wnak]
#        d.append(draw.Text(sc.pglyphs[i],font_size=15,x=coords[ny][nx][0]+(toffup[num][nakcount[wnak]][0]),y=coords[ny][nx][1]+(toffup[num][nakcount[wnak]][1])))
#        nakcount[wnak]+=1


# sbc_constants.py; drawing parts of the chakra itself
#    ## first seven{{{2
#    for y in range(1,8):
#        # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
#        # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
#        # first row
#        if(len(nakshatra[nak]) > 9):
#            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[y][0][0],y=coords[y][0][1]+25))
#        else:
#            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[y][0][0]+10,y=coords[y][0][1]+25))
#        nak+=1
#
#    ## second seven, along the side{{{2
#    for y in range(1,8):
#        # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
#        # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
#        # first row
#        if(len(nakshatra[nak]) > 9):
#            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[8][y][0],y=coords[8][y][1]+25))
#        else:
#            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[8][y][0]+10,y=coords[8][y][1]+25))
#        nak+=1
#
#    ## third seven, along the bottom, need to count backwards this time{{{2
#    for y in range(1,8).__reversed__():
#        # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
#        # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
#        # first row
#        if(len(nakshatra[nak]) > 9):
#            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[y][8][0],y=coords[y][8][1]+25))
#        else:
#            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[y][8][0]+10,y=coords[y][8][1]+25))
#        nak+=1
#
#    ## fourth seven, along the left, need to count backwards this time{{{2
#    for y in range(1,8).__reversed__():
#        # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
#        # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
#        # first row
#        if(len(nakshatra[nak]) > 9):
#            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[0][y][0],y=coords[0][y][1]+25))
#        else:
#            d.append(draw.Text(nakshatra[nak],font_size=5,x=coords[0][y][0]+10,y=coords[0][y][1]+25))
#        nak+=1
#
#                                                                         #}}}
#                                                                          #}}}
                                      #}}}
# original versions of name init functions

def init_sbc_nakshatra_names(langfile=mixed):
    names = configparser.ConfigParser()
    names.read(langfile)

    nakshatra = []

    nnames = names["NAKSHATRA"]

    nakshatra.append(nnames["Krittika"])
    nakshatra.append(nnames["Rohini"])
    nakshatra.append(nnames["Mrigashira"])
    nakshatra.append(nnames["Ardra"])
    nakshatra.append(nnames["Punarvasu"])
    nakshatra.append(nnames["Pushya"])
    nakshatra.append(nnames["Ashlesha"])
    nakshatra.append(nnames["Magha"])
    nakshatra.append(nnames["Purva Phalguni"])
    nakshatra.append(nnames["Uttara Phalguni"])
    nakshatra.append(nnames["Hasta"])
    nakshatra.append(nnames["Chitra"])
    nakshatra.append(nnames["Svati"])
    nakshatra.append(nnames["Vishakha"])
    nakshatra.append(nnames["Anuradha"])
    nakshatra.append(nnames["Jyeshtha"])
    nakshatra.append(nnames["Mula"])
    nakshatra.append(nnames["Purva Ashadha"])
    nakshatra.append(nnames["Uttara Ashadha"])
    nakshatra.append(nnames["Abhijit"])
    nakshatra.append(nnames["Shravana"])
    nakshatra.append(nnames["Danishtha"])
    nakshatra.append(nnames["Shatabhisha"])
    nakshatra.append(nnames["Purva Bhadrapada"])
    nakshatra.append(nnames["Uttara Bhadrapada"])
    nakshatra.append(nnames["Revati"])
    nakshatra.append(nnames["Ashvini"])
    nakshatra.append(nnames["Bharani"])

    return nakshatra

def init_sbc_aditya_names(langfile=mixed):
    names = configparser.ConfigParser()
    names.read(langfile)

    adityas = []

    anames = names["ADITYAS"]

    adityas.append(anames["Dhata"])
    adityas.append(anames["Aryama"])
    adityas.append(anames["Mitra"])
    adityas.append(anames["Varuna"])
    adityas.append(anames["Indra"])
    adityas.append(anames["Vivasvan"])
    adityas.append(anames["Tvashta"])
    adityas.append(anames["Vishnu"])
    adityas.append(anames["Amshu"])
    adityas.append(anames["Bhaga"])
    adityas.append(anames["Pusha"])
    adityas.append(anames["Parjanya"])
    
    return adityas


# this was a program called make_sbc_image.py

#!/usr/bin/python

import drawsvg as draw
import argparse
import sbcnames
import sbc_constants as sc

global args

def make_sbc_main():
    global args
    args = get_args()

    d = draw.Drawing(500, 500)

    d = sc.draw_chakra(d,args.zodiac)

    # Display
    d.set_pixel_scale(2)
    if args.output_file:
        d.save_svg(args.output_file)
    elif args.zodiac:
        d.save_svg(sc.sbc_image_zodiac)
    else:
        d.save_svg(sc.sbc_image)
    d



def get_args():
    parser = argparse.ArgumentParser(
        prog="make-sbc-image",
        usage="%(prog)s [options]", 
        description=f"make an image of the sarvatobhadra charka, an svg image. default is adityas and \n28 equal nakshatras with krtikka and aryama at the ascending equinox",
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

make_sbc_main() 
