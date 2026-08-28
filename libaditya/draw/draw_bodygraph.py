# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC

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

import drawsvg as draw

from libaditya import constants as const
from libaditya.hd import constants as hdc


class DrawBodyGraph:
    """
    Mixin that inherits unto charts.bodygraph.Bodygraph in order to drawsvg this bodygraph
    """

    def draw_svg(self, theme_file=hdc.default_theme, outfile=None):
        """
        output a .svg of this bodygraph

        default outfile is name associated with the chart, all lowercase, spaces replaced with "-"
        if there is no name and outfile=None, then it uses the julianday number as the file name
        """
        d = draw.Drawing(500, 500)
        # initialize the theme from the theme_file
        theme = const.init_theme(theme_file)
        theme["gates"] = self.gates_theme(theme["gates"])
        theme = self.get_defined_centers(theme, self.activated_gates())
        d = self.draw_bodygraph(
            d,
            theme,
            self.conscious_planets().gates(),
            self.unconscious_planets().gates(),
            self.context.get_info_str_hd(),
            self.unconscious_planets().context.get_info_str_hd(),
        )
        # display to the correct output file
        d.set_pixel_scale(1)
        if outfile == None:
            name = self.context.name.lower().replace(" ", "-")
            if not name:
                # if name is empty, use julian day number
                name = f"{self.context.timeJD.jd_number()}"
            foutname = f"{name}.svg"
        else:
            foutname = outfile
        d.save_svg(foutname)
        d

    def get_defined_centers(self, theme, gates):
        """
        recolor the theme so every UNDEFINED center takes theme["undefined"]

        the center-definition calc itself lives in hd.definition (shared with
        Bodygraph.defined_centers); this only applies its verdict to the theme,
        leaving a defined center's own color untouched.  ``gates`` is whatever
        Bodygraph.activated_gates() hands over (integer gate numbers).
        """
        from libaditya.hd import definition as hddef

        for center, is_defined in hddef.defined_centers(gates).items():
            if not is_defined:
                theme[center] = theme["undefined"]

        return theme

    # centers are always taken care of in this order
    # head
    # ajna
    # throat
    # ji
    # sacral
    # root
    # spleen
    # solar
    # will
    def draw_bodygraph(self, d, theme, cgates, ugates, rstr, lstr):

        d.append(
            draw.Rectangle(0, 0, 500, 500, rx=None, ry=None, fill=theme["background"])
        )

        # draw the channels
        # technically, draw the half-channel for each gate that is defined
        d = self.draw_channels(d, theme, cgates, ugates)

        # draw the centers and color them according to defined or undefined
        d = self.draw_centers(d, theme)

        # theme["gates"] is 0 for numbers, 1 for hexagrams
        # corresponding to the proper index of the gate tuple
        # in the hdc.gates dictionary
        # this draws the gate numbers/hexagrams in the centers
        d = self.draw_gates(d, theme, cgates + ugates)

        # draw the gate information on the sides of the bodygraph
        d = self.draw_gate_boxes(d, theme, cgates, ugates)

        # info boxes mean the name and birth or time/date information
        d = self.draw_info_boxes(d, theme, rstr, lstr)

        return d

    def draw_centers(self, d, theme):
        # draw head center
        head = draw.Lines(
            210,
            50,
            250,
            10,
            290,
            50,
            210,
            50,
            stroke=theme["lines"],
            fill=theme["head"],
        )
        d.append(head)

        # draw ajna center
        ajna = draw.Lines(
            210,
            70,
            250,
            120,
            290,
            70,
            210,
            70,
            stroke=theme["lines"],
            fill=theme["ajna"],
        )
        d.append(ajna)

        # draw throat center
        throat = draw.Rectangle(
            220, 140, 60, 60, rx=5, stroke=theme["lines"], fill=theme["throat"]
        )
        d.append(throat)

        # draw ji center
        ji = draw.Rectangle(
            220,
            210,
            60,
            60,
            rx=5,
            stroke=theme["lines"],
            transform="rotate(45,230,250)",
            fill=theme["ji"],
        )
        d.append(ji)

        # draw sacral center
        sacral = draw.Rectangle(
            220, 330, 60, 60, rx=5, stroke=theme["lines"], fill=theme["sacral"]
        )
        d.append(sacral)

        # draw root center
        root = draw.Rectangle(
            220, 420, 60, 60, rx=5, stroke=theme["lines"], fill=theme["root"]
        )
        d.append(root)

        # draw spleen center
        spleen = draw.Lines(
            100,
            400,
            100,
            330,
            170,
            365,
            100,
            400,
            stroke=theme["lines"],
            fill=theme["spleen"],
        )
        d.append(spleen)

        # draw solar center
        solar = draw.Lines(
            400,
            400,
            400,
            330,
            330,
            370,
            400,
            400,
            stroke=theme["lines"],
            fill=theme["solar"],
        )
        d.append(solar)

        # draw will center
        will = draw.Lines(
            295,
            300,
            315,
            255,
            360,
            290,
            295,
            300,
            stroke=theme["lines"],
            fill=theme["will"],
        )
        d.append(will)

        return d

    def draw_gates(self, d, theme, gates):

        gtype = theme["gates"]
        gx = 2
        gy = 3

        # for drawing circles around defined gates
        # gates=[int(x) for x in gates]

        # make an x-coordinate offset for when printing gates as hexagrams
        xoff = 0
        if gtype == 1:
            xoff = 2

        for i in range(1, 65):
            d.append(
                draw.Text(
                    hdc.gates[i][gtype],
                    x=xoff + hdc.gates[i][gx],
                    y=hdc.gates[i][gy],
                    font_size=10,
                )
            )
            # for drawing circles around defined gates, but i dont like how it looks
            # if i in gates:
            # d.append(draw.Circle(xoff+hdc.gates[i][gx]+6,hdc.gates[i][gy]-3,6,stroke="black",fill="none"))

        return d

    def gates_theme(self, argsgates):
        # choose how gates will be displayed on the bodygraph and sides
        # 0 and 1 are the indexes for pconst.gates which hold
        # a string representation of the number and the hexgram respectively
        gatestheme = 0
        if argsgates:
            if argsgates == "numbers":
                gatestheme = 0
            elif argsgates == "hexagrams":
                gatestheme = 1
            else:  # wrong argument or a type, use numbers
                print(
                    f"argument was given but not recognized; check spelling; using numbers for gates"
                )
                gatestheme = 0
        else:
            if gatestheme == "numbers":
                gatestheme = 0
            if gatestheme == "hexagrams":
                gatestheme = 1
        return gatestheme

    def draw_channels(self, d, theme, cgates, ugates):
        """
        each gate draws into own half of the channel
        they meet in the middle

        if an gate is both unconscious and conscious
        draw the unconscious first, then draw the conscious one
        with stroke_dasharray='5,9'), which will cause it to have
        dashes in both collors, like this:
        d.append(draw.Line(140,350,300,297, stroke="orange", stroke_width=5, stroke_dasharray='5,9'))

        if just one is defined, draw the whole channel with that color
        """

        # since some channels need to be drawn below others
        # this list is that order; that is why it is not done with
        # a simple range() loop
        gs = [
            57,
            10,
            34,
            44,
            26,
            12,
            22,
            35,
            36,
            21,
            45,
            51,
            25,
            20,
            40,
            37,
            59,
            6,
            27,
            50,
            48,
            16,
            58,
            18,
            38,
            28,
            54,
            32,
            41,
            30,
            39,
            55,
            19,
            49,
            64,
            47,
            61,
            24,
            63,
            4,
            17,
            62,
            11,
            56,
            43,
            23,
            31,
            7,
            1,
            8,
            33,
            13,
            15,
            5,
            46,
            29,
            2,
            14,
            42,
            53,
            3,
            60,
            9,
            52,
        ]

        # take out the chiron gate, since we print it, but it does not acutally activate a gate
        if len(cgates) == 14:
            cgates = cgates[:13]
        if len(ugates) == 14:
            ugates = ugates[:13]
        if len(cgates) == 28:
            cgates = cgates[:13] + cgates[14:27]
        if len(ugates) == 28:
            ugates = ugates[:13] + ugates[14:27]

        # indexes of coordinates in hdc.gates
        csx = 4
        csy = 5
        cex = 6
        cey = 7

        # cgates and ugates contain a float, gate.line, so get rid of the line number
        cgates = [int(x) for x in cgates]
        ugates = [int(x) for x in ugates]

        # for channels between 57,34,10,20
        # need to do some manual drawing
        for g in gs:
            if g in cgates and g in ugates:
                d.append(
                    draw.Line(
                        hdc.gates[g][csx],
                        hdc.gates[g][csy],
                        hdc.gates[g][cex],
                        hdc.gates[g][cey],
                        stroke=theme["unconscious"],
                        stroke_width=5,
                    )
                )
                d.append(
                    draw.Line(
                        hdc.gates[g][csx],
                        hdc.gates[g][csy],
                        hdc.gates[g][cex],
                        hdc.gates[g][cey],
                        stroke=theme["conscious"],
                        stroke_width=5,
                        stroke_dasharray="2,2",
                    )
                )
                if g == 34:
                    # draw extra line towards
                    if 20 in cgates or 20 in ugates:
                        d.append(
                            draw.Line(
                                140,
                                311,
                                180,
                                230,
                                stroke=theme["unconscious"],
                                stroke_width=5,
                            )
                        )
                        d.append(
                            draw.Line(
                                140,
                                311,
                                180,
                                230,
                                stroke=theme["conscious"],
                                stroke_width=5,
                                stroke_dasharray="2,2",
                            )
                        )
                    if 10 in cgates or 10 in ugates:
                        d.append(
                            draw.Line(
                                140,
                                311,
                                167,
                                258,
                                stroke=theme["unconscious"],
                                stroke_width=5,
                            )
                        )
                        d.append(
                            draw.Line(
                                140,
                                311,
                                167,
                                258,
                                stroke=theme["conscious"],
                                stroke_width=5,
                                stroke_dasharray="2,2",
                            )
                        )
                if g == 10:
                    if 20 in cgates or 20 in ugates:
                        d.append(
                            draw.Line(
                                167,
                                258,
                                180,
                                230,
                                stroke=theme["unconscious"],
                                stroke_width=5,
                            )
                        )
                        d.append(
                            draw.Line(
                                167,
                                258,
                                180,
                                230,
                                stroke=theme["conscious"],
                                stroke_width=5,
                                stroke_dasharray="2,2",
                            )
                        )
            elif g in cgates:
                d.append(
                    draw.Line(
                        hdc.gates[g][csx],
                        hdc.gates[g][csy],
                        hdc.gates[g][cex],
                        hdc.gates[g][cey],
                        stroke=theme["conscious"],
                        stroke_width=5,
                    )
                )
                if g == 34:
                    # draw extra line towards
                    if 20 in cgates or 20 in ugates:
                        d.append(
                            draw.Line(
                                140,
                                311,
                                180,
                                230,
                                stroke=theme["conscious"],
                                stroke_width=5,
                            )
                        )
                    if 10 in cgates or 10 in ugates:
                        d.append(
                            draw.Line(
                                140,
                                311,
                                167,
                                258,
                                stroke=theme["conscious"],
                                stroke_width=5,
                            )
                        )
                if g == 10:
                    if 20 in cgates or 20 in ugates:
                        d.append(
                            draw.Line(
                                167,
                                258,
                                180,
                                230,
                                stroke=theme["conscious"],
                                stroke_width=5,
                            )
                        )
            elif g in ugates:
                d.append(
                    draw.Line(
                        hdc.gates[g][csx],
                        hdc.gates[g][csy],
                        hdc.gates[g][cex],
                        hdc.gates[g][cey],
                        stroke=theme["unconscious"],
                        stroke_width=5,
                    )
                )
                if g == 34:
                    # draw extra line towards
                    if 20 in cgates or 20 in ugates:
                        d.append(
                            draw.Line(
                                140,
                                311,
                                180,
                                230,
                                stroke=theme["unconscious"],
                                stroke_width=5,
                            )
                        )
                    if 10 in cgates or 10 in ugates:
                        d.append(
                            draw.Line(
                                140,
                                311,
                                167,
                                258,
                                stroke=theme["unconscious"],
                                stroke_width=5,
                            )
                        )
                if g == 10:
                    if 20 in cgates or 20 in ugates:
                        d.append(
                            draw.Line(
                                167,
                                258,
                                180,
                                230,
                                stroke=theme["unconscious"],
                                stroke_width=5,
                            )
                        )
            else:
                d.append(
                    draw.Line(
                        hdc.gates[g][csx],
                        hdc.gates[g][csy],
                        hdc.gates[g][cex],
                        hdc.gates[g][cey],
                        stroke=theme["undefined"],
                        stroke_width=5,
                    )
                )

        return d

    def draw_gate_boxes(self, d, theme, cgates, ugates):
        cx = 450
        ux = 30
        y = 15

        if len(ugates) == 14:
            # just a bodygraph
            d.append(
                draw.Text(
                    "Personality",
                    font_size=10,
                    x=cx - 20,
                    y=8,
                    stroke=theme["right-text"],
                )
            )
            d.append(
                draw.Text("Design", font_size=10, x=ux, y=8, stroke=theme["left-text"])
            )
        elif len(ugates) == 28 and len(cgates) == 14:
            # a bodygraph and transit chart; bodygraph gates on left, transit on right
            d.append(
                draw.Text(
                    "Transit", font_size=10, x=cx - 3, y=8, stroke=theme["right-text"]
                )
            )
            d.append(
                draw.Text("D", font_size=10, x=ux + 5, y=8, stroke=theme["left-text"])
            )
            d.append(
                draw.Text("P", font_size=10, x=ux + 37, y=8, stroke=theme["left-text"])
            )
        elif len(ugates) == 28 and len(cgates) == 28:
            # this is a composite chart, so two sets of gates on each side
            d.append(
                draw.Text("D", font_size=10, x=cx, y=8, stroke=theme["right-text"])
            )
            d.append(
                draw.Text("P", font_size=10, x=cx + 30, y=8, stroke=theme["right-text"])
            )
            d.append(
                draw.Text("D", font_size=10, x=ux + 5, y=8, stroke=theme["left-text"])
            )
            d.append(
                draw.Text("P", font_size=10, x=ux + 37, y=8, stroke=theme["left-text"])
            )
        else:
            # ugates is an empty list, meaning this is a transit only chart
            d.append(
                draw.Text(
                    "Transit", font_size=10, x=cx - 3, y=8, stroke=theme["right-text"]
                )
            )

        # each element of cgates/ugates is a float gate.line
        # turn each element into a list of strings ["gate","line"]
        cgates = [str(x).split(".") for x in cgates]
        ugates = [str(x).split(".") for x in ugates]

        # gates on the right side
        if not ugates:
            # a transit only chart, so draw gates in transit color
            # transits if present are in cgates
            for n in range(0, 14):
                d.append(
                    draw.Rectangle(
                        cx,
                        y + n * 35,
                        25,
                        25,
                        rx=2,
                        stroke=theme["lines"],
                        fill=theme["transit"],
                    )
                )
                d.append(
                    draw.Text(
                        hdc.hd_glyphs[n], font_size=13, x=cx + 8, y=y + n * 35 + 12
                    )
                )
                d.append(
                    draw.Text(
                        hdc.gates[int(cgates[n][0])][theme["gates"]]
                        + "."
                        + cgates[n][1],
                        font_size=10,
                        x=cx + 4,
                        y=y + n * 35 + 22,
                    )
                )
        elif len(cgates) == 28:
            # a composite chart
            for n in range(0, 14):
                d.append(
                    draw.Rectangle(
                        cx - 10,
                        y + n * 35,
                        25,
                        25,
                        rx=2,
                        stroke=theme["lines"],
                        fill=theme["conscious"],
                    )
                )
                d.append(
                    draw.Text(
                        hdc.hd_glyphs[n], font_size=13, x=cx - 3, y=y + n * 35 + 12
                    )
                )
                d.append(
                    draw.Text(
                        hdc.gates[int(cgates[n][0])][theme["gates"]]
                        + "."
                        + cgates[n][1],
                        font_size=10,
                        x=cx - 6,
                        y=y + n * 35 + 22,
                    )
                )
            for n in range(0, 14):
                d.append(
                    draw.Rectangle(
                        cx + 20,
                        y + n * 35,
                        25,
                        25,
                        rx=2,
                        stroke=theme["lines"],
                        fill=theme["conscious"],
                    )
                )
                d.append(
                    draw.Text(
                        hdc.hd_glyphs[n], font_size=13, x=cx + 28, y=y + n * 35 + 12
                    )
                )
                d.append(
                    draw.Text(
                        hdc.gates[int(cgates[n + 14][0])][theme["gates"]]
                        + "."
                        + cgates[n + 14][1],
                        font_size=10,
                        x=cx + 24,
                        y=y + n * 35 + 22,
                    )
                )
        else:
            # just a bodygraph
            for n in range(0, 14):
                d.append(
                    draw.Rectangle(
                        cx,
                        y + n * 35,
                        25,
                        25,
                        rx=2,
                        stroke=theme["lines"],
                        fill=theme["conscious"],
                    )
                )
                d.append(
                    draw.Text(
                        hdc.hd_glyphs[n], font_size=13, x=cx + 8, y=y + n * 35 + 12
                    )
                )
                d.append(
                    draw.Text(
                        hdc.gates[int(cgates[n][0])][theme["gates"]]
                        + "."
                        + cgates[n][1],
                        font_size=10,
                        x=cx + 4,
                        y=y + n * 35 + 22,
                    )
                )

        # gates on the left side
        if len(ugates) == 14:
            # just a bodygraph
            for n in range(0, 14):
                d.append(
                    draw.Rectangle(
                        ux,
                        y + n * 35,
                        25,
                        25,
                        rx=2,
                        stroke=theme["lines"],
                        fill=theme["unconscious"],
                    )
                )
                d.append(
                    draw.Text(
                        hdc.hd_glyphs[n], font_size=13, x=ux + 8, y=y + n * 35 + 12
                    )
                )
                d.append(
                    draw.Text(
                        hdc.gates[int(ugates[n][0])][theme["gates"]]
                        + "."
                        + ugates[n][1],
                        font_size=10,
                        x=ux + 4,
                        y=y + n * 35 + 22,
                    )
                )
        elif len(ugates) == 28:
            # transits with a bodygraph, draw both sets of gates on the left
            # or a composite chart
            for n in range(0, 14):
                d.append(
                    draw.Rectangle(
                        ux,
                        y + n * 35,
                        25,
                        25,
                        rx=2,
                        stroke=theme["lines"],
                        fill=theme["unconscious"],
                    )
                )
                d.append(
                    draw.Text(
                        hdc.hd_glyphs[n], font_size=13, x=ux + 8, y=y + n * 35 + 12
                    )
                )
                d.append(
                    draw.Text(
                        hdc.gates[int(ugates[n][0])][theme["gates"]]
                        + "."
                        + ugates[n][1],
                        font_size=10,
                        x=ux + 4,
                        y=y + n * 35 + 22,
                    )
                )
            for n in range(0, 14):
                d.append(
                    draw.Rectangle(
                        ux + 30,
                        y + n * 35,
                        25,
                        25,
                        rx=2,
                        stroke=theme["lines"],
                        fill=theme["unconscious"],
                    )
                )
                d.append(
                    draw.Text(
                        hdc.hd_glyphs[n], font_size=13, x=ux + 36, y=y + n * 35 + 12
                    )
                )
                d.append(
                    draw.Text(
                        hdc.gates[int(ugates[n + 14][0])][theme["gates"]]
                        + "."
                        + ugates[n + 14][1],
                        font_size=10,
                        x=ux + 33,
                        y=y + n * 35 + 22,
                    )
                )
        else:
            # dont draw anything on the left
            n = 0

        return d

    def draw_info_boxes(self, d, theme, rstr, lstr):

        d.append(draw.Text(rstr, font_size=10, x=305, y=10, stroke=theme["right-text"]))
        d.append(draw.Text(lstr, font_size=10, x=80, y=10, stroke=theme["left-text"]))

        return d
