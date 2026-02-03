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

import os
import pathlib
from dataclasses import replace
from typing import Self
import swisseph as swe

from libaditya.stars.stellarium.remote_control import RemoteControl

class Stellarium:
    """
    this is the main libaditya interface to stellarium

    it gets a RemoteControl(), which is code copied from another project (StellariumRC)
    rather than make it a dependency, I just copied the whole thing verbatim, with the license, etc.
    i believe its license, MIT, is more permissive.

    this interface abstracts the main functions needed from stellarium for its use in libaditya
    but the whole RemoteControl interface can be accessed through this object as well
    """

    def __init__(self, context, ip="127.0.0.1", port="8090", password=""):
        self.context = context
        self._rc = RemoteControl(ip,port,password)
        self.init_context()

    def rc(self):
        return self._rc

    def status(self):
        return self.rc().main.getStatus()

    def init_context(self):
        """
        move Stellarium to the time and place of self.context
        """
        self.stop_time()
        self.set_timeJD()
        self.set_location()

    def change_context(self,context):
        """
        replace self.context with context
        then initialize it
        """
        self.context = context
        self.init_context()

    def stop_time(self):
        """
        stop time moving in the stellarium
        it seems the default is for the time to be moving forward,
        which is nice when using the program
        """
        self.rc().main.setTimeRate(0)

    def set_timeJD(self):
        """
        set the time in stellarium to JulianDay self.context.timeJD
        """
        self.rc().main.setTimeJD(self.context.timeJD.jd_number())

    def set_location(self):
        """
        set the location in stellarium to Location self.context.location
        """
        self.rc().location.setLocation(longitude=self.context.location.longitude(),latitude=self.context.location.latitude(),name=self.context.location.placename(),planet=self.context.location.planet())

