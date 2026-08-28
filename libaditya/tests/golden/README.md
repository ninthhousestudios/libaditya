# Golden-master regression harness

Phase 0 of the pyswisseph → swisseph_rs migration. It freezes the current
C-`pyswisseph` numeric output of `libaditya` as git-tracked fixtures; the whole
migration's definition of done is **"this stays green."** It runs on `master`
with no backend change yet, and is a prerequisite for all later phases.

## Running

> The task-oriented workflow (one-step CI entry, the bless discipline, tolerance
> policy, the migration backend switch) lives in
> [`docs/golden-master-harness.md`](../../../docs/golden-master-harness.md). This
> file is the fixture-internals reference.

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
  D-series plus every special negative-amsha "deity" varga), `panchanga`
  (tithi / karana / yoga / nakshatra / vara plus the four `rise_trans`
  rise/set instants — sunrise, sunset, moonrise, moonset — each frozen as a
  JulianDay so both the boundary jd and its revjul calendar tuple are pinned),
  `vimshottari` (dasha/antardasha boundaries; each period's `start` is the whole
  JulianDay, freezing the boundary jd *and* its revjul calendar tuple to guard
  the julday↔revjul round-trip), `ephemeris` (obliquity), and — as `extra_views`
  on specific cases — `houses_by_system` (every hsys in the full `HOUSE_SYSTEMS`
  set, each with its cusps, `ascmc`/`armc`, the `house_name` casing string, and
  every body's `house_pos`), `ayanamsa_sweep` (the whole Swiss-Ephemeris
  sidereal-mode table plus libaditya's custom codes, frozen at one epoch), and
  `vedic_derived` (the higher-level Vedic layer — `jaimini` chara karakas /
  arudha padas / first- and third-strength rankings; `avasthas`, all five
  Parashara systems per karaka; and `yogas`, the nabhasa / panchamahapurusha /
  solar / lunar sets with each yoga's fired flag and `to_move` metric), and
  `events` (the GM-4 iterative-search layer — `fixed_stars` for a representative
  star sample frozen in both the case frame and the true-sidereal SVP/USER_UT
  path, `eclipses` next/previous solar loc+glob and lunar as raw swe tuples,
  `rise_trans` raw Sun/Moon rise/set/mtransit/itransit incl. `BIT_HINDU_RISING`,
  `heliacal` next evening-first / morning-last for Moon/Mercury/Venus, and
  `mooncross` the next Moon/node crossing — every search seeded from the
  subject's pinned time/location), and `feature_modules` (the GM-5 downstream
  feature layer — `bodygraph`, the Human Design activation set: `conscious`
  (personality), `unconscious` (design), and `dream` bodies, each of the 13
  bodygraph bodies + Chiron frozen as raw ecliptic longitude plus its exact
  gate/line/color/tone/base, together with the `design_time` (88° of solar arc
  before birth) and `dream_time` (88° of lunar arc) instants that the HD ingress
  searches derive; and `cot`, the Cards of Truth surface: the jack/queen/king
  `quadrations`, the `birth_card`, the `birth_spread` / `year_spreads` /
  `day_quadrations` — each a 14-card spread plus its planet→card map and the
  chart-body placements — and `savana_day`, the sunrise-on-the-equator boundary
  instant that dates the birth card via `rise_trans` + `revjul`).

  **HD scope.** `feature_modules.bodygraph` freezes only what libaditya actually
  calculates today — the full *activation* set and the design/dream derivations.
  It deliberately omits defined channels, defined centers, and type / authority
  / profile: libaditya has no calc for those yet (the sole "defined centers"
  logic in the tree, `DrawBodyGraph.get_defined_centers`, is entangled with SVG
  theme mutation, and this task is scoped to the activation set, not the SVG).
  When those calcs are ported in, extend `probe_bodygraph` and re-freeze.

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

The `vedic_derived` view (GM-3) is astrologically meaningful only on a Vedic
chart, so rather than the whole zodiac/system sweep it rides a deliberate
subset: **every subject under both aditya-default and sidereal-Lahiri**. Each
subject therefore has an `aditya` case and a plain `sidereal` (ayanamsa 1) case
carrying the view — the three subjects that previously lacked a plain
sidereal-Lahiri case (`sydney`, `reykjavik`, `yamakoti`) gain one here — so the
panchanga / vimshottari / jaimini / avastha / yoga layer is frozen against two
ayanamsas per chart geometry. (`panchanga` and `vimshottari` themselves stay in
*every* case, since they already were; GM-3 only extended their contents.)

The `events` view (GM-4) is a search layer that depends almost entirely on the
subject's pinned time/location rather than the zodiac/circle config, so it rides
just **one `aditya` case per subject** (`nyc`, `sydney`, `reykjavik`, `equator`,
`yamakoti`) — one freeze per coordinate/era edge is enough, and `reykjavik`'s
high latitude specifically exercises the no-rise / no-event failure paths.
Every call is wrapped so a rejection freezes as a visible `__error__` leaf.
Fixed stars run last within the view because the true-sidereal SVP path mutates
the global swe sidereal mode; the other searches are frame-geometric and seed
their own args, so the probe is order-independent (verified by running the
`events` cases in isolation).

The `feature_modules` view (GM-5) rides the **same one `aditya` case per subject**
as `events`, for the same reason: HD activations are config-independent
(`HDLongitude` is pinned to the tropical ecliptic regardless of circle/ayanamsa)
and Cards of Truth is date + location driven. The Cards spreads and their
planet-into-card placements do read the chart geometry (a body's card is keyed
by its sign lord), so that single freeze rides the aditya geometry; a second
geometry is not worth the repeated solar-return search cost. Year spreads and day
quadrations are frozen for a small fixed set of ages/day-offsets (0 and 1) so the
solar-return / forward-day searches are exercised without the run cost of a long
sweep, and every derived-instant search is wrapped in `capture`.

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
- GM-1 froze the core; GM-2 extended it to the full zodiac/system config sweep,
  the whole varga set, the complete house-system table (`house_name` + every
  body's `house_pos`), and the ayanamsa-code sweep. GM-3 adds the derived Vedic
  layer — panchanga rise/set instants, vimshottari boundary calendar tuples, and
  the `vedic_derived` view (jaimini, avasthas, rashi yogas) — plus a plain
  sidereal-Lahiri case for each remaining subject. GM-4 adds the `events` view —
  the iterative-search surface (fixed stars incl. the true-sidereal SVP path,
  eclipses, rise/trans, heliacal, mooncross), the part of the migration most
  likely to move (swisseph_rs changes these functions' return types and raises
  `NoConvergence` on crossings), rode on one aditya case per subject so every
  coordinate/era edge is covered. GM-5 adds the `feature_modules` view — the
  self-contained downstream features (Human Design bodygraph activations + their
  88°-arc design/dream searches, and the Cards of Truth quadrations / spreads /
  savana-day boundary) — on the same one-aditya-case-per-subject footing.
- GM-5 froze only the HD calcs that exist today (the activation set + design/
  dream derivations). Defined channels, defined centers, and type / authority /
  profile are **not** frozen because libaditya does not calculate them yet — they
  live only inside the SVG drawing mixin (`DrawBodyGraph.get_defined_centers`,
  theme-coupled). When those calcs land (they are being ported from another
  project), extend `probe_bodygraph`, add their fixtures, and re-freeze; the new
  leaves will diff cleanly against a backend swap like everything else.
- GM-6 is the Phase-0 gate: it froze the full GM-2..GM-5 fixture set against
  `pyswisseph` on `master` (baseline **24/24 PASS**, a clean re-freeze diffs to
  nothing), wired the one-step suite entry `python -m libaditya.tests` (offline
  smoke + golden check, single exit code), and moved the run/bless/tolerance/
  backend-switch **workflow** into the living doc
  [`docs/golden-master-harness.md`](../../../docs/golden-master-harness.md).
  This README stays the fixture-internals reference. The per-field tolerance
  mechanism (`compare(..., field_tolerances=...)`) already exists here for a
  later phase to loosen an individual noisy field without raising the global bar.
