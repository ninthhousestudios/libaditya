from drawlib.apis import *
import math
import pyphglobals as pglob
import pyphprint


def draw_chart():
    draw_base_chart()
    draw_planets()
    save()


def draw_base_chart():
    config(width=100, height=100, grid_only=True)
    # used typst to make a circle with 12 lines, angles of 30 degrees
    draw_heliocentric()
    # draw_barycentric()
    # outer edge of the wheel
    donuts(xy=(50, 50), radius=40, width=4)
    draw_signs()
    pglob.init_names()
    draw_adityas()


planet_glyphs = [
    "images/glyphs/sun.png",
    "images/glyphs/moon.png",
    "images/glyphs/mercury.png",
    "images/glyphs/venus.png",
    "images/glyphs/mars.png",
    "images/glyphs/jupiter.png",
    "images/glyphs/saturn.png",
    "images/glyphs/uranus.png",
    "images/glyphs/neptune.png",
    "images/glyphs/pluto.png",
    "images/glyphs/rahu.png",
    "images/glyphs/ketu.png",
    "images/glyphs/earth.png",
]

# these are coordinates for where to draw planets
# where to draw the planet obviously depends on the sign,
# but then also how many planets are in the sign
# so the arrays will contain a list of tuples
# that contain the coordinates of successive planets

aries_coords = [
    (82, 55),
    (82, 45),
    (76, 53),
    (76, 47),
    (70, 53),
    (70, 47),
    (63, 50),
]

cancer_coords = [
    (55, 82),
    (45, 82),
    (53, 76),
    (47, 76),
    (53, 70),
    (47, 70),
    (50, 63),
]

libra_coords = [
    (18, 55),
    (18, 45),
    (24, 53),
    (24, 47),
    (30, 53),
    (30, 47),
    (37, 50),
]

capricorn_coords = [
    (55, 18),
    (45, 18),
    (53, 24),
    (47, 24),
    (53, 30),
    (47, 30),
    (50, 37),
]


def draw_planets():
    planets = pyphprint.init_Planets()


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


draw_chart()
