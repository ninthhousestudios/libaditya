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

"""Diff engine: compare a freshly computed canonical record against its golden.

Numeric leaves compare within an absolute tolerance (default ``1e-9`` -- tight,
per the arc's exact-freeze decision); every other leaf compares exactly.
Structural mismatches (missing/extra keys, length or type changes) are
divergences too.  Traversal is deterministic (sorted dict keys, list order), so
"the first divergence" is well defined and stable.

Per-field tolerances override the default for matching paths: a list of
``(glob, tol)`` where ``glob`` is matched with ``fnmatch`` against the dotted
path (e.g. ``snapshot.panchanga.vara`` or ``snapshot.rashi.cusps[0].daily_speed``).
The first matching glob wins.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fnmatch import fnmatchcase
from typing import Any

from .canonical import FLOAT_TAG

DEFAULT_TOL = 1e-9


@dataclass
class Divergence:
    path: str
    golden: Any
    candidate: Any
    detail: str

    def __str__(self) -> str:
        return f"{self.path}: {self.detail}\n    golden    = {self.golden!r}\n    candidate = {self.candidate!r}"


@dataclass
class CompareResult:
    passed: bool
    divergences: list[Divergence] = field(default_factory=list)

    @property
    def first(self) -> Divergence | None:
        return self.divergences[0] if self.divergences else None


def _is_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _is_tagged_float(x: Any) -> bool:
    return isinstance(x, dict) and set(x.keys()) == {FLOAT_TAG}


def tolerance_for(
    path: str, default: float, overrides: list[tuple[str, float]]
) -> float:
    for glob, tol in overrides:
        if fnmatchcase(path, glob):
            return tol
    return default


def compare(
    golden: Any,
    candidate: Any,
    *,
    tol: float = DEFAULT_TOL,
    field_tolerances: list[tuple[str, float]] | None = None,
) -> CompareResult:
    overrides = field_tolerances or []
    divergences: list[Divergence] = []
    _walk(golden, candidate, "", tol, overrides, divergences)
    return CompareResult(passed=not divergences, divergences=divergences)


def _walk(g, c, path, tol, overrides, out: list) -> None:
    # numeric leaves: absolute-tolerance comparison
    if _is_number(g) and _is_number(c):
        field_tol = tolerance_for(path, tol, overrides)
        delta = abs(float(g) - float(c))
        if delta > field_tol:
            out.append(
                Divergence(
                    path or "<root>", g, c, f"|delta|={delta:.3e} > tol={field_tol:.3e}"
                )
            )
        return

    # tagged non-finite floats compare exactly (same tag)
    if _is_tagged_float(g) or _is_tagged_float(c):
        if g != c:
            out.append(Divergence(path or "<root>", g, c, "non-finite float mismatch"))
        return

    # type mismatch
    if type(g) is not type(c) and not (_is_number(g) and _is_number(c)):
        out.append(
            Divergence(
                path or "<root>", g, c, f"type {type(g).__name__} != {type(c).__name__}"
            )
        )
        return

    if isinstance(g, dict):
        gk, ck = set(g.keys()), set(c.keys())
        for key in sorted(gk - ck):
            out.append(
                Divergence(_join(path, key), g.get(key), None, "missing in candidate")
            )
        for key in sorted(ck - gk):
            out.append(
                Divergence(_join(path, key), None, c.get(key), "extra in candidate")
            )
        for key in sorted(gk & ck):
            _walk(g[key], c[key], _join(path, key), tol, overrides, out)
        return

    if isinstance(g, list):
        if len(g) != len(c):
            out.append(
                Divergence(path or "<root>", g, c, f"length {len(g)} != {len(c)}")
            )
            return
        for i, (gi, ci) in enumerate(zip(g, c)):
            _walk(gi, ci, f"{path}[{i}]", tol, overrides, out)
        return

    # scalars (str / bool / None): exact
    if g != c:
        out.append(Divergence(path or "<root>", g, c, "value mismatch"))


def _join(path: str, key: str) -> str:
    return f"{path}.{key}" if path else key
