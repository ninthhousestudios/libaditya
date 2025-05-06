from drawlib.apis import *
import pyphglobals as pglob

image_dir = "/home/josh/w/astro/soft/pyphemeris/images/"

planet_glyphs = [
    image_dir + "glyphs/sun.png",
    image_dir + "glyphs/moon.png",
    image_dir + "glyphs/mercury.png",
    image_dir + "glyphs/venus.png",
    image_dir + "glyphs/mars.png",
    image_dir + "glyphs/jupiter.png",
    image_dir + "glyphs/saturn.png",
    image_dir + "glyphs/uranus.png",
    image_dir + "glyphs/neptune.png",
    image_dir + "glyphs/pluto.png",
    image_dir + "glyphs/rahu.png",
    image_dir + "glyphs/ketu.png",
    image_dir + "glyphs/earth.png",
]

# these are coordinates for where to draw planets
# where to draw the planet obviously depends on the sign,
# but then also how many planets are in the sign
# so the arrays will contain a list of tuples
# that contain the coordinates of successive planets

aries_coords = [
    (82, 50),
    (82, 55),
    (82, 45),
    (76, 53),
    (76, 47),
    (70, 53),
    (70, 47),
    (63, 50),
]

taurus_coords = [
    (77, 66),
    (75, 70),
    (80, 63),
    (70, 66),
    (75, 60),
    (66, 62),
    (70, 58),
    (60, 56),
]

gemini_coords = [
    (66, 77),
    (63, 80),
    (69, 75),
    (60, 73),
    (65, 70),
    (57, 67),
    (60, 63),
    (55, 60),
]

cancer_coords = [
    (50, 80),
    (55, 82),
    (45, 82),
    (53, 76),
    (47, 76),
    (53, 70),
    (47, 70),
    (50, 63),
]

leo_coords = [
    (34, 77),
    (37, 80),
    (31, 75),
    (40, 73),
    (35, 70),
    (43, 67),
    (40, 63),
    (45, 60),
]

virgo_coords = [
    (23, 66),
    (25, 70),
    (20, 63),
    (30, 66),
    (25, 60),
    (34, 62),
    (30, 58),
    (40, 56),
]

libra_coords = [
    (18, 50),
    (18, 55),
    (18, 45),
    (24, 53),
    (24, 47),
    (30, 53),
    (30, 47),
    (37, 50),
]

scorpio_coords = [
    (23, 34),
    (25, 30),
    (20, 37),
    (30, 34),
    (25, 40),
    (34, 38),
    (30, 42),
    (40, 44),
]

sagittarius_coords = [
    (34, 23),
    (37, 20),
    (31, 25),
    (40, 27),
    (35, 30),
    (43, 33),
    (40, 37),
    (45, 40),
]

capricorn_coords = [
    (50, 20),
    (55, 18),
    (45, 18),
    (53, 24),
    (47, 24),
    (53, 30),
    (47, 30),
    (50, 37),
]

aquarius_coords = [
    (66, 23),
    (70, 25),
    (63, 20),
    (66, 30),
    (60, 25),
    (62, 34),
    (58, 30),
    (56, 40),
]

pisces_coords = [
    (77, 34),
    (75, 30),
    (80, 37),
    (70, 34),
    (75, 40),
    (66, 38),
    (70, 42),
    (60, 44),
]

coords_list = [
    aries_coords,
    taurus_coords,
    gemini_coords,
    cancer_coords,
    leo_coords,
    virgo_coords,
    libra_coords,
    scorpio_coords,
    sagittarius_coords,
    capricorn_coords,
    aquarius_coords,
    pisces_coords,
]
pwidth = 4


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
