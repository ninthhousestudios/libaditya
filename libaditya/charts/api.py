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

from dataclasses import replace
from typing import Self

class API:
    """
    Mixin class for Chart api
    """

    def ayanamsa(self):
        return self.context.ayanamsa

    def ascendant(self):
        return self.rashi().lagna()

    def nakshatra(self):
        """
        this returns a Nakshatra object
        """
        return self.rashi().planets().moon().nakshatra()
