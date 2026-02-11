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


class Deck:
    cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH',
                   'JH', 'QH', 'KH', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC',
                   'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD',
                   'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS']

    hearts = list(range(0,13))
    clubs = list(range(13,26))
    diamonds = list(range(26,39))
    spades = list(range(39,52))

    # spades, hearts, clubs, diamonds
    aces = [39,0,13,26]
    twos = [40,1,14,27]
    threes = [41,2,15,28]
    fours = [42,3,16,29]
    fives = [43,4,17,30]
    sixes = [44,5,18,31]
    sevens = [45,6,19,32]
    eights = [46,7,20,33]
    nines = [47,8,21,34]
    tens = [48,9,22,35]
    jacks = [49,10,23,36]
    queens = [50,11,24,37]
    kings = [51,12,25,38]

    def __init__(self, type="52 playing cards"):
        self._deck = self.cards

    def __iter__(self):
        return iter(self._deck)

    def __getitem__(self, n):
        return self._deck[n]

    def deck(self):
        return self._deck

    def index(self, card):
        return self._deck.index(card)
