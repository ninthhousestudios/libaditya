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
from libaditya.cards.deck import Deck


class Spread:
    """
    initialize a Spread object
    the most important argument is spread_list, which is the list of numbers presenting the cards of the spread
    """

    def __init__(self, spread_list, order="vedic", deck=Deck()):
        self._list = spread_list
        self._deck = deck
        self._order = order
        self._spread = self._init_Spread()

    def __iter__(self):
        return iter(self._spread)

    def __getitem__(self, key):
        if isinstance(key,str):
            return self._spread[key]
        else:
            # get the planet key as a string from the correct planet order
            # key here is an int, corresponding to the desired card
            # 0 for the base card, 1 for sun, 2 for moon, etc.
            return self._spread[cardsc.planet_order[self._order][key]]

    def deck(self):
        return self._deck

    def _init_Spread(self):
        """
        initialize the Spread, self._spread
        a dictionary, "Planet": Card
        also through __getitem__, Spread()[int] where int is the planet number appropriate to the system
        """
        spread = {}
        for spread_position,planet_key in enumerate(cardsc.planet_order[self._order]):
            # self._list = spread_list is a list of 14 cards in the proper positions starting from 0, the base card
            # base card is list[0], sun is list[1], moon is list[2]
            # for vedic mars is list[3], for solar_system mercury is list[3], etc.
            # self._list[spread_position] as the int representation of the card at that position
            # put this int into cardsc.cards to get the string version, e.g., "KD"
            spread[planet_key] = self.deck()[cardsc.cards[self._list[spread_position]]]
            # with this above, we should be able to iterate over Spread regardless of the system
        return spread

    def richDrawing(self):
        spread = Table(box=box.SIMPLE)

        spread.add_column(" ",justify="center",style="white")
        spread.add_column(" ",justify="center",style="white")
        spread.add_column(" ",justify="center",style="white")
        spread.add_column(" ",justify="center",style="white")
        spread.add_column(" ",justify="center",style="white")
        spread.add_column(" ",justify="center",style="white")
        spread.add_column(" ",justify="center",style="white")

        spread.add_row(" "," "," ",self[0].drawing()," "," "," ")
        spread.add_row(self[7].drawing(),self[6].drawing(),self[5].drawing(),self[4].drawing(),self[3].drawing(),self[2].drawing(),self[1].drawing())
        spread.add_row(" "," ",self[9].drawing()," ",self[8].drawing()," "," ")
        spread.add_row(" "," "," ",self[10].drawing()," "," "," ")
        spread.add_row(" "," ",self[13].drawing(),self[12].drawing(),self[11].drawing()," "," ")

        return spread
