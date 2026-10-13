from .the_stars import TheStars
from .utilities import *


def __getattr__(name):
    if name == 'stellarium':
        from .stellarium import stellarium as _s
        globals()['stellarium'] = _s
        return _s
    if name == 'RemoteControl':
        from .stellarium import RemoteControl as _rc
        globals()['RemoteControl'] = _rc
        return _rc
    if name == 'Stellarium':
        from .stellarium import Stellarium as _st
        globals()['Stellarium'] = _st
        return _st
    raise AttributeError(f"module 'libaditya.stars' has no attribute {name}")
