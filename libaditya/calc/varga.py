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

from rich import box
from rich.table import Table
from rich.console import Console

from libaditya import constants as const
from libaditya import utils
from libaditya import print_functions as printf

from libaditya.objects import Sign, Signs, Longitude, Planet, Planets, Cusp, Cusps, RashiBala
from libaditya.objects import planets as planet_constructors
from libaditya.calc import vimshottari
from libaditya.calc.panchanga import Panchanga
from libaditya.calc.swe_functions import SWERashi
from libaditya.calc.hellenistic import Hellenistic
from libaditya.draw.draw_sbc import DrawSBC

from .jaimini import Jaimini
from .jaimini_get import JaiminiGet

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
        
#    def mkheader(self):
#        header = ""
#        header += f"{self.context.name}\n"
#        header += f"Varga {self._amsha} {self.varga_name()}\n"
#        header += f"{self.sysflgstr} coordinates\n"
#        header += f"{const.circle_name(self.context.circle)}\n"
#        header += f"House system {swe.house_name(self.context.hsys.encode())}\n"
#        digplace = "rashi" if self.context.rashi_temporary_friendships else "varga"
#        header += f"Dignities based on {digplace}\n"
#        header += f"{self.context.rashi_aspects} rashi aspects\n"
#        if self.context.sysflg == swe.FLG_SIDEREAL:
#            # for sidereal signs we actually use swisseph 36
#            # dhruva equatorial is only for nakshatras
#            if self.context.ayanamsa == 98:
#                header += f"{const.ayanamsa_name(36)} ayanamsa for signs\n"
#                header += f"{const.ayanamsa_name(98)} ayanamsa for nakshatras\n"
#            else:
#                header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
#        elif self.context.sysflg == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
#            if self.context.ayanamsa == 98:
#                header += f"{const.ayanamsa_name(36)} ayanamsa for signs\n"
#                header += f"{const.ayanamsa_name(98)} ayanamsa for nakshatras\n"
#            header += f"{self.context.location.placename()} ({self.context.location.latitude()} lat, {self.context.location.longitude()} long)\n"
#            header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
#        else:
#            header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
#        header += f"{self.context.location.placename()} ({self.context.location.latitude()} lat, {self.context.location.longitude()} long)\n"
#        header += f"{self.context.timeJD}\n"
#        return header

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


class Rashi(Varga,SWERashi,JaiminiGet,RashiBala,DrawSBC,Hellenistic):

    def __init__(self,context,chart):
        self.master = chart
        super().__init__(context=context,amsha=1)
        self._dig_balas = self.init_dig_balas()
        self._saptavargaja_balas = self.init_saptavargaja_balas()
        self._sama_visama_balas = self.init_sama_visama_balas()
        self._kendradi_balas = self.init_kendradi_balas()
        self._drig_balas = self.init_drig_balas()

    def planets(self):
        return self._planets

    def ecliptic(self):
        return self._ecliptic

    def cusps(self):
        return self._cusps

    def signs(self):
        return self._signs

    def house_position(self, planet: str, hsys=None) -> float:
        """
        a wrapper for the function swe.house_pos()
        planet is the Planet.identity(), i.e., the english name of the desired planet
        """
        armc = self.cusps().armc()
        lat = self.context.location.latitude()
        eo = self.context.timeJD.ecliptic_obliquity()
        planet = self.planets()[planet]
        planet_coords = (planet.ecliptic_longitude(),planet.latitude())
        if hsys == None:
            hsys = self.context.hsys
        return swe.house_pos(armc,lat,eo,planet_coords,hsys.encode())

    def Master(self):
        """
        return the Chart that spawned it
        """
        return self.master

    def panchanga(self, **kwargs):
        """
        panchanga is here because it has to do with the sun and moon, with time
        that is the Rashi chart essentially
        none of the other vargas really need a separate class, because they are really subsections of this class
        which is why Rashi can hopefully reach all the Vargas

        Panchanga.__str__ prints the basic panchagna, and also the panchanga addendum
        __repr__ prints only the basic time and panchanga information
        """
        context = replace(self.context,**kwargs)
        return Panchanga(context)

    def print_current_vimshottari_dasha(self,yrlen="saura",levels=5):
        vimshottari.print_current_vdasha(self.context,yrlen,levels)
        return

    def rashi_argala(self) -> [[Planet],[Planet],[Planet]]:
        """
        it returns a list a lists, where each sublist is the combinatino of the corresponding argala lists of lagna and seventh

        this combines the argala formed to both 1st and 7th
        """
        lagna_arg = self.argala(self.signs().lagna())
        seventh_arg = self.argala(self.signs()[self.signs().lagna().astrological_signs_forward(7)])
        ret = [[],[],[]]
        for n,arg in enumerate(lagna_arg):
            for planet in lagna_arg[n]:
                ret[n].append(planet)
            for planet in seventh_arg[n]:
                ret[n].append(planet)
        return ret
        # each arg has three elements; put all of lagna_arg[0] together with seventh_arg[0], etc.


    def akriti_yogas(self):
        """
        find the akriti yogas in this Rashi varga
        these are rarely found perfectly or completely, so we find
        how many planets would need to be moved to create each
        this function returns a list of tuples of the name of each yoga and how many planets would
        need to be moved in order to create the yoga
        for these yogas, planets means the seven embodied planets, i.e., karakas
        """
        # this will be a list of tuples ("name", planets_to_move_to_form_yoga)
        akritis = []
        # these yogas are based on signs from the lagna
        lagna = self.signs().lagna()
        second = self.signs()[lagna.astrological_signs_foward(2)].how_many_karakas()
        third = self.signs()[lagna.astrological_signs_foward(3)].how_many_karakas()
        fourth = self.signs()[lagna.astrological_signs_foward(4)].how_many_karakas()
        fifth = self.signs()[lagna.astrological_signs_foward(5)].how_many_karakas()
        sixth = self.signs()[lagna.astrological_signs_foward(6)].how_many_karakas()
        seventh = self.signs()[lagna.astrological_signs_foward(7)].how_many_karakas()
        eighth = self.signs()[lagna.astrological_signs_foward(8)].how_many_karakas()
        ninth = self.signs()[lagna.astrological_signs_foward(9)].how_many_karakas()
        tenth = self.signs()[lagna.astrological_signs_foward(10)].how_many_karakas()
        eleventh = self.signs()[lagna.astrological_signs_foward(11)].how_many_karakas()
        twelfth = self.signs()[lagna.astrological_signs_foward(12)].how_many_karakas()
        lagna = self.signs().lagna().how_many_karakas()

        # sringataka yoga; all planets in 1,5,9 from lagna
        # the number of planets to move is 7 - the number of planets in these signs
        to_move = 7 - (lagna + fifth + ninth)
        akritis.append(("Sringataka", to_move))

        # artha hala; all planets in 2,6,10
        # the number of planets to move is 7 - the number of planets in these signs
        to_move = 7 - (second + sixth + tenth)
        akritis.append(("Artha Hala", to_move))

        # kama hala; all planets in 3,7,11
        # the number of planets to move is 7 - the number of planets in these signs
        to_move = 7 - (third + seventh + eleventh)
        akritis.append(("Kama Hala", to_move))

        # moksha hala; all planets in 4,8,12
        # the number of planets to move is 7 - the number of planets in these signs
        to_move = 7 - (fourth + eighth + twelfth)
        akritis.append(("Moksha Hala", to_move))

        # gada yogas; all planets in two successive angles 1/4,4/7,7/10,10/1, so check all of these

        # 1/4 gada
        to_move = 7 - (lagna + fourth)
        akritis.append(("Gada 1/4", to_move))

        # 4/7 gada
        to_move = 7 - (fourth + seventh)
        akritis.append(("Gada 4/7", to_move))

        # 7/10 gada
        to_move = 7 - (seventh + tenth)
        akritis.append(("Gada 7/10", to_move))

        # 10/1 gada
        to_move = 7 - (lagna + tenth)
        akritis.append(("Gada 1/4", to_move))

        # sakata; all planets in 1 and 7
        to_move = 7 - (lagna + seventh)
        akritis.append(("Sakata", to_move))

        # vihaga; all planets in 4 and 10 
        to_move = 7 - (fourth + tenth)
        akritis.append(("Vihaga", to_move))

        # kamala; all planets in the four angles
        to_move = 7 - (lagna + fourth + seventh + tenth)
        akritis.append(("Kamala", to_move))

        # panaphara vapi; all planets in 2,5,8,11
        to_move = 7 - (second + fifth + eighth + eleventh)
        akritis.append(("Panaphara Vapi", to_move))

        # apoklima vapi; all planets in 3,6,9,12
        to_move = 7 - (third + sixth + ninth + twelfth)
        akritis.append(("Apoklima Vapi", to_move))

        # do vajra and yava yogas
        # find out who is kruura and saumya and how to find out


        # yupa yoga; all planets in 1,2,3,4
        to_move = 7 - (lagna + second + third + fourth)
        akritis.append(("Yupa", to_move))

        # shara yoga: all planets in 4,5,6,7
        to_move = 7 - (fourth + fifth + sixth + seventh)
        akritis.append(("Shara", to_move))

        # shakti yoga; all planets in 7,8,9,10
        to_move = 7 - (seventh + eighth + ninth + tenth)
        akritis.append(("Shakti", to_move))

        # danda yoga; all planets in 10,11,12,1
        to_move = 7 - (tenth + eleventh + twelfth + lagna)
        akritis.append(("Danda", to_move))

#        # nauka yoga; all planets in the 1,2,3,4,5,6,7
#        to_move = 7 - (lagna + second + third + fourth + fifth + sixth + seventh)
#        akritis.append(("Nauka", to_move))
#
#        # kuta yoga; all planets in 4,5,6,7,8,9,10
#        to_move = 7 - (fourth + fifth + sixth + seventh + eighth + ninth + tenth)
#        akritis.append(("Kuta", to_move))
#
#        # chatra yoga; all planets in 7,8,9,10,11,12,1
#        to_move = 7 - (seventh + eighth + ninth + tenth + eleventh + twelfth + lagna)
#        akritis.append(("Chatra", to_move))
#
#        # chapa yoga; all planets in 10,11,12,1,2,3,4
#        to_move = 7 - (tenth + eleventh + twelfth + lagna + second + third + fourth)
#        akritis.append(("Chapa", to_move))
#
#        # artha panaphara ardha chandra; all planets in 2,3,4,5,6,7,8
#        to_move = 7 - (second + third + fourth + fifth + sixth + seventh + eighth)
#        akritis.append(("Artha Panaphara Ardha Chandra", to_move))
#
#        # dharma panaphara ardha chandra; all planets in 5,6,7,8,9,10,11
#        to_move = 7 - (fifth + sixth + seventh + eighth + ninth + tenth + eleventh)
#        akritis.append(("Dharma Panaphara Ardha Chandra", to_move))
#
#        # moksha panaphara ardha chandra; all planets in 8,9,10,11,12,1,2
#        to_move = 7 - (eighth + ninth + tenth + eleventh + twelfth + lagna + second)
#        akritis.append(("Moksha Panaphara Ardha Chandra", to_move))
#
#        # kama panaphara ardha chandra; all planets in 11,12,1,2,3,4,5
#        to_move = 7 - (eleventh + twelfth + lagna + second + third + fourth + fifth)
#        akritis.append(("Kama Panaphara Ardha Chandra", to_move))
#
#        # kama apoklima ardha chandra; all planets in 3,4,5,6,7,8,9
#        to_move = 7 - (third + fourth + fifth + sixth + seventh + eighth + ninth)
#        akritis.append(("Kama Apoklima Ardha Chandra", to_move))
#
#        # artha apoklima ardha chandra; all planets in 6,7,8,9,10,11,12
#        to_move = 7 - (sixth + seventh + eighth + ninth + tenth + eleventh + twelfth)
#        akritis.append(("Artha Apoklima Ardha Chandra", to_move))
#
#        # dharma apoklima ardha chandra; all planets in 9,10,11,12,1,2,3
#        to_move = 7 - (ninth + tenth + eleventh + twelfth + lagna + second + third)
#        akritis.append(("Dharma Apoklima Ardha Chandra", to_move))
#
#        # moksha apoklima ardha chandra; all planets in 12,1,2,3,4,5,6
#        to_move = 7 - (twelfth + lagna + second + third + fourth + fifth + sixth)
#        akritis.append(("Moksha Apoklima Ardha Chandra", to_move))

        # chakra yoga; all planets in 1,3,5,7,9,11
        to_move = 7 - (lagna + third + fifth + seventh + ninth + eleventh)
        akritis.append(("Chakra", to_move))

        # samudra yoga; all plants in 2,4,6,8,10,12
        to_move = 7 - (second + fourth + sixth + eighth + tenth + twelfth)
        akritis.append(("Samdura", to_move))

        return akritis

