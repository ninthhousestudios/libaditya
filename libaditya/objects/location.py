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

from libaditya import constants as const

class Location:
    def __init__(
        self,
        lat=0,
        long=165.76666666666668,
        alt=0,
        placename="Yamakoti",
        timezone="YKT",
    ):
        self.lat = float(lat)
        self.long = float(long)
        self.alt = float(alt)
        self.placename = placename
        self.timezone = timezone

    def __str__(self):
        return f"{self.placename} ({self.lat} lat,{self.long} long)\nelevation {self.alt} m\ntimezone: {self.timezone}\n"

    def place(self):
        return f"{self.placename} {round(self.lat,3)},{round(self.long,3)})"

    def swe_location(self):
        # swe argument order is long, lat, alt
        return (self.long, self.lat, self.alt)

Yamakoti = Location(0, 165.76666666666668, 0, "Yamakoti", "ykt")
