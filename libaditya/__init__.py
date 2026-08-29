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

# HISTORICAL (Phase 3, libaditya/4): libaditya's domain modules once bound the
# engine with `import swisseph as swe`, and a LIBADITYA_SWE_BACKEND env var could
# alias sys.modules["swisseph"] to a candidate before those imports ran. Since
# the Phase 2 cutover (libaditya/21) every ephemeris call goes through
# libaditya.ephemeris.seam onto swisseph_rs directly, and C pyswisseph has been
# dropped -- so no module imports "swisseph" and there is nothing left to alias.
# The env var is gone; swisseph_rs is the sole engine.
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
