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
import pathlib
from dataclasses import replace

from libaditya.objects import *
from libaditya.calc import *
from libaditya.charts import * 
from libaditya.hd import *
from libaditya import constants as const
from libaditya import utils
from libaditya import read
from libaditya import write
from libaditya import print_functions as printf


# base_path means for libaditya src itself
base_path = os.path.dirname(os.path.realpath(__file__))
# the 
package_path = os.path.dirname(pathlib.Path(__file__).parent)+"/"

swe.set_ephe_path(base_path + "/ephe/")

from ._version import __version__
