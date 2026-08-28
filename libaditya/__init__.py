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
import pathlib
from dataclasses import replace
from rich.console import Console

from libaditya.objects import *
from libaditya.calc import *
from libaditya.charts import *
from libaditya.hd import *
from libaditya.stars import *
from libaditya.cards import *
from libaditya import constants as const
from libaditya import utils
from libaditya import read
from libaditya import write
from libaditya import print_functions as printf


# base_path means for libaditya src itself
base_path = os.path.dirname(os.path.realpath(__file__))
# the
package_path = os.path.dirname(pathlib.Path(__file__).parent) + "/"

swe.set_ephe_path(base_path + "/ephe/")

console = Console()

# from ._version import __version__
