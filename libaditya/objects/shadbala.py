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

"""
shadbala is not an object, but these are all Mixin classes that go into classes in libaditya.objects
when i put these in calc/ there were import errors
"""

from .julian_day import JulianDay
from .location import Location, Yamakoti
from .context import EphContext
from .longitude import Longitude
from .cusps import Cusp, Cusps
from .nakshatras import Nakshatra, Nakshatras

class PlanetBala:
    """
    a Mixin for libaditya.objects.Planet which has shadbala methods
    has most of them expect for class specific ones, e.g., Sun.cheshta_bala()
    """

    def _dig_bala(self, cusp: Cusp) -> float:
        """
        cusp is the Cusp of whereat Planet has digbala

        uses Longitude.virupas_between(point), where point is where the Planet has 60 virupas
        so this is generalized, can be used for digbala with a cusp
        """
        return self.virupas_between(cusp.amsha_longitude())
    
    def ucca_bala(self):
        """
        this method will work in each Varga, given the "amsha_longitude()", the longitude in whatever amsha this is in

        get ucca bala for Planet; note, Moon and Mercury have their own special method because they have ex/db ranges, not points
        if a planets longitude is at their Planet.ucca, ucca_bala is 60 points
        if it is at thier Planet.nica, it is 0 points
        it is a proportion of 60 in accord with its proportion between the two points
        """
        if isinstance(self, Moon) or isinstance(self, Mercury):
            return self._ucca_bala_mm()
        # ucca/nica are stored as sign.degrees, but we need the actual longitude to calculate ucca bala
        ucca = utils.sign_degree_to_longitude(self.ucca(),self.context)
        #nica = utils.sign_degree_to_longitude(self.nica(),self.context)

        return self.virupas_between(ucca)

    def _ucca_bala_mm(self):
        """
        get ucca bala for Moon or Mercury, not including Moon or Mercury
        if a planets longitude is at their Planet.ucca, ucca_bala is 60 points
        if it is at thier Planet.nica, it is 0 points
        it is a proportion of 60 in accord with its proportion between the two points

        you could use this in others vargas. the exaltation points would remaind the same
        you could change it to move th exaltation point through the vargas as if it were another point
        maybe will add that
        """
        # ucca/nica are stored as sign.degrees, but we need the actual longitude to calculate ucca bala
        lower_ucca = utils.sign_degree_to_longitude(self.ucca()[0],self.context)
        upper_ucca = utils.sign_degree_to_longitude(self.ucca()[1],self.context)
        lower_nica = utils.sign_degree_to_longitude(self.nica()[0],self.context)
        upper_nica = utils.sign_degree_to_longitude(self.nica()[1],self.context)

        if self.amsha_longitude() >= lower_ucca and self.amsha_longitude() < upper_ucca:
            return 60
        if self.amsha_longitude() >= lower_nica and self.amsha_longitude() < upper_nica:
            return 0

        # these are the same, since the ex-db ranges are the same
        # for the moon, each is 177, for mercury, each is 165
        # ucca_length = 180-(upper_ucca - lower_ucca)
        # nica_length = 180-(upper_nica - lower_nica)
        # this is the length that gets 60 proportional points
        calc_length = 180-(upper_ucca-lower_ucca)

        if self.amsha_between(upper_ucca,lower_nica):
            # 0-3 is the range of exaltation, so 60 points is divided into 177 degrees
            from_lower_nica = self.amsha_degrees_apart(lower_nica) 
            return (from_lower_nica/calc_length)*60
        if self.amsha_between(upper_nica,lower_ucca):
            from_lower_ucca = self.amsha_degrees_apart(lower_ucca) 
            from_upper_nica = calc_length-from_lower_ucca
            return (from_upper_nica/calc_length)*60

    def mean_longitude(self):
        t = self.context.timeJD.T()
        return const.mean_longitude_formulas[self.identity()](t)

    def cheshta_bala(self):
        t = self.context.timeJD.T()
        sun_mean_longitude = Sun(self.context).mean_longitude()
        mean = const.mean_longitude_formulas[self.identity()](t)
        average = (self.ecliptic_longitude()+mean)/2
        if self.identity() == "Mercury" or self.identity() == "Venus":
            apogee = mean
            mean = sun_mean_longitude
        else:
            apogee = sun_mean_longitude
        reduce = abs(apogee - average)
        if reduce > 180:
            reduce = (360 - reduce)%360
        return reduce/3

class RashiBala:
    """
    a Mixin for libaditya.calc.vargas.Rashi which has shadbala methods that work best at the Rashi level
    """

    def init_dig_balas(self):
        digbs = self.planets()._dig_balas(self.cusps())
        return digbs

    def dig_balas(self):
        return self._dig_balas

    def saptavargaja_balas(self):
        """
        find the saptavargaja bala for each karaka
        set them in their Planet class
        """
        sapta_vargas = self.master.saptavargas()

        points = {
            "MT": 45,
            "OH": 30,
            "GF": 20,
            "F": 15,
            "N": 10,
            "E": 4,
            "GE": 2
        }

        # list of totals in karaka order
        totals = []

#        #import pdb; pdb.set_trace()
        for planet in self.planets().karakas().values():
            this_total = 0
            for varga in sapta_vargas:
                dignity = varga.planets()[planet.identity()].combined_relationship()
                this_total += points[dignity]
            totals.append(this_total)

        return totals
