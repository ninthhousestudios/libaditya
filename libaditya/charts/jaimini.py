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

from libaditya.objects import EphContext
from libaditya.charts import Chart

class Jaimini(Chart):

    def __init__(self,  context=EphContext()):
        super().__init__(context)
        self.ak = self.atmakaraka # so you can call chart.jaimini().ak()

    def pada(self, amsha=1):
        if amsha == 1:
            return self.rashi().pada()
        return self.varga(amsha).pada()

    def upapada(self, amsha=1):
        if amsha == 1:
            return self.rashi().upapada()
        return self.varga(amsha).upapada()

    def padas(self, amsha=1):
        if amsha == 1:
            return self.rashi().padas()
        return self.varga(amsha).padas()

    def karakas(self):
        """
        get the Jaimini karakas for this Chart/Jaimini
        """
        return self.rashi().planets().jaimini_karakas()

    def atmakaraka(self):
        return self.karakas()[0]

    def svamsha(self):
        """
        returns the Sign that the AK is in in the navamsha
        """
        return self.varga(9).signs()[self.varga(9).where_is(self.atmakaraka()).sign()]

    def karakamsha(self):
        return self.rashi().signs()[self.atmakaraka().sign()]

    def darakaraka(self):
        # there are 7 karakas, python is 0-indexed, so 6 is the 7th starting from 0
        return self.karakas()[6]

    def first_strength(self, amsha=1):
        if amsha == 1:
            return self.rashi().jaimini_first_strength()
        else:
            return self.varga(amsha).jaimini_first_strength()

    def second_strength(self, amsha=1):
        if amsha == 1:
            return self.rashi().jaimini_second_strength()
        else:
            return self.varga(amsha).jaimini_second_strength()

    def argala(self):
        """
        determine the argala in this chart
        this means combined argala to 1st and 7th houses in the Rashi chart

        the deepest python function for argala will be able to do it to any sign in any varga
        """
        return self.rashi().rashi_argala()
