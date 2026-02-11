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


spades_symbol="♠"
hearts_symbol="♥"
clubs_symbol="♣"
diamonds_symbol="♦"

symbols = {
    "S": spades_symbol,
    "H": hearts_symbol,
    "C": clubs_symbol,
    "D": diamonds_symbol
}

planet_order = {
    "vedic": ["Base","Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Rahu","Ketu","Ecliptic","Uranus","Neptune","Pluto"],
    "solar_system": ["Base","Sun","Moon","Mercury","Venus","Mars","Jupiter","Saturn","Rahu","Ketu","Ecliptic","Uranus","Neptune","Pluto"]
}

cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH',
               'JH', 'QH', 'KH', 'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC',
               'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD',
               'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS']

name = {
    "number": {
        "A": "Ace",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "T": "Ten",
        "J": "Jack",
        "Q": "Queen",
        "K": "King"
    },
    "suit": {
        "S": "Spades",
        "H": "Hearts",
        "C": "Clubs",
        "D": "Diamonds"
    }
}

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

# utility function for quadration
def topthree(quad):
    """Return the top three cards on the deck"""
    pile = []
    for i in range(3):
        pile.append(quad.pop(0))
    return pile

# this is the jack quadration, 1 through 52
# 1 is the Ace of Hearts, 52 is the King of Spades...we'll see how that turns out later
jackquad = list(range(0,52))
# the first bc starting 01/01/2026 at sunrise is KS
# at next sunrise switches to QS
# etc.: goes in reverse order; but each month starts with a different card
birth_card_order = list(cards.__reversed__())
# first card of the month is as follows, starting with January
# then each day goes in order according to calendar day number, based on the savana day at the equator for a given longitude
# e.g., February 29 after sunrise will be
first_card_of_the_month = [birth_card_order.index(card) for card in ["KS","JS","9S","7S","5S","3S","AS","QD","TD","8D","3D","4D"]]

def days_in_the_month(month: int):
    """
    month is 0-indexed to january
    for cards of truth, February has 29 days...so that "card" only gets that turn to play whenever it is feb.29, right?
    """
    match match:
        case 1 | 3 | 5 | 7 | 8 | 10:
            return 31
        case 4 | 6 | 9 | 11 | 12:
            return 30
        case 2:
            return 20
