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
    "factor": ["3 with malefic", "6 with malefic", "esp: 9 with Jupiter"],
    # others?
    "vargas": ["1"]
}

adultery = {
    "factor": ["AK in Mars or AK in Venus"],
    "vargas": ["9","7","1"]
}

spouse = {
    "factor": ["7 away AK"],
    "vargas": ["9","7","1"]
}

might = {
    "factor": ["3 away AK"],
    "vargas": ["9","3","1"]
}

conjurer = {
    "factor": ["5 away AK and 9 away AK"],
    "vargas": ["9","1"]
}

# dont forget const.multi_vargas

class JaiminiGet:
    """
    a inheritor for calc.Rashi
    defines functions that get certain sets of planets

    these are functions that may use any varga, so they are in the Rashi, which has access to all vargas

    functions that work on the vargas themselves are defined in calc.Varga/calc.Jaimini
    """

    def get_spiritual_planets(self,d24=-240):
        """
        get a dictionary of the spiritual planets

        varga -240 is siddhamsha, where even signs start with cancer and go in reverse order

        returns a dictionary that can be converted to toml
        """
        vargas = ["1","9",f"{d24}"]
        ret = {
            "description": "12 from AK; 1,9,24",
            "aspect_type": self.context.rashi_aspects,
            vargas[0]: {
                "conjunction": [],
                "aspecting": []
            },
            vargas[1]: {
                "conjunction": [],
                "aspecting": []
            },
            vargas[2]: {
                "conjunction": [],
                "aspecting": []
            }
        }
        # for judging personal deity, want 12th from svamsha in d9, d24s, d1
        # get 12th from svamsha in d9,d24,d1
        ak = self.planets().jaimini_karakas()[0]

        for amsha in vargas:
            varga = self.master.varga(int(amsha))
            aksign = varga.where_is(ak.identity())
            # "sign" determines the direction we count in, 1 is forward, -1 is reverse
            direction = 1 if aksign.sign()%2 == 1 else -1
            twelfth_from_ak = varga.signs()[aksign.astrological_signs_forward(12*direction)]
            aspecting = varga.rashi_aspects_given_to(twelfth_from_ak)
            aspecting = [this_one.grahas() for this_one in aspecting]
            ret[amsha]["conjunction"].append([p.jaimini_info() for p in twelfth_from_ak.grahas()])
            for sign in aspecting:
                ret[amsha]["aspecting"].append([p.jaimini_info() for p in sign])

        return ret

