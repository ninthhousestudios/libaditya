# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC

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

# --- ephemeris backend selection (must run before `import swisseph`) --------
# Set the LIBADITYA_SWE_BACKEND environment variable to the name of an
# API-compatible ephemeris module (e.g. "swisseph_rs") to make every
# `import swisseph as swe` in libaditya bind to it instead of pyswisseph. This
# is the switch the golden-master harness uses to compare backends. Unset (the
# default) leaves pyswisseph in place and changes nothing.
import os as _os
import sys as _sys

_swe_backend = _os.environ.get("LIBADITYA_SWE_BACKEND")
if _swe_backend and _swe_backend not in ("swisseph", "pyswisseph"):
    import importlib as _importlib

    _sys.modules["swisseph"] = _importlib.import_module(_swe_backend)

import swisseph as swe
import os
import pathlib

base_path = os.path.dirname(os.path.realpath(__file__))
package_path = os.path.dirname(pathlib.Path(__file__).parent) + "/"
swe.set_ephe_path(base_path + "/ephe/")

from libaditya._version import __version__
from libaditya import _extras

_extras.install()

from libaditya import constants as const
from libaditya import utils
from libaditya import read
from libaditya import write
from libaditya import print_functions as printf

_LAZY_IMPORTS = {
    "JulianDay": "libaditya.objects.julian_day",
    "Planet": "libaditya.objects.planets",
    "Planets": "libaditya.objects.planets",
    "Sun": "libaditya.objects.planets",
    "Moon": "libaditya.objects.planets",
    "Mars": "libaditya.objects.planets",
    "Mercury": "libaditya.objects.planets",
    "Venus": "libaditya.objects.planets",
    "Jupiter": "libaditya.objects.planets",
    "Saturn": "libaditya.objects.planets",
    "Rahu": "libaditya.objects.planets",
    "Ketu": "libaditya.objects.planets",
    "Longitude": "libaditya.objects.longitude",
    "Location": "libaditya.objects.location",
    "Yamakoti": "libaditya.objects.location",
    "EphContext": "libaditya.objects.context",
    "Circle": "libaditya.objects.context",
    "Cusp": "libaditya.objects.cusps",
    "Cusps": "libaditya.objects.cusps",
    "Nakshatra": "libaditya.objects.nakshatras",
    "Nakshatras": "libaditya.objects.nakshatras",
    "RashiBala": "libaditya.objects.shadbala",
    "Sign": "libaditya.objects.signs",
    "Signs": "libaditya.objects.signs",
    "Panchanga": "libaditya.calc.panchanga",
    "Varga": "libaditya.calc.varga",
    "Rashi": "libaditya.calc.rashi",
    "Jaimini": "libaditya.charts.jaimini",
    "API": "libaditya.charts.api",
    "Chart": "libaditya.charts.chart",
    "Tajika": "libaditya.charts.tajika",
    "HDLongitude": "libaditya.hd.longitude",
    "YiLongitude": "libaditya.hd.longitude",
    "TheStars": "libaditya.stars.the_stars",
    "Deck": "libaditya.cards.deck",
    "CardsOfTruth": "libaditya.cards.cards_of_truth",
    "CoT": "libaditya.cards.cot",
}


def __getattr__(name):
    if name in _LAZY_IMPORTS:
        import importlib

        module = importlib.import_module(_LAZY_IMPORTS[name])
        attr = getattr(module, name)
        globals()[name] = attr
        return attr
    if name == "console":
        from rich.console import Console

        c = Console()
        globals()["console"] = c
        return c
    if name == "replace":
        from dataclasses import replace as _replace

        globals()["replace"] = _replace
        return _replace
    if name == "__all__":
        return _star_exports()
    raise AttributeError(f"module 'libaditya' has no attribute {name}")


def _star_exports():
    """`from libaditya import *` stays eager: everything the subpackages export.

    `import libaditya` (and `from libaditya.x import y`) only pays for what it
    touches; the star-import asks for __all__, which lands here and loads the
    whole library, in the same order and with the same winners as before the
    imports went lazy.
    """
    import importlib

    g = globals()
    aliases = {k: g[k] for k in ("const", "utils", "read", "write", "printf")}
    for pkg in ("objects", "calc", "charts", "hd", "stars", "cards"):
        mod = importlib.import_module(f"libaditya.{pkg}")
        for n, v in vars(mod).items():
            if not n.startswith("_"):
                g[n] = v
    g.update(aliases)
    __getattr__("console")
    __getattr__("replace")
    names = [n for n in g if not n.startswith("_")]
    g["__all__"] = names
    return names
