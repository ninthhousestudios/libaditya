# Golden-master regression harness — workflow

This is the operating guide for the golden-master harness that gates the
`pyswisseph` → `swisseph_rs` migration (Phase 0). It froze the current C-engine
numeric output of `libaditya` as git-tracked fixtures, and the whole migration's
definition of done is one sentence:

> **This stays green.**

Every later phase (the `EphContext` distiller, the ephemeris seam, dropping
`pyswisseph`) is only allowed to land if this harness still reports 100% PASS
against the fixtures frozen here on `master`.

For the *internals* — the fixture file layout, the pinned subject matrix, the
canonical serializer's determinism guarantees, and the per-view probe design —
see the reference beside the code: [`libaditya/tests/golden/README.md`](../libaditya/tests/golden/README.md).
This doc is the workflow: how to run it, how to re-bless a fixture, why the
tolerance is what it is, and (historically) how the migration pointed the
candidate at another engine.

All commands assume the project venv (Python 3.13, with `libaditya`
importable):

```bash
source .venv/bin/activate      # or prefix each command with .venv/bin/
```

## One-step entry (CI / a human gating a change)

Run the whole regression surface — the offline smoke test *and* the
golden-master check — in a single command:

```bash
python -m libaditya.tests
```

It runs the smoke test (`libaditya.tests.legacy_smoke`, a fast shape/sanity
check of the public API) followed by the golden check on `swisseph_rs`
(libaditya's sole ephemeris engine), and exits `0` only if both pass. This is
the command to wire into CI or run before a commit.

## Running the golden check directly

When you want a subset, a different tolerance, or the case list, drive the
golden harness itself:

```bash
# check the current engine against the frozen goldens (the normal case)
python -m libaditya.tests.golden

# just the cases you touched (repeatable)
python -m libaditya.tests.golden --case nyc-aditya --case sydney-aditya

# list the full case matrix (and which extra views each case carries) and exit
python -m libaditya.tests.golden --list

# loosen the numeric tolerance for a one-off run (does not change the default)
python -m libaditya.tests.golden --tolerance 1e-7

# see every flag
python -m libaditya.tests.golden --help
```

Exit code is `0` when every selected case passes, `1` otherwise. On a failure
the report prints the **first divergence** for each failing case — the dotted
path, the golden value, the candidate value, and the delta — which is enough to
tell a real regression from an intended change.

The report header also pins the run-time provenance that never enters a fixture:
the bound backend (module + version), the ephemeris data release (the
`sepl_18.se1` header lines), and the number of cases selected. If a later run
drifts, that header makes *why* legible instead of surfacing as an unexplained
tolerance failure.

## Regenerating / blessing fixtures

The fixtures are the frozen truth; you only rewrite them when a change to
`libaditya` **intentionally** moves the numbers, and only after that change has
been reviewed and blessed.

```bash
# re-freeze every case from the current engine
python -m libaditya.tests.golden --update

# re-freeze only the cases a blessed change actually moved
python -m libaditya.tests.golden --update --case nyc-aditya
```

`--bless` is an alias for `--update`. The discipline:

1. Make the code change.
2. Run the check. If it fails, decide whether the movement is a **bug** (fix the
   code) or an **intended** output change (proceed).
3. For an intended change, `--update` the affected cases.
4. **Review the fixture diff.** `git diff libaditya/tests/golden/fixtures/` *is*
   the record of exactly what moved and by how much — it belongs in the same
   commit as the code change, and a reviewer reads it as part of the review.

The fixtures were originally frozen from `pyswisseph` 2.10.03 (the C reference)
to gate the migration. Post-migration `swisseph_rs` is the sole engine, so a
`--update` now re-freezes from it — which means you must be doubly sure the
movement is intended, since there is no longer a second engine to cross-check
against.

## Tolerance — why it is tight, and how to loosen one field

The most likely regression from a backend swap is **sub-arcsecond drift**, so a
loose arcsecond tolerance would silently swallow exactly what this harness
exists to catch. Two deliberate choices keep it sharp:

- **The serializer stores full double precision.** It reads each object's raw
  instance attributes (`planet.long`, `cusps.ascmc`, …), *not* the public
  display accessors, nearly all of which round (`longitude()`/`speed()` to
  `context.toround`, panchanga/nakshatra helpers to a hardcoded 2–3 dp).
  Serializing the rounded views would throw away the drift class we are hunting.
- **Comparison uses a tight absolute tolerance, default `1e-9`** (about
  3.6 × 10⁻⁶ arcsec on a degree value). A `1e-8°` perturbation trips the diff;
  a `1e-11°` one does not. Every non-numeric leaf compares **exactly**;
  structural mismatches (missing/extra keys, length or type changes) are
  divergences too.

When a specific field is legitimately noisy under a new engine and blessing the
whole thing would hide real drift elsewhere, loosen **only that field** with a
per-field tolerance rather than raising the global bar. Tolerances are a list of
`(glob, tol)` matched with `fnmatch` against the dotted path, first match wins:

```python
from libaditya.tests.golden import harness

report = harness.check(
    harness.all_cases(),
    field_tolerances=[("snapshot.panchanga.vara", 1e-6)],
)
```

The glob matches paths like `snapshot.panchanga.vara` or
`snapshot.rashi.cusps[0].daily_speed`. Keep the override as narrow as the drift
is real; a per-field loosening is a documented concession, not a blanket
`--tolerance` bump.

## The engine (historical: the migration switch)

`swisseph_rs` is now the **sole** ephemeris engine. `libaditya`'s ephemeris seam
(`libaditya/ephemeris/seam.py`) imports it directly, so there is nothing to swap
and `--backend` is a single-choice knob kept only so the run report can name the
engine and its provenance.

Historically this section documented the migration switch: the fixtures were
frozen once from C `pyswisseph`, and `--backend` / the `LIBADITYA_SWE_BACKEND`
environment variable pointed the *candidate* at `swisseph_rs` (aliased into
`sys.modules['swisseph']` before `libaditya` bound `import swisseph as swe`).
Phase 3 (libaditya/4) dropped `pyswisseph` and removed that machinery; the seam
is the only importer of an ephemeris engine and it imports `swisseph_rs`
unconditionally. The bit-for-bit reference tests (`test_seam.py`,
`test_distiller.py`) that compared the seam against C `pyswisseph` were retired
with it — their equivalence is now baked into the fixtures below.

## Baseline

The baseline: **24 cases, 24/24 PASS**. The fixtures were originally frozen from
`pyswisseph` 2.10.03 (module version `20230604`), ephemeris `sepl_18.se1`
(`SWISSEPH 1 / Copyright Astrodienst AG, Switzerland, 1998`), and `swisseph_rs`
reproduces them (within the documented per-field speed/search tolerances). A
clean check against `swisseph_rs` is 24/24 green; this is the number every
change must preserve.
