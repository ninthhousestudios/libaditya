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
from prettytable import PrettyTable
from typing import Self

from rich import box
from rich.table import Table
from rich.console import Console

from libaditya import constants as const
from libaditya import utils

from .planets import *
from .cusps import Cusp, Cusps
from .context import EphContext

class Sign:

    def __init__(self, number, planets, cusps, context, master):
        self.context = context
        self._planets = planets
        self._cusps = cusps
        self._objects = self.init_objects()
        self._sign_index = (number-1)%12
        self._sign_name = const.names[self.context.names_type][self.context.sign_names][self.sign_index()]
        self._id = number
        self.master = master
        self._lajjitaadi_avasthas = {}
        # a dictionary that defines our rashi aspects, {int: (int,int,int)}
        
    def sign_index(self):
        return self._sign_index

    def sign_name(self):
        return self._sign_name

    def name(self):
        return self.sign_name()

    def sign(self):
        return self._id

    def Self(self):
        return self

    def planets(self) -> [Planet]:
        """
        Planet is anything that can possibly be a Planet
        return a list of Planets that are in this sign
        """
        return self._planets

    def cusps(self):
        return self._cusps

    def lajjitaadi_avasthas(self):
        return self._lajjitaadi_avasthas

    def lord(self) -> str:
        return const.lords[self.sign()]

    def gender(self):
        if utils.odd(self.sign()):
            return "M"
        if utils.even(self.sign()):
            return "F"

    def rashis_from_lagna(self):
        """
        lagna can be a Sign class or a sign number
        how many signs apart are this one sign and other_sign
        if self=12 and other=1 -> (1-12)%12 = 1
        used for temporary relationships
        """
        lagna = self.master.lagna().sign()
        return ((self.sign() - lagna)%12)+1

    def house_type(self):
        """
        is this an Angle, Panaphara, or Apoklima
        this uses signs from lagna to determine this
        """
        lagna = self.master.lagna()
        signs_from_lagna = self.rashis_from_lagna()
        match signs_from_lagna:
            case 1 | 4 | 7 | 10:
                return "Angle"
            case 2 | 5 | 8 | 11:
                return "Panaphara"
            case 3 | 6 | 9 | 12:
                return "Apoklima"

    def karakas(self) -> [Planet]:
        """
        return a list of Planet classes of the karakas in this sign
        karakas are sun-sat
        """
        ks = []
        for planet in self.planets():
            if planet.is_karaka():
                ks.append(planet)
        return ks

    def grahas(self) -> [Planet]:
        """
        return a list of Planet classes of the grahas in this sign
        grahas are sun-ketu
        """
        gs = []
        for planet in self.planets():
            if planet.is_graha():
                gs.append(planet)
        return gs

    def how_many_objects(self):
        return len(self._objects)

    def how_many_karakas(self):
        return len(self.karakas())

    def how_many_grahas(self):
        return len(self.grahas())

    def objects(self):
        return self._objects

    def objects_within_one_degree(self):
        objects = []
        for object_chosen in self.objects():
            for object_line in self.objects():
                if object_chosen == object_line:
                    continue
                if abs(object_chosen.amsha_longitude()-object_line.amsha_longitude()) < 1:
                    objects.append((object_chosen,object_line))
        return objects

    def init_objects(self):
        if self.context.sysflg == const.BARY or self.context.sysflg == const.HELIO:
            return self._planets
        else:
            return self._planets + self._cusps

    def astrological_signs_forward(self,n) -> int:
        """
        go forward n signs
        this means in the astrologically sense
        so this sign is 1 and then we count
        e.g., if this sign is sign 8 and we go forward 4 signs ->
        8,9,10,11, so 4 signs forwards from Scorpio is Aquarius
        so self.astrological_signs_forward(1) =  self

        but in terms of sign numbers, we add n-1 to the sign number
        and have to deal with how it wraps around


        """
        if n == 0 or  n == -1:
            return self.sign()
        if n < 0:
            # go backwards
            almost = (self.sign() - (abs(n)-1))%12
            if almost == 0:
                return 12
            else:
                return almost
        forward = self.sign() + (n-1)
        if forward > 0 and forward <= 12:
            return forward
        else:
            return forward % 12

    def astrological_signs_backward(self, n: int):
        """
        go backwards n signs in the astrological sense
        this just calls astrological_signs_forward with -n
        """
        return self.astrological_signs_forward(-n)
        
    def astrological_signs_apart(self, other_sign: int) -> int:
        """
        how many signs apart are this one sign and other_sign
        if self=12 and other=1 -> (1-12)%12 = 1
        astrological means counting in an astrological way
        i.e., signs 10 and 1 are 4 signs apart
        other_sign is the sign number of the other sign
        """
        return ((other_sign - self.sign())%12)+1

    def modality(self):
        """
        return modality "Moveable", "Fixed", "Dual"
        """
        match self.sign():
            case 1 | 4 | 7 | 10:
                return "Moveable"
            case 2 | 5 | 8 | 11:
                return "Fixed"
            case 3 | 6 | 9 | 12:
                return "Dual"

    def ordered_cusps(self, reverse=False):
        return sorted(self.cusps(),key = (lambda cusp: cusp.ecliptic_longitude()), reverse=reverse)

    def ordered_planets(self, reverse=False):
        return sorted(self.planets(),key = (lambda cusp: cusp.ecliptic_longitude()), reverse=reverse)

    def ordered_objects(self, reverse=False):
        return sorted(self.ordered_cusps() + self.ordered_planets(),key = (lambda obj: obj.amsha_longitude()), reverse=reverse)

    def __str__(self):
        """
        a string representation that is used for printing charts
        each objects is listed:
        name
        longitude
        """
        ret = ""

        for obj in self.ordered_objects():
            if not self.context.print_outer_planets and obj.object_type()=="Planet" and obj.is_outer_planet():
                # dont print outer objs
                continue
            if obj.identity() == "Sun" and self.context.sysflg == const.HELIO:
                # dont print sun with heliocentric coordinates
                continue
            if (obj.identity() == "Rahu" or obj.identity() == "Ketu") and (self.context.sysflg == const.HELIO or self.context.sysflg == const.BARY):
                # dont print Rahu or Ketu for helio/barycentric
                continue
            if isinstance(obj,Cusp) and (self.context.sysflg == const.HELIO or self.context.sysflg == const.BARY):
                # dont print cusps in heliocentric or barycentric
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
        header += f"\n{self.sign()=} {self.sign_name()}\t{self.context.amsha}\n"
        output = PrettyTable()
        output.field_names = ["Object", "In Amsha Longitude", "Ecliptic Longitude"]
        output.align["Object"] = "l"
        output.align["In Sign Longitude"] = "r"
        output.align["Ecliptic Longitude"] = "r"

        for p in self._planets:
            output.add_row([p.name(),p.amsha_in_sign_longitude(),p.raw_longitude()])
        for c in self._cusps:
            output.add_row([c.name(),c.amsha_in_sign_longitude(),c.raw_longitude()])

        ret = output.get_string(fields=["Object", "In Amsha Longitude", "Ecliptic Longitude"])

        return header + ret

    def richDrawing(self, header_style="#6b00ff", info_style="#00ff00"):
        sign = Table(box=box.ROUNDED, style=header_style)

        # add a "header_style=" argument to change color of this header itself
        sign.add_column(f"{self.sign()} {self.name()}",justify="center",style=info_style)

        # add objects in rows
        sign_str = self.__str__()
        lines = sign_str.split("\n")
        for line in lines:
            sign.add_row(line)

        return sign

    def rich(self):
        console = Console()
        console.print(self.richDrawing())


class One(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(1,planets,cusps,context,master)

    def modality(self) -> str:
        return "Moveable"

    def element(self):
        return "Fire"

    def glyph(self):
        return "♈"

class Two(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(2,planets,cusps,context,master)

    def modality(self) -> str:
        return "Fixed"

    def element(self):
        return "Earth"

    def glyph(self):
        return "♉"

class Three(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(3,planets,cusps,context,master)
        
    def modality(self) -> str:
        return "Dual"

    def element(self):
        return "Air"

    def glyph(self):
        return "♊"

class Four(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(4,planets,cusps,context,master)
        
    def modality(self) -> str:
        return "Moveable"

    def element(self):
        return "Water"

    def glyph(self):
        return "♋"

class Five(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(5,planets,cusps,context,master)

    def modality(self) -> str:
        return "Fixed"

    def element(self):
        return "Fire"

    def glyph(self):
        return "♌️"
        

class Six(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(6,planets,cusps,context,master)
        
    def modality(self) -> str:
        return "Dual"

    def element(self):
        return "Earth"

    def glyph(self):
        return "♍"

class Seven(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(7,planets,cusps,context,master)
        
    def modality(self) -> str:
        return "Moveable"

    def element(self):
        return "Air"

    def glyph(self):
        return "♎"

class Eight(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(8,planets,cusps,context,master)
        
    def modality(self) -> str:
        return "Fixed"

    def element(self):
        return "Water"

    def glyph(self):
        return "♏"

class Nine(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(9,planets,cusps,context,master)
        
    def modality(self) -> str:
        return "Dual"

    def element(self):
        return "Fire"

    def glyph(self):
        return "♐"

class Ten(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(10,planets,cusps,context,master)
        
    def modality(self) -> str:
        return "Moveable"

    def element(self):
        return "Earth"

    def glyph(self):
        return "♑"

class Eleven(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(11,planets,cusps,context,master)
        
    def modality(self) -> str:
        return "Fixed"

    def element(self):
        return "Air"

    def glyph(self):
        return "♒"

class Twelve(Sign):

    def __init__(self,planets,cusps,context,master):
        super().__init__(12,planets,cusps,context,master)

    def modality(self) -> str:
        return "Dual"

    def element(self):
        return "Water"

    def glyph(self):
        return "♓"
        

local_Signs = {
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
        self.aspects = const.rashi_aspects[self.context.rashi_aspects]
        self._signs = self.init_Signs()
        self.sysflgstr = const.sysflgstr(context.sysflg)

    def __iter__(self):
        return iter(self._signs.values())

    def __getitem__(self,n: int) -> Self:
        """
        s=Signs(), then you can write
        then you can write s[key] with key between 1 and 12 inclusive
        modified so you can use negatives to go backwards
        astrologal then means that
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

    def amsha(self):
        return self.context.amsha

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
            stmp[p.amsha_sign_index()][inner_index].append(p)
        # now do cusps
        inner_index = 1
        for c in self._cusps:
            stmp[c.amsha_sign_index()][inner_index].append(c)
        retsigns={}
        for n, sign in enumerate(stmp):
            retsigns[n+1] = local_Signs[n+1](planets=sign[0],cusps=sign[1],context=self.context,master=self)
        return retsigns

    def signs(self):
        return self._signs

    def rashi_aspect_between(self, sign1: Sign, sign2: Sign):
        """
        tells if there are rashi aspects between sign1 and sign2
        0 - none either way
        1 - sign1 aspects sign2
        2 - sign2 aspects sign1
        3 - both aspect each other
        i.e., sign1 aspects means that there is at least one graha in sign1 caring its aspect to sign2
        """
        ltr = self.rashi_aspect_from_to(sign1,sign2)
        rtl = self.rashi_aspect_from_to(sign2,sign1)
        match (ltr,rtl):
            case (0,0):
                return 0
            case (1,0):
                return  1
            case (0,1):
                return 2
            case (1,1):
                return 3

    def rashi_aspect_from_to(self, sign1: Sign, sign2: Sign):
        """
        tells if there are rashi aspects between sign1 and sign2
        0 - none either way
        1 - sign1 aspects sign2
        i.e., sign1 aspects means that there is at least one graha in sign1 caring its aspect to sign2
        """
        if not (sign2.sign() in self.aspects[sign1.sign()]):
            # sign1 is the key to the aspects dictionary
            # the value is a tuple of integers, the signs which sign1 aspects
            # if sign2 is one of those signs, then sign1 can aspect, depending
            # on planets in a sign
            # so if not, return 0, meaning no aspect
            return 0
        # else: sign1 can aspect sign2; if sign1 does have a graha, it aspects, so return 1
        # needs to be grahas; not .planets(), that includes Uranus, etc.
        if sign1.grahas():
            return 1
        else:
            # 0 means there is no aspect. there could be if there were a planet, but there isnt so no planet
            return 0

    def rashi_aspects_given_by(self, sign: Sign) -> [Sign]:
        """
        get Signs that rashi aspect Sign sign
        """
        # sign aspects 3 signs
        # those 3 signs aspect this sign
        # for practical purposes, we want to know which of these 3 signs has grahas in them
        # for this purpose, only the Sign-s of those three that grahas are returned
        aspected_signs = self.aspects[sign.sign()]
        ret = []
        for aspected_sign in [self.signs()[each] for each in aspected_signs]:
            if self.rashi_aspect_from_to(aspected_sign,sign):
                ret.append(aspected_sign)
        return ret

    def rashi_aspects_given_to(self, sign: Sign) -> [Sign]:
        """
        get Signs that rashi aspect Sign sign
        """
        # sign aspects 3 signs
        # those 3 signs aspect this sign
        # for practical purposes, we want to know which of these 3 signs has grahas in them
        # for this purpose, only the Sign-s of those three that grahas are returned
        aspecting_signs = self.aspects[sign.sign()]
        ret = []
        for aspecting_sign in [self.signs()[each] for each in aspecting_signs]:
            if self.rashi_aspect_from_to(aspecting_sign,sign):
                ret.append(aspecting_sign)
        return ret

    def lagna(self) -> Sign:
        """
        return the Sign class of the lagna sign, i.e., whichever one has Cusp 1
        """
        return self.where_is(1) # 1 means Cusp 1
        
    def where_is(self, object: int | str) -> Sign:
        """
        if object is int, a Cusp
        if object is str, a Planet id
        return the Sign class that has in it object
        """
        if isinstance(object, Planet):
            object = object.identity()
        if isinstance(object, Cusp):
            object = object.number()
        for sign in self:
            if isinstance(object, str):
                for planet in sign.planets():
                    if object == planet.identity():
                        return sign
            if isinstance(object, int):
                for cusp in sign.cusps():
                    if object == cusp.number():
                        return sign

    def get_signs_of(self, planet: Planet | str) -> [Sign]:
        """
        get the signs of Planet, either a Planet class or a Planet.identity
        """
        ret = []
        # find the lord string of the Planet
        if isinstance(planet, Planet):
            planet = planet.identity()
        for sign in self:
            if sign.lord() == planet:
                ret.append(sign)
        return ret

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
        return utils.mkheader(self)

    # this is to placate a field in utils.mkheader()
    # this information is in Varga and is not really necessary
    # since we do know the amsha
    def varga_name(self):
        return ""

    def __repr__(self):
        """
        represents as a header with the chart information
        """
        return self.mkheader()


