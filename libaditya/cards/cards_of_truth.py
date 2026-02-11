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

from libaditya.objects import EphContext, Sun

from libaditya.cards import cards_constants as cardsc
from .cot import CoT

class CardsOfTruth(CoT):

    def __init__(self, context=EphContext(), master=None):
        self.context = context
        self._master = master
        self._birth_card = self._get_birth_card()
        self._birth_spread = self._get_birth_spread()

    def master(self):
        return self._master

    def birth_card(self):
        return self._birth_card

    def birth_spread(self):
        return self._birth_spread

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

    def _get_birth_spread_list(self):
        birth_card = self.birth_card()
        return self.get_birthspread_from_quadration(birth_card)

    def _get_birth_spread(self):
        """
        return a Spread object with
        """
        bspread = self._get_birth_spread_list()

        return bspread

    def deck(self):
        return self._deck

    def year_spread(self, year):
        """
        get a year spread for age year

        add way of doing default argument where it uses current age
        """
        return self.get_birthspread_from_quadration(self.birth_card(),self.quadraten(cardsc.jackquad,year+1))

