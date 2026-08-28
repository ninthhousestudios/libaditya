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

``libaditya`` binds to the ephemeris engine with a plain ``import swisseph as
swe`` scattered across its modules.  To run the golden harness against a
different implementation (the future ``swisseph_rs`` Rust port) we alias the
chosen module into ``sys.modules['swisseph']`` *before* ``libaditya`` is first
imported, so every one of those imports resolves to the same object.

The golden fixtures are always frozen from ``pyswisseph`` (the reference C
engine).  ``--backend`` chooses the *candidate* that gets compared against that
frozen truth; the golden itself never changes when the backend does.
"""

from __future__ import annotations

import importlib
import os
import sys
from typing import Any

# Logical backend name -> importable module name.  ``pyswisseph`` already
# installs itself as ``swisseph``, so it needs no aliasing.
BACKENDS = {
    "pyswisseph": "swisseph",
    "swisseph_rs": "swisseph_rs",
}

DEFAULT_BACKEND = "pyswisseph"

# The library performs the actual swap early, before it binds `swe`, by reading
# this environment variable in libaditya/__init__.py. The harness runs as
# `python -m libaditya.tests.golden`, which imports libaditya (binding `swe`)
# before any harness code runs, so a non-default backend must be requested via
# this variable in the environment -- not aliased after the fact.
ENV_VAR = "LIBADITYA_SWE_BACKEND"


def select_backend(name: str) -> dict[str, Any]:
    """Verify the requested backend is the one libaditya bound, return provenance.

    ``pyswisseph`` (the default) is always available and needs no environment
    setup.  A non-default backend must already be bound via the ``ENV_VAR``
    environment variable (which libaditya honours before it imports swisseph);
    if it is not, this raises with the exact command to use, rather than
    silently comparing the wrong engine.
    """
    if name not in BACKENDS:
        raise ValueError(f"unknown backend {name!r}; choose one of {sorted(BACKENDS)}")

    module_name = BACKENDS[name]
    env = os.environ.get(ENV_VAR)
    bound = sys.modules.get("swisseph")

    if not _is_imported():
        # Ideal path: libaditya has not bound `swe` yet, so we can alias now.
        if module_name != "swisseph":
            os.environ[ENV_VAR] = module_name
            sys.modules["swisseph"] = _import_backend(name, module_name)
        return provenance(
            name, sys.modules.get("swisseph") or _import_backend(name, "swisseph")
        )

    # libaditya already imported: `swe` is bound. Confirm it is what was asked.
    if _bound_matches(name, module_name, env, bound):
        return provenance(name, bound)

    raise RuntimeError(
        f"backend {name!r} was requested but libaditya bound a different "
        f"ephemeris engine (module={getattr(bound, '__name__', None)!r}, "
        f"{ENV_VAR}={env!r}).\n"
        f"Select it before libaditya is imported, e.g.:\n"
        f"    {ENV_VAR}={module_name} python -m libaditya.tests.golden "
        f"--backend={name}"
    )


def _is_imported() -> bool:
    return "libaditya" in sys.modules


def _bound_matches(name: str, module_name: str, env: str | None, bound: Any) -> bool:
    if name == DEFAULT_BACKEND:
        return env in (None, "", "swisseph", "pyswisseph")
    # a non-default engine either came in via the env var, or is itself
    # installed under the name "swisseph"
    return env == module_name or getattr(bound, "__name__", None) == module_name


def _import_backend(name: str, module_name: str) -> Any:
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            f"backend {name!r} requires the {module_name!r} module, which is "
            f"not installed"
        ) from exc


def provenance(name: str, module: Any) -> dict[str, Any]:
    """Best-effort identity of the bound engine, for the run report."""
    return {
        "backend": name,
        "module": getattr(module, "__name__", None),
        "version": getattr(module, "__version__", None),
        "file": getattr(module, "__file__", None),
    }
