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
from dataclasses import replace
from typing import Self

from libaditya import constants as const

from libaditya.objects import EphContext, Planets, Cusps, Circle
from libaditya.charts import Rashi, Varga

class Chart:

    def __init__(self, context=EphContext()):
        self.context = context
        self._Rashi = Rashi(Planets(self.context), Cusps(self.context), self.context, self)

    def __str__(self):
        return f"{self.rashi()}" 

    def __repr__(self):
        return self.__str__()

    def aditya(self, **kwargs):
        """
        take the current EphContext and change what is needed to make it a tropical Aditya chart

        sysflg=const.TROP
        circle=Circle.ADITYA
        names=replace(self.context.names,sign_names=const.adityas)

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,sysflg=const.TROP,circle=Circle.ADITYA,names=replace(self.context.names,sign_names=const.adityas),**kwargs))

    def tropical(self, **kwargs):
        """
        take the current EphContext and change what is needed to make it a tropical zodiac chart

        sysflg=const.TROP
        circle=Circle.ZODIAC
        names=replace(self.context.names,sign_names=const.zodiac)

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,sysflg=const.TROP,circle=Circle.ZODIAC,names=replace(self.context.names,sign_names=const.zodiac),**kwargs))

    def sidereal(self, **kwargs):
        """
        take the current EphContext and change what is needed to make it a sidereal zodiac chart

        sysflg=const.SID
        circle=Circle.ZODIAC
        names=replace(self.context.names,sign_names=const.zodiac)
        ayanamsa=98/36 by default; use Chart.sidereal(ayanamsa=n) to set the ayanamsa

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,sysflg=const.SID,circle=Circle.ZODIAC,names=replace(self.context.names,sign_names=const.zodiac),**kwargs))

    def _new_chart(self, **kwargs):
        """
        return a Chart replacing anything in this EphContext by **kwargs
        e.g., Chart.new_chart(hsys='R', ayanamsa=27) will return this Chart but using Regiomontanus house system
        and True Citra ayanamsa, all the other options staying the same

        be very careful with this as there are no protections on the option combinations and you could
        easily choose a combination of options that doesnt really make sense
        """
        return Chart(context=replace(self.context,**kwargs))

    def rashi(self):
        return self._Rashi

    def get_varga(self, amsha: int):
        """
        use Chart.rashi() for the rashi() chart
        you must pass an integer to get_varga
        Chart.get_varga(1) return something that has the same Planets and Cusps as the Rashi() chart, but
        is different in some respects...not sure if they should be or not, e.g., wrt to argala
        """
        return Varga(amsha,self.rashi().planets(),self.rashi().cusps(),self.context,self)

    def jaimini(self):
        from libaditya.charts import Jaimini
        return Jaimini(context=self.context)
