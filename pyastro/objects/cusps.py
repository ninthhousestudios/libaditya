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

from .julian_day import JulianDay
from .location import Location
from .context import EphContext
from pyastro import constants as const
from pyastro import utils

class Cusps:
    """
    calculate house cusps for a certain place lat,long (NE both positive)
    with a certain house system hsys at a time JulianDay
    hsys is a letter; swisseph actually needs it as a byte, so it is encoded
    with utf-8...you cant just pass a python string 'R';

    however, the argument for this function should be a python string; so is the
    default in pyphglobals; __init__ takes care of the encoding

    Campanus is the default house system, 'C'
    """

    def __init__(self, context=EphContext()):
        self.context = context
        self.hsys = self.context.hsys.encode()
        self.location = self.context.location
        self.timeJD = self.context.timeJD
        self.jd = self.timeJD.jd
        self.system = self.context.sysflg # if it is sidereal or sidereal topocentric
        self.hname = swe.house_name(self.hsys)
        self.ayanamsa = self.context.ayanamsa
        self.cusps, self.ascmc, self.cuspsspeed, self.ascmcspeed = self.init_cusps()  # a 12 tuple of cusp points

    def __iter__(self):
        return iter(self.cusps)

    def __repr__(self):
        """
        the function swe.houses(time,lat,long,hsys) take lat first
        """
        place = f"Cusps for {self.location.placename} ({self.location.lat},{self.location.long})\n"
        time = f"{self.timeJD}\n"
        sys = f"Using house system {self.hname}\n"
        cusps = f"{self.cusps}\n"
        ayanamsa = ""
        if self.system == swe.FLG_SIDEREAL or self.system == swe.FLG_TOPOCTR:
            ayanamsa = f"Using {const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        return place + time + sys + cusps + ayanamsa

    def __str__(self):
        output = PrettyTable()
        output.field_names = [
            "Cusp",
            "Longitude",
            "Hourly Motion",
            "Daily Motion",
        ]
        output.align["Planet"] = "l"
        output.align["Longitude"] = "l"
        output.align["Hourly Motion"] = "r"
        output.align["Daily Motion"] = "r"

        for n in range(0,len(self.cusps)):
            output.add_row(self.table_row(n))

        ret = output.get_string(fields=["Cusp", "Longitude", "Hourly Motion", "Daily Motion"])

        return self.mkheader() + ret

    def table_row(self,n):
        """
        get table row for cusp n
        """
        return [f"{n+1}"] + [self.longitude(n)] + [self.hourly_motion(n)] + [self.speed(n)]

    def mkheader(self):
        """
        the function swe.houses(time,lat,long,hsys) take lat first
        """
        place = f"Cusps for {self.location.placename} ({self.location.lat},{self.location.long})\n"
        time = f"{self.timeJD}\n"
        sys = f"Using house system {self.hname}\n"
        ayanamsa = ""
        if self.system == swe.FLG_SIDEREAL or self.system == swe.FLG_TOPOCTR:
            ayanamsa = f"Using {const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        return place + time + sys + ayanamsa

    def longitude(self,n):
        if self.context.signize:
            return utils.signize(self.cusps[n],self.context.toround,self.context.sign_names)
        else:
            return self.cusps[n]

    def speed(self,n):
        if self.context.toround[0]:
            return round(self.cuspsspeed[n],self.context.toround[1])
        else:
            return self.cuspsspeed[n]

    def hourly_motion(self,n):
        return round(self.speed(n)/24,self.context.toround[1])

    def init_cusps(self):
        """
        find our house cusps
        cusps will be a 12-tuple with cusps 1-12
        """
        flag = 0
        if self.system == swe.FLG_SIDEREAL or self.system == swe.FLG_TOPOCTR:
            flag = swe.FLG_SIDEREAL
            if self.ayanamsa == 98:
                self.ayanamsa = 36
            swe.set_sid_mode(self.ayanamsa)
        return swe.houses_ex2(self.jd, self.location.lat, self.location.long, self.hsys, flag)

    def house_name(self):
        return self.hname

    def lagna(self):
        """returns ecliptic longitude of lagna"""
        return self.cusps[0]

    def ic(self):
        return self.cusps[3]

    def descendant(self):
        return self.cusps[6]

    def mc(self):
        return self.cusps[9]
