#!/usr/bin/python

import drawsvg as draw
from sbcnames import *

d = draw.Drawing(500, 500)

# Background pattern (not supported by Cairo, d.rasterize() will not show it)
#pattern = draw.Pattern(width=0.20, height=0.20)
#pattern.append(draw.Rectangle(0, 0, .15, .15, fill='#00ff00'))
#d.draw(draw.Rectangle(-0.75, -0.75, 1.5, 1, fill=pattern, fill_opacity=0.4))
d.append(draw.Circle(250,250,250,fill='khaki'))

# makes coordinate system that that
# coords[r][c] gives the coordinates for the square in the
# rth row and cth column
def make_coords(x=40,y=40):
    # each list is a row, so coords[3][4] will get the 5th column of the 4th row
    coords = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for n in range(9):
            coords[i].append(tuple((x*(i+2),y+(40*(n+1)))))
    return coords

coords=make_coords()

# draw the 81 squares of the chakra
for i in range(9):
    for n in range(9):
        d.append(draw.Rectangle(coords[i][n][0], coords[i][n][1], 30, 30, rx='1', ry='1', stroke='black', fill='yellow'))

# draw names of nakshatras
# init names
nnames = init_sbcaditya_names()
nak = 0 # 0 is krittika, and so on

## first seven
for y in range(1,8):
    # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
    # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
    # first row
    if(len(nnames[nak]) > 9):
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[y][0][0],y=coords[y][0][1]+25))
    else:
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[y][0][0]+10,y=coords[y][0][1]+25))
    nak+=1

## second seven, along the side
for y in range(1,8):
    # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
    # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
    # first row
    if(len(nnames[nak]) > 9):
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[8][y][0],y=coords[8][y][1]+25))
    else:
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[8][y][0]+10,y=coords[8][y][1]+25))
    nak+=1

## third seven, along the bottom, need to count backwards this time
for y in range(1,8).__reversed__():
    # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
    # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
    # first row
    if(len(nnames[nak]) > 9):
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[y][8][0],y=coords[y][8][1]+25))
    else:
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[y][8][0]+10,y=coords[y][8][1]+25))
    nak+=1

for y in range(1,8).__reversed__():
    # first row is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
    # coords[x][y] is a tuple (a,b), so need to do coords[x][y][a]
    # first row
    if(len(nnames[nak]) > 9):
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[0][y][0],y=coords[0][y][1]+25))
    else:
        d.append(draw.Text(nnames[nak],font_size=5,x=coords[0][y][0]+10,y=coords[0][y][1]+25))
    nak+=1


# Display
d.set_pixel_scale(2)
d.save_svg('sbc-algo.svg')
d
