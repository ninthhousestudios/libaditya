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

from libaditya.objects import Signs

class Varga:

    def __init__(self,identifier,planets,cusps,context):
        self.context = context
        self._identifier = identifier
        self._planets = planets
        self._cusps = cusps
        self._signs = Signs(self._planets,self._cusps,self.context)
        self.sysflgstr = const.sysflgstr(context.sysflg)

    def varga_name(self):
        match self._identifier:
            case 1:
                return "Rashi"
            case 9:
                return "Navamsha"
            case _:
                return "Not yet implemented"

    def identifier(self):
        return self._identifier

    def planets(self):
        return self._planets

    def cusps(self):
        return self._cusps

    def signs(self):
        return self._signs
    
    def __str__(self):
        output = PrettyTable()
        output.field_names = ["  ", "   ", "    ", "     "]

        output.add_row([f"{self.signs()[12]}", f"{self.signs()[1]}", f"{self.signs()[2]}", f"{self.signs()[3]}"])
        output.add_divider()
        output.add_row([f"{self.signs()[11]}", "  ", "  ", f"{self.signs()[4]}"])
        output.add_divider()
        output.add_row([f"{self.signs()[10]}", "  ", "  ", f"{self.signs()[5]}"])
        output.add_divider()
        output.add_row([f"{self.signs()[9]}", f"{self.signs()[8]}", f"{self.signs()[7]}", f"{self.signs()[6]}"])

        ret = output.get_string(fields=["  ", "   ", "    ", "     "])

        return self.mkheader() + ret


    def __repr__(self):
        """
        this is for every varga except the Rashi
        the rashi is printed with nakshatras
        the others are not

        str prints a table with signs at the top
        each object is printed under its sign
        as "object in_sign_longitude"
        the number of rows will be equal to the most objects that are in one sign
        """
        output = PrettyTable()
        # list of the sign names
        output.field_names= list([sign for sign in [self.context.names.sign_names]][0])

        # get the sign with the most objects, so we know how many rows to print
        rows = self._signs.most_objects()

        for r in range(0,rows):
            # construct the row
            row = []
            # could also write for s in self._signs.signs().values()
            # and then replace self._signs[s]._objects by s._objects
            for s in self._signs.keys():
                if len(self._signs[s]._objects) > r:
                    if not self.context.print_outer_planets and self._signs[s]._objects[r].object_type()=="Planet" and self._signs[s]._objects[r].is_outer_planet():
                        row.append("")
                        continue
                    if self._signs[s]._objects[r].identity() == "Sun" and self.context.sysflg == const.HELIO:
                        # dont print the Sun is using heliocentric coordinates
                        row.append("")
                        continue
                    rowstr = f"{self._signs[s]._objects[r].name()}\n{self._signs[s]._objects[r].in_sign_longitude()}\n"
                    # if this is a Rashi, print nakshatras, if that is specified
                    # unless it is barycentric or heliocentric
                    if isinstance(self,Rashi) and (self.context.sysflg != const.BARY and self.context.sysflg != const.HELIO):
                        # print nakshatras or not
                        if self.context.print_nakshatras:
                            rowstr += f"{self._signs[s]._objects[r].nakshatra_name()}\n{self._signs[s]._objects[r].nakshatra().elapsed()}\n"
                    row.append(rowstr) 
                else:
                    row.append("")
            output.add_row(row)

        ret = output.get_string(fields=list([sign for sign in [self.context.names.sign_names]][0]))
        return self.mkheader() + ret

    def draw_sun_by_sign_table(self):
        """
        this prints nakshatras with the chart
        """
        output = PrettyTable()
        # list of the sign names
        output.field_names=list(["Object"] + list([sign for sign in [self.context.names.sign_names]][0]) + ["Nakshatra"] + ["Elapsed"])

        # now rows
        # first the planets, then cusps
        # if the planet is in a sign, print its in_sign_longitude in the column, otherwise print nothing
        for p in self._planets:
            output.add_row([p.name(),*utils.construct_varga_row(p),p.nakshatra_name(),p.nakshatra().elapsed()])

        for c in self._cusps:
            output.add_row([c.name(),*utils.construct_varga_row(c),c.nakshatra_name(),c.nakshatra().elapsed()])

        if isinstance(self, Rashi):
            ret = output.get_string(fields=list(["Object"] + list([sign for sign in [self.context.names.sign_names]][0]) + ["Nakshatra"] + ["Elapsed"]))
        else:
            ret = output.get_string(fields=list(["Object"] + list([sign for sign in [self.context.names.sign_names]][0])))

        return self.mkheader() + ret
        
    def mkheader(self):
        header = ""
        header += f"Varga {self._identifier} {self.varga_name()}\n"
        header += f"{self.sysflgstr} coordinates\n"
        header += f"{const.circle_name(self.context.circle)}\n"
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
        header += f"{self.context.location}\n"
        header += f"{self.context.timeJD}\n"
        return header



class Rashi(Varga):
    
    def __init__(self,planets,cusps,context):
        super().__init__(identifier=1,planets=planets,cusps=cusps,context=context)

