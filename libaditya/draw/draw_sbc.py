#    This file is part of libaditya.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
#
#    libaditya is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    libaditya is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with libaditya.  If not, see <https://www.gnu.org/licenses/>.

from dataclasses import replace

from libaditya import constants as const

from libaditya.objects import Circle

class DrawSBC:
    """
    Mixin for drawing a sarvatobhadra chakra

    meant to be used as Rashi.draw_sbc(english_letters: bool = False, **kwargs)

    **kwargs is for any option in self.context
    meant to be used for names_type (eng,iast,deva,mixed,abbrev) or sign_names (adityas,zodiac)
    """

    def draw_sbc(self, english_letters=False):
        """
        draw this chart as an sbc in .svg format

        **kwargs is for context; you can change any option you want
        this is dangerous i guess, but it is really meant for names_type and sign_names
        for controlling how these are displayed on the chakra

        return a Drawing, d
        can be saved with, e.g., d.save_svg("this-chart.svg")

        you should probably call this like: Rashi.draw_sbc()
        """
        import drawsvg as draw
        d = draw.Drawing(500, 500)

        # from sbc.py:151: d = sc.draw_chakra(d, zodiac=zodiac, langfile=langfile, themefile=themefile)
        d = draw_chakra_base(d, self.context)

        if english_letters:
            d = draw_english_letters(d)

        # now the base is complete

        # start drawing

        # draw the rest of the chart stream of consciousness style
        # display panchangas birth panchanga
        bpanch = self.panchanga()
        birth_panchanga = bpanch.info_string()
        d.append(
            draw.Rectangle(395, 450, 70, 45, rx="1", ry="1", stroke="black", fill="yellow")
        )
        d.append(draw.Text(birth_panchanga, font_size=6, x=400, y=450))

        return d
        
# all of these where "assembled by hand"
# guess at coordinates and seeing what look good and adjusting...

# there are two set of coordinates

# the sbc has 81 boxes, so there is a coordinate system for that
# and then the coordinate system of Drawing itself, 500x500
# the origin is in the top left
# i think the 81 system works the same way
# 0-indexed in the top left, 2-tuple (column,row)
# i.e., (0,0) is the first column, first row
# and,  (7,7) is the last column, last row
# and,  (6,3) is the sixth column, third row

def make_coords(x=40, y=40):
    # each list is a column, so coords[3][4] will get the 4th column of the 5th row
    coords = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for n in range(9):
            # the logic is that i tried it and retried until it looked good and
            # seemed to work
            coords[i].append(tuple((x * (i + 2) - 4, y + (40 * (n + 1)) - 5)))
    return coords


def make_nak_coords():
    # nakshatra names have to be drawn in order
    # so these are the coordinates for the nakshatra boxes in order
    nak_coords = []
    for y in range(1, 8):
        nak_coords.append((y, 0))
    for y in range(1, 8):
        nak_coords.append((8, y))
    for y in range(1, 8).__reversed__():
        nak_coords.append((y, 8))
    for y in range(1, 8).__reversed__():
        nak_coords.append((0, y))
    return nak_coords


# diagonals will be purple, here are their sbc coordinates
diag_coords = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (8, 8),
    (7, 7),
    (6, 6),
    (5, 5),
    (8, 0),
    (7, 1),
    (6, 2),
    (5, 3),
    (0, 8),
    (1, 7),
    (2, 6),
    (3, 5),
]
# the outer most square of 20 letters
outer_letters_coords = [
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 2),
    (7, 3),
    (7, 4),
    (7, 5),
    (7, 6),
    (6, 7),
    (5, 7),
    (4, 7),
    (3, 7),
    (2, 7),
    (1, 6),
    (1, 5),
    (1, 4),
    (1, 3),
    (1, 2),
]
# rashis
rashis_coords = [
    (3, 2),
    (4, 2),
    (5, 2),
    (6, 3),
    (6, 4),
    (6, 5),
    (5, 6),
    (4, 6),
    (3, 6),
    (2, 5),
    (2, 4),
    (2, 3),
]
# four tithis
tithi_coords = [(4, 3), (5, 4), (4, 5), (3, 4)]
# nakshatra coordinates, in the proper order
nak_coords = make_nak_coords()


def get_colors(file=const.sbc_default_theme):
    input = open(file, "r")
    for line in input:
        if not "=" in line:
            continue
        field, value = line.split("=")
        field = field.strip()
        value = value.strip()
        if field.startswith("na"):
            nak_color = value
        if field.startswith("ti"):
            vals = value.split(
                ","
            )  # if two values given, the second is for purna tithi
            if len(vals) == 3:
                tithi_color = vals[0].strip()
                purna_color = vals[1].strip()
                purna_text_color = vals[2].strip()
            elif len(vals) == 2:
                tithi_color = vals[0].strip()
                purna_color = vals[1].strip()
            else:
                tithi_color = "red"
                purna_color = "black"
                purna_text_color = "white"
        if field.startswith("ra"):
            rashi_color = value
        if field.startswith("ou"):
            outer_letters_color = value
        if field.startswith("di"):
            diagonal_color = value
        if field.startswith("ci"):
            circle_color = value
    return [
        nak_color,
        tithi_color,
        purna_color,
        purna_text_color,
        rashi_color,
        outer_letters_color,
        diagonal_color,
        circle_color,
    ]


# pass in the drawsvg.drawing.Drawing object; return it too
def draw_chakra_base(d, context, themefile=const.sbc_default_theme):
    import drawsvg as draw
    (
        nak_color,
        tithi_color,
        purna_color,
        purna_text_color,
        rashi_color,
        outer_letters_color,
        diagonal_color,
        circle_color,
    ) = get_colors(themefile)

    # draw a black rectangle for a background
    d.append(draw.Rectangle(0, 0, 500, 500, rx=None, ry=None, fill="rgb(0,0,0)"))

    if circle_color.startswith("va"):  # varied, make circle art
        d.append(draw.Circle(250, 250, 250, fill="yellow"))
        d.append(draw.Circle(250, 250, 245, fill="black"))
        d.append(draw.Circle(250, 250, 240, fill="yellow"))
        d.append(draw.Circle(250, 250, 225, fill="blue"))
        d.append(draw.Circle(250, 250, 215.5, fill="forestgreen"))
        d.append(draw.Circle(250, 250, 209.25, fill="blue"))
        d.append(draw.Circle(250, 250, 200, fill="yellow"))
        d.append(draw.Circle(250, 250, 175, fill="red"))
        d.append(draw.Circle(250, 250, 150, fill="yellow"))
        d.append(draw.Circle(250, 250, 125, fill="#6b00ff"))
        d.append(draw.Circle(250, 250, 100, fill="yellow"))
        d.append(draw.Circle(250, 250, 75, fill="black"))
        d.append(draw.Circle(250, 250, 50, fill="yellow"))
    else:
        d.append(draw.Circle(250, 250, 250, fill=circle_color))

    # makes coordinate system that that
    # coords[c][r] gives the coordinates for the square in the
    # cth column and rth row
    coords = make_coords()

    # coloring the boxes

    # draw the 81 squares of the chakra
    for i in range(9):
        for n in range(9):
            if (i, n) in diag_coords:
                d.append(
                    draw.Rectangle(
                        coords[i][n][0],
                        coords[i][n][1],
                        30,
                        30,
                        rx="1",
                        ry="1",
                        stroke="black",
                        fill=diagonal_color,
                    )
                )
            elif (i, n) in outer_letters_coords:
                d.append(
                    draw.Rectangle(
                        coords[i][n][0],
                        coords[i][n][1],
                        30,
                        30,
                        rx="1",
                        ry="1",
                        stroke="black",
                        fill=outer_letters_color,
                    )
                )
            elif (i, n) in nak_coords:
                d.append(
                    draw.Rectangle(
                        coords[i][n][0],
                        coords[i][n][1],
                        30,
                        30,
                        rx="1",
                        ry="1",
                        stroke="black",
                        fill=nak_color,
                    )
                )  # #9980ff
            elif (i, n) in rashis_coords:
                d.append(
                    draw.Rectangle(
                        coords[i][n][0],
                        coords[i][n][1],
                        30,
                        30,
                        rx="1",
                        ry="1",
                        stroke="black",
                        fill=rashi_color,
                    )
                )
            elif (i, n) in tithi_coords:
                d.append(
                    draw.Rectangle(
                        coords[i][n][0],
                        coords[i][n][1],
                        30,
                        30,
                        rx="1",
                        ry="1",
                        stroke="black",
                        fill=tithi_color,
                    )
                )
            elif (i, n) == (4, 4):
                d.append(
                    draw.Rectangle(
                        coords[i][n][0],
                        coords[i][n][1],
                        30,
                        30,
                        rx="1",
                        ry="1",
                        stroke="black",
                        fill=purna_color,
                    )
                )
            else:
                d.append(
                    draw.Rectangle(
                        coords[i][n][0],
                        coords[i][n][1],
                        30,
                        30,
                        rx="1",
                        ry="1",
                        stroke="black",
                        fill="yellow",
                    )
                )

    # initalize all the names to write
    planets, nakshatras, tithis, karanas, varas, yogas, adityas, zodiac, abhijit = [const.names[context.names_type][x] for x in const.names[context.names_type]]
    # "nakshatraeq" is what I called 28 equal nakshatras with Abhijit at index 19
    nakshatraeq = nakshatras.copy()
    nakshatraeq.insert(19,abhijit)

    # draw names of nakshatras {{{1 }}}
    # init names
    # nnames = init_sbc_nakshatra_names()
    nak = 0  # 0 is krittika, and so on

    for n in range(28):
        thiscol = nak_coords[n][0]
        thisrow = nak_coords[n][1]
        d.append(
            draw.Text(
                nakshatraeq[n],
                font_size=5,
                x=coords[thiscol][thisrow][0] + 5,
                y=coords[thiscol][thisrow][1] + 25,
            )
        )

    # draw sanskrit letters {{{1

    ## outermost; a,A,i,I {{{2
    d.append(
        draw.Text("अ", font_size=20, x=coords[0][0][0] + 5, y=coords[0][0][1] + 22)
    )
    d.append(
        draw.Text("आ", font_size=20, x=coords[8][0][0] + 3, y=coords[8][0][1] + 22)
    )
    d.append(
        draw.Text("इ", font_size=20, x=coords[8][8][0] + 8, y=coords[8][8][1] + 22)
    )
    d.append(
        draw.Text("ई", font_size=20, x=coords[0][8][0] + 8, y=coords[0][8][1] + 24)
    )

    ## inner square of 28 letters {{{2
    letters = [
        "उ",
        "अ",
        "व",
        "क",
        "ह",
        "ड",
        "ऊ",
        "म",
        "ट",
        "प",
        "र",
        "त",
        "ऋ",
        "न",
        "य",
        "भ",
        "ज",
        "ख",
        "ॠ",
        "ग",
        "स",
        "द",
        "च",
        "ल",
    ]
    # let = "letter" in letters
    let = 0

    ## first seven{{{3
    for y in range(1, 8):
        # first column is coords[0][1],coords[0][2], etc. for the 2-8 boxes in the
        # coords[y][x] is a tuple (a,b), so need to do coords[col][row][a]
        # first row
        d.append(
            draw.Text(
                letters[let],
                font_size=20,
                x=coords[y][1][0] + 8,
                y=coords[y][1][1] + 22,
            )
        )
        let += 1

    ## second seven, along the side
    for y in range(2, 8):
        d.append(
            draw.Text(
                letters[let],
                font_size=20,
                x=coords[7][y][0] + 8,
                y=coords[7][y][1] + 22,
            )
        )
        let += 1

    ## third seven, along the bottom, need to count backwards this time
    for y in range(1, 7).__reversed__():
        d.append(
            draw.Text(
                letters[let],
                font_size=20,
                x=coords[y][7][0] + 8,
                y=coords[y][7][1] + 22,
            )
        )
        let += 1

    ## fourth seven, along the left, need to count backwards this time
    for y in range(2, 7).__reversed__():
        d.append(
            draw.Text(
                letters[let],
                font_size=20,
                x=coords[1][y][0] + 8,
                y=coords[1][y][1] + 22,
            )
        )
        let += 1

    ## middle square of four letters; lR,lRR,e,ai {{{2
    d.append(
        draw.Text("ऌ", font_size=20, x=coords[2][2][0] + 7, y=coords[2][2][1] + 22)
    )
    d.append(
        draw.Text("ॡ", font_size=20, x=coords[6][2][0] + 7, y=coords[6][2][1] + 22)
    )
    d.append(
        draw.Text("ए", font_size=20, x=coords[6][6][0] + 8, y=coords[6][6][1] + 21)
    )
    d.append(
        draw.Text("ऐ", font_size=20, x=coords[2][6][0] + 8, y=coords[2][6][1] + 23)
    )

    ## inner square of four letters; o,au,aM,aH {{{2
    d.append(
        draw.Text("ओ", font_size=20, x=coords[3][3][0] + 5, y=coords[3][3][1] + 22)
    )
    d.append(
        draw.Text("औ", font_size=20, x=coords[5][3][0] + 3, y=coords[5][3][1] + 22)
    )
    d.append(
        draw.Text("अं", font_size=20, x=coords[5][5][0] + 8, y=coords[5][5][1] + 22)
    )
    d.append(
        draw.Text("अः", font_size=20, x=coords[3][5][0] + 5, y=coords[3][5][1] + 24)
    )

    # draw aditya names {{{1
    # adityas = init_sbc_aditya_names()
    adit_coords = [
        (3, 2),
        (4, 2),
        (5, 2),
        (6, 3),
        (6, 4),
        (6, 5),
        (5, 6),
        (4, 6),
        (3, 6),
        (2, 5),
        (2, 4),
        (2, 3),
    ]

    # decide which names to use, adityas or zodiac
    if context.sign_names == "adityas":
        sign_names = adityas
    if context.sign_names == "zodiac":
        sign_names = zodiac

    for n in range(12):
        thisx = adit_coords[n][0]
        thisy = adit_coords[n][1]
        d.append(
            draw.Text(
                sign_names[n],
                font_size=5,
                x=coords[thisx][thisy][0] + 5,
                y=coords[thisx][thisy][1] + 25,
            )
        )

        # draw tithi names and vara names {{{1
        # nanda, ravivara, mangalavara
        d.append(
            draw.Text(
                tithis[0], font_size=5, x=coords[4][3][0] + 9, y=coords[4][3][1] + 5
            )
        )
        d.append(
            draw.Text(
                varas[0], font_size=5, x=coords[4][3][0] + 7, y=coords[4][3][1] + 20
            )
        )
        d.append(
            draw.Text(
                varas[2], font_size=5, x=coords[4][3][0] + 3, y=coords[4][3][1] + 25
            )
        )
        # bhadra, somavara, budhavara
        d.append(
            draw.Text(
                tithis[1], font_size=5, x=coords[5][4][0] + 8, y=coords[5][4][1] + 5
            )
        )
        d.append(
            draw.Text(
                varas[1], font_size=5, x=coords[5][4][0] + 6, y=coords[5][4][1] + 20
            )
        )
        d.append(
            draw.Text(
                varas[3], font_size=5, x=coords[5][4][0] + 5, y=coords[5][4][1] + 25
            )
        )
        # jaya, guruvara
        d.append(
            draw.Text(
                tithis[2], font_size=5, x=coords[4][5][0] + 11, y=coords[4][5][1] + 5
            )
        )
        d.append(
            draw.Text(
                varas[4], font_size=5, x=coords[4][5][0] + 7, y=coords[4][5][1] + 25
            )
        )
        # rikta, shukravara
        d.append(
            draw.Text(
                tithis[3], font_size=5, x=coords[3][4][0] + 11, y=coords[3][4][1] + 5
            )
        )
        d.append(
            draw.Text(
                varas[5], font_size=5, x=coords[3][4][0] + 6, y=coords[3][4][1] + 25
            )
        )
        # purna, shanivara
        d.append(
            draw.Text(
                tithis[4],
                font_size=5,
                x=coords[4][4][0] + 9,
                y=coords[4][4][1] + 5,
                fill=purna_text_color,
            )
        )
        d.append(
            draw.Text(
                varas[6],
                font_size=5,
                x=coords[4][4][0] + 7,
                y=coords[4][4][1] + 25,
                fill=purna_text_color,
            )
        )
    # }}}
    return d

def draw_english_letters(d):
    """draw english letter equivalents on the sanskrit letter boxes"""
    import drawsvg as draw

    coords = make_coords()

    d.append(draw.Text("a", font_size=5, x=coords[0][0][0] + 2, y=coords[0][0][1] + 28))
    d.append(draw.Text("A", font_size=5, x=coords[8][0][0] + 2, y=coords[8][0][1] + 28))
    d.append(draw.Text("i", font_size=5, x=coords[8][8][0] + 2, y=coords[8][8][1] + 28))
    d.append(draw.Text("I", font_size=5, x=coords[0][8][0] + 2, y=coords[0][8][1] + 28))
    eng_letters = [
        "u",
        "a",
        "va",
        "ka",
        "ha",
        "Da",
        "U",
        "m",
        "Ta",
        "pa",
        "ra",
        "ta",
        "R",
        "na",
        "ya",
        "bha",
        "ja",
        "kha",
        "RR",
        "ga",
        "sa",
        "da",
        "ca",
        "la",
    ]
    elet = 0
    for y in range(1, 8):
        d.append(
            draw.Text(
                eng_letters[elet],
                font_size=5,
                x=coords[y][1][0] + 2,
                y=coords[y][1][1] + 28,
            )
        )
        elet += 1
    for y in range(2, 8):
        d.append(
            draw.Text(
                eng_letters[elet],
                font_size=5,
                x=coords[7][y][0] + 2,
                y=coords[7][y][1] + 28,
            )
        )
        elet += 1
    for y in range(1, 7).__reversed__():
        d.append(
            draw.Text(
                eng_letters[elet],
                font_size=5,
                x=coords[y][7][0] + 2,
                y=coords[y][7][1] + 28,
            )
        )
        elet += 1
    for y in range(2, 7).__reversed__():
        d.append(
            draw.Text(
                eng_letters[elet],
                font_size=5,
                x=coords[1][y][0] + 2,
                y=coords[1][y][1] + 28,
            )
        )
        elet += 1
    d.append(
        draw.Text("lR", font_size=5, x=coords[2][2][0] + 2, y=coords[2][2][1] + 28)
    )
    d.append(
        draw.Text("lRR", font_size=5, x=coords[6][2][0] + 2, y=coords[6][2][1] + 28)
    )
    d.append(draw.Text("e", font_size=5, x=coords[6][6][0] + 2, y=coords[6][6][1] + 28))
    d.append(
        draw.Text("ai", font_size=5, x=coords[2][6][0] + 2, y=coords[2][6][1] + 28)
    )

    d.append(draw.Text("o", font_size=5, x=coords[3][3][0] + 2, y=coords[3][3][1] + 28))
    d.append(
        draw.Text("au", font_size=5, x=coords[5][3][0] + 2, y=coords[5][3][1] + 28)
    )
    d.append(
        draw.Text("aM", font_size=5, x=coords[5][5][0] + 2, y=coords[5][5][1] + 28)
    )
    d.append(
        draw.Text("aH", font_size=5, x=coords[3][5][0] + 2, y=coords[3][5][1] + 28)
    )
    return d
