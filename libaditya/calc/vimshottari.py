#    This file is part of pyphemeris.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
#
#    pyphemeris is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyphemeris is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with pyphemeris.  If not, see <https://www.gnu.org/licenses/>.

import swisseph as swe

from libaditya import constants as const
from libaditya import utils
from libaditya.objects import Moon

# to make code more readable
lord = 0
length = 1

def print_vimshottari_dasha(planet=Moon(),dlevels=1,yrlen=365.2422):
    """
    print vimshottari dasha based on the position of planet
    to levels = dlevels
    using year lenght yrlen; default is 365.2422, a saura year
    this prints the dashas as it calculates them
    """

    print("\n\nVimshottari Dasha\n")

    # this is for the year length
    for opt in const.dasha_years:
        if yrlen == opt[1]:
            yrstr = opt[0].capitalize()

    print(f"Based on the position of {planet.name()}")
    print(f"Using {planet.ayanamsa_name()}")
    print(f"Using {yrstr} year length")


    # long is the sidereal longitude
    # nindex is the index of the nakhsatra into pglob.nakshatra
    long = planet.nakshatra().ashvini_longitude()
    nindex = planet.nakshatra().index()

    # how far into the nakshatra the moon is
    elapsed = long-(nindex*planet.nakshatra().naksize())
    elapsedfraction = elapsed/planet.nakshatra().naksize()

    # find which dasha is the first mahadasha
    first_dasha = nindex%9
    # dont actually need years_left
    # years_left = const.vimshottari_dashas[first_dasha][length]-dashas[first_dasha][length]*elapsedfraction
    years_elapsed = const.vimshottari_dashas[first_dasha][length]*elapsedfraction
    # age when the mahadasha started, which was probably before birth
    age = -years_elapsed

    #print(f"Moon is nakshatra {pglob.nakshatra[nindex]}, at {elapsed} degrees out of 13.33")
    #print(f"First mahadasha is of {dashas[first_dasha][0]}, {dashas[first_dasha][1]*elapsedfraction} years into the dasha")

#    print(f"\n{dashas[first_dasha][lord]} mahadasha: {putil.dec2ymd(age)}")
#    planet.context.timeJD.indent_print(level)
#    next_dasha_starts = panch.shift('f','d', years_left*yrlen)
#    age += dashas[first_dasha%9][length]
    dasha_starts = planet.timeJD.shift('b','d',-age*yrlen)
    level = 0
    for d in range(0,9):
        this_dasha = (first_dasha+d)%9
        # the following is the list of dasha lords
        # we pass to the function that prints the next dasha level
        # in order to calculate the time in that dasha
        dlist = []
        dlist.append(this_dasha)
        print(f"\n{const.vimshottari_dashas[this_dasha][lord]} mahadasha: {utils.dec2ymd(age)}")
        print(f"Duration: {const.vimshottari_dashas[(first_dasha+d)%9][length]} years")
        dasha_starts.indent_print(level)
        if level+1 < dlevels:
            print_next_dasha_level(dlist,dasha_starts,level+1,dlevels,yrlen,age)
        # the other dashas after the first get their full time
        dasha_starts = dasha_starts.shift('f','d', (const.vimshottari_dashas[(first_dasha+d)%9][length])*yrlen)
        age += const.vimshottari_dashas[(first_dasha+d)%9][length]

def print_next_dasha_level(dlist,dasha_time,level,dlevels,yrlen,age):
    # if dlevels is 3 and level is 3, we want to print this level, else just return
    if level <= dlevels:
        this_dasha = (dlist[level-1])%9
        # how many tabs to indent printing, based on the level
        tab = utils.mktab(level)
        # how many "sub" dashas
        sub = utils.mksub(level)
        for d in range(0,9):
            lordstr = mklord(dlist+[this_dasha])
            # now we figure out how long this dasha runs
            # then we shift forward to that time, so that on the next loop, we print that information first
            # length of this dasha
            dlen = 1
            #print(f"{dlist=}")
            # dlist has all the dasha level before this one, so multiply all of those
            for lord in dlist:
                dlen = dlen * const.vimshottari_dashas[lord][length]
            # then multiply the lenght of this one
            dlen = dlen * const.vimshottari_dashas[this_dasha][length]
            #print(f"{dlen=}")
            # this gives the decimal value in years for this dasha
            # for two levels, divided by 120, for 3 levels, divide by (120*120), etc.
            # since we start at level 0 in the first function, here level=1 for the second level
            # level=2 for the 3rd level, etc.
            divfac = 120**level
            #print(f"{divfac=}")
            dlen = dlen / divfac 
            #print(f"{dlen=} {dlen*yrlen}")
            #print(f"{dlen=}")
            # this print the starts time, date, and age for the current dasha
            print(f"\n{tab}{lordstr} {sub}dasha: {utils.dec2ymd(age)}")
            print(f"{tab}Duration: {utils.dec2ymd(dlen)}")
            dasha_time.indent_print(level)
            if level+1 < dlevels:
                print_next_dasha_level(dlist+[this_dasha],dasha_time,level+1,dlevels,yrlen,age)
            # now shift forward to the next dasha on this level
            # this sets up all the needed information in the next loop
            dasha_time = dasha_time.shift('f','d', dlen*yrlen)
            age += dlen
            this_dasha = (this_dasha+1)%9

# make a string for dasha lords including subdashas
def mklord(dlist):
    """
    make a string of dashas lords
    """
    lordstr = ""
    for lord in range(0,len(dlist)):
        if lord == len(dlist)-1:
            lordstr += const.vimshottari_dashas[dlist[lord]][0]
        else:
            lordstr += const.vimshottari_dashas[dlist[lord]][0] + "/"
    return lordstr

def calculate_vimshottari_dasha(planet=Moon(),dlevels=1,yrlen=const.dasha_years[0][1]):
    """
    calculate vimshottari dasha
    first initilaze the base condition
    time is a JulianDay class
    then call calc_vdasha, which is a recursive function that does
    the acutal calculations
    return a list [[dasha1jd,dasha1length,subdasha],etc.,first_dasha_lord,beginning_age]
    """

    # initialization

    # long is the sidereal longitude
    # nindex is the index of the nakhsatra into pglob.nakshatra

    long = planet.nakshatra().ashvini_longitude()
    nindex = planet.nakshatra().index()

    # how far into the nakshatra the moon is
    elapsed = long-(nindex*planet.nakshatra().naksize())
    elapsedfraction = elapsed/planet.nakshatra().naksize()

    # find which dasha is the first mahadasha
    first_dasha = nindex%9
    # dont actually need years_left
    # years_left = const.vimshottari_dashas[first_dasha][length]-dashas[first_dasha][length]*elapsedfraction
    years_elapsed = const.vimshottari_dashas[first_dasha][length]*elapsedfraction
    # age when the mahadasha started, which was probably before birth
    age = -years_elapsed

    dasha_starts_jd = planet.timeJD.shift('b','d',-age*yrlen)
    level = 0
    dlist = [first_dasha]
    vdasha = calc_vdasha(dlist,dasha_starts_jd,level,dlevels,yrlen)

    return vdasha + [first_dasha] + [age]

def calc_vdasha(dlist,dasha_time,level,dlevels,yrlen):
    this_dasha_list = []
    next_dasha_list = []
    # if dlevels is 3 and level is 3, we want to print this level, else just return
    if level+1 <= dlevels:
        this_dasha = (dlist[level])%9
        for d in range(0,9):
            # find the length of this (sub)dasha
            dlen = 1
            for lord in range(1,len(dlist)):
                dlen = dlen * const.vimshottari_dashas[dlist[lord]][length]
            dlen = dlen * const.vimshottari_dashas[this_dasha][length]
            divfac = 120**level
            dlen = dlen / divfac 
            #print(f"{dlen=} {dlen*yrlen}")
            # now dlen is the length of the dasha in years
            if level+1 < dlevels:
                next_dasha_list = calc_vdasha(dlist+[this_dasha],dasha_time,level+1,dlevels,yrlen)
            this_dasha_list.append([dasha_time,dlen*yrlen,next_dasha_list])
            dasha_time = dasha_time.shift('f','d', dlen*yrlen)
            this_dasha = (this_dasha+1)%9
    return this_dasha_list

def print_calculated_vimshottari_dasha(dasha):
    """
    print the dasha given in the list dasha
    dasha has the form:
    [[dasha1jd,dasha1length,subdasha],etc.,first_dasha_lord,beginning_age]
    """
    # these initialize what we need to recurse down the dasha list
    age = dasha.pop()
    first_dasha = dasha.pop()
    level = 0

    pd([first_dasha],dasha,level,age)

def pd(dlist,dasha,level,age):
    # how many tabs to indent printing, based on the level
    tab = utils.mktab(level)
    # how many "sub" dashas
    sub = utils.mksub(level)

    this_dasha = dlist[len(dlist)-1]

    for d in range(0,len(dasha)):
        lordstr = mklord(dlist[1:]+[this_dasha])
        print(f"\n{tab}{lordstr} {sub}dasha: {utils.dec2ymd(age)}")
        print(f"{tab}Duration: {utils.dec2ymd(dasha[d][1]/365.2422)}")
        dasha[d][0].indent_print(level)
        if dasha[d][2] != []:
            pd(dlist+[this_dasha],dasha[d][2],level+1,age)
        age += dasha[d][1]/365.2422
        this_dasha = (this_dasha+1)%9

