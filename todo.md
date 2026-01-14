## jaimini

#
vargas

#
jaimini first strength

r2hHrGxbvS0CjjlporjPYrGDD9OTqLWmMW2EBbs5Y1s=
****.chtk, d16, last three get mixed up, seems clear from
chart why Kala order is what it is

check my check, d27, mix up between 9 and 6


## interface

#
add a time element to Chart
specifically something designed for rectification

#
write sample scripts for going through a directory of .chtk files and doing something
with the data

write the actual function to do this

#
where to add Panchanga; it currently isnt directly accesible
Rashi, probably

#
revamp .pyph file
make interactive .pyph creator


## strucutre

#
nakshatras. update to have 28 derived classes for each nakshatra
change Nakshatras to be a dictionary probably with integer keys
maybe name keys, depending on dealing with abhijit

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
consider binding together Planet and Planets
if each Planet could access its Planets, that would make the api easier
then we may not need to set_attributes? or it could be done differently

#
think about removing Names from EphContext
    they are only used in ephemeris mode in order to print to screen
    in terms of calculation, they are not really needed
    so can i remove the Names from the calculation and deal with them later
    if i need to print?
    maybe it returns the data and __str/repr__ can provide defaults to print to
    screen, defaults that cant be changed

#
something way off with draconic coordinates. i wish it worked. try later
restructure entire way of doing draconic

# 

-Hc and -Bc dont work currently

#
do lowest_daily_speed for other planets

#
fix next_vara
    it basically works. it is just that sometimes if it is literally at the
beginning of the vara, it will say the vara that is beginning, not the next one

## calculations

#
checkout Planet.ingress vs. Sun.ingress

#
akriti yogas
    the ones needing all planets in 7 houses need work
    the same algorithm doesnt work for them as for the others
    actually, relook at all of them because all probably need some work

#
ucca bala
    almost works
    add a method to Longitude that determines if one longitude is inbetween two other
    moon and mercury not working
longitudes on the circle

chesta bala
dig bala

## hd

#
hd.calc.dream_context is not working properly fix it
