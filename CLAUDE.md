# libaditya

Python 3.13+ astrological calculation library built on pyswisseph. Supports tropical, sidereal (46+ ayanamsas), and Aditya Circle zodiacs. Vedic (Jaimini, Panchanga, Vimshottari, Shadbala), Human Design, Cards of Truth, fixed stars, SBC drawing. AGPL v3+. Published on PyPI.

## Project structure

```
libaditya/
  objects/       # EphContext, Planet, Sign, Cusp, Nakshatra, Longitude, JulianDay, Location
  calc/          # Rashi, Varga, Jaimini, Panchanga, Vimshottari, Hellenistic, Returns, Avasthas
  charts/        # Chart (main entry), Bodygraph, Jaimini, Tajika
  cards/         # Cards of Truth: birth/year/day spreads, quadrations
  hd/            # Human Design: gate/line/channel calculations
  draw/          # SVG drawing: bodygraph, SBC, themes/
  stars/         # Fixed star catalog (~8000+ stars)
  ephe/          # Swiss Ephemeris data files (~37 MB)
  constants.py   # All constants, mappings, ayanamsa definitions (~1600 lines)
  utils.py       # DMS conversion, date parsing, signization, dignity helpers
  read.py        # File I/O: TOML charts, Kala .chtk parsing
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
chart.tropical() / chart.sidereal(ayanamsa=27) / chart.aditya()
chart.rashi() / chart.varga(9)
chart.rashi().panchanga().vimshottari_dasha()
chart.bodygraph().draw_svg()       # Human Design
chart.cot().birth_spread()         # Cards of Truth
```

All objects are chainable. Most things work with zero arguments via sensible defaults.

## Key design principles

- Chainable API with sensible defaults
- Multiple output representations: `__str__`, `__repr__`, `.rich()`
- EphContext is the immutable configuration dataclass
- Chart is the main entry point; wraps EphContext
- Calculations should be transparent to astrologers

## Conventions

- `uv` for package management, not pip
- TOML for chart data files
- Rich for terminal formatting
- drawsvg for SVG generation
- Constants go in `constants.py`
- Printing/formatting in `print_functions.py`, not in objects

## Testing

Basic tests in `libaditya/tests.py`. Example TOML charts in `libaditya/toml-test/`.

## Notable APIs

**`calc/jaimini.py`**: `jaimini_first_strength(kn_rao=False)` ranks all 12 signs by 8 tiebreaker levels. Uses `_compare_strength()` comparator with `cmp_to_key`. `jaimini_third_strength()` classifies signs as Kendra/Panapara/Apoklima by distance % 3.

**`calc/jaimini_get.py`**: `JaiminiGet.get(spec)` computes Jaimini sign influences (conjunctions + rashi aspects) for any topic. Takes declarative specs from `Gets` class (factor + vargas). Handles odd/even sign direction. See `calc/jaimini-get-arch.md`.

**`calc/avasthas.py`**: All 5 Parashara avastha systems — Lajjitaadi, Baladi, Jagradadi, Deeptadi, Shayanadi.

**`calc/rashi.py`**: Nabhasa yogas (32 across 4 subcategories), Panchamahapurusha, Solar/Lunar yogas. Each yoga has `to_move` metric. Print/rich display functions in `print_functions.py`.

## Active work

See `todo.md` for roadmap.
