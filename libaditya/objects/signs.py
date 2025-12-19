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

    def __iter__(self):
        return iter(self._signs)

    def __getitem__(self,n):
        return self._signs[n]

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
        print(f"init_Signs {type(self._planets)=}")
        for p in self._planets:
            stmp[p.sign_index()][inner_index].append(p)
        # now do cusps
        inner_index = 1
        for c in self._cusps:
            stmp[c.sign_index()][inner_index].append(c)
        signs=[]
        for n, sign in enumerate(stmp):
            signs.append(Sign(n,planets=sign[0],cusps=sign[0],context=self.context))
        return signs
