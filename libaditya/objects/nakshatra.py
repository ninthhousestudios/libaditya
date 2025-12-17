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
from .planet import Planet, Moon, Ketu
from .cusps import Cusp

from libaditya import constants as const


class Nakshatra:
    def __init__(self, occupant=Moon()):
        self.naksize = 13+(1/3)
        self._occupant = occupant
        self.context = occupant.context
        self.timeJD = occupant.timeJD
        self.base_long = self._occupant.raw_longitude()
        self.is_sidereal = self.is_it_sidereal_already(self.context.sysflg)
        self.ayanamsa = self.context.ayanamsa
        # ashlong means the number of degrees from ashvini; in most cases, the sidereal longitude
        self.ash_long = self.init_ash_long()

    def __str__(self):
        nak = f"Nakshatra of {self.occupant()}\n"
        base_long = f"base longitude: {self.base_longitude()}\n"
        ash_long = f"Degrees from beginning of ashvini: {self.ashvini_longitude()}\n"
        ayana = f"Using {self.ayanamsa_name()} ayanamsa\n"
        return nak + base_long + ash_long + ayana

    def occupant(self):
        return self._occupant.name()

    def base_longitude(self):
        return self.base_long

    def ashvini_longitude(self):
        return self.ash_long

    def index(self):
        return int(self.ashvini_longitude()/self.naksize)

    def nakshatra(self):
        return self.context.nakshatras[self.index()]

    def is_it_sidereal_already(self, sysflg):
        if sysflg == swe.FLG_SIDEREAL or sysflg == (swe.FLG_SIDEREAL | swe.FLG_TOPOCTR):
            return True
        else:
            return False

    def init_ash_long(self):
        # otherwise, find the number of degrees from ashvini
        # insert custom ayanamsa codes and methods here
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
        if isinstance(self._occupant,Ketu):
            long = (long-180)%360
        return long

    def dhruva_gc_equatorial(self):
        gcequ=swe.fixstar(",SgrA*",self.timeJD.jd, swe.FLG_EQUATORIAL)[0][0]
        mula=gcequ-(self.naksize/2)
        ashvini=mula-(18*self.naksize)
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
        ashvini = 360 - (270+5*self.naksize)
        return (self.base_longitude()+ashvini)%360

    def vedanga_jyotisha_equatorial(self):
        """
        dhanishta at the winter solstice, but equatorial nakshatras
        so find the equatorial longitude of the solstice, then
        determine nakshatras from there with equatorial planet longitudes
        the projection of the winter solstice onto the equator is always at 270 equatorial longitude
        but im calculating it just for the form of it, on principle
        """
        # equatorial longitude of the winter solstice
        # the swe.calc call is for the ecliptic_obliquity, which is required for coordinate transformations
        # according to the documentation, '-' is used to go from ecliptic to equatorial, which we are doing here
        solequ = swe.cotrans((270,0,1),-swe.calc(self.timeJD.jd,swe.ECL_NUT)[0][0])[0]
        # find where equatorial ashvini starts; it is five nakshatras after dhanishta
        ashvini = 360 - (solequ+5*self.naksize)
        # equatorial longitude of this planet
        if isinstance(self._occupant,Planet):
            equlong = swe.calc_ut(self.timeJD.jd, self._occupant.pnumber, swe.FLG_EQUATORIAL)[0][0]
            equlong = self.ketuize(equlong)
        if isinstance(self._occupant,Cusp):
            equlong = swe.cotrans((self.base_longitude(),0,1),self.timeJD.ecliptic_obliquity())[0]
        return (equlong+ashvini)%360
