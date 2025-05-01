import swisseph as swe
import pyphglobals as pglob
import pyphutils as putil
from pyphclasses import *
from pyphobjs import *
from prettytable import PrettyTable

# printing functions for pyphemeris


def init_Planets(tjd=JulianDay()):
    """
    return a list of Planet classes, one for each
    Sun,Moon,Mercury,Venus,Mars,Jupiter,Saturn,Uranus,Neptune,Pluto (indexes 0-9)
    Rahu at index 11, Ketu at index 10
    Earth at index 12
    """
    planets = []
    for i in range(10):
        planets.append(Planet(i, tjd))  # Planet takes a JulianDay class, tjd
    planets.append(Rahu(tjd))
    planets.append(Ketu(tjd))
    # must use swe.EARTH=14, if changed will given wrong results
    # plgob.earth is 12 since it indexes
    planets.append(Planet(swe.EARTH, tjd))
    return planets


def print_planets(tjd=JulianDay(), sysflg=0):
    if sysflg == pglob.ECL:
        print(f"\nEcliptic coordinates")
    if sysflg == pglob.EQU:
        print(f"\nEquatorial coordinates")
    if sysflg == pglob.HELIO:
        print(f"\nHeliocentric coordinates")
    if sysflg == pglob.BARY:
        print(f"\nBarycentric coordinates")
    print(tjd)
    print(planets_str(tjd, sysflg))


# get a PrettyTable string to print
def planets_str(tjd=JulianDay(), sysflg=0):
    """
    return a PrettyTable string with coordinates for all planets on julianday
    using sysflag coordinates
    """
    Planets = init_Planets(tjd)
    output = PrettyTable()
    output.field_names = [
        "Planet",
        "Longitude",
        "Latitude",
        "Distance",
        "Speed",
        "Latitude Speed",
        "Distance Speed",
    ]
    output.align["Planet"] = "l"
    output.align["Longitude"] = "l"
    output.align["Latitude"] = "r"
    output.align["Speed"] = "r"
    # doing it this way so I can add Earth after Venus for helio and bary coords
    # get coordinates for Sun through Pluto, 10 planets
    for i in range(10):
        if (
            i == 0 and sysflg == pglob.HELIO
        ):  # dont print sun if heliocentric coordinates
            continue
        output.add_row(Planets[i].table_list(sysflg))

    # if getting ECL or EQU, add Rahu and Ketu
    if sysflg == pglob.ECL or sysflg == pglob.EQU:
        # output.add_row(Planets[pglob.rahu].table_list(sysflg))
        # ketuls = Planets[pglob.ketu].table_list(sysflg)
        # ketuls[1] = pglob.sign_func((Planets[pglob.rahu].coords[0] - 180) % 360)
        # output.add_row(ketuls)
        output.add_row(Planets[10].table_list(sysflg))
        output.add_row(Planets[11].table_list(sysflg))

    # if helio or bary coordinates, dont add rahu or ketu but add earth
    if sysflg == pglob.HELIO or sysflg == pglob.BARY:
        output.add_row(Planets[pglob.earth].table_list(sysflg))

    ret = output.get_string(fields=["Planet", "Longitude", "Latitude", "Speed"])

    return ret


def print_Cusps(loc=Location(), tjd=JulianDay()):
    theCusps = Cusps(pglob.hsys, loc, tjd)
    theCusps.init_cusps()
    output = PrettyTable(["Cusp", "Longitude"])
    output.align["Cusp"] = "r"
    output.align["Longitude"] = "l"

    for i in range(12):
        output.add_row([i + 1, pglob.sign_func(pglob.round_func(theCusps.cusps[i]))])

    print(f"\nHouse Cusps with house system {theCusps.house_name()}\n")
    print(f"Location: {loc.place()}")
    print(f"Time: {tjd}")
    print(output)


def print_planets_nakshatras(tjd=JulianDay(), ayanamsa=pglob.ayanamsa):
    print("\nNakshatras of the planets:")
    print(tjd)
    print(f"Got #{ayanamsa}: {swe.get_ayanamsa_name(ayanamsa)}")
    print(pnakshatra_str(tjd, ayanamsa))


def pnakshatra_str(tjd=JulianDay(), ayanamsa=pglob.ayanamsa):
    planets = init_Planets(tjd)
    output = PrettyTable()
    output.field_names = ["Planet", "Nakshatra", "Percent Elapsed"]
    output.align["Planet"] = "l"
    output.align["Nakshatra"] = "l"
    output.align["Percent Elapsed"] = "r"

    for i in range(10):
        output.add_row(planets[i].nakshatra_table_list(ayanamsa))

    output.add_row(planets[10].nakshatra_table_list(ayanamsa))
    output.add_row(planets[11].nakshatra_table_list(ayanamsa))
    # ketulong = (planets[pglob.rahu].sidlong - 180) % 360
    # output.add_row(planets[pglob.rahu].nakshatra_table_list())
    # ketunindex = putil.nakshatra_index(ketulong)
    # output.add_row(
    #    list(
    #        (
    #            "Ketu",
    #            pglob.nakshatra[ketunindex],
    #            round(((ketulong - ketunindex * pglob.nak) / pglob.nak) * 100, 2),
    #        )
    #    )
    # )

    return output.get_string()
