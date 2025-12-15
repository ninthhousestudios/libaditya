import swisseph as swe
from pyastro import constants as const

base_path = os.path.dirname(os.path.realpath(__file__))

swe.set_ephe_path(base_path + "/ephe/")
