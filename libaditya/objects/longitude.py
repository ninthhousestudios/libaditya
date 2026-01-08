#    This file is part of pyphemeris.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
#
#    pyphemeris is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyphemeris is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with pyphemeris.  If not, see <https://www.gnu.org/licenses/>.

import swisseph as swe

from libaditya import constants as const
from libaditya import utils

from .context import EphContext, Circle

def even(n):
    return n%2 == 0 

def odd(n):
    return n%2 == 1 

class Longitude:
    """
    Longitude expects at minimum a longitude
    
    for vargas, pass the longitude in the rashi along with, e.g., amsha=9
    Longitude will know its original longitude, as well as the varga one
    but it will consider itself to be a navamsha
    so that Longitude.longitude() will give the longitude in the navamsha
    """

    def __init__(self, longitude, amsha, context=EphContext()):
        self.context = context
        if self.context.circle == Circle.ADITYA:
            self.aditya_offset = 30
        else:
            self.aditya_offset = 0
        self._amsha = amsha
        self.jd = self.context.timeJD.jd_number()
        # _longitude the ecliptic longitude of this longitude; i.e., in the rashi varga
        self._longitude = longitude
        self._real_index = int((self.real_longitude() % 360) / 30)
        self._amsha_longitude = self.varga(amsha)
        self._amsha_index = int((self.amsha_raw_longitude() % 360) / 30)
        self.rahu = self.get_rahu()


    def real_longitude(self) -> float:
        return self._longitude

    def amsha_raw_longitude(self):
        return self._amsha_longitude

    def raw_longitude(self) -> float:
        if self.context.toround[0]:
            return round(self.real_longitude(), self.context.toround[1])
        else:
            return self.real_longitude()

    def amsha_longitude(self) -> float:
        if self.context.toround[0]:
            return round(self._amsha_longitude, self.context.toround[1])
        else:
            return self._amsha_longitude

    def longitude(self) -> float | str:
        if self.context.signize:
            return self.signize()
        else:
            return self.amsha_longitude()

    def real_index(self):
        return self._real_index

    def real_sign_index(self):
        if self.context.circle == Circle.ADITYA:
            return (self.real_index() + 1) % 12
        else:
            return self.real_index()

    def amsha_index(self):
        return self._amsha_index

    def amsha_sign_index(self):
        if self.context.circle == Circle.ADITYA:
            return (self.amsha_index() + 1) % 12
        else:
            return self.amsha_index()

    def sign(self) -> int:
        return self.amsha_sign_index() + 1

    def sign_name(self) -> str:
        return self.context.names.sign_names[self.amsha_sign_index()]

    def get_rahu(self) -> float:
        """
        return float of rahus "real_longitude"
        """
        if self.context.sysflg == const.DRAC:
            return swe.calc_ut(self.jd,swe.TRUE_NODE)[0][0] 
        else:
            return 0

    def in_sign_longitude(self) -> str:
        if self.context.toround[0]:
            inlong = round(self._longitude % 30, self.context.toround[1])
        else:
            inlong = self._longitude % 30
        return utils.dec2dmsstr(inlong)

    def real_in_sign_longitude(self) -> float:
        return self.real_longitude() % 30

    def amsha_in_sign_longitude(self) -> float:
        if self.context.toround[0]:
            inlong = round(self.amsha_longitude() % 30, self.context.toround[1])
        else:
            inlong = self.amsha_longitude() % 30
        return utils.dec2dmsstr(inlong)

    def amsha(self) -> int:
        return self._amsha

    def lord(self) -> str:
        """
        return the planetary lord of the sign this longitude is in in this amsha
        """
        return const.lords[self.sign()]

    def deity(self) -> str:
        """
        returns the varga deity of the amsha that this longitude is in
        varga lord is set in Longitude.varga() when it finds the longitude
        amsha=1 can be passed if you want the lord of its sign in this varga
        """
        if self.amsha() == 1:
            return const.lords[self.sign()]
        elif self.amsha() > 1:
            # do sign lords in the parivritti vargas for now
            return const.lords[self.sign()]
        else:
            # varga lord is set in Longitude.varga() when it finds the longitude
            return self._deity

    def signize(self):
        """
        return a string with 360degree longitude long given with
        long (sign), with long being in the sign
        signs contains the signs to be used, which might be adityas
        """
        return f"{self.amsha_in_sign_longitude()} {self.sign_name()}"

    def degrees_apart(self, next_long):
        """
        how many degrees from this longitude to next_long going forward around the ecliptic
        """
        # we dont cross the equinox to find the difference
        if next_long > self.real_longitude():
            return next_long - self.real_longitude()
        # we have to cross the equinox, thus find the remainder in this cycle
        # plus the portion of the next cycle
        else:
            return (360 - self.real_longitude()) + next_long

    def signs_apart(self, other_sign):
        """
        how many signs apart are this one sign and other_sign
        if self=12 and other=1 -> (1-12)%12 = 1
        used for temporary relationships
        """
        return (other_sign - self.sign())%12

    def astrological_signs_foward(self,n) -> int:
        """
        go forward n signs
        this means in the astrologically sense
        so this sign is 1 and then we count
        e.g., if this sign is sign 8 and we go forward 4 signs ->
        8,9,10,11, so 4 signs forwards from Scorpio is Aquarius
        so self.astrological_signs_foward(1) =  self

        but in terms of sign numbers, we add n-1 to the sign number
        and have to deal with how it wraps around
        """
        forward = self.sign() + (n-1)
        if forward <= 12:
            return forward
        else:
            return forward % 12

    def amsha(self):
        return self._amsha

    def varga(self,amsha) -> float:
        """
        get varga with amsha divisions
        returns float of longitude that varga
        options for amsha:
        all positive numbers give parivritti varga of that number
        other numbers are for special vargas (listed as implemented):
            -2 Hora -> the second half of a sign relates to the opposite sign
                        the first half of a sign is of that element, the second half of the other

        these are called by functions in Longitude: .hora(), .drekkana(), etc.
        this is where the actual calculation is done
        """
        if amsha == 1:
            return self.real_longitude()
        if amsha > 0:
            return self.parvritti_varga(amsha)
        match amsha:
            case -2:
                return self.hora() 
            case -3:
                return self.drekkana()
            case -4:
                return self.chaturthamsha()
            case _:
                return "not yet implemented"

    def hora(self):
        """
        in the hora, lord of first half of a male sign is the sun, of second half is the moon
                     lord of first half of a female sign is hte moon, of second half is the sun
                     a planet in the first half stays in that sign
                     a planet in the second half goes to the opposite sign

        this 1) returns the longitude of the planet in the hora
             2) sets self._deity to the hora lord
        """
        # just to make sure we are working with the rashi longitude
        real_sign = self.real_sign_index()+1 # +1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        base_longitude = ((30*(real_sign-1))-self.aditya_offset)%360
        opposite_base_longitude = ((base_longitude+180)%360)

        # we need to 1) set the lord 2) return the amsha=-2 longitude
        if odd(real_sign) and real_in_sign < 15:
            # first half of odd sign ->
            self._deity = "Sun"
            # stays in this sign
            # minus makes the sign number into an index
            hora_elapsed = (real_in_sign/15)*30
            #            print(f"{self.real_longitude()=}\n{self.sign()=}\t{real_sign=}")
            return base_longitude+hora_elapsed
        if odd(real_sign) and real_in_sign >= 15:
            # second half of odd sign ->
            self._deity = "Moon"
            # goes to opposite sign
            hora_elapsed = ((real_in_sign-15)/15)*30
            return opposite_base_longitude+hora_elapsed
        if even(real_sign) and real_in_sign < 15:
            # first half of even sign ->
            self._deity = "Moon"
            # stays in this sign
            # minus makes the sign number into an index
            hora_elapsed = (real_in_sign/15)*30
            return base_longitude+hora_elapsed
        if even(real_sign) and real_in_sign >= 15:
            # second half of odd sign ->
            self._deity = "Sun"
            # goes to opposite sign
            hora_elapsed = ((real_in_sign-15)/15)*30
            return opposite_base_longitude+hora_elapsed

    def drekkana(self):
        """
        same element, different modality
        divide the sign into three: first 3rd remains as that sign, sign 1 from this sign (sign means Longitude(amsha), which implies a sign); narada
                                    second 3rd goes to the next trine, the next sign of same element, different modality, sign 5 from here;  agastya
                                    third 3rd goes to the next next trine, the next next sign of same element, different different modality, sign 9 from here; durvasas

        this 1) returns the longitude of the planet in the hora
             2) sets self._deity to the hora lord
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.real_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        # take care of it being aditya here, by adding self.aditya_offset; 30 if using Circle.ADITYA: 0 if using Circle.ZODIAC
        base_longitude = ((30*(real_sign-1))-self.aditya_offset)%360
        trine_longitude = (base_longitude+120)%360
        trine_trine_longitude = (base_longitude+240)%360

        if real_in_sign < 10:
            self._deity = "Narada"
            return base_longitude + (real_in_sign/10)*30
        if real_in_sign >= 10 and real_in_sign < 20:
            self._deity = "Agastya"
            return trine_longitude + ((real_in_sign-10)/10)*30
        if real_in_sign >= 20 and real_in_sign < 30:
            self._deity = "Durvasas"
            return trine_trine_longitude + ((real_in_sign-20)/10)*30

    def chaturthamsha(self):
        """
        same modality, different element
        divide the sign into four: first 4th remains, sanaka
                                   second 4th goes to next sign of same modality, sananada
                                   third 4th goes to opposite sign of same modality, sanatkumāra
                                   fourth 4th goes to third sign of same modality, sanātana 

        this 1) returns the longitude of the planet in the hora
             2) sets self._deity to the hora lord
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.real_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        # take care of it being aditya here, by adding self.aditya_offset; 30 if using Circle.ADITYA: 0 if using Circle.ZODIAC
        base_longitude = ((30*(real_sign-1))-self.aditya_offset)%360
        square_longitude = (base_longitude+90)%360
        square_square_longitude = (base_longitude+180)%360
        square_square_square_longitude = (base_longitude+270)%360

        fourth = 30/4

        if real_in_sign < fourth:
            self._deity = "Sanaka"
            return base_longitude + (real_in_sign/fourth)*30
        if real_in_sign >= fourth and real_in_sign < 2*fourth:
            self._deity = "Sananda"
            return square_longitude + ((real_in_sign-fourth)/fourth)*30
        if real_in_sign >= 2*fourth and real_in_sign < 3*fourth:
            self._deity = "Sanatkumāra"
            return square_square_longitude + ((real_in_sign-2*fourth)/fourth)*30
        if real_in_sign >= 3*fourth and real_in_sign < 4*fourth:
            self._deity = "Sanātana"
            return square_square_square_longitude + ((real_in_sign-3*fourth)/fourth)*30

        
    def parvritti_varga(self, amsha):
        """
        return the "real" longitude for self.real_longitude() in
        varga number "division"
        number 2-60 all refer to parvritti vargas

        this algorithm was adapted from pyjhora
        """
        # self.aditya_offset is to take care of aditya/zodiac cirlce
        one_amsha = (360.0 / (12 * amsha))  # There are also 108 navamsas
        one_sign = 12.0 * one_amsha    # = 40 degrees exactly
        signs_elapsed = (self.real_longitude()+self.aditya_offset) / one_sign
        left = signs_elapsed % 1
        sign = int(left * 12)
        in_sign_long = (((self.real_longitude()+self.aditya_offset)/one_amsha)%1)*30
        return ((sign*30) + (in_sign_long)) - self.aditya_offset
