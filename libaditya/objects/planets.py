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

from libaditya import constants as const
from libaditya import utils

from .context import EphContext
from .planet import Sun, Moon, Mars, Mercury, Venus, Jupiter, Saturn, Rahu, Ketu, Uranus, Neptune, Pluto, Earth, Chiron
from .nakshatra import *


class Planets:
    _planets = [
        Sun,
        Moon,
        Mars,
        Mercury,
        Venus,
        Jupiter,
        Saturn,
        Rahu,
        Ketu,
        Uranus,
        Neptune,
        Pluto,
        Earth,
        Chiron,
    ]

    def __init__(self, context=EphContext()):
        self.timeJD = context.timeJD  # the JulianDay class of this planet
        self.context = context
        self.jd = self.timeJD.jd
        self.ayanamsa = context.ayanamsa
        self.system = context.sysflg
        self.sysflgstr = const.sysflgstr(context.sysflg)
        self.planets = self.init_Planets()
        self._nakshatras = Nakshatras(self.planets,self.context)

    def __iter__(self):
        return iter(self.planets)

    def __getitem__(self,n):
        return self.planets[n]

    def init_Planets(self):
        ret = []
        for p in self._planets:
            ret.append(p(self.context))
        return ret

    def __repr__(self):
        """
        the function swe.houses(time,lat,long,hsys) take lat first
        """
        return self.mkheader() + str([planet for planet in self.planets])

    def __str__(self):
        """
        return a PrettyTable string with coordinates for all planets on julianday
        using sysflag coordinates
        """
        output = PrettyTable()
        output.field_names = [
            "Planet",
            "Longitude",
            "Speed",
            "Latitude",
            "Latitude Speed",
            "Distance",
            "Distance Speed",
        ]
        output.align["Planet"] = "l"
        output.align["Longitude"] = "l"
        output.align["Speed"] = "r"
        output.align["Latitude"] = "r"
        output.align["Latitude Speed"] = "r"
        output.align["Distance"] = "r"
        output.align["Distance Speed"] = "r"

        for p in self.planets:
            # dont print earth unless it is heliocentric or barycentric
            if isinstance(p, Earth) and not (
                self.system == const.HELIO or self.system == const.BARY
            ):
                continue
            # dont print rahuketu if it is heliocentric or barycentric
            if (isinstance(p, Rahu) or isinstance(p, Ketu)) and (
                self.system == const.HELIO or self.system == const.BARY
            ):
                continue
            # dont print the Sun when printing heliocentric coordinates
            if isinstance(p, Sun) and self.system == const.HELIO:
                continue
            output.add_row(p.table_row())

        ret = output.get_string(
            fields=[
                "Planet",
                "Longitude",
                "Speed",
                "Latitude",
                "Latitude Speed",
                "Distance",
                "Distance Speed",
            ]
        )

        return self.mkheader() + ret

    def mkheader(self):
        header = f"{self.sysflgstr} coordinates\n"
        if self.system == swe.FLG_SIDEREAL:
            header += f"{const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        if self.system == swe.FLG_TOPOCTR:
            header += f"{self.context.location}"
        if self.system == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
            header += f"{self.context.location}"
            header += f"{const.ayanamsa_name(self.ayanamsa)} ayanamsa\n"
        header += f"{self.timeJD}\n"
        return header
    
    def nakshatras(self):
        return self._nakshatras
