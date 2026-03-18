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

def varga_deities(deities):
    """
    takes a list of dignites from Planets.deities and output a string form
    """
    ret = ""
    for n in range(0,9):
        ret += f"{const.graha_glyphs[n]} :  {deities[n]}\n"
    ret += f"Lg :  {deities[9]}\n"
    return ret

def print_varga_deities(deities):
    print(varga_deities(deities))

def parashara_aspect_table_planets(aspects):
    """
    aspects is a list of lists, i.e., a list of rows returned by Planets.parashara_aspects
    make a prettytable list of these values
    """
    output = PrettyTable()
    output.field_names = [" "] + [glyph for glyph in const.graha_glyphs]
    output.align[" "] = "l"

    for n,row in enumerate(aspects):
        output.add_row(*[[const.karaka_glyphs[n]] + row]) 
        output.add_divider()

    ret = output.get_string(fields=[" "] + [glyph for glyph in const.graha_glyphs])

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

def print_jaimini_karakas(karakas):
    print(jaimini_karakas_str(karakas))

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

def print_jaimini_aspects(chart):
    """
    print all effective rashi aspects for this chart
    """
    print(f"Rashi aspects ({chart.context.rashi_aspects})")

    s = chart.rashi().signs()
    for sign in s:
        print(f"\n{sign.name()}")
        aspected = s.rashi_aspects_given_by(sign)
        aspecting = s.rashi_aspects_given_to(sign)
        for ap in aspected:
            print(f"{sign.name()} -> {ap.name()}")
        for ap in aspecting:
            print(f"{sign.name()} <- {ap.name()}")

def print_jaimini_spiritual_planets(splanets):
    """
    prints infomration returned by Rashi.get_spiritual_planets
    """
    vargas = ["1","9","24","-24","-240"]
    print("Spiritual planets:")

    for varga in splanets.keys():
        if not varga in vargas:
            continue
        print(f"d{varga}:")
        print("Conjunctions")
        for planet in splanets[varga]["conjunction"][0]:
            # planets that are conjunct
            print(f"\t{planet}")
        print("Aspecting")
        for sign in splanets[varga]["aspecting"]:
            for planet in sign:
                print(f"\t{planet}")

def print_visible_times(times):
    """
    takes a list of three JulianDay classes
    0 - start of visibility
    1 - optimum visibility
    2 - end of visibility
    """
    print("Start of visibility:")
    print(times[0])
    print("Optimum visibility:")
    print(times[1])
    print("End of visibility:")
    print(times[2])

def lajjitaadi_avasthas_table(avasthas) -> str:
    """
    Takes the dict returned by Rashi.lajjitaadi_avasthas() and returns
    a PrettyTable string.
    """
    output = PrettyTable()
    output.field_names = ["Planet", "Avastha", "Source", "Details", "Strength"]
    output.align["Planet"] = "l"
    output.align["Avastha"] = "l"
    output.align["Source"] = "l"
    output.align["Details"] = "l"
    output.align["Strength"] = "r"

    for planet_name, planet_avasthas in avasthas.items():
        for avastha_name, factors in planet_avasthas.items():
            for factor in factors:
                source = factor.get("source", "")
                strength = factor.get("strength", "")
                details = ""
                if "planet" in factor:
                    details = factor["planet"]
                elif "lord" in factor:
                    details = f"lord: {factor['lord']}"
                elif "dignity" in factor:
                    details = factor["dignity"]
                elif "detail" in factor:
                    details = factor["detail"]
                output.add_row([planet_name, avastha_name.capitalize(), source, details, strength])

    return output.get_string()

def print_lajjitaadi_avasthas(avasthas):
    print(lajjitaadi_avasthas_table(avasthas))


AVASTHA_PLANET_ORDER = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]

def avasthas_table(lajjitaadi, baladi, jagradadi, deeptadi, shayanadi) -> str:
    # simple avasthas table
    simple = PrettyTable()
    simple.field_names = ["Planet", "Baladi", "Jagradadi", "Deeptadi", "Shayanadi"]
    simple.align = "l"
    for name in AVASTHA_PLANET_ORDER:
        simple.add_row([name,
                        baladi.get(name, ""),
                        jagradadi.get(name, ""),
                        deeptadi.get(name, ""),
                        shayanadi.get(name, "")])

    # lajjitaadi table
    lajj = lajjitaadi_avasthas_table(lajjitaadi)

    # lajjitaadi interaction sentences
    verbs = {"delighted": "delighting", "starved": "starving", "agitated": "agitating",
             "thirsty": "thirsting", "shamed": "shaming"}
    adjectives = {"healthy": "secure", "proud": "proud"}
    interactions = PrettyTable()
    interactions.field_names = ["Interaction"]
    interactions.align = "l"
    for planet_name, planet_avasthas in lajjitaadi.items():
        for avastha_name, factors in planet_avasthas.items():
            if avastha_name in adjectives:
                interactions.add_row([f"{planet_name} is {adjectives[avastha_name]}"])
                continue
            verb = verbs.get(avastha_name)
            if not verb:
                continue
            for factor in factors:
                if "planet" in factor:
                    interactions.add_row([f"{factor['planet']} is {verb} {planet_name}"])

    return simple.get_string() + "\n\nLajjitaadi Avasthas\n" + lajj + "\n\n" + interactions.get_string()

def print_avasthas(lajjitaadi, baladi, jagradadi, deeptadi, shayanadi):
    print(avasthas_table(lajjitaadi, baladi, jagradadi, deeptadi, shayanadi))


def akriti_yogas_table(akritis) -> str:
    """
    Takes the list of AkritiYoga dataclasses returned by Rashi.akriti_yogas()
    and returns a PrettyTable string, sorted by to_move ascending.
    """
    output = PrettyTable()
    output.field_names = ["Yoga", "Translation", "To Move", "Houses"]
    output.align["Yoga"] = "l"
    output.align["Translation"] = "l"
    output.align["To Move"] = "r"
    output.align["Houses"] = "l"
    for y in akritis:
        houses_str = ", ".join(str(h) for h in y.houses)
        output.add_row([y.name, y.translation, y.to_move, houses_str])
    return output.get_string()

def print_akriti_yogas(akritis):
    print(akriti_yogas_table(akritis))

def rich_akriti_yogas_table(akritis):
    """
    Takes the list of AkritiYoga dataclasses returned by Rashi.akriti_yogas()
    and returns a Rich Table renderable, sorted by to_move ascending.
    """
    from rich.table import Table
    from rich.text import Text

    output = Table(title="Akriti Yogas", box=None)
    output.add_column("Yoga", style="bold", justify="left")
    output.add_column("Translation", justify="left")
    output.add_column("To Move", justify="right")
    output.add_column("Houses", justify="left")

    for y in akritis:
        houses_str = ", ".join(str(h) for h in y.houses)
        tm = y.to_move
        if tm <= 2:
            style = "bold green"
        elif tm <= 4:
            style = "green"
        elif tm <= 5:
            style = ""
        else:
            style = "dim"
        output.add_row(
            Text(y.name, style=style),
            Text(y.translation, style=style),
            Text(str(tm), style=style),
            Text(houses_str, style=style),
        )
    return output

def rich_akriti_yogas(akritis):
    from rich.console import Console
    Console().print(rich_akriti_yogas_table(akritis))


def nabhasa_yogas_table(yogas) -> str:
    """
    Takes the list returned by Rashi.nabhasa_yogas() (or ashraya/dala/sankhya)
    and returns a PrettyTable string, sorted by to_move ascending.
    """
    output = PrettyTable()
    output.field_names = ["Yoga", "Translation", "Category", "To Move", "Condition"]
    output.align["Yoga"] = "l"
    output.align["Translation"] = "l"
    output.align["Category"] = "l"
    output.align["To Move"] = "r"
    output.align["Condition"] = "l"
    for y in yogas:
        cat = getattr(y, 'category', 'Akriti')
        cond = getattr(y, 'condition', None) or ", ".join(str(h) for h in y.houses)
        output.add_row([y.name, y.translation, cat, y.to_move, cond])
    return output.get_string()

def print_nabhasa_yogas(yogas):
    print(nabhasa_yogas_table(yogas))

def rich_nabhasa_yogas_table(yogas):
    """
    Takes the list returned by Rashi.nabhasa_yogas() (or ashraya/dala/sankhya)
    and returns a Rich Table renderable, sorted by to_move ascending.
    """
    from rich.table import Table
    from rich.text import Text

    output = Table(title="Nabhasa Yogas", box=None)
    output.add_column("Yoga", style="bold", justify="left")
    output.add_column("Translation", justify="left")
    output.add_column("Category", justify="left")
    output.add_column("To Move", justify="right")
    output.add_column("Condition", justify="left")

    for y in yogas:
        cat = getattr(y, 'category', 'Akriti')
        cond = getattr(y, 'condition', None) or ", ".join(str(h) for h in y.houses)
        tm = y.to_move
        if tm <= 2:
            style = "bold green"
        elif tm <= 4:
            style = "green"
        elif tm <= 5:
            style = ""
        else:
            style = "dim"
        output.add_row(
            Text(y.name, style=style),
            Text(y.translation, style=style),
            Text(cat, style=style),
            Text(str(tm), style=style),
            Text(cond, style=style),
        )
    return output

def rich_nabhasa_yogas(yogas):
    from rich.console import Console
    Console().print(rich_nabhasa_yogas_table(yogas))


def mahapurusha_yogas_table(yogas) -> str:
    output = PrettyTable()
    output.field_names = ["Yoga", "Translation", "Planet", "Present", "House", "Dignity"]
    output.align["Yoga"] = "l"
    output.align["Translation"] = "l"
    output.align["Planet"] = "l"
    output.align["Present"] = "c"
    output.align["House"] = "r"
    output.align["Dignity"] = "l"
    for y in yogas:
        output.add_row([y.name, y.translation, y.planet,
                        "Yes" if y.present else "No", y.house, y.dignity])
    return output.get_string()

def print_mahapurusha_yogas(yogas):
    print(mahapurusha_yogas_table(yogas))

def rich_mahapurusha_yogas_table(yogas):
    from rich.table import Table
    from rich.text import Text

    output = Table(title="Panchamahapurusha Yogas", box=None)
    output.add_column("Yoga", style="bold", justify="left")
    output.add_column("Translation", justify="left")
    output.add_column("Planet", justify="left")
    output.add_column("Present", justify="center")
    output.add_column("House", justify="right")
    output.add_column("Dignity", justify="left")

    for y in yogas:
        style = "bold green" if y.present else "dim"
        output.add_row(
            Text(y.name, style=style),
            Text(y.translation, style=style),
            Text(y.planet, style=style),
            Text("Yes" if y.present else "No", style=style),
            Text(str(y.house), style=style),
            Text(y.dignity, style=style),
        )
    return output

def rich_mahapurusha_yogas(yogas):
    from rich.console import Console
    Console().print(rich_mahapurusha_yogas_table(yogas))


def solar_yogas_table(yogas) -> str:
    output = PrettyTable()
    output.field_names = ["Yoga", "Present", "Planets"]
    output.align["Yoga"] = "l"
    output.align["Present"] = "c"
    output.align["Planets"] = "l"
    for y in yogas:
        output.add_row([y.name, "Yes" if y.present else "No",
                        ", ".join(y.planets) if y.planets else "—"])
    return output.get_string()

def print_solar_yogas(yogas):
    print(solar_yogas_table(yogas))

def rich_solar_yogas_table(yogas):
    from rich.table import Table
    from rich.text import Text

    output = Table(title="Solar Yogas", box=None)
    output.add_column("Yoga", style="bold", justify="left")
    output.add_column("Present", justify="center")
    output.add_column("Planets", justify="left")

    for y in yogas:
        style = "bold green" if y.present else "dim"
        planets_str = ", ".join(y.planets) if y.planets else "—"
        output.add_row(
            Text(y.name, style=style),
            Text("Yes" if y.present else "No", style=style),
            Text(planets_str, style=style),
        )
    return output

def rich_solar_yogas(yogas):
    from rich.console import Console
    Console().print(rich_solar_yogas_table(yogas))


def lunar_yogas_table(yogas) -> str:
    output = PrettyTable()
    output.field_names = ["Yoga", "Present", "Planets"]
    output.align["Yoga"] = "l"
    output.align["Present"] = "c"
    output.align["Planets"] = "l"
    for y in yogas:
        output.add_row([y.name, "Yes" if y.present else "No",
                        ", ".join(y.planets) if y.planets else "—"])
    return output.get_string()

def print_lunar_yogas(yogas):
    print(lunar_yogas_table(yogas))

def rich_lunar_yogas_table(yogas):
    from rich.table import Table
    from rich.text import Text

    output = Table(title="Lunar Yogas", box=None)
    output.add_column("Yoga", style="bold", justify="left")
    output.add_column("Present", justify="center")
    output.add_column("Planets", justify="left")

    for y in yogas:
        style = "bold green" if y.present else "dim"
        planets_str = ", ".join(y.planets) if y.planets else "—"
        output.add_row(
            Text(y.name, style=style),
            Text("Yes" if y.present else "No", style=style),
            Text(planets_str, style=style),
        )
    return output

def rich_lunar_yogas(yogas):
    from rich.console import Console
    Console().print(rich_lunar_yogas_table(yogas))


from libaditya.cards import cards_constants as cardsc
cards=cardsc.cards

def print_cot_quadration(pquad):
    """Print a quadration"""
    # remember that lists are indexed starting with 0
    print('        {}  {}  {}      '.format(cards[pquad[51]], cards[pquad[50]], cards[pquad[49]]))
    print('{}  {}  {}  {}  {}  {}  {}'.format(cards[pquad[6]], cards[pquad[5]], cards[pquad[4]],
                                        cards[pquad[3]], cards[pquad[2]], cards[pquad[1]], cards[pquad[0]]))
    print('{}  {}  {}  {}  {}  {}  {}'.format(cards[pquad[13]], cards[pquad[12]], cards[pquad[11]], cards[pquad[10]],
                                        cards[pquad[9]], cards[pquad[8]], cards[pquad[7]]))
    print('{}  {}  {}  {}  {}  {}  {}'.format(cards[pquad[20]], cards[pquad[19]], cards[pquad[18]], cards[pquad[17]],
                                        cards[pquad[16]], cards[pquad[15]], cards[pquad[14]]))
    print('{}  {}  {}  {}  {}  {}  {}'.format(cards[pquad[27]], cards[pquad[26]], cards[pquad[25]], cards[pquad[24]],
                                        cards[pquad[23]], cards[pquad[22]], cards[pquad[21]]))
    print('{}  {}  {}  {}  {}  {}  {}'.format(cards[pquad[34]], cards[pquad[33]], cards[pquad[32]],
                                        cards[pquad[31]], cards[pquad[30]], cards[pquad[29]], cards[pquad[28]]))
    print('{}  {}  {}  {}  {}  {}  {}'.format(cards[pquad[41]], cards[pquad[40]], cards[pquad[39]], cards[pquad[38]],
                                        cards[pquad[37]], cards[pquad[36]], cards[pquad[35]]))
    print('{}  {}  {}  {}  {}  {}  {}'.format(cards[pquad[48]], cards[pquad[47]], cards[pquad[46]], cards[pquad[45]],
                                        cards[pquad[44]], cards[pquad[43]], cards[pquad[42]]))

def print_cot_basic_spread(bspread):
    """print a birth spread"""
    print('         {}         '.format(cards[bspread[0]]))
    print('{} {} {} {} {} {} {}'.format(cards[bspread[7]],cards[bspread[6]],
                                        cards[bspread[5]],cards[bspread[4]],cards[bspread[3]],
                                        cards[bspread[2]],cards[bspread[1]]))
    print('      {}    {}      '.format(cards[bspread[9]],cards[bspread[8]]))
    print('         {}         '.format(cards[bspread[10]]))
    print('      {} {} {}      '.format(cards[bspread[13]],cards[bspread[12]],cards[bspread[11]]))
