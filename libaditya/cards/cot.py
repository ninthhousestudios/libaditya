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

def getindex(card):
    """Get the index number of the birth card from the Jack Quadration"""
    return cardsc.cards.index(card)

class CoT:
    """
    CoT is a class of static methods that provide most of the basic cot calculation functionality

    this is a Mixin, having no __init__() method

    you can use these methods through CardsOfTruth, the class this inherits unto, e.g.,:
    >>> CardsOfTruth().queen_quadration()
    """

    @staticmethod
    def jack_quadration():
        return cardsc.jackquad

    @staticmethod
    def queen_quadration():
        return CoT.quadrate(cardsc.jackquad)

    @staticmethod
    def king_quadration():
        return CoT.quadrate(CoT.queen_quadration())

    @staticmethod
    def quadrate(tquad):
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
            pile1 = cardsc.topthree(quad)+pile1
            pile2 = cardsc.topthree(quad)+pile2
            pile3 = cardsc.topthree(quad)+pile3
            pile4 = cardsc.topthree(quad)+pile4
            
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

    @staticmethod
    def quadraten(nquad,n):
        while n:
            nquad=CoT.quadrate(nquad.copy())
            n=n-1
        return nquad


    @staticmethod
    def getbspreadwxcfromquad(card,pos,quad):
        """get the birth spread from quad where card is in pos"""
        """0 is the birth card position, 1 is the sun card, 9 is rahu card, 13 is pluto card, etc."""
        cindex=quad.index(getindex(card)) # this is where the card is in the quadration
        # we want to get the birth spread for which card is in pos
        # so if pos is 0, we can simply call getbirthspreadfromquad(card,quad)
        # if pos is not 0, we want to find the card that would be in the 0 pos in quad
        # say pos is 4, then 4-4=0 is the birth card
        # cindex is the index of the desired card in the quad
        # so cindex-pos is the index of the birth card
        # if cindex-pos>=0 this is fine, we can call getbirthspreadfromquad(cindex-pos,quad)
        # otherwise, if cindex-pos=-1, then the index is actually 51, i.e, 52-1
        if cindex-pos>=0:
            return CoT.get_birthspread_from_quadration(cardsc.cards[quad[cindex-pos]],quad)
        else:
            return CoT.get_birthspread_from_quadration(cardsc.cards[quad[52-(cindex-pos)]],quad)

    @staticmethod
    def get_birth_spread_with_card_in_position(card,pos):
        """
        get a birth spread where card is in pos#
        0 is the birth card, 2 is the moon card, 7 is the saturn card, etc.
        """
        return CoT.getbspreadwxcfromquad(card,pos,CoT.queen_quadration())

    @staticmethod
    def get_birthspread_from_quadration(birthcard,quad=None):
        """birthcard is two characters that indicate the birth card, eg., 'AS', ace of spades"""
        """so we need to get that card and the next 13 cards from the Queen Quadration"""
        if quad is None:
            quad = CoT.queen_quadration()
        bc=quad.index(getindex(birthcard))
        bspread=[]
        for x in range(bc,bc+14):
            bspread.append(quad[x%52])
        return bspread
