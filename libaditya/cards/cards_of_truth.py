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

from libaditya.objects import EphContext, Sun

from libaditya.cards import cards_constants as cardsc
from .cot import CoT
from libaditya.cards.deck import Deck

class CardsOfTruth(CoT):

    def __init__(self, context=EphContext(), master=None):
        self.context = context
        self._master = master
        self._birth_card: str = self._get_birth_card()
        self._birth_spread: self.Spread = self._get_birth_spread()

    def master(self):
        return self._master

    def birth_card(self):
        return self._birth_card

    def birth_spread(self):
        """
        self._birth_spread is the list of card integers of that spread
        """
        return self.Spread(self._birth_spread, self.context.cot_planet_order)

    def _get_birth_card(self):
        """
        find the birth card
        first, find the time the sunrises at longitude of the persons place of birth, but on the equator
        """
        sunrise_location = self.context.location.nearest_equatorial_crossing()
        sunrise_time = Sun(EphContext(timeJD=self.context.timeJD.midnightJD(),location=sunrise_location)).rise()
        if self.context.timeJD.jd_number() >= sunrise_time.jd_number():
            # after sunrise on this day
            # so use card associated with this calendar day 
            card_day = [self.context.timeJD.usrmonth(),self.context.timeJD.usrday()]
        else:
            # before sunrise on this day
            # so use card associated with previous calendar day
            # so we go back, but need to make everything switches back properly, i.e., the month or year
            month = self.context.timeJD.usrmonth()
            day = self.context.timeJD.usrday()-1
            if day != 0:
                card_day = [month,day]
            else:
                # we need to go back to the last day of the previous month
                # i.e., the last card, but not necessarily in the normal sequence 
                # in python, list()[-1] is the last element of the list
                # so if month is jaunary=element0, then month-1=december,element11
                # then we need to know how many days are in that month
                card_day = [month-1,cardsc.days_in_the_month(month-1)]
        # minus 1 since months are 1-12 but python is 0-indexed
        start_card = cardsc.first_card_of_the_month[(card_day[0]-1)]
        # go forward the number of days from that card to find the birth card
        birth_card = cardsc.birth_card_order[start_card+(card_day[1]-1)]
        return birth_card

    def _get_birth_spread(self):
        birth_card = self.birth_card()
        return self.get_birthspread_from_quadration(birth_card)

    def deck(self):
        return self._deck

    def year_spread(self, year):
        """
        get a year spread for age year

        add way of doing default argument where it uses current age
        """
        return self.get_birthspread_from_quadration(self.birth_card(),self.quadraten(cardsc.jackquad,year+1))

    
    class Spread:
        """
        initialize a Spread object
        the most important argument is spread_list, which is the list of numbers presenting the cards of the spread
        """

        def __init__(self, spread_list, order="vedic"):
            self._list = spread_list
            self._deck = Deck()
            self._order = order
            self._spread = self._init_Spread()
            self._planets = self._init_Planets()

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

        def spread(self):
            return self._spread

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

        def _init_Planets(self):
            """
            this function gets the necessary planetary information for a birth spread
            it initializes those Planet-s into Spread
            it also adds those Planet-s to their proper Card in the Spread
            so then we will have Spread().planets() and Spread()["Sun"] to see which Planet-s are in the Sun card
            """
            pass

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

        def print_rich(self):
            from rich.console import Console
            console.print(self.richDrawing())
