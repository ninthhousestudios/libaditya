# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC
"""YiLongitude / HDLongitude must honour a per-instance gate 1 anchor."""

from dataclasses import replace

from libaditya.hd import constants as hdc
from libaditya.hd.longitude import HDLongitude, YiLongitude
from libaditya.objects.context import EphContext


def test_yilongitude_instance_gate_one_shifts_gate():
    lon = 223.25 + 2.5  # inside gate 1 with the standard anchor
    # YiLongitude has no gate accessors of its own; compare the raw distance
    # from gate 1, which every derived coordinate is computed from
    assert YiLongitude(lon)._distance == 2.5
    shifted = YiLongitude(lon, gate_one=223.25 - 30)
    assert shifted._distance == 32.5
    assert shifted.gate_one == 193.25
    assert YiLongitude.gate_one == hdc.gate_one, "class default must stay untouched"


def test_hdlongitude_uses_context_hd_gate_one():
    ctx = EphContext()
    lon = 223.25 + 2.5
    standard = HDLongitude(lon, ctx).gate_number()
    aditya = HDLongitude(lon, replace(ctx, hd_gate_one=193.25)).gate_number()
    assert standard == hdc.wheel[0]
    assert aditya == hdc.wheel[5]
