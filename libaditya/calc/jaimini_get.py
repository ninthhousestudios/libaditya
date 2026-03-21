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



class Gets:
    """
    factor-s are all signs

    it is the planets that are conjunct or aspect that provide the effect
    but that is interpretive, what effect and to what extent

    "gets" are just about calculations

    to do the interpretation, we need to know which planets are conjunct or aspecting the ak,
    which sign the ak is in in various vargas, etc.

    that is what we are doing here.
    """

    karakamshas = {
        # AK, i.e.,s the sign of the AK
        "factor": ["AK"],
        "vargas": ["9","1","7"]
    }

    spirituality = {
        "factor": ["12 away AK"],
        "vargas": ["9","24","1"]
    }

    mundane_deity = {
        "factor": ["6 away AmK"],
        "vargas": ["30","9","1"]
    }

    home = {
        "factor": ["4 away AK"],
        "vargas": ["4","16","1"]
    }

    dharma = {
        "factor": ["9 away AK"],
        # 12 for seeing if parental influence supports innate dharma
        "vargas": ["9","1","12"]
    }

    farmer = {
        "factor": ["3", "6", "9"],
        # others?
        "vargas": ["1"]
    }

    # this is interpretive actually
    # this is will be covered by "karamashas" near the top
#    adultery = {
#        "factor": ["AK in Mars or AK in Venus"],
#        "vargas": ["9","7","1"]
#    }

    spouse = {
        "factor": ["7 away AK"],
        "vargas": ["9","7","1"]
    }

    might = {
        "factor": ["3 away AK"],
        "vargas": ["9","3","1"]
    }

    conjurer = {
        "factor": ["5 away AK", "9 away AK"],
        "vargas": ["9","1"]
    }

    capability = {
        # 1.2.40-42: how capable/successful a person is at their livelihood
        "factor": ["10 away AK"],
        "vargas": ["9","1","10"]
    }

    disease_foundation = {
        # 1.2.88-90: chronic/glandular/skin disease (vitiligo, leprosy)
        # same factor as home but different vargas — D30 changes the reading
        "factor": ["4 away AK"],
        "vargas": ["9","30","1"]
    }

    disease_vitality = {
        # 1.2.91-95: bodily wasting, boils, water disease, poison
        "factor": ["AK", "5 away AK"],
        "vargas": ["9","30","1"]
    }

    authorship = {
        # 1.2.102-104: writing ability (Moon+Jupiter = author, etc.)
        "factor": ["AK", "5 away AK"],
        "vargas": ["9","1","10"]
    }

    intelligence = {
        # 1.2.105-114: type of intelligence (poet, logician, mathematician, etc.)
        "factor": ["AK", "5 away AK"],
        "vargas": ["9","24","1"]
    }

    speech = {
        # 1.2.116-118: secondary skills; Ketu+malefic = speech problems
        "factor": ["2 away AK"],
        "vargas": ["9","1"]
    }

    # dont forget const.multi_vargas

    # karaka abbreviations in jaimini_karakas() order
    KARAKA_ORDER = ["AK", "AmK", "BK", "MK", "PiK", "GK", "DK"]


class JaiminiGet:
    """
    a inheritor for calc.Rashi
    defines functions that get certain sets of planets

    these are functions that may use any varga, so they are in the Rashi, which has access to all vargas

    functions that work on the vargas themselves are defined in calc.Varga/calc.Jaimini
    """

    # default varga overrides: when a Gets spec says "24", use -240 (siddhamsha) by default
    DEFAULT_VARGA_OVERRIDES = {"24": "-240"}

    def _parse_factor(self, factor_str):
        """
        parse a factor string into (offset, karaka_abbrev) or (cusp_number, None)

        "12 away AK"  -> (12, "AK")
        "AK"          -> (0, "AK")
        "6 away AmK"  -> (6, "AmK")
        "3"           -> (3, None)      # raw cusp number
        """
        parts = factor_str.split()
        if len(parts) == 3 and parts[1] == "away":
            return int(parts[0]), parts[2]
        elif factor_str in Gets.KARAKA_ORDER:
            return 0, factor_str
        else:
            return int(factor_str), None

    def _resolve_vargas(self, spec_vargas, varga_overrides=None):
        """
        apply varga overrides to the spec's varga list

        varga_overrides is a dict like {"24": "-240"} that replaces
        varga numbers with alternate divisional chart variants
        """
        overrides = dict(self.DEFAULT_VARGA_OVERRIDES)
        if varga_overrides:
            overrides.update(varga_overrides)
        return [overrides.get(v, v) for v in spec_vargas]

    def _get_influences(self, varga, sign):
        """
        given a varga and a Sign, return the conjunction and aspect planets
        """
        aspecting = varga.rashi_aspects_given_to(sign)
        aspecting = [this_one.grahas() for this_one in aspecting]
        conjunction = [p.jaimini_info() for p in sign.grahas()]
        aspect_list = []
        for sign_planets in aspecting:
            aspect_list.append([p.jaimini_info() for p in sign_planets])
        return {"conjunction": conjunction, "aspecting": aspect_list}

    def _find_factor_sign(self, varga, factor_str, karakas):
        """
        given a varga, a factor string, and the karaka list,
        return the Sign that the factor points to
        """
        offset, karaka_abbrev = self._parse_factor(factor_str)

        if karaka_abbrev is None:
            # raw cusp number
            cusp_sign_num = varga.cusps()[offset].sign()
            return varga.signs()[cusp_sign_num]

        karaka_index = Gets.KARAKA_ORDER.index(karaka_abbrev)
        karaka = karakas[karaka_index]
        karaka_sign = varga.where_is(karaka.identity())

        if offset == 0:
            return karaka_sign

        direction = 1 if karaka_sign.sign() % 2 == 1 else -1
        return varga.signs()[karaka_sign.astrological_signs_forward(offset * direction)]

    def jaimini_get(self, spec, varga_overrides=None):
        """
        general method to get influences for any Gets spec

        spec is a dict from Gets, e.g. Gets.spirituality, Gets.karakamshas
        varga_overrides is an optional dict like {"24": "-240"} to choose
        alternate varga variants

        returns a dictionary that can be converted to toml
        """
        factors = spec["factor"]
        vargas = self._resolve_vargas(spec["vargas"], varga_overrides)
        karakas = self.planets().jaimini_karakas()

        ret = {
            "aspect_type": self.context.rashi_aspects,
        }

        for factor_str in factors:
            factor_ret = {}
            for amsha in vargas:
                varga = self.master.varga(int(amsha))
                sign = self._find_factor_sign(varga, factor_str, karakas)
                factor_ret[amsha] = self._get_influences(varga, sign)
            ret[factor_str] = factor_ret

        return ret

    def get_spiritual_planets(self, d24=-240):
        """get spiritual planets using the general get() method"""
        return self.jaimini_get(Gets.spirituality, varga_overrides={"24": str(d24)})

