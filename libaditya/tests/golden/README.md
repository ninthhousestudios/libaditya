# Golden-master regression harness

Phase 0 of the pyswisseph → swisseph_rs migration. It freezes the current
C-`pyswisseph` numeric output of `libaditya` as git-tracked fixtures; the whole
migration's definition of done is **"this stays green."** It runs on `master`
with no backend change yet, and is a prerequisite for all later phases.

## Running

Use the project venv (Python 3.13; the harness needs `libaditya` importable):

```bash
# check the current engine against the frozen goldens (the normal case)
.venv/bin/python -m libaditya.tests.golden

# (re)freeze the goldens from pyswisseph after a *blessed* change
.venv/bin/python -m libaditya.tests.golden --update

# a subset of cases, or a looser tolerance, or just list the matrix
.venv/bin/python -m libaditya.tests.golden --case nyc-aditya --case sydney-aditya
.venv/bin/python -m libaditya.tests.golden --tolerance 1e-7
.venv/bin/python -m libaditya.tests.golden --list
```

Exit code is `0` when every selected case passes, `1` otherwise (suitable for
CI). Intended output changes are consciously re-blessed with `--update`; the
diff of the fixture files under review is the record of what moved.

## Choosing a backend

The golden fixtures are **always** frozen from `pyswisseph` (the reference C
engine). `--backend` chooses the *candidate* that gets compared against that
frozen truth — the golden itself never changes when the backend does.

`libaditya` binds the engine with `import swisseph as swe` at import time, so a
non-default engine must be selected **before** `libaditya` is imported. The
library reads the `LIBADITYA_SWE_BACKEND` environment variable at the very top
of `libaditya/__init__.py` and, if set to an API-compatible module name, aliases
it in as `swisseph`. Because `python -m libaditya.tests.golden` imports
`libaditya` before any harness code runs, request an alternate backend like:

```bash
LIBADITYA_SWE_BACKEND=swisseph_rs \
  .venv/bin/python -m libaditya.tests.golden --backend=swisseph_rs
```

`--backend=pyswisseph` (the default) needs no environment setup. If `--backend`
names an engine the library did not actually bind, the harness fails loudly with
the exact command to use rather than silently comparing the wrong engine.

## Fixture layout

```
libaditya/tests/golden/
  __main__.py     entry point (python -m libaditya.tests.golden)
  backend.py      engine selection / provenance
  subjects.py     pinned subjects + the case matrix
  probes.py       walks a computed Chart, emits raw numeric/categorical leaves
  canonical.py    deterministic canonical serializer (domain-agnostic)
  compare.py      per-field-tolerance diff engine, first divergence
  harness.py      freeze / check orchestration + IO
  fixtures/
    <case-id>.json   one frozen golden per case, git-tracked
```

Each fixture is `{schema, meta, snapshot}`:

- `meta` echoes the case inputs (subject id, config, and the resolved
  `EphContext`: julian day, location, ayanamsa, sysflg, circle, hsys) so a
  fixture is self-describing.
- `snapshot` holds the computed views: `rashi` (all planets' raw positions /
  speeds / RA-dec / nakshatra + pada, the house cusps, `ascmc`/`armc`, lagna),
  `vargas` (a dict keyed by amsha over `VARGA_AMSHAS` — the positive parivritti
  D-series plus every special negative-amsha "deity" varga), `panchanga`,
  `vimshottari`, `ephemeris` (obliquity), and — as `extra_views` on specific
  cases — `houses_by_system` (every hsys in the full `HOUSE_SYSTEMS` set, each
  with its cusps, `ascmc`/`armc`, the `house_name` casing string, and every
  body's `house_pos`) and `ayanamsa_sweep` (the whole Swiss-Ephemeris
  sidereal-mode table plus libaditya's custom codes, frozen at one epoch).

A fixture contains **nothing clock-derived**, so it is reproducible forever.
Runtime facts that legitimately vary (backend identity, ephemeris data release,
wall clock) are printed in the report, never written to a fixture.

## Pinned test subjects

Birth data is a fixed `(year, month, day, decimal_hour_UTC)` tuple — never
`.now()` or the library default clock. Longitudes are East-positive (swisseph
convention). The subjects span the coordinate/era edges a backend swap is most
likely to diverge on:

| subject     | when (UTC)        | where                    | why |
|-------------|-------------------|--------------------------|-----|
| `nyc`       | 1990-02-13 22:30  | 40.71 N, 74.01 W         | mid-latitude northern, modern era |
| `sydney`    | 1935-06-21 04:00  | 33.87 S, 151.21 E        | southern hemisphere, older era |
| `reykjavik` | 1975-12-01 09:00  | 64.15 N, 21.94 W         | high latitude — swept over the full house-system set |
| `equator`   | 2000-01-01 12:00  | 0 N, 0 E ("Null Island") | savana-day / equatorial edge |
| `yamakoti`  | 2024-03-20 06:06  | library default location | freezes the zero-argument default code path |

The case matrix (`subjects.cases()`) runs `nyc` through the full zodiac/system
sweep — `aditya` (both `Circle.ADITYA` and, via a `context_overrides` circle
swap, `Circle.ZODIAC`), `tropical`, `heliocentric`, `barycentric`, `draconic`,
`equatorial` (a `sysflg=const.EQU` override), `topocentric` (a
`sysflg=const.TOPO` override), and sidereal across a representative ayanamsa set
(1 Lahiri, 3 Raman, 5 Krishnamurti, 27 True Citra, 36 Gal.Center/Mula, 97
true-sidereal, 98 aditya-default). The remaining subjects cover the other edges:
`sydney` adds the `SID | TOPO` topocentric branch, `reykjavik` carries the full
`houses_by_system` sweep, and `equator` (≈ J2000) carries the `ayanamsa_sweep`.
Configuration knobs the builder methods set for themselves — the raw `sysflg`
and `circle` — are applied *after* the builder via `Chart._new_chart`, since
passing them as keywords would clash with the value the builder already sets.

## Precision & tolerance — why it's tight

The most likely regression from a backend swap is **sub-arcsecond drift**, so a
loose arcsecond tolerance would silently swallow exactly what this harness
exists to catch. Therefore:

- The serializer stores **full double precision** by reading each object's
  **raw instance attributes** (`planet.long`, `planet._declination`,
  `cusps.ascmc` …), *not* the public display accessors. Nearly every accessor in
  `libaditya` rounds — `longitude()`/`speed()`/`latitude()` round to
  `context.toround` (3 dp by default), and `Nakshatra.degrees_elapsed()`,
  `Panchanga.*_degrees_*()` round to a hardcoded 2–3 dp regardless of context.
  Serializing those would throw away the drift class we are hunting for. See the
  header of `probes.py` for the full list of rounding traps that were bypassed.
- Comparison uses a tight absolute tolerance, default `1e-9` (about
  3.6 × 10⁻⁶ arcsec for a degree value). A 1e-8° perturbation trips the diff; a
  1e-11° one does not.
- Per-field tolerances can loosen individual noisy fields when a later phase
  needs it: `compare(..., field_tolerances=[("snapshot.panchanga.vara", 1e-6)])`,
  matched with `fnmatch` against the dotted path, first match wins.

## Determinism guarantees

Output is byte-for-byte identical across runs, machines and `PYTHONHASHSEED`
values (verified against seeds 0/1/1234/random):

- dict keys are stringified and sorted; set/frozenset elements are sorted by
  their own canonical form, so hash-seed iteration order never leaks out;
- floats normalise `-0.0 → 0.0` and tag the non-finite values (`nan`/`inf`) so
  the file stays strict JSON;
- no wall clock, locale, or randomness enters a fixture.

## Notes for the next phase

- `ephe/` is a git-tracked directory here (not a symlink to untracked data), so
  a Swiss-Ephemeris data-release swap would show up in git. The report still
  pins the `sepl_18.se1` header (`SWISSEPH 1 / Copyright Astrodienst AG,
  Switzerland, 1998`) so any drift is legible rather than surfacing as an
  unexplained tolerance failure.
- Anything that can raise (a house system an engine rejects, a broken chart
  path) is frozen as a visible `{"__error__": ...}` leaf, not swallowed — a
  backend that changes an error then trips the diff like any other value.
- GM-1 froze the core; GM-2 extends it to the full zodiac/system config sweep,
  the whole varga set, the complete house-system table (`house_name` + every
  body's `house_pos`), and the ayanamsa-code sweep. GM-3..GM-6 extend the
  remaining view set, subjects, and per-field tolerance policy on top of this
  infrastructure.
