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

"""Swiss-Ephemeris backend selection.

Historical: during the pyswisseph -> swisseph_rs migration this module aliased a
chosen engine into ``sys.modules['swisseph']`` before ``libaditya`` was first
imported, so the harness could compare a *candidate* engine against the C
pyswisseph reference. Phase 3 (libaditya/4) dropped pyswisseph: ``libaditya``'s
ephemeris seam imports ``swisseph_rs`` directly, so there is no ``import
swisseph`` left to alias and only one engine to run. ``--backend`` survives as a
single-choice knob (``swisseph_rs``) purely so the run report can name the
engine and its provenance; the golden fixtures remain the frozen regression
truth.
"""

from __future__ import annotations

import importlib
from typing import Any

# Logical backend name -> importable module name. swisseph_rs is now the sole
# ephemeris engine; the seam imports it directly, so no sys.modules aliasing is
# needed anymore.
BACKENDS = {
    "swisseph_rs": "swisseph_rs",
}

DEFAULT_BACKEND = "swisseph_rs"


def select_backend(name: str) -> dict[str, Any]:
    """Confirm the requested engine is installed and return its provenance.

    Post-migration there is exactly one engine (``swisseph_rs``), imported
    directly by the seam, so this no longer swaps ``sys.modules`` or races
    libaditya's import -- it just validates the name and reports what will run.
    """
    if name not in BACKENDS:
        raise ValueError(f"unknown backend {name!r}; choose one of {sorted(BACKENDS)}")

    module_name = BACKENDS[name]
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            f"backend {name!r} requires the {module_name!r} module, which is "
            f"not installed"
        ) from exc
    return provenance(name, module)


def provenance(name: str, module: Any) -> dict[str, Any]:
    """Best-effort identity of the bound engine, for the run report."""
    return {
        "backend": name,
        "module": getattr(module, "__name__", None),
        "version": getattr(module, "__version__", None),
        "file": getattr(module, "__file__", None),
    }
