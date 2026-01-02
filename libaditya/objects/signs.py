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
from prettytable import PrettyTable
from typing import Self

from libaditya import constants as const

from .planets import Planet, Planets
from .cusps import Cusps
from .context import EphContext

class Sign:

    def __init__(self, number, planets, cusps, context):
        self.context = context
        self._planets = planets
        self._cusps = cusps
        self._objects = self.init_objects()
        self._sign_index = (number-1)%12
        self._sign_name = self.context.names.sign_names[self.sign_index()]
        self._id = number
        
    def sign_index(self):
        return self._sign_index

    def sign_name(self):
        return self._sign_name

    def sign(self):
        return self._id

    def planets(self):
        return self._planets

    def cusps(self):
        return self._cusps

    def lord(self) -> str:
        return const.lords[self.sign()]

    def how_many_objects(self):
        return len(self._objects)

    def how_many_karakas(self):
        n = 0
        for planet in self.planets():
            if planet.is_karaka():
                n+=1
        return n

    def init_objects(self):
        if self.context.sysflg == const.BARY or self.context.sysflg == const.HELIO:
            return self._planets
        else:
            return self._planets + self._cusps

    def n_signs_forward(self,n) -> int:
        """
        go forward n signs
        this means in the astrologically sense
        so this sign is 1 and then we count
        e.g., if this sign is sign 8 and we go forward 4 signs ->
        8,9,10,11, so 4 signs forwards from Scorpio is Aquarius
        so self.n_signs_forward(1) =  self

        but in terms of sign numbers, we add n-1 to the sign number
        and have to deal with how it wraps around
        """
        forward = self.sign() + (n-1)
        if forward <= 12:
            return forward
        else:
            return forward % 12
        
    def astrological_signs_apart(self, other_sign: int) -> int:
        """
        how many signs apart are this one sign and other_sign
        if self=12 and other=1 -> (1-12)%12 = 1
        astrological means counting in an astrological way
        i.e., signs 10 and 1 are 4 signs apart
        other_sign is the sign number of the other sign
        """
        return ((other_sign - self.sign())%12)+1

    def __str__(self):
        """
        a string representation that is used for printing charts
        each objects is listed:
        name
        longitude
        """
        ret = ""
        for obj in self._objects:
            if not self.context.print_outer_planets and obj.object_type()=="Planet" and obj.is_outer_planet():
                # dont print outer planets
                continue
            if obj.identity() == "Sun" and self.context.sysflg == const.HELIO:
                # dont print sun with heliocentric coordinates
                continue
            ret += f"{obj.name()} "
            if self.context.signize:
                ret += f"{obj.longitude().split(" ")[0]}\n" # remove the sign name here since we are printing in a south indian chart
            else:
                ret += f"{obj.raw_longitude()}\n" # remove the sign name here since we are printing in a south indian chart
            if self.context.print_nakshatras and (self.context.sysflg != const.BARY and self.context.sysflg != const.HELIO):
                ret += f"{obj.nakshatra_name()} "
                ret += f"{obj.nakshatra().elapsed()}\n"
            ret += "\n"

        # remove final \n when returning
        return ret[:-1]

    def __repr__(self):
        header = ""
        header += f"\n{self.sign()=} {self.sign_name()}\n"
        output = PrettyTable()
        output.field_names = ["Object", "In Sign Longitude", "Real Longitude"]
        output.align["Object"] = "l"
        output.align["In Sign Longitude"] = "r"
        output.align["Real Longitude"] = "r"

        for p in self._planets:
            output.add_row([p.name(),p.in_sign_longitude(),p.raw_longitude()])
        for c in self._cusps:
            output.add_row([c.name(),c.in_sign_longitude(),c.raw_longitude()])

        ret = output.get_string(fields=["Object", "In Sign Longitude", "Real Longitude"])

        return header + ret

#    def __repr__(self):
#        name = ""
#        name += f"{self.sign_index()=} {self.sign_name()=}\n"
#        for p in self._planets:
#            name += f"{p}"
#        for c in self._cusps:
#            name += f"{c}"
#        name += "\n"
#        return name

class One(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(1,planets,cusps,context)

class Two(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(2,planets,cusps,context)

class Three(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(3,planets,cusps,context)
        

class Four(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(4,planets,cusps,context)
        

class Five(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(5,planets,cusps,context)
        

class Six(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(6,planets,cusps,context)
        

class Seven(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(7,planets,cusps,context)
        

class Eight(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(8,planets,cusps,context)
        

class Nine(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(9,planets,cusps,context)
        

class Ten(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(10,planets,cusps,context)
        

class Eleven(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(11,planets,cusps,context)
        

class Twelve(Sign):

    def __init__(self,planets,cusps,context):
        super().__init__(12,planets,cusps,context)
        

signs = {
    1: One,
    2: Two,
    3: Three,
    4: Four,
    5: Five,
    6: Six,
    7: Seven,
    8: Eight,
    9: Nine,
    10: Ten,
    11: Eleven,
    12: Twelve
}

class Signs:
    
    def __init__(self, planets=Planets(), cusps=Cusps(), context=EphContext()):
        self.context = context
        self._planets = planets
        self._cusps = cusps
        self.circle = self.context.circle
        self._signs = self.init_Signs()
        self.sysflgstr = const.sysflgstr(context.sysflg)

    def __iter__(self):
        return iter(self._signs.values())

    def __getitem__(self,n):
        """
        s=Signs(), then you can write
        then you can write s[key] with key between 1 and 12 inclusive
        """
        return self._signs[n]

    def keys(self):
        """
        say s=Signs()
        without this method, i have to do s.signs().keys()
        s.signs() is the dictionary of signs
        with this, i can just write s.keys()
        """
        return self._signs.keys()

    def __str__(self):
        ret = ""
        ret += self.mkheader()

        for number,sign in self._signs.items():
            ret += f"{number}: {sign}\n"
        ret += "\n"

        return ret

    def init_Signs(self):
        """
        initialize signs
        first go through all the planets and cusps
        and put them in the right holding place in "signs", then
        initialize a list of Sign classes
        """
        stmp = [[[],[]] for x in range(0,12)]
        # do planets first, inner index = 0
        inner_index = 0
        for p in self._planets:
            stmp[p.sign_index()][inner_index].append(p)
        # now do cusps
        inner_index = 1
        for c in self._cusps:
            stmp[c.sign_index()][inner_index].append(c)
        retsigns={}
        for n, sign in enumerate(stmp):
            retsigns[n+1] = Sign(n+1,planets=sign[0],cusps=sign[1],context=self.context)
        return retsigns

    def signs(self):
        return self._signs

    def lagna(self) -> Sign:
        """
        return the Sign class of the lagna sign, i.e., whichever one has Cusp 1
        """
        for sign in self.signs().values():
            for cusp in sign.cusps():
                if cusp.number() == 1:
                    return sign


    def most_objects(self):
        """
        return the number of objects that is greatest of any sign
        """
        most=0
        for sign in self:
            if sign.how_many_objects() > most:
                most = sign.how_many_objects()
        return most

    def mkheader(self):
        header = f"{self.sysflgstr} coordinates\n"
        if self.context.sysflg == swe.FLG_SIDEREAL:
            # for sidereal signs we actually use swisseph 36
            # dhruva equatorial is only for nakshatras
            if self.context.ayanamsa == 98:
                header += f"{const.ayanamsa_name(36)} ayanamsa for signs\n"
                header += f"{const.ayanamsa_name(98)} ayanamsa for nakshatras\n"
            else:
                header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
        elif self.context.sysflg == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
            if self.context.ayanamsa == 98:
                self.context.ayanamsa = 36
            header += f"{self.context.location}\n"
            header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
        else:
            header += f"{const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
        if self.context.sysflg == swe.FLG_TOPOCTR:
            header += f"{self.context.location}"
        header += f"{self.context.timeJD}\n"
        return header

