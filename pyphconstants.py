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

hb_aries_coords = [
    (82, 50),
    (82, 55),
    (76, 47),
    (70, 53),
    (70, 47),
    (82, 45),
    (76, 53),
    (63, 50),
]

hb_taurus_coords = [
    (77, 66),
    (75, 70),
    (80, 63),
    (70, 66),
    (75, 60),
    (66, 62),
    (70, 58),
    (60, 56),
]

hb_gemini_coords = [
    (66, 77),
    (63, 80),
    (69, 75),
    (60, 73),
    (65, 70),
    (57, 67),
    (60, 63),
    (55, 60),
]

hb_cancer_coords = [
    (50, 80),
    (55, 82),
    (45, 82),
    (53, 76),
    (47, 76),
    (53, 70),
    (47, 70),
    (50, 63),
]

hb_leo_coords = [
    (34, 77),
    (37, 80),
    (31, 75),
    (40, 73),
    (35, 70),
    (43, 67),
    (40, 63),
    (45, 60),
]

hb_virgo_coords = [
    (23, 66),
    (25, 70),
    (20, 63),
    (30, 66),
    (25, 60),
    (34, 62),
    (30, 58),
    (40, 56),
]

hb_libra_coords = [
    (18, 50),
    (18, 55),
    (18, 45),
    (24, 53),
    (24, 47),
    (30, 53),
    (30, 47),
    (37, 50),
]

hb_scorpio_coords = [
    (23, 34),
    (25, 30),
    (20, 37),
    (30, 34),
    (25, 40),
    (34, 38),
    (30, 42),
    (40, 44),
]

hb_sagittarius_coords = [
    (34, 23),
    (37, 20),
    (31, 25),
    (40, 27),
    (35, 30),
    (43, 33),
    (40, 37),
    (45, 40),
]

hb_capricorn_coords = [
    (50, 20),
    (55, 18),
    (45, 18),
    (53, 24),
    (47, 24),
    (53, 30),
    (47, 30),
    (50, 37),
]

hb_aquarius_coords = [
    (66, 23),
    (70, 25),
    (63, 20),
    (66, 30),
    (60, 25),
    (62, 34),
    (58, 30),
    (56, 40),
]

hb_pisces_coords = [
    (77, 34),
    (75, 30),
    (80, 37),
    (70, 34),
    (75, 40),
    (66, 38),
    (70, 42),
    (60, 44),
]

hb_coords_list = [
    hb_aries_coords,
    hb_taurus_coords,
    hb_gemini_coords,
    hb_cancer_coords,
    hb_leo_coords,
    hb_virgo_coords,
    hb_libra_coords,
    hb_scorpio_coords,
    hb_sagittarius_coords,
    hb_capricorn_coords,
    hb_aquarius_coords,
    hb_pisces_coords,
]
pwidth = 4

cusps_numerals = [
    "Asc",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
    "X",
    "XI",
    "XII",
]

cusps_coords = [
    [(33, 76), (37, 76), (33, 79)],
    [(54, 76), (58, 76), (54, 79)],
    [(76, 76), (80, 76), (76, 79)],
    [(76, 54), (80, 54), (76, 57)],
    [(76, 32), (80, 32), (76, 35)],
    [(76, 9), (80, 9), (76, 12)],
    [(54, 9), (58, 9), (54, 12)],
    [(32, 9), (36, 9), (32, 12)],
    [(10, 9), (14, 9), (10, 12)],
    [(10, 31), (14, 31), (10, 34)],
    [(10, 53), (14, 53), (10, 56)],
    [(10, 75), (14, 75), (10, 78)],
]

geo_aries_coords = [
    (39, 83),
    (45, 90),
    (39, 90),
    (33, 83),
    (45, 83),
    (45, 76),
    (39, 76),
]

geo_taurus_coords = [
    (60, 83),
    (67, 83),
    (67, 76),
    (57, 90),
    (53, 83),
    (53, 90),
    (60, 76),
]

geo_gemini_coords = [
    (83, 83),
    (76, 90),
    (90, 76),
    (81, 90),
    (76, 83),
    (90, 83),
    (84, 76),
]

geo_cancer_coords = [
    (83, 61),
    (76, 68),
    (90, 54),
    (81, 68),
    (76, 61),
    (90, 61),
    (84, 54),
]

geo_leo_coords = [
    (83, 39),
    (76, 46),
    (90, 32),
    (81, 46),
    (76, 39),
    (90, 39),
    (84, 32),
]

geo_virgo_coords = [
    (83, 17),
    (76, 23),
    (90, 10),
    (81, 23),
    (76, 17),
    (90, 17),
    (84, 10),
]

geo_libra_coords = [
    (61, 17),
    (54, 23),
    (68, 10),
    (59, 23),
    (54, 17),
    (68, 17),
    (62, 10),
]

geo_scorpio_coords = [
    (39, 17),
    (46, 23),
    (46, 10),
    (41, 23),
    (32, 17),
    (46, 17),
    (40, 10),
]

geo_sagittarius_coords = [
    (17, 17),
    (24, 23),
    (24, 10),
    (19, 23),
    (10, 17),
    (24, 17),
    (18, 10),
]

geo_capricorn_coords = [
    (17, 39),
    (24, 45),
    (24, 32),
    (19, 45),
    (10, 39),
    (24, 39),
    (18, 32),
]

geo_aquarius_coords = [
    (17, 61),
    (24, 67),
    (24, 54),
    (19, 67),
    (10, 61),
    (24, 61),
    (18, 54),
]

geo_pisces_coords = [
    (17, 83),
    (24, 89),
    (24, 76),
    (19, 89),
    (10, 83),
    (24, 83),
    (18, 76),
]

geo_coords_list = [
    geo_aries_coords,
    geo_taurus_coords,
    geo_gemini_coords,
    geo_cancer_coords,
    geo_leo_coords,
    geo_virgo_coords,
    geo_libra_coords,
    geo_scorpio_coords,
    geo_sagittarius_coords,
    geo_capricorn_coords,
    geo_aquarius_coords,
    geo_pisces_coords,
]


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


def draw_aditya_chart_lines():
    line(xy1=(50, 89), xy2=(50, 78))
    line(xy1=(50, 22), xy2=(50, 10))
    line(xy1=(11, 50), xy2=(22, 50))
    line(xy1=(78, 50), xy2=(89, 50))


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
    pwidth = 3
    image(xy=(31, 91), width=pwidth, image=image_dir + "glyphs/aries.png")
    image(xy=(69, 91), width=pwidth, image=image_dir + "glyphs/taurus.png")
    image(xy=(90, 91), width=pwidth, image=image_dir + "glyphs/gemini.png")
    image(xy=(90, 69), width=pwidth, image=image_dir + "glyphs/cancer.png")
    image(xy=(90, 47), width=pwidth, image=image_dir + "glyphs/leo.png")
    image(xy=(90, 23), width=pwidth, image=image_dir + "glyphs/virgo.png")
    image(xy=(70, 23), width=pwidth, image=image_dir + "glyphs/libra.png")
    image(xy=(31, 23), width=pwidth, image=image_dir + "glyphs/scorpio.png")
    image(xy=(10, 23), width=pwidth, image=image_dir + "glyphs/sagittarius.png")
    image(xy=(10, 46), width=pwidth, image=image_dir + "glyphs/capricorn.png")
    image(xy=(10, 69), width=pwidth, image=image_dir + "glyphs/aquarius.png")
    image(xy=(10, 91), width=pwidth, image=image_dir + "glyphs/pisces.png")


def draw_adityas_square():
    text(xy=(33, 91), text=pglob.adityas[11])
    text(xy=(65, 91), text=pglob.adityas[0])
    text(xy=(88, 91), text=pglob.adityas[1])
    text(xy=(88, 69), text=pglob.adityas[2])
    text(xy=(88, 47), text=pglob.adityas[3])
    text(xy=(88, 24), text=pglob.adityas[4])
    text(xy=(66, 24), text=pglob.adityas[5])
    text(xy=(33, 24), text=pglob.adityas[6])
    text(xy=(12, 24), text=pglob.adityas[7])
    text(xy=(12, 46), text=pglob.adityas[8])
    text(xy=(12, 68), text=pglob.adityas[9])
    text(xy=(12, 91), text=pglob.adityas[10])
