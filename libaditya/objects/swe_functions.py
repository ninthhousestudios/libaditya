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

from libaditya import utils

from libaditya.objects import JulianDay

class SWEFirstLast:
    """
    this class inherits unto Moon, Mercury, Venus
    contains all the relevant swe functions

    will document here as implemented
    
    next_heliacal_rising()
    next_heliacal_setting() -> if either is Moon, returns None
    next_evening_first()
    next_morning_last() -> both for Moon, Mercury, Venus only
    """

    def next_evening_first(self):
        if self.identity() not in ["Moon", "Mercury", "Venus"]:
            return
        return utils.toJD(swe.heliacal_ut(
            self.timeJD.jd_number(),
            self.context.location.swe_location(),
            # need to figure out how to get current information for the place
            # relative humdity can do with metpy, but it is a lot of dependcies for just one thing that
            # may not really be that important
            # the 4-tuple of 0 sets atmospheric information to general values
            (0,0,0,0),
            # a 6-tuple of values relative to an observer and various observing situations
            (0,0,0,0,0,0),
            self.identity(),
            swe.EVENING_FIRST,
            # this is the ephemeris flag, i think
            self.sysflg
       ), self.context)

    def next_morning_last(self) -> [JulianDay]:
        if self.identity() not in ["Moon", "Mercury", "Venus"]:
            return
        return utils.toJD(swe.heliacal_ut(
            self.timeJD.jd_number(),
            self.context.location.swe_location(),
            # need to figure out how to get current information for the place
            # relative humdity can do with metpy, but it is a lot of dependcies for just one thing that
            # may not really be that important
            # the 4-tuple of 0 sets atmospheric information to general values
            (0,0,0,0),
            # a 6-tuple of values relative to an observer and various observing situations
            (0,0,0,0,0,0),
            self.identity(),
            swe.MORNING_LAST,
            # this is the ephemeris flag, i think
            self.sysflg
       ), self.context)


    # add meridian transits
