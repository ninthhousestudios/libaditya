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

from libaditya.objects import EphContext

import libaditya.star_signs.stars

# how you find the true sidereal ayanamsa
# swe.set_sid_mode(swe.SIDM_USER + swe.SIDBIT_USER_UT, 2451545.0, 31.2836)
# use swe.get_ayanamsa(tjd) to get ayanamsa on julian day tjd
# this is from the faq section of masteringthezodiac.com
star_signs_sweflg = swe.SIDM_USER + swe.SIDBIT_USER_UT
star_signs_ref_date = 2451545.0
star_signs_ayanamsa = 31.2836


