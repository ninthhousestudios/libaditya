# stars/ — fixed star catalog for Swiss Ephemeris

This directory contains `sefstars.txt`, a fixed star data file for the Swiss Ephemeris (`swe_fixstar()` / `swe_fixstar2()`), and `make_swe_stars.py`, the script that generates it from SIMBAD data.

## sefstars.txt format

The stock Swiss Ephemeris `sefstars.txt` stores one data line per star, with the long-form name (e.g., "Alpha Tauri") as the lookup key. To find a star by its traditional name ("Aldebaran") or HIP number, you need to already know the Bayer designation convention.

This file uses a **multi-line format**: each star gets multiple data lines, one per name variant. Every line is a complete, self-contained sefstars.txt record with identical astrometric data:

```
#0# alfTau, Alpha Tauri, Aldebaran, HIP 21421
alfTau,alfTau,ICRS,04,35,55.23907,+16,30,33.4885,63.45,-188.94,54.398,48.94,0.86
Alpha Tauri,alfTau,ICRS,04,35,55.23907,+16,30,33.4885,63.45,-188.94,54.398,48.94,0.86
Aldebaran,alfTau,ICRS,04,35,55.23907,+16,30,33.4885,63.45,-188.94,54.398,48.94,0.86
HIP 21421,alfTau,ICRS,04,35,55.23907,+16,30,33.4885,63.45,-188.94,54.398,48.94,0.86
```

This means `swe_fixstar("Aldebaran")`, `swe_fixstar("alfTau")`, `swe_fixstar("Alpha Tauri")`, and `swe_fixstar("HIP 21421")` all work — no need for the `,nomen` prefix convention.

The `#0#` comment lines group entries visually and serve as an index. Swiss Ephemeris skips all `#` lines.

### backward compatibility

The format is fully backward compatible with any program that reads sefstars.txt. Each line follows the exact field spec. The only cost is file size (~2.6x more data lines than one-per-star) and marginally slower linear scan in `swe_fixstar()`. The hash-based `swe_fixstar2()` is unaffected.

`sefstars_oneper.txt` is the one-line-per-star variant if you need a minimal file.

### field spec

Fields are comma-separated:

```
traditional name, nomenclature name, equinox, RA hours, RA minutes, RA seconds,
Dec degrees, Dec minutes, Dec seconds, PM RA, PM Dec, radial velocity,
parallax, magnitude V
```

- Equinox is always `ICRS`
- Proper motion in 0.001"/year (RA component includes cos(decl) factor)
- Parallax in 0.001"
- Radial velocity in km/s

## make_swe_stars.py

Generates sefstars.txt entries by querying the SIMBAD astronomical database. Handles Bayer, Flamsteed, HIP, Messier, NGC, and HD designations, and expands nomenclature to full Latin genitive form.

### basic usage

```bash
# print entries to stdout
python make_swe_stars.py Sirius Aldebaran "Alpha Ursae Minoris"

# append to sefstars.txt (skips stars already present)
python make_swe_stars.py -o sefstars.txt Vega Canopus

# preview without writing
python make_swe_stars.py --dry-run Betelgeuse

# read star names from a file
python make_swe_stars.py -i my_stars.txt -o sefstars.txt
```

### input file format

One star identifier per line. Blank lines and `#` comments are skipped:

```
# bright navigational stars
Sirius
Canopus
Arcturus
Vega
# Orion belt
HIP 26727
HIP 26311
HIP 25930
```

### verifying entries

Compare existing sefstars.txt entries against current SIMBAD data to check for coordinate drift or data errors:

```bash
python make_swe_stars.py --verify "Alpha Canis Majoris" "Alpha Scorpii" -o sefstars.txt
```

Output shows `OK` for matches, or reports coordinate/magnitude differences.

### options

| Flag | Description |
|------|-------------|
| `-o`, `--output-file` | Append entries to this file instead of stdout |
| `-i`, `--input-file` | Read star names from a file (one per line) |
| `-n`, `--dry-run` | Show what would be generated without writing |
| `--verify NOMEN...` | Compare existing entries against SIMBAD |

### duplicate detection

When `-o` is specified, the script loads existing names from the output file and skips any star name that already has an entry. This prevents duplicate lines when re-running the script or adding stars incrementally.

### star identifier formats

The script accepts any identifier that SIMBAD resolves:

- **Traditional names**: `Sirius`, `Aldebaran`, `Betelgeuse`
- **Bayer designations**: `alfCMa`, `Alpha Canis Majoris`
- **Flamsteed numbers**: `48Lib`, `61Cyg`
- **Catalog numbers**: `HIP 32349`, `HD 48915`, `HR 2491`
- **Messier objects**: `M45`, `M87`
- **NGC objects**: `NGC 7654`

### nomenclature expansion

The script expands short-form nomenclature to full Latin genitive:

| Short | Long |
|-------|------|
| `alfTau` | Alpha Tauri |
| `betPer` | Beta Persei |
| `48Lib` | Librae48 |
| `gam01Sgr` | Gamma Sagittarii 1 |
| `HIP32349` | Hipparcos Catalogue 32349 |

## other files

| File | Description |
|------|-------------|
| `sefstars.txt` | Multi-line format, ~1117 stars, ~2865 data lines |
| `sefstars_oneper.txt` | One line per star, same ~1117 stars |
| `fixed_star.py` | Python class for working with fixed star positions |
| `the_stars.py` | Star lists and groupings |
| `utilities.py` | Helper functions for star calculations |
| `star-sign-boundaries` | Sign boundary data for fixed stars |
