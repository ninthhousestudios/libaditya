# jaimini_get.py — Architecture

## What this does

In Jaimini astrology, interpretation often starts from a specific sign — usually derived from a karaka (significator) placement — and then asks: **what planets influence that sign?** Influence means conjunction (planets in the sign) and rashi aspects (planets in signs that aspect it).

The question varies by topic:

- **Spirituality**: what influences the 12th sign from the Atmakaraka?
- **Spouse**: what influences the 7th sign from the Atmakaraka?
- **Home**: what influences the 4th sign from the Atmakaraka?
- **Karakamshas**: what influences the sign the Atmakaraka itself sits in?
- **Farmer**: what influences the 3rd, 6th, and 9th house cusps?

Each of these is the same operation with different inputs. `jaimini_get.py` encodes those inputs declaratively and provides one general method to compute them all.

## Gets: the declarative specs

The `Gets` class holds topic definitions as class-level dicts. Each has two keys:

- **`factor`**: a list of strings identifying which sign(s) to examine
- **`vargas`**: a list of divisional chart numbers to check, in priority order

### Factor string format

Three shapes:

| Format | Example | Meaning |
|---|---|---|
| `"N away XK"` | `"12 away AK"` | Count N signs from karaka XK. Direction depends on odd/even: odd sign = forward, even sign = backward. |
| `"XK"` | `"AK"` | The sign the karaka occupies (no counting). |
| `"N"` | `"3"` | The sign of the Nth house cusp (no karaka involved). |

Karaka abbreviations map to `jaimini_karakas()` return order:

```
0: AK    (Atmakaraka)
1: AmK   (Amatyakaraka)
2: BK    (Bhratrukaraka)
3: MK    (Matrukaraka / Putrakaraka)
4: PiK   (Pitrkaraka)
5: GK    (Gnatikaraka)
6: DK    (Darakaraka)
```

### Varga overrides

Some vargas have variants. The D24 (Chaturvimsamsha) has a standard version and the Siddhamsha (`-240`), where even signs start from Cancer in reverse. The `get()` method accepts `varga_overrides` to swap variants. Default: `{"24": "-240"}`.

## JaiminiGet.get(): the general method

`get(spec, varga_overrides=None)` does the following:

1. Resolves varga numbers through overrides
2. Gets the jaimini karaka list once
3. For each factor in the spec:
   - For each varga:
     - Finds the target sign (karaka placement + offset with direction, or cusp sign)
     - Collects conjunctions and rashi aspects to that sign
4. Returns a nested dict keyed by factor, then by varga

### Return structure

```python
{
    "aspect_type": "quadrant",       # which rashi aspect system is in use
    "12 away AK": {                  # one key per factor
        "9": {                       # one key per varga
            "conjunction": [         # flat list of planet info strings
                "Mercury,Benefic,Mercury,OH"
            ],
            "aspecting": [           # list of lists, grouped by aspecting sign
                ["Sun,Malefic,Venus,DB", "Mars,Malefic,Venus,F"],
                ["Saturn,Malefic,Saturn,OH"]
            ]
        },
        "-240": { ... },
        "1": { ... }
    }
}
```

Planet info strings come from `Planet.jaimini_info()`: `name,nature,lord,dignity`.

Aspecting is a list of lists because multiple signs can aspect the target — each inner list contains the planets from one aspecting sign, so the astrologer can see which planets aspect together from the same place.

## Why it's built this way

The alternative was one function per topic (like the original `get_spiritual_planets()`). That would mean ~10 nearly identical functions differing only in which karaka, which offset, and which vargas. The declarative approach means:

- Adding a new topic is one dict in `Gets`, no new code
- The counting logic (odd/even direction, karaka lookup, cusp resolution) is tested once
- The output format is consistent across all topics, which makes downstream formatting and TOML export uniform

`get_spiritual_planets()` is kept as a thin wrapper for backward compatibility.
