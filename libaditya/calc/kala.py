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

from libaditya.objects import JulianDay, Sun, EphContext
from libaditya.calc import Panchanga

def lunar_new_year(year) -> Panchanga:
    """
    find chinese lunar new year in calendar year "year"
    chinese lunar new year is the second new moon after the winter solstice
    so the lunar new year in 2026 is after the solstice in 2025
    year can be an integer or a JulianDay class
    """
    if isinstance(year,JulianDay):
        year = year.year()
    # get january 1st of the previous year so we can find the winter solstice of that year
    solstice_yearJD = JulianDay(swe.julday(year-1,1,1))
    solsticeSun = Sun(EphContext(timeJD=solstice_yearJD)).ingress(270)

    # now get a Panchanga for this time
    panch = Panchanga(solsticeSun.context)

    new_year = panch.next_new_moon().next_new_moon()

    return new_year



def cardinal_points(year) -> [JulianDay]:
    """
    return the cardinal points of the year in order
    i.e., ascending equinox, northern solstice, descedending equinox, southern solstice
    """
    year_jd = swe.julday(year,1,1,0)
    s=Sun(EphContext(timeJD=JulianDay(year_jd)))
    return [s.ingress(0), s.ingress(90), s.ingress(180), s.ingress(270)]

def print_cardinal_points(year: int | JulianDay) -> None:
    """
    print four cardinal points of year
    year can be specified as either integer or JulianDay
    """
    # get january 1 of year
    if isinstance(year,JulianDay):
        year = year.year()
    points = cardinal_points(year)

    print(f"Cardinal points for {year}\n")

    print("Ascending equinox:")
    print(points[0])
    print("Northern solstice:")
    print(points[1])
    print("Descending equinox:")
    print(points[2])
    print("Southern solstice:")
    print(points[3])
