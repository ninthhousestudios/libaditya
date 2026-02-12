# README

```libaditya``` is an astrological calculation library meant to be easily understood in terms
of what calculations are performed and how they are done. 

My hope is that astrologers will be able to use this directly themselves. There is
obviously value in the various types of GUI programs and viewing a chart (though
```libaditya``` can draw some kinds of charts), there is also value in thinking about
astrology in a way that interacting with it through ```libaditya``` would help
cultivate. I hope to use it to create more "end-user-friendly" software, but I would
also like it to be possible for non-programmers to learn and use.

There is a companion program ```pyphemeris``` which is meant to serve as an easily
readable documentation on how the library works. Each function in ```libaditya``` itself is
meant to return the requested data in a way that can then be presented in some way.
Built into most ```libaditya``` classes are functions to represent themselves as text
through repr (__repr__) and ```print```, i.e., through ```__str__```. ```pyphemeris```
makes use of these in order to print the requested data to ```stdout```. I have also
started adding ```rich``` representations in ```libaditya``` itself, through ```.rich()``` methods.


# Table of Contents

- [README](#readme)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
  - [Defaults](#defaults)
  - [Entering a Chart](#entering-a-chart)
  - [Reading a Chart from a File](#reading-a-chart-from-a-file)
  - [Chart Types and Options](#chart-types-and-options)
  - [Dignity Example](#dignity-example)
- [Vargas](#vargas)
- [Human Design](#human-design)
- [Sarvatobhadra Chakra](#sarvatobhadra-chakra)
- [Cards of Truth](#cards-of-truth)

# Installation

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

# Usage

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

## Defaults

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

## Entering a Chart

It is now possible to enter chart information "interactively", not really, which will
produce a ```.toml``` chart file.

```
>>> write.new_chart_interactive()
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
                   // below is how Kala represents these in their .chtk file
                   3) 0DD(E/W)MM'SS(.SS)
                   3) DD(N/S)MM'SS(.SS)
alt: float - meters
placename: str (optional)
```

The file that will be written is "name", all lowercase, with any spaces replaced by
"-". Call the function with argument ```outfile="your-filename.toml```". 

The only software I know of that does astrology like this is Kala, produced by Ernst
Wilhelm and his wife; I believe she did the actual programming. I have been using it and
thus the ```.chtk``` format. It is now possible to convert between them. However, the
```.toml``` format has a place for altitude of the Location. The Kala format doesn't.
Right now ```read.chtk_to_toml``` will write it as 0..need to change that.

## Reading a Chart from a File

```read.toml_to_context()``` takes a ```toml``` file such as produced by
```write.new_chart_interactive()```. You can use that to instantiate a Chart:
```
>>> context = read.toml_to_context("chart.toml")
>>> chart = Chart(context)
```

Likewise for ```.chtk``` files

```
>>> context = read.chtk_to_context(infile)
```

this returns an ```EphContext``` that you can then use to instantiate a Chart.

An ```EphContext``` also includes all the options for the chart.

## Chart Types and Options

Plus basic Python if you are new to this.


## Dignity example

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

Vargas can be accessed using ```Chart().varga(n)```.

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

# Human Design

```libaditya``` currently has basic Human Design support and can draw Human Design natal
bodygraphs for a Chart. It can also disply all of the relevant information about the
Human Design properties of the planets, both conscious and unconscious, e.g., their
gate, line, etc.

How to get Human Design information about the planets:
```
>>> c = Chart()
>>> hdp = c.bodygraph().planets()
>>> print(hdp)
// c.bodygraph().(un)conscious_planets() returns a Planets class of all the Planet-s
>>> cp = c.bodygraph().conscious_planets().hd_planets()
>>> print(cp)
>>> ucp = c.bodygraph().unconscious_planets().hd_planets()
>>> print(ucp)
```

To draw a bodygraph:
```
>>> c.bodygraph().draw_svg(outfile="my-bodygraph.svg")
```

A reminder if you are new to Python: if you want to know can come after ```c.bodygraph()```, 
then assign that object to a variable, then you can inspect it using ```dir()``` or tab
completion:
```
>>> bg = c.bodygraph()
>>> dir(bg)
>>> bg.(<TAB><TAB>)
```

TODO:

add Variables, the "arrows" that you can see on some bodygraphs on both sides of the
head center. also, all of the information that also comes from the color, tone, and base
from other planets, e.g., diet, environment, etc.
all of the calculations are necessary, i just need to figure out what thing specifies
what and write that into ```libaditya```.

# Sarvatobhadra Chakra

An early version of ```libaditya``` had a program that would draw a sarvatobhadra
chakra. I have started moving that over to work with ```libaditya```, so that any chart
will be able to draw a sarvatobhadra chakra for itself.

Right now, it only draws the base chart. When this is fully implemented, you will be
able to do something like ```chart.draw_sbc()``` and it will draw one for you.
```
/// english_letters: bool for whether or not to include small English equivalents of the
/// Sanskrit letters
/// right now, .draw_sbc() drawing a Drawing object from drawsvg
>>> d = c.rashi().draw_sbc(english_letters=True)
>>> d.save_svg("sbc-base.svg")
```

# Cards of Truth

I have just started an implementation of Cards of Truth in ```libaditya```.

Currently, it can do year spreads with just the cards, no planets:
```
>>> c = Chart()
>>> births = c.cot().birth_spread()
```

This returns a ```Spread``` object. ```Spread``` currently does not have a ```__str__```
or a ```__repr__```, but you can view it using ```rich```:
```
>>> births.rich()
```

Also, year spreads, though there may be some bugs currently in the implementation:
```
/// ideally .year_spread() with no arguments will be the current year spread; not sure
/// how completely accurate this is currently
/// you can put in any year; 0 is the birth spread, 1 the year after, etc.
>>> c.cot().year_spread().rich()
>>> c.cot().Year_spread(28).rich()
```

If you are new to Python, but know Cards of Truth, check out some of the objects
to see what further information you can get:
```
>>> cot = c.cot()
>>> cot
<libaditya.cards.cards_of_truth.CardsOfTruth object at 0x7f7547f86250>
>>> cot.(<TAB><TAB>)
cot.Spread(                                  cot.jack_quadration()                        
cot.birth_card()                             cot.king_quadration()                        
cot.birth_spread()                           cot.master()                                 
cot.context                                  cot.quadrate(                                
cot.deck()                                   cot.quadraten(                               
cot.get_birth_spread_with_card_in_position(  cot.queen_quadration()                       
cot.get_birthspread_from_quadration(         cot.year_spread(                             
cot.getbspreadwxcfromquad(              
```

Notice that some of these names end with ```()```, some with ```(``` and some with
nothing. Those ending with ```()``` are methods that can be called with no arguments,
and in fact do not have any arguments. So by the list, you know you can properly call:
```
>>> cot.birth_card()
'KD'
```

The names with nothing are variables or objects in their own right. Check them out:
```
>>> cot.context
```

The names with ```(``` can take at least one argument, but may or may not need to have
one or more arguments. You can always try to call them without any:
```
>>> cot.Spread()
Traceback (most recent call last):
  File "<python-input-35>", line 1, in <module>
    cot.Spread()
    ~~~~~~~~~~^^
TypeError: CardsOfTruth.Spread.__init__() missing 1 required positional argument: 'spread_list'
```

And we see that didn't really work. Python has a built-in documentation feature. Under
each class/function/method definition, you can put multi-line comments surrounded by
triple quotes (""") at beginning and end. I have been trying to put documentation into
these. With this, you can look up help in the Python ```repl``` itself:
```
>>> help(cot.Spread)
```
If you read that, you find out we can test ```Spread``` even using spreads that may
never actually exist:
```
>>> cot.Spread([0,1,2,3,4,5,6,7,8,9,10,11,12,13]).rich()
```

At least it works this way right now. It may change once I implemented putting Planet-s into
Card-s.
