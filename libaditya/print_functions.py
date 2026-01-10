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

"""
a variety of functions to return string forms of various information
that can be computed with libaditya
"""

from prettytable import PrettyTable

from libaditya import constants as const
from libaditya.objects import Planet, Sign


def dignity_table(dignities):
    """
    takes a list of dignites from Planets.dignities and output a string form
    """
    ret = ""
    for n in range(0,len(dignities)):
        ret += f"{const.karaka_glyphs[n]} :  {dignities[n]}\n"
    # slice removes last \n
    return ret[:-1]

def print_dignity_table(dignites):
    print(dignity_table(dignites))

def parashara_aspect_table_planets(aspects):
    """
    aspects is a list of lists, i.e., a list of rows returned by Planets.parashara_aspects
    make a prettytable list of these values
    """
    output = PrettyTable()
    output.field_names = [" "] + [glyph for glyph in const.grahas_glyphs]
    output.align[" "] = "l"

    for n,row in enumerate(aspects):
        output.add_row(*[[const.karaka_glyphs[n]] + row]) 
        output.add_divider()

    ret = output.get_string(fields=[" "] + [glyph for glyph in const.grahas_glyphs])

    return ret

def parashara_aspect_table_cusps(aspects):
    """
    aspects is a list of lists, i.e., a list of rows returned by Planets.parashara_aspects
    make a prettytable list of these values
    """
    output = PrettyTable()
    output.field_names = [" "] + [str(n) for n in range(1,13)]
    output.align[" "] = "l"

    for n,row in enumerate(aspects):
        output.add_row(*[[const.karaka_glyphs[n]] + row]) 
        output.add_divider()

    return output.get_string(fields=[" "] + [str(n) for n in range(1,13)])

def jaimini_karakas_str(karakas) -> str:
    """
    return a PrettyTable string displaying the Jaimini karakas in karakas
    karakas is a list of Planet classes, with ak being element 0, amk element 1, etc.
    """
    output = PrettyTable()
    output.field_names = ["AK", "AmK", "BK", "MK/PuK", "PiK", "GK", "DK"]

    # this table only has a header and one row
    output.add_row([planet.glyph() for planet in karakas])

    return output.get_string(fields=["AK", "AmK", "BK", "MK/PuK", "PiK", "GK", "DK"])

def print_padas(padas):
    """
    receive a dictionary of all the padas
    key is the sign number, value is the Sign of the pada
    """
    for sign,pada in padas.items():
        print(f"{sign.sign_name()} pada: {pada.sign_name()}") 

def print_jaimini_first_strength(fs: [int]) -> None:
    """
    print jaiminis first strength
    """
    for n,s in enumerate(fs):
        print(f"{n+1}\t{s.glyph()} {s.sign()}")

def print_jaimini_second_strength(ssd: {Sign: [Planet]}) -> None:
    """
    print jaiminis second strength
    """
    for sign, strengths in ssd.items():
        fstr = ""
        fstr += f"({sign.sign()}) {sign.glyph()}\t"
        for strength in strengths:
            # strengh is a Planet class
            fstr+=f" {strength.abbreviation()} "
        print(fstr) 

def print_jaimini_argala(result: [Planet]):
    """
    result is a list of Planet-s returned by Varga().argala()
    the result of argala to one specific house
    Rashi().argala() returns the results of argala to the signs of the lagna and 7th cusp; not currently printed by this function

    result[0] = planets forming argala
    result[1] = malefics forming malefic argala to the 3rd
    result[2] = planets having their argala obstructed
    """
    print(f"argala to the rashi:")
    for planet in result[0]:
        print(planet.identity())
    print(f"\nmalefics causing argala from/to the third:")
    for planet in result[1]:
        print(planet.identity())
    print(f"\nobstructed planets from the rashi:")
    for planet in result[2]:
        print(planet.identity())
