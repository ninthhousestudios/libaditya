#!/usr/bin/python

import drawsvg as draw
import argparse
import sbcnames

def main():
    args = get_args()

    d = draw.Drawing(500, 500)

    d.append(draw.Circle(250,250,250,fill='yellow'))
    d.append(draw.Circle(250,250,245,fill='black'))
    d.append(draw.Circle(250,250,240,fill='yellow'))
    d.append(draw.Circle(250,250,225,fill='blue'))
    d.append(draw.Circle(250,250,200,fill='yellow'))
    d.append(draw.Circle(250,250,175,fill='red'))
    d.append(draw.Circle(250,250,150,fill='yellow'))
    d.append(draw.Circle(250,250,125,fill='purple'))
    d.append(draw.Circle(250,250,100,fill='yellow'))
    d.append(draw.Circle(250,250,75,fill='black'))
    d.append(draw.Circle(250,250,50,fill='yellow'))

    # makes coordinate system that that
    # coords[c][r] gives the coordinates for the square in the
    # cth column and rth row
    coords=sbcnames.make_coords()

    # nakshatra names have to be drawn in order, but for drawing and coloring
    # the boxes themselves, any order is fine
    nak_coords = []
    for y in range(1,8):
        nak_coords.append((y,0))
        nak_coords.append((0,y))
        nak_coords.append((y,8))
        nak_coords.append((8,y))

    # coloring the boxes
    # diagonals will be purple, here are their sbc coordinates
    diag_coords=[(0,0),(1,1),(2,2),(3,3),(8,8),(7,7),(6,6),(5,5),(8,0),(7,1),(6,2),(5,3),(0,8),(1,7),(2,6),(3,5)]

    # the outer most square of letters
    outer_letters_coords=[(2,1),(3,1),(4,1),(5,1),(6,1),(7,2),(7,3),(7,4),(7,5),(7,6),(6,7),(5,7),(4,7),(3,7),(2,7),(1,6),(1,5),(1,4),(1,3),(1,2)]

    # rashis
    rashis_coords=[(3,2),(4,2),(5,2),(6,3),(6,4),(6,5),(5,6),(4,6),(3,6),(2,5),(2,4),(2,3)]

    # four tithis
    tithi_coords=[(4,3),(5,4),(4,5),(3,4)]
    
    # draw the 81 squares of the chakra
    for i in range(9):
        for n in range(9):
            if (i,n) in diag_coords:
                d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30,
                                        30, rx='1', ry='1', stroke='black',
                                        fill='#6b00ff'))
            elif (i,n) in outer_letters_coords:
                d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30,
                                        30, rx='1', ry='1', stroke='black',
                                        fill='forestgreen'))
            elif (i,n) in nak_coords:
                d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30,
                                        30, rx='1', ry='1', stroke='black',
                                        fill='orange')) # #9980ff
            elif (i,n) in rashis_coords:
                d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30,
                                        30, rx='1', ry='1', stroke='black',
                                        fill='cyan'))
            elif (i,n) in tithi_coords:
                d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30,
                                        30, rx='1', ry='1', stroke='black',
                                        fill='red'))
            elif (i,n) == (4,4):
                d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30,
                                        30, rx='1', ry='1', stroke='black',
                                        fill='black'))
            else:
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
    adit_coords=[(3,2),(4,2),(5,2),(6,3),(6,4),(6,5),(5,6),(4,6),(3,6),(2,5),(2,4),(2,3)]

    for n in range(12):
        thisx=adit_coords[n][0]
        thisy=adit_coords[n][1]
        d.append(draw.Text(adityas[n],font_size=5,x=coords[thisx][thisy][0]+5,y=coords[thisx][thisy][1]+25))


    # draw tithi names and vara names {{{1
        # nanda, ravivara, mangalavara
        d.append(draw.Text(tithi[0],font_size=5,x=coords[4][3][0]+9,y=coords[4][3][1]+5))
        d.append(draw.Text(vara[0],font_size=5,x=coords[4][3][0]+7,y=coords[4][3][1]+20))
        d.append(draw.Text(vara[2],font_size=5,x=coords[4][3][0]+3,y=coords[4][3][1]+25))
        # bhadra, somavara, budhavara
        d.append(draw.Text(tithi[1],font_size=5,x=coords[5][4][0]+8,y=coords[5][4][1]+5))
        d.append(draw.Text(vara[1],font_size=5,x=coords[5][4][0]+6,y=coords[5][4][1]+20))
        d.append(draw.Text(vara[3],font_size=5,x=coords[5][4][0]+5,y=coords[5][4][1]+25))
        # jaya, guruvara
        d.append(draw.Text(tithi[2],font_size=5,x=coords[4][5][0]+11,y=coords[4][5][1]+5))
        d.append(draw.Text(vara[4],font_size=5,x=coords[4][5][0]+7,y=coords[4][5][1]+25))
        # rikta, shukravara
        d.append(draw.Text(tithi[3],font_size=5,x=coords[3][4][0]+11,y=coords[3][4][1]+5))
        d.append(draw.Text(vara[5],font_size=5,x=coords[3][4][0]+6,y=coords[3][4][1]+25))
        # purna, shanivara
        d.append(draw.Text(tithi[4],font_size=5,x=coords[4][4][0]+9,y=coords[4][4][1]+5,fill="white"))
        d.append(draw.Text(vara[6],font_size=5,x=coords[4][4][0]+7,y=coords[4][4][1]+25,fill="white"))
    #}}}                      

    # Display
    d.set_pixel_scale(2)
    if args.zodiac:
        d.save_svg('sbc-signs.svg')
    else:
        d.save_svg('sbc.svg')
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

    args = parser.parse_args()
    return args

main() 
