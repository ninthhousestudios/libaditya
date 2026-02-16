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

from libaditya.objects import EphContext, Sun

class Returns:
    """
    inherits unto Rashi
    provides calculations for returns, e.g., solar return, etc.

    TODO:
    """

    def solar_return(self, year: int = None) -> EphContext:
        """
        return EphContext for the next time the Sun is at the same degree at it is in this Rashi

        if year is None, solar_return will calculate for the current year of the persons life
        i.e., year=0 is the birth year; year=1 is the next time it is at that degree

        of if you are 36, Rashi().solar_return() will give the current solar return chart for the time
        in between being 36 and 37
        """
        if year == None:
            year = int(self.context.timeJD.current_age())
        context = self.context
        original_sun = self.planets().sun()
        return_longitude = original_sun.ecliptic_longitude()
        while year > 0:
            this_sun = Sun(context)
            # move it forward slightly, so that when we ingress it to its ecliptic_longitude, its find the next time it is there
            this_sun = this_sun.ingress(this_sun.ecliptic_longitude()+.1)
            next_sun =  this_sun.ingress(return_longitude)
            context = next_sun.context
            year -= 1
        return self.master._new_context(context)
