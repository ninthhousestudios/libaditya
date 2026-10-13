# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC

#    This file is part of libaditya.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
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

"""Human Design bodygraph definition: defined channels and defined centers.

Pure functions over a set of activated gate numbers.  Given the gates a
bodygraph activates (personality + design, Chiron excluded -- it activates no
gate), these derive which of the 36 channels are complete and, from those, which
of the 9 centers are defined.  The topology lives in ``hd.constants``
(``channels`` / ``centers``); this module only applies it.

This is the calc the SVG draw layer consumes (see
``draw.draw_bodygraph.DrawBodyGraph.get_defined_centers``) rather than
re-deriving centers inline; it is also what ``charts.bodygraph.Bodygraph``
exposes as ``defined_channels()`` / ``defined_centers()``.

Deliberately NOT implemented here: HD type, authority, and profile.  Those are
derivable from the channels / centers / gates this library already computes, but
are out of scope for libaditya by design.
"""

from __future__ import annotations

from collections.abc import Iterable

from libaditya.hd import constants as hdc


def gate_numbers(gates: Iterable) -> set[int]:
    """Normalise activations to a set of integer gate numbers.

    Accepts whatever the bodygraph hands over: plain gate numbers (``int``) or
    ``gate.line`` activations (``float``/``str`` like ``30.1``); the line and
    anything after the decimal point is irrelevant to channel/center definition.
    """
    return {int(str(gate).split(".")[0]) for gate in gates}


def defined_channels(gates: Iterable) -> list[tuple[int, int]]:
    """Channels activated by ``gates``, as sorted ``(low_gate, high_gate)`` pairs.

    A channel is activated only when BOTH of its gates are present.
    """
    active = gate_numbers(gates)
    return sorted(
        pair for pair in hdc.channels if pair[0] in active and pair[1] in active
    )


def defined_centers(gates: Iterable) -> dict[str, bool]:
    """Map every one of the 9 centers to whether it is defined by ``gates``.

    A center is defined when at least one defined channel touches it.  All nine
    centers are always present in the result (keyed in ``hdc.centers`` order),
    ``False`` for undefined -- so callers never have to guess an absent key.
    """
    defined = {center: False for center in hdc.centers}
    for pair in defined_channels(gates):
        first, second = hdc.channels[pair]
        defined[first] = True
        defined[second] = True
    return defined
