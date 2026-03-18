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

The following calculations in `calc/rashi.py` were implemented by Claude (Opus):

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

## Active work areas

See `todo.md` for the full roadmap. Key areas: Cards of Truth subperiod timing, fixed star catalog improvements, SBC drawing completion, vara (weekday) calculations, Jaimini first strength edge cases.
