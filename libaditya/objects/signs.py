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

from libaditya import constants as const

from .planets import Planets
from .cusps import Cusps
from .context import EphContext, Circle

class Sign:

    def __init__(self, index, planets, cusps, context):
        self.context = context
        self._planets = planets
        self._cusps = cusps
        self._sign_index = index
        self._sign_name = self.context.names.sign_names[self.sign_index()]

    def __str__(self):
        header = ""
        header += f"\n{self.sign_name()}\n"
        output = PrettyTable()
        output.field_names = ["Object", "In Sign Longitude", "Real Longitude"]
        output.align["Object"] = "l"
        output.align["In Sign Longitude"] = "r"
        output.align["Real Longitude"] = "r"

        for p in self._planets:
            output.add_row([p.name(),p.in_sign_longitude(),p.raw_longitude()])
        for c in self._cusps:
            output.add_row([c.name(),c.in_sign_longitude(),c.raw_longitude()])

        ret = output.get_string(fields=["Object", "In Sign Longitude", "Real Longitude"])

        return header + ret

    def __repr__(self):
        name = ""
        name += f"{self.sign_index()=} {self.sign_name()=}\n"
        for p in self._planets:
            name += f"{p}"
        for c in self._cusps:
            name += f"{c}"
        name += "\n"
        return name

    def sign_index(self):
        return self._sign_index

    def sign_name(self):
        return self._sign_name

class Signs:
    
    def __init__(self, planets=Planets(), cusps=Cusps(), context=EphContext()):
        self.context = context
        self._planets = planets
        self._cusps = cusps
        self.circle = self.context.circle
        self._signs = self.init_Signs()
        self.sysflgstr = const.sysflgstr(context.sysflg)

    def __iter__(self):
        return iter(self._signs)

    def __getitem__(self,n):
        return self._signs[n]

    def __str__(self):
        ret = ""
        ret += self.mkheader()

        for s in self._signs:
            ret += f"{s}"

        return ret

    def init_Signs(self):
        """
        initialize signs
        first go through all the planets and cusps
        and put them in the right holding place in "signs", then
        initialize a list of Sign classes
        """
        stmp = [[[],[]] for x in range(0,12)]
        # do planets first, inner index = 0
        inner_index = 0
        for p in self._planets:
            stmp[p.sign_index()][inner_index].append(p)
        # now do cusps
        inner_index = 1
        for c in self._cusps:
            stmp[c.sign_index()][inner_index].append(c)
        signs=[]
        for n, sign in enumerate(stmp):
            signs.append(Sign(n,planets=sign[0],cusps=sign[1],context=self.context))
        return signs

    def mkheader(self):
        header = f"{self.sysflgstr} coordinates\n"
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
        if self.context.sysflg == swe.FLG_TOPOCTR:
            header += f"{self.context.location}"
        header += f"{self.context.timeJD}\n"
        return header

