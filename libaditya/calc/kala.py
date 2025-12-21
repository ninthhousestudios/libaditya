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

from libaditya.objects import JulianDay, Sun, EphContext

def lunar_new_year(year):
    """
    find chinese lunar new year in calendar year "year"
    """
    pass

def cardinal_points(year) -> [JulianDay]:
    """
    return the cardinal points of the year in order
    i.e., ascending equinox, northern solstice, descedending equinox, southern solstice
    """
    # get january 1 of year
    year_jd = swe.julday(year,1,1,0)
    s=Sun(EphContext(timeJD=JulianDay(year_jd)))
    return [s.ingress(0), s.ingress(90), s.ingress(180), s.ingress(270)]

def print_cardinal_points(year) -> None:
    pass
