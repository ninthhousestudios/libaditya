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

from more_itertools import collapse

from libaditya import utils

from libaditya.objects import Planet, Planets, Sign

class Jaimini:
    """
    this is calc.Jaimini

    it is really a Varga, even though Varga inherits from here

    this class is a "Mixin"
    it has no __init__ functions and cannot instantiate anything
    it inherits unto Varga, giving Varga all of Jaimini capabilities

    can use any Varga.methods()

    this is really just to keep Varga from being humongeous by itself, so the functionality
    will be split in modules that inherit into Varga

    do not confuse with charts.Jaimini, which provides API functionality through Chart
    that is the frontend
    this is the backend
    """


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

    def padas(self) -> {Sign:Sign}:
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
            return self.signs()[sign.astrological_signs_forward(4)]
        if signs_apart == 1 or signs_apart == 7:
            return self.signs()[sign.astrological_signs_forward(10)]
        # otherwise signs_apart forward from lagna lord is the pada
        lords_sign = self.signs()[lord.sign()]
        return self.signs()[lords_sign.astrological_signs_forward(signs_apart)]

    def bandhana_yogas(self) -> [([Planet],[Planet])]:
        """
        return a list of tuples of Planet lists that are forming bandhana yogas
        tuple[0] and tuple[1] are planets are that in bandhana relationship to each other from the ascendant
        if, in:
        2-12
        3-11
        4-10
        5-9
        6-8
        relationship as signs from the ascedant
        """
        # pairs=((2,12),(3,11),(4,10),(5,9),(6,8))
        # we go forwards and backwards by the same amount

        pairs = (2,3,4,5,6)
        lagna = self.lagna()

        ret = []

        for pair in pairs:
            one = self.signs()[lagna.astrological_signs_forward(pair)]
            two = self.signs()[lagna.astrological_signs_backward(pair)]
            if one.how_many_grahas() == two.how_many_grahas():
                if one.how_many_grahas() == 0:
                    continue
                s1ls = []
                s2ls = []
                for sign1, sign2 in zip(one.grahas(),two.grahas()):
                    s1ls.append(sign1)
                    s2ls.append(sign2)
                ret.append((s1ls,s2ls))

        return ret

    def argala(self, rashi: Sign) -> [[Planet], [Planet], [Planet]]:
        """
        get argala to rashi in this varga
        
        returns three lists
        [Planet classes forming argala from/to rashi]
        [malefic Planet classes forming argala to 3rd from rashi]
        [Planet classes being obstructed from/to rashi]
        """
        # will need the first strength of all the signs to determine argala
        fs = self.jaimini_first_strength() 
        # if ketu is in this sign, we could backwards for argala
        sign = -1 if self.where_is("Ketu").sign() == rashi.sign() else 1 
        # find our Sign classes of argala-virodhina pairs
        # 2-12
        # 11-3
        # 4-10
        # 9-5
        # check third for more malefics than benefics
        second = self.signs()[rashi.astrological_signs_forward(sign*2)]
        twelfth = self.signs()[rashi.astrological_signs_forward(sign*12)]
        eleventh = self.signs()[rashi.astrological_signs_forward(sign*11)]
        third = self.signs()[rashi.astrological_signs_forward(sign*3)]
        fourth = self.signs()[rashi.astrological_signs_forward(sign*4)]
        tenth = self.signs()[rashi.astrological_signs_forward(sign*10)]
        ninth = self.signs()[rashi.astrological_signs_forward(sign*9)]
        fifth = self.signs()[rashi.astrological_signs_forward(sign*5)]
        argala = []
        obstructed = []
        pairs = [(second,twelfth),(eleventh,third),(fourth,tenth),(ninth,fifth)]

        # now we can loop on these pairs
        for arg,vir in pairs:
            if arg.how_many_grahas() > vir.how_many_grahas():
                # if there are more grahas in arg, then they cause argala
                # cant be obstructed by vir, so add them to argala list
                argala.append(arg.grahas())
            if arg.how_many_grahas() < vir.how_many_grahas():
                # virodhina house has fewer planets, but are they are also weaker?
                # if they are weaker than cannot obstruct; if not weaker, can obstruct
                # how to determine how weak? sign strength
                if fs.index(vir) > fs.index(arg):
                    # vir has a higher index, it is weaker, so it cannot obstruct
                    # argala sign is stronger, so the planets form argala
                    argala.append(arg.grahas())
                else:
                    # if vir has a lower index, it is stronger, so it does obstruct
                    obstructed.append(arg.grahas())
            if arg.how_many_grahas() == vir.how_many_grahas():
                obstructed.append(arg.grahas())

        # check malefic argala in 3rd
        mal = [] # how many malefics in Three
        ben = [] # how many benefics in Three
        for graha in third.grahas():
            if graha.nature() == "Malefic":
                mal.append(graha)
            else:
                ben.append(graha)
        third_argala = []
        if len(mal) > len(ben):
            # if there are more malefics in the 3rd than benefics, these malefics causes a special argala
            third_argala.append(mal)

        return list(collapse(argala)),list(collapse(third_argala)),list(collapse(obstructed))


    def jaimini_first_strength(self) -> [Sign]:
        """
        calculate Jaiminis first source of strength for all signs
        return a list of Sign classes with highest strength, then second-highest, etc.
        """
        sortedls = []
        for sign in self.signs():
            # determine where in ls to put the sign
            if sortedls == []:
                sortedls.append(sign)
                continue
            # determine if sign is stronger than sortedls[0]
            # if so, put it at sortedls[0], if not check against sortedls[1] if it exists
            for n,sorted_sign in enumerate(sortedls):
                #if sign.sign() == 12 and n == 3:
                #import pdb; pdb.set_trace()
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
                    continue
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

                            has_higher = utils.compare_planets_dignities(self.planets()._dignities()[signs_Lord.list_index()],self.planets()._dignities()[sorted_signs_Lord.list_index()])

                            # compare the signs of the lords

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
                                if has_higher == 1:
                                    sortedls.insert(n,sign)
                                    break # break out of this while loop and go back to the for loop, checking the next sign
                                if has_higher == 2:
                                    # sign is weaker, so go to next sorted_sign to check that
                                    if n == len(sortedls) - 1:
                                    # this is the last sign in what we have so far
                                    # sign is the weaker, so append it at the end
                                        sortedls.append(sign)
                                        break
                                    continue
                                if has_higher == 0:
                                    # the lords have the same dignity, so check the modalities of their signs
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
                                        # 6. if both the lords are the same strong according to the above measures, 
                                        # then the lord who has the highest degrees within the rasi it is in is the stronger, and thus its rasi will be the stronger
                                        if signs_Lord.real_in_sign_longitude() == sorted_signs_Lord.real_in_sign_longitude():
                                            # this means the lord is the same, so we have to go to the last tier of strength
                                            # so get the two signs of the planet
                                            if sign.sign()%2 == 1:
                                                # odd sign is stronger
                                                sortedls.insert(n,sign)
                                                break
                                            else:
                                                if n == len(sortedls) - 1:
                                                # this is the last sign in what we have so far
                                                # sign is the weaker, so append it at the end
                                                    sortedls.append(sign)
                                                    break
                                                continue
                                        if signs_Lord.real_in_sign_longitude() > sorted_signs_Lord.real_in_sign_longitude():
                                            sortedls.insert(n,sign)
                                            break
                                        else:
                                            sortedls.append(sign)
                                            break
                                        # if this is equal, then we are dealing with two signs of the same lord
                                        # that are not differentiated by any other qualities, so below is how we do it
                # if it is not stronger than any, it is weaker than all, so it goes at the end
        return sortedls

    def jaimini_second_strength(self) -> {Sign: [Planets]}:
        """
        calculate Jaiminis second source of strength for all signs
        return a dictionary of Sign: [Planet]
        [Planet] is a list of Planet classes that provide a source of strength to Sign
        due either to conjunctino or rashi aspect
        this be either Mercury, Jupiter, or the Lord of Sign
        """
        sss = {}

        jupiter_Sign = self.signs()[self.planets().jupiter().sign()]
        mercury_Sign = self.signs()[self.planets().mercury().sign()]

        for sign in self.signs():
            sourcels = [] # list to hold Planet-s that are conjunct or aspect this sign
            jup_aspects = self.signs().rashi_aspect_from_to(jupiter_Sign,sign)
            # 1 means jupiter aspects sign from jupiter_Sign; 0 not
            mer_aspects = self.signs().rashi_aspect_from_to(mercury_Sign,sign)
            lord = self.planets()[sign.lord()]
            lords_Sign = self.signs()[lord.sign()]
            lord_aspects = self.signs().rashi_aspect_from_to(lords_Sign,sign)
            if jupiter_Sign == sign or jup_aspects: # the object itself should be the same; means they are in the same sign
                sourcels.append(self.planets().jupiter())
            if mercury_Sign == sign or mer_aspects: # the object itself should be the same
                sourcels.append(self.planets().mercury())
            if lords_Sign == sign or lord_aspects:
                sourcels.append(lord)
            sss[sign] = sourcels
        return sss
