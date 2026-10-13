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
from dataclasses import dataclass, replace

from libaditya.objects import Planet, RashiBala
from libaditya.calc import Varga
from libaditya.calc import vimshottari
from libaditya.calc.panchanga import Panchanga
from libaditya.calc.swe_functions import SWERashi
from libaditya.calc.hellenistic import Hellenistic
from libaditya.calc.returns import Returns
from libaditya.calc.avasthas import (LajjitaadiAvasthas, BaladiAvasthas,
                                     JagradadiAvasthas, DeeptadiAvasthas,
                                     ShayanadiAvasthas)
from libaditya.draw.draw_sbc import DrawSBC

from .jaimini_get import JaiminiGet


@dataclass
class AkritiYoga:
    name: str
    translation: str
    to_move: int
    houses: tuple

    def __str__(self):
        return f"{self.name} ({self.translation}): {self.to_move} to move — houses {self.houses}"

    def __repr__(self):
        return f"AkritiYoga({self.name!r}, to_move={self.to_move})"


@dataclass
class NabhasaYoga:
    name: str
    translation: str
    category: str
    to_move: int
    condition: str

    def __str__(self):
        return f"{self.name} ({self.translation}): {self.to_move} to move — {self.condition}"

    def __repr__(self):
        return f"NabhasaYoga({self.name!r}, category={self.category!r}, to_move={self.to_move})"


@dataclass
class MahapurushaYoga:
    name: str
    translation: str
    planet: str
    present: bool
    house: int
    dignity: str

    def __str__(self):
        if self.present:
            return f"{self.name} ({self.translation}): {self.planet} in house {self.house}, {self.dignity}"
        return f"{self.name} ({self.translation}): not present"

    def __repr__(self):
        return f"MahapurushaYoga({self.name!r}, planet={self.planet!r}, present={self.present})"


@dataclass
class SolarYoga:
    name: str
    planets: list
    present: bool

    def __str__(self):
        if self.present:
            return f"{self.name}: {', '.join(self.planets)}"
        return f"{self.name}: not present"

    def __repr__(self):
        return f"SolarYoga({self.name!r}, present={self.present})"


@dataclass
class LunarYoga:
    name: str
    planets: list
    present: bool

    def __str__(self):
        if self.present:
            return f"{self.name}: {', '.join(self.planets)}"
        return f"{self.name}: not present"

    def __repr__(self):
        return f"LunarYoga({self.name!r}, present={self.present})"


class Rashi(Varga,SWERashi,JaiminiGet,RashiBala,DrawSBC,Hellenistic,Returns,LajjitaadiAvasthas,BaladiAvasthas,JagradadiAvasthas,DeeptadiAvasthas,ShayanadiAvasthas):

    def __init__(self,context,chart):
        self.master = chart
        super().__init__(context=context,amsha=1)
        self._dig_balas = self.init_dig_balas()
        self._saptavargaja_balas = self.init_saptavargaja_balas()
        self._sama_visama_balas = self.init_sama_visama_balas()
        self._kendradi_balas = self.init_kendradi_balas()
        self._drig_balas = self.init_drig_balas()
        self._lajjitaadi_avasthas = self.lajjitaadi_avasthas()
        self._baladi_avasthas = self.baladi_avasthas()
        self._jagradadi_avasthas = self.jagradadi_avasthas()
        self._deeptadi_avasthas = self.deeptadi_avasthas()
        self._shayanadi_avasthas = self.shayanadi_avasthas()

    def planets(self):
        return self._planets

    def ecliptic(self):
        return self._ecliptic

    def cusps(self):
        return self._cusps

    def signs(self):
        return self._signs

    def avasthas(self):
        from libaditya import print_functions as printf
        printf.print_avasthas(self._lajjitaadi_avasthas,
                              self._baladi_avasthas,
                              self._jagradadi_avasthas,
                              self._deeptadi_avasthas,
                              self._shayanadi_avasthas)

    def house_position(self, planet: str, hsys=None) -> float:
        """
        a wrapper for the function swe.house_pos()
        planet is the Planet.identity(), i.e., the english name of the desired planet
        """
        armc = self.cusps().armc()
        lat = self.context.location.latitude()
        eo = self.context.timeJD.ecliptic_obliquity()
        planet = self.planets()[planet]
        planet_coords = (planet.ecliptic_longitude(),planet.latitude())
        if hsys == None:
            hsys = self.context.hsys
        return swe.house_pos(armc,lat,eo,planet_coords,hsys.encode())

    def Master(self):
        """
        return the Chart that spawned it
        """
        return self.master

    def panchanga(self, **kwargs):
        """
        panchanga is here because it has to do with the sun and moon, with time
        that is the Rashi chart essentially
        none of the other vargas really need a separate class, because they are really subsections of this class
        which is why Rashi can hopefully reach all the Vargas

        Panchanga.__str__ prints the basic panchagna, and also the panchanga addendum
        __repr__ prints only the basic time and panchanga information
        """
        context = replace(self.context,**kwargs)
        return Panchanga(context)

    def print_current_vimshottari_dasha(self,yrlen="saura",levels=5):
        vimshottari.print_current_vdasha(self.context,yrlen,levels)
        return

    def rashi_argala(self) -> [[Planet],[Planet],[Planet]]:
        """
        it returns a list a lists, where each sublist is the combinatino of the corresponding argala lists of lagna and seventh

        this combines the argala formed to both 1st and 7th
        """
        lagna_arg = self.argala(self.signs().lagna())
        seventh_arg = self.argala(self.signs()[self.signs().lagna().astrological_signs_forward(7)])
        ret = [[],[],[]]
        for n,arg in enumerate(lagna_arg):
            for planet in lagna_arg[n]:
                ret[n].append(planet)
            for planet in seventh_arg[n]:
                ret[n].append(planet)
        return ret
        # each arg has three elements; put all of lagna_arg[0] together with seventh_arg[0], etc.


    def akriti_yogas(self):
        """
        find the 20 akriti yogas in this Rashi varga
        these are rarely found perfectly or completely, so we find
        how many planets would need to be moved to create each
        for these yogas, planets means the seven embodied planets, i.e., karakas (Sun-Saturn)
        returns a list of AkritiYoga dataclasses sorted by to_move ascending
        """
        akritis = []
        lagna_sign = self.signs().lagna()
        # karaka counts per house (1-indexed by house number from lagna)
        h = {}
        for i in range(1, 13):
            h[i] = self.signs()[lagna_sign.astrological_signs_forward(i)].how_many_karakas()

        # for vajra/yava: count benefic and malefic karakas per house
        # uses fixed natural classification: Moon, Mercury, Jupiter, Venus = benefic
        # Sun, Mars, Saturn = malefic
        FIXED_MALEFICS = {"Sun", "Mars", "Saturn"}
        bh = {}  # benefic karaka count per house
        mh = {}  # malefic karaka count per house
        for i in range(1, 13):
            sign = self.signs()[lagna_sign.astrological_signs_forward(i)]
            karakas = sign.karakas()
            b = 0
            m = 0
            for k in karakas:
                if k.identity() in FIXED_MALEFICS:
                    m += 1
                else:
                    b += 1
            bh[i] = b
            mh[i] = m

        def tm(*houses):
            """to_move: how many of the 7 karakas are outside the given houses"""
            return 7 - sum(h[i] for i in houses)

        def tm_dist(*houses):
            """to_move for yogas requiring distribution across houses.
            accounts for both planets outside AND empty required houses,
            since a planet must be moved into each empty house."""
            outside = 7 - sum(h[i] for i in houses)
            empty = sum(1 for i in houses if h[i] == 0)
            return max(outside, empty)

        # --- trine yogas ---
        akritis.append(AkritiYoga("Sringataka", "mountain having three peaks",
                                  tm(1, 5, 9), (1, 5, 9)))
        akritis.append(AkritiYoga("Hala Artha", "plough",
                                  tm(2, 6, 10), (2, 6, 10)))
        akritis.append(AkritiYoga("Hala Kama", "plough",
                                  tm(3, 7, 11), (3, 7, 11)))
        akritis.append(AkritiYoga("Hala Moksha", "plough",
                                  tm(4, 8, 12), (4, 8, 12)))

        # --- gada yogas: all planets in two successive angles ---
        akritis.append(AkritiYoga("Gada 1/4", "mace",
                                  tm(1, 4), (1, 4)))
        akritis.append(AkritiYoga("Gada 4/7", "mace",
                                  tm(4, 7), (4, 7)))
        akritis.append(AkritiYoga("Gada 7/10", "mace",
                                  tm(7, 10), (7, 10)))
        akritis.append(AkritiYoga("Gada 10/1", "mace",
                                  tm(10, 1), (10, 1)))

        # --- two-house angle yogas ---
        akritis.append(AkritiYoga("Sakata", "cart",
                                  tm(1, 7), (1, 7)))
        akritis.append(AkritiYoga("Vihaga", "skygoer",
                                  tm(4, 10), (4, 10)))

        # --- four-house yogas ---
        akritis.append(AkritiYoga("Kamala", "lotus",
                                  tm(1, 4, 7, 10), (1, 4, 7, 10)))
        akritis.append(AkritiYoga("Vapi Panaphara", "pond",
                                  tm(2, 5, 8, 11), (2, 5, 8, 11)))
        akritis.append(AkritiYoga("Vapi Apoklima", "pond",
                                  tm(3, 6, 9, 12), (3, 6, 9, 12)))

        # --- vajra and yava: benefic/malefic distribution in angles ---
        # vajra: all benefics in 1 & 7, all malefics in 4 & 10
        vajra_correct = (bh[1] + bh[7]) + (mh[4] + mh[10])
        akritis.append(AkritiYoga("Vajra", "thunderbolt",
                                  7 - vajra_correct, (1, 4, 7, 10)))
        # yava: all malefics in 1 & 7, all benefics in 4 & 10
        yava_correct = (mh[1] + mh[7]) + (bh[4] + bh[10])
        akritis.append(AkritiYoga("Yava", "barleycorn",
                                  7 - yava_correct, (1, 4, 7, 10)))

        # --- four consecutive house yogas ---
        akritis.append(AkritiYoga("Yupa", "sacrificial pillar",
                                  tm(1, 2, 3, 4), (1, 2, 3, 4)))
        akritis.append(AkritiYoga("Sara", "arrow",
                                  tm(4, 5, 6, 7), (4, 5, 6, 7)))
        akritis.append(AkritiYoga("Shakti", "power",
                                  tm(7, 8, 9, 10), (7, 8, 9, 10)))
        akritis.append(AkritiYoga("Danda", "rod",
                                  tm(10, 11, 12, 1), (10, 11, 12, 1)))

        # --- seven consecutive house yogas (use tm_dist for distribution) ---
        akritis.append(AkritiYoga("Nauka", "boat",
                                  tm_dist(1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7)))
        akritis.append(AkritiYoga("Kuta", "peak",
                                  tm_dist(4, 5, 6, 7, 8, 9, 10), (4, 5, 6, 7, 8, 9, 10)))
        akritis.append(AkritiYoga("Chatra", "parasol",
                                  tm_dist(7, 8, 9, 10, 11, 12, 1), (7, 8, 9, 10, 11, 12, 1)))
        akritis.append(AkritiYoga("Chapa", "bow",
                                  tm_dist(10, 11, 12, 1, 2, 3, 4), (10, 11, 12, 1, 2, 3, 4)))

        # --- ardha chandra: seven consecutive from a panaphara or apoklima ---
        akritis.append(AkritiYoga("Ardha Chandra Artha Panaphara", "half moon",
                                  tm_dist(2, 3, 4, 5, 6, 7, 8), (2, 3, 4, 5, 6, 7, 8)))
        akritis.append(AkritiYoga("Ardha Chandra Dharma Panaphara", "half moon",
                                  tm_dist(5, 6, 7, 8, 9, 10, 11), (5, 6, 7, 8, 9, 10, 11)))
        akritis.append(AkritiYoga("Ardha Chandra Moksha Panaphara", "half moon",
                                  tm_dist(8, 9, 10, 11, 12, 1, 2), (8, 9, 10, 11, 12, 1, 2)))
        akritis.append(AkritiYoga("Ardha Chandra Kama Panaphara", "half moon",
                                  tm_dist(11, 12, 1, 2, 3, 4, 5), (11, 12, 1, 2, 3, 4, 5)))
        akritis.append(AkritiYoga("Ardha Chandra Kama Apoklima", "half moon",
                                  tm_dist(3, 4, 5, 6, 7, 8, 9), (3, 4, 5, 6, 7, 8, 9)))
        akritis.append(AkritiYoga("Ardha Chandra Artha Apoklima", "half moon",
                                  tm_dist(6, 7, 8, 9, 10, 11, 12), (6, 7, 8, 9, 10, 11, 12)))
        akritis.append(AkritiYoga("Ardha Chandra Dharma Apoklima", "half moon",
                                  tm_dist(9, 10, 11, 12, 1, 2, 3), (9, 10, 11, 12, 1, 2, 3)))
        akritis.append(AkritiYoga("Ardha Chandra Moksha Apoklima", "half moon",
                                  tm_dist(12, 1, 2, 3, 4, 5, 6), (12, 1, 2, 3, 4, 5, 6)))

        # --- six alternate house yogas (use tm_dist for distribution) ---
        akritis.append(AkritiYoga("Chakra", "wheel",
                                  tm_dist(1, 3, 5, 7, 9, 11), (1, 3, 5, 7, 9, 11)))
        akritis.append(AkritiYoga("Samudra", "sea",
                                  tm_dist(2, 4, 6, 8, 10, 12), (2, 4, 6, 8, 10, 12)))

        akritis.sort(key=lambda y: y.to_move)
        return akritis


    def ashraya_yogas(self):
        """
        Ashraya ("resting place") yogas: 3 yogas based on the modality
        of the signs the 7 karakas rest in.
        Rajju = all in movable, Musala = all in fixed, Nala = all in dual.
        """
        lagna_sign = self.signs().lagna()
        movable = 0
        fixed = 0
        dual = 0
        for i in range(1, 13):
            sign = self.signs()[lagna_sign.astrological_signs_forward(i)]
            n = sign.how_many_karakas()
            mod = sign.modality()
            if mod == "Moveable":
                movable += n
            elif mod == "Fixed":
                fixed += n
            else:
                dual += n

        yogas = [
            NabhasaYoga("Rajju", "rope", "Ashraya", 7 - movable,
                        "all planets in movable signs"),
            NabhasaYoga("Musala", "pestle", "Ashraya", 7 - fixed,
                        "all planets in fixed signs"),
            NabhasaYoga("Nala", "reed", "Ashraya", 7 - dual,
                        "all planets in dual signs"),
        ]
        yogas.sort(key=lambda y: y.to_move)
        return yogas


    def dala_yogas(self):
        """
        Dala ("petal") yogas: 2 yogas based on benefic/malefic occupation
        of the kendras (houses 1, 4, 7, 10).
        Mala = all benefics in kendras, Sarpa = all malefics in kendras.
        Uses each planet's actual nature (Moon varies by phase).
        """
        lagna_sign = self.signs().lagna()
        kendras = {1, 4, 7, 10}
        benefics_in_kendras = 0
        malefics_in_kendras = 0
        total_benefics = 0
        total_malefics = 0

        for i in range(1, 13):
            sign = self.signs()[lagna_sign.astrological_signs_forward(i)]
            for planet in sign.karakas():
                if planet.nature() == "Benefic":
                    total_benefics += 1
                    if i in kendras:
                        benefics_in_kendras += 1
                else:
                    total_malefics += 1
                    if i in kendras:
                        malefics_in_kendras += 1

        yogas = [
            NabhasaYoga("Mala", "garland", "Dala",
                        total_benefics - benefics_in_kendras,
                        "all benefics in kendras"),
            NabhasaYoga("Sarpa", "serpent", "Dala",
                        total_malefics - malefics_in_kendras,
                        "all malefics in kendras"),
        ]
        yogas.sort(key=lambda y: y.to_move)
        return yogas


    def sankhya_yogas(self):
        """
        Sankhya ("number") yogas: 7 yogas based on how many houses
        the 7 karakas occupy. Exactly one is always active (to_move=0).
        """
        lagna_sign = self.signs().lagna()
        occupied = 0
        for i in range(1, 13):
            if self.signs()[lagna_sign.astrological_signs_forward(i)].how_many_karakas() > 0:
                occupied += 1

        sankhya_defs = [
            ("Veena", "lute", 7),
            ("Dama", "garland", 6),
            ("Pasa", "noose", 5),
            ("Kedara", "field", 4),
            ("Sula", "spike", 3),
            ("Yuga", "yoke", 2),
            ("Gola", "globe", 1),
        ]
        yogas = []
        for name, trans, required in sankhya_defs:
            yogas.append(NabhasaYoga(name, trans, "Sankhya",
                                     abs(occupied - required),
                                     f"planets in {required} houses"))
        yogas.sort(key=lambda y: y.to_move)
        return yogas


    def nabhasa_yogas(self):
        """
        All 32 Nabhasa yogas: Ashraya (3) + Dala (2) + Sankhya (7) + Akriti (20).
        Returns a list of mixed NabhasaYoga and AkritiYoga dataclasses,
        sorted by to_move ascending.
        """
        all_yogas = self.ashraya_yogas() + self.dala_yogas() + self.sankhya_yogas() + self.akriti_yogas()
        all_yogas.sort(key=lambda y: y.to_move)
        return all_yogas


    def panchamahapurusha_yogas(self):
        """
        Panchamahapurusha yogas: Mars, Mercury, Jupiter, Venus, or Saturn
        in an angle (house 1, 4, 7, 10) AND in own, moolatrikona, or exaltation sign.
        Returns a list of 5 MahapurushaYoga dataclasses.
        """
        defs = [
            ("Ruchaka", "radiant", "Mars"),
            ("Bhadra", "blessed", "Mercury"),
            ("Hamsa", "swan", "Jupiter"),
            ("Malavya", "of Malava", "Venus"),
            ("Sasa", "rabbit", "Saturn"),
        ]
        yogas = []
        for name, trans, planet_name in defs:
            sign = self.signs().where_is(planet_name)
            house = sign.rashis_from_lagna()
            dig = self.planets()[planet_name].dignity()
            in_angle = house in (1, 4, 7, 10)
            in_own_or_ex = dig in ("OH", "EX", "MT")
            present = in_angle and in_own_or_ex
            yogas.append(MahapurushaYoga(name, trans, planet_name,
                                         present, house, dig))
        return yogas


    def solar_yogas(self):
        """
        Solar yogas based on starry planets (Mars, Mercury, Jupiter, Venus, Saturn)
        — NOT Moon, Rahu, or Ketu — in the 2nd and/or 12th from the Sun.
        Vosi: planet(s) in the 12th from Sun (rises before Sun)
        Vesi: planet(s) in the 2nd from Sun (sets after Sun)
        Ubhayachari: planets in both 2nd and 12th from Sun
        """
        sun_sign = self.signs().where_is("Sun")
        sun_house = sun_sign.rashis_from_lagna()
        lagna_sign = self.signs().lagna()
        # house numbers of 2nd and 12th from Sun
        h12_from_sun = ((sun_house - 2) % 12) + 1  # 12th from Sun
        h2_from_sun = (sun_house % 12) + 1          # 2nd from Sun

        STARRY = {"Mars", "Mercury", "Jupiter", "Venus", "Saturn"}
        sign_12 = self.signs()[lagna_sign.astrological_signs_forward(h12_from_sun)]
        sign_2 = self.signs()[lagna_sign.astrological_signs_forward(h2_from_sun)]

        vosi_planets = [p.identity() for p in sign_12.karakas()
                        if p.identity() in STARRY]
        vesi_planets = [p.identity() for p in sign_2.karakas()
                        if p.identity() in STARRY]

        yogas = [
            SolarYoga("Vosi", vosi_planets, len(vosi_planets) > 0),
            SolarYoga("Vesi", vesi_planets, len(vesi_planets) > 0),
            SolarYoga("Ubhayachari", vosi_planets + vesi_planets,
                      len(vosi_planets) > 0 and len(vesi_planets) > 0),
        ]
        return yogas


    def lunar_yogas(self):
        """
        Lunar yogas based on planets (not Sun, Rahu, Ketu) in the
        2nd and/or 12th from the Moon.
        Anapha: planet(s) in the 12th from Moon
        Sunapha: planet(s) in the 2nd from Moon
        Durudhara: planets in both 2nd and 12th from Moon
        Kemadruma: none of the above
        """
        moon_sign = self.signs().where_is("Moon")
        moon_house = moon_sign.rashis_from_lagna()
        lagna_sign = self.signs().lagna()
        h12_from_moon = ((moon_house - 2) % 12) + 1
        h2_from_moon = (moon_house % 12) + 1

        ELIGIBLE = {"Mars", "Mercury", "Jupiter", "Venus", "Saturn"}
        sign_12 = self.signs()[lagna_sign.astrological_signs_forward(h12_from_moon)]
        sign_2 = self.signs()[lagna_sign.astrological_signs_forward(h2_from_moon)]

        anapha_planets = [p.identity() for p in sign_12.karakas()
                          if p.identity() in ELIGIBLE]
        sunapha_planets = [p.identity() for p in sign_2.karakas()
                           if p.identity() in ELIGIBLE]

        has_anapha = len(anapha_planets) > 0
        has_sunapha = len(sunapha_planets) > 0

        yogas = [
            LunarYoga("Anapha", anapha_planets, has_anapha),
            LunarYoga("Sunapha", sunapha_planets, has_sunapha),
            LunarYoga("Durudhara", anapha_planets + sunapha_planets,
                      has_anapha and has_sunapha),
            LunarYoga("Kemadruma", [], not has_anapha and not has_sunapha),
        ]
        return yogas

    def jaimini_kemadruma(self):
        """
        Jaimini Kemadruma Yoga (1.2.119-120)

        from the svamsha (AK in D9), lagna, or pada:
        if there are an equal number of malefics in the 2nd and 8th,
        with no benefics in either house, that is kemadruma yoga

        count backward if the reference sign is even (jaimini direction rule)
        malefics are planets where .nature() == "Malefic"

        also checks from AK in rashi (D1)

        moon aspecting the malefics makes it more severe (1.2.120)

        returns a list of dicts, one per reference point where kemadruma is present
        each dict has: reference, second_malefics, eighth_malefics, moon_aspects, sign
        """
        ak = self.planets().jaimini_karakas()[0]
        d9 = self.master.varga(9)

        # reference points: (name, sign, varga to use)
        refs = [
            ("lagna", self.lagna(), self),
            ("AK in D1", self.signs().where_is(ak.identity()), self),
            ("pada", self.pada(), self),
            ("svamsha", d9.where_is(ak.identity()), d9),
        ]

        moon_sign = self.signs()[self.planets().moon().sign()]

        results = []
        for name, ref_sign, varga in refs:
            direction = 1 if ref_sign.sign() % 2 == 1 else -1
            second = varga.signs()[ref_sign.astrological_signs_forward(2 * direction)]
            eighth = varga.signs()[ref_sign.astrological_signs_forward(8 * direction)]

            second_malefics = [p for p in second.grahas() if p.nature() == "Malefic"]
            eighth_malefics = [p for p in eighth.grahas() if p.nature() == "Malefic"]
            second_benefics = [p for p in second.grahas() if p.nature() == "Benefic"]
            eighth_benefics = [p for p in eighth.grahas() if p.nature() == "Benefic"]

            if (len(second_malefics) == 0 or len(eighth_malefics) == 0):
                continue
            if len(second_malefics) != len(eighth_malefics):
                continue
            if second_benefics or eighth_benefics:
                continue

            # check if moon aspects either house (1.2.120 — more severe)
            moon_aspects_second = self.signs().rashi_aspect_from_to(moon_sign, second)
            moon_aspects_eighth = self.signs().rashi_aspect_from_to(moon_sign, eighth)

            results.append({
                "reference": name,
                "sign": ref_sign,
                "second": second,
                "second_malefics": second_malefics,
                "eighth": eighth,
                "eighth_malefics": eighth_malefics,
                "moon_aspects": moon_aspects_second or moon_aspects_eighth,
            })

        return results

