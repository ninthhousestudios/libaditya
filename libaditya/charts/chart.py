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

from libaditya import constants as const

from libaditya.objects import EphContext, Planets, Cusps, Circle, JulianDay
from libaditya.calc import Varga, Rashi
import libaditya.stars as stars

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
    libaditya_path = os.path.dirname(pathlib.Path(__file__).parent)+"/"
    ephe_path = libaditya_path + "ephe/"

    def __init__(self, context=EphContext()):
        swe.set_ephe_path(self.ephe_path)
        self.context = context
        self._Rashi = Rashi(self.context,self)

    def __repr__(self):
        return repr(self.rashi())

    def __str__(self):
        return self.__repr__()

    def chart(self):
        return self

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

    def saptavargas(self):
        """
        return a list of of the saptaVargas
        i.e., 1, -2, -3, 7, 9, -12, 30
        """
        saptavargas = [1,-2,-3,7,9,-12,30]
        return [Varga(self.context,amsha) for amsha in saptavargas]

    # do the other groups of vargas, dasha, etc.

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
        return Chart(context=replace(self.context,sysflg=const.TROP,circle=Circle.ADITYA,sign_names="adityas",**kwargs))

    def tropical(self, **kwargs):
        """
        take the current EphContext and change what is needed to make it a tropical zodiac chart

        sysflg=const.TROP
        circle=Circle.ZODIAC
        names=replace(self.context.names,sign_names=const.zodiac)

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,sysflg=const.TROP,circle=Circle.ZODIAC,sign_names="zodiac",**kwargs))

    def sidereal(self, ayanamsa=27, **kwargs):
        """
        take the current EphContext and change what is needed to make it a sidereal zodiac chart

        sysflg=const.SID
        circle=Circle.ZODIAC
        sign_names=sign_names=const.zodiac
        ayanamsa=27, True Citra ayanamsa by default; use Chart.sidereal(ayanamsa=n) to set the ayanamsa

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,ayanamsa=ayanamsa,sysflg=const.SID,circle=Circle.ZODIAC,sign_names="zodiac",**kwargs))

    def heliocentric(self, **kwargs):
        """
        take the current EphContext and change what is needed to make it a heliocentric chart

        sysflg=const.HELIO

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,sysflg=const.HELIO,**kwargs))

    def barycentric(self, **kwargs):
        """
        take the current EphContext and change what is needed to make it a barycentric chart

        sysflg=const.BARY

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,sysflg=const.BARY,**kwargs))

    def draconic(self, **kwargs):
        """
        take the current EphContext and change what is needed to make it a draconic chart

        sysflg=const.DRAC

        **kwargs can take any keyword argument that can be used for EphContext
        so if you want to change the ayanamsa, pass Chart.aditya(ayanamsa=27) and it will give you a new chart for that
        """
        return Chart(context=replace(self.context,sysflg=const.DRAC,**kwargs))

    def shift(self, dir, unit, number):
        """
        calls self.JulianDay effectively and return a Chart with shifted JulianDay
        """
        return Chart(context=replace(self.context,timeJD=self.context.timeJD.shift(dir,unit,number)))

    def timejd(self, next_time):
        """
        shift the time only
        current next_time only accepts a julianday number
        carries along the timezone from this context
        """
        if isinstance(next_time, float):
            return Chart(context=replace(self.context,timeJD=JulianDay(next_time,self.context.timeJD.utcoffset)))

    def now(self):
        """
        return a chart like this one but for right now
        """
        return Chart(context=replace(self.context,timeJD=JulianDay("now",self.context.timeJD.utcoffset)))

    def _new_chart(self, **kwargs):
        """
        return a Chart replacing anything in this EphContext by **kwargs
        e.g., Chart.new_chart(hsys='R', ayanamsa=27) will return this Chart but using Regiomontanus house system
        and True Citra ayanamsa, all the other options staying the same

        be very careful with this as there are no protections on the option combinations and you could
        easily choose a combination of options that doesnt really make sense
        """
        return Chart(context=replace(self.context,**kwargs))

    def the_Stars(self):
        """
        this literally returns the module stars.the_stars

        this lets you do things like
        Chart().the_Stars().Erakis()
        this is good if you known specifically which FixedStar class you want; this gives access like that

        the stand approach is to use the (,)noMen name with TheStars, e.g.,:
        >>> TheStars()["alTau"]

        the other thing is that there are sometimes multiple long names for one noMen name
        TheStars() only has access to one of those
        e.g., TheStars()[",muCep"] returns TheGarnetStar()
        however, if we do:
        >>> TheStars()["muCep"]() ==  Chart().the_Stars().Erakis()
        True
        likewise
        >>> Chart().the_Stars().TheGarnetStar() ==  Chart().the_Stars().Erakis()
        True
        >>> Chart().the_Stars().TheGarnetStar ==  Chart().the_Stars().Erakis
        False
        this is because the constructors are different, but functionally they are the same
        any two objects that have the same swe_id() are the same in this sense
        this is about the object; they could be on different days, == only checks if swe_id() is the same
        """
        return stars.the_stars
