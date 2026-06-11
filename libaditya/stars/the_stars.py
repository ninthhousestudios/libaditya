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

from functools import partial

from libaditya import constants as const
from libaditya import utils

"""
FixedStars populated from ephe/sefstars.txt
this is most of the stars in there
some have more than one traditional name; in that case only one appears here
unless I have manually added a different one

my additions are first; not a lot of them
"""

import swisseph as swe

from libaditya.objects import EphContext, Planet

from .fixed_star import correct_nomen_name
from .fixed_star import FixedStar
from .stellarium import Stellarium
from .utilities import *


class Constellation:
    """
    class to model a constellation in true sidereal astrology
    needs to have a first star and a last star, which can be used to
    find a midpoint between this constellation and thus next, and thus the sign boundary on the ecliptic
    """

    def __init__(
        self, first_star: FixedStar, last_star: FixedStar, context=EphContext()
    ):
        self._first_star = first_star
        self._last_star = last_star
        self.attributes = {"planets": [], "stars": []}
        self.set_attribute(("stars", self.first_star()))
        self.set_attribute(("stars", self.last_star()))

    def set_attribute(self, attrs):
        """
        attrs is a tuple ("attribute",value)
        add all of these to self.attributes
        attritube is a string that will be a dictionary key for value
        """
        key, value = attrs
        if key == "planets" or key == "stars":
            # the keys have values that are lists of Planet-s or FixedStar-s
            if isinstance(self.attributes[key], list):
                self.attributes[key].append(value)
        else:
            self.attributes[key] = value

    def planets(self):
        return self.attributes["planets"]

    def how_many_planets(self):
        return len(self.attributes["planets"])

    def stars(self):
        return self.attributes["stars"]

    def how_many_stars(self):
        return len(self.attributes["stars"])

    def objects(self):
        return self.attributes["planets"] + self.attributes["stars"]

    def how_many_objects(self):
        return len(self.attributes["planets"] + self.attributes["stars"])

    def first_star(self):
        return self._first_star

    def last_star(self):
        return self._last_star

    def name(self):
        return self._name

    def constellation_index(self):
        return self._constellation_index

    def constellation_number(self):
        return self.constellation_index() + 1

    def beginning(self):
        return self.attributes["beginning"]

    def end(self):
        return self.attributes["end"]

    def length(self):
        return self.attributes["length"]


class Aries(Constellation):
    def __init__(
        self,
        first_star=FixedStar("gamAri"),
        last_star=FixedStar("delAri"),
        context=EphContext(),
    ):
        self._name = "Aries"
        self._constellation_index = 0
        self._stars_to_place = []
        super().__init__(first_star, last_star, context)


class Taurus(Constellation):
    def __init__(
        self,
        first_star=FixedStar("omiTau"),
        last_star=FixedStar("zetTau"),
        context=EphContext(),
    ):
        self._name = "Taurus"
        self._constellation_index = 1
        super().__init__(first_star, last_star, context)


class Gemini(Constellation):
    def __init__(
        self,
        first_star=FixedStar("1Gem"),
        last_star=FixedStar("kapGem"),
        context=EphContext(),
    ):
        self._name = "Gemini"
        self._constellation_index = 2
        super().__init__(first_star, last_star, context)


class Cancer(Constellation):
    def __init__(
        self,
        first_star=FixedStar("chiCnc"),
        last_star=FixedStar("alfCnc"),
        context=EphContext(),
    ):
        self._name = "Cancer"
        self._constellation_index = 3
        super().__init__(first_star, last_star, context)


class Leo(Constellation):
    def __init__(
        self,
        first_star=FixedStar("kapLeo"),
        last_star=FixedStar("betLeo"),
        context=EphContext(),
    ):
        self._name = "Leo"
        self._constellation_index = 4
        super().__init__(first_star, last_star, context)


class Virgo(Constellation):
    def __init__(
        self,
        first_star=FixedStar("nu.Vir"),
        last_star=FixedStar("mu.Vir"),
        context=EphContext(),
    ):
        self._name = "Virgo"
        self._constellation_index = 5
        super().__init__(first_star, last_star, context)


class Libra(Constellation):
    def __init__(
        self,
        first_star=FixedStar("alf02Lib"),
        last_star=FixedStar("48Lib"),
        context=EphContext(),
    ):
        self._name = "Libra"
        self._constellation_index = 6
        super().__init__(first_star, last_star, context)


class Scorpio(Constellation):
    def __init__(
        self,
        first_star=FixedStar("delSco"),
        last_star=FixedStar("tauSco"),
        context=EphContext(),
    ):
        self._name = "Scorpio"
        self._constellation_index = 7
        super().__init__(first_star, last_star, context)


class Ophiucus(Constellation):
    def __init__(
        self,
        first_star=FixedStar("etaOph"),
        last_star=FixedStar("45Oph"),
        context=EphContext(),
    ):
        self._name = "Ophiucus"
        self._constellation_index = 8
        super().__init__(first_star, last_star, context)


class Sagittarius(Constellation):
    def __init__(
        self,
        first_star=FixedStar("gam02Sgr"),
        last_star=FixedStar("omeSgr"),
        context=EphContext(),
    ):
        self._name = "Sagittarius"
        self._constellation_index = 9
        super().__init__(first_star, last_star, context)


class Capricorn(Constellation):
    def __init__(
        self,
        first_star=FixedStar("betCap"),
        last_star=FixedStar("delCap"),
        context=EphContext(),
    ):
        self._name = "Capricorn"
        self._constellation_index = 10
        super().__init__(first_star, last_star, context)


class Aquarius(Constellation):
    def __init__(
        self,
        first_star=FixedStar("iotAqr"),
        last_star=FixedStar("phiAqr"),
        context=EphContext(),
    ):
        self._name = "Aquarius"
        self._constellation_index = 11
        super().__init__(first_star, last_star, context)


class Pisces(Constellation):
    def __init__(
        self,
        first_star=FixedStar("gamPsc"),
        last_star=FixedStar("alfPsc"),
        context=EphContext(),
    ):
        self._name = "Pisces"
        self._constellation_index = 12
        super().__init__(first_star, last_star, context)


class Ecliptic:
    number_to_name = {
        1: "Aries",
        2: "Taurus",
        3: "Gemini",
        4: "Cancer",
        5: "Leo",
        6: "Virgo",
        7: "Libra",
        8: "Scorpio",
        9: "Ophiucus",
        10: "Sagittarius",
        11: "Capricorn",
        12: "Aquarius",
        13: "Pisces",
    }

    def __init__(self, context=EphContext(), master=None):
        """
        master is the Chart() to which this belongs
        the import happens here in Ecliptic.__init__() because it causes circular import errors otherwise...
        which is appropriate, since it is circular
        this will let us set Planet attributes for true sidereal
        and to interact with the same Planets from Ecliptic()...eventually
        """
        self.context = context
        # if this import is anywhere else there is a circular import error
        from libaditya.charts import Chart

        # this is effectively master: Chart = Chart()...but has to here due to circularity of importing Chart elswhere
        # having master gives Ecliptic access to Planets and any other objects
        # this is sidereal and includes an ayanamsa, but Chart() itself can be anything
        # likewise, it doesnt matter if your Chart() is tropical, sidereal, or aditya, this true sidereal Ecliptic will be the same
        if master == None:
            master = Chart()
        self._master = master
        self._true_sidereal_master = self.master().sidereal(ayanamsa=97)
        self.context.sysflg = const.SID
        self.context.ayanamsa = 97
        utils.set_swe_true_sidereal_ayanamsa()
        self._constellations = self._init_Constellations()
        self._boundaries = self._init_boundaries()
        self._init_constellation_lengths()
        self._planets = self._init_Planets()

    def __iter__(self):
        return iter(self._constellations.values())

    def __getitem__(self, n):
        if isinstance(n, int):
            return self._constellations[self.number_to_name[n]]
        return self._constellations[n]

    def master(self):
        return self._master

    def true_sidereal_master(self):
        return self._true_sidereal_master

    def place(
        self, constellation: str, obj: Planet | FixedStar, attr: str = "planets"
    ):  # or "stars"
        """
        place an object in a constellation, such that
        Constellation().objects() will include object in the output
        """
        self[constellation].set_attribute((attr, obj))

    def place_stars(self):
        """
        read all stars from ephe/sefstars.txt
        so where the go in the ecliptic, if at all

        in Ecliptic, we only place stars that are within 10 degrees latitude of the ecliptic itself
        """
        swe_ids = read_swe_ids()  # from stars.utilities

        for swe_id in swe_ids:
            star = FixedStar(swe_id, self.context)
            if abs(star.latitude()) < 10:
                constellation = self.longitude_to_constellation(
                    star.ecliptic_longitude()
                )
                star.set_attribute(("constellation", constellation))
                constellation_name = constellation.split()[1]
                if star in self[constellation_name].stars():
                    # only place each star once
                    continue
                else:
                    self.place(constellation_name, star, "stars")

    def _init_Constellations(self):
        """
        intialize the 13 Constellation classes that make up the ecliptic, starting with Aries
        """
        consts = {}
        consts["Aries"] = Aries(
            FixedStar("gamAri", self.context),
            FixedStar("delAri", self.context),
            self.context,
        )
        consts["Taurus"] = Taurus(
            FixedStar("omiTau", self.context), FixedStar("zetTau", self.context)
        )
        consts["Gemini"] = Gemini(
            FixedStar("1Gem", self.context),
            FixedStar("kapGem", self.context),
            self.context,
        )
        consts["Cancer"] = Cancer(
            FixedStar("chiCnc", self.context),
            FixedStar("alfCnc", self.context),
            self.context,
        )
        consts["Leo"] = Leo(
            FixedStar("kapLeo", self.context),
            FixedStar("betLeo", self.context),
            self.context,
        )
        consts["Virgo"] = Virgo(
            FixedStar("nu.Vir", self.context),
            FixedStar("mu.Vir", self.context),
            self.context,
        )
        consts["Libra"] = Libra(
            FixedStar("alf02Lib", self.context),
            FixedStar("48Lib", self.context),
            self.context,
        )
        consts["Scorpio"] = Scorpio(
            FixedStar("delSco", self.context),
            FixedStar("tauSco", self.context),
            self.context,
        )
        consts["Ophiucus"] = Ophiucus(
            FixedStar("etaOph", self.context),
            FixedStar("45Oph", self.context),
            self.context,
        )
        consts["Sagittarius"] = Sagittarius(
            FixedStar("gam02Sgr", self.context),
            FixedStar("omeSgr", self.context),
            self.context,
        )
        consts["Capricorn"] = Capricorn(
            FixedStar("betCap", self.context),
            FixedStar("delCap", self.context),
            self.context,
        )
        consts["Aquarius"] = Aquarius(
            FixedStar("iotAqr", self.context),
            FixedStar("phiAqr", self.context),
            self.context,
        )
        consts["Pisces"] = Pisces(
            FixedStar("gamPsc", self.context),
            FixedStar("alfPsc", self.context),
            self.context,
        )
        # these keys allow me to use the output from CelestialObject.constellation() easily
        # it gives longitude as "DD:MM:SS Constellation"
        # so using the return from this: ret.split()[1] gives the Constellation, which
        # can be used as a key for "self"
        return consts

    def _init_boundaries(self) -> [float]:
        """
        find the boundaries according to the midpoint method

        returns a list of boundaries, the beginning of Aries, of Taurus, etc.
        """
        # calculate in order, starting with the last start of Aries to first star of Taurus, etc.
        # then put the last element to the front; the last element being last star of Pisces to first star of Aries,
        # i.e., the beginning of the zodiac
        ret = []
        for constellation in self:
            if constellation.name() == "Pisces":
                next_star_key = "Aries"
                next_star = self[next_star_key].first_star()
                distance = constellation.last_star().degrees_apart(
                    next_star.amsha_longitude()
                )
            else:
                # how far the next star of next constellation is from last star of this constellation
                next_star_key = self.number_to_name[
                    constellation.constellation_number() + 1
                ]
                next_star = self[next_star_key].first_star()
                distance = constellation.last_star().degrees_apart(
                    next_star.amsha_longitude()
                )
            # go forward half this distance from the star of this constellation; that is the end of this constellation
            # and the beginning of the next constellation
            midpoint = (
                constellation.last_star().amsha_longitude() + distance / 2
            ) % 360
            constellation.set_attribute(("end", midpoint))
            self[next_star_key].set_attribute(("beginning", midpoint))
            ret.append(midpoint)
        # the last point between Pisces and Aries is actually the first, so put it there
        return ret[-1:] + ret[:-1]

    def _init_constellation_lengths(self):
        """
        after finding the boundaries of each constellation, we can update them with their lengths
        """
        for constellation in self:
            end = constellation.end()
            begin = constellation.beginning()
            if constellation.name() == "Aries" and begin > 359:
                length = end + (360 - begin)
            elif constellation.name() == "Pisces" and begin < 1:
                length = (360 + end) - beginning
            else:
                length = end - begin
            constellation.set_attribute(("length", length))
        return

    def _init_Planets(self):
        """
        put the Planets into their appropriate constellations
        tell the Planet so it knows
        Planet-s are all in both self.master() and self.true_sidereal_master()
        this way, self.master() can have any options, and yet they can all include
        the true sidereal information
        """
        parent_planets = self.master().rashi().planets()
        true_sidereal_planets = self.true_sidereal_master().rashi().planets()
        # find out which constellation each planet is in
        for planet in true_sidereal_planets:
            # take the raw aries_longitude (i.e., ecliptic longitude with ayanamsa=97 and sysflg=const.SID)
            # i.e., the longitude from the 0 point, the beginning of aries constellation
            # and find the in-constellation longitude, e.g., 23:43:57 Taurus
            # set this attribute in both parent_planets and true_sidereal_planets
            constellation = self.longitude_to_constellation(planet.ecliptic_longitude())
            parent_planets[planet.identity()].set_attribute(
                ("constellation", constellation)
            )
            true_sidereal_planets[planet.identity()].set_attribute(
                ("constellation", constellation)
            )
            # now put the planets in their proper constellations
            # print(f"{planet.name()} {constellation=}")
            self.place(constellation.split()[1], planet, "planets")

    def longitude_to_constellation(self, long: float):
        """
        take a float longitude and return the name of its constellation
        """
        bounds = self.boundaries().copy()
        # so that if the beginning is 359.994 is changes to -.00599 so that "and" statements works in checking where the long is
        if bounds[0] < 1:
            bounds.append(bounds[0] + 360)
        else:
            bounds.append(bounds[0])
        if bounds[0] > 359:
            bounds[0] = -(360 - bounds[0])
        cnames = const.names["eng"]["zodiac"].copy()
        cnames.insert(8, const.names["eng"]["ophiucus"])
        for n in range(0, len(bounds)):
            # print(f"l_to_c: {n=} {long=} {bounds[n]=} {bounds[(n+1)%13]=}")
            if long >= bounds[n] and long < bounds[n + 1]:
                in_long = long - bounds[n]
                if self.context.toround[0]:
                    in_long = round(in_long, self.context.toround[1])
                return f"{utils.dec2dmsstr(in_long)} {cnames[n]} ({round((in_long / self[cnames[n]].length()) * 100, 3)} %)"

    def boundaries(self):
        return self._boundaries

    def constellations(self):
        return self._constellations

    def aries(self):
        return self.constellations()["Aries"]

    def taurus(self):
        return self.constellations()["Taurus"]

    def gemini(self):
        return self.constellations()["Gemini"]

    def cancer(self):
        return self.constellations()["Cancer"]

    def leo(self):
        return self.constellations()["Leo"]

    def virgo(self):
        return self.constellations()["Virgo"]

    def libra(self):
        return self.constellations()["Libra"]

    def scorpio(self):
        return self.constellations()["Scorpio"]

    def ophiucus(self):
        return self.constellations()["Ophiucus"]

    def sagittarius(self):
        return self.constellations()["Sagittarius"]

    def capricorn(self):
        return self.constellations()["Capricorn"]

    def aquarius(self):
        return self.constellations()["Aquarius"]

    def pisces(self):
        return self.constellations()["Pisces"]


class TheStars:
    """
    represents all of the fixed stars
    should be the main interface through which to interact with the stars
    but you can also use fixed_stars.FixedStar()
    """

    def __init__(self, context=EphContext(), stellarium=False) -> dict:
        self.context = context
        # defined just above
        self.the_stellarium = None
        if stellarium:
            self.the_stellarium = self.init_Stellarium()

    def __getitem__(self, key):
        """
        keys:
        (,)noMen for swe objects
        other for stellarium; best is to use HIP object has it

        instantiate star denoted by key with this context
        so you can or not used "," for the (,)noMen name
        (,)noMen name is used by swisseph (swe)
        "HIP nnnnn" is used by Stellarium
        also, names with spaces, e.g., "M 31", which is a galaxy, can be instantiated into a FixedStar
        """
        if "st:" in key:
            # all of these indicate objects that can be found with Stellarium().info(key)
            # or in stars.the_stars.the_stars
            if self.the_stellarium:
                # the_stellarium is our Stellarium() object
                # the key is a we want from Stellarium, so we have to pass the "phone", so to speak
                # return whatever object Stellarium finds
                return FixedStar(key, self.context, self.the_stellarium)
        key = correct_nomen_name(key)
        return FixedStar(key, self.context)

    def search_star_interactive(self, bitflags=swe.FLG_TROPICAL) -> FixedStar:
        """
        this returns a FixedStar class of the specific star, if there is one, else error
        e.g., to get Aldebaran:
        >>>  aldebaran = TheStars().search_star_interactive()
        enter "alde" (Enter)
        this gives you the constructor
        <class 'libaditya.stars.the_stars.Aldebaran'>
        a star by itself needs a context; you can use Chart().context to pass it the information for any chart
        you are working with and it will intialize accordingly
        """
        pattern = input(
            "Enter first few letters of traditional name as appears in .../ephe/sefstars.txt: "
        )
        if not "," in pattern:
            # then they are searching a traditional name, so include wildcard
            pattern = f"{pattern}%"
        information, name, retflags = swe.fixstar2_ut(
            pattern, self.context.timeJD.jd_number(), bitflags
        )
        print(
            f"Star: {name} appears at {information[0]} longitude on {self.context.timeJD}"
        )
        return self[name.split(",")[1]]

    def stellarium(self):
        return self.the_stellarium

    def init_Stellarium(self, ip="127.0.0.1", port="8090", password=""):
        """
        if you are using this alot, assign the return value to a variable
        if not, it will reconnect each time, making each operation very slow
        so: not: chart(context).stars()["Andromeda"], chart(context).stars()["OmiTau"]
        but: thestars=chart(context).stars(), then thestars["Andromeda"], etc.
        note: both swe and stellarium objects can be instantiated using [] notation
        it works for any key,object pair in the dictionary stars.the_stars.the_stars=TheStars._the_stars

        if you get an http error, it is because stellarium is not on, or the RemoteControl plugin is not on
        start stellarium, press F2, go the rightmost tab, Plugins. on the left, go down to "Remote Control"
        bottom left of the information about the plugin:
        Options
        Load at startup
        if "Load at startup" is not checked, then check it and restart stellarium
        then go back to F2->Plugins->Remote Control
        then click "Configure"
        click "Server Enabled"; that will turn the server on, then you can use the default ip, port, and password options here
        if you want it to load automatically, check "Enable automatically on startup"
        """
        try:
            return Stellarium(self.context, ip, port, password)
        except:
            print("Stellarium not available...")
            return
