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
from libaditya.calc import Varga, Rashi

from .api import API
from .bodygraph import Bodygraph

class Chart(API):
    """
    the primary interface into libaditya is the Chart
    Chart is a collection of vargas

    it explicity includes a Rashi chart Chart.rashi()
    any implemented varga can gotten by Chart.varga(varga_code)

    can return a new Chart that has different options set
    aditya(),tropical(),sidereal() all have certain options they set, any others can be passed as keyword arguments, e.g., ayanamsa=27
    defaults are documented in those functions

    Jaimini and Tajika inherit from Chart, and they are here to give syntactic functionality to this
    simply for ease of use; explained more in a code comment

    the actually functionality is provided through Varga and on down.

    where the syntax for chart=Chart() is chart.jaimini().first_strength()
    .first_strength() actually belongs to Varga...so on any varga you can call
    Varga.jaimini_first_strength()

    not sure this syntax is really worth it? leaving it for now
    """

    def __init__(self, context=EphContext()):
        self.context = context
        self._Rashi = Rashi(self.context,self)

    def __repr__(self):
        return repr(self.rashi())

    def __str__(self):
        return "Chart str"

    def rashi(self):
        return self._Rashi

    def bodygraph(self):
        return Bodygraph(self.context)

    def varga(self, amsha: int):
        """
        use Chart.rashi() for the rashi() chart
        you must pass an integer to varga
        Chart.varga(1) return something that has the same Planets and Cusps as the Rashi() chart, but
        is different in some respects...not sure if they should be or not, e.g., wrt to argala

        1-N for positive integers make a parivritti varga of that amsha
        special vargas have negative integer codes (updated here as implemeneted)
        these vargas all have deities associated with the amsha in various ways
        these can be accessed by Longitude.deity(). Longitude knows what amsha it is in. Longitude.lord() gives the
        planetary lord for the sign Longitude inhabits in the amsha.
            -2 Hora; Sun and Moon, same stays, opposite goes opposite
            -3 Drekkana;
        """
        return Varga(self.context,amsha)

    # jaimini and tajika
    # these inherit from Chart, then Chart calls them here, which is why there is a local import statement
    # the reason is that i like to have the syntax, e.g., chart.jaimini().pada()
    # i could make a Mixin like with Varga and calc.Jaimini, then the syntax would be
    # chart.jaimini_pada(), chart.tajika_vargas(); but for some reason, i want to be able to write, chart.tajika()
    # really, if you want to really use that chart, then do tajika_chart = chart.tajika()
    # jaimini and tajika really just contain wrappers and syntax for that functionality
    # the calculation is also done lower, e.g., in Varga

    def jaimini(self):
        from libaditya.charts import Jaimini
        return Jaimini(context=self.context)

    def tajika(self):
        from libaditya.charts import Tajika
        return Tajika(context=self.context)

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

    def sidereal(self, ayanamsa=27, **kwargs):
        """
        take the current EphContext and change what is needed to make it a sidereal zodiac chart

        sysflg=const.SID
        circle=Circle.ZODIAC
        names=replace(self.context.names,sign_names=const.zodiac)
        ayanamsa=27, True Citra ayanamsa by default; use Chart.sidereal(ayanamsa=n) to set the ayanamsa

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,ayanamsa=ayanamsa,sysflg=const.SID,circle=Circle.ZODIAC,names=replace(self.context.names,sign_names=const.zodiac),**kwargs))

    def _new_chart(self, **kwargs):
        """
        return a Chart replacing anything in this EphContext by **kwargs
        e.g., Chart.new_chart(hsys='R', ayanamsa=27) will return this Chart but using Regiomontanus house system
        and True Citra ayanamsa, all the other options staying the same

        be very careful with this as there are no protections on the option combinations and you could
        easily choose a combination of options that doesnt really make sense
        """
        return Chart(context=replace(self.context,**kwargs))



