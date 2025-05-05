from drawlib.apis import *
import math
import pyphglobals as pglob
import pyphutils as putil
import pyphprint
from pyphobjs import *
from pyphconstants import *

pglob.init_names()


def draw_chart(sysflg):
    planets = pyphprint.init_Planets()

    draw_base_chart(pglob.HELIO, "signs")
    if sysflg == pglob.HELIO:
        draw_date(planets[0].julianday)
        # draw_table(pyphprint.planets_str(planets[0].julianday, sysflg))
        draw_heliocentric_planets(planets)

    save()


def draw_base_chart(ctype, signs):
    config(width=100, height=200, grid_only=True)
    # used typst to make a circle with 12 lines, angles of 30 degrees
    if ctype == pglob.HELIO:
        draw_heliocentric()
    if ctype == pglob.BARY:
        draw_barycentric()

    # outer edge of the wheel
    donuts(xy=(50, 50), radius=40, width=4)

    if signs == "signs":
        draw_signs()
    if signs == "adityas":
        draw_adityas()


def draw_date(jd=JulianDay()):
    txt = f"{jd}"
    utc, usr, julian = txt.split("\n")
    text(xy=(2, 197), text=utc, style=TextStyle(halign="left"))
    text(xy=(2, 194), text=usr, style=TextStyle(halign="left"))
    text(xy=(2, 191), text=julian, style=TextStyle(halign="left"))


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


def draw_heliocentric():
    image(xy=(50, 50), width=100, image="images/heliocentric.png")


def draw_barycentric():
    image(
        xy=(50, 50), width=100, image="images/barycentric.png"
    )  # for barycentric charts


def draw_signs():
    # now draw sign glyphs onto the circle
    image(xy=(88, 50), width=3, image="images/glyphs/aries.png")
    image(xy=(82.5, 70), width=3, image="images/glyphs/taurus.png")
    image(xy=(69, 83), width=3, image="images/glyphs/gemini.png")
    image(xy=(50, 88), width=3, image="images/glyphs/cancer.png")
    image(xy=(31, 83), width=3, image="images/glyphs/leo.png")
    image(xy=(17.5, 70), width=3, image="images/glyphs/virgo.png")
    image(xy=(12, 50), width=3, image="images/glyphs/libra.png")
    image(xy=(17.5, 30), width=3, image="images/glyphs/scorpio.png")
    image(xy=(31, 17), width=3, image="images/glyphs/sagittarius.png")
    image(xy=(50, 12), width=3, image="images/glyphs/capricorn.png")
    image(xy=(69, 17), width=3, image="images/glyphs/aquarius.png")
    image(xy=(82.5, 30), width=3, image="images/glyphs/pisces.png")


def draw_adityas():
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


draw_chart(pglob.HELIO)
