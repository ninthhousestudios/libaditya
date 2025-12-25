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

class Longitude:

    def __init__(self, longitude, context=EphContext()):
        self.context = context
        self._longitude = longitude 
        self.index = int((self._longitude % 360) / 30)
        self.rahu = self.get_rahu()


    def real_longitude(self) -> float:
        return self._longitude

    def raw_longitude(self) -> float:
        if self.context.toround[0]:
            return round(self.long, self.context.toround[1])
        else:
            return self.long

    def longitude(self) -> float | str:
        if self.context.sysflg == const.DRAC:
            self._longitude = (self._longitude - self.rahu)%360
        if self.context.signize:
            return self.signize()
        else:
            return self.raw_longitude()

    def index(self):
        return self.index

    def sign_index(self):
        if self.context.circle == Circle.ADITYA:
            return (self.index + 1) % 12
        else:
            return self.index

    def sign(self) -> int:
        return self.sign_index()+1

    def sign_name(self) -> str:
        return self.context.names.sign_names[self.sign_index()]

    def get_rahu(self):
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

    def lord(self):
        return const.lords[self.sign()]

    def signize(self):
        """
        return a string with 360degree longitude long given with
        long (sign), with long being in the sign
        signs contains the signs to be used, which might be adityas
        """
        return f"{self.in_sign_longitude()} {self.sign_name()}"

    def degrees_apart(self, next_long):
        """
        how many degrees apart this longitude is from next_long
        """
        next_long%=360
        if next_long > self.real_longitude():
            return next_long - self.real_longitude()
        else:
            return (next_long+360) - self.real_longitude()

    def signs_apart(self, other_sign):
        """
        how many signs apart are this one sign and other_sign
        if self=12 and other=1 -> (1-12)%12 = 1
        used for temporary relationships
        """
        return (other_sign - self.sign())%12
        
    def varga(self, amsha):
        """
        return the "real" longitude for self.real_longitude() in
        varga number "division"
        number 2-60 all refer to parvritti vargas

        this algorithm was adapted from pyjhora
        """
        # shift is to take care of aditya/zodiac cirlce
        shift = 0
        if self.context.circle == Circle.ADITYA:
            shift = 30
        one_amsha = (360.0 / (12 * amsha))  # There are also 108 navamsas
        one_sign = 12.0 * one_amsha    # = 40 degrees exactly
        signs_elapsed = (self.real_longitude()+shift) / one_sign
        left = signs_elapsed % 1
        sign = int(left * 12)
        in_sign_long = (((self.real_longitude()+shift)/one_amsha)%1)*30
        return ((sign*30) + (in_sign_long)) - shift
