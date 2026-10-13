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

import math
import swisseph as swe

from libaditya import constants as const
from libaditya import utils

KARAKAS = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
GRAHAS = KARAKAS + ["Rahu", "Ketu"]
WATER_SIGNS = {4, 8, 12}

BALADI_STATES = ["Bala", "Kumara", "Yuva", "Vriddha", "Mrita"]
JAGRADADI_STATES = ["Jagrat", "Swapna", "Sushupti"]
DEEPTADI_STATES = ["Deepta", "Swastha", "Mudita", "Shanta", "Shakta",
                   "Peedita", "Deena", "Vikala", "Khala"]
SHAYANADI_STATES = ["Shayana", "Upavesha", "Netrapani", "Prakasha",
                    "Gamana", "Agamana", "Sabha", "Agama",
                    "Bhojana", "Nrityalipsa", "Kautuka", "Nidra"]
SHAYANADI_MULTIPLIERS = {"Sun": 5, "Moon": 2, "Mars": 2, "Mercury": 3,
                         "Jupiter": 5, "Venus": 3, "Saturn": 3}
COMBUST_ORBS = {"Moon": 12, "Mars": 17, "Mercury": 14, "Jupiter": 11,
                "Venus": 10, "Saturn": 15}
BENEFIC_NAVAMSA_SIGNS = {2, 3, 4, 6, 7, 9, 12}
NATURAL_MALEFICS = {"Sun", "Mars", "Saturn", "Rahu", "Ketu"}


class LajjitaadiAvasthas:

    def lajjitaadi_avasthas(self) -> dict:
        """
        Calculate Lajjitaadi Avasthas for the seven karakas.

        Returns a dict keyed by planet name, each value being a dict of
        avastha names mapped to lists of contributing factors. Each factor
        has a source, strength (0-60), and relevant planet/lord info.

        Ernst Wilhelm's version plus custom Healthy (Svastha) avastha.
        """
        planets = self.planets()
        signs = self.signs()
        cusps = self.cusps()
        lagna = signs.lagna()
        fifth_sign_num = lagna.astrological_signs_forward(5)

        result = {}

        for name in KARAKAS:
            planet = planets[name]
            avasthas = {}
            sign_num = planet.sign()
            sign_lord = const.lords[sign_num]

            # precompute natural relationships and aspects from other planets
            for other_name in GRAHAS:
                if other_name == name:
                    continue
                other = planets[other_name]
                aspect = planet.parashara_aspect_from(other)
                is_conjunction = (aspect == "Y")
                aspect_strength = aspect if isinstance(aspect, (int, float)) else None
                # natural relationship: how does planet feel about other?
                if other_name in KARAKAS:
                    rel = planet.natural_relationship_from(other)
                else:
                    rel = None
                is_friend = rel in ("F", "OH")
                is_enemy = rel == "E"

                # --- Delighted ---
                # conjunct Jupiter
                if is_conjunction and other_name == "Jupiter":
                    _add(avasthas, "delighted", {"source": "conjunction", "planet": other_name, "strength": 60})
                # conjunct natural friend (except Saturn)
                if is_conjunction and is_friend and other_name != "Saturn":
                    _add(avasthas, "delighted", {"source": "conjunction", "planet": other_name, "strength": 60})
                # aspected by natural friend
                if aspect_strength and is_friend:
                    _add(avasthas, "delighted", {"source": "aspect", "planet": other_name, "strength": aspect_strength})

                # --- Starved ---
                # conjunct natural enemy
                if is_conjunction and is_enemy:
                    _add(avasthas, "starved", {"source": "conjunction", "planet": other_name, "strength": 60})
                # conjunct Saturn (for non-Saturn planets)
                if is_conjunction and other_name == "Saturn":
                    _add(avasthas, "starved", {"source": "conjunction", "planet": "Saturn", "strength": 60})
                # aspected by natural enemy
                if aspect_strength and is_enemy:
                    _add(avasthas, "starved", {"source": "aspect", "planet": other_name, "strength": aspect_strength})

                # --- Agitated ---
                # conjunct Sun
                if is_conjunction and other_name == "Sun":
                    _add(avasthas, "agitated", {"source": "conjunction", "planet": "Sun", "strength": 60})
                # aspected by natural enemy who is also a natural malefic
                if aspect_strength and is_enemy and other_name in KARAKAS:
                    if other.nature() == "Malefic":
                        _add(avasthas, "agitated", {"source": "aspect", "planet": other_name, "strength": aspect_strength})

                # --- Thirsty ---
                # in a water sign AND aspected by natural enemy
                if sign_num in WATER_SIGNS and aspect_strength and is_enemy:
                    _add(avasthas, "thirsty", {"source": "aspect", "planet": other_name, "strength": aspect_strength})

            # --- Delighted: in sign of natural friend ---
            if sign_lord != name and sign_lord in KARAKAS:
                lord_planet = planets[sign_lord]
                rel_to_lord = planet.natural_relationship_from(lord_planet)
                if rel_to_lord in ("F", "OH"):
                    _add(avasthas, "delighted", {"source": "sign", "lord": sign_lord, "strength": 60})

            # --- Starved: in sign of natural enemy ---
            if sign_lord != name and sign_lord in KARAKAS:
                lord_planet = planets[sign_lord]
                rel_to_lord = planet.natural_relationship_from(lord_planet)
                if rel_to_lord == "E":
                    _add(avasthas, "starved", {"source": "sign", "lord": sign_lord, "strength": 60})

            # --- Healthy: planet in own sign ---
            if planet.is_oh():
                _add(avasthas, "healthy", {"source": "sign", "strength": 60})

            # --- Proud: planet is EX or MT ---
            if planet.is_ex():
                _add(avasthas, "proud", {"source": "dignity", "dignity": "EX", "strength": 60})
            elif planet.is_mt():
                _add(avasthas, "proud", {"source": "dignity", "dignity": "MT", "strength": 60})

            # --- Thirsty: water sign check (base condition) ---
            # already handled above in the per-other loop; the water sign is a
            # prerequisite for the aspect trigger, not a standalone trigger

            # --- Shamed ---
            # conjunct Sun/Mars/Saturn AND (conjunct Rahu/Ketu OR in 5th sign OR conjunct 5th cusp)
            conj_sun_mars_saturn = []
            conj_rahu_ketu = False
            for other_name in GRAHAS:
                if other_name == name:
                    continue
                other = planets[other_name]
                aspect = planet.parashara_aspect_from(other)
                if aspect == "Y":
                    if other_name in ("Sun", "Mars", "Saturn"):
                        conj_sun_mars_saturn.append(other_name)
                    if other_name in ("Rahu", "Ketu"):
                        conj_rahu_ketu = True

            if conj_sun_mars_saturn:
                in_fifth_sign = (sign_num == fifth_sign_num)
                conj_fifth_cusp = (planet.sign() == cusps[5].sign())
                if conj_rahu_ketu or in_fifth_sign or conj_fifth_cusp:
                    for trigger in conj_sun_mars_saturn:
                        _add(avasthas, "shamed", {"source": "conjunction", "planet": trigger, "strength": 60})
                    if conj_rahu_ketu:
                        _add(avasthas, "shamed", {"source": "condition", "detail": "conjunct Rahu/Ketu"})
                    if in_fifth_sign:
                        _add(avasthas, "shamed", {"source": "condition", "detail": "in 5th sign"})
                    if conj_fifth_cusp and not in_fifth_sign:
                        _add(avasthas, "shamed", {"source": "condition", "detail": "conjunct 5th cusp"})

            planet.attributes["lajjitaadi_avasthas"] = avasthas
            if avasthas:
                result[name] = avasthas
                sign_obj = signs[sign_num]
                sign_obj._lajjitaadi_avasthas[name] = avasthas

        # build giving and receiving dicts for each karaka
        for name in KARAKAS:
            planet = planets[name]
            avasthas = planet.attributes["lajjitaadi_avasthas"]
            # receiving: factors from my avasthas where another planet is the cause
            receiving = {}
            for avastha, factors in avasthas.items():
                planet_factors = [f for f in factors if "planet" in f]
                if planet_factors:
                    receiving[avastha] = planet_factors
            planet.attributes["lajjitaadi_receiving"] = receiving
            # giving: scan all other planets' avasthas for factors where I am the cause
            giving = {}
            for other_name in KARAKAS:
                if other_name == name:
                    continue
                other_avasthas = planets[other_name].attributes["lajjitaadi_avasthas"]
                for avastha, factors in other_avasthas.items():
                    for f in factors:
                        if f.get("planet") == name:
                            _add(giving, avastha, {**f, "to": other_name})
            planet.attributes["lajjitaadi_giving"] = giving

        return result


def _add(avasthas, avastha_name, factor):
    if avastha_name not in avasthas:
        avasthas[avastha_name] = []
    avasthas[avastha_name].append(factor)


class BaladiAvasthas:

    def baladi_avasthas(self) -> dict:
        planets = self.planets()
        result = {}
        for name in KARAKAS:
            planet = planets[name]
            degree = planet.real_in_sign_longitude()
            b = math.floor(degree / 6.0)
            if b > 4:
                b = 4
            if utils.even(planet.sign()):
                b = 4 - b
            state = BALADI_STATES[b]
            planet.attributes["baladi_avastha"] = state
            result[name] = state
        return result


class JagradadiAvasthas:

    def jagradadi_avasthas(self) -> dict:
        planets = self.planets()
        result = {}
        for name in KARAKAS:
            planet = planets[name]
            if planet.is_ex() or planet.is_oh() or planet.is_mt():
                state = "Jagrat"
            elif planet.dignity() in ("F", "GF"):
                state = "Swapna"
            else:
                state = "Sushupti"
            planet.attributes["jagradadi_avastha"] = state
            result[name] = state
        return result


class DeeptadiAvasthas:

    def deeptadi_avasthas(self) -> dict:
        planets = self.planets()
        sun = planets["Sun"]
        result = {}
        for name in KARAKAS:
            planet = planets[name]
            state = self._deeptadi_state(planet, name, planets, sun)
            planet.attributes["deeptadi_avastha"] = state
            result[name] = state
        return result

    def _deeptadi_state(self, planet, name, planets, sun):
        # 1. Deepta - exalted
        if planet.is_ex():
            return "Deepta"
        # 2. Swastha - own sign
        if planet.is_oh():
            return "Swastha"
        # 3. Mudita - friend's sign
        if planet.dignity() in ("F", "GF"):
            return "Mudita"
        # 4. Shanta - benefic navamsa sign
        navamsa_sign = math.floor(planet.ecliptic_longitude() / (30 / 9)) % 12 + 1
        if navamsa_sign in BENEFIC_NAVAMSA_SIGNS:
            return "Shanta"
        # 5. Shakta - retrograde
        if planet.retrograde():
            return "Shakta"
        # 6. Peedita - conjunct a natural malefic
        for other_name in GRAHAS:
            if other_name == name:
                continue
            if other_name not in NATURAL_MALEFICS:
                continue
            other = planets[other_name]
            aspect = planet.parashara_aspect_from(other)
            if aspect == "Y":
                return "Peedita"
        # 7. Deena - debilitated
        if planet.is_db():
            return "Deena"
        # 8. Vikala - combust
        if name != "Sun" and name in COMBUST_ORBS:
            sep = abs(planet.ecliptic_longitude() - sun.ecliptic_longitude())
            if sep > 180:
                sep = 360 - sep
            orb = COMBUST_ORBS[name]
            if name == "Mercury" and planet.retrograde():
                orb = 12
            if sep <= orb:
                return "Vikala"
        # 9. Khala - enemy's sign
        if planet.dignity() in ("E", "GE"):
            return "Khala"
        # fallback (shouldn't normally happen - neutral sign, not retro, not combust, etc.)
        return "Shanta"


class ShayanadiAvasthas:

    def shayanadi_avasthas(self) -> dict:
        planets = self.planets()
        context = self.context
        birth_jd = context.timeJD.jd_number()
        # find the most recent sunrise before birth
        # rise_trans finds the *next* rise, so start from ~1 day before birth
        sunrise_jd = swe.rise_trans(
            birth_jd - 1,
            swe.SUN,
            swe.CALC_RISE | swe.BIT_HINDU_RISING,
            context.location.swe_location(),
        )[1][0]
        # if that sunrise is still after birth (shouldn't happen), go back further
        if sunrise_jd > birth_jd:
            sunrise_jd = swe.rise_trans(
                birth_jd - 2,
                swe.SUN,
                swe.CALC_RISE | swe.BIT_HINDU_RISING,
                context.location.swe_location(),
            )[1][0]
        birth_ghatis = (birth_jd - sunrise_jd) * 60

        result = {}
        for name in KARAKAS:
            planet = planets[name]
            nak_num = planet.nakshatra().index() + 1
            multiplier = SHAYANADI_MULTIPLIERS[name]
            navamsa_num = math.floor(planet.real_in_sign_longitude() / (30 / 9)) + 1
            value = math.floor(nak_num * multiplier + navamsa_num + birth_ghatis) % 12
            state = SHAYANADI_STATES[value]
            planet.attributes["shayanadi_avastha"] = state
            result[name] = state
        return result
