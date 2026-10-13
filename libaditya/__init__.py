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
import os
import pathlib

base_path = os.path.dirname(os.path.realpath(__file__))
package_path = os.path.dirname(pathlib.Path(__file__).parent) + "/"
swe.set_ephe_path(base_path + "/ephe/")

from libaditya import constants as const
from libaditya import utils
from libaditya import read
from libaditya import write
from libaditya import print_functions as printf

_LAZY_IMPORTS = {
    'JulianDay': 'libaditya.objects.julian_day',
    'Planet': 'libaditya.objects.planets',
    'Planets': 'libaditya.objects.planets',
    'Sun': 'libaditya.objects.planets',
    'Moon': 'libaditya.objects.planets',
    'Mars': 'libaditya.objects.planets',
    'Mercury': 'libaditya.objects.planets',
    'Venus': 'libaditya.objects.planets',
    'Jupiter': 'libaditya.objects.planets',
    'Saturn': 'libaditya.objects.planets',
    'Rahu': 'libaditya.objects.planets',
    'Ketu': 'libaditya.objects.planets',
    'Longitude': 'libaditya.objects.longitude',
    'Location': 'libaditya.objects.location',
    'Yamakoti': 'libaditya.objects.location',
    'EphContext': 'libaditya.objects.context',
    'Circle': 'libaditya.objects.context',
    'Cusp': 'libaditya.objects.cusps',
    'Cusps': 'libaditya.objects.cusps',
    'Nakshatra': 'libaditya.objects.nakshatras',
    'Nakshatras': 'libaditya.objects.nakshatras',
    'RashiBala': 'libaditya.objects.shadbala',
    'Sign': 'libaditya.objects.signs',
    'Signs': 'libaditya.objects.signs',
    'Panchanga': 'libaditya.calc.panchanga',
    'Varga': 'libaditya.calc.varga',
    'Rashi': 'libaditya.calc.rashi',
    'Jaimini': 'libaditya.charts.jaimini',
    'API': 'libaditya.charts.api',
    'Chart': 'libaditya.charts.chart',
    'Tajika': 'libaditya.charts.tajika',
    'HDLongitude': 'libaditya.hd.longitude',
    'YiLongitude': 'libaditya.hd.longitude',
    'TheStars': 'libaditya.stars.the_stars',
    'Deck': 'libaditya.cards.deck',
    'CardsOfTruth': 'libaditya.cards.cards_of_truth',
    'CoT': 'libaditya.cards.cot',
}


def __getattr__(name):
    if name in _LAZY_IMPORTS:
        import importlib
        module = importlib.import_module(_LAZY_IMPORTS[name])
        attr = getattr(module, name)
        globals()[name] = attr
        return attr
    if name == 'console':
        from rich.console import Console
        c = Console()
        globals()['console'] = c
        return c
    if name == 'replace':
        from dataclasses import replace as _replace
        globals()['replace'] = _replace
        return _replace
    raise AttributeError(f"module 'libaditya' has no attribute {name}")

