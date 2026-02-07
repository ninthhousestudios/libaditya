## features

#
stars

something is wrong with Kappa Geminorum

may be happening with another star
ec.boundaries() is obviously not correct

it greatly jumps longitude around years 19-22

>>> for n in range(0,50):
...     thisone=here1980.shift("f","y",n).stars()["kapGem"]
...     print(n,thisone,thisone.swe_id())
...     
Stellarium not available...
0 (24.701871548093862,24.702,1) ,kapGem
Stellarium not available...
1 (24.755265680303086,24.755,1) ,kapGem
Stellarium not available...
2 (24.813640766327328,24.814,1) ,kapGem
Stellarium not available...
3 (24.87773676327356,24.878,1) ,kapGem
Stellarium not available...
4 (24.94891215334488,24.949,1) ,kapGem
Stellarium not available...
5 (25.028071456767464,25.028,1) ,kapGem
Stellarium not available...
6 (25.1167459890359,25.117,1) ,kapGem
Stellarium not available...
7 (25.217241516783034,25.217,1) ,kapGem
Stellarium not available...
8 (25.331851032537802,25.332,1) ,kapGem
Stellarium not available...
9 (25.46436509569815,25.464,1) ,kapGem
Stellarium not available...
10 (25.62028256421613,25.62,1) ,kapGem
Stellarium not available...
11 (25.806812160404036,25.807,1) ,kapGem
Stellarium not available...
12 (26.035743043829438,26.036,1) ,kapGem
Stellarium not available...
13 (26.32544134120104,26.325,1) ,kapGem
Stellarium not available...
14 (26.705954493670674,26.706,1) ,kapGem
Stellarium not available...
15 (27.232438102263913,27.232,1) ,kapGem
Stellarium not available...
16 (28.014066723966522,28.014,1) ,kapGem
Stellarium not available...
17 (29.30408774659443,29.304,1) ,kapGem
Stellarium not available...
18 (31.853508875877683,31.854,1) ,kapGem
Stellarium not available...
19 (39.250329354437405,39.25,1) ,kapGem
Stellarium not available...
20 (113.6680288960029,113.668,1) ,kapGem
Stellarium not available...
21 (189.09866804178543,189.099,1) ,kapGem
Stellarium not available...
22 (196.54893486972585,196.549,1) ,kapGem
Stellarium not available...
23 (199.10940351940644,199.109,1) ,kapGem
Stellarium not available...
24 (200.40457116159936,200.405,1) ,kapGem
Stellarium not available...
25 (201.18932154466415,201.189,1) ,kapGem
Stellarium not available...
26 (201.71805325833498,201.718,1) ,kapGem
Stellarium not available...
27 (202.10049107032992,202.1,1) ,kapGem
Stellarium not available...
28 (202.39094510679934,202.391,1) ,kapGem
Stellarium not available...
29 (202.62007992281337,202.62,1) ,kapGem
Stellarium not available...
30 (202.8061974262802,202.806,1) ,kapGem
Stellarium not available...
31 (202.96049217859573,202.96,1) ,kapGem
Stellarium not available...
32 (203.09113144929555,203.091,1) ,kapGem
Stellarium not available...
33 (203.20328639200164,203.203,1) ,kapGem
Stellarium not available...
34 (203.30076134993928,203.301,1) ,kapGem
Stellarium not available...
35 (203.38680690370444,203.387,1) ,kapGem
Stellarium not available...
36 (203.4634684231916,203.463,1) ,kapGem
Stellarium not available...
37 (203.5325073207531,203.533,1) ,kapGem
Stellarium not available...
38 (203.59562430542513,203.596,1) ,kapGem
Stellarium not available...
39 (203.65379546006355,203.654,1) ,kapGem
Stellarium not available...
40 (203.7078192990385,203.708,1) ,kapGem
Stellarium not available...
41 (203.75871570900802,203.759,1) ,kapGem
Stellarium not available...
42 (203.80675725654078,203.807,1) ,kapGem
Stellarium not available...
43 (203.852265383683,203.852,1) ,kapGem
Stellarium not available...
44 (203.89585383511147,203.896,1) ,kapGem
Stellarium not available...
45 (203.93724250607636,203.937,1) ,kapGem
Stellarium not available...
46 (203.976775306079,203.977,1) ,kapGem
Stellarium not available...
47 (204.014621246551,204.015,1) ,kapGem
Stellarium not available...
48 (204.05041365504582,204.05,1) ,kapGem
Stellarium not available...
49 (204.08460775933736,204.085,1) ,kapGem

#
fix Varga/Rashi header

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
