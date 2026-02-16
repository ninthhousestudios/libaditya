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
from datetime import date
from dataclasses import replace
from typing import Self

from libaditya import constants as const
from libaditya import utils
from libaditya import print_functions as printf

from libaditya.objects import Sun, Moon, EphContext, JulianDay

class Panchanga:
    """
    an independent object that is a function of EphContext
    does everything related to panchanga

    repr(Panchanga()) gives the concise information on the specific Panchanga

    print(Panchanga()) gives all the information that is given in a row that might be printed in libaditya/monthly_panchanga.py
    it actually prints to stdout rather than return a string...i should maybe change that to produce a string...
    """

    def __init__(self, context=EphContext()):
        self.context = context
        self.location = self.context.location
        self.timeJD = self.context.timeJD
        self._sun = Sun(self.context)
        self._moon = Moon(self.context)
        self._tithi_number, self._tithi_elapsed, self._tithi_remaining = self.init_tithi()
        self._karana_number, self._karana_elapsed, self._karana_remaining = self.init_karana()
        self._karana_index = self.karana_index()
        self._yoga_raw, self._yoga_elapsed, self._yoga_remaining = self.init_yoga()

    def __str__(self):
        """
        print everything that is known about this Panchanga()
        this prints directly...should change to return a string
        """
        panch = "\nPanchanga\n\n"
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

        print(panch)

        self.print_addendum()

        return ""

    def __repr__(self):
        """
        for the purposes of identification in a repl, or for just the basic panchanga information
        """
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

    def info_string(self):
        panch = ""
        panch += f"\nAbsolute tithi: {self.tithi()}\n"
        if self.tithi() > 15:
            panch += f"Relative tithi: {self.tithi() - 15}\n"
        panch += f"Type: {self.tithi_type()}\n"

        panch += f"Karana: {self.karana()}\n"
        panch += f"Vara: {self.vara()}\n"
        panch += f"Nakshatra: {self.nakshatra()}\n"
        panch += f"Yoga: {self.yoga()}\n"

        return panch

    def sun(self):
        return self._sun
    
    def moon(self):
        return self._moon

    def sunrise(self):
        """
        return a JulianDay
        """
        return self._sun.riseset(swe.CALC_RISE, self.location)

    def sunset(self):
        return self._sun.riseset(swe.CALC_SET, self.location)

    def moonrise(self):
        return self._moon.riseset(swe.CALC_RISE, self.location)

    def moonset(self):
        return self._moon.riseset(swe.CALC_SET, self.location)

    def init_tithi(self):
        traw = ((self._moon.ecliptic_longitude() - self._sun.ecliptic_longitude()) % 360) / 12
        remainder = traw % 1  # remainder shows how much has elapsed
        elapsed = remainder * 12  # degrees elapsed
        remaining = 12 - elapsed  # degrees remaining
        return (int(traw)+1, elapsed, remaining)

    def tithi(self) -> int:
        """
        returns number of the tithi
        """
        return self._tithi_number

    def tithi_type(self):
        return const.names[self.context.names_type]["tithis"][(self.tithi()-1)%5]

    def tithi_degrees_elapsed(self):
        return round(self._tithi_elapsed,3)

    def tithi_degrees_remaining(self):
        return round(self._tithi_remaining,3)

    def init_karana(self):
        kraw = ((self._moon.ecliptic_longitude() - self._sun.ecliptic_longitude()) % 360) / 6
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
        return const.names[self.context.names_type]["karanas"][self.karana_index()[0]][self.karana_index()[1]]

    def karana_number(self):
        return self._karana_number

    def karana_degrees_elapsed(self):
        return round(self._karana_elapsed,3)

    def karana_degrees_remaining(self):
        return round(self._karana_remaining,3)

    def vara(self):
        weekday = date(
            self.timeJD.datetime[0],
            self.timeJD.datetime[1],
            self.timeJD.datetime[2],
        ).isoweekday()  # 1 is Monday
        # there is this nice function in swe actually...
        # but for it Monday = 0 and Sunday = 6
        #weekday = swe.day_of_week(self.context.timeJD.jd_number())
        sunriseyk = self._sun.sunrise_yamakoti()
        if sunriseyk < self.context.timeJD:
            return const.names[self.context.names_type]["varas"][(weekday + 1) % 7]
        else:
            return const.names[self.context.names_type]["varas"][weekday % 7]

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
        elapsed = remainder * (13+(1/3))  # degrees elapsed
        remaining = (13+(1/3)) - elapsed  # degrees remaining
        return (yraw, elapsed, remaining)

    def yoga_index(self):
        return int(self._yoga_raw)

    def yoga_number(self):
        return self.yoga_index()+1

    def yoga_name(self):
        return const.names[self.context.names_type]["yogas"][self.yoga_index()]

    def yoga(self):
        return f"{self.yoga_number()} {self.yoga_name()}"

    def yoga_degrees_elapsed(self):
        return round(self._yoga_elapsed,3)

    def yoga_degrees_remaining(self):
        return round(self._yoga_remaining,3)

    def next_tithi(self) -> Self:
        if self.tithi_degrees_remaining() == 0:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","seconds",5)))
        shift_factor = self.tithi_degrees_remaining()*self._moon.lowest_hourly_speed()
        return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","hours",shift_factor))).next_tithi()

    def next_karana(self) -> Self:
        if self.karana_degrees_remaining() == 0:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","seconds",5)))
        shift_factor = self.karana_degrees_remaining()*self._moon.lowest_hourly_speed()
        return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","hours",shift_factor))).next_karana()
        
    # doesnt work
    def next_vara(self) -> Self:
        # find sunrise at yamakoti on this day
        today_yamakotiJD = self._sun.sunrise_yamakoti()
        # if the current time is before sunrise at yamakoti, todayJD is the next varas
        if self.timeJD.jd_number() < today_yamakotiJD.jd_number():
            return Panchanga(replace(self.context,timeJD=today_yamakotiJD.shift("f","minutes",5)))
        # if the current time is after sunrise at yamaktoi, go ahead one today
        next_yamakotiJD = Sun(replace(self.context,timeJD=self.timeJD.shift("f","day",1))).sunrise_yamakoti()
        return Panchanga(replace(self.context,timeJD=next_yamakotiJD.timeJD.shift("f","minutes",5))).next_vara()

    def next_nakshatra(self):
        if self._moon.nakshatra().degrees_remaining() <= .00001:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","minute",1)))
        shift_factor = self._moon.nakshatra().degrees_remaining()*self._moon.lowest_hourly_speed()
        return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","hours",shift_factor))).next_nakshatra()

    def next_yoga(self):
        if self.yoga_degrees_remaining() == 0:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","seconds",5)))
        shift_factor = self.yoga_degrees_remaining()*self._moon.lowest_hourly_speed()
        return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","hours",shift_factor))).next_yoga()

    def shift(self,dir,tunit,shift_factor):
        return Panchanga(replace(self.context,timeJD=self.timeJD.shift(dir,tunit,shift_factor)))

    def print_next_new_moon(self):
        """
        an actual print() function

        also prints previous last visibility and next first visibility of the moon around the "next_new_moon"
        """
        next = self.next_new_moon()  # return the Panchanga of the next new moon
        print(f"\n\tLast visibility:")
        next.shift("back","days",10).moon().next_morning_last()[1].indent_print(1)
        print("\nNext new moon at:")
        print(next.timeJD)
        print(f"At: {next._moon.longitude()}")
        print(f"Nakshatra: {next._moon.nakshatra_name()}")
        next.moon().nakshatra().print_in_longitude()
        print(f"\n\tNext visibility:")
        # print the middle JulianDay of the return list, the "optimum" visibility as when you can first see it next
        # JulianDay.indent_print() uses print() itself
        next.moon().next_evening_first()[1].indent_print(1)
        # use this but put it somewhere else as an option
#        print(f"Next last morning visibility:")
#        # Moon/Mercury/Venus.next_morning_last() returns a list of 3 JulianDay classes
#        # earliest, best, latest visibility for that event
#        printf.print_visible_times(next.moon().next_morning_last())
#        print(f"Next evening first visibility:")
#        printf.print_visible_times(next.moon().next_evening_first())


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
        if (self._sun.ecliptic_longitude() - self._moon.ecliptic_longitude()) <= 0.001:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","second",10)))
        remaining = self.tithi_degrees_remaining()
        shift_factor = remaining*self._moon.lowest_hourly_speed()
        return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","hours",shift_factor))).next_new_moon()

    def next_full_moon(self) -> Self:
        """
        return the Panchanga of the full moon that comes after
        self.timeJD
        """
        if (self.tithi() != 15):  
            # if the tithi isnt 15, it cant be a full moon, so go forward 8 hours
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","hour", 8))).next_full_moon()
        target = (self._sun.ecliptic_longitude() + 180) % 360
        diff = abs(self._moon.ecliptic_longitude() - target)
        if diff <= 0.0001:
            return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","second",10)))
        shift_factor = diff*self._moon.lowest_hourly_speed()
        return Panchanga(replace(self.context,timeJD=self.timeJD.shift("f","hours",shift_factor))).next_full_moon()


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

        next_tithi = self.next_tithi()

        hours_left = abs(self.timeJD.jd_number() - next_tithi.timeJD.jd_number())*24

        print(f"Ending time of current tithi: {round(hours_left, 2)} hours from panchanga time")
        print(f"Next tithi is {next_tithi.tithi()} ({next_tithi.tithi_type()}), starting at:")
        print(f"{next_tithi.timeJD}")
        
        # karana
        kelapsed = round(self.karana_degrees_elapsed(), 3)
        kremaining = round(self.karana_degrees_remaining(), 3)

        print(f"\nKarana: {self.karana()}")
        print("Elapsed: ", kelapsed, " degrees (", round((kelapsed / 6) * 100, 2), "%)")
        print(
            "Remaining: ", kremaining, " degree (", round((kremaining / 6) * 100, 2), "%)"
        )

        next_karana = self.next_karana()

        hours_left = abs(self.timeJD.jd_number() - next_karana.timeJD.jd_number())*24

        print(f"Ending time of current karana: {round(hours_left, 2)} hours from panchanga time")
        print(f"Next karana is {next_karana.karana()}, starting at:")
        print(f"{next_karana.timeJD}\n")

        # vara

        # this doesnt work perfectly - fix it sometime

        next_vara = self.next_vara()

        hours_left = abs(self.timeJD.jd_number() - next_vara.timeJD.jd_number())*24
        print(f"Ending time of current vara: {round(hours_left, 2)} hours from panchanga time")
        print(f"Next vara is {next_vara.vara()}, starting at:")
        print(f"{next_vara.timeJD}")

        # nakshatra
        print(f"\nNakshatra: {self._moon.nakshatra_name()}")
        self._moon.nakshatra().print_in_longitude()
        next_nakshatra = self.next_nakshatra()
        hours_left = (next_nakshatra.timeJD.jd_number() - self.timeJD.jd_number()) * 24
        print(f"Ending time of current nakshatra: {round(hours_left, 2)} hours from panchanga time")
        print(f"Next nakshatra is {next_nakshatra.nakshatra()}, starting at:")
        print(f"{next_nakshatra.timeJD}\n")

        # yoga
        yelapsed = round(self.yoga_degrees_elapsed(), 2)
        yremaining = round(self.yoga_degrees_remaining(), 2)

        print(f"\nYoga: {self.yoga()}")
        print("Elapsed: ", yelapsed, " degrees (", round((yelapsed / (13+(1/3))) * 100, 2), "%)")
        print(
            "Remaining: ", yremaining, " degree (", round((yremaining / (13+(1/3))) * 100, 2), "%)"
        )

        next_yoga = self.next_yoga()

        hours_left = abs(self.timeJD.jd_number() - next_yoga.timeJD.jd_number())*24

        print(f"Ending time of current yoga: {round(hours_left, 2)} hours from panchanga time")
        print(f"Next yoga is {next_yoga.yoga()}, starting at:")
        print(f"{next_yoga.timeJD}\n")


