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

from libaditya import constants as const
from libaditya import utils

from libaditya.hd import constants as hdc


class YiLongitude:
    """
    YiLongitude is the most basic representation of the Human Design longitude
    which is the ecliptic longitude and its subdivisions thereof into
    hexagram, line, color, tone, and base
    
    note: this class takes no context, thus has no options
    it is possible to do sidereal, true sidereal and other shifted HD,
    but this most basic class those are built on will have this representation at the core
    in any case, if you have the ecliptic_longitude you can easily use other libaditya functions to get the data you want
    """

    # ok, obviously, if you change hdc.gate_one, you can make this whatever you want
    # if there are weird bugs, check and make sure this is where you want it to be
    # it should be 223+1/4 (13:15 of tropical Scorpio; that point on the ecliptic)
    gate_one = hdc.gate_one

    def __init__(self, longitude, gate_one=hdc.gate_one):
        self._longitude = longitude
        # declaring variables that are initialized in self.init_gate()
        self._distance = 0
        self._hexagrams = 0
        self._lines = 0
        self._colors = 0
        self._tones = 0
        self._bases = 0
        self._gate = self.init_gate(self._longitude) 

    def init_gate(self, longitude):
        # distance from gate 1 to the current gate in degrees
        dist = (longitude-self.gate_one)%360
        self._distance = dist
        # how many lines that amounts to
        self._bases = int(dist/hdc.base)
        self._tones, self._base = divmod(self._bases,5)
        self._base+=1 # base is 1-5, not 0-4
        self._colors, self._tone = divmod(self._tones,6)
        self._tone+=1
        self._lines, self._color = divmod(self._colors,6)
        self._color+=1
        # gate is how many gates from gate 1 the planet is
        # so index this into pconst.wheel
        gates_from, self._line = divmod(self._lines,6)
        self._line += 1 # lines are numbered 1-6, not 0-5
        self._hexagram = hdc.wheel[gates_from]
        self._hexagrams = int(gates_from)
        # gates are represented as a float, e.g., 12.1 = gate 12, line 1
        # easiest was to make a string "12.1", then convert to float
        return float(str(int(self._hexagram))+'.'+str(int(self._line)))

class HDLongitude(YiLongitude):
    """
    manages longitude functions for hd

    this is where we manage other systems, sidereal, true sidereal, other possibilities

    i personally dont use those systems, but im building it into here because it is a fun challenge
    to structure it appropriately

    fundamentally, i believe hd should be based on ecliptic longitude, regardless of what you believe about stars
    i dont really think it is meant to be used with signs primarily
    i think, since signs are what were familiar, the voice used these as a marker, but it appears the hd as a system
    itself does not use zodiac signs in any way. this also goes for various tropical systems, in particular "tropical and aditya"
    this library was named as adityas, but i dont believe using adityas with the sign shift should be applied to hd. i think
    gate 1 should be fixed at that point on the ecliptic; thus, that is how YiLongitude is implemented. It consists of the
    fundamental coordinates of human design, hexagram,line,color,tone, and base
    """

    def __init__(self, longitude, context):
        self.context = context
        super().__init__(longitude,self.context.hd_gate_one)

    def longitude(self):
        return self._longitude

    def raw_longitude(self):
        if self.context.toround[0]:
            return round(self.longitude(), self.context.toround[1])
        else:
            return self.longitude()

    def gate(self) -> str:
        return float(self.hexagram() + "." + str(self.line()))

    def hexagram(self) -> str:
        return hdc.gates[self._hexagram][self.context.hd_print_hexagrams]

    def gate_number(self) -> int:
        return self._hexagram

    def line(self) -> int:
        return self._line

    def color(self) -> int:
        return self._color        

    def tone(self) -> int:
        return self._tone        

    def base(self) -> int:
        return self._base        

    def gates(self):
        """
        returns complete number of hexagrams from hexagram 1
        """
        return self._hexagrams

    def lines(self):
        """
        returns complete number of lines from hexagram 1
        """
        return self._lines

    def colors(self):
        """
        returns complete number of colors from hexagram 1
        """
        return self._colors

    def tones(self):
        """
        returns complete number of tones from hexagram 1
        """
        return self._tones

    def bases(self):
        """
        returns complete number of bases from hexagram 1
        """
        return self._bases

    def gate_in_longitude(self):
        ginlong = (self.longitude()-(self.gate_one+(hdc.gate*hdc.wheel.index(self.gate_number()))))%360
        if self.context.toround[0]:
            return round(ginlong,self.context.toround[1])
        else:
            return ginlong

    def gate_elapsed(self):
        """
        returns percent how much this object has elapsed
        """
        return round(self.gate_in_longitude()/hdc.gate*100,2)

    def line_in_longitude(self):
        linlong = self.gate_in_longitude()-(hdc.line*(self.line()-1))
        if self.context.toround[0]:
            return round(linlong,self.context.toround[1])
        else:
            return linlong

    def line_elapsed(self):
        return round(self.line_in_longitude()/hdc.line*100,2)

    def color_in_longitude(self):
        cinlong = self.line_in_longitude()-(hdc.color*(self.color()-1))
        if self.context.toround[0]:
            return round(cinlong,self.context.toround[1])
        else:
            return cinlong

    def color_elapsed(self):
        return round(self.color_in_longitude()/hdc.color*100,2)

    def tone_in_longitude(self):
        tinlong = self.color_in_longitude()-(hdc.tone*(self.tone()-1))
        if self.context.toround[0]:
            return round(tinlong,self.context.toround[1])
        else:
            return tinlong

    def tone_elapsed(self):
        return round(self.tone_in_longitude()/hdc.tone*100,2)

    def base_in_longitude(self):
        binlong = self.tone_in_longitude()-(hdc.base*(self.base()-1))
        if self.context.toround[0]:
            return round(binlong,self.context.toround[1])
        else:
            return binlong

    def base_elapsed(self):
        return round(self.base_in_longitude()/hdc.base*100,2)

    def row(self):
        """
        return a list that can be part of a prettytable row
        the calling function will provide the "Planet" name
        output.align["Longitude"] = "l"
        output.align["Gate"] = "r"
        output.align["Gate Elapsed"] = "r"
        output.align["Line"] = "r"
        output.align["Line Elapsed"] = "r"
        "Color"
        "Color Elapsed"
        "Tone"
        "Tone Elapsed"
        "Base"
        "Base Elapsed"
        """
        return [str(self.raw_longitude()), str(self.hexagram()), str(str(self.gate_in_longitude())+f" ({self.gate_elapsed()} %)"), str(self.line()), str(str(self.line_in_longitude())+f" ({self.line_elapsed()} %)"), str(self.color()), str(str(self.color_in_longitude())+f" ({self.color_elapsed()} %)"), str(self.tone()), str(str(self.tone_in_longitude())+f" ({self.tone_elapsed()} %)"), str(self.base()), str(str(self.base_in_longitude())+str(f" ({self.base_elapsed()} %))"))]

    def row_definition(self):
        """
        return a list that can be part of a prettytable row
        the calling function will provide the "Planet" name
        output.align["Longitude"] = "l"
        output.align["Gate"] = "r"
        output.align["Line"] = "r"
        "Color"
        "Tone"
        "Base"
        """
        return [str(self.raw_longitude()), str(self.hexagram()), str(self.line()), str(self.color()), str(self.tone()), str(self.base())]

    def row_state(self):
        """
        return a list that can be part of a prettytable row
        the calling function will provide the "Planet" name
        output.align["Longitude"] = "l"
        output.align["Gate Elapsed"] = "r"
        output.align["Line Elapsed"] = "r"
        "Color Elapsed"
        "Tone Elapsed"
        "Base Elapsed"
        """
        return [str(self.raw_longitude()), str(str(self.gate_in_longitude())+f" ({self.gate_elapsed()} %)"), str(str(self.line_in_longitude())+f" ({self.line_elapsed()} %)"), str(str(self.color_in_longitude())+f" ({self.color_elapsed()} %)"), str(str(self.tone_in_longitude())+f" ({self.tone_elapsed()} %)"), str(str(self.base_in_longitude())+str(f" ({self.base_elapsed()} %))"))]

    def __repr__(self):
        """
        bare representation of the attributes of this HDLongitude
        """
        return str(self.row_definition() + self.row_state())

    def __str__(self):
        ret = ""
        ret += f"Longitude: {self.raw_longitude()}\n"
        ret += f"Hexagram: {self.hexagram()}\n"
        ret += f"Line: {self.line()}\n"
        ret += f"Color: {self.color()}\n"
        ret += f"Tone: {self.tone()}\n"
        ret += f"Base: {self.base()}"
        return ret

