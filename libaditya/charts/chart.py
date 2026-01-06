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
from typing import Self

from libaditya.objects import EphContext, Planets, Cusps
from libaditya.charts import Rashi, Varga

class Chart:

    def __init__(self, context=EphContext()):
        self.context = context
        self._Rashi = Rashi(Planets(self.context), Cusps(self.context), self.context, self)

    def __str__(self):
        return f"{self.rashi()}" 

    def __repr__(self):
        return self.__str__()

    def rashi(self):
        return self._Rashi

    def get_varga(self, amsha: int):
        """
        use Chart.rashi() for the rashi() chart
        you must pass an integer to get_varga
        Chart.get_varga(1) return something that has the same Planets and Cusps as the Rashi() chart, but
        is different in some respects...not sure if they should be or not, e.g., wrt to argala
        """
        return Varga(amsha,self.rashi().planets(),self.rashi().cusps(),self.context,self)

    def jaimini(self):
        from libaditya.charts import Jaimini
        return Jaimini(context=self.context)
