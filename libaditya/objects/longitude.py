#    This file is part of libaditya.
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

import swisseph as swe
from typing import Self

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
        self._ecliptic_index = int((self.ecliptic_longitude() % 360) / 30)
        self._amsha_longitude = self.varga(amsha)%360
        self._amsha_index = int((self.amsha_raw_longitude() % 360) / 30)
        self.rahu = self.get_rahu()

    def Longitude(self):
        return self

    def ecliptic_longitude(self) -> float:
        return self._longitude

    def amsha_raw_longitude(self):
        return self._amsha_longitude

    def raw_longitude(self) -> float:
        if self.context.toround[0]:
            return round(self.ecliptic_longitude(), self.context.toround[1])
        else:
            return self.ecliptic_longitude()

    def amsha_longitude(self) -> float:
        if self.context.toround[0]:
            return round(self._amsha_longitude, self.context.toround[1])
        else:
            return self._amsha_longitude

    def amsha_opposite(self):
        return (self.amsha_longitude()+180)%360

    def longitude(self) -> float | str:
        if self.context.signize:
            return self.signize()
        else:
            return self.amsha_longitude()

    def ecliptic_index(self):
        return self._ecliptic_index

    def ecliptic_sign_index(self):
        if self.context.circle == Circle.ADITYA:
            return (self.ecliptic_index() + 1) % 12
        else:
            return self.ecliptic_index()

    def ecliptic_sign(self):
        """
        ecliptic sign means the sign in the Rashi chart
        this is the number of that sign
        """
        return self.ecliptic_sign_index()+1

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
        return const.names[self.context.names_type][self.context.sign_names][self.amsha_sign_index()]

    def get_rahu(self) -> float:
        """
        return float of rahus "ecliptic_longitude"
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
        """
        i changed real_longitude to ecliptic_longitude

        it might be tempting to change this name, but it works
        i think it is just in the vargas, so would have to change all of them

        there is a formula using this that makes it more clear what is going on
        so dont change it
        """
        return self.ecliptic_longitude() % 30

    def amsha_in_sign_longitude(self) -> float:
        if self.context.toround[0]:
            inlong = round(self.amsha_longitude() % 30, self.context.toround[1])
        else:
            inlong = self.amsha_longitude() % 30
        return utils.dec2dmsstr(inlong)

    def amsha_raw_in_sign_longitude(self) -> float:
        if self.context.toround[0]:
            return round(self.amsha_longitude() % 30, self.context.toround[1])
        else:
            return self.amsha_longitude() % 30


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
        if self.amsha() < 0:
            # if we have deities for this amsha, use them, otherwise, planetary lords
            # varga lord is set in Longitude.varga() when it finds the longitude
            return self._deity
        else:
            return const.lords[self.sign()]

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
        if next_long > self.ecliptic_longitude():
            return next_long - self.ecliptic_longitude()
        # we have to cross the equinox, thus find the remainder in this cycle
        # plus the portion of the next cycle
        else:
            return (360 - self.ecliptic_longitude()) + next_long

    def amsha_degrees_apart(self, next_long):
        """
        how many degrees from this longitude to next_long going forward around the ecliptic
        """
        # we dont cross the equinox to find the difference
        if next_long > self.amsha_longitude():
            return next_long - self.amsha_longitude()
        # we have to cross the equinox, thus find the remainder in this cycle
        # plus the portion of the next cycle
        else:
            return (360 - self.amsha_longitude()) + next_long

    def amsha_between(self, long1: float, long2: float) -> bool:
        """
        is self between long1 and long2, going signwise around the ecliptic?

        this method is doesnt need to know what "kind" of longitude long1 and long2 are
        not even what amsha. "on" means in the same relative circle. 
        """
        # how far long1 is from 360
        offset = 360 - long1
        # this should = 0 mod 360
        long1 = (long1+offset)%360
        long2 = (long2+offset)%360
        slong = (self.amsha_longitude()+offset)%360
        return long1 <= slong and slong <= long2

    def virupas_between(self, point: float | Self) -> float:
        """
        cusp is the Cusp of whereat Planet has digbala
        point is the longitude (Cusp,Planet, other point)

        between one point?

        between point and its opposite point
        in that 180 degrees, where is it?

        between were this Longitude.amsha_longitude()
        """
        if isinstance(point, float) or isinstance(point, int):
            point = Longitude(point,1,self.context)
        if self.amsha_longitude() == point.amsha_longitude():
                return 60
        if self.amsha_longitude() == point.amsha_opposite():
            return 0
        # see if Planet is between 0 dig and 60 dig
        if self.amsha_between(point.amsha_opposite(),point.amsha_longitude()):
            how_far_into_this_cycle = ((self.amsha_longitude()-point.amsha_opposite())%360)/180
            return how_far_into_this_cycle*60
        # see if Planet is amsha_between 60 dig and 0 dig
        if self.amsha_between(point.amsha_longitude(),point.amsha_opposite()):
            how_close_to_opposite = ((point.amsha_opposite()-self.amsha_longitude())%360)/180
            return how_close_to_opposite*60
        return -1

    def signs_apart(self, other_sign) -> int:
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
            return self.ecliptic_longitude()
        if amsha > 0:
            return self.parivritti_varga(amsha)
        match amsha:
            case -2:
                return self.hora() 
            case -3:
                return self.drekkana()
            case -4:
                return self.chaturthamsha()
            case -10:
                return self.dashamsha()
            case -12:
                return self.dvadashamsha()
            case -16:
                return self.shodashamsha()
            case -20:
                return self.vimshamsha()
            case -240:
                return self.siddhamsha()
            case -24:
                return self.siddhamsha(parashara=True)
            case -27:
                return self.bhamsha()
            case -40:
                return self.khavedamsha()
            case -45:
                return self.akshavedamsha()
            case -60:
                return self.shashtyamsha()
            case _:
                return "not yet implemented"

    varga_deities={
        2: ["Sun", "Moon"],
        7: ["Kshara", "Kshira", "Dadhya", "Ajya", "Ikshurasa", "Madhya", "Shuddha Jala"],
        9: ["Deva","Nri","Rakshasa"],
        10: ["Indra","Agni","Yama","Rakshasa","Varuna","Vayu","Kubera","Ishana","Brahma","Ananta"],
        12: ["Ganesha", "Ashvins", "Yama", "Hayagriva"],
        16: ["Brahma", "Vishnu", "Shiva", "Sun"],
        20: ["Daya", "Megha", "Chinnashirsha", "Pishachani", "Dhumavati", "Matangi", "Bala", "Bhadra", "Aruna", "Anala", "Pingala", "Chucchuka", "Ghora", "Varahi", "Vaishnavi", "Sita", "Bhuvanesvari", "Bhairavi", "Mangala", "Aparajita"],
        # 21 is for odd signs in the -20
        21: ["Kali", "Gauri", "Jaya", "Lakshmi", "Vijaya", "Vimala", "Sati", "Tara", "Jvalamukhi", "Shveta", "Lalita", "Bagalamukhi", "Pratyangira", "Sachi", "Raudri", "Bhavani", "Varada", "Jaya", "Tripura", "Sumukhi"],
        24: ["Skanda", "Parsudhara", "Anala", "Vishwakarma", "Bhaga", "Mitra", "Maya", "Antaka", "Vrishadhwaja", "Govinda", "Madana", "Bhima"],
        27: ["Dastra", "Yama", "Agni", "Pitamaha", "Chandra", "Isha", "Aditi", "Jiva", "Ahi", "Pitara", "Bhaga", "Aryama", "Arka", "Tvashta", "Marut", "Shakragni", "Mitra", "Vasava", "Nirriti", "Varuna", "Vishvadeva", "Govinda", "Vasu", "Varuna", "Ajapa", "Ahirbudhanya", "Pusha"],
        40: ["Vishnu", "Chandra", "Marichi", "Tvashta", "Dhata", "Shiva", "Ravi", "Yama", "Yaksha", "Gandharva", "Kala", "Varuna"],
        45: ["Vidhi", "Isha", "Acyuta"],
        # for -45 fixed signs
        46: ["Isha", "Acyuta", "Surajyeshta"],
        # for -45 dual signs
        47: ["Vishnu", "Ka", "Isha"],
        60: ["Ghora", "Rakshasa", "Deva", "Kubera", "Yaksha", "Kimnara", "Bhrashta", "Kulaghna", "Garala", "Vahni", "Maya", "Purishaka", "Apampathi", "Marut", "Kala", "Sarpa", "Amrita", "Indu", "Mridu", "Komala", "Heramba", "Brahma", "Vishnu", "Maheshwara", "Deva", "Ardra", "Kalinasha", "Kshitisha", "Kamalakara", "Gulika", "Mrityu", "Kala", "Davagni", "Ghora", "Yama", "Kantaka", "Sudha", "Amrita", "Purnachandra", "Vishadaghda", "Kulanasa", "Vamsakshaya", "Utpata", "Kala", "Saumya", "Komala", "Sitala", "Karaladamshtra", "Chandramukhi", "Pravina", "Kala Pavaka", "Dandayudha", "Nirmala", "Saumya", "Krura", "Atisitala", "Amrita", "Payodhi", "Bhramana", "Chandra Rekha"]
    }

    def parivritti_varga(self, this_amsha):
        """
        return the "real" longitude for self.ecliptic_longitude() in
        varga number "division"
        number 2-60 all refer to parvritti vargas
        """
        # just to make sure we are working with the rashi longitude
        real_sign = self.ecliptic_sign_index()+1 # +1 to transform index into sign
        real_longitude = self.ecliptic_longitude()+self.aditya_offset

        amsha = 30/this_amsha
        # position = which amsha this is in
        position = real_longitude/amsha
        amsha_elapsed = int(position)
        # which amsha out of all the amshas
        # i.e., in 2, there are 24 portions, in 9, 108
        self._which_amsha = amsha_elapsed+1
        current_in_amsha = position%1

        base_longitude = 0-self.aditya_offset

        return base_longitude + (amsha_elapsed*30) + (current_in_amsha*30)

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
        real_sign = self.ecliptic_sign_index()+1 # +1 to transform index into sign
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
            #            print(f"{self.ecliptic_longitude()=}\n{self.sign()=}\t{real_sign=}")
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
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
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
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        # take care of it being aditya here, by subtracting self.aditya_offset; 30 if using Circle.ADITYA: 0 if using Circle.ZODIAC
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


    def dashamsha(self):
        """
        -10
        odd signs start with themselves
        even signs start with the ninth from themselves

        odd signs ruled over by the 10 deities in order
        even signs ruled over by the 10 deities in reverse order
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        base_longitude_odd = ((30*(real_sign-1))-self.aditya_offset)%360
        # even starts with the 9th sign
        # since we start counting at the sign itself in astrology, that means we have to add 8 to get to the 9th sign
        even_start = ((real_sign-1)+8)%12
        base_longitude_even = ((30*even_start)-self.aditya_offset)%360
    
        amsha = 30/10
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        if even(real_sign):
            self._deity = list(self.varga_deities[10].__reversed__())[amsha_elapsed%12]
        if odd(real_sign):
            self._deity = self.varga_deities[10][amsha_elapsed%12]
        
        if odd(real_sign):
            base_longitude = base_longitude_odd
        if even(real_sign):
            base_longitude = base_longitude_even
        return base_longitude+(amsha_elapsed*30)+(current_in_amsha)*30

    def dvadashamsha(self):
        """
        -12
        for this varga, each sign is divided up into 12 parts, with the first part corresponding to itself

        so gemini is divided into 12, labelled: "gemini", "cancer", "leo", etc.
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        base_longitude = ((30*(real_sign-1))-self.aditya_offset)%360

        amsha=30/12 # length of one portion in this sign
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        self._deity = self.varga_deities[12][amsha_elapsed%4]

        return base_longitude+(amsha_elapsed*30)+(current_in_amsha)*30

    def shodashamsha(self):
        """
        -16
        for moveable, start from Aries
        for fixed, start from Leo
        for dual, start from Sagittarius
        then the 16 amshas in the normal order from the starting point
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        base_sign_moveable = 1
        base_longitude_moveable = ((30*(base_sign_moveable-1))-self.aditya_offset)%360
        base_sign_fixed = 5
        base_longitude_fixed = ((30*(base_sign_fixed-1))-self.aditya_offset)%360
        base_sign_dual = 9
        base_longitude_dual = ((30*(base_sign_dual-1))-self.aditya_offset)%360

        amsha=30/16 # length of one portion in this sign
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        if real_sign in [1,4,7,10]:
            base_longitude = base_longitude_moveable
        if real_sign in [2,5,8,11]:
            base_longitude = base_longitude_fixed
        if real_sign in [3,6,9,12]:
            base_longitude = base_longitude_dual

        if odd(real_sign):
            self._deity = self.varga_deities[16][amsha_elapsed%4]
        else:
            self._deity = list(self.varga_deities[16].__reversed__())[amsha_elapsed%4]

        return base_longitude+(amsha_elapsed*30)+(current_in_amsha)*30

    def vimshamsha(self):
        """
        -20
        divide each sign into 20 portions, starting with the first as follows:
        for moveable signs: start from Aries
        for fixed signs: start from Sagittarius
        for dual signs: starts from Leo
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        base_sign_moveable = 1
        base_longitude_moveable = ((30*(base_sign_moveable-1))-self.aditya_offset)%360
        base_sign_fixed = 9
        base_longitude_fixed = ((30*(base_sign_fixed-1))-self.aditya_offset)%360
        base_sign_dual = 5
        base_longitude_dual = ((30*(base_sign_dual-1))-self.aditya_offset)%360

        amsha=30/20 # length of one portion in this sign
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        if real_sign in [1,4,7,10]:
            base_longitude = base_longitude_moveable
        if real_sign in [2,5,8,11]:
            # real_sign is fixed, so start with sagittarius
            base_longitude = base_longitude_fixed
        if real_sign in [3,6,9,12]:
            base_longitude = base_longitude_dual

        if odd(real_sign):
            self._deity = self.varga_deities[21][amsha_elapsed]
        else:
            self._deity = self.varga_deities[20][amsha_elapsed]

        return base_longitude+(amsha_elapsed*30)+(current_in_amsha)*30

    def siddhamsha(self, parashara=False):
        """
        -240 is the code for this varga
        a varga of 24 divisions
        odd signs: start at leo and go around the circle in order twice
        even: start at cancer and go twice around the circle in reverse order
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        # the base longitude for odd signs is leo/indra, sign 5
        base_sign_odd = 5
        base_longitude_odd = ((30*(base_sign_odd-1))-self.aditya_offset)%360
        base_sign_even = 4
        base_longitude_even = ((30*(base_sign_even-1))-self.aditya_offset)%360
        
        amsha=30/24 # length of one portion in this sign
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        if odd(real_sign):
            self._deity = self.varga_deities[24][amsha_elapsed%12]
        if even(real_sign):
            self._deity = list(self.varga_deities[24].__reversed__())[amsha_elapsed%12]

        if odd(real_sign):
            base_longitude = base_longitude_odd
            return base_longitude+(amsha_elapsed*30)+(current_in_amsha)*30
        if even(real_sign):
            base_longitude = base_longitude_even
            if parashara:
                sign = 1
            else:
                sign = -1
            return base_longitude+(sign*amsha_elapsed*30)+(current_in_amsha)*30

    def bhamsha(self):
        """
        -27
        divide each sign into 27 equal parts
        the first amsha of a sign is a moveable sign; the moveable signs go into order for starting
        i.e., Aries starts with Aries, Taurus starts with Cancer, Gemini starts with Libra, Cancer starts with Capricorn
              Leo starts with Aries, Virgo starts with Cancer, etc.
        i.e., fire signs start at Aries
              earth signs start at Cancer
              air signs start at Libra
              water signs start at Capricorn
        deities are nakshatra deities
        normal order for odd signs
        reverse for even signs
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        base_sign_fire = 1
        base_longitude_fire = ((30*(base_sign_fire-1))-self.aditya_offset)%360
        base_sign_earth = 4
        base_longitude_earth = ((30*(base_sign_earth-1))-self.aditya_offset)%360
        base_sign_air = 7
        base_longitude_air = ((30*(base_sign_air-1))-self.aditya_offset)%360
        base_sign_water = 10
        base_longitude_water = ((30*(base_sign_water-1))-self.aditya_offset)%360

        amsha=30/27 # length of one portion in this sign
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        match real_sign:
            case 1 | 5 | 9:
                # fire sign
                base_longitude = base_longitude_fire
            case 2 | 6 | 10:
                # earth sign
                base_longitude = base_longitude_earth
            case 3 | 7 | 11:
                # air sign
                base_longitude = base_longitude_air
            case 4 | 8 | 12:
                # water sign
                base_longitude = base_longitude_water

        if odd(real_sign):
            self._deity = self.varga_deities[27][amsha_elapsed]
        if even(real_sign):
            self._deity = list(self.varga_deities[27].__reversed__())[amsha_elapsed]

        return base_longitude+(amsha_elapsed*30)+(current_in_amsha)*30


    def khavedamsha(self):
        """
        -40
        divide each sign into 40 equal sections
        odd signs start at Aries
        even signs start at Libra

        deities go in same order for all signs
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        base_sign_odd = 1
        base_longitude_odd = ((30*(base_sign_odd-1))-self.aditya_offset)%360
        base_sign_even = 7
        base_longitude_even = ((30*(base_sign_even-1))-self.aditya_offset)%360

        amsha=30/40 # length of one portion in this sign
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        if odd(real_sign):
            base_longitude = base_longitude_odd
        if even(real_sign):
            base_longitude = base_longitude_even
    
        self._deity = self.varga_deities[40][amsha_elapsed%12]

        return base_longitude+(amsha_elapsed*30)+(current_in_amsha)*30

    def akshavedamsha(self):
        """
        -45
        divide each sign into 45 portions
        moveable signs start with Aries
        fixed signs start with Leo
        dual signs start with Sagittarius
        Brahma, Shiva, Vishnu rules the portions
        moveable: brahma, shiva, vishnu
        fixed: shiva, vishnu, brahma
        dual: vishnu, brahma, shiva
        """
        # just to make sure we are working with the rashi longitude
        real_sign = 1 + self.ecliptic_sign_index() # + 1 to transform index into sign
        real_in_sign = self.real_in_sign_longitude()

        base_sign_moveable = 1
        base_longitude_moveable = ((30*(base_sign_moveable-1))-self.aditya_offset)%360
        # index is for setting the deity
        index = 45
        base_sign_fixed = 5
        base_longitude_fixed = ((30*(base_sign_fixed-1))-self.aditya_offset)%360
        index = 46
        base_sign_dual = 9
        base_longitude_dual = ((30*(base_sign_dual-1))-self.aditya_offset)%360
        index = 47

        amsha=30/45 # length of one portion in this sign
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        if real_sign in [1,4,7,10]:
            # modality of real_sign and base_longitude are the same here
            base_longitude = base_longitude_moveable
        if real_sign in [2,5,8,11]:
            # real_sign is fixed, so start with sagittarius
            base_longitude = base_longitude_fixed
        if real_sign in [3,6,9,12]:
            base_longitude = base_longitude_dual

        self._deity = self.varga_deities[index][amsha_elapsed%3]

        return base_longitude+(amsha_elapsed*30)+(current_in_amsha)*30

    def shashtyamsha(self):
        """
        -60
        algorithm as described in santhanam's translation of bphs, vol. 1, page 83
        deities are in order for odd signs, reverse for even signs
        """
        real_longitude = Longitude(self.ecliptic_longitude(), 1, self.context)
        real_sign = real_longitude.sign()
        real_in_sign = self.real_in_sign_longitude()
        calc = int(real_in_sign*2)
        _, remainder = divmod(calc,12)
        # this is how many signs from real_sign the d60 sign is
        from_amsha = remainder+1
        sign = real_longitude.astrological_signs_foward(from_amsha)

        base_longitude = ((30*(sign-1))-self.aditya_offset)%360

        amsha=30/60 # length of one portion in this sign
        position = real_in_sign/amsha
        amsha_elapsed = int(position)
        current_in_amsha = position%1

        if odd(real_sign):
            self._deity = self.varga_deities[60][amsha_elapsed]
        if even(real_sign):
            self._deity = list(self.varga_deities[60].__reversed__())[amsha_elapsed]

        return base_longitude+(current_in_amsha*30)

    def __repr__(self):
        return f"({self.ecliptic_longitude()},{self.amsha_longitude()},{self.amsha()})"
