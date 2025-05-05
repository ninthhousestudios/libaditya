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
