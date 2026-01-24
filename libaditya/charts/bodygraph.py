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

from libaditya.objects import Planets
from libaditya.hd import calc as hdcalc

class Bodygraph:
    """
    by calculation, a bodygraph is simply a set of 
    """

    def __init__(self, context):
        self.context = context
        self._conscious_planets = Planets(self.context)
        self._unconscious_context = hdcalc.unconscious_context(self.context)
        self._unconscious_planets = Planets(self._unconscious_context)
        self._dream_context = hdcalc.dream_context(self.context)
        self._dream_planets = Planets(self._dream_context)

    def conscious_planets(self):
        return self._conscious_planets.hd_planets()

    def unconscious_planets(self):
        return self._unconscious_planets.hd_planets()

    def dream_planets(self):
        """
        these are the unconscious dream planets, since the conscious ones for the dreamgraph
        are the same as the conscious ones for the bodygraph
        """
        return self._dream_planets.hd_planets()

    def _new_bodygraph(self, **kwargs):
        return Bodygraph(context=replace(self.context,**kwargs))
