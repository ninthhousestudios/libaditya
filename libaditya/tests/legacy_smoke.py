# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Ninth House Studios LLC

# tests from libaditya.py

print(
    f"computing ephemeris for {name=}, {placename=}, {month=}, {day=}, {year=}, {timedec=}, {lat=}, {long=}, {utcoffset=}, {timezone=}"
)
print(swe.fixstar(",SgrA*", 2404506))
print(swe.calc_ut(2405061, swe.CHIRON))
print(f"using dictionary: {lang_file=}")

timeJD = JulianDay((year, month, day, timedec), utcoffset, timezone)

print(timeJD)

ayanamsa = 0
sysflg = const.ECL
if args.equatorial:
    sysflg = const.EQU
if args.helios:
    sysflg = const.HELIO
if args.baryos:
    sysflg = const.BARY
if args.sidereal:
    sysflg = const.SID
    ayanamsa = int(args.sidereal)

sun = Planet(swe.SUN, timeJD, sysflg, ayanamsa)
moon = Planet(swe.MOON, timeJD, sysflg, ayanamsa)
rahu = Planet(swe.TRUE_NODE, timeJD, sysflg, ayanamsa)
ketu = Ketu(timeJD, sysflg, ayanamsa)

print(sun)
print(moon)
print(rahu)
print(ketu)
