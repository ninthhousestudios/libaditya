# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
#
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

"""Fast, dependency-light smoke test of the public API.

Not a regression check -- that is the golden-master harness
(``python -m libaditya.tests.golden``).  This just asserts the library imports
and the headline chainable calls actually *run* and return sane, shaped output
on a pinned chart: rashi positions, a varga, panchanga, the Human Design
bodygraph definition layer, and a Cards-of-Truth birth card.  It uses fixed
birth data (no wall clock) and ``icao=None`` (no METAR network call), so it is
reproducible and offline.

Run it directly::

    python -m libaditya.tests.legacy_smoke

Exit code is 0 when every check passes, 1 otherwise.

(The file kept its historical name; its previous contents were a dead fragment
of the original ``libaditya.py`` CLI -- undefined names, a Planet constructor
signature that no longer exists -- that had never been runnable.)
"""

from __future__ import annotations

import sys

from libaditya import Chart, EphContext, JulianDay, Location
from libaditya.hd import constants as hdc

# A pinned subject: New York, 1990-02-13 22:30 UTC (matches the golden `nyc`).
_JD = (1990, 2, 13, 22.5)
_UTCOFFSET = -5.0


def _pinned_chart() -> Chart:
    jd = JulianDay(_JD, utcoffset=_UTCOFFSET, timezone="America/New_York")
    location = Location(
        lat=40.7128,
        long=-74.0060,
        alt=10.0,
        placename="New York",
        utcoffset=_UTCOFFSET,
        icao=None,  # no METAR lookup
    )
    return Chart(EphContext(name="smoke", timeJD=jd, location=location)).aditya()


def _check(label: str, condition: bool) -> bool:
    print(f"  [{'PASS' if condition else 'FAIL'}] {label}")
    return condition


def run() -> bool:
    print("libaditya smoke test (pinned nyc / aditya)")
    chart = _pinned_chart()
    ok = True

    rashi = chart.rashi()
    planets = list(rashi.planets())
    ok &= _check("rashi computes >= 10 planets", len(planets) >= 10)
    ok &= _check(
        "every planet longitude in [0, 360)",
        all(0.0 <= p.ecliptic_longitude() < 360.0 for p in planets),
    )
    ok &= _check("lagna resolves to a sign 1..12", rashi.lagna().sign() in range(1, 13))

    d9 = chart.varga(9)
    ok &= _check(
        "navamsha (D9) lagna is a sign 1..12", d9.lagna().sign() in range(1, 13)
    )

    pan = rashi.panchanga()
    ok &= _check("panchanga tithi in 1..30", pan._tithi_number in range(1, 31))

    bg = chart.bodygraph()
    centers = bg.defined_centers()
    ok &= _check("bodygraph reports all 9 centers", len(centers) == 9)
    channels = bg.defined_channels()
    ok &= _check("defined channels are a subset of the 36", 0 <= len(channels) <= 36)
    ok &= _check(
        "a defined channel implies both its centers are defined",
        all(
            centers[a] and centers[b]
            for a, b in (hdc.channels[pair] for pair in channels)
        ),
    )

    card = chart.cot().birth_card()
    ok &= _check(
        "cot birth card is a two-character code",
        isinstance(card, str) and len(card) == 2,
    )

    return bool(ok)


def main() -> int:
    passed = run()
    print("OK" if passed else "FAILED")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
