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

from libaditya.objects import Sign

class API:
    """
    a Mixin API for Varga
    these are just functions to help make finding information easier
    these are all simply wrappers for other functions
    e.g., rashi_aspects are computed by Signs, but there is a function in here
    to access them from Varga
    """

    def rashi_aspects_given_to(self, sign: Sign) -> [Sign]:
        return self.signs().rashi_aspects_given_to(sign)
