from .julian_day import JulianDay
from .planets import *
from .location import Location, Yamakoti
from .context import EphContext
from .cusps import Cusp, Cusps
from .nakshatra import Nakshatra, Nakshatras

import os
import pathlib
import swisseph as swe
from libaditya import constants as const

base_path = os.path.dirname(pathlib.Path(__file__).parent)

swe.set_ephe_path(base_path + "/ephe/")
