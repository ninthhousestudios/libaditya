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

class Nakshatra:
    def __init__(self, occupant):
        self._occupant = occupant
        self.context = occupant.context
        self.timeJD = occupant.timeJD
        self.base_long = self._occupant.ecliptic_longitude()
        self.ayanamsa = self.context.ayanamsa
        self._naksize = 360/28 if self.ayanamsa == 101 else 13+(1/3)
        # ashlong means the number of degrees from ashvini; in most cases, the sidereal longitude
        self.ash_long = self.init_ash_long()

    def __str__(self):
        nak = f"Nakshatra of {self.occupant()}\n"
        base_long = f"base longitude: {self.base_longitude()}\n"
        ash_long = f"Degrees from beginning of ashvini: {self.ashvini_longitude()}\n"
        ayana = f"Using {self.ayanamsa_name()} ayanamsa\n"
        nakshatra = f"{self.nakshatra()}\n"
        return nak + base_long + ash_long + ayana + nakshatra

    def __repr__(self):
        """
        return neutral string representation for database
        returns the English name of this nakshatra, in hopes that everyone can type that on any keyboard
        ...my terminal emunlator cannot properly disply devangari
        """
        return f"{self.identity()}"
#        nak = f"Nakshatra of {self.occupant()}\n"
#        base_long = f"base longitude: {self.base_longitude()}\n"
#        ash_long = f"Degrees from beginning of ashvini: {self.ashvini_longitude()}\n"
#        ayana = f"Using {self.ayanamsa_name()} ayanamsa\n"
#        nakshatra = f"{self.nakshatra()}\n"
#        return nak + base_long + ash_long + ayana + nakshatra

    def occupant(self):
        return self._occupant.name()

    def naksize(self):
        return self._naksize

    def base_longitude(self):
        return self.base_long

    def ashvini_longitude(self):
        return self.ash_long

    def index(self):
        if self.ayanamsa == 101:
            return int(self.ashvini_longitude()/self.naksize())%28
        return int(self.ashvini_longitude()/self.naksize())%27

    def identity(self):
        """
        return the English name to use as an all purpose nakshatras dictionary index
        ['Ashvini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'P. Phalguni', 'U. Phalguni', 'Hasta', 'Chitra', 'Svati', 'Vishakha', 'Anuradha', 'Jyeshtha', 'Mula', 'P. Ashadha', 'U. Ashadha', 'Shravana', 'Danishtha', 'Shatabhisha', 'P. Bhadrapada', 'U. Bhadrapada', 'Revati'
        """
        nak_key = "nakshatras_28eq" if self.ayanamsa == 101 else "nakshatras"
        return const.names["eng"][nak_key][self.index()]

    def nakshatra(self):
        nak_key = "nakshatras_28eq" if self.ayanamsa == 101 else "nakshatras"
        return const.names[self.context.names_type][nak_key][self.index()]

    def degrees_elapsed(self):
        if self.context.toround[0] == True:
            return round(self.ashvini_longitude()-(self.index()*self.naksize()),2)
        else:
            return self.ashvini_longitude()-(self.index()*self.naksize())

    def degrees_remaining(self):
        if self.context.toround[0] == True:
            return round(self.naksize()-self.degrees_elapsed(),2)
        else:
            return self.naksize()-self.degrees_elapsed()

    def percent_elapsed(self):
        if self.context.toround[0] == True:
            return round((self.degrees_elapsed()/self.naksize())*100,2)
        else:
            return (self.degrees_elapsed()/self.naksize())*100

            return False
    def elapsed(self):
        return f"{self.degrees_elapsed()} ({self.percent_elapsed()} %)" 
    
    def print_in_longitude(self):
        print(f"Elapsed: {self.degrees_elapsed()} deg ({round((self.degrees_elapsed() / self.naksize()) * 100, 3)} %)")
        degremain = self.degrees_remaining()
        print(
            f"Remaining: {degremain} deg ({round((degremain / self.naksize()) * 100, 3)} %)"
        )

    def init_ash_long(self):
        from .planets import Planet
        from .cusps import Cusp
        # otherwise, find the number of degrees from ashvini
        # insert custom ayanamsa codes and methods here
        if self.ayanamsa == -1:
            return self.base_longitude()
        if self.ayanamsa == 101:
            return self.base_longitude()
        if self.ayanamsa == 98:
            return self.dhruva_gc_equatorial()
        if self.ayanamsa == 99:
            return self.vedanga_jyotisha_ecliptic()
        if self.ayanamsa == 100:
            return self.vedanga_jyotisha_equatorial()
        if isinstance(self._occupant, Planet):
            return self.init_ash_long_Planet()
        if isinstance(self._occupant, Cusp):
            return self.init_ash_long_Cusp()
        else:
            print(f"instance of type {type(self._occupant)} cannot be in a nakshatra")

    def init_ash_long_Planet(self):
        swe.set_sid_mode(self.ayanamsa)
        long = swe.calc_ut(self.timeJD.jd_number(), self._occupant.pnumber, swe.FLG_SIDEREAL)[0][0]
        long = self.ketuize(long)
        return long

    def init_ash_long_Cusp(self):
        swe.set_sid_mode(self.ayanamsa)
        cusps, _, _, _ = swe.houses_ex2(
            self._occupant.timeJD.jd_number(),
            self._occupant.location.lat,
            self._occupant.location.long,
            self._occupant.hsys,
            swe.FLG_SIDEREAL,
        )
        return cusps[self._occupant.cusp_index()]

    def ayanamsa_name(self):
        return const.ayanamsa_name(self.ayanamsa)

    def ketuize(self,long):
        from .planets import Ketu
        if isinstance(self._occupant,Ketu):
            long = (long-180)%360
        return long

    def dhruva_gc_equatorial(self):
        from .planets import Planet
        from .cusps import Cusp
        gcequ=swe.fixstar(",SgrA*",self.timeJD.jd, swe.FLG_EQUATORIAL)[0][0]
        mula=gcequ-(self.naksize()/2)
        ashvini=mula-(18*self.naksize())
        if isinstance(self._occupant,Planet):
            equlong = swe.calc_ut(self.timeJD.jd, self._occupant.pnumber, swe.FLG_EQUATORIAL)[0][0]
            equlong = self.ketuize(equlong)
        if isinstance(self._occupant,Cusp):
            equlong = swe.cotrans((self.base_longitude(),0,1),self.timeJD.ecliptic_obliquity())[0]
        if equlong < ashvini:
            equlong+=360
        return equlong-ashvini

    def vedanga_jyotisha_ecliptic(self):
        """
        dhanishta begins at the winter solstice, i.e., 270 degrees ecliptic longitude
        this puts ashivini to start at 336+2/3 ecliptic longitude
        so our "ayanamsa" is 23+1/3, in order to line up with our nakshatra list
        but we have to add this, so that ashvini+ayanamsa=0
        """
        # aval = 23+1/3
        # this is how it is calculated
        # find where ashvini starts; it is five nakshatras after dhanishta
        ashvini = 360 - (270+5*self.naksize())
        return (self.base_longitude()+ashvini)%360

    def vedanga_jyotisha_equatorial(self):
        """
        dhanishta at the winter solstice, but equatorial nakshatras
        so find the equatorial longitude of the solstice, then
        determine nakshatras from there with equatorial planet longitudes
        the projection of the winter solstice onto the equator is always at 270 equatorial longitude
        but im calculating it just for the form of it, on principle
        """
        from .planets import Planet
        from .cusps import Cusp
        # equatorial longitude of the winter solstice
        # the swe.calc call is for the ecliptic_obliquity, which is required for coordinate transformations
        # according to the documentation, '-' is used to go from ecliptic to equatorial, which we are doing here
        solequ = swe.cotrans((270,0,1),-swe.calc(self.timeJD.jd,swe.ECL_NUT)[0][0])[0]
        # find where equatorial ashvini starts; it is five nakshatras after dhanishta
        ashvini = 360 - (solequ+5*self.naksize())
        # equatorial longitude of this planet
        if isinstance(self._occupant,Planet):
            equlong = swe.calc_ut(self.timeJD.jd, self._occupant.pnumber, swe.FLG_EQUATORIAL)[0][0]
            equlong = self.ketuize(equlong)
        if isinstance(self._occupant,Cusp):
            equlong = swe.cotrans((self.base_longitude(),0,1),self.timeJD.ecliptic_obliquity())[0]
        return (equlong+ashvini)%360

class Ashvini(Nakshatra):
    pass

class Nakshatras:

    def __init__(self, occupants, context):
        self._occupants = occupants
        self.context = context
        self.nakshatras = self.init_Nakshatras()

    def __iter__(self):
        return iter(self.nakshatras)

    def __getitem__(self,n):
        return self.nakshatras[n]

    def __str__(self):
        output = PrettyTable()
        output.field_names = [f"{self.occupant_type()}", "Nakshatra", "Percent Elapsed"]
        output.align[f"{self.occupant_type()}"] = "l"
        output.align["Nakshatra"] = "l"
        output.align["Percent Elapsed"] = "r"

        for occupant in self.nakshatras:
            output.add_row([occupant.occupant(),occupant.nakshatra(),f"{occupant.degrees_elapsed()} ({occupant.percent_elapsed()} %)"])

        ret = output.get_string(fields=[f"{self.occupant_type()}","Nakshatra","Percent Elapsed"])

        return self.mkheader() + ret

    def __repr__(self):
        return self.mkheader()

    def occupant_type(self) -> str:
        from .planets import Planets
        from .cusps import Cusps
        if isinstance(self._occupants,Planets):
            return "Planet"
        elif isinstance(self._occupants,Cusps):
            return "Cusp"
        else:
            raise TypeError("cannot make Nakshatras from this type")

    def init_Nakshatras(self):
        ret = []
        for occupant in self._occupants:
            ret.append(occupant.nakshatra())
        return ret

    def mkheader(self):
        from .planets import Planets
        from .cusps import Cusps
        if isinstance(self._occupants,Planets):
            return self.mkheader_Planets()
        elif isinstance(self._occupants,Cusps):
            return self.mkheader_Cusps()
        else:
            raise TypeError("cannot make Nakshatras from this type")

    def mkheader_Planets(self):
        header = "Nakshatras of the planets:\n"
        header += f"{self.context.timeJD}\n"
        header += f"using {const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
        return header

    def mkheader_Cusps(self):
        header = "Nakshatras of the cusps:\n"
        header += f"{self.context.timeJD}\n"
        header += f"{self.context.location}\n"
        header += f"using {const.ayanamsa_name(self.context.ayanamsa)} ayanamsa\n"
        header += f"using house system {self._occupants[0].house_system()}\n"
        return header
