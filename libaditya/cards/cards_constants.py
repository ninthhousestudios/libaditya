# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC

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


spades_symbol = "♠"
hearts_symbol = "♥"
clubs_symbol = "♣"
diamonds_symbol = "♦"

symbols = {
    "S": spades_symbol,
    "H": hearts_symbol,
    "C": clubs_symbol,
    "D": diamonds_symbol,
}

planet_order = {
    "vedic": [
        "Base",
        "Sun",
        "Moon",
        "Mars",
        "Mercury",
        "Jupiter",
        "Venus",
        "Saturn",
        "Rahu",
        "Ketu",
        "Ecliptic",
        "Uranus",
        "Neptune",
        "Pluto",
    ],
    "solar_system": [
        "Base",
        "Sun",
        "Moon",
        "Mercury",
        "Venus",
        "Mars",
        "Jupiter",
        "Saturn",
        "Rahu",
        "Ketu",
        "Ecliptic",
        "Uranus",
        "Neptune",
        "Pluto",
    ],
}

cards = [
    "AH",
    "2H",
    "3H",
    "4H",
    "5H",
    "6H",
    "7H",
    "8H",
    "9H",
    "TH",
    "JH",
    "QH",
    "KH",
    "AC",
    "2C",
    "3C",
    "4C",
    "5C",
    "6C",
    "7C",
    "8C",
    "9C",
    "TC",
    "JC",
    "QC",
    "KC",
    "AD",
    "2D",
    "3D",
    "4D",
    "5D",
    "6D",
    "7D",
    "8D",
    "9D",
    "TD",
    "JD",
    "QD",
    "KD",
    "AS",
    "2S",
    "3S",
    "4S",
    "5S",
    "6S",
    "7S",
    "8S",
    "9S",
    "TS",
    "JS",
    "QS",
    "KS",
]

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
        "K": "King",
    },
    "suit": {"S": "Spades", "H": "Hearts", "C": "Clubs", "D": "Diamonds"},
}

hearts = list(range(0, 13))
clubs = list(range(13, 26))
diamonds = list(range(26, 39))
spades = list(range(39, 52))

# spades, hearts, clubs, diamonds
aces = [39, 0, 13, 26]
twos = [40, 1, 14, 27]
threes = [41, 2, 15, 28]
fours = [42, 3, 16, 29]
fives = [43, 4, 17, 30]
sixes = [44, 5, 18, 31]
sevens = [45, 6, 19, 32]
eights = [46, 7, 20, 33]
nines = [47, 8, 21, 34]
tens = [48, 9, 22, 35]
jacks = [49, 10, 23, 36]
queens = [50, 11, 24, 37]
kings = [51, 12, 25, 38]


# utility function for quadration
def topthree(quad):
    """Return the top three cards on the deck"""
    pile = []
    for i in range(3):
        pile.append(quad.pop(0))
    return pile


# this is the jack quadration, 1 through 52
# 1 is the Ace of Hearts, 52 is the King of Spades...we'll see how that turns out later
jackquad = list(range(0, 52))
# the first bc starting 01/01/2026 at sunrise is KS
# at next sunrise switches to QS
# etc.: goes in reverse order; but each month starts with a different card
birth_card_order = list(cards.__reversed__())
# first card of the month is as follows, starting with January
# then each day goes in order according to calendar day number, based on the savana day at the equator for a given longitude
# e.g., February 29 after sunrise will be
#
# every month starts two cards further down the sequence than the one before:
# Jan KS(0), Feb JS(2), Mar 9S(4) ... Dec 4D(22). November used to read "3D",
# index 23, the only break in that progression -- which shifted all 29 November
# birth cards by three and pushed November 30 past the end of the deck. "6D" is
# index 20, and it agrees with the published birth card chart (Nov 1 = 6D,
# Nov 30 = 3H).
first_card_of_the_month = [
    birth_card_order.index(card)
    for card in ["KS", "JS", "9S", "7S", "5S", "3S", "AS", "QD", "TD", "8D", "6D", "4D"]
]


def is_leap_year(year: int) -> bool:
    """
    proleptic Gregorian, which is the calendar the rest of the library computes
    in: every swe.julday/swe.revjul call here leaves cal at its GREG_CAL
    default, pre-1582 dates included. a Julian rule here would disagree with
    them -- it would call 1500 long, while swe.revjul rolls Gregorian 1500-02-29
    straight to March 1.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_the_month(month: int, year: int | None = None) -> int:
    """
    month is 1-indexed to january

    year decides February. omit it and February is 29, the length the CARD TABLE
    uses -- the 29th has its own card (9C) that is simply only reachable in a
    leap year. pass a year and February is that year's real length, which is
    what a caller stepping back to "the last day of the previous month" needs:
    the day before March 1 1990 is the 28th, not a 29th that never happened.
    """
    if not 1 <= month <= 12:
        raise ValueError(f"month must be 1-12, got {month!r}")
    if month == 2:
        return 29 if year is None or is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31
