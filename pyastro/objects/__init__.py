from .julian_day import JulianDay
from .planet import *
from .planets import *
from .location import Location, Yamakoti
from .context import EphContext

import os
import pathlib
import swisseph as swe
from pyastro import constants as const

base_path = os.path.dirname(pathlib.Path(__file__).parent)

swe.set_ephe_path(base_path + "/ephe/")
