# CLAUDE.md - libaditya

## What is this?

libaditya is a Python 3.13+ astrological calculation library built on top of the Swiss Ephemeris (pyswisseph). It supports tropical, sidereal (46+ ayanamsas), and "Aditya Circle" zodiacs. It covers Vedic astrology (Jaimini, Panchanga, Vimshottari Dashas, Shadbala), Human Design (bodygraph SVG generation), Cards of Truth, fixed stars, and Sarvatobhadra Chakra drawing.

Licensed AGPL v3+. Published on PyPI as `libaditya`. Hosted on GitLab.

## Project structure

```
libaditya/
  objects/       # Core data objects: EphContext, Planet, Sign, Cusp, Nakshatra, Longitude, JulianDay, Location
  calc/          # Calculation modules: Rashi, Varga, Jaimini, Panchanga, Vimshottari, Hellenistic, Returns
  charts/        # High-level chart interfaces: Chart (main entry point), Bodygraph, Jaimini, Tajika
  cards/         # Cards of Truth system: birth/year/day spreads, quadrations
  hd/            # Human Design: gate/line/channel calculations
  draw/          # SVG drawing: bodygraph, Sarvatobhadra Chakra, themes/
  stars/         # Fixed star catalog (~8000+ stars), Stellarium integration
  ephe/          # Swiss Ephemeris data files (~37 MB)
  constants.py   # All constants, mappings, ayanamsa definitions (~1600 lines)
  utils.py       # DMS conversion, date parsing, signization, dignity helpers
  read.py        # File I/O: TOML charts, Kala .chtk parsing
  write.py       # Interactive chart creation (TOML output)
  print_functions.py  # Terminal output formatting (PrettyTable, Rich)
```

## Build and dev setup

```bash
uv venv && source .venv/bin/activate && uv add . --dev
```

Build system: Hatchling. Package manager: uv.

## Dependencies

pyswisseph, drawsvg, metar, more-itertools, prettytable, requests, rich, toml

## Usage pattern

```python
from libaditya import *

chart = Chart()                    # current time, default location (Yamakoti)
chart.tropical()                   # switch to tropical
chart.sidereal(ayanamsa=27)        # switch to sidereal
chart.rashi()                      # D1 chart
chart.varga(9)                     # Navamsha
chart.rashi().panchanga()          # Panchanga
chart.rashi().panchanga().vimshottari_dasha()
chart.bodygraph().draw_svg()       # Human Design SVG
chart.cot().birth_spread()         # Cards of Truth
```

All objects are chainable. Most things work with zero arguments via sensible defaults.

## Key design principles

- Calculations should be transparent and understandable to astrologers
- Chainable API with sensible defaults (everything works with no arguments)
- Multiple output representations: `__str__`, `__repr__`, `.rich()`
- EphContext is the immutable configuration dataclass (time, location, calc options)
- Chart is the main entry point; wraps EphContext

## Conventions

- `uv` for package management, not pip
- TOML for chart data files
- Rich for terminal formatting
- drawsvg for SVG generation
- Constants go in `constants.py`
- Printing/formatting logic goes in `print_functions.py`, not in the objects themselves

## Testing

Basic tests in `libaditya/tests.py`. Example TOML charts in `libaditya/toml-test/`.

## Calculations added by Claude

The following calculations were implemented by Claude (Opus):

**`calc/vimshottari.py`** (non-recursive helpers):

- **`period_duration(lords)`** — computes the duration in days of any vimshottari period given a list of lord indices (maha, bhukti, pratyantar, …) without traversing the full dasha tree
- **`calculate_specific_period(planet, lords)`** — returns `(start_jd, duration_days)` for any specific period identified by lord indices, walking only the requested path rather than recursively expanding all levels

**`calc/rashi.py`**:

- **Avasthas** — all five primary Parashara avastha systems in `calc/avasthas.py`: Lajjitaadi, Baladi, Jagradadi, Deeptadi, Shayanadi
- **Nabhasa Yogas** — all 32 yogas across 4 subcategories, each with a `to_move` metric showing how many karakas would need to move to perfect the yoga:
  - `ashraya_yogas()` — Rajju, Musala, Nala (modality-based)
  - `dala_yogas()` — Mala, Sarpa (benefic/malefic in kendras)
  - `sankhya_yogas()` — Gola through Veena (1–7 occupied houses)
  - `akriti_yogas()` — 20 shape yogas (pre-existing, extended)
  - `nabhasa_yogas()` — combined view of all 32
- **Panchamahapurusha Yogas** — `panchamahapurusha_yogas()`: Ruchaka, Bhadra, Hamsa, Malavya, Sasa (Mars/Mercury/Jupiter/Venus/Saturn in angle + own/exaltation)
- **Solar Yogas** — `solar_yogas()`: Vosi, Vesi, Ubhayachari (starry planets in 12th/2nd from Sun)
- **Lunar Yogas** — `lunar_yogas()`: Anapha, Sunapha, Durudhara, Kemadruma (planets in 12th/2nd from Moon)

Each has corresponding `print_` and `rich_` display functions in `print_functions.py`.

- **Jaimini Kemadruma Yoga** — `jaimini_kemadruma()`: checks from lagna, AK in D1, pada, and svamsha (AK in D9) for equal malefics in 2nd and 8th with no benefics (1.2.119). Applies odd/even direction rule. Reports Moon aspecting for severity (1.2.120).

**`calc/jaimini.py`**:

- **First Source of Strength** — `jaimini_first_strength(kn_rao=False)`: ranks all 12 signs by 8 tiebreaker levels (planet count, dignity, modality, lord's rashi planet count, lord's rashi dignity, lord's rashi modality, distance to lord, final tiebreaker). Refactored by Claude to use `_compare_strength()` comparator with `cmp_to_key`. Supports KN Rao tiebreaker mode.
- **Third Source of Strength** — `jaimini_third_strength()`: classifies each sign as Kendra/Panapara/Apoklima based on distance from sign to its lord (distance % 3).

**`calc/jaimini_get.py`**:

- **`JaiminiGet.get(spec)`** — general method to compute Jaimini sign influences (conjunctions and rashi aspects) for any topic. Takes a declarative spec from the `Gets` class that defines the factor (karaka + offset, or cusp number) and which vargas to check. Handles odd/even sign direction counting automatically. Supports varga variant overrides (e.g. Siddhamsha vs standard D24). Returns nested dict keyed by factor then varga. See `calc/jaimini-get-arch.md` for full architecture.
- **`Gets`** — declarative registry of Jaimini topic specs: karakamshas, spirituality, mundane_deity, home, dharma, farmer, spouse, might, conjurer. Each is a dict with `factor` (sign identification strings) and `vargas` (divisional chart priority list).

## Active work areas

See `todo.md` for the full roadmap. Key areas: Cards of Truth subperiod timing, fixed star catalog improvements, SBC drawing completion, vara (weekday) calculations, Jaimini first strength edge cases.
