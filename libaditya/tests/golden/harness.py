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

# swisseph_rs and pyswisseph agree bit-for-bit on ecliptic/equatorial POSITIONS
# (long/lat/dist, RA/dec all match to <1e-9; verified libaditya/14), but diverge
# at the engine noise floor in a handful of derived quantities. Every glob applies
# to EVERY case; every bound stays far tighter than any real cutover regression
# (arcseconds+ on a position / minutes+ on a date for a mis-distilled config), so
# they absorb engine noise without hiding bugs:
#
#   *speed*  -- swisseph_rs's SEFLG_SPEED (analytic) velocities land ~1e-8 deg/day
#     off pyswisseph, worst ~2e-8 on Chiron/outers. Its SPEED3 finite-difference
#     path agrees to ~1e-10, but that is a DIFFERENT quantity than the golden
#     froze under SPEED, so no flag makes them match. 1e-7 deg/day is
#     astrologically null (no effect on pada, retrograde, or dignity). Also
#     catches ascmcspeed / cusp daily_speed as later subsystems cut over.
#
#   *.amsha_longitude -- the varga map multiplies the in-sign longitude by the
#     divisor, so D60 (x60) amplifies a ~2e-11 raw-longitude ULP gap into ~1.2e-9
#     (observed max 1.168e-9 on Neptune). Only the highest varga trips the 1e-9
#     default; 5e-9 gives headroom while staying tight for every lower varga.
#
#   NAKSHATRA / YOGA / VIMSHOTTARI (libaditya/17) -- the dhruva-gc-equatorial
#     nakshatra path (the DEFAULT ayanamsa 98) references ashvini off the Galactic
#     Centre fixed star. swisseph_rs exposes only the fixstar2 catalog, whose SgrA*
#     equatorial longitude tracks pyswisseph's swe.fixstar (v1) to ~5e-8 deg -- an
#     engine noise floor, not a distiller error (positions of the bodies themselves
#     still match <1e-9). That offset lands in every dhruva ash_long (~1.2e-7 deg),
#     doubles into the nitya-yoga sum (~2.5e-7), and -- because a nakshatra fraction
#     scales to the multi-year dasha length -- amplifies into the vimshottari period
#     boundaries (~6e-5 JD ~= 5 s over decades; the datetime hour column is that
#     JD x24). Sidereal ash_long (calc_ut path) still matches <1e-9; these globs
#     loosen it too but stay orders tighter than any real regression.
#
#   ECLIPSES (libaditya/19) -- the sol/lun eclipse searches are Newton-iterated to
#     an internal convergence threshold, and swisseph_rs lands the contact instants
#     ~1e-8 JD (~1 ms) off pyswisseph's -- an iterative-search noise floor, the same
#     class as rise_trans / the fixstar SgrA* offset, NOT a distiller error (the
#     retflags and the whole local-circumstance ``attr`` array still match <1e-9).
#     Only the ``tret`` time slots move; 1e-7 gives an order of headroom while
#     staying far tighter than any real regression (a mislocated eclipse moves by
#     minutes/hours, not milliseconds).
#
#   RISE/SET/TRANSIT (libaditya/20) -- swisseph_rs's rise_trans root-find lands
#     ~1.8e-6 JD (~0.15 s) off pyswisseph's, an iterative-search noise floor (the
#     class the eclipse note names) and eph-config-independent (a tropical vs
#     sidereal Ephemeris gives the same instant). It moves the events.rise_trans
#     tret[0] and the panchanga sunrise/sunset/moonrise/moonset jds; the derived
#     datetime hour column is that JD x24 (~4.3e-5 h). mooncross needs NO tolerance
#     -- the seam calls swisseph_rs's true-UT node crossing and the mooncross golden
#     leaf was re-blessed from that corrected value (libaditya/25), so candidate and
#     golden agree bit-for-bit again (the ~delta-T ~8e-4 JD gap is baked into the
#     fixture, not absorbed by a tolerance). pyswisseph's own mooncross_node_ut is
#     buggy -- it returns the ET-frame instant under a _ut name -- so it no longer
#     defines this leaf's truth.
#
#   HELIACAL (libaditya/20) -- the heliacal-visibility search runs its OWN
#     atmospheric root-find, so swisseph_rs lands the window jds ~1.3e-4 JD (~11 s)
#     off pyswisseph's -- the same iterative class, looser because the search is
#     harder (a visibility DATE is what matters; 11 s is null). Positions still
#     match <1e-9. The datetime hour column is that JD x24 (~3.2e-3 h).
GLOBAL_FIELD_TOLERANCES: list[tuple[str, float]] = [
    ("*speed*", 1e-7),
    ("*.amsha_longitude", 5e-9),
    ("*.nakshatra.ashvini_longitude", 1e-6),
    ("*.panchanga.yoga_*", 1e-6),
    ("*.vimshottari.age", 1e-6),
    ("*.vimshottari.periods*start.jd", 5e-4),
    ("*.vimshottari.periods*start.datetime*", 1e-2),
    ("*.events.eclipses.*", 1e-7),
    ("*.events.rise_trans.*", 5e-6),
    ("*.panchanga.*rise.jd", 5e-6),
    ("*.panchanga.*set.jd", 5e-6),
    ("*.panchanga.*rise.datetime*", 1e-4),
    ("*.panchanga.*set.datetime*", 1e-4),
    ("*.events.heliacal.*.jd", 5e-4),
    ("*.events.heliacal.*.datetime*", 1e-2),
]


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
    # Default to the global engine-noise overrides; an explicit [] disables them.
    if field_tolerances is None:
        field_tolerances = GLOBAL_FIELD_TOLERANCES
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
