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

from libaditya.objects import Planet

class Hellenistic:
    """
    inherits unto Rashi
    provides calculations used for hellenistic astrology

    TODO:
    first thing, profections
    Chart().natal().profection() should list the current year lord
    Chart().natal().profection(n) should list the year lord at age n
    also implement monthly, daily, hourly profections
    """

    def profection(self, year=None) -> Planet:
        """
        return year lord for current year if year is None
        otherwise, for the age year
        """
        pass
