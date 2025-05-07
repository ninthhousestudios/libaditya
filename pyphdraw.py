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

    # the correct coordinates according to sysflg
    # are gotten in the per_signs function
    planets = init_Planets(ephtime)

    # start drawing the chart
    draw_base_chart(sysflg, signs)
    if sysflg != pglob.ECL:
        draw_date_circle(ephtime)
        draw_panchanga_circle(Panchanga(ephtime))
        draw_table_circle(planets_table_circle(planets, sysflg))
    else:
        draw_date_square(ephtime)
        draw_panchanga_square(Panchanga(ephtime))
        draw_table_square(planets_table_square(planets, sysflg))

    if sysflg == pglob.HELIO:
        draw_heliocentric_planets(planets)
    elif sysflg == pglob.BARY:
        draw_barycentric_planets(planets)
    else:
        if args.adityas:
            draw_south_indian_planets_adityas(planets)
        else:
            draw_south_indian_planets(planets)

    save(file=image_dir + "pyphdraw.png")


def draw_base_chart(ctype, signs):
    # used typst to make a circle with 12 lines, angles of 30 degrees
    if ctype == pglob.HELIO:
        config(width=100, height=150, grid_only=True)
        draw_heliocentric_base()
    elif ctype == pglob.BARY:
        config(width=100, height=150, grid_only=True)
        draw_barycentric_base()
    else:
        config(width=100, height=175, grid_only=True)
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
            draw_adityas_square()


def draw_date_circle(jd=JulianDay()):
    txt = f"{jd}"
    utc, usr, julian = txt.split("\n")
    text(xy=(60, 143), text=utc, style=TextStyle(halign="left"))
    text(xy=(60, 140), text=usr, style=TextStyle(halign="left"))
    text(xy=(60, 137), text=julian, style=TextStyle(halign="left"))


def draw_date_square(jd=JulianDay()):
    txt = f"{jd}"
    utc, usr, julian = txt.split("\n")
    text(xy=(5, 165), text=utc, style=TextStyle(halign="left"))
    text(xy=(5, 161), text=usr, style=TextStyle(halign="left"))
    text(xy=(5, 157), text=julian, style=TextStyle(halign="left"))


def draw_table_circle(tdata):
    table = dsart.Table()
    table.clear_styles()
    table.draw(
        xy=(2, 145),
        width=40,
        height=50,
        data=tdata,
    )


def draw_table_square(tdata):
    table = dsart.Table()
    table.clear_styles()
    table.draw(
        xy=(2, 145),
        width=40,
        height=50,
        data=tdata,
    )


def draw_heliocentric_planets(planets):
    # since it is heliocentric, there is no Sun and no Rahu and Ketu
    # so indexes 1,2,3,4,5,6,7,8,9 and 12 will be printed
    signs_index = per_sign(planets, pglob.HELIO)
    for sign in range(12):
        if len(signs_index[sign]) == 1:
            image(
                xy=hb_coords_list[sign][0],
                width=pwidth,
                image=planet_glyphs[signs_index[sign][0]],
            )
        if len(signs_index[sign]) > 1:
            for n in range(len(signs_index[sign])):
                image(
                    xy=hb_coords_list[sign][n + 1],
                    width=pwidth,
                    image=planet_glyphs[signs_index[sign][n]],
                )


def draw_barycentric_planets(planets):
    # since it is barycentric, there is no Rahu and Ketu
    # so indexes 0,1,2,3,4,5,6,7,8,9 and 12 will be printed
    signs_index = per_sign(planets, pglob.BARY)
    for sign in range(12):
        if len(signs_index[sign]) == 1:
            image(
                xy=hb_coords_list[sign][0],
                width=pwidth,
                image=planet_glyphs[signs_index[sign][0]],
            )
        if len(signs_index[sign]) > 1:
            for n in range(len(signs_index[sign])):
                image(
                    xy=hb_coords_list[sign][n + 1],
                    width=pwidth,
                    image=planet_glyphs[signs_index[sign][n]],
                )


def draw_south_indian_planets(planets):
    pwidth = 4
    signs_index = per_sign(planets, pglob.ECL)
    for sign in range(12):
        for planet in range(len(signs_index[sign])):
            image(
                xy=geo_coords_list[sign][planet],
                width=pwidth,
                image=planet_glyphs[signs_index[sign][planet]],
            )


def draw_south_indian_planets_adityas(planets):
    pwidth = 4
    signs_index = per_sign(planets, pglob.ECL)
    for sign in range(12):
        for planet in range(len(signs_index[sign])):
            image(
                # planets in aries go into taurus for the adityas
                xy=geo_coords_list[(sign + 1) % 12][planet],
                width=pwidth,
                image=planet_glyphs[signs_index[sign][planet]],
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
        if sysflg == pglob.ECL:  # skip the earth
            if i == 12:
                continue
        signs_index[planets[i].sign_index(sysflg)].append(i)
    return signs_index


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


def planets_table_circle(planets, sysflg=pglob.ECL):
    """
    return a PrettyTable string with coordinates for all planets on julianday
    using sysflag coordinates
    """
    output = []
    if sysflg == pglob.HELIO:
        output.append(["Heliocentric", " "])
    if sysflg == pglob.BARY:
        output.append(["Barycentric", " "])
    output.append(
        [
            "Planet",
            "Longitude",
        ]
    )
    # get coordinates for Sun through Pluto, 10 planets
    for i in range(10):
        if (
            i == 0 and sysflg == pglob.HELIO
        ):  # dont print sun if heliocentric coordinates
            continue
        output.append(
            [planets[i].planet_name] + [putil.yessignize(planets[i].longitude(sysflg))]
        )

    # if getting ECL or EQU, add Rahu and Ketu
    if sysflg == pglob.ECL:
        # output.add_row(Planets[pglob.rahu].table_list(sysflg))
        # ketuls = Planets[pglob.ketu].table_list(sysflg)
        # ketuls[1] = pglob.sign_func((Planets[pglob.rahu].coords[0] - 180) % 360)
        # output.add_row(ketuls)
        output.append(
            [planets[10].planet_name]
            + [putil.yessignize(planets[10].longitude(sysflg))]
        )
        output.append(
            [planets[11].planet_name]
            + [putil.yessignize(planets[11].longitude(sysflg))]
        )

    # if helio or bary coordinates, dont add rahu or ketu but add earth
    if sysflg == pglob.HELIO or sysflg == pglob.BARY:
        output.append(
            ["Earth"] + [putil.yessignize(planets[pglob.earth].longitude(sysflg))]
        )

    return output


def planets_table_square(planets, sysflg=pglob.ECL):
    """
    return a PrettyTable string with coordinates for all planets on julianday
    using sysflag coordinates
    """
    output = []
    output.append(
        [
            "Planet",
            "Longitude",
        ]
    )
    # get coordinates for Sun through Pluto, 10 planets
    for i in range(10):
        if (
            i == 0 and sysflg == pglob.HELIO
        ):  # dont print sun if heliocentric coordinates
            continue
        output.append(
            [planets[i].planet_name] + [putil.yessignize(planets[i].longitude(sysflg))]
        )

    # if getting ECL or EQU, add Rahu and Ketu
    if sysflg == pglob.ECL:
        # output.add_row(Planets[pglob.rahu].table_list(sysflg))
        # ketuls = Planets[pglob.ketu].table_list(sysflg)
        # ketuls[1] = pglob.sign_func((Planets[pglob.rahu].coords[0] - 180) % 360)
        # output.add_row(ketuls)
        output.append(
            [planets[10].planet_name]
            + [putil.yessignize(planets[10].longitude(sysflg))]
        )
        output.append(
            [planets[11].planet_name]
            + [putil.yessignize(planets[11].longitude(sysflg))]
        )

    # if helio or bary coordinates, dont add rahu or ketu but add earth
    if sysflg == pglob.HELIO or sysflg == pglob.BARY:
        output.append(
            ["Earth"] + [putil.yessignize(planets[pglob.earth].longitude(sysflg))]
        )

    return output


def panchanga_str(panch=Panchanga()):
    str = ""
    str += "Panchanga\n"

    str += f"Absolute tithi: {panch.tithi()}\n"

    str += f"Karana: {panch.karana()}\n"
    str += f"Vara: {panch.vara()}\n"
    str += f"Nakshatra: {panch.moon.nakshatra()}\n"
    str += f"Yoga: {panch.yoga()}"
    return str


def draw_panchanga_circle(panch=Panchanga()):
    title, tithi, karana, vara, nakshatra, yoga = panchanga_str(panch).split("\n")

    text(xy=(60, 125), text=title, style=TextStyle(halign="left"))
    text(xy=(60, 122), text=tithi, style=TextStyle(halign="left"))
    text(xy=(60, 119), text=karana, style=TextStyle(halign="left"))
    text(xy=(60, 116), text=vara, style=TextStyle(halign="left"))
    text(xy=(60, 113), text=nakshatra, style=TextStyle(halign="left"))
    text(xy=(60, 110), text=yoga, style=TextStyle(halign="left"))


def draw_panchanga_square(panch=Panchanga()):
    title, tithi, karana, vara, nakshatra, yoga = panchanga_str(panch).split("\n")

    text(xy=(50, 166), text=title, style=TextStyle(halign="left"))
    text(xy=(50, 162), text=tithi, style=TextStyle(halign="left"))
    text(xy=(50, 159), text=karana, style=TextStyle(halign="left"))
    text(xy=(50, 156), text=vara, style=TextStyle(halign="left"))
    text(xy=(50, 153), text=nakshatra, style=TextStyle(halign="left"))
    text(xy=(50, 150), text=yoga, style=TextStyle(halign="left"))


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
