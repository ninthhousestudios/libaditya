#!/usr/bin/python

import drawsvg as draw
from sbcnames import *

d = draw.Drawing(500, 500)

d.append(draw.Circle(250,250,250,fill='khaki'))

# makes coordinate system that that
# coords[c][r] gives the coordinates for the square in the
# cth column and rth row
def make_coords(x=40,y=40):
    # each list is a row, so coords[3][4] will get the 5th column of the 4th row
    coords = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for n in range(9):
            coords[i].append(tuple((x*(i+2)-4,y+(40*(n+1))-5)))
    return coords

coords=make_coords()

# draw the 81 squares of the chakra
for i in range(9):
    for n in range(9):
        d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30, 30, rx='1', ry='1', stroke='black', fill='yellow'))

# draw names of nakshatras {{{1
# init names
nnames = init_sbc_nakshatra_names()
nak = 0 # 0 is krittika, and so on

## first seven{{{2
for y in range(1,8):
    # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
    # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
    # first row
    if(len(nnames[nak]) > 9):
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[y][0][0],y=coords[y][0][1]+25))
    else:
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[y][0][0]+10,y=coords[y][0][1]+25))
    nak+=1

## second seven, along the side{{{2
for y in range(1,8):
    # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
    # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
    # first row
    if(len(nnames[nak]) > 9):
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[8][y][0],y=coords[8][y][1]+25))
    else:
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[8][y][0]+10,y=coords[8][y][1]+25))
    nak+=1

## third seven, along the bottom, need to count backwards this time{{{2
for y in range(1,8).__reversed__():
    # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
    # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
    # first row
    if(len(nnames[nak]) > 9):
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[y][8][0],y=coords[y][8][1]+25))
    else:
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[y][8][0]+10,y=coords[y][8][1]+25))
    nak+=1

## fourth seven, along the left, need to count backwards this time{{{2
for y in range(1,8).__reversed__():
    # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
    # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
    # first row
    if(len(nnames[nak]) > 9):
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[0][y][0],y=coords[0][y][1]+25))
    else:
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[0][y][0]+10,y=coords[0][y][1]+25))
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
    d.append(draw.Text(letters[let],font_size=20,x=coords[y][1][0]+5,y=coords[y][1][1]+22))
    let+=1

## second seven, along the side{{{3
for y in range(2,8):
    d.append(draw.Text(letters[let],font_size=20,x=coords[7][y][0]+5,y=coords[7][y][1]+22))
    let+=1

## third seven, along the bottom, need to count backwards this time{{{3
for y in range(1,7).__reversed__():
    d.append(draw.Text(letters[let],font_size=20,x=coords[y][7][0]+5,y=coords[y][7][1]+22))
    let+=1

## fourth seven, along the left, need to count backwards this time{{{3
for y in range(2,7).__reversed__():
    d.append(draw.Text(letters[let],font_size=20,x=coords[1][y][0]+5,y=coords[1][y][1]+22))
    let+=1

## middle square of four letters; lR,lRR,e,ai {{{2
d.append(draw.Text("ऌ",font_size=20,x=coords[2][2][0]+5,y=coords[2][2][1]+22))
d.append(draw.Text("ॡ",font_size=20,x=coords[6][2][0]+3,y=coords[6][2][1]+22))
d.append(draw.Text("ए",font_size=20,x=coords[6][6][0]+8,y=coords[6][6][1]+22))
d.append(draw.Text("ऐ",font_size=20,x=coords[2][6][0]+8,y=coords[2][6][1]+24))

## inner square of four letters; o,au,aM,aH {{{2
d.append(draw.Text("ओ",font_size=20,x=coords[3][3][0]+5,y=coords[3][3][1]+22))
d.append(draw.Text("औ",font_size=20,x=coords[5][3][0]+3,y=coords[5][3][1]+22))
d.append(draw.Text("अं",font_size=20,x=coords[5][5][0]+8,y=coords[5][5][1]+22))
d.append(draw.Text("अः",font_size=20,x=coords[3][5][0]+5,y=coords[3][5][1]+24))


# draw aditya names {{{1
adityas = init_sbc_aditya_names()
adit_coords=[(2,3),(3,2),(4,2),(5,2),(6,3),(6,4),(6,5),(5,6),(4,6),(3,6),(2,5),(2,4)]

for n in range(12):
    thisx=adit_coords[n][0]
    thisy=adit_coords[n][1]
    d.append(draw.Text(adityas[n],font_size=5,x=coords[thisx][thisy][0]+5,y=coords[thisx][thisy][1]+25))

# Display
d.set_pixel_scale(2)
d.save_svg('sbc-algo.svg')
d
