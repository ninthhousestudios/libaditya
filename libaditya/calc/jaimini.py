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

from functools import cmp_to_key

from more_itertools import collapse

from libaditya import utils

from libaditya.objects import Planet, Planets, Sign

class Jaimini:
    """
    this is calc.Jaimini, it inherits unto calc.Varga

    it is really a Varga, even though Varga inherits from here

    these are calculations that can happen on any varga, in that varga

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


    def _compare_strength(self, sign1, sign2, kn_rao=False) -> int:
        """
        compare two signs by Jaimini first source of strength
        returns 1 if sign1 is stronger, -1 if sign2 is stronger, 0 if equal

        8 tiebreaker levels per the Jaimini sutras:
        0: planet count in sign
        1: highest dignity among occupying planets (sorted comparison)
        2: modality (dual > fixed > movable)
        3: planet count in the lord's sign
        4: highest dignity in the lord's sign
        5: modality of the lord's sign
        6: distance from sign to its lord (greater distance wins)
        7: final tiebreaker (standard: higher rashi number; KN Rao: lord's degree in sign)
        """
        dignities = self.dignities()

        # Level 0: planet count in sign
        c1, c2 = sign1.how_many_karakas(), sign2.how_many_karakas()
        if c1 != c2:
            return 1 if c1 > c2 else -1

        # Level 1: dignity comparison among occupying planets
        result = utils.compare_signs_dignities(sign1, sign2, dignities)
        if result == 1: return 1
        if result == 2: return -1

        # Level 2: modality
        result = utils.compare_signs_modalities(sign1, sign2)
        if result == 1: return 1
        if result == 2: return -1

        # Levels 3-5: same three checks on the lord's rashi
        lord1 = self.planets()[sign1.lord()]
        lord2 = self.planets()[sign2.lord()]
        lord1_rashi = self.signs().where_is(sign1.lord())
        lord2_rashi = self.signs().where_is(sign2.lord())

        # Level 3: planet count in lord's sign
        c1, c2 = lord1_rashi.how_many_karakas(), lord2_rashi.how_many_karakas()
        if c1 != c2:
            return 1 if c1 > c2 else -1

        # Level 4: dignity comparison in lord's sign
        result = utils.compare_signs_dignities(lord1_rashi, lord2_rashi, dignities)
        if result == 1: return 1
        if result == 2: return -1

        # Level 5: modality of lord's sign
        result = utils.compare_signs_modalities(lord1_rashi, lord2_rashi)
        if result == 1: return 1
        if result == 2: return -1

        # Level 6: distance from sign to its lord (greater distance wins)
        d1 = sign1.astrological_signs_apart(lord1.sign())
        d2 = sign2.astrological_signs_apart(lord2.sign())
        if d1 != d2:
            return 1 if d1 > d2 else -1

        # Level 7: final tiebreaker
        if kn_rao:
            deg1 = lord1.real_in_sign_longitude()
            deg2 = lord2.real_in_sign_longitude()
            if deg1 != deg2:
                return 1 if deg1 > deg2 else -1
            return 0
        else:
            # standard: higher rashi number wins
            if sign1.sign() != sign2.sign():
                return 1 if sign1.sign() > sign2.sign() else -1
            return 0

    def jaimini_first_strength(self, kn_rao=False) -> [Sign]:
        """
        calculate Jaiminis first source of strength for all signs
        return a list of Sign classes from strongest (index 0) to weakest (index 11)

        kn_rao=True uses KN Rao's tiebreaker at level 7 (lord's degree in sign)
        kn_rao=False (default) uses standard tiebreaker (higher rashi number wins)
        """
        signs = list(self.signs())
        signs.sort(key=cmp_to_key(lambda a, b: self._compare_strength(a, b, kn_rao)), reverse=True)
        return signs

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

    def jaimini_third_strength(self) -> {Sign: (int, str)}:
        """
        calculate Jaiminis third source of strength for all signs
        classifies each sign by the distance from sign to its lord:
        Kendra (distance % 3 == 1) = 2 (strong)
        Panapara (distance % 3 == 2) = 1 (moderate)
        Apoklima (distance % 3 == 0) = 0 (weak)

        return a dictionary of Sign: (value, category_name)
        """
        categories = {1: (2, "Kendra"), 2: (1, "Panapara"), 0: (0, "Apoklima")}
        ret = {}
        for sign in self.signs():
            lord = self.planets()[sign.lord()]
            distance = sign.astrological_signs_apart(lord.sign())
            ret[sign] = categories[distance % 3]
        return ret
