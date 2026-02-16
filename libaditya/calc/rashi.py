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
from dataclasses import replace

from libaditya.objects import Planet, RashiBala
from libaditya.calc import Varga
from libaditya.calc import vimshottari
from libaditya.calc.panchanga import Panchanga
from libaditya.calc.swe_functions import SWERashi
from libaditya.calc.hellenistic import Hellenistic
from libaditya.calc.returns import Returns
from libaditya.draw.draw_sbc import DrawSBC

from .jaimini_get import JaiminiGet


class Rashi(Varga,SWERashi,JaiminiGet,RashiBala,DrawSBC,Hellenistic,Returns):

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

