#    This file is part of libaditya.
#
#    Copyright (c) 2025 Josh Harper <humanhaven@substack.com>
#
#    libaditya is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    libaditya is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with libaditya.  If not, see <https://www.gnu.org/licenses/>.

import swisseph as swe

from libaditya import constants as const
from libaditya import utils
from libaditya.objects import Moon, JulianDay

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
    for key,value in const.dasha_years.items():
        if yrlen == value:
            yrstr = key.capitalize()

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
            lordstr = utils.mk_dasha_lord(dlist+[this_dasha])
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


def calculate_vimshottari_dasha(planet=Moon(),dlevels=1,yrlen=const.dasha_years["saura"]):
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

def period_duration(lords,yrlen=const.dasha_years["saura"]):
    """
    duration in days of a vimshottari period defined by lord indices
    lords = [maha, bhukti, pratyantar, ...]
    e.g. [2,4,5] for Sun-Mars-Rahu pratyantar dasha
    """
    years = 1.0
    for lord_idx in lords:
        years *= const.vimshottari_dashas[lord_idx][length]
    n = len(lords)
    years /= 120 ** (n - 1)
    return years * yrlen

def calculate_specific_period(planet=Moon(),lords=[],yrlen=const.dasha_years["saura"]):
    """
    calculate start time and duration of a specific vimshottari period
    without computing the entire dasha tree

    lords: list of lord indices, e.g. [2, 4, 5] for Sun mahadasha,
           Mars bhukti, Rahu pratyantar
           indices into const.vimshottari_dashas:
           0=Ketu, 1=Venus, 2=Sun, 3=Moon, 4=Mars, 5=Rahu,
           6=Jupiter, 7=Saturn, 8=Mercury

    returns (start_jd, duration_days)
    """
    if not lords:
        return None

    # initialization (same as calculate_vimshottari_dasha)
    long = planet.nakshatra().ashvini_longitude()
    nindex = planet.nakshatra().index()
    elapsed = long - (nindex * planet.nakshatra().naksize())
    elapsedfraction = elapsed / planet.nakshatra().naksize()
    first_dasha = nindex % 9
    years_elapsed = const.vimshottari_dashas[first_dasha][length] * elapsedfraction
    age = -years_elapsed
    current_jd = planet.timeJD.shift('b','d',-age*yrlen)

    # walk each level, skipping to the requested lord
    for level in range(len(lords)):
        target = lords[level]

        # which lord starts this level's sequence?
        if level == 0:
            start_lord = first_dasha
        else:
            start_lord = lords[level - 1]  # sub-periods start from parent lord

        # skip past all periods before the target lord
        this_lord = start_lord
        count = 0
        while this_lord != target and count < 9:
            trial_lords = lords[:level] + [this_lord]
            dur = period_duration(trial_lords, yrlen)
            current_jd = current_jd.shift('f','d', dur)
            this_lord = (this_lord + 1) % 9
            count += 1

    duration = period_duration(lords, yrlen)
    return (current_jd, duration)

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
        lordstr = utils.mk_dasha_lord(dlist[1:]+[this_dasha])
        print(f"\n{tab}{lordstr} {sub}dasha: {utils.dec2ymd(age)}")
        print(f"{tab}Duration: {utils.dec2ymd(dasha[d][1]/365.2422)}")
        dasha[d][0].indent_print(level)
        if dasha[d][2] != []:
            pd(dlist+[this_dasha],dasha[d][2],level+1,age)
        age += dasha[d][1]/365.2422
        this_dasha = (this_dasha+1)%9

def current_vimshottari_dasha(planet=Moon(),nowtimeJD=JulianDay(),dlevels=3,yrlen=const.dasha_years["saura"]):
    """
    find the dasha at nowtime for the dashas of someone born at btime down to dlevels levels
    returns a list [lord,lord,lord,...,next_dasha_startsJD]
    """
    # first we need to find where the dashas start

    # long is the sidereal longitude
    # nindex is the index of the nakhsatra into pglob.nakshatra
    long = planet.nakshatra().ashvini_longitude()
    nindex = planet.nakshatra().index()

    # how far into the nakshatra the moon is
    elapsed = long-(nindex*planet.nakshatra().naksize())
    elapsedfraction = elapsed/planet.nakshatra().naksize()

    # find which dasha is the first mahadasha
    first_dasha = nindex%9
    years_elapsed = const.vimshottari_dashas[first_dasha][length]*elapsedfraction
    # age when the mahadasha started, which was probably before birth
    age = -years_elapsed

    dasha_startsJD = planet.timeJD.shift('b','d',-age*yrlen)
    level = 0
    dlist = [first_dasha]
    # returns a list
    # [[current,dasha,lords], [next,dasha,lords], time_next_dasha_starts]
    result = calc_current(dlist,dasha_startsJD,nowtimeJD,level,dlevels,yrlen)

    return result
    
def calc_current(dlist,this_dasha_startsJD,nowtimeJD,level,dlevels,yrlen):
    this_dasha = (dlist[level])%9
    next_dasha = (this_dasha+1)%9

    if level+1<=dlevels:
        for n in range(0,9):
        # find the length of the current dasha
            dlen = 1
            for lord in range(1,len(dlist)):
                dlen = dlen * const.vimshottari_dashas[dlist[lord]][length]
            dlen = dlen * const.vimshottari_dashas[this_dasha][length]
            divfac = 120**level
            dlen = dlen / divfac  # the length of this dasha in years
            next_dasha_startsJD = this_dasha_startsJD.shift('f','d',dlen*yrlen)
            # if next_dasha starts after current time, then we are in this dasha
            if next_dasha_startsJD > nowtimeJD:
                next_dasha = calc_current(dlist+[this_dasha],this_dasha_startsJD,nowtimeJD,level+1,dlevels,yrlen)
                if next_dasha == []:
                    return [this_dasha] + [next_dasha_startsJD]
                else:
                    return [this_dasha] + next_dasha # next_dasha is a list
#                return [this_dasha] + calc_current(dlist+[this_dasha],this_dasha_startsJD,nowtimeJD,level+1,dlevels,yrlen)
            this_dasha = next_dasha
            next_dasha = (this_dasha+1)%9
            this_dasha_startsJD = next_dasha_startsJD
    return []

def get_next_lord(lord: int) -> int:
    """
    lord is an integer
    """
    return (lord+1)%9

def next_dasha_lords(lords):
    """
    lords is list of dasha lords
    it finds the next dasha lords to the same number of levels

    only works properly down to 5 levels

    in this function, we reverse the list
    "first_lord" is actually the last lord in the dasha scheme, etc.
    """
    lords = list(lords.__reversed__())

    if len(lords) == 1:
        return [get_next_lord(lords[0])]

    length = len(lords)

    first_lord = lords[0]
    next_lord = lords[1]
    if get_next_lord(first_lord) == next_lord:
        if length > 2:
            next_next_lord = lords[2]
            if get_next_lord(next_lord) == next_next_lord:
                if length > 3:
                    next_next_next_lord = lords[3]
                    if get_next_lord(next_next_lord) == next_next_next_lord:
                        if length > 4:
                            mahadasha_lord = lords[4]
                            if get_next_lord(next_next_next_lord) == mahadasha_lord:
                                mahadasha_lord = get_next_lord(mahadasha_lord)
                                lords[0] = lords[1] = lords[2] = lords[3] = lords[4] = mahadasha_lord
                            else:
                                next_next_next_lord = get_next_lord(next_next_next_lord)
                                lords[0] = lords[1] = lords[2] = lords[3] = next_next_next_lord
                    else:
                        next_next_lord = get_next_lord(next_next_lord)
                        lords[0] = lords[1] = lords[2] = next_next_lord
            else:
                next_lord = get_next_lord(next_lord)
                first_lord = next_lord
                lords[0] = lords[1] = next_lord
        else:
            next_lord = get_next_lord(next_lord)
            lords[0] = lords[1] = next_lord
    else:
        lords[0]=get_next_lord(lords[0])

    return list(lords.__reversed__())

def print_current_vdasha(context,yrlen,levels):
    """
    print information on current vimshottari dasha
    levels is a list of levels, e.g., [1,2,3]
    it will print the information for all these levels
    """
    print("\n\nCurrent Vimshottari Dasha\n")

    # this is for the year length
    yrstr=""
    for key,value in const.dasha_years.items():
        if yrlen == key:
            yrlen = const.dasha_years[key]
            yrstr = key.capitalize()

    planet = Moon(context)
    now = JulianDay("now")

    print(f"Based on the position of {planet.name()}")
    print(f"Using {planet.ayanamsa_name()}")
    print(f"Using {yrstr} year length\n")

    levels = [x for x in range(1,levels+1)]
    
    for level in levels:
        current_dasha = current_vimshottari_dasha(planet,now,level,yrlen)
        next_dasha_startsJD = current_dasha.pop()

        print(f"Current dasha: {utils.mk_dasha_lord(current_dasha)}")
        print(f"Next dasha: {utils.mk_dasha_lord(next_dasha_lords(current_dasha))}, starts at:")
        print(f"{next_dasha_startsJD}")
        print(f"in {utils.dec2ymd((next_dasha_startsJD.jd_number()-now.jd_number())/365.2422)}\n")
    return
