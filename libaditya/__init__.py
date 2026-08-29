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

# --- ephemeris backend selection (harness-only; VESTIGIAL for libaditya) -----
# HISTORICAL: libaditya's domain modules used to bind the engine with
# `import swisseph as swe`, so setting LIBADITYA_SWE_BACKEND to an API-compatible
# module name aliased sys.modules["swisseph"] before those imports ran.
#
# Post-cutover (libaditya/21) NO domain module imports swisseph -- every
# ephemeris call goes through libaditya.ephemeris.seam onto swisseph_rs directly.
# So this alias no longer affects libaditya's own runtime. It is retained ONLY
# for the golden harness's backend contract (tests/golden/backend.py) and the
# seam/distiller reference tests, which still `import swisseph` to compare the
# seam against C pyswisseph. Unset (the default) it is inert.
import os as _os
import sys as _sys

_swe_backend = _os.environ.get("LIBADITYA_SWE_BACKEND")
if _swe_backend and _swe_backend not in ("swisseph", "pyswisseph"):
    import importlib as _importlib

    _sys.modules["swisseph"] = _importlib.import_module(_swe_backend)

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

console = Console()

# from ._version import __version__
