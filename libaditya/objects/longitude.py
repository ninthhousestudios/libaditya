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


    def real_longitude(self):
        return self._longitude

    def raw_longitude(self):
        if self.context.toround[0]:
            return round(self.long, self.context.toround[1])
        else:
            return self.long

    def longitude(self):
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

    def sign_name(self):
        return self.context.names.sign_names[self.sign_index()]

    def get_rahu(self):
        if self.context.sysflg == const.DRAC:
            return swe.calc_ut(self.jd,swe.TRUE_NODE)[0][0] 
        else:
            return 0

    def in_sign_longitude(self):
        if self.context.toround[0]:
            inlong = round(self._longitude % 30, self.context.toround[1])
        else:
            inlong = self._longitude % 30
        return inlong

    def signize(self):
        """
        return a string with 360degree longitude long given with
        long (sign), with long being in the sign
        signs contains the signs to be used, which might be adityas
        """
        return f"{utils.dec2dmsstr(self.in_sign_longitude())} {self.sign_name()}"
