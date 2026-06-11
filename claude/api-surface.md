# libaditya API Surface

Generated 2026-04-09 from source at `/home/josh/nhs/soft/astrology/libaditya/libaditya/`

---

## Top-level import

`libaditya/__init__.py` star-imports everything:

```python
from libaditya.objects import *
from libaditya.calc import *
from libaditya.charts import *
from libaditya.hd import *
from libaditya.stars import *
from libaditya.cards import *
from libaditya import constants as const
from libaditya import utils, read, write
from libaditya import print_functions as printf
```

---

## EphContext — configuration dataclass

File: `objects/context.py:33`

```python
@dataclass
class EphContext:
    name: str = ""
    timeJD: JulianDay = JulianDay()
    location: Location = Location()

    # Calculation
    sysflg: int = const.ECL         # ECL / SID / TROP / HELIO / BARY / DRAC
    amsha: int = 1                   # varga divisor; 1 = rashi
    ayanamsa: int = 98               # 98 = Dhruva equatorial; 27 = True Citra; etc.
    hsys: str = "C"                  # house system letter
    circle: Circle = Circle.ADITYA   # ADITYA or ZODIAC
    rashi_temporary_friendships: bool = True
    rashi_aspects: str = "quadrant"  # "quadrant", "element", "conventional"

    # Display
    names_type: str = "mixed"        # "mixed", "eng", "iast", "deva"
    sign_names: str = "adityas"      # "adityas" or "zodiac"
    signize: bool = True
    toround: (bool, int) = (True, 3)
    print_nakshatras: bool = True
    print_outer_planets: bool = True

    # HD
    hd_gate_one: float = hdc.gate_one
    hd_print_hexagrams: bool = False

    # Cards of Truth
    cot_savana_day: bool = True
    cot_planet_order: str = "vedic"  # "vedic" or "solar_system"
```

---

## Chart — primary entry point

File: `charts/chart.py:34` (inherits from `API` mixin at `charts/api.py:21`)

### Construction

```python
Chart(context=EphContext())
```

### Zodiac / system switching (all return new Chart)

```python
chart.aditya(**kwargs) -> Chart
chart.tropical(**kwargs) -> Chart
chart.sidereal(ayanamsa=27, **kwargs) -> Chart
chart.heliocentric(**kwargs) -> Chart
chart.barycentric(**kwargs) -> Chart
chart.draconic(**kwargs) -> Chart
```

### Varga access

```python
chart.rashi(n=None) -> Rashi | Varga   # rashi(); rashi(9) == varga(9)
chart.natal() -> Rashi                  # alias for rashi()
chart.varga(amsha: int) -> Varga        # positive = parivritti; negative = special
chart.saptavargas() -> [Varga]          # [1, -2, -3, 7, 9, -12, 30]
```

Special varga codes: `-2` Hora, `-3` Drekkana, `-4` Chaturthamsha, `-10` Dashamsha, `-100` Dashamsha (even-sign reverse), `-12` Dvadashamsha, `-16` Shodashamsha, `-20` Vimshamsha, `-24` Parashara Chaturvimshamsha, `-240` Siddhamsha, `-27` Bhamsha, `-40` Khavedamsha, `-45` Akshavedamsha, `-60` Shashtyamsha.

### Time manipulation

```python
chart.shift(dir, unit, number, **kwargs) -> Chart   # dir='f'/'b', unit='d'/'days'/etc.
chart.timejd(next_time: float) -> Chart
chart.now() -> Chart
```

### Sub-objects

```python
chart.bodygraph() -> Bodygraph
chart.jaimini() -> Jaimini
chart.tajika() -> Tajika
chart.cot(**kwargs) -> CardsOfTruth
chart.stars(stellarium=False) -> TheStars
chart.ecliptic() -> Ecliptic
```

### API mixin methods

```python
chart.ayanamsa() -> int
chart.ascendant() -> Sign
chart.nakshatra() -> Nakshatra     # Moon's nakshatra
```

---

## Varga — calculation backbone

File: `calc/varga.py:36` (inherits from `Jaimini, API`)

```python
Varga(context, amsha=1)
```

### Core accessors

```python
varga.amsha() -> int
varga.varga_name() -> str           # "Rashi", "Navamsha", etc.
varga.planets() -> Planets
varga.cusps() -> Cusps
varga.signs() -> Signs
varga.lagna() -> Sign               # sign containing Cusp 1
varga.where_is(object: int | str) -> Sign
varga.dignities() -> [str]          # Sun-Saturn natural order
varga.deities() -> [...]            # varga deities for 9 grahas + lagna
```

### Display

```python
str(varga)                           # PrettyTable south-Indian chart grid
repr(varga)                          # header only
varga.mkheader() -> str
varga.rich(which="circular")         # which="south_indian" or "circular"
```

---

## Rashi — the main chart object

File: `calc/rashi.py:113`

Inherits from: `Varga, SWERashi, JaiminiGet, RashiBala, DrawSBC, Hellenistic, Returns, LajjitaadiAvasthas, BaladiAvasthas, JagradadiAvasthas, DeeptadiAvasthas, ShayanadiAvasthas`

```python
Rashi(context, chart)   # chart = parent Chart instance
```

### Core accessors

```python
rashi.planets() -> Planets
rashi.cusps() -> Cusps
rashi.signs() -> Signs
rashi.ecliptic() -> ...
rashi.Master() -> Chart             # parent Chart
rashi.panchanga(**kwargs) -> Panchanga
rashi.house_position(planet: str, hsys=None) -> float
rashi.print_current_vimshottari_dasha(yrlen="saura", levels=5)
```

### Yoga methods

```python
rashi.nabhasa_yogas() -> [NabhasaYoga | AkritiYoga]
rashi.akriti_yogas() -> [AkritiYoga]
rashi.ashraya_yogas() -> [NabhasaYoga]
rashi.dala_yogas() -> [NabhasaYoga]
rashi.sankhya_yogas() -> [NabhasaYoga]
rashi.panchamahapurusha_yogas() -> [MahapurushaYoga]
rashi.solar_yogas() -> [SolarYoga]
rashi.lunar_yogas() -> [LunarYoga]
rashi.jaimini_kemadruma() -> [dict]
```

### Argala

```python
rashi.rashi_argala() -> [[Planet],[Planet],[Planet]]
rashi.argala(sign) -> [[Planet],[Planet],[Planet]]
```

### Avastha display

```python
rashi.avasthas()   # prints all 5 systems
```

### Yoga dataclasses (rashi.py)

```python
@dataclass AkritiYoga:       name, translation, to_move: int, houses: tuple
@dataclass NabhasaYoga:      name, translation, category, to_move: int, condition
@dataclass MahapurushaYoga:  name, translation, planet, present: bool, house: int, dignity: str
@dataclass SolarYoga:        name, planets: list, present: bool
@dataclass LunarYoga:        name, planets: list, present: bool
```

---

## Planets collection

File: `objects/planets.py`

```python
Planets(context=EphContext(), planets_dict=None)
```

### Iteration and access

```python
planets[name: str] -> Planet        # planets["Sun"], planets["Moon"]
for p in planets: ...
planets.items()                     # dict-like items

planets.karakas() -> dict           # Sun-Saturn (7 planets)
planets.grahas() -> dict            # Sun-Ketu (9 planets)
```

### Named convenience accessors

```python
planets.sun() -> Sun
planets.moon() -> Moon
planets.mars() -> Mars
planets.mercury() -> Mercury
planets.jupiter() -> Jupiter
planets.venus() -> Venus
planets.saturn() -> Saturn
planets.rahu() -> Rahu
planets.ketu() -> Ketu
```

### Jaimini

```python
planets.jaimini_karakas() -> [Planet]   # sorted by in-sign longitude, 7 planets
```

### Aspects

```python
planets.parashara_aspects() -> [[float|str]]
    # 7x9 matrix (karakas x grahas)
    # "Y" = conjunction, float = 0-60 strength, "" = no aspect
```

### HD

```python
planets.hd_planets() -> [HDLongitude]
planets.gates(chiron=True) -> [...]
```

### Dignities

```python
planets._dignities(temp_planets=None) -> [str]
```

Planet subclasses: `Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn, Rahu, Ketu, Uranus, Neptune, Pluto, Chiron, Earth`.

---

## Planet object

File: `objects/planets.py:34` (inherits from `CelestialObject, Longitude, PlanetBala`)

### Identity

```python
planet.name() -> str                # "Sun", "Moon (R)" (includes retrograde marker)
planet.identity() -> str            # plain name: "Sun", "Moon"
planet.key() -> str                 # same as identity()
planet.object_type() -> str         # "Planet"
planet.swe_id() -> int
planet.number(system="vedic") -> int
planet.list_index() -> int          # 0=Sun ... 8=Ketu
```

### Position (from Longitude base)

```python
planet.ecliptic_longitude() -> float      # raw 0-360
planet.amsha_longitude() -> float         # longitude in current varga (rounded)
planet.amsha_raw_longitude() -> float     # same, unrounded
planet.longitude() -> str | float         # sign-formatted if signize=True
planet.raw_longitude() -> float           # ecliptic, rounded
planet.sign() -> int                      # 1-12 in current varga
planet.sign_name() -> str
planet.in_sign_longitude() -> str         # DMS string within sign (ecliptic)
planet.real_in_sign_longitude() -> float  # ecliptic_longitude % 30
planet.amsha_in_sign_longitude() -> float # in-sign longitude in current varga
planet.amsha_sign_index() -> int
planet.amsha_index() -> int
planet.ecliptic_index() -> int
planet.ecliptic_sign() -> int
```

### Motion

```python
planet.retrograde() -> bool
planet.retrostr() -> str              # "" or " (R)"
planet.longitude_speed() -> float     # degrees/day
planet.speed() -> float               # alias
planet.latitude_speed() -> float
planet.distance_speed() -> float
planet.daily_motion() -> float
planet.lowest_hourly_speed() -> float
planet.lowest_minutely_speed() -> float
planet.lowest_secondly_speed() -> float
```

### Physical properties

```python
planet.latitude() -> float
planet.distance() -> float
planet.right_ascension() -> float
planet.ra() -> str                    # "HHhMMmSSs"
planet.declination() -> float
planet.dec() -> str                   # "DDdMMmSSs"
planet.equatorial_distance() -> float
planet.altitude() -> float
planet.azimuth() -> float
planet.gender() -> str                # "M", "F", "N"
planet.nature() -> str                # "Benefic", "Malefic", "none"
```

### Dignity

```python
planet.dignity() -> str
    # "EX" (exalted), "DB" (debilitated), "MT" (moolatrikona),
    # "OH" (own house), "GF" (great friend), "F" (friend),
    # "N" (neutral), "E" (enemy), "GE" (great enemy), "" (outer planets)

planet.is_ex() -> bool
planet.is_db() -> bool
planet.is_mt() -> bool
planet.is_oh() -> bool
planet.is_karaka() -> bool          # Sun-Saturn
planet.is_graha() -> bool           # Sun-Ketu
planet.is_outer_planet() -> bool
planet.is_benefic() -> bool
planet.ucca() -> (sign, degrees)    # exaltation point
planet.nica() -> ...                # debilitation point
planet.natural_relationship_from(other: Planet) -> str
planet.combined_relationship() -> str
```

### Aspects

```python
planet.parashara_aspect_to(other: Planet) -> float | str
    # "" = no aspect, "Y" = conjunction, float 0-60 = strength
planet.parashara_aspect_from(other: Planet) -> float | str
```

Mars, Jupiter, Saturn override with their special aspects.

### Nakshatra

```python
planet.nakshatra() -> Nakshatra
planet.nakshatra_name() -> str
```

### Avasthas (set during Rashi init, cached on planet)

```python
planet.lajjitaadi_avasthas() -> dict
planet.lajjitaadi_avasthas_giving() -> dict
planet.lajjitaadi_avasthas_receiving() -> dict
planet.baladi_avastha() -> str       # "Bala","Kumara","Yuva","Vriddha","Mrita"
planet.jagradadi_avastha() -> str    # "Jagrat","Swapna","Sushupti"
planet.deeptadi_avastha() -> str     # "Deepta","Swastha","Mudita","Shanta","Shakta","Peedita","Deena","Vikala","Khala"
planet.shayanadi_avastha() -> str    # one of 12 states
```

### Shadbala (from PlanetBala mixin, `objects/shadbala.py:28`)

```python
# Sthana Bala
planet.ucca_bala() -> float
planet.saptavargaja_bala() -> float
planet.sama_visama_bala() -> float
planet.kendradi_bala() -> float
planet.drekkana_bala() -> float
planet.sthana_bala() -> float         # sum of above

# Dig Bala
planet.dig_bala() -> float
planet.dig_bala_cusp() -> int

# Kala Bala
planet.ayana_bala() -> float
planet.cheshta_bala() -> float
planet.mean_longitude() -> float

# Drig Bala
planet.drig_bala() -> float
```

### Rise/Set (from CelestialObject, `objects/celestial_object.py:25`)

```python
planet.rise(bitflags=swe.BIT_HINDU_RISING, location=None) -> JulianDay
planet.set(bitflags=swe.BIT_HINDU_RISING, location=None) -> JulianDay
planet.rise_trans(bitflags, location=None) -> JulianDay
planet.next_heliacal_rising(atmosphere=(0,0,0,0), observer=(0,0,0,0,0,0))
planet.next_heliacal_setting(atmosphere=(0,0,0,0), observer=(0,0,0,0,0,0))
```

### HD

```python
planet.hd() -> HDLongitude
planet.constellation() -> str        # "n/a" unless set by Stellarium
```

---

## Sign object

File: `objects/signs.py:33` — subclasses `One` through `Twelve`

```python
Sign(number, planets, cusps, context, master)
```

### Identity

```python
sign.sign() -> int            # 1-12
sign.sign_name() -> str
sign.name() -> str             # alias
sign.sign_index() -> int       # 0-11
sign.lord() -> str             # e.g., "Sun" (sign 5)
sign.gender() -> str           # "M" (odd), "F" (even)
sign.modality() -> str         # "Moveable", "Fixed", "Dual"
sign.element() -> str          # "Fire", "Earth", "Air", "Water"
sign.glyph() -> str            # Unicode glyph
```

### Contents

```python
sign.planets() -> [Planet]
sign.cusps() -> [Cusp]
sign.objects() -> [Planet | Cusp]
sign.karakas() -> [Planet]     # Sun-Saturn only
sign.grahas() -> [Planet]      # Sun-Ketu
sign.how_many_objects() -> int
sign.how_many_karakas() -> int
sign.how_many_grahas() -> int
sign.objects_within_one_degree() -> [(obj, obj)]
sign.lajjitaadi_avasthas() -> dict
```

### House position

```python
sign.rashis_from_lagna() -> int       # 1-12, house number
sign.house_type() -> str              # "Angle", "Panaphara", "Apoklima"
```

### Navigation

```python
sign.astrological_signs_forward(n: int) -> int
sign.astrological_signs_backward(n: int) -> int
sign.astrological_signs_apart(other_sign: int) -> int
```

### Sorting

```python
sign.ordered_cusps(reverse=False) -> [Cusp]
sign.ordered_planets(reverse=False) -> [Planet]
sign.ordered_objects(reverse=False) -> [Planet | Cusp]
```

### Display

```python
str(sign)          # formatted object list for chart printing
repr(sign)         # PrettyTable with sign number and objects
sign.richDrawing(header_style, info_style) -> rich.Table
sign.rich()
```

---

## Signs collection

File: `objects/signs.py:483`

```python
Signs(planets=Planets(), cusps=Cusps(), context=EphContext())
```

```python
signs[n: int] -> Sign          # 1-12
for sign in signs: ...
signs.keys()
signs.signs() -> dict          # {1: Sign, ..., 12: Sign}
signs.amsha() -> int

signs.lagna() -> Sign          # sign containing Cusp 1
signs.where_is(object: int | str | Planet | Cusp) -> Sign

signs.get_signs_of(planet: Planet | str) -> [Sign]
signs.most_objects() -> int
```

### Rashi aspects (sign-level)

```python
signs.rashi_aspect_between(sign1, sign2) -> int   # 0=none, 1=s1->s2, 2=s2->s1, 3=both
signs.rashi_aspect_from_to(sign1, sign2) -> int    # 0 or 1
signs.rashi_aspects_given_by(sign) -> [Sign]
signs.rashi_aspects_given_to(sign) -> [Sign]
```

---

## Cusp / Cusps

File: `objects/cusps.py:26` (Cusp), `:106` (Cusps)

### Cusp

```python
Cusp(longitude, amsha, speed, number, context=EphContext())

cusp.name() -> str            # "Cusp N"
cusp.identity() -> str
cusp.number() -> int           # 1-12
cusp.cusp_index() -> int       # 0-11
cusp.speed() -> float
cusp.hourly_motion() -> float
cusp.house_system() -> str     # e.g., "Campanus"
cusp.object_type() -> str      # "Cusp"
cusp.nakshatra() -> Nakshatra
cusp.nakshatra_name() -> str
cusp.table_row() -> list
# Plus all Longitude methods (ecliptic_longitude, sign, etc.)
```

### Cusps collection

```python
Cusps(context=EphContext(), cusps=None)

cusps[n] -> Cusp               # 1-indexed
for cusp in cusps: ...
cusps.armc() -> float          # right ascension of MC
cusps.lagna() -> Cusp          # Cusp 1
cusps.ic() -> Cusp             # Cusp 4
cusps.descendant() -> Cusp     # Cusp 7
cusps.mc() -> Cusp             # Cusp 10
cusps.nakshatras() -> Nakshatras
cusps.closest_cusp(longitude: float | Planet) -> int
cusps.house_system() -> str
```

---

## Longitude base class

File: `objects/longitude.py:27`

```python
longitude.varga(amsha) -> float
longitude.deity() -> str
longitude.signize() -> str                            # "DD:MM:SS SignName"
longitude.amsha_raw_in_sign_longitude() -> float
longitude.amsha_between(a, b) -> bool
longitude.amsha_degrees_apart(other) -> float
longitude.virupas_between(point: float) -> float      # 0-60 virupas
longitude.degrees_apart(other_longitude: float) -> float
longitude.signs_apart(sign_number: int) -> int
```

---

## Avasthas API

File: `calc/avasthas.py`

All five systems are mixins on `Rashi`, computed during `Rashi.__init__()` and cached. Results also stored on each `Planet.attributes`.

### Lajjitaadi (avasthas.py:43)

```python
rashi.lajjitaadi_avasthas() -> dict
    # Keys: planet names (only planets with at least one avastha)
    # Values: {avastha_name: [factor_dicts]}
    # Avastha names: "delighted", "starved", "agitated", "thirsty", "proud", "healthy", "shamed"
    # Factor dict keys: "source", "planet", "strength", "lord", "dignity", "detail"

planet.lajjitaadi_avasthas() -> dict
planet.lajjitaadi_avasthas_giving() -> dict
planet.lajjitaadi_avasthas_receiving() -> dict
```

### Baladi (avasthas.py:215)

```python
rashi.baladi_avasthas() -> dict      # {planet_name: state_str}
planet.baladi_avastha() -> str       # "Bala", "Kumara", "Yuva", "Vriddha", "Mrita"
```

### Jagradadi (avasthas.py:234)

```python
rashi.jagradadi_avasthas() -> dict
planet.jagradadi_avastha() -> str    # "Jagrat", "Swapna", "Sushupti"
```

### Deeptadi (avasthas.py:252)

```python
rashi.deeptadi_avasthas() -> dict
planet.deeptadi_avastha() -> str     # "Deepta", "Swastha", "Mudita", "Shanta",
                                      # "Shakta", "Peedita", "Deena", "Vikala", "Khala"
```

### Shayanadi (avasthas.py:312)

```python
rashi.shayanadi_avasthas() -> dict
planet.shayanadi_avastha() -> str    # 12 states: "Shayana", "Upavesha", "Netrapani",
                                      # "Prakasha", "Gamana", "Agamana", "Sabha", "Agama",
                                      # "Bhojana", "Nrityalipsa", "Kautuka", "Nidra"
```

### Combined

```python
rashi.avasthas()   # prints all 5 systems via printf.print_avasthas()
```

---

## Shadbala (strength) API

File: `objects/shadbala.py`

### Per-planet (PlanetBala mixin, shadbala.py:28)

```python
planet.ucca_bala() -> float           # 0-60
planet.saptavargaja_bala() -> float
planet.sama_visama_bala() -> float
planet.kendradi_bala() -> float
planet.drekkana_bala() -> float       # 0 or 15
planet.sthana_bala() -> float         # sum of above

planet.dig_bala() -> float
planet.dig_bala_cusp() -> int

planet.ayana_bala() -> float
planet.cheshta_bala() -> float
planet.mean_longitude() -> float

planet.drig_bala() -> float           # can be negative
```

### Chart-level (RashiBala mixin, shadbala.py:201)

All return lists in Sun-Saturn (karaka) natural order:

```python
rashi.saptavargaja_balas() -> [float]
rashi.sama_visama_balas() -> [float]
rashi.kendradi_balas() -> [float]
rashi.drekkana_balas() -> [float]
rashi.sthana_balas() -> [float]
rashi.dig_balas() -> [float]
rashi.ayana_balas() -> [float]
rashi.cheshta_balas() -> [float]
rashi.drig_balas() -> [float]
```

---

## Vimshottari Dasha API

File: `calc/vimshottari.py` — module-level functions

```python
calculate_vimshottari_dasha(planet=Moon(), dlevels=1, yrlen=const.dasha_years["saura"])
    # Returns: [[dasha_jd, length_days, [sub_dashas]], ...] + [first_lord_index] + [beginning_age]

current_vimshottari_dasha(planet=Moon(), nowtimeJD=JulianDay(), dlevels=3, yrlen=...)
    # Returns: [lord_index, lord_index, ..., next_starts_JulianDay]
    # lord indices: 0=Ketu, 1=Venus, 2=Sun, 3=Moon, 4=Mars, 5=Rahu, 6=Jupiter, 7=Saturn, 8=Mercury

calculate_specific_period(planet=Moon(), lords=[], yrlen=...) -> (JulianDay, float)
    # lords: e.g., [2, 4, 5] = Sun maha, Mars bhukti, Rahu pratyantar
    # returns (start_jd, duration_days)

period_duration(lords: list, yrlen=...) -> float     # duration in days
next_dasha_lords(lords: list) -> list                # next period at same depth
get_next_lord(lord: int) -> int                      # (lord+1) % 9

# Print functions (side-effect: prints to stdout)
print_vimshottari_dasha(planet=Moon(), dlevels=1, yrlen=365.2422)
print_current_vdasha(context, yrlen, levels)
print_calculated_vimshottari_dasha(dasha: list)
```

### Via Rashi

```python
rashi.print_current_vimshottari_dasha(yrlen="saura", levels=5)
    # yrlen can be: "saura", "savana", "sidereal", "tropical"
```

### Year lengths (`const.dasha_years`)

- `"saura"` -> 365.2422 (default solar year)

---

## Panchanga

File: `calc/panchanga.py`

```python
Panchanga(context)
    # accessed via: rashi.panchanga(**kwargs)
    # str() prints full panchanga + addendum
    # repr() prints basic time and panchanga
```

---

## Human Design module

### HDLongitude

File: `hd/longitude.py`

```python
HDLongitude(ecliptic_longitude: float, context=EphContext())
    # accessed via: planet.hd()
```

### Bodygraph

File: `charts/bodygraph.py:29`

```python
Bodygraph(context)
    # accessed via: chart.bodygraph()

bodygraph.conscious_planets() -> Planets
bodygraph.unconscious_planets() -> Planets     # design (Sun-88 deg before birth)
bodygraph.dream_planets() -> Planets           # Moon-88 deg before birth
bodygraph.planets() -> [HDLongitude]           # conscious + unconscious combined
bodygraph.conscious_gates(chiron=True) -> list
bodygraph.unconscious_gates(chiron=True) -> list
bodygraph.all_gates(chiron=False) -> list
bodygraph.draw_svg(outfile=None)
```

### HD calc functions

File: `hd/calc.py`

```python
unconscious_context(context=EphContext()) -> EphContext   # Sun 88 deg earlier
dream_context(context=EphContext()) -> EphContext         # Moon 88 deg earlier
```

---

## Jaimini API

File: `calc/jaimini.py` (mixin on Varga), `calc/jaimini_get.py` (mixin on Rashi)

```python
# On any Varga (including Rashi):
varga.jaimini_first_strength(kn_rao=False) -> [Sign]
varga.jaimini_third_strength() -> dict

# Jaimini karakas:
planets.jaimini_karakas() -> [Planet]    # 7 planets sorted by in-sign longitude desc

# JaiminiGet mixin on Rashi:
rashi.get(spec) -> ...
rashi.argala(sign) -> [[Planet], [Planet], [Planet]]
rashi.pada() -> Sign                     # Arudha Lagna

# On Chart:
chart.jaimini() -> Jaimini

# Kemadruma:
rashi.jaimini_kemadruma() -> [dict]
    # dict keys: "reference", "sign", "second", "second_malefics",
    #            "eighth", "eighth_malefics", "moon_aspects"
```

---

## Other chart types

### Tajika

File: `charts/tajika.py`

```python
chart.tajika() -> Tajika    # inherits Chart
```

### Returns

File: `calc/returns.py` (mixin on Rashi) — Solar/Lunar return calculations.

### Hellenistic

File: `calc/hellenistic.py:20` (mixin on Rashi)

```python
rashi.profection(year=None) -> Planet    # NOT YET IMPLEMENTED (stub)
```

### DrawSBC

File: `draw/draw_sbc.py` (mixin on Rashi) — SVG South Bhava Chart drawing.

---

## Cards of Truth

File: `cards/cards_of_truth.py`

```python
CardsOfTruth(context, master)
    # accessed via: chart.cot(**kwargs)

cot.birth_spread() -> ...
cot.year_spread() -> ...
cot.day_spread() -> ...
```

---

## Fixed Stars

File: `stars/the_stars.py`

```python
TheStars(context, stellarium=False)
    # accessed via: chart.stars(stellarium=False)
```

---

## Key constants

File: `constants.py`

```python
const.TROP            # tropical sysflg
const.SID             # sidereal sysflg
const.ECL             # ecliptic (default)
const.HELIO           # heliocentric
const.BARY            # barycentric
const.DRAC            # draconic

const.lords           # {1: "Mars", 2: "Venus", ...} sign lords
const.rashi_aspects   # {"quadrant": {...}, "element": {...}, "conventional": {...}}
const.vimshottari_dashas  # [[lord_name, years], ...] 9 entries, 0=Ketu
const.dasha_years     # {"saura": 365.2422, ...}
const.ayanamsa_name(n) -> str
const.sysflgstr(sysflg) -> str
const.mean_longitude_formulas  # {planet_name: callable(t)}
const.names           # nested dict: names_type -> sign_names/planets -> [names]
const.adityas         # sign name list for Aditya circle
const.zodiac          # sign name list for Zodiac circle
```

---

## Utilities

File: `utils.py`

```python
utils.dec2dms(decimal) -> (d, m, s)
utils.dec2dmsstr(decimal) -> str
utils.dec2ymd(decimal_years) -> str
utils.mkheader(obj) -> str
utils.mktab(level) -> str
utils.mksub(level) -> str
utils.mk_dasha_lord(dlist) -> str
utils.sign_degree_to_longitude(sign_degree, context) -> float
utils.odd(n) -> bool
utils.even(n) -> bool
utils.toJD(result, context) -> JulianDay
utils.is_stellarium_id(swe_id) -> bool
utils.set_swe_true_sidereal_ayanamsa()
```

---

## File:line reference summary

| API area | File |
|---|---|
| Chart | `charts/chart.py:34` |
| Chart.API mixin | `charts/api.py:21` |
| Varga | `calc/varga.py:36` |
| Rashi | `calc/rashi.py:113` |
| Yoga dataclasses | `calc/rashi.py:37-110` |
| EphContext | `objects/context.py:33` |
| Planet base class | `objects/planets.py:34` |
| PlanetBala mixin | `objects/shadbala.py:28` |
| RashiBala mixin | `objects/shadbala.py:201` |
| Longitude base | `objects/longitude.py:27` |
| CelestialObject | `objects/celestial_object.py:25` |
| Sign / Signs | `objects/signs.py:33 / 483` |
| Cusp / Cusps | `objects/cusps.py:26 / 106` |
| Avasthas (all 5) | `calc/avasthas.py` |
| Vimshottari | `calc/vimshottari.py` |
| Jaimini mixin | `calc/jaimini.py` |
| JaiminiGet mixin | `calc/jaimini_get.py` |
| Panchanga | `calc/panchanga.py` |
| Hellenistic mixin | `calc/hellenistic.py:20` |
| Returns mixin | `calc/returns.py` |
| Bodygraph | `charts/bodygraph.py:29` |
| HD calc | `hd/calc.py` |
| HD exports | `hd/__init__.py` |
| HDLongitude | `hd/longitude.py` |
| Cards of Truth | `cards/cards_of_truth.py` |
| Fixed Stars | `stars/the_stars.py` |
| Constants | `constants.py` |
| Utils | `utils.py` |
