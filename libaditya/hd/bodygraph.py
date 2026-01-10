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
from dataclasses import replace
from typing import Self

from libaditya.objects import EphContext, Planets

from .context import HDContext

class Bodygraph:
    """
    by calculation, a bodygraph is simply a set of 
    """

    def __init__(self, context=EphContext(hdcontext=HDContext())):
        self.context = context
        self._conscious_planets = Planets(self.context)
        self._design_JD = JulianDay()
        self._unconscious_planets = Planets()
