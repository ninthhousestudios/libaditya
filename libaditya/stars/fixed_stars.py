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
import os

from libaditya import constants as const

from libaditya.objects import Longitude, CelestialObject, EphContext, Earth

stars_path = os.path.dirname(os.path.realpath(__file__))
the_stars_file = stars_path + "/the_stars.py"

class TheStars:

    def __init__(self, context=EphContext(), stars_file=const.stars_file) -> dict:
        self.context = context
        with open(stars_file,"r") as stars_fd:
            the_stars_lines = dict() 
            the_lines = stars_fd.readlines()
            for n,line in enumerate(the_lines):
                if "#" in line:
                    # a comment, continue
                    continue
                the_stars_lines[n] = line
            self._the_stars_lines = the_stars_lines
        self._the_stars = self.init_the_stars()

    def init_the_stars(self):
        """
        here we take self._the_stars_lines and create a dictionary
        "nomenclature_nature": "traditiona_name" -> self._the_stars

        the_stars_file (.../stars/the_stars.py) has all the FixedStar classes for each star
        read just the name of each class and pass as a dictionary key to use as a constructor
        """
        with open(the_stars_file,"r") as starsfd:
            lines = stars.readlines() 
        the_stars = dict()
        for line in lines:
            if not "class" in line:
                continue
            # line has the form: class Name(FixedStar):
            value = line.split(" ")[1].split("(")[0]
        return the_stars

    def the_stars(self):
        """
        this is the main interface here
        essentially is a dictionary, with the key being "nomenclature" name of the star
        the value is the traditional name of the star
        """
        return self._the_stars

    def search_star_interactive(self, bitflags=swe.FLG_TROPICAL):
        pattern = input("Enter first few letters of traditional name as appears in .../ephe/sefstars.txt: ")
        if not "," in pattern:
            # then they are searching a traditional name, so include wildcard
            pattern = f"{pattern}%"
        information, name, retflags = swe.fixstar2_ut(pattern,self.context.timeJD.jd_number(),bitflags)
        print(f"Star: {name} appears at {information[0]} longitude on {self.context.timeJD}")
        print(f"{Longitude(information[0],1).longitude()}")

    def print_the_stars(self) -> None:
        for n,(nomen,trad) in enumerate(self.the_stars().items()):
            print(f"{n}\t{nomen.strip()}\t{trad.strip()}")


class FixedStar(Longitude,CelestialObject):

    def __init__(self, swe_id: str, context: EphContext = EphContext()):
        self.context = context
        self.system = self.context.sysflg
        self.sysflg = self.system | swe.FLG_SPEED
        # swe_id is the nomenclature name of the star
        # can pass it with or without comma
        self._swe_id = swe_id if "," in swe_id else ","+swe_id
        try:
            # if it works, the swe_id is valid
            swe.fixstar2_ut(self._swe_id,self.context.timeJD.jd_number())
        except:
            # if not, assume it is a search
            # so remove "," from beginning, add "%" to end for wildcard
            self._swe_id = self._swe_id[1:]+"%"
        # self._coords is a 6-tuple
        # will be unpacked into FixedStar.longitude(), etc., for each value in the tuple
        (self.long, self.lat, self.dist, self.long_speed, self.lat_speed, self.dist_speed), self._name, _ = self.init_coords()
        self._name, self._swe_id = self._name.split(",")
        (self._right_ascension, self._declination, _,_,_,_) = swe.fixstar2_ut(self.swe_id(),self.context.timeJD.jd_number(),swe.FLG_EQUATORIAL)[0]
        # now that we know which star this is, make sure it has the right swe_id()
        super().__init__(self.long,1)

    def init_coords(self):
        loc = self.context.location.swe_location()
        if self.system == const.SID:
            # will need to add custom ayanamsas here
            if self.ayanamsa() == 98:
                self._ayanamsa = 36
            swe.set_sid_mode(self.ayanamsa())
        if self.system == const.TOPO:
            swe.set_topo(loc[0], loc[1], loc[2])
        if self.system == (const.SID | const.TOPO):
            swe.set_sid_mode(self.ayanamsa())
            swe.set_topo(loc[0], loc[1], loc[2])
        return swe.fixstar2_ut(self._swe_id, self.context.timeJD.jd_number(), self.sysflg if self.sysflg >= 0 else 0)

    def __eq__(self, fs2):
        return self.swe_id() == fs2.swe_id()

    # longitude is taken care of by inheritor, Longitude

    def name(self):
        return self._name

    def swe_id(self):
        return ","+self._swe_id

    def identity(self):
        return self.swe_id()
        
    def magnitude(self):
        return swe.fixstar2_mag(self.swe_id())[0]

