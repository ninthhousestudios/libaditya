#

split pyphemeris off from libaditya

i changed pyproject.toml to use hatch
it built and published libaditya correctly, with all the ephe files; it works, i checked
it
it didnt include pyphemeris because i didnt tell it to
so then i can just move pyphemeris

#

consider binding together Planet and Planets
if each Planet could access its Planets, that would make the api easier
then we may not need to set_attributes? or it could be done differently

likewise with Sign and Signs
if there was recursion, i could write
```
chart.jaimini().svamsha().aspects_to()
```

right now, only Signs knows how rashi aspects
so we have to do
```
chart.jaimini().rashi().signs().rashi_aspects_to(Sign)
```

#

do lowest_daily_speed for other planets

hd.calc.dream_context is not working properly fix it

#

fix next_vara
    it basically works. it is just that sometimes if it is literally at the
beginning of the vara, it will say the vara that is beginning, not the next one

#

panchanga and monthly_panchanga
    seemed to fix moonrise and moonset just by some hacks; not sure how well
they work for everything
    need to look at nakshatra, tithi, yoga
    also have issue like moonrise/set about date and utc/local
    but also between Kala, mp and pyph -e i was getting three different times
for the next nakshatra


#

akriti yogas
    the ones needing all planets in 7 houses need work
    the same algorithm doesnt work for them as for the others
    actually, relook at all of them because all probably need some work

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

#

validate vargas with parivritti calculations

#

think about implementing non-parivritti vargas
    started hora - mostly works with tropical
    with my chart, Sun dignity in Hora says "None"
    placement works with Adityas and Tropical; in my Aditya Hora, Sun and Moon
        say "None"

#

check first strength in vargas

#

revamp .pyph file
make interactive .pyph creator

#

jaimini
    first source of strength
    check my check, d27, mix up between 9 and 6 in fss
    argala
    vargas

#

ucca bala
chesta bala
dig bala
