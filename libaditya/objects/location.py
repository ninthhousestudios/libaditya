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
        # swe argument order is long, lat, alt
        return (self.long, self.lat, self.alt)


# Yamakoti is an ancient prime meridian
# this spot is used to calculate the vara, a savana day that is the same at once in the whole world
Yamakoti = Location(0, 165.76666666666668, 0, "Yamakoti", "ykt")
