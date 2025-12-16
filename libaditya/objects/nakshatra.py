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

from .context import EphContext
from .planet import Planet, Moon
from .cusps import Cusp

from libaditya import constants as const


class Nakshatra:
    def __init__(self, occupant=Moon()):
        self.occupant = occupant
        self.context = occupant.context
        self.timeJD = occupant.timeJD
        self.base_long = self.occupant.raw_longitude()
        self.is_sidereal = self.is_it_sidereal_already(self.context.sysflg)
        self.ayanamsa = self.context.ayanamsa
        # ashlong means the number of degrees from ashvini; in most cases, the sidereal longitude
        self.ash_long = self.init_ash_long()

    def __str__(self):
        nak = f"Nakshatra of {self.occupant_name()}\n"
        base_long = f"base longitude: {self.base_longitude()}\n"
        ash_long = f"Degrees from beginning of ashvini: {self.ashvini_longitude()}\n"
        ayana = f"Using {self.ayanamsa_name()} ayanamsa\n"
        return nak + base_long + ash_long + ayana

    def occupant_name(self):
        return self.occupant.name()

    def base_longitude(self):
        return self.base_long

    def ashvini_longitude(self):
        return self.ash_long

    def is_it_sidereal_already(self, sysflg):
        if sysflg == swe.FLG_SIDEREAL or sysflg == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
            return True
        else:
            return False

    def init_ash_long(self):
        if self.is_sidereal:
            return self.base_long
        # otherwise, find the number of degrees from ashvini
        # insert custom ayanamsa codes and methods here
        if self.ayanamsa == 98:
            # just for now
            self.ayanamsa = 36
        if isinstance(self.occupant, Planet):
            return self.init_ash_long_Planet()
        if isinstance(self.occupant, Cusp):
            return self.init_ash_long_Cusp()
        else:
            print(f"instance of type {type(self.occupant)} cannot be in a nakshatra")

    def init_ash_long_Planet(self):
        swe.set_sid_mode(self.ayanamsa)
        return swe.calc_ut(
            self.timeJD.jd_number(), self.occupant.pnumber, swe.FLG_SIDEREAL
        )[0][0]

    def init_ash_long_Cusp(self):
        swe.set_sid_mode(self.ayanamsa)
        cusps, _, _, _ = swe.houses_ex2(
            self.occupant.timeJD.jd_number(),
            self.occupant.location.lat,
            self.occupant.location.long,
            self.occupant.hsys,
            swe.FLG_SIDEREAL,
        )
        return cusps[self.occupant.cusp_index()]

    def ayanamsa_name(self):
        return const.ayanamsa_name(self.ayanamsa)
