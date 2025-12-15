import swisseph as swe

from pyastro.objects import *
from pyastro import constants as const
from pyastro import utils
from pyastro import read

base_path = os.path.dirname(os.path.realpath(__file__))

swe.set_ephe_path(base_path + "/ephe/")
