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

from libaditya import constants as const

from libaditya.objects import Sun, Moon, EphContext

class Panchanga:

    def __init__(self, context=EphContext()):
        self.context = context
        self._sun = Sun(self.context)
        self._moon = Moon(self.context)
        self._tithi_number, self._tithi_elapsed, self._tithi_remaining = self.init_tithi()


    def init_tithi(self):
        traw = ((self._moon.longitude() - self._sun.longitude()) % 360) / 12
        remainder = traw % 1  # remainder shows how much has elapsed
        elapsed = remainder * 12  # degrees elapsed
        remaining = 12 - elapsed  # degrees remaining
        return (int(traw)+1, elapsed, remaining)

    def tithi_number(self):
        return self.tithi_number

    #def tithi
