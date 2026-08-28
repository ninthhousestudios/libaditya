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

"""Single runnable entry point for the golden harness.

    python -m libaditya.tests.golden --backend=pyswisseph          # check
    python -m libaditya.tests.golden --update                      # (re)freeze
    python -m libaditya.tests.golden --case nyc-aditya --case sydney-aditya
    python -m libaditya.tests.golden --list

The backend is chosen *before* libaditya is imported (see ``backend``), so the
heavy ``harness`` import is deferred until after ``select_backend`` has run.
"""

from __future__ import annotations

import argparse
import sys

from . import backend


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m libaditya.tests.golden",
        description="Golden-master regression harness for libaditya.",
    )
    parser.add_argument(
        "--backend",
        default=backend.DEFAULT_BACKEND,
        choices=sorted(backend.BACKENDS),
        help="ephemeris engine the CANDIDATE runs on (goldens are always frozen "
        "from pyswisseph). default: %(default)s",
    )
    parser.add_argument(
        "--update",
        "--bless",
        action="store_true",
        dest="update",
        help="(re)freeze the selected cases' golden fixtures from this backend",
    )
    parser.add_argument(
        "--case",
        action="append",
        dest="cases",
        metavar="CASE_ID",
        help="restrict to this case id (repeatable); default: all cases",
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=None,
        help="absolute numeric comparison tolerance (default: harness default 1e-9)",
    )
    parser.add_argument("--list", action="store_true", help="list case ids and exit")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    # Bind the ephemeris backend BEFORE importing anything that imports libaditya.
    provenance = backend.select_backend(args.backend)

    # Safe to pull in the libaditya-touching modules now.
    from . import harness

    cases = harness.all_cases()

    if args.list:
        for case in cases:
            extra = f"  (+{', '.join(case.extra_views)})" if case.extra_views else ""
            print(f"{case.id}{extra}")
        return 0

    selected = harness.select_cases(cases, args.cases)

    print(
        f"backend:   {provenance['backend']} "
        f"(module={provenance['module']}, version={provenance['version']})"
    )
    eph = harness.ephemeris_provenance()
    print(f"ephemeris: {eph.get('header', eph)}")
    print(f"cases:     {len(selected)} selected of {len(cases)}")
    print()

    if args.update:
        if args.backend != backend.DEFAULT_BACKEND:
            print(
                f"WARNING: freezing goldens from {args.backend!r}, not the "
                f"reference {backend.DEFAULT_BACKEND!r}.\n"
            )
        report = harness.freeze(selected)
        for outcome in report.outcomes:
            mark = "froze" if outcome.status == "frozen" else "ERROR"
            line = f"  [{mark}] {outcome.case_id}"
            if outcome.message:
                line += f"  -- {outcome.message}"
            print(line)
        print()
        errors = [o for o in report.outcomes if o.status == "error"]
        print(f"{len(report.outcomes) - len(errors)} frozen, {len(errors)} errored")
        return 1 if errors else 0

    tol_kwargs = {} if args.tolerance is None else {"tol": args.tolerance}
    report = harness.check(selected, **tol_kwargs)
    for outcome in report.outcomes:
        mark = {
            "pass": "PASS",
            "fail": "FAIL",
            "missing": "MISS",
            "error": "ERR ",
        }[outcome.status]
        print(f"  [{mark}] {outcome.case_id}")
        if outcome.status == "fail" and outcome.result is not None:
            first = outcome.result.first
            n = len(outcome.result.divergences)
            print(f"         first of {n} divergence(s):")
            for line in str(first).splitlines():
                print(f"         {line}")
        elif outcome.message:
            print(f"         {outcome.message}")
    print()
    passed = sum(1 for o in report.outcomes if o.status == "pass")
    print(f"{passed}/{len(report.outcomes)} passed")
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
