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
from metar import Metar

from libaditya import constants as const


class Location:
    def __init__(
        self,
        lat=0,
        long=165.76666666666668,
        alt=0,
        placename="Yamakoti",
        timezone="YKT",
        icao=None
    ):
        self.lat = float(lat)
        self.long = float(long)
        self.alt = float(alt)
        self.placename = placename
        self.timezone = timezone
        self.icao = icao

    def __str__(self):
        return f"{self.placename} ({round(self.lat,3)} lat,{round(self.long,3)} long)\nelevation {self.alt} m\ntimezone: {self.timezone}"

    def place(self):
        return f"{self.placename} ({round(self.lat, 3)},{round(self.long, 3)})"

    def latitude(self):
        return self.lat

    def longitude(self):
        return self.long

    def __repr__(self):
        return f"({self.lat},{self.long})"

    def swe_location(self):
        """
        if you need a location for a swe library function, use this
        this returns a tuple, which is what "geopos" usually is in the python functions
        """
        # swe argument order is long, lat, alt
        return (self.long, self.lat, self.alt)

    def get_metar(self, icao=None):
        """
        get metar for icao
        this will be used for swe.heliacal_ut() and any other place-based things like that
        for atmospheric pressure, tempature, and the dewpoint can hopefully be used to calculate relative humidity

        need to figure out if i can get past data; this is only current data

        url is taken from get_report.py from python-metar package
        """
        BASE_URL = "https://tgftp.nws.noaa.gov/data/observations/metar/stations"
        name = icao
        url = "%s/%s.TXT" % (BASE_URL, name)
        from urllib.request import urlopen
        urlh = urlopen(url)
        report = ""
        for line in urlh:
            if not isinstance(line, str):
                line = line.decode()  # convert Python3 bytes buffer to string
            if line.startswith(name):
                report = line.strip()
                obs = Metar.Metar(line)
                return obs
                break
        if not report:
            print("No data for ", name, "\n\n")


# Yamakoti is an ancient prime meridian
# this spot is used to calculate the vara, a savana day that is the same at once in the whole world
# PKMJ is Marshall Islands International Airport
# an airport close to Yamakoti, for purposes of weather information
Yamakoti = Location(0, 165.76666666666668, 0, "Yamakoti", "ykt", "PKMJ")
