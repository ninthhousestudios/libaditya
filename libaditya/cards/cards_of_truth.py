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

from libaditya import utils
from libaditya.objects import EphContext, Sun, JulianDay

from libaditya.cards import cards_constants as cardsc
from libaditya.cards.deck import Deck
from .cot import CoT

class CardsOfTruth(CoT):

    def __init__(self, context=EphContext(), master=None):
        self.context = context
        self.master = master
        self._birth_card: str = self._get_birth_card()
        self._birth_spread: self.Spread = self._get_birth_spread()

    def birth_card(self):
        return self._birth_card

    def birth_spread(self):
        """
        self._birth_spread is the list of card integers of that spread
        """
        return self.Spread(self._birth_spread, self.master, self.context.cot_planet_order)

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

    def year_spread(self, year=None):
        """
        get a year spread for age year

        add way of doing default argument where it uses current age

        if None, use current age, or try
        not sure how well it actually works
        """
        if year == None:
            # find the persons current age
            now=JulianDay("now")
            # age is a decimal in years
            age = self.context.timeJD.age(now.jd_number())
            year = int(utils.dec2ymd(age).split()[0])-1
        year_spread_list = self.get_birthspread_from_quadration(self.birth_card(),self.quadraten(cardsc.jackquad,year+1))
        # change planets to self.master.solar_return(year)...i.e., write solar_return
        return self.Spread(year_spread_list, self.master, self.context.cot_planet_order)
    
    class Spread:
        """
        initialize a Spread object
        the most important argument is spread_list, which is the list of numbers presenting the cards of the spread

        this object will be responsible for intializing the planets
        im not entirely sure what the calculations for the different spreads are called
        i think they are some sort of progression
        probably, those calculations will end up going somewhere else depending on what exactly they are

        spread_list needs to have 14 numbers in it between 0 and 51.

        these integers represent the cards. the integer representing a certain card is the index of that card 
        in the list cards_constants.cards

        but Spread does not check to make sure that the spread is a valid one
        it simply puts the cards in the spread in order: base, sun, moon, etc.
        the precise order is given by CardsOfTruth.context.cot_planet_order
        the default is "vedic"; the other option is "solar_system"

        it finds the proper planets given the spread type
        i.e., for a birth spread, the birth planets, for a year spread, the planets at that solar return, etc.
        and puts them into the "Sun" card, the "Moon" card, etc.

        To test this out by itself, you can do this:
        >>> CardsOfTruth().Spread(spread_list=[0,4,3,45,...])
        where "spread_list" is a list of 14 integers between 0 and 51
        you can also test out the planet order:
        >>> CardsOfTruth().Spread(spread_list=[0,4,3,45,...],order="solar_system")

        TODO: currently, Planet-s being put into cards is not implemented
        """

        def __init__(self, spread_list, rashi, order="vedic"):
            self._list = spread_list
            self._deck = Deck()
            self._order = order
            self._spread = self._init_Spread()
            self._rashi = rashi
            self._place_Objects()

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

        def _place_Objects(self):
            """
            it initializes those Planet-s into Spread
            it adds these Planet-s to their proper Card in the Spread
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

        def rich(self):
            from rich.console import Console
            Console().print(self.richDrawing())
