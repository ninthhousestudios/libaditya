# README

```libaditya``` is an astrological calculation library meant to be easily understood in terms
of what calculations are performed and how they are done. 

there is a companion program ```pyphemeris``` which is meant to serve as an easily
readable documentation on how the library works. Each function in libaditya itself is
meant to return the requested data in a way that can then be presented in some way.
Built into most ```libaditya``` classes are functions to represent themselves as text
through repr (__repr__) and ```print```, i.e., through ```__str__```. ```pyphemeris```
makes use of these in order to print the requested data to ```stdout```.

you can try ```pyphemeris``` by using ```uv``` to add it to your libaditya project:
```
uv add pyphemeris
```

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Options](#options)

## Dependencies

automatically installed with ```uv```

python, [pyswisseph](https://pypi.org/project/pyswisseph/), [python-prettytable](https://pypi.org/project/prettytable/)

written with python 3.13

## Installation

```libaditya``` is now on pypi.org, so it can be installed with ```pip install
libaditya```...I think. I use Arch (btw) and they do python packages differently (I
think?...Python packaging is strange), so I use virtual environments through ```uv```.

In any case, at this point ```libaditya``` is not really mature enough to have a major
version, so if you are interested in testing it out or changing it or working on it, I
recommend installing is the following way, then you can pull changes as they come:

I recommend using ```uv``` to install ```libaditya```. On MacOS, you can ```brew install uv```

```sh

git clone https://gitlab.com/j0sh4rp3/libaditya

uv venv
source .venv/bin/activate
uv add . --dev
```

then, 1) if you dont change any of the code at all, then you can do ```git pull```, and
it should update from the gitlab repo. 2) if you make changes to libaditya, im not really sure with
how that would work in git from getting updates from libaditya and your own...

## Usage

then you can go into the Python ```repl``` using
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
classes and function so that there is something helpuful printed. 

### Defaults

Basically all values have defaults, so you can also do this
```
>>> c=Chart()
>>> dir(c)
```
to see all of what Chart has and can do.

Chart is the main interface for any information, since Chart() is an instantiion of a
particular time and/or location. You can try ```sun=Sun()```, for instance. This works
and you can use it to explore Sun and what it can do, but in actual practice you want a
particular Sun, so you should use chart.rashi().planets().sun() and then whatever you
want to know, e.g., ```chart.rashi().planets().sun().dignity()```

Most of this is meant to be self explanatory. The one thing I need to document better is
how to input information. It is through EphContext, from libaditya.objects.context. It
takes a JulianDay and a Location, then a bunch of options. All of these have defaults
that should a chart for the current time more or less.

### Entering a Chart

It is now possible to enter chart information "interactively", not really, which will
produce a ```.toml``` chart file.

```
>>> write.write_new_chart_interactive()
```

In order, it will expect:
```
name: str (optional)
date: MM/DD/YYYY
hour: (HH:MM(:SS)) (UTC)
utcoffset: float
lat: N is positive
long: E is positive
    three formats: 1) decimal
                   2) DD:MM(:SS)
                   # below is how Kala represents these in their .chtk file
                   3) 0DD(E/W)MM'SS(.SS)
                   3) DD(N/S)MM'SS(.SS)
alt: float - meters
placename: str (optional)
```

The file that will be written is "name", all lowercase, with any specials replaced by
"-". Call the function with argument ```outfile="your-filename.toml```. 

The only software I know of that does astrology like this is Kala, produced by Ernst
Wilhelm and his wife; I believe she did the actual programming. I have been using it and
thus the ```.chtk``` format. It is now possible to convert between them. However, the
```.toml``` format has a place for altitude of the Location. The Kala format doesn't.
Right now chtk_to_toml will write it as 0..need to change that.

### reading a chart from a ```.toml``` file

```read.toml_to_context()``` takes a ```toml``` file such as produced by
```write_new_chart_interactive()```. You can use that to instantiate a Chart:
```
>>> context = read.toml_to_context("chart.toml")
>>> chart = Chart(context)
```

### ```.chtk``` files

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
ayanamsa=98          # this shouldnt be the default, but it is; Lahiri - 1; True Citra - 27; any
                     # swisseph ayanamsa
circle=Circle.ZODIAC # circle starts where the zodiac starts; with Circle.ADITYA, it
                     # doesnt start where the "zodiac" starts, i.e., ecltipic longitude doesn't line up to
                     # where the zodiac starts; if you dont change this, it might be
                     # confusing!
```

### Read a .chtk file

this is the most useful for getting birth information without needing to do it manually

```
jhcontext = read.chtk_to_context("josh.chtk")
(or)
jhcontext = read.chtk_to_toml("josh.toml")
jhchart = Chart(jhcontext)
```

to change any of the options, do like this:

```
jhsiderealcontext =
replace(jhcontext,sysflg=const.SID,ayanamsa=27,circle=Circle.ZODIAC,print_outer_planets=False)
```

this keeps everything else the same same, and changes what you specified to what you
specified

```
jhdsidchart = Chart(jhsiderealcontext)
```

using tab completion is a good way to explore:
type

```>>> jhchart.```

then tab twice, and you will see a list:
```
>>> jhchart.
jhchart.context     jhchart.get_varga(  jhchart.jaimini()   jhchart.rashi()  
```

actualy it will look different now
you should see something like ```jhchart.sidereal()```
you can use that to get a sidereal version of that chart. Default ayanamsa is 27.
Ayanamsa are swiss ephemeris values, which will be elsewhere in this documentation
eventually. Also, 98 for Dhruva GC mid-Mula, 99 for Ecliptic Vedanga Jyotisha and 100
for Equatorial Vedanga Jyotisha
Ayanamsa can be set by calling
```
jhchart.sidereal(ayanamsa=18)
```

if you working mostly with a sidereal chart, you can assign it to a variable
```
sidchart = jhchart.sidereal(ayanamsa=25)
```

then for the tropical or aditya versions of that chart, you could
```
sidchart.tropical()
sidchart.aditya().rashi()
```

a Chart is basically a collection of Vargas. The Rashi is the most important. You can
access it through Chart.rashi()

if you assign is to a variable while in the repl:
```
>>> rashi=jhchart.rashi()
```

then you can use tab completion of, ```dir()```:

```
>>> dir(rashi)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_amsha', '_cusps', '_get_pada', '_planets', '_rashi_planets', '_signs', 'akriti_yogas', 'amsha', 'argala', 'bandhana_yogas', 'chart', 'context', 'cusps', 'dignities', 'draw_sun_by_sign_table', 'init_cusps', 'init_planets', 'jaimini_first_strength', 'lagna', 'mkheader', 'pada', 'padas', 'planets', 'signs', 'sysflgstr', 'upapada', 'varga_name', 'where_is']
```

everything surrounded by "__" is a special Python  method. The ones without any
underscores are the methods that "Rashi" has, things you can know about the rashi at
hand.

e.g.,

```
>>> rashi.lagna()

self.sign()=8 viṣṇu
+--------+-------------------+----------------+
| Object | In Sign Longitude | Real Longitude |
+--------+-------------------+----------------+
| Cusp 1 |          12:59:45 |        192.996 |
+--------+-------------------+----------------+
```

The functions of the Classes themselves give the information in some way, and then there
is a separate part that prints. Most of these have in-built printing methods due to
Python, so that is why we can look at them to here. But to use them in a different
application, we need to understand the data is returned, so we can read it and use it is
whichever way we need at some time.

#### Dignity example

for example

```
>>> rashi.dignities()
['GF', 'N', 'GF', 'OH', 'EX', 'N', 'MT']
```

```
>>> help(rashi.dignities)
```

you will see a help screen where you can read

```
dignities() -> [<class 'str'>]
    return a list of dignities in the natural order
    Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn
```

so is returns a list of strings "EX", "DB", "GF", etc. for all the dignities of the
planets in normal Vedic order. So that is the data; it is use to you how to find it.

in libaditya.printf (which you should be able to use as printf if you did ```from
libaditya import *```), there are print functions for some things.

for example
```
printf.print_dignity_table(chart.rashi().dignities())
```

you can get a varga with ```.varga(n)```

get dignities in the navamsha
```
printf.print_dignity_table(chart.varga(9).dignities())
```

to find the chara karakas
```
printf.print_jaimini_karakas(chart.rashi().planets().jaimini_karakas())
```

so then you can find the AK in the d9
```
ak = chart.rashi().planets().jaimini_karakas()[0]
```

```Planets.jaimini_karakas()``` return a list of ```Planet``` classes. So if the AK is
Venus, then ```ak``` would the ```Venus``` class of the Venus of the Rashi chart.

get svamsha
```
svamsha = chart.varga(9).signs()[ak.sign()]
```

```Varga.signs()``` returns a dictionary, where the keys are integers 1-12, which
correspond to signs 1-12. This is true regardless of the system we are using. The system
is set by the ```sysflg``` and by the ```circle=Circle```. ```sysflg``` can be tropical
or sidereal (footnote: some others that aren't well implemeneted yet, e.g., helio, bary,
draconic, true sidereal) ```circle=Circle.ZODIAC``` or ```circle=Circle.ADITYA```. In
the former, sign 1 = Aries (whether tropical or sidereal). In the later, sign 1 = Dhata,
which is at 330 tropical ecliptic longitude.

This takes care of all necessary tropical, Aditya, sidereal calculations.

When accessed through ```Chart()``` all of these works as given by the ```EphContext```
parameters ```sysflg``` and ```circle``` with the options as just explained, and of
course ```ayanamsa```.

To see all the options in ```EphContext```:
```
help(EphContext)
```

# Vargas

Vargas can be accessed using ```Chart.varga(n)```.

If ```n``` is positive, the corresponding parivritti varga of that number will be
produced.

Other vargas will have negative numbers to indicate them. Here are the vargas currently
implemeneted:
```
-2 Hora
-3 Drekkana
-4 Chaturthamsha
-10 Dashamsha
-100 Dashamsha with Even Rashis going in reverse
-12 Dvadashamsha
-16 Shodashamsha
-20 Vimshamsha
-24 Parashara Chaturvimshamsha
-240 Siddhamsha
-27 Bhamsha
-40 Khdavedamsha
-45 Akshavedamsha
-60 Shashtyamsha
```
