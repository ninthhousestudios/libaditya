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

"""Freeze / check orchestration and IO for the golden harness.

Fixtures live one-file-per-case under ``fixtures/<case-id>.json`` and are
git-tracked.  A fixture holds ``{schema, meta, snapshot}`` and NOTHING
clock-derived, so it is reproducible forever.  Run-time facts that legitimately
vary (backend identity, ephemeris data release, wall clock) go in the stdout
report, never in a fixture.

This module imports ``libaditya`` (indirectly via ``probes``/``subjects``) and
so must only be imported *after* ``backend.select_backend`` has run.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .canonical import dumps, loads
from .compare import DEFAULT_TOL, CompareResult, compare
from .probes import produce_record
from .subjects import Case, cases

FIXTURE_DIR = Path(__file__).parent / "fixtures"


def fixture_path(case_id: str) -> Path:
    return FIXTURE_DIR / f"{case_id}.json"


# --------------------------------------------------------------------------- #
# provenance (for the report only, never a fixture)
# --------------------------------------------------------------------------- #
def ephemeris_provenance() -> dict[str, Any]:
    """The .se1 header lines that identify the ephemeris data release.

    ``ephe/`` is a git-tracked directory here (not a symlink to untracked data),
    so a data-release swap would show up in git -- but pinning the header in the
    report still makes any drift legible instead of surfacing as an unexplained
    tolerance failure.
    """
    try:
        from libaditya import constants as const

        path = Path(const.ephe_path) / "sepl_18.se1"
        with open(path, "rb") as fh:
            head = fh.read(300)
        lines = head.split(b"\r\n")
        return {
            "file": "sepl_18.se1",
            "header": [ln.decode("latin-1").strip() for ln in lines[:3]],
        }
    except Exception as exc:  # noqa: BLE001 - provenance is best-effort
        return {"error": f"{type(exc).__name__}: {exc}"}


# --------------------------------------------------------------------------- #
# freeze / check
# --------------------------------------------------------------------------- #
@dataclass
class CaseOutcome:
    case_id: str
    status: str  # "pass" | "fail" | "frozen" | "missing" | "error"
    result: CompareResult | None = None
    message: str = ""


@dataclass
class RunReport:
    outcomes: list[CaseOutcome] = field(default_factory=list)

    @property
    def failed(self) -> list[CaseOutcome]:
        return [o for o in self.outcomes if o.status not in ("pass", "frozen")]

    @property
    def ok(self) -> bool:
        return not self.failed


def select_cases(all_cases: list[Case], only: list[str] | None) -> list[Case]:
    if not only:
        return all_cases
    wanted = set(only)
    picked = [c for c in all_cases if c.id in wanted]
    missing = wanted - {c.id for c in picked}
    if missing:
        raise SystemExit(f"unknown case id(s): {sorted(missing)}")
    return picked


def freeze(selected: list[Case]) -> RunReport:
    FIXTURE_DIR.mkdir(parents=True, exist_ok=True)
    report = RunReport()
    for case in selected:
        try:
            record = produce_record(case)
            fixture_path(case.id).write_text(dumps(record), encoding="utf-8")
            report.outcomes.append(CaseOutcome(case.id, "frozen"))
        except Exception as exc:  # noqa: BLE001
            report.outcomes.append(
                CaseOutcome(case.id, "error", message=f"{type(exc).__name__}: {exc}")
            )
    return report


def check(
    selected: list[Case],
    *,
    tol: float = DEFAULT_TOL,
    field_tolerances: list[tuple[str, float]] | None = None,
) -> RunReport:
    report = RunReport()
    for case in selected:
        path = fixture_path(case.id)
        if not path.exists():
            report.outcomes.append(
                CaseOutcome(
                    case.id, "missing", message="no golden fixture; run --update"
                )
            )
            continue
        try:
            candidate = produce_record(case)
        except Exception as exc:  # noqa: BLE001
            report.outcomes.append(
                CaseOutcome(case.id, "error", message=f"{type(exc).__name__}: {exc}")
            )
            continue
        golden = loads(path.read_text(encoding="utf-8"))
        result = compare(golden, candidate, tol=tol, field_tolerances=field_tolerances)
        report.outcomes.append(
            CaseOutcome(case.id, "pass" if result.passed else "fail", result=result)
        )
    return report


def all_cases() -> list[Case]:
    return cases()
