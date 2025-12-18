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
from datetime import date

from libaditya import constants as const

from libaditya.objects import Sun, Moon, EphContext

class Panchanga:

    def __init__(self, context=EphContext()):
        self.context = context
        self._sun = Sun(self.context)
        self._moon = Moon(self.context)
        self._tithi_index, self._tithi_elapsed, self._tithi_remaining = self.init_tithi()
        self._karana_number, self._karana_elapsed, self._karana_remaining = self.init_karana()
        self._karana_index = self.karana_index()
        self._yoga_raw, self_yoga_elapsed, self._yoga_remaining = self.init_yoga()

    def __str__(self):
        panch = "\nPanchanga\n"
        panch += f"\n{self.context.timeJD}\n"

        panch += f"\nAbsolute tithi: {self.tithi()}\n"
        if self.tithi() > 15:
            panch += f"Relative tithi: {self.tithi() - 15}\n"
        panch += f"Type: {self.tithi_type()}\n"

        panch += f"Karana: {self.karana()}\n"
        panch += f"Vara: {self.vara()}\n"
        panch += f"Nakshatra: {self.nakshatra()}\n"
        panch += f"Yoga: {self.yoga()}\n"

        return panch

    def init_tithi(self):
        traw = ((self._moon.real_longitude() - self._sun.real_longitude()) % 360) / 12
        remainder = traw % 1  # remainder shows how much has elapsed
        elapsed = remainder * 12  # degrees elapsed
        remaining = 12 - elapsed  # degrees remaining
        return (int(traw)+1, elapsed, remaining)

    def tithi(self):
        return self._tithi_index

    def tithi_type(self):
        return self.context.names.tithis[(self.tithi()-1)%5]

    def tithi_degrees_elapsed(self):
        return self._tithi_elapsed

    def tithi_degrees_remaining(self):
        return self._tithi_remaining

    def init_karana(self):
        kraw = ((self._moon.real_longitude() - self._sun.real_longitude()) % 360) / 6
        remainder = kraw % 1  # remainder shows how much has elapsed
        elapsed = remainder * 6  # degrees elapsed
        remaining = 6 - elapsed  # degrees remaining
        return (kraw, elapsed, remaining)

    def karana_index(self):
        if self._tithi_remaining > 6:
            return (self.tithi()-1,0)
        else:
            return (self.tithi()-1,1)

    def karana(self):
        return self.context.names.karanas[self.karana_index()[0]][self.karana_index()[1]]

    def vara(self):
        weekday = date(
            self.context.timeJD.datetime[0],
            self.context.timeJD.datetime[1],
            self.context.timeJD.datetime[2],
        ).isoweekday()  # 1 is Monday
        sunriseyk = self._sun.sunrise_yamakoti()
        if sunriseyk < self.context.timeJD:
            return self.context.names.varas[(weekday + 1) % 7]
        else:
            return self.context.names.varas[weekday % 7]

    def nakshatra(self):
        return self._moon.nakshatra_name()

    def init_yoga(self):
        """
        sun and moon longitude should be taken from the beginning of the first yoga, which
        is equivalent to the beginning of ashvini, thus we need to add (or subtract) the ayanamsa value
        to the longitudes
        """
#        sunlong=self._sun.real_longitude()
#        moonlong=self._moon.real_longitude()
#        if self.context.ayanamsa < 98:
#            swe.set_sid_mode(self.context.ayanamsa)
#            offset = swe.get_ayanamsa(self.context.timeJD.jd)
#        elif self.context.ayanamsa == 98:
#            # get ayanamsa value for my dhurva gc mid-mula
#            gcequ=swe.fixstar(",SgrA*",self.context.timeJD.jd, swe.FLG_EQUATORIAL)[0][0]
#            mula=gcequ-((13+1/3)/2)
#            # offset is the start of ashvini, which is essentially the ayanamsa value
#            offset=mula-(18*pglob.nak)
#            sunlong=swe.calc_ut(self.context.timeJD.jd,swe.SUN,swe.FLG_EQUATORIAL)[0][0]
#            moonlong=swe.calc_ut(self.context.timeJD.jd,swe.MOON,swe.FLG_EQUATORIAL)[0][0]
#        elif self.context.ayanamsa == 99 or self.context.ayanamsa == 100:
#            # for vedanga jyotisha
#            # ashvini is at 336.66667, so we have to add to the tropical longitude
#            offset = -(23+(1/3))
#        else:
#            offset=0
        yraw = ((self._moon.nakshatra().ashvini_longitude() + self._sun.nakshatra().ashvini_longitude()) % 360) / (13 + (20 / 60))
        remainder = yraw % 1  # remainder shows how much has elapsed
        elapsed = remainder * 12  # degrees elapsed
        remaining = 12 - elapsed  # degrees remaining
        return (yraw, elapsed, remaining)

    def yoga_index(self):
        return int(self._yoga_raw)

    def yoga_number(self):
        return self.yoga_index()+1

    def yoga_name(self):
        return self.context.names.yogas[self.yoga_index()]

    def yoga(self):
        return f"{self.yoga_number()} {self.yoga_name()}"
