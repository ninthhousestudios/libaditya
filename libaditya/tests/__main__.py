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

"""One-step regression entry: run the whole libaditya test suite.

    python -m libaditya.tests

Runs the offline smoke test and then the golden-master regression check (on
``swisseph_rs``, libaditya's sole ephemeris engine) in sequence, and exits
non-zero if either fails. This is the single command CI or a human runs to gate
a change.

For anything beyond the default run -- re-blessing fixtures, a case subset, a
looser tolerance -- drive the golden harness directly:

    python -m libaditya.tests.golden --help

See ``docs/golden-master-harness.md`` for the full workflow.
"""

from __future__ import annotations

import sys

from . import legacy_smoke
from .golden import __main__ as golden_cli


def main() -> int:
    print("=== smoke ===")
    smoke_rc = legacy_smoke.main()

    print("\n=== golden-master ===")
    golden_rc = golden_cli.main([])  # default backend, all cases, check (no freeze)

    print()
    ok = smoke_rc == 0 and golden_rc == 0
    print("SUITE OK" if ok else "SUITE FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
