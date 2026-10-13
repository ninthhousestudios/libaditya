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
        # otherwise, if cindex-pos=-1, then the index is actually 51, i.e, 52+(-1)
        # (td-eek4: this used to be 52-(cindex-pos), which for -1 gives 53 and
        # walks off the end of the 52-card quadration -> IndexError)
        if cindex-pos>=0:
            return CoT.get_birthspread_from_quadration(cardsc.cards[quad[cindex-pos]],quad)
        else:
            return CoT.get_birthspread_from_quadration(cardsc.cards[quad[52+(cindex-pos)]],quad)

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

    @staticmethod
    def seat_rows(birthcard, decks=None):
        """The same fourteen SEATS read in the jack, queen and king quadrations.

        Each cell of the spread carries three cards: a small one at the bottom
        left, the card face in the middle, and a small one at the top right.
        They are not three calculations. The birth spread occupies
        fourteen consecutive seats of the queen quadration, and the two small
        cards are simply what the OTHER two quadrations hold at those same
        seats. The spread is headed "Queen Quadration" because that names which
        of the three the faces come from.

        Returns ``(jack_row, queen_row, king_row)``, each a list of fourteen
        two-letter card CODES. ``queen_row`` is exactly
        ``get_birthspread_from_quadration(birthcard)`` translated through
        ``cards_constants.cards``.

        Codes rather than deck indices so that a caller never has to index
        ``cards_constants.cards`` itself — that is app-side arithmetic on an
        engine table, and it is the step where an off-by-one turns into a wrong
        card that still looks like a card.

        The seat comes from the QUEEN quadration for all three rows. Do not
        "simplify" this to::

            CoT.get_birthspread_from_quadration(birthcard, CoT.king_quadration())

        That re-finds the birth card in the king deck, where it sits at a
        different seat, and returns a different fourteen cards. For birth card
        3D the seat is 5 in the queen deck but 16 in the king deck::

            this method : QD 2C AS 9H 4D JH 6D 6S AC 9S 7S 3D 6H AD
            that call   : 3D 6H AD TC 8C 3S 4H 5S QS 6C 3H AH 9D 5C

        It never raises, and the wrong answer is not noise: ``quadraten(jackquad,
        2)`` IS the king quadration, so that call returns the year spread for
        age 1 -- a real spread from a different screen.

        The same substitution is available on the jack row and is HARMLESS only
        because the jack quadration is the unshuffled deck, so its own seat
        always coincides. Do not conclude from that that the seats are
        interchangeable.

        Three birth cards hide the error completely: JH, 8C and KS are the fixed
        points where the card sits at the same seat in the queen and king decks.
        A chart with one of those as its birth card cannot detect the wrong
        call, and its Mars/Jupiter/Uranus cell shows the same card three times.
        """
        # ``decks`` lets a caller pass the three quadrations it already holds.
        # They are process constants -- none of the three takes a chart, a date
        # or a context -- but ``queen_quadration()`` and ``king_quadration()``
        # BUILD A NEW LIST on every call, so a caller that does not pass them
        # re-shuffles a 52-card deck two or three times per spread for a value
        # that cannot change.
        if decks is None:
            jack, queen, king = (CoT.jack_quadration(),
                                 CoT.queen_quadration(),
                                 CoT.king_quadration())
        else:
            jack, queen, king = decks
        seat = list(queen).index(getindex(birthcard))
        seats = [(seat + i) % 52 for i in range(14)]
        # Read through each deck rather than using the seat number directly for
        # the jack row: the two are equal only while jackquad is the identity,
        # and writing the three rows as one expression is what keeps them so.
        return ([cardsc.cards[jack[s]] for s in seats],
                [cardsc.cards[queen[s]] for s in seats],
                [cardsc.cards[king[s]] for s in seats])
