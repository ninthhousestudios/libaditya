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
from dataclasses import replace

from libaditya import utils

from libaditya.objects import JulianDay, EphContext

class SWERashi:
    """
    swe functions that seem best placed in the Rashi
    e.g., swe.sol_eclipse_when_loc(), the next solar eclipse for a location
    can easily adjust Rashi to do horary, prashna, or whatever. most of the calculations are there
    the rest is mostly api
    """

    def next_solar_eclipse_here(self):
        """
        return the next solar eclipse
        return the Chart of that eclipse, or the context?
        """
        return swe.sol_eclipse_when_loc(self.context.timeJD.jd_number(),self.context.location.swe_location())

    def next_solar_eclipse_here_maximum(self):
        return replace(self.context,timeJD=JulianDay(self.next_solar_eclipse_here()[1][0],self.context.timeJD.utcoffset))

    def previous_solar_eclipse_here(self):
        """
        return the previous solar eclipse
        return the Chart of that eclipse, or the context?
        """
        return swe.sol_eclipse_when_loc(self.context.timeJD.jd_number(),self.context.location.swe_location(),backwards=True)

    def previous_solar_eclipse_here_maximum(self):
        return repalce(self.context,timeJD=JulianDay(self.previous_solar_eclipse_here()[1][0],self.context.timeJD.utcoffset))

    def next_solar_eclipse(self, etype=0) -> EphContext:
        """
        find the next solar eclipse from this.context.timeJD
        type is the swe flags for kinds of eclipses to return
        0 is any, so this just returns the next eclipse of any variety
        happening anywhere in the world

        by calculation, it can be in Sun, but it makes more sense overall, since astrologically
        it is often about everything, not just the sun. so return an EphContext

        return the EphContext of the next solar eclipse
        """
        return swe.sol_eclipse_when_glob(self.context.timeJD.jd_number(),etype)

    def next_solar_eclipse_maximum(self, etype=0) -> EphContext:
        return replace(self.context,timeJD=JulianDay(self.next_solar_eclipse()[1][0],self.context.timeJD.utcoffset))

    def previous_solar_eclipse(self, etype=0) -> EphContext:
        """
        find the previous solar eclipse from this.context.timeJD
        type is the swe flags for kinds of eclipses to return
        0 is any, so this just returns the next eclipse of any variety
        happening anywhere in the world

        that is why it is here is Sun; obviously it has to do with the Moon to, but the swe function
        does not explicitly require the Moon

        return the EphContext of the next solar eclipse
        """
        return swe.sol_eclipse_when_glob(self.context.timeJD.jd_number(),etype,backwards=True)

    def previous_solar_eclipse_maximum(self, etype=0) -> EphContext:
        return replace(self.context,timeJD=JulianDay(self.previous_solar_eclipse()[1][0],self.context.timeJD.utcoffset))

    def next_lunar_eclipse(self, etype=0) -> EphContext:
        """
        find the next lunar eclipse from this.context.timeJD
        type is the swe flags for kinds of eclipses to return
        0 is any, so this just returns the next eclipse of any variety
        happening anywhere in the world

        by calculation, it can be in Sun, but it makes more sense overall, since astrologically
        it is often about everything, not just the sun. so return an EphContext

        return the EphContext of the next lunar eclipse
        """
        return swe.lun_eclipse_when(self.context.timeJD.jd_number(),etype)

    def next_lunar_eclipse_maximum(self, etype=0) -> EphContext:
        return replace(self.context,timeJD=JulianDay(self.next_lunar_eclipse()[1][0],self.context.timeJD.utcoffset))

    def previous_lunar_eclipse(self, etype=0) -> EphContext:
        """
        find the previous lunar eclipse from this.context.timeJD
        type is the swe flags for kinds of eclipses to return
        0 is any, so this just returns the next eclipse of any variety
        happening anywhere in the world

        that is why it is here is Sun; obviously it has to do with the Moon to, but the swe function
        does not explicitly require the Moon

        return the EphContext of the next lunar eclipse
        """
        return swe.lun_eclipse_when(self.context.timeJD.jd_number(),etype,backwards=True)

    def previous_lunar_eclipse_maximum(self, etype=0) -> EphContext:
        return replace(self.context,timeJD=JulianDay(self.previous_lunar_eclipse()[1][0],self.context.timeJD.utcoffset))
