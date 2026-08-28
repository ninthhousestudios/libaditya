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

"""Deterministic canonical serializer.

Turns an arbitrary Python value (built by the probe layer) into a canonical,
JSON-serialisable tree whose textual form is byte-for-byte reproducible across
runs, machines and ``PYTHONHASHSEED`` values.  Guarantees:

* dict keys are stringified and sorted; set/frozenset elements are sorted by
  their own canonical form -- so hash-seed iteration order never leaks out;
* floats are stored at FULL double precision (shortest round-tripping repr),
  never the library's display rounding; ``-0.0`` is collapsed to ``0.0`` and
  non-finite values are tagged so the output stays strict JSON;
* no wall-clock, locale or randomness enters the output.

This module is deliberately domain-agnostic.  Domain types (``JulianDay``,
``Location``, ``EphContext``, ``Nakshatra`` ...) are handled by *reducers*
passed in by the probe layer, so ``canonical`` never imports ``libaditya`` and
can be unit-tested on its own.
"""

from __future__ import annotations

import dataclasses
import enum
import json
import math
from collections.abc import Callable
from fractions import Fraction
from types import BuiltinFunctionType, FunctionType, MethodType, ModuleType
from typing import Any

# Tag values for the three non-finite floats.  A tagged float is a one-key
# dict so it survives a JSON round-trip and can never be confused with a real
# numeric leaf (a real leaf is a bare number).
FLOAT_TAG = "__float__"
NAN = "nan"
POS_INF = "inf"
NEG_INF = "-inf"

# Sentinel emitted when a genuine reference cycle is hit on the current path.
CYCLE = "__cycle__"

# Attribute names skipped by the generic object walker.  These are either
# back-references (which form cycles), the shared immutable config (serialised
# once at the top level, not re-embedded in every planet/cusp), or the
# order-dependent lazily-populated ``attributes`` cache.  The probe layer reads
# named raw attributes explicitly and rarely relies on the generic walker, but
# this keeps the walker safe as a fallback.
DEFAULT_SKIP_ATTRS = frozenset(
    {"context", "master", "timeJD", "location", "jd", "attributes"}
)

# A Reducer takes the object and a ``recurse`` callback (already bound to the
# cycle-detection path *including* this object) and returns a plain structure.
Reducer = Callable[[Any, Callable[[Any], Any]], Any]

_CALLABLE_TYPES = (ModuleType, FunctionType, BuiltinFunctionType, MethodType, type)


def _canon_float(x: float) -> Any:
    if math.isnan(x):
        return {FLOAT_TAG: NAN}
    if math.isinf(x):
        return {FLOAT_TAG: POS_INF if x > 0 else NEG_INF}
    if x == 0.0:  # collapse -0.0 -> 0.0 so the sign of zero never causes a diff
        return 0.0
    return x


def _reduce_bytes(b: bytes) -> Any:
    try:
        return b.decode("ascii")
    except UnicodeDecodeError:
        return {"__bytes__": b.hex()}


def _type_name(v: Any) -> str:
    t = v if isinstance(v, type) else type(v)
    return f"{t.__module__}.{t.__qualname__}"


def _sorted_items(mapping):
    return sorted(mapping.items(), key=lambda kv: str(kv[0]))


def canonicalize(
    value: Any,
    *,
    reducers: list[tuple[type, Reducer]] | None = None,
    skip_attrs: frozenset[str] = DEFAULT_SKIP_ATTRS,
    _seen: frozenset[int] | None = None,
) -> Any:
    """Return a canonical JSON-able representation of ``value``.

    ``reducers`` is an ordered list of ``(type, fn)``; the first whose type the
    value is an instance of wins.  ``skip_attrs`` names attributes the generic
    object walker drops.  ``_seen`` carries the ids of objects on the current
    recursion path for cycle detection (internal).
    """
    if reducers is None:
        reducers = []
    if _seen is None:
        _seen = frozenset()

    # --- scalars: cannot form cycles, must not consume the cycle path ---
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, int):  # bool already handled above
        return value
    if isinstance(value, float):
        return _canon_float(value)
    if isinstance(value, str):
        return value
    if isinstance(value, (bytes, bytearray)):
        return _reduce_bytes(bytes(value))
    if isinstance(value, Fraction):  # exact rational -> [num, den]
        return [value.numerator, value.denominator]
    if isinstance(value, enum.Enum):  # member name is stable and legible
        return {"__enum__": f"{type(value).__name__}.{value.name}"}

    # --- everything below is a compound value: guard against cycles ---
    if id(value) in _seen:
        return CYCLE
    child_seen = _seen | {id(value)}

    def recurse(v: Any) -> Any:
        return canonicalize(
            v, reducers=reducers, skip_attrs=skip_attrs, _seen=child_seen
        )

    # domain reducers win over generic container/object handling
    for typ, fn in reducers:
        if isinstance(value, typ):
            return fn(value, recurse)

    if isinstance(value, dict):
        return {str(k): recurse(v) for k, v in _sorted_items(value)}
    if isinstance(value, (list, tuple)):
        return [recurse(v) for v in value]
    if isinstance(value, (set, frozenset)):
        # canonicalise each element, then sort by its stable textual form so
        # the output order is independent of the set's hash-seed iteration.
        elems = [recurse(v) for v in value]
        return sorted(elems, key=lambda e: json.dumps(e, sort_keys=True))
    if isinstance(value, _CALLABLE_TYPES):  # not data
        return {"__opaque__": _type_name(value)}
    if dataclasses.is_dataclass(value):  # instance (type excluded by the guard above)
        return {
            f.name: recurse(getattr(value, f.name))
            for f in sorted(dataclasses.fields(value), key=lambda f: f.name)
        }
    if hasattr(value, "__dict__"):  # generic object: walk vars() with the skip-set
        return {
            k: recurse(v)
            for k, v in _sorted_items(vars(value))
            if k not in skip_attrs and not isinstance(v, _CALLABLE_TYPES)
        }
    return {"__opaque__": _type_name(value)}  # opaque, e.g. a bare C handle


def dumps(canonical: Any) -> str:
    """Serialise a canonical tree to a stable JSON string (with trailing NL).

    ``sort_keys`` is belt-and-suspenders on top of the canonicaliser's own key
    sorting; ``ensure_ascii=False`` keeps IAST/Devanagari names readable in the
    git-tracked fixtures.  ``allow_nan=False`` guarantees strict JSON -- any
    non-finite float must already have been tagged by ``canonicalize``.
    """
    return (
        json.dumps(
            canonical,
            sort_keys=True,
            indent=2,
            ensure_ascii=False,
            allow_nan=False,
        )
        + "\n"
    )


def loads(text: str) -> Any:
    return json.loads(text)
