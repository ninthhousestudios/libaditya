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
from dataclasses import replace

from libaditya import constants as const
from libaditya import utils

from libaditya.objects import Sun, Moon, EphContext

class Panchanga:

    def __init__(self, context=EphContext()):
        self.context = context
        self.location = self.context.location
        self.timeJD = self.context.timeJD
        self._sun = Sun(self.context)
        self._moon = Moon(self.context)
        self._tithi_index, self._tithi_elapsed, self._tithi_remaining = self.init_tithi()
        self._karana_number, self._karana_elapsed, self._karana_remaining = self.init_karana()
        self._karana_index = self.karana_index()
        self._yoga_raw, self._yoga_elapsed, self._yoga_remaining = self.init_yoga()

    def __str__(self):
        panch = "\nPanchanga\n"
        panch += f"{const.ayanamsa_name(self.context.ayanamsa)}"
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
        return round(self._tithi_elapsed,3)

    def tithi_degrees_remaining(self):
        return round(self._tithi_remaining,3)

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

    def karana_degrees_elapsed(self):
        return self._karana_elapsed

    def karana_degrees_remaining(self):
        return self._karana_remaining

    def vara(self):
        weekday = date(
            self.timeJD.datetime[0],
            self.timeJD.datetime[1],
            self.timeJD.datetime[2],
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

    def yoga_degrees_elapsed(self):
        return self._yoga_elapsed

    def yoga_degrees_remaining(self):
        return self._yoga_remaining

    def print_next_new_moon(self):
        next = self.next_new_moon()  # return the Panchanga of the next new moon
        print("\nNext new moon at:")
        print(next.timeJD)
        print(f"At: {next._moon.longitude()}")
        print(f"Nakshatra: {next._moon.nakshatra_name()}")
        next._moon.nakshatra().print_in_longitude()

    def print_next_full_moon(self):
        next = self.next_full_moon()  # return the Panchanga of the next new moon
        print("\nNext full moon at:")
        print(next.timeJD)
        print(f"At: {next._moon.longitude()}")
        print(f"Nakshatra: {next._moon.nakshatra_name()}")
        next._moon.nakshatra().print_in_longitude()

    def next_new_moon(self):
        """
        return the Panchanga of the new moon that comes after
        self.timeJD
        """
        if (self.tithi() != 30):  
            # if the tithi isnt 30, it cant be a new moon, so go forward 8 hours
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","hour", 8))).next_new_moon()
        if abs(round(self._sun.real_longitude() - self._moon.real_longitude(), 4)) <= 0.0001:
            return self
        remaining = self.tithi_degrees_remaining()
        # if there are more than x degrees remaining, check a time y forward
        if remaining > 6:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "hour", 8))).next_new_moon()
        elif remaining > 3:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "hour", 4))).next_new_moon()
        elif remaining > 1:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "minutes", 30))).next_new_moon()
        elif remaining > 0.5:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "minutes", 15))).next_new_moon()
        elif remaining > 0.1:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "minutes", 1))).next_new_moon()
        elif remaining > 0.01:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "second", 5))).next_new_moon()
        elif remaining > 0.001:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "second", 1))).next_new_moon()
        elif remaining < 0.001:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "second", 1/4))).next_new_moon()
        else:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "second", 1))).next_new_moon()

    def next_full_moon(self):
        if self.tithi() != 15:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "hour", 8))).next_full_moon()
        target = (self._sun.real_longitude() + 180) % 360
        diff = abs(self._moon.real_longitude() - target)
        if diff > 16:  # at least six more degrees until a full moon
            # moon moves about 1 degree/2 hours, so lets move it 5 degrees forward => 10 hours
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "days", 1))).next_full_moon()
        elif diff > 5 and diff <= 16:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "hours", 4))).next_full_moon()
        elif diff > 1 and diff <= 5:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "hours", 1))).next_full_moon()
        elif diff > .5 and diff <= 1:
            # moon is between 1 and 3 degrees from full, so move forward 1 degree
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "hours", 1/2))).next_full_moon()
        elif diff > 0.25 and diff <= .5:
            # moon is between .1 and  1 degree from full, so move foward about .1 degrees
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "hours", 1/8))).next_full_moon()
        elif diff > 0.1 and diff <= 0.25:
            # moon is between .01 and .1 degree from full, so move forward about .01 degrees
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "minutes", 5))).next_full_moon()
        elif diff > 0.01 and diff <= 0.1:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "minutes", 1/4))).next_full_moon()
        elif diff > 0.001 and diff <= 0.01:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f", "seconds", 1/2))).next_full_moon()
        elif diff <= .0001:
            return self
        else:
            return Panchanga(EphContext(timeJD=self.timeJD.shift("f", "seconds", 1/8),signize=self.context.signize,toround=self.context.toround)).next_full_moon()

    def print_addendum(self):
        print("\nPanchanga addendum")

        dmsun = self._sun.daily_motion()
        dmmoon = self._moon.daily_motion()

        print(
            f"\nSunrise {self.timeJD.date()} at {self.location.place()}:\n{self._sun.riseset(swe.CALC_RISE, self.location)}\n"
        )
        print(
            f"Sunset {self.timeJD.date()} at {self.location.place()}:\n{self._sun.riseset(swe.CALC_SET, self.location)}\n"
        )

        # give moonrise for three days, the one before, this one, and the one after
        # yesterpanch = Panchanga(panch.shift("b", "day", 1))
        # morrowpanch = Panchanga(panch.shift("f", "day", 1))
        print(
            f"Moonrise {self.timeJD.date()} at {self.location.place()}: \n{self._moon.riseset(swe.CALC_RISE, self.location)}"
        )
        print(
            f"\nMoonset {self.timeJD.date()} at {self.location.place()}: \n{self._moon.riseset(swe.CALC_SET, self.location)}"
        )

        print(f"\nTithi: {self.tithi()}")
        print("Elapsed: ", self.tithi_degrees_elapsed(), " degrees (", round((self.tithi_degrees_elapsed() / 12) * 100, 3), "%)")
        print(
            "Remaining: ", self.tithi_degrees_remaining(), " degree (", round((self.tithi_degrees_remaining() / 12) * 100, 3), "%)"
        )

        hours_left = ((self.tithi_degrees_remaining()) / (dmmoon - dmsun)) * 24
        end_time = self.timeJD.shift("f", "hour", hours_left)

        print(
            f"Ending time of current tithi: {round(hours_left, 2)} hours from panchanga time, at\n{end_time.timedate()}\n{end_time.usrtimedate()}"
        )
        
        # karana
        kelapsed = round(self.karana_degrees_elapsed(), 3)
        kremaining = round(self.karana_degrees_remaining(), 3)

        print(f"\nKarana: {self.karana()}")
        print("Elapsed: ", kelapsed, " degrees (", round((kelapsed / 6) * 100, 2), "%)")
        print(
            "Remaining: ", kremaining, " degree (", round((kremaining / 6) * 100, 2), "%)"
        )

        hours_left = ((kremaining) / (dmmoon - dmsun)) * 24
        end_time = self.timeJD.shift("f", "hour", hours_left)

        print(
            f"Ending time of current karana: {round(hours_left, 2)} hours from panchanga time, at\n{end_time.timedate()}\n{end_time.usrtimedate()}"
        )

        # vara

        hrsnxtvara = ((self._sun.sunrise_yamakoti().jd - self.timeJD.jd) / self.timeJD.onehrjd) % 24
        nxtvara = self.timeJD.shift("f", "hour", hrsnxtvara)
        print(
            f"\nNext vara begins: {utils.time2str(utils.dec2dms(hrsnxtvara))} hours from panchanga time\nat {nxtvara.timedate()}\n   {nxtvara.usrtimedate()}"
        )

        # nakshatra
        print(f"\nNakshatra: {self._moon.nakshatra_name()}")
        self._moon.nakshatra().print_in_longitude()
        hours_left = (self._moon.nakshatra().degrees_remaining() / dmmoon) * 24
        end_time = self.timeJD.shift("f", "hour", hours_left)
        print(
            f"Ending time of current nakshatra: {round(hours_left, 2)} hours from panchanga time, at\n{end_time.timedate()}\n{end_time.usrtimedate()}"
        )

        # yoga
        yelapsed = round(self.yoga_degrees_elapsed(), 2)
        yremaining = round(self.yoga_degrees_remaining(), 2)

        print(f"\nYoga: {self.yoga()}")
        print("Elapsed: ", yelapsed, " degrees (", round((yelapsed / 12) * 100, 2), "%)")
        print(
            "Remaining: ", yremaining, " degree (", round((yremaining / 12) * 100, 2), "%)"
        )

        hours_left = ((yremaining) / (dmmoon - dmsun)) * 24
        end_time = self.timeJD.shift("f", "hour", hours_left)

        print(
            f"Ending time of current yoga: {round(hours_left, 2)} hours from panchanga time, at\n{end_time.timedate()}\n{end_time.usrtimedate()}"
        )

