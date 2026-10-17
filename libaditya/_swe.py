# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC

#    This file is part of libaditya.
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

"""
swisseph, with libaditya's ephemeris path set on whichever thread calls it

Swiss Ephemeris keeps its state per thread, so a path set at import holds only
on the importing thread. On any other thread swisseph looks in its default
path, where the asteroid files (seas_*.se1, used by Chiron) and sefstars.txt
are missing, so those calls raise; and the planets silently fall back to the
Moshier ephemeris, which moves them by fractions of an arcsecond with no error.

every libaditya module imports swisseph through here:

    from libaditya import _swe as swe

every swisseph function is re-exported wrapped so that it sets the path on the
calling thread first (once per thread); constants and the
swe.Error exception class are re-exported as they are.
"""

import functools
import os
import threading

import swisseph as _swisseph

LIBADITYA_EPHE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/ephe/"

_thread = threading.local()


def ensure_ephe_path():
    """set libaditya's ephemeris path on the current thread, if not yet set there"""
    try:
        _thread.ephe_path_set
    except AttributeError:
        _swisseph.set_ephe_path(LIBADITYA_EPHE_PATH)
        _thread.ephe_path_set = True


def _on_this_thread(function):
    @functools.wraps(function)
    def call(*args, **kwargs):
        try:
            _thread.ephe_path_set
        except AttributeError:
            ensure_ephe_path()
        return function(*args, **kwargs)

    return call


# bound as module globals, not served by a module __getattr__: libaditya reads
# swe.<name> in its innermost loops, and a __getattr__ on every read cost ~17%
# of the golden-master run
for _name in dir(_swisseph):
    if _name.startswith("__"):
        continue
    _value = getattr(_swisseph, _name)
    if callable(_value) and not isinstance(_value, type):
        _value = _on_this_thread(_value)
    globals()[_name] = _value
del _name, _value
