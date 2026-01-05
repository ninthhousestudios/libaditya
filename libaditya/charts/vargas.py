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

    def __init__(self,amsha,planets,cusps,context,chart):
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
        self.chart = chart

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
        return self._get_pada(lagna)

    def upapada(self) -> Sign:
        """
        the "foot" of the 10th cusp
        find how many signs the lagna lord is from the lagna
        from the lord that many signs is the pada
        if the lord is in the 4th or 10th from lagna, pada is in the 4th
        if the lord is in the 1st or 7th from lagna, pada is in the 10th

        return Sign class of the pada
        """
        # we need to find the Sign that has the 10th cusp
        tenth = self.signs().where_is(10) # 10 means the 10th cusp
        return self._get_pada(tenth)

    def padas(self):
        """
        return a dictionary of all the padas
        key is the Sign, value is the Sign of the pada
        """
        padas = {}
        for sign in self.signs():
            padas[sign] = self._get_pada(sign)
        return padas

    def _get_pada(self, sign: Sign) -> Sign:
        """
        a generic helper to get the pada Sign of Sign sign
        """
        # Planet class of the lord
        lord = self.planets()[sign.lord()]
        signs_apart = sign.astrological_signs_apart(lord.sign())

        # check special pada rules
        if signs_apart == 4 or signs_apart == 10:
            return self.signs()[sign.astrological_signs_foward(4)]
        if signs_apart == 1 or signs_apart == 7:
            return self.signs()[sign.astrological_signs_foward(10)]
        # otherwise signs_apart forward from lagna lord is the pada
        lords_sign = self.signs()[lord.sign()]
        return self.signs()[lords_sign.astrological_signs_foward(signs_apart)]

    def jaimini_first_strength(self) -> [Sign]:
        """
        calculate Jaiminis first source of strength for all signs
        return a list of Sign classes with highest strength, then second-highest, etc.
        """
        #import pdb; pdb.set_trace()
        sortedls = []
        for sign in self.signs():
            # determine where in ls to put the sign
            if sortedls == []:
                sortedls.append(sign)
                continue
            # determine if sign is stronger than sortedls[0]
            # if so, put it at sortedls[0], if not check against sortedls[1] if it exists
            for n,sorted_sign in enumerate(sortedls):
                if sign.how_many_karakas() > 0 and sorted_sign.how_many_karakas() == 0:
                    # sign is stronger than sorted_sign, so put sign at sorted_sign
                    sortedls.insert(n,sign)
                    break # break out of this while loop and go back to the for loop, checking the next sign
                if sign.how_many_karakas() > sorted_sign.how_many_karakas():
                    # sign is stronger, so insert here, then get next sign
                    sortedls.insert(n,sign)
                    break
                if sign.how_many_karakas() < sorted_sign.how_many_karakas():
                    # sign is weaker, so go to next sorted_sign to check that
                    if n == len(sortedls) - 1:
                    # this is the last sign in what we have so far
                    # sign is the weaker, so append it at the end
                        sortedls.append(sign)
                        break
                if sign.how_many_karakas() == sorted_sign.how_many_karakas():
                    # need to find which planet has the highest dignitiy
                    has_higher = utils.compare_signs_dignities(sign,sorted_sign,self.dignities())
                    if has_higher == 1:
                        # sign is stronger
                        sortedls.insert(n,sign)
                        break
                    if has_higher == 2:
                        # sorted_sign is stronger, so continue this loop to check against the next sign
                        # unless this is the last element, then append
                        if n == len(sortedls) - 1:
                        # this is the last sign in what we have so far
                        # sign is the weaker, so append it at the end
                            sortedls.append(sign)
                            break
                        continue
                    if has_higher == 0:
                        # they have the same strength on this level, so we must check other things
                        # we have to check sign modalities to see which is stronger
                        # dual strongest, fixed middle, moveable weakest
                        modality_strength = utils.compare_signs_modalities(sign,sorted_sign)
                        if modality_strength == 1:
                            # sign is stronger
                            sortedls.insert(n,sign)
                            break
                        if modality_strength == 2:
                            # if this is the last element in sortedls, append sign since it is weaker
                            if n == len(sortedls) - 1:
                            # this is the last sign in what we have so far
                            # sign is the weaker, so append it at the end
                                sortedls.append(sign)
                                break
                            # if not the last Planet in sortedls, test against the next Planet to see where to put it
                            continue
                        if modality_strength == 0:
                            # have same modality strength, check next level, which is the rashis of the lords of these rashis
                            # 5. If both the Rasis are the same modality, then consider the
                            # lord of the Rasi in the same manner as the Rasi has been considered.
                            # he says "consider the lord of the Rasi in the same manner as the Rashi"
                            # can we consider a Planet in the same way as a Sign? no
                            # a Planet is or is not a karaka, but does not have .how_many_karakas() like Sign
                            # so we need to consider the (two) rāśī of the lords of these two rashis "rāśī adhipatyoḥ imau"
                            # so consider the rashi the lord is in and the rashi the sorted signs lord is in, and which is stronger
                            # therein is the stronger; if this doesn't decide, then go to 6. below
                            signs_lord = sign.lord()
                            signs_Lord = self.planets()[signs_lord] # the Planet class of the lord
                            signs_lords_rashi = self.signs().where_is(signs_lord) # return the Sign class
                            sorted_signs_lord = sorted_sign.lord()
                            sorted_signs_Lord = self.planets()[sorted_signs_lord]
                            sorted_signs_lords_rashi = self.signs().where_is(sorted_signs_lord)
                            # now lets compare their rashis just as we did above

                            if signs_lords_rashi.how_many_karakas() > 0 and sorted_signs_lords_rashi.how_many_karakas() == 0:
                                # sign is stronger than sorted_sign, so put sign at sorted_sign
                                sortedls.insert(n,sign)
                                break # break out of this while loop and go back to the for loop, checking the next sign
                            if signs_lords_rashi.how_many_karakas() > sorted_signs_lords_rashi.how_many_karakas():
                                # sign is stronger, so insert here, then get next sign
                                sortedls.insert(n,sign)
                                break
                            if signs_lords_rashi.how_many_karakas() < sorted_signs_lords_rashi.how_many_karakas():
                                # sign is weaker, so go to next sorted_sign to check that
                                if n == len(sortedls) - 1:
                                # this is the last sign in what we have so far
                                # sign is the weaker, so append it at the end
                                    sortedls.append(sign)
                                    break
                                continue
                            if signs_lords_rashi.how_many_karakas() == sorted_signs_lords_rashi.how_many_karakas():
                                # need to find which planet has the highest dignitiy
                                has_higher = utils.compare_signs_dignities(signs_lords_rashi,sorted_signs_lords_rashi,self.dignities())
                                if has_higher == 1:
                                    # sign is stronger
                                    sortedls.insert(n,sign)
                                    break
                                if has_higher == 2:
                                    # sorted_sign is stronger, so continue this loop to check against the next sign
                                    if n == len(sortedls) - 1:
                                    # this is the last sign in what we have so far
                                    # sign is the weaker, so append it at the end
                                        sortedls.append(sign)
                                        break
                                    continue
                                if has_higher == 0:
                                    # they have the same strength on this level, so we must check other things
                                    # we have to check sign modalities to see which is stronger
                                    # dual strongest, fixed middle, moveable weakest
                                    modality_strength = utils.compare_signs_modalities(signs_lords_rashi,sorted_signs_lords_rashi)
                                    if modality_strength == 1:
                                        # sign is stronger
                                        sortedls.insert(n,sign)
                                        break
                                    if modality_strength == 2:
                                        if n == len(sortedls) - 1:
                                        # this is the last sign in what we have so far
                                        # sign is the weaker, so append it at the end
                                            sortedls.append(sign)
                                            break
                                        continue
                                    if modality_strength == 0:
                                        # 6. If both the lords are the same strong according to the above measures, 
                                        # then the lord who has the highest degrees within the Rasi it is in is the stronger, and thus its Rasi will be the stronger
                                        if signs_Lord.real_in_sign_longitude() >= sorted_signs_Lord.real_in_sign_longitude():
                                            sortedls.insert(n,sign)
                                        else:
                                            sortedls.append(sign)
                            break
                # if it is not stronger than any, it is weaker than all, so it goes at the end
        return sortedls


    def dignities(self):
        return self.planets().dignities(self._rashi_planets)

    def __str__(self):
        output = PrettyTable()
        output.field_names = ["  ", "   ", "    ", "     "]

        # we pass _rashi_planets to dignities so that it uses the rashi to calculate temporary relationships
        dignities = printf.dignity_table(self.dignities())

        jaimini_karakas = printf.jaimini_karakas_str(self.chart.jaimini().karakas())

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
    
    def __init__(self,planets,cusps,context,chart):
        self.context = context
        self._planets = planets
        self._cusps = cusps
        self._signs = Signs(self._planets,self._cusps,self.context)
        super().__init__(amsha=1,planets=self._planets,cusps=self._cusps,context=self.context,chart=chart)

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
