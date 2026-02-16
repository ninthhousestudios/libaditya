

#
couldnt make Planet().constellation() work from pyphemeris
calling Chart().Ecliptic() didnt change anything
try it again

#
README.md

FixedStar
TheStars
Ecliptic

#
add .whoami() method to Chart; this is mostly for calculation options, e.g., tropical,
aditya, sidereal, which ayanamsa, etc.
could mean also adding one to EphContext

some easy way to identify a chart

#

steps; currently libaditya has no way to do steps
plotting, data visualisation, etc.

obviously, python itself can be used to do steps, so not sure how necessary or useful
this is

was an idea, but need actual use cases to decide if it would be worth it

#
stars

perhaps change TheStars.search_star_interactive() to search names in info field? #0#

add nakshatras to fixed stars

make __repr__ and __str__ for Ecliptic
checkout rich?

#
fix Varga/Rashi header

#
draw
hd and sbc

can now draw hd bodygraph
```
chart.bodygraph().draw_svg()
```
so add transit charts, composite charts, and the return/opposition charts
also, dream charts

continue sbc...still quite a bit to do

#
implement all swisseph features in the appropriate place

started alt/azimuth coordinates

TODO: 
    Planet.nod_aps_ut()

#
add Mean Node option

#
devanagari output in terminal

greek names?

#
avasthas

lajjitaadi
baladi
jagradadi
deeptadi

everything is in place to do this

add "detriment" or "fall" for Western/Hellenistic


## jaimini

#
vargas

for varga deities
check 40
check -45/45
check 60
check d-45 deities
add iast/deva versions of varga deities

add dignities in each varga for each Planet and in Rashi

#
jaimini first strength

r2hHrGxbvS0CjjlporjPYrGDD9OTqLWmMW2EBbs5Y1s=
****.chtk, d16, last three get mixed up, seems clear from
chart why Kala order is what it is
also same chart, look at fss in d9

check my check, d27, mix up between 9 and 6

irina-tweedie.chtk - multiple issues in first strength with tropical and aditya

## interface

#
move vimshottari around
put calc functions in Rashi and print functions in print_functions

use this to test to make sure setting ephe_path in Chart.__init__() works


## strucutre

#
nakshatras. update to have 28 derived classes for each nakshatra
change Nakshatras to be a dictionary probably with integer keys
maybe name keys, depending on dealing with abhijit

though regardless of creating a class for each, it would probably be better to have all
the nakshatra information in a dictionary in constants.py


#
something way off with draconic coordinates. i wish it worked. try later
restructure entire way of doing draconic


#
fix next_vara
    it basically works. it is just that sometimes if it is literally at the
beginning of the vara, it will say the vara that is beginning, not the next one

the vara isnt working properly
it currently uses a python library, but swe actually has its own function for day of the
week, but is has Monday as 0, where as the python library has Monday as 1, so need to
change everything and make it work correctly

this time doesnt work. says it is shukravara and that the next vara is shukravara
2461071.2983680554

it just doesnt work. needs to be completely reworked

## calculations


#
akriti yogas
    the ones needing all planets in 7 houses need work
    the same algorithm doesnt work for them as for the others
    actually, relook at all of them because all probably need some work

was watching tsoding about creating a diff tool in python...levenshtein algorithm could
be adapted to yogas if yogas are represented a certain way


#
add dispositors, final dispositors, parivartana or chakra yogas

#
add dignities in vargas

## hd

#
trying to shift gate_one didnt work
also consider sidereal
