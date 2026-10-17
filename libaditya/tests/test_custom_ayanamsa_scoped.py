# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
"""using_custom_ayanamsa: a local definition that never replaces the saved one."""

import threading

import swisseph as swe

from libaditya import custom_ayanamsa as ca

JD = 2451545.0  # J2000


def _custom_offset():
    ca.apply_sid_mode(ca.CUSTOM_AYANAMSA_ID)
    return swe.get_ayanamsa_ut(JD)


def test_override_applies_inside_and_restores_after():
    ca.set_custom_ayanamsa(23.85, 2000, "Saved")
    calls = []
    ca.on_change(lambda: calls.append(1))
    with ca.using_custom_ayanamsa(20.0, 2000, "Preview"):
        assert ca.get_custom_ayanamsa() == ("Preview", 20.0, 2000)
        assert abs(_custom_offset() - 20.0) < 1e-6
    assert ca.get_custom_ayanamsa() == ("Saved", 23.85, 2000)
    assert abs(_custom_offset() - 23.85) < 1e-6
    assert calls == [], "a scoped override must not notify the caches"


def test_override_is_local_to_its_thread():
    ca.set_custom_ayanamsa(23.85, 2000, "Saved")
    seen = {}
    inside = threading.Event()
    release = threading.Event()

    def worker():
        with ca.using_custom_ayanamsa(21.0, 2000):
            inside.set()
            release.wait(5)
            seen["worker"] = ca.get_custom_ayanamsa()

    t = threading.Thread(target=worker)
    t.start()
    inside.wait(5)
    seen["main"] = ca.get_custom_ayanamsa()
    release.set()
    t.join(5)
    assert seen["main"] == ("Saved", 23.85, 2000)
    assert seen["worker"] == ("Custom", 21.0, 2000)
