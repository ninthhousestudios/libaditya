import swisseph as swe

from libaditya.objects import *
from libaditya.calc import *
from libaditya.charts import * 
from libaditya import constants as const
from libaditya import utils
from libaditya import read

base_path = os.path.dirname(os.path.realpath(__file__))

swe.set_ephe_path(base_path + "/ephe/")
