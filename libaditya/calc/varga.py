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

import swisseph as swe
from prettytable import PrettyTable
from dataclasses import replace

from rich.table import Table
from rich.console import Console

from libaditya import constants as const
from libaditya import utils
from libaditya import print_functions as printf

from libaditya.objects import Sign, Signs, Longitude, Planet, Planets, Cusp, Cusps, RashiBala
from libaditya.objects import planets as planet_constructors

from .jaimini import Jaimini

from .api import API

class Varga(Jaimini,API):
    """
    Varga is the main calculation interface

    important and special functions can be found or added to the API baseclass (Mixin) to Chart
    i.e., if you want to know the ayanmsa => Chart.ayanamsa()

    Chart itself does not have an ayanamsa, actually
    it returns Rashi.ayanamsa()

    this keeps the astrology interface distinct from the humandesign interace (through libaditya.hd)
    for now i have put i have put an HDContext into EphContext
    this actually makes it so that with object, an EphContext, i can calculate and text-display anything i want
    """

    def __init__(self,context,amsha=1):
        if amsha != 1:
            self.context = replace(context,amsha=amsha,print_nakshatras=False)
        else:
            self.context = replace(context,amsha=amsha)
        self._amsha = self.context.amsha
        self._planets = Planets(self.context)
        # this finds the physical cusps 
        self._cusps = Cusps(self.context)
        if self._amsha != 1:
            # if we are in a varga, self.init_Cusps will change them to that varga
            self._cusps = self.init_Cusps(self._cusps)
        self._signs = Signs(self._planets, self._cusps, self.context)
        self._rashi_planets = Planets(replace(self._planets.context,amsha=1))
        self._signs = Signs(self._planets,self._cusps,self.context)
        self.sysflgstr = const.sysflgstr(self.context.sysflg)
        # we need to initalize dignities so that we can do saptavargaja bala on demand
        self._dignities = self._get_dignities()

    def varga_name(self):
        match self._amsha:
            case 1:
                return "Rashi"
            case 2:
                return "Hora Parivritti"
            case 3:
                return "Drekkana Parivritti"
            case 4:
                return "Chaturthamsha Parivritti"
            case 5:
                return "Panchamsha"
            case 7:
                return "Saptamsha"
            case 9:
                return "Navamsha"
            case 30:
                return "Trimshamsha (Parivritti)"
            case -2:
                return "Hora"
            case -3:
                return "Drekkana"
            case -4:
                return "Chaturthamsha"
            case -10:
                return "Dashamsha"
            case -100:
                return "Dashamsha - Even Signs Reverse"
            case -12:
                return "Dvadashamsha"
            case -16:
                return "Shodashamsha"
            case -20:
                return "Vimshamsha"
            case -24:
                return "Parashara Chaturvimshamsha"
            case -240:
                return "Siddhamsha (d24s)"
            case -27:
                return "Bhamsha"
            case -40:
                return "Khavedamsha"
            case -45:
                return "Akshavedamsha"
            case -60:
                return "Shashtyamsha"
            case _ if self.amsha() > 5:
                return "parivritti"

    def amsha(self):
        return self._amsha

    def init_Planets(self, planets):
        retplanets = {}
        for name,planet in planets.items():
            retplanets[name] = planet_constructors[name](self.context,longitude=Longitude(planet.ecliptic_longitude(),amsha=self.amsha()))
        return Planets(self.context,retplanets)
              
    def init_Cusps(self, cusps):
        """
        cusps is a list of Cusp classes, which is what is stored in Cusps.self.cusps
        so iterate through, copying everything over, while changing the longitude
        """
        varga_cusps = []
        for cusp in cusps:
            varga_cusps.append(Cusp(longitude=cusp.ecliptic_longitude(),amsha=self.amsha(),speed=cusp.speed(),number=cusp.number(),context=cusp.context))
        return Cusps(self.context,cusps=varga_cusps)

    def planets(self):
        return self._planets

    def cusps(self):
        return self._cusps

    def signs(self):
        return self._signs

    def where_is(self, object: int | str) -> Sign:
        return self.signs().where_is(object)

    def lagna(self):
        if self.context.sysflg == const.HELIO or self.context.sysflg == const.BARY:
            return self.signs()[7]
            # this is for using Varga().rich("circular")
            # the lagna will be printed on the left side in the center
            # then the houses and signs go counter clockwise in the order of usual western astrology chart
            # so with the 7th on the left, we will have north at the top and east on the right
            # with heliocentric, the sun in the middle
            # with barycentric, the barycenter in the middle
            # though, with barycentric, it makes it seem like the sun is the same distance as the other planets from the barycenter
            # but obviously it is not. it seems on average the barycenter is not in the sun, but rather close to it
            # so it seems like maybe sometimes the barycenter is inside the sun? so then it is sort of like the sun is "off-center"
            # the solar system, and jupiter in particular, pull the sun "off-center"
        return self.signs().lagna()

    def deities(self):
        """
        return varga deities for the nine grahas and the lagna in that order
        """
        to_get = self.planets().grahas()
        to_get[1] = self.cusps()[1]
        ret = []
        for obj in to_get.values():
            ret.append(obj.deity())
        return ret

    def dignities(self):
        return self._dignities

    def _get_dignities(self) -> [str]:
        """
        return a list of dignities in the natural order
        Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn

        dignity is a combination of natural and temporary relationship
        we can use the temporary relationship from the varga itself, or from the rashi chart

        if Planets is in a varga and temp_planets=None, then it will use temporary relationships based on that varga
        so if, for instance, you want to determine dignity in the Navamsha based on temporary friends in the Rashi
        you must past d9Planets.dignites(temp_planets=d1Planets)
        """
        if self.context.rashi_temporary_friendships:
            return self.planets()._dignities(self._rashi_planets)
        else:
            return self.planets()._dignities(self.planets()) # could pass self.planets(), but that is what Planets.dignities() will do without an argument
        
    def __str__(self):
        output = PrettyTable()
        output.field_names = ["  ", "   ", "    ", "     "]

        # we pass _rashi_planets to dignities so that it uses the rashi to calculate temporary relationships
        dignities = printf.dignity_table(self.dignities())

        jaimini_karakas = printf.jaimini_karakas_str(self.planets().jaimini_karakas())

        output.add_row([f"{self.signs()[12]}", f"{self.signs()[1]}", f"{self.signs()[2]}", f"{self.signs()[3]}"])
        output.add_divider()
        output.add_row([f"{self.signs()[11]}", f"{dignities} ", f"{jaimini_karakas}", f"{self.signs()[4]}"])
        output.add_divider()
        output.add_row([f"{self.signs()[10]}", "  ", "  ", f"{self.signs()[5]}"])
        output.add_divider()
        output.add_row([f"{self.signs()[9]}", f"{self.signs()[8]}", f"{self.signs()[7]}", f"{self.signs()[6]}"])

        ret = output.get_string(fields=["  ", "   ", "    ", "     "])

        return self.mkheader() + ret


    def __repr__(self):
        """
        represents as a header with the chart information
        """
        return self.mkheader()

    def mkheader(self):
        return utils.mkheader(self)
        

    def richDrawing_south_indian(self):
        spread = Table(box=None)

        spread.add_column(" ",justify="center")
        spread.add_column(" ",justify="center")
        spread.add_column(" ",justify="center")
        spread.add_column(" ",justify="center")
        spread.add_column(" ",justify="center")

        spread.add_row(self.signs()[12].richDrawing(),self.signs()[1].richDrawing(),self.signs()[2].richDrawing(),self.signs()[3].richDrawing())
        spread.add_row(self.signs()[11].richDrawing(),"dignities?","jaimini karakas?",self.signs()[4].richDrawing())
        spread.add_row(self.signs()[10].richDrawing(),"empty","empty",self.signs()[5].richDrawing())
        spread.add_row(self.signs()[9].richDrawing(),self.signs()[8].richDrawing(),self.signs()[7].richDrawing(),self.signs()[6].richDrawing())

        return spread

    def richDrawing_circular(self):
        spread = Table(box=None)

        spread.add_column(" ",justify="center",style="#00ff00")
        spread.add_column(" ",justify="center")
        spread.add_column(" ",justify="center")
        spread.add_column(" ",justify="center")
        spread.add_column(" ",justify="center")

        lagna = self.lagna()

        # list of sign classes
        # with the empty list at the beginning
        # we can use 1-12 as the index, just as with Varga().signs()
        signs = [[]]

        # initialize list of Sign classes
        for sign in range(1,13):
            signs.append(self.signs()[lagna.astrological_signs_forward(sign)])

        # call signs.richDrawing() at the appropriate place
        # lagna is on the leftmost, which is east, facing south, which is the center of the 5x5 table

        # usually Chart().rashi().signs()[n] means the nth sign
        # here, signs[n] means signs from the lagna
        spread.add_row("",signs[11].richDrawing(),signs[10].richDrawing(),signs[9].richDrawing(),"")
        spread.add_row(signs[12].richDrawing(),"","","",signs[8].richDrawing())
        spread.add_row(signs[1].richDrawing(),"","","",signs[7].richDrawing())
        spread.add_row(signs[2].richDrawing(),"","","",signs[6].richDrawing())
        spread.add_row("",signs[3].richDrawing(),signs[4].richDrawing(),signs[5].richDrawing(),"")

        return spread

    def rich(self, which="circular"):
        console = Console()
        match which:
            case "south_indian":
                console.print(self.richDrawing_south_indian())
            case "circular":
                console.print(self.richDrawing_circular())
            case _:
                return


