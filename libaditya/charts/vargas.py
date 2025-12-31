#    This file is part of pyphemeris.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
#
#    pyphemeris is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyphemeris is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with pyphemeris.  If not, see <https://www.gnu.org/licenses/>.

import swisseph as swe
from prettytable import PrettyTable
from dataclasses import replace

from libaditya import constants as const
from libaditya import utils
from libaditya import print_functions as printf

from libaditya.objects import Sign, Signs, Planets, Cusp, Cusps
# to make it less confusing, pdict will be the dictionary of Planet classes
from libaditya.objects import planets as pdict

class Varga:

    def __init__(self,amsha,planets,cusps,context):
        self._amsha = amsha
        self._rashi_planets = planets
        if amsha == 1:
            self._planets = planets
        else:
            # dont print nakshatras in vargas not = 1
            self.context = replace(context,print_nakshatras=False)
            self._planets = self.init_planets(planets)
        self._cusps = self.init_cusps(cusps)
        self._signs = Signs(self._planets,self._cusps,self.context)
        self.sysflgstr = const.sysflgstr(context.sysflg)

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
            case 9:
                return "Navamsha"
            case _:
                return "Not yet implemented"

    def amsha(self):
        return self._amsha

    def init_planets(self, planets):
        retplanets = {}
        for name,planet in planets.items():
            retplanets[name] = pdict[name](self.context,longitude=((planet.varga(self.amsha()))))
        return Planets(self.context,retplanets)
              
    def init_cusps(self, cusps):
        """
        cusps is a list of Cusp classes, which is what is stored in Cusps.self.cusps
        so iterate through, copying everything over, while changing the longitude
        """
        varga_cusps = []
        for cusp in cusps:
            varga_cusps.append(Cusp(cusp.varga(self.amsha()),cusp.speed(),cusp.number(),cusp.context))
        return Cusps(self.context,varga_cusps)

    def planets(self):
        return self._planets

    def cusps(self):
        return self._cusps

    def signs(self):
        return self._signs

    def lagna(self):
        return self.signs().lagna()

    def pada(self) -> Sign:
        """
        the "foot" of the lagna
        find how many signs the lagna lord is from the lagna
        from the lord that many signs is the pada
        if the lord is in the 4th or 10th from lagna, pada is in the 4th
        if the lord is in the 1st or 7th from lagna, pada is in the 10th

        return Sign class of the pada
        """
        lagna = self.signs().lagna()
        return lagna.pada(self.planets()[lagna.lord()])
#        # Sign class of the lagna
#        lagna = self.signs().lagna()
#        # Planet class of the lord
#        lagna_lord = self.planets()[lagna.lord()]
#        signs_apart = lagna.astrological_signs_apart(lagna_lord.sign())
#
#        # check special pada rules
#        if signs_apart == 4 or signs_apart == 10:
#            return self.signs()[lagna.n_signs_forward(4)]
#        if signs_apart == 1 or signs_apart == 7:
#            return self.signs()[lagna.n_signs_forward(10)]
#        # otherwise signs_apart forward from lagna lord is the pada
#        lords_sign = self.signs()[lagna_lord.sign()]
#        return self.signs()[lords_sign.n_signs_forward(signs_apart)]
#
    def upapada(self) -> Sign:
        """
        the "foot" of the 10th house
        find how many signs the lagna lord is from the lagna
        from the lord that many signs is the pada
        if the lord is in the 4th or 10th from lagna, pada is in the 4th
        if the lord is in the 1st or 7th from lagna, pada is in the 10th

        return Sign class of the pada
        """
        tenth = self.signs()[self.signs().lagna().n_signs_forward(10)]
        return tenth.pada(self.planets()[tenth.lord()])
#        # Sign class of the lagna
#        lagna = self.signs().lagna()
#        tenth = self.signs()[lagna.n_signs_forward(10)]
#        # Planet class of the lord
#        tenth_lord = self.planets()[tenth.lord()]
#        signs_apart = tenth.astrological_signs_apart(tenth_lord.sign())
#
#        # check special pada rules
#        if signs_apart == 4 or signs_apart == 10:
#            return self.signs()[tenth.n_signs_forward(4)]
#        if signs_apart == 1 or signs_apart == 7:
#            return self.signs()[tenth.n_signs_forward(10)]
#        # otherwise signs_apart forward from lagna lord is the pada
#        lords_sign = self.signs()[tenth_lord.sign()]
#        return self.signs()[lords_sign.n_signs_forward(signs_apart)]
    
    def __str__(self):
        output = PrettyTable()
        output.field_names = ["  ", "   ", "    ", "     "]

        # we pass _rashi_planets to dignities so that it uses the rashi to calculate temporary relationships
        dignities = printf.dignity_table(self.planets().dignities(self._rashi_planets))

        # print jaimini karakas in the rashi
        jaimini_karakas = ""
        if self._amsha == 1:
            jaimini_karakas = printf.jaimini_karakas(self.planets().jaimini_karakas())

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
        this is for every varga except the Rashi
        the rashi is printed with nakshatras
        the others are not

        str prints a table with signs at the top
        each object is printed under its sign
        as "object in_sign_longitude"
        the number of rows will be equal to the most objects that are in one sign
        """
        output = PrettyTable()
        # list of the sign names
        output.field_names= list([sign for sign in [self.context.names.sign_names]][0])

        # get the sign with the most objects, so we know how many rows to print
        rows = self._signs.most_objects()

        for r in range(0,rows):
            # construct the row
            row = []
            # could also write for s in self._signs.signs().values()
            # and then replace self._signs[s]._objects by s._objects
            for s in self._signs.keys():
                if len(self._signs[s]._objects) > r:
                    if not self.context.print_outer_planets and self._signs[s]._objects[r].object_type()=="Planet" and self._signs[s]._objects[r].is_outer_planet():
                        row.append("")
                        continue
                    if self._signs[s]._objects[r].identity() == "Sun" and self.context.sysflg == const.HELIO:
                        # dont print the Sun is using heliocentric coordinates
                        row.append("")
                        continue
                    rowstr = f"{self._signs[s]._objects[r].name()}\n{self._signs[s]._objects[r].in_sign_longitude()}\n"
                    # if this is a Rashi, print nakshatras, if that is specified
                    # unless it is barycentric or heliocentric
                    if isinstance(self,Rashi) and (self.context.sysflg != const.BARY and self.context.sysflg != const.HELIO):
                        # print nakshatras or not
                        if self.context.print_nakshatras:
                            rowstr += f"{self._signs[s]._objects[r].nakshatra_name()}\n{self._signs[s]._objects[r].nakshatra().elapsed()}\n"
                    row.append(rowstr) 
                else:
                    row.append("")
            output.add_row(row)

        ret = output.get_string(fields=list([sign for sign in [self.context.names.sign_names]][0]))
        return self.mkheader() + ret

    def draw_sun_by_sign_table(self):
        """
        this prints nakshatras with the chart
        """
        output = PrettyTable()
        # list of the sign names
        output.field_names=list(["Object"] + list([sign for sign in [self.context.names.sign_names]][0]) + ["Nakshatra"] + ["Elapsed"])

        # now rows
        # first the planets, then cusps
        # if the planet is in a sign, print its in_sign_longitude in the column, otherwise print nothing
        for p in self._planets:
            output.add_row([p.name(),*utils.construct_varga_row(p),p.nakshatra_name(),p.nakshatra().elapsed()])

        for c in self._cusps:
            output.add_row([c.name(),*utils.construct_varga_row(c),c.nakshatra_name(),c.nakshatra().elapsed()])

        if isinstance(self, Rashi):
            ret = output.get_string(fields=list(["Object"] + list([sign for sign in [self.context.names.sign_names]][0]) + ["Nakshatra"] + ["Elapsed"]))
        else:
            ret = output.get_string(fields=list(["Object"] + list([sign for sign in [self.context.names.sign_names]][0])))

        return self.mkheader() + ret
        
    def mkheader(self):
        header = ""
        header += f"Varga {self._amsha} {self.varga_name()}\n"
        header += f"{self.sysflgstr} coordinates\n"
        header += f"{const.circle_name(self.context.circle)}\n"
        if self.context.sysflg == swe.FLG_SIDEREAL:
            # for sidereal signs we actually use swisseph 36
            # dhruva equatorial is only for nakshatras
            if self.context.ayanamsa == 98:
                header += f"{const.ayanamsa_name(36)} ayanamsa for signs\n"
                header += f"{const.ayanamsa_name(98)} ayanamsa for nakshatras\n"
            else:
                header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
        elif self.context.sysflg == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
            if self.context.ayanamsa == 98:
                self.context.ayanamsa = 36
            header += f"{self.context.location}\n"
            header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
        else:
            header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
        header += f"{self.context.location}\n"
        header += f"{self.context.timeJD}\n"
        return header



class Rashi(Varga):
    
    def __init__(self,planets,cusps,context):
        self.context = context
        self._planets = planets
        self._cusps = cusps
        self._signs = Signs(self._planets,self._cusps,self.context)
        super().__init__(amsha=1,planets=self._planets,cusps=self._cusps,context=self.context)

    def planets(self):
        return self._planets

    def cusps(self):
        return self._cusps

    def signs(self):
        return self._signs

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
        second = self.signs()[lagna.n_signs_forward(2)].how_many_karakas()
        third = self.signs()[lagna.n_signs_forward(3)].how_many_karakas()
        fourth = self.signs()[lagna.n_signs_forward(4)].how_many_karakas()
        fifth = self.signs()[lagna.n_signs_forward(5)].how_many_karakas()
        sixth = self.signs()[lagna.n_signs_forward(6)].how_many_karakas()
        seventh = self.signs()[lagna.n_signs_forward(7)].how_many_karakas()
        eighth = self.signs()[lagna.n_signs_forward(8)].how_many_karakas()
        ninth = self.signs()[lagna.n_signs_forward(9)].how_many_karakas()
        tenth = self.signs()[lagna.n_signs_forward(10)].how_many_karakas()
        eleventh = self.signs()[lagna.n_signs_forward(11)].how_many_karakas()
        twelfth = self.signs()[lagna.n_signs_forward(12)].how_many_karakas()
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
