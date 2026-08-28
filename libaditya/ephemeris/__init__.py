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

"""swisseph_rs ephemeris seam for libaditya (pyswisseph -> swisseph_rs migration).

Two co-located modules, one namespace: :mod:`~libaditya.ephemeris.config` is the
EphContext -> EphemerisConfig distiller; :mod:`~libaditya.ephemeris.seam` is the
native surface (engine wrapper, body/flag ints, name tables, typed errors) every
cutover routes through. Together they are the ONLY importers of ``swisseph_rs``.
"""

from libaditya.ephemeris import seam
from libaditya.ephemeris.config import distill_config
from libaditya.ephemeris.seam import (
    build_ephemeris,
    calc_ut,
    get_ayanamsa_name,
    house_name,
    to_body,
    to_flags,
)

__all__ = [
    "distill_config",
    "seam",
    "build_ephemeris",
    "calc_ut",
    "get_ayanamsa_name",
    "house_name",
    "to_body",
    "to_flags",
]
