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
from dataclasses import replace

from libaditya.objects import Sun, EphContext

def unconscious_context(context=EphContext()):
    """
    return an EphContext where the time is the hd unconscious "design" date, 88 degrees of the Sun's motion before the conscious "personality" date, i.e., the birth date and time
    """
    sun=Sun(context)
    sought_longitude = (sun.ecliptic_longitude()-88)%360

    # go back before 88 degrees
    # Sun.ingress finds the next time the Sun is at the ecliptic_longitude passed to .ingress()
    # so go before the time we need, and it will get the next time
    past_sun = Sun(replace(sun.context,timeJD=sun.timeJD.shift('b','days',95)))
    # unconscious sun
    usun = past_sun.ingress(sought_longitude)

    # we are returning an EphContext; not the unconscious sun, but the EphContext of the unconscious sun
    return replace(context,timeJD=usun.timeJD)
