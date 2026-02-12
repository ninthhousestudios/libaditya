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
import libaditya.constants as const
from libaditya.hd import calc as hdcalc
from libaditya.hd import constants as hdc

from libaditya.draw.draw_bodygraph import DrawBodyGraph


class Bodygraph(DrawBodyGraph):
    """
    by calculation, a bodygraph is simply a set of planets
    the conscious planets are the birth planets, in this order:
    Sun, Earth, Moon, Rahu, Ketu, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Chiron (doesn't activate gate)
    the unconscious planets are the planets at the time when the Sun was 88 degrees before the birth placement
    the dream planets are the planets at the time the Moon was 88 degrees before the birth placement

    this can draw a bodygraph

    use Bodygraph().draw_svg(outfile="(optional; default is {Bodygraph().context.name}.svg)")
    """

    def __init__(self, context):
        self.context = context
        self._conscious_planets = Planets(self.context)
        self._unconscious_context = hdcalc.unconscious_context(self.context)
        self._unconscious_planets = Planets(self._unconscious_context)
        self._dream_context = hdcalc.dream_context(self.context)
        self._dream_planets = Planets(self._dream_context)

    def conscious_planets(self):
        return self._conscious_planets

    def unconscious_planets(self):
        return self._unconscious_planets
    
    def planets(self):
        return self.conscious_planets().hd_planets() + self.unconscious_planets().hd_planets()

    def conscious_gates(self,chiron=True):
        return self.conscious_planets().gates(chiron)

    def unconscious_gates(self,chiron=True):
        return self.unconscious_planets().gates()

    def all_gates(self,chiron=False):
        """
        get all_gates that should be activated in the bodygraph
        """
        return self.conscious_gates(chiron) + self.unconscious_gates(chiron)

    def dream_planets(self):
        """
        these are the unconscious dream planets, since the conscious ones for the dreamgraph
        are the same as the conscious ones for the bodygraph
        """
        return self._dream_planets

    def _new_bodygraph(self, **kwargs):
        return Bodygraph(context=replace(self.context,**kwargs))

