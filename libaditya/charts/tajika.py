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

class Tajika(Chart):

    def __init__(self, context=EphContext()):
        super().__init__(context)

    def vargas(self) -> {int: "varga"}:
        """
        return a dictionary of tajika parivritti vargas
        1-12 in a dictionary {int: Sign}
        """
        vargas = {}
        for n in range(1,13):
            vargas[n] = self.varga(n)
        return vargas
