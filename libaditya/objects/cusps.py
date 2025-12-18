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

from .context import EphContext

from libaditya import constants as const
from libaditya import utils

class Cusp:
    def __init__(self, longitude, speed, number, context=EphContext()):
        self.context = context
        self.hsys = self.context.hsys.encode()
        self.location = self.context.location
        self.timeJD = self.context.timeJD
        self.jd = self.timeJD.jd
        self.system = self.context.sysflg  # if it is sidereal or sidereal topocentric
        self.hname = swe.house_name(self.hsys)
        self.ayanamsa = self.context.ayanamsa
        self.long = longitude
        self.daily_speed = speed
        self._cusp_index = number
        self._number = number + 1
        self.cusp_name = f"Cusp {self._number}"
        from .nakshatra import Nakshatra
        self._nakshatra = Nakshatra(self)

    def __str__(self):
        return self.cusp_name + " at " + str(self.longitude())


    def __repr__(self):
        return self.cusp_name + " at " + str(self.long)

    def name(self):
        return self.cusp_name

    def number(self):
        return self._number

    def cusp_index(self):
        return self._cusp_index

    def longitude(self):
        if self.context.signize:
            return self.signize()
        else:
            return self.raw_longitude()

    def signize(self):
        """
        return a string with 360degree longitude long given with
        long (sign), with long being in the sign
        signs contains the signs to be used, which might be adityas
        """
        index = int(
            (self.long % 360) / 30
        )  # mod 360 in case long=360...but it probably wouldnt with swe, right?
        if self.context.toround[0]:
            inlong = round(self.long % 30, self.context.toround[1])
        else:
            inlong = self.long % 30
        return f"{utils.dec2dmsstr(inlong)} {self.context.sign_names[index]}"

    def raw_longitude(self):
        if self.context.toround[0]:
            return round(self.long, self.context.toround[1])
        else:
            return self.long

    def speed(self):
        if self.context.toround[0]:
            return round(self.daily_speed, self.context.toround[1])
        else:
            return self.daily_speed

    def hourly_motion(self):
        if self.context.toround[0]:
            return round(self.speed() / 24, self.context.toround[1])
        else:
            return self.speed() / 24

    def table_row(self):
        """
        get table row for cusp n
        """
        return (
            [f"{self.number()}"]
            + [self.longitude()]
            + [self.hourly_motion()]
            + [self.speed()]
        )

    def house_system(self):
        return self.hname

    def object_type(self):
        return "Cusp"

    def nakshatra(self):
        return self._nakshatra


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
        from .nakshatra import Nakshatras
        self.context = context
        self.hsys = self.context.hsys.encode()
        self.location = self.context.location
        self.timeJD = self.context.timeJD
        self.jd = self.timeJD.jd
        self.system = self.context.sysflg  # if it is sidereal or sidereal topocentric
        self.hname = swe.house_name(self.hsys)
        self.ayanamsa = self.context.ayanamsa
        self.cusps, self.ascmc, self.ascmcspeed = self.init_cusps() # a 12 tuple of cusp points
        self._nakshatras = Nakshatras(self.cusps,self.context)

    def __iter__(self):
        return iter(self.cusps)

    def __getitem__(self,n):
        return self.cusps[n]

    def __repr__(self):
        """
        the function swe.houses(time,lat,long,hsys) take lat first
        """
        return self.mkheader() + str([cusp for cusp in self.cusps])

    def __str__(self):
        output = PrettyTable()
        output.field_names = [
            "Cusp",
            "Longitude",
            "Hourly Motion",
            "Daily Motion",
        ]
        output.align["Cusp"] = "r"
        output.align["Longitude"] = "l"
        output.align["Hourly Motion"] = "r"
        output.align["Daily Motion"] = "r"

        for cusp in self.cusps:
            output.add_row(cusp.table_row())

        ret = output.get_string(
            fields=["Cusp", "Longitude", "Hourly Motion", "Daily Motion"]
        )

        return self.mkheader() + ret

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
        cusps, ascmc, speeds, ascmcspeeds = swe.houses_ex2(
            self.jd, self.location.lat, self.location.long, self.hsys, flag
        )
        retcusps = []
        for n, cusp in enumerate(cusps):
            retcusps.append(Cusp(cusp, speeds[n], n, self.context))
        return retcusps, ascmc, ascmcspeeds

    def mkheader(self):
        """
        the function swe.houses(time,lat,long,hsys) take lat first
        """
        place = f"Cusps for\n{self.location}\n"
        time = f"{self.timeJD}\n"
        sys = f"Using {self.hname} house system\n"
        ayanamsa = ""
        if self.system == swe.FLG_SIDEREAL or self.system == swe.FLG_TOPOCTR:
            ayanamsa = f"Using {const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        return place + time + sys + ayanamsa

    def house_system(self):
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

    def nakshatras(self):
        return self._nakshatras
