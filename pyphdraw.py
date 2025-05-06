#!/usr/bin/python

import swisseph as swe
import argparse
import time
from drawlib.apis import *
import pyphglobals as pglob
import pyphutils as putil
from pyphclasses import *
from pyphobjs import *
from pyphconstants import *


global ephtime
image_dir = "/home/josh/w/astro/soft/pyphemeris/images/"


def main():
    global ephtime
    args = get_args()

    if args.lang:
        pglob.init_names(args.lang)
    else:
        pglob.init_names(pglob.langfile)

    if args.edir:
        swe.set_ephe_path(args.edir)
    else:
        swe.set_ephe_path(pglob.edir)

    if args.timezone:
        pglob.timezone = args.timezone

    if args.julian:
        # user entered a julian day
        ephtime = JulianDay(float(args.julian))

    if args.date:
        month, day, year = putil.intize_date(args.date)
    if args.time:
        ephclock = putil.intize_time(args.time)
    if args.date:
        if args.time:
            ephtime = JulianDay(swe.julday(year, month, day, ephclock))
        else:
            nowtime = time.gmtime()
            ephtime = JulianDay(
                swe.julday(
                    year, month, day, nowtime[3] + nowtime[4] / 60 + nowtime[5] / 3600
                )
            )
    else:
        if args.time:
            nowtime = time.gmtime()
            ephtime = JulianDay((nowtime[0], nowtime[1], nowtime[2], ephclock))
        else:
            ephtime = JulianDay()

    if args.helios:
        sysflg = pglob.HELIO
    elif args.baryos:
        sysflg = pglob.BARY
    else:
        sysflg = pglob.ECL

    if args.adityas:
        signs = "adityas"
    else:
        signs = "rasis"

    draw_base_chart(sysflg, signs)

    # start drawing the chart
    draw_date(ephtime)

    if sysflg == pglob.HELIO:
        draw_heliocentric_planets()

    save(file=image_dir + "pyphdraw.png")


def draw_base_chart(ctype, signs):
    config(width=100, height=200, grid_only=True)
    # used typst to make a circle with 12 lines, angles of 30 degrees
    if ctype == pglob.HELIO:
        draw_heliocentric_base()
    elif ctype == pglob.BARY:
        draw_barycentric_base()
    else:
        draw_south_indian_base()

    if signs == "rasis":
        if ctype == pglob.HELIO or ctype == pglob.BARY:
            draw_signs_circle()
        else:
            draw_signs_square()
    if signs == "adityas":
        if ctype == pglob.HELIO or ctype == pglob.BARY:
            draw_adityas_circle()
        else:
            draw_signs_square()


def draw_date(jd=JulianDay()):
    txt = f"{jd}"
    utc, usr, julian = txt.split("\n")
    text(xy=(2, 197), text=utc, style=TextStyle(halign="left"))
    text(xy=(2, 194), text=usr, style=TextStyle(halign="left"))
    text(xy=(2, 191), text=julian, style=TextStyle(halign="left"))


def draw_table(tdata):
    table = dsart.Table()
    table.clear_styles()
    table.draw(
        xy=(50, 150),
        width=10,
        height=10,
        data=tdata,
    )


def draw_heliocentric_planets(planets):
    # since it is heliocentric, there is no Sun and no Rahu and Ketu
    # so indexes 1,2,3,4,5,6,7,8,9 and 12 will be printed
    signs_index = per_sign(planets, pglob.HELIO)
    for sign in range(12):
        if len(signs_index[sign]) == 1:
            image(
                xy=coords_list[sign][0],
                width=pwidth,
                image=planet_glyphs[signs_index[sign][0]],
            )
        if len(signs_index[sign]) > 1:
            for n in range(len(signs_index[sign])):
                image(
                    xy=coords_list[sign][n + 1],
                    width=pwidth,
                    image=planet_glyphs[signs_index[sign][n]],
                )


def per_sign(planets, sysflg):
    """
    takes a list of planets, and returns a list of lists of indexes
    showing what planet is in which sign
    e.g., if sun and mercury are in aries, then the first element of the list
    will be the list [0,2], containing the indexes of the planets in the sign
    """
    signs_index = [
        [] for _ in range(12)
    ]  # initialize our empty list with 12 empty lists
    for i in range(len(planets)):
        if sysflg == pglob.HELIO:  # skip sun, rahu, ketu
            if i == 0 or i == 10 or i == 11:
                continue
        if sysflg == pglob.BARY:  # skip rahu and ketu
            if i == 10 or i == 11:
                continue
        signs_index[planets[i].sign_index(sysflg)].append(i)
    return signs_index


def draw_heliocentric_base():
    image(xy=(50, 50), width=100, image=image_dir + "heliocentric.png")
    # outer edge of the wheel
    donuts(xy=(50, 50), radius=40, width=4)


def draw_barycentric_base():
    image(
        xy=(50, 50), width=100, image=image_dir + "barycentric.png"
    )  # for barycentric charts
    # outer edge of the wheel
    donuts(xy=(50, 50), radius=40, width=4)


def draw_south_indian_base():
    image(xy=(50, 50), width=100, image=image_dir + "south_indian_base.png")


def draw_signs_circle():
    # now draw sign glyphs onto the circle
    image(xy=(88, 50), width=3, image=image_dir + "glyphs/aries.png")
    image(xy=(82.5, 70), width=3, image=image_dir + "glyphs/taurus.png")
    image(xy=(69, 83), width=3, image=image_dir + "glyphs/gemini.png")
    image(xy=(50, 88), width=3, image=image_dir + "glyphs/cancer.png")
    image(xy=(31, 83), width=3, image=image_dir + "glyphs/leo.png")
    image(xy=(17.5, 70), width=3, image=image_dir + "glyphs/virgo.png")
    image(xy=(12, 50), width=3, image=image_dir + "glyphs/libra.png")
    image(xy=(17.5, 30), width=3, image=image_dir + "glyphs/scorpio.png")
    image(xy=(31, 17), width=3, image=image_dir + "glyphs/sagittarius.png")
    image(xy=(50, 12), width=3, image=image_dir + "glyphs/capricorn.png")
    image(xy=(69, 17), width=3, image=image_dir + "glyphs/aquarius.png")
    image(xy=(82.5, 30), width=3, image=image_dir + "glyphs/pisces.png")


def draw_adityas_circle():
    # now draw aditya names on the outside of the circle
    # these names were very specifically placed
    text(
        xy=(95, 50),
        text=pglob.adityas[0],  # , style=TextStyle(font=FontSerif.COURIER_BOLD)
    )
    text(xy=(89, 72), text=pglob.adityas[1])
    text(xy=(72, 89), text=pglob.adityas[2])
    text(xy=(50, 94), text=pglob.adityas[3])
    text(xy=(26, 88), text=pglob.adityas[4])
    text(xy=(10, 72), text=pglob.adityas[5])
    text(xy=(5, 50), text=pglob.adityas[6])
    text(xy=(10, 29), text=pglob.adityas[7])
    text(xy=(26, 13), text=pglob.adityas[8])
    text(xy=(50, 5), text=pglob.adityas[9])
    text(xy=(74, 12), text=pglob.adityas[10])
    text(xy=(89, 29), text=pglob.adityas[11])


def draw_signs_square():
    return


def draw_adityas_square():
    return


def get_args():
    parser = argparse.ArgumentParser(
        prog="pyphdraw",
        usage="%(prog)s [options]",
        description="draw a chart for -d MM/DD/YYYY -t HH:MM:SS (utc)",
    )
    parser.add_argument(
        "-d",
        "--date",
        help="date specified as MM/DD/YYYY; if not present will give the current day",
    )
    parser.add_argument(
        "-t",
        "--time",
        help="time specified as HH:MM:SS, (utc); if not present will use midnight utc",
    )
    parser.add_argument("-j", "--julian", help="time specificed as the julian day")
    parser.add_argument("-e", "--edir", help="path to swiss ephemeris files")
    parser.add_argument(
        "-a", "--ayanamsa", help="pass swisseph value for desired ayanamsa"
    )
    parser.add_argument(
        "-u",
        "--utcoffset",
        help="utc offset in hours, positive is east; default is currently -4 (EDT)",
    )
    parser.add_argument(
        "-H",
        "--house",
        help="house system, default: C for Campanus; try R for Regiomantus",
    )
    parser.add_argument(
        "-p",
        "--position",
        help="latitude and longitutde in the form NN,EE; north and east are positive; don't pass directional letters; if latitude is negative, pass argument as -p=-30,40, for example",
    )
    parser.add_argument(
        "-s", "--helios", action="store_true", help="heliocentric coordinates"
    )
    parser.add_argument(
        "-b",
        "--baryos",
        action="store_true",
        help="barycentric coordinates - i.e., with the solar system's barycenter as the center of the coordinate system",
    )
    parser.add_argument(
        "-A",
        "--adityas",
        action="store_true",
        help="toggle printing adityas from the default behavior",
    )
    parser.add_argument("-l", "--lang", help="language file; default is ./dict.eng")
    parser.add_argument(
        "-z", "--timezone", help="a string showing the timezone; e.g., CDT"
    )
    args = parser.parse_args()
    return args


main()
