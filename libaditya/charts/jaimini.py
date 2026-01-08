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

from libaditya.objects import EphContext
from libaditya.charts import Chart

class Jaimini(Chart):

    def __init__(self,  context=EphContext()):
        super().__init__(context)

    def pada(self, amsha=1):
        if amsha == 1:
            return self.rashi().pada()
        return self.get_varga(amsha).pada()

    def upapada(self, amsha=1):
        if amsha == 1:
            return self.rashi().upapada()
        return self.get_varga(amsha).upapada()

    def padas(self, amsha=1):
        if amsha == 1:
            return self.rashi().padas()
        return self.get_varga(amsha).padas()

    def karakas(self):
        """
        get the Jaimini karakas for this Chart/Jaimini
        """
        return self.rashi().planets().jaimini_karakas()

    def first_strength(self, amsha=1):
        if amsha == 1:
            return self.rashi().jaimini_first_strength()
        else:
            return self.get_varga(amsha).jaimini_first_strength()

    def second_strength(self, amsha=1):
        if amsha == 1:
            return self.rashi().jaimini_second_strength()
        else:
            return self.get_varga(amsha).jaimini_second_strength()

    def argala(self):
        """
        determine the argala in this chart
        this means combined argala to 1st and 7th houses in the Rashi chart

        the deepest python function for argala will be able to do it to any sign in any varga
        """
        return self.rashi().argala()
