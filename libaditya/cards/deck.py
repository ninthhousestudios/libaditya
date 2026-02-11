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

from libaditya.cards import cards_constants as cardsc
from libaditya.cards.card import Card

class Deck:
    """
    could this also be a tarot deck, or would that be different?
    but tarot doesnt use planets, so it doesnt really have any astrology in it
    """

    def __init__(self, deck_type="52 playing cards"):
        self._deck_type = deck_type
        self._deck = self._init_Deck()

    def __iter__(self):
        return iter(self._deck)

    def __getitem__(self, card: str):
        return self._deck[card]

    def deck(self):
        return self._deck

    def index(self, card):
        return self._deck.index(card)

    def _init_Deck(self):
        """
        a dictionary of 52 k-v pairs: "Card": Card
        i.e., key-constructor
        """
        deck = {}

        for index,card in enumerate(cardsc.cards):
            deck[card] = Card(card,index)

        return deck
