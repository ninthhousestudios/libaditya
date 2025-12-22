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

from .longitude import Longitude
from .context import EphContext

from libaditya import constants as const

class Cusp(Longitude):
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
        super().__init__(self.long,self.context)
        from .nakshatras import Nakshatra
        self._nakshatra = Nakshatra(self)

    def __str__(self):
        return self.cusp_name + " at " + str(self.longitude()) + "\n"

    def __repr__(self):
        return self.cusp_name + " at " + str(self.long) + "\n"

    def name(self):
        return self.cusp_name

    def number(self):
        return self._number

    def cusp_index(self):
        return self._cusp_index

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
            + [self.nakshatra_name()]
            + [self.nakshatra().elapsed()]
            + [self.hourly_motion()]
            + [self.speed()]
        )

    def house_system(self):
        return self.hname

    def object_type(self):
        return "Cusp"

    def nakshatra(self):
        return self._nakshatra

    def nakshatra_name(self):
        return self._nakshatra.nakshatra()


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
        self.system = self.context.sysflg  # if it is sidereal or sidereal topocentric
        self.hname = swe.house_name(self.hsys)
        self.ayanamsa = self.context.ayanamsa
        self.cusps, self.ascmc, self.ascmcspeed = self.init_cusps() # a 12 tuple of cusp points
        from .nakshatras import Nakshatras
        self._nakshatras = Nakshatras(self,self.context)

    def __iter__(self):
        return iter(self.cusps)

    def __getitem__(self,n):
        return self.cusps[n]

    def init_cusps(self):
        """
        find our house cusps
        cusps will be a 12-tuple with cusps 1-12
        """
        flag = 0
        if self.system == swe.FLG_SIDEREAL or self.system == swe.FLG_TOPOCTR:
            flag = swe.FLG_SIDEREAL
            if self.ayanamsa == 98:
                swe.set_sid_mode(36)
            else:
                swe.set_sid_mode(self.ayanamsa)
        cusps, ascmc, speeds, ascmcspeeds = swe.houses_ex2(
            self.jd, self.location.lat, self.location.long, self.hsys, flag
        )
        retcusps = []
        for n, cusp in enumerate(cusps):
            retcusps.append(Cusp(cusp, speeds[n], n, self.context))
        return retcusps, ascmc, ascmcspeeds


    def __str__(self):
        output = PrettyTable()
        output.field_names = [
            "Cusp",
            "Longitude",
            "Nakshatra",
            "Elapsed",
            "Hourly Motion",
            "Daily Motion",
        ]
        output.align["Cusp"] = "r"
        output.align["Longitude"] = "l"
        output.align["Nakshatra"] = "r"
        output.align["Elapsed"] = "r"
        output.align["Hourly Motion"] = "r"
        output.align["Daily Motion"] = "r"

        for cusp in self.cusps:
            output.add_row(cusp.table_row())

        if self.context.print_nakshatras:
            ret = output.get_string(
                fields=["Cusp", "Longitude", "Nakshatra", "Elapsed", "Hourly Motion", "Daily Motion"]
            )
        else:
            ret = output.get_string(
                fields=["Cusp", "Longitude", "Hourly Motion", "Daily Motion"]
            )

        return self.mkheader() + ret


    def mkheader(self):
        """
        the function swe.houses(time,lat,long,hsys) take lat first
        """
        draconic = "Draconic " if self.context.sysflg == const.DRAC else ""
        sidereal = "Sidereal " if self.context.sysflg == const.SID else ""
        place = f"{draconic}{sidereal}Cusps for\n{self.location}\n"
        circle = f"{const.circle_name(self.context.circle)}\n"
        time = f"{self.timeJD}\n"
        sys = f"Using {self.hname} house system\n"
        ayanamsa = ""
        if self.context.sysflg == const.SID:
            # for sidereal signs we actually use swisseph 36
            # dhruva equatorial is only for nakshatras
            if self.ayanamsa == 98:
                ayanamsa += f"{const.ayanamsa_name(36)} ayanamsa for cusps\n"
                ayanamsa += f"{const.ayanamsa_name(98)} ayanamsa for nakshatras\n"
            else:
                ayanamsa += f"{const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        else:
            ayanamsa = f"Using {const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        return place + circle + time + sys + ayanamsa

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
