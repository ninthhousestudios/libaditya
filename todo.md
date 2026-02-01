## features

#
have TheStars print all the stars and their information

#
draw
hd and sbc

can now draw hd bodygraph
```
chart.bodygraph().draw_svg()
```

#
implement all swisseph features in the appropriate place

e.g., Planet.nod_aps_ut()

started swe.heliacal_ut() in objects/swe_functions.py as inheritor Mixin SWEPlanet
added metar for weather data. from this can satisfy function arguments concerning place.
this will be built-in to location. but the user must pass the correct "location" for
this, which will be an ICAO identifier; basically, the nearest airport and the weather
data there. need to implement finding relative humidity from dewpoint. also see about
finding old metar data. i would like to have .next_heliacal_rising/setting work for
whatever jds are reasonable

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

#
fixed stars

want to do "true sidereal", but also just, fixed stars in general

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
write sample scripts for going through a directory of .chtk files and doing something
with the data

write the actual function to do this

started this in ladb, works pretty well
some charts have weird problems and i have no idea what is wrong
maybe i will just reenter them in kala

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
2025/12/01 - first part done strcuturally
Sign and Signs are now recursive
so we can put all of the Signs functions in Sign

right now, only Signs knows how rashi aspects
so we have to do
```
chart.jaimini().rashi().signs().rashi_aspects_to(Sign)
```
TODO: this->
likewise with Sign and Signs
if there was recursion, i could write
```
chart.jaimini().svamsha().aspects_to()
```


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

## hd

#
trying to shift gate_one didnt work
also consider sidereal
