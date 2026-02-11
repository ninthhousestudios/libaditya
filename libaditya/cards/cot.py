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

from libaditya.cards import Deck


# utility function for quadration
def topthree(quad):
    """Return the top three cards on the deck"""
    pile = []
    for i in range(3):
        pile.append(quad.pop(0))
    return pile

deck = Deck()
# this is the jack quadration, 1 through 52
# 1 is the Ace of Hearts, 52 is the King of Spades...we'll see how that turns out later
jackquad = list(range(0,52))
# the first bc starting 01/01/2026 at sunrise is KS
# at next sunrise switches to QS
# etc.: goes in reverse order; but each month starts with a different card
birth_card_order = list(deck.deck().__reversed__())
# first card of the month is as follows, starting with January
# then each day goes in order according to calendar day number, based on the savana day at the equator for a given longitude
# e.g., February 29 after sunrise will be
first_card_of_the_month = [birth_card_order.index(card) for card in ["KS","JS","9S","7S","5S","3S","AS","QD","TD","8D","3D","4D"]]

class CardsOfTruth:

    def __init__(self, context=EphContext(), master=None):
        self.context = context
        self._master = master
        self._jack_quadration = jackquad
        self._queen_quadration = self.quadrate(self._jack_quadration)
        self._king_quadration = self.quadrate(self._queen_quadration)

    def master(self):
        return self._master

    def birth_card(self):
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
            print(f"Born before sunrising...")
            card_day = [0,0]
        # minus 1 since months are 1-12 but python is 0-indexed
        start_card = first_card_of_the_month[card_day[0]-1]
        # go forward the number of days from that card to find the birth card
        birth_card = birth_card_order[start_card+(card_day[1]-1)]
        return birth_card

    def birth_spread(self):
        birth_card = self.birth_card()
        return get_birthspread_from_quadration(birth_card,queenquad)

    def get_birthspread_from_quadration(birthcard,quad):
        """birthcard is two characters that indicate the birth card, eg., 'AS', ace of spades"""
        """so we need to get that card and the next 13 cards from the Queen Quadration"""
        bc=quad.index(getindex(birthcard))
        bspread=[]
        for x in range(bc,bc+14):
            bspread.append(quad[x%52])
        return bspread

    def deck(self):
        return self._deck

    def jack_quadration(self):
        return self._jack_quadration

    def queen_quadration(self):
        return self._queen_quadration

    def king_quadration(self):
        return self._king_quadration

    def quadrate(self, tquad):
        """
        tquad is the deck that you want to quadrate
        """
        # say we are starting with the jack quadration
        # we pick up the AH, put 2H on top of that, 3H on top, etc. until KS is on the top
        # then we turn the deck over and start from the top, which is now AH
        # this is why I have made AH=1(0) and KS=52(51)
        quad=tquad.copy() # so that i dont have to pass a copy of the quadration to this function
        # first we need to take the top four cards together and put them in one pile
        pile1 = []
        pile2 = []
        pile3 = []
        pile4 = []
        # the new pile needs to go on, i.e., the last element of the new next to the first element of the bottom one
        while len(quad) > 4: 
            pile1 = topthree(quad)+pile1
            pile2 = topthree(quad)+pile2
            pile3 = topthree(quad)+pile3
            pile4 = topthree(quad)+pile4
            
        pile1=[quad.pop(0)]+pile1
        pile2=[quad.pop(0)]+pile2
        pile3=[quad.pop(0)]+pile3
        pile4=[quad.pop(0)]+pile4

        # now we have four piles. now we need to put the second on top of the first
        # we can use quad since we popped all of its item off
        quad = (pile4+(pile3+(pile2+pile1)))

        # now we put the first card into the first pile, the second into the second, etc.
        # until there are no more cards

        # make sure our piles are empty
        pile1 = []
        pile2 = []
        pile3 = []
        pile4 = []
        
        while len(quad):
            pile1=[quad.pop(0)]+pile1
            pile2=[quad.pop(0)]+pile2
            pile3=[quad.pop(0)]+pile3
            pile4=[quad.pop(0)]+pile4

        quad = (pile4+(pile3+(pile2+pile1)))

        # this should be the next quadration. we dont have to deal with turning the deck over here
        # as long as everything was done correctly
        
        return quad

