# README

```libaditya``` is an astrological calculation library meant to be easily understood in terms
of what calculations are performed and how they are done. it includes a sample program
called ```pyphemeris```.

```pyphemeris``` is meant to serve as an easily readable documentation on how
the library works. Each function in libaditya itself is meant to return the requested
data in a way that can then be presented in some way. Built into most ```libaditya```
classes are functions to represent themselves as text through repr (__repr__) and
```print```, i.e., through ```__str__```. ```pyphemeris``` makes use of these in order
to print the requested data to ```stdout```.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Options](#options)

## Dependencies

python, [pyswisseph](https://pypi.org/project/pyswisseph/), [python-prettytable](https://pypi.org/project/prettytable/)

written with python 3.13

## Installtion

```sh
git clone https://gitlab.com/j0sh4rp3/libaditya
```

if using ```uv``` then:
```
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Usage

then you can run
```
uv run pyphemeris/pyphemeris.py
```

This will print a chart for right now at the time and place specified in
```pyphemeris/defaults.py```. You can change any of the defaults in that file, and then
most options have a flag, some of which are toggles. eventually, there will be
documentation for the options ands for what exactly each does. what it says may not be
100% accurate at the moment

or you can go into the Python ```repl``` using
```python```

then
```
>>> from libaditya import *
>>> dir()
['Chart', 'Chiron', 'Circle', 'Cusp', 'Cusps', 'Earth', 'EphContext', 'Jaimini', 'JulianDay', 'Jupiter', 'Ketu', 'Location', 'Longitude', 'Mars', 'Mercury', 'Moon', 'Nakshatra', 'Nakshatras', 'Names', 'Neptune', 'Panchanga', 'Planet', 'Planets', 'Pluto', 'PrettyTable', 'Rahu', 'Rashi', 'Saturn', 'Self', 'Sign', 'Signs', 'Sun', 'Uranus', 'Varga', 'Venus', 'Yamakoti', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'base_path', 'calc', 'calc_current', 'calc_vdasha', 'calculate_vimshottari_dasha', 'cardinal_points', 'chart', 'charts', 'const', 'constants', 'context', 'current_vimshottari_dasha', 'cusps', 'get_next_lord', 'jaimini', 'julian_day', 'kala', 'length', 'location', 'longitude', 'lord', 'lunar_new_year', 'nakshatras', 'next_dasha_lords', 'objects', 'os', 'panchanga', 'pathlib', 'pd', 'planet_dict', 'planets', 'print_calculated_vimshottari_dasha', 'print_cardinal_points', 'print_functions', 'print_next_dasha_level', 'print_vimshottari_dasha', 'printf', 'read', 'replace', 'signs', 'swe', 'utils', 'vargas', 'vimshottari']
```

you can then use ```help()```, e.g.:
```
>>> help(Chart)
```

and this will print info for Chart. I am trying to add documentation to each of these
classes and function so that there is something helpuful printed. Basically all values
have defaults, so you can also do this
```
>>> c=Chart()
>>> dir(c)
```
to see all of what Chart has and can do.

Most of this is meant to be self explanatory. The one thing I need to document better is
how to input information. It is through EphContext, from libaditya.objects.context. It
takes a JulianDay and a Location, then a bunch of options. All of these have defaults
that should a chart for the current time more or less.

You can read a .chtk file into the repl like this:
```
>>> context = read.chtk_to_context(infile)
```

this returns an ```EphContext``` that you can then use to instantiated a Chart.

An ```EphContext``` also includes all the options for the chart.

### Sidereal

Sidereal is possible, but here is how you must do it to get meaningful results:
three options must be set:

```
sysflg=const.SID     # indicates sidereal ecliptic
ayanamsa=98          # this shouldnt be the default, but it is; Lahiri - 1; True Citra - 27; and
                     # swisseph ayanamsa
circle=Circle.ZODIAC # circle starts where the zodiac starts; with Circle.ADITYA, it
                     # doesnt start where the "zodiac" starts, i.e., ecltipic longitude doesn't line up to
                     # where the zodiac starts; if you dont change this, it might be
                     # confusing!
```
