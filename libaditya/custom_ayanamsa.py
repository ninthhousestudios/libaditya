# Copyright (C) 2026 Lorris Turpin / 360 Hearts in the Sky
# Licensed under AGPL-3.0 — see LICENSE file for details.
"""The user's own ayanamsa (id 255) and the one place that sets the Swiss sidereal mode.

A custom ayanamsa is a value in degrees at a reference year. Swiss Ephemeris
user mode (SIDM_USER) carries it to any other date with its own precession
model, so it behaves like the built-in modes everywhere: planets, cusps,
nakshatras and the offset readouts.

Every engine site that used to call ``swe.set_sid_mode(ayanamsa)`` calls
``apply_sid_mode(ayanamsa)`` instead; with a built-in id it is exactly the same
call. The definition is process state, set from the settings at startup and on
Apply; modules that cache by ayanamsa id register ``on_change`` to drop their
cache when it changes.
"""

import swisseph as swe

from libaditya import utils

CUSTOM_AYANAMSA_ID = 255  # == swe.SIDM_USER

DEFAULT_NAME = "Custom"
DEFAULT_VALUE_DEG = 23.85  # degrees at the reference year
DEFAULT_REFERENCE_YEAR = 2000

_state = {
    "name": DEFAULT_NAME,
    "value": DEFAULT_VALUE_DEG,
    "year": DEFAULT_REFERENCE_YEAR,
}
_listeners = []


def reference_jd(year):
    """1 January of ``year`` at 12:00 UT; year 2000 gives J2000 (2451545.0)."""
    return swe.julday(int(year), 1, 1, 12.0)


def get_custom_ayanamsa():
    """(name, value_deg, reference_year) of the current definition."""
    return _state["name"], _state["value"], _state["year"]


def set_custom_ayanamsa(value_deg, reference_year, name=""):
    """Install a definition; notify the caches only when it really changed."""
    new = {
        "name": (name or "").strip() or DEFAULT_NAME,
        "value": float(value_deg),
        "year": int(reference_year),
    }
    if new == _state:
        return False
    _state.update(new)
    for callback in list(_listeners):
        callback()
    return True


def on_change(callback):
    """Call ``callback()`` whenever the definition changes (cache_clear hooks)."""
    if callback not in _listeners:
        _listeners.append(callback)
    return callback


def apply_sid_mode(ayanamsa):
    """``swe.set_sid_mode`` for any ayanamsa id, including the custom one.

    Also carries libaditya's true-sidereal code 97 (an SVP-based user mode): a
    plain ``swe.set_sid_mode(97)`` would silently clamp to Fagan-Bradley, so
    planets, cusps and nakshatras must all come through here to agree. The
    98->36 sign remap is NOT applied here; callers that need it remap first.
    """
    if ayanamsa == 97:
        utils.set_swe_true_sidereal_ayanamsa()
    elif ayanamsa == CUSTOM_AYANAMSA_ID:
        swe.set_sid_mode(
            swe.SIDM_USER + swe.SIDBIT_USER_UT,
            reference_jd(_state["year"]),
            _state["value"],
        )
    else:
        swe.set_sid_mode(ayanamsa)
