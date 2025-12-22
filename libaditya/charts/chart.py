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

from libaditya.objects import EphContext, Planets, Cusps
from libaditya.charts import Rashi

class Chart:

    def __init__(self, context=EphContext()):
        self.context = context
        self._Rashi = Rashi(Planets(self.context), Cusps(self.context), self.context)

    def __str__(self):
        return f"{self.rashi()}" 

    def __repr__(self):
        return self.__str__()

    def rashi(self):
        return self._Rashi
