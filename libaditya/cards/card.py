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

from rich import box
from rich.table import Table
from rich.console import Console

from libaditya.cards import cards_constants as cardsc

class Card:

    def __init__(self, card, index, planet="", deck_type="52 playing card"):
        self._card = card
        self._deck_type = deck_type
        self._index = index
        self._planet = planet
        self.attributes = {
            "planets": [],
            "cusps": []
        }
        self._drawing = self.richDrawing()

    def set_attribute(self,attrs):
        """
        attrs is a tuple ("attribute",value)
        add all of these to self.attributes
        attritube is a string that will be a dictionary key for value
        """
        key,value=attrs
        self.attributes[key] = value

    def card(self):
        return self._card

    def index(self):
        return self._index

    def name(self):
        return cardsc.name["number"][self.card()[0]] + " of " + cardsc.name["suit"][self.card()[1]]

    def symbol(self):
        return f"{self.card()[0]}{cardsc.symbols[self.card()[1]]}"

    def planet(self):
        return self._planet

    def planets(self):
        return self.attributes["planets"]

    def cusps(self):
        return self.attributes["cusps"]

    def richDrawing(self):
        """
        return a rich.Table object representing this card
        """
        card = Table(box=box.ROUNDED)
        color = "red" if (self.card()[1] == "H" or self.card()[1] == "D") else "white"
        card.add_column(self.planet(),justify="center",style="white")
        card.add_row(self.symbol(),style=color)
        # do more, like add planets
        return card

    def drawing(self):
        return self._drawing

    def draw(self):
        console = Console()
        console.print(self.drawing())
