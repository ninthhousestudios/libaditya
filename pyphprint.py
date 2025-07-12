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
    Rahu at index 10, Ketu at index 11
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


def print_Cusps_nakshatras(ayanamsa=pglob.ayanamsa, loc=Location(), tjd=JulianDay()):
    theCusps = Cusps(pglob.hsys, loc, tjd)
    theCusps.init_cusps()
    output = PrettyTable(["Cusp", "Nakshatra"])
    output.align["Cusp"] = "r"
    output.align["Nakshatra"] = "l"

    cusps_nakshatras = theCusps.cusps_nakshatras(ayanamsa)

    for i in range(12):
        output.add_row([i + 1, cusps_nakshatras[i]])

    print(f"\nHouse Cusps nakshatras\nwith house system {theCusps.house_name()}")
    if pglob.ayanamsa == 98:
        print("using Dhruva GC mid-Mula equatorial ayanamsa")
    elif pglob.ayanamsa == 99:
        print("using Dhruva GC mid-Mula ecliptic coordinates ayanamsa")
    elif pglob.ayanamsa == 100:
        print("using tropical krittika at ascedening equinx with 28 equal nakshatras")
    else:
        print(f"using {swe.get_ayanamsa_name(ayanamsa)} ayanamsa")
    print(f"Location: {loc.place()}")
    print(f"Time: {tjd}")
    print(output)


def print_planets_nakshatras(tjd=JulianDay(), ayanamsa=pglob.ayanamsa):
    print("\nNakshatras of the planets:")
    print(tjd)
    if ayanamsa == 98:
        print("Dhruva GC mid-Mula equatorial coordinates ayanamsa")
    elif ayanamsa == 99:
        print("Dhruva GC mid-Mula ecliptic coordinates ayanamsa")
    elif ayanamsa == 100:
        print("Tropical Krittika at ascending equinox; 28 equal nakshatras")
    else:
        print(f"{swe.get_ayanamsa_name(ayanamsa)} ayanamsa")
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

    return output.get_string()


def print_panchanga(panch=Panchanga()):
    print("\nPanchanga")
    print(panch)

    print(f"\nAbsolute tithi: {panch.tithi()}")
    if panch.tithi() > 15:
        print(f"Relative tithi: {panch.tithi() - 15}")
    print(f"Type: {panch.tithi_type()}")

    print(f"Karana: {panch.karana()}")
    print(f"Vara: {panch.vara()}")
    print(f"Nakshatra: {panch.nakshatra()}")
    print(f"Yoga: {panch.yoga()}")


def print_panchanga_addendum(panch=Panchanga(), loc=Location()):
    print("\nPanchanga addendum")

    dmsun = panch.sun.daily_motion()
    dmmoon = panch.moon.daily_motion()

    # tithi
    telapsed = round(panch.tithi_degrees_elapsed(), 2)
    tremaining = round(panch.tithi_degrees_remaining(), 2)

    print(f"\nTithi: {panch.tithi()}")
    print("Elapsed: ", telapsed, " degrees (", round((telapsed / 12) * 100, 2), "%)")
    print(
        "Remaining: ", tremaining, " degree (", round((tremaining / 12) * 100, 2), "%)"
    )

    hours_left = ((tremaining) / (dmmoon - dmsun)) * 24
    end_time = panch.shift("f", "hour", hours_left)

    print(
        f"Ending time of current tithi: {round(hours_left, 2)} hours from panchanga time, at\n{end_time.timedate()}\n{end_time.usrtimedate()}"
    )

    # vara
    print(
        f"\nSunrise {panch.date()} at {loc.place()}:\n{panch.sun.riseset(swe.CALC_RISE, loc)}\n"
    )
    print(
        f"Sunset {panch.date()} at {loc.place()}:\n{panch.sun.riseset(swe.CALC_SET, loc)}\n"
    )

    hrsnxtvara = ((panch.sun.sunrise_yamakoti().jd - panch.jd) / pglob.onehrjd) % 24
    nxtvara = panch.shift("f", "hour", hrsnxtvara)
    print(
        f"Next vara begins: {putil.time2str(putil.dec2dms(hrsnxtvara))} hours from panchanga time\nat {nxtvara.timedate()}\n   {nxtvara.usrtimedate()}"
    )

    # give moonrise for three days, the one before, this one, and the one after
    # yesterpanch = Panchanga(panch.shift("b", "day", 1))
    # morrowpanch = Panchanga(panch.shift("f", "day", 1))
    print(
        f"\nMoonrise {panch.date()} at {loc.place()}: \n{panch.moon.riseset(swe.CALC_RISE, loc)}"
    )
    print(
        f"\nMoonset {panch.date()} at {loc.place()}: \n{panch.moon.riseset(swe.CALC_SET, loc)}"
    )
    # nakshatra
    ninfo = panch.moon.nakshatra_table_list(pglob.ayanamsa)
    print(f"\nNakshatra: {ninfo[1]}")
    print(f"Elapsed: {ninfo[2]}")
    degremain = pglob.nak - float(ninfo[2].split(" ")[0])
    print(
        f"Remaining: {round(degremain, 2)} deg ({round((degremain / pglob.nak) * 100, 2)} %)"
    )
    hours_left = (degremain / dmmoon) * 24
    end_time = panch.shift("f", "hour", hours_left)
    print(
        f"Ending time of current nakshatra: {round(hours_left, 2)} hours from panchanga time, at\n{end_time.timedate()}\n{end_time.usrtimedate()}"
    )

    # yoga
    yelapsed = round(panch.yoga_degrees_elapsed(), 2)
    yremaining = round(panch.yoga_degrees_remaining(), 2)

    print(f"\nYoga: {panch.yoga()}")
    print("Elapsed: ", yelapsed, " degrees (", round((yelapsed / 12) * 100, 2), "%)")
    print(
        "Remaining: ", yremaining, " degree (", round((yremaining / 12) * 100, 2), "%)"
    )

    hours_left = ((yremaining) / (dmmoon - dmsun)) * 24
    end_time = panch.shift("f", "hour", hours_left)

    print(
        f"Ending time of current yoga: {round(hours_left, 2)} hours from panchanga time, at\n{end_time.timedate()}\n{end_time.usrtimedate()}"
    )


def print_next_new_moon(panch=Panchanga()):
    next = panch.next_new_moon()  # return the Panchanga of the next new moon
    print("\nNext new moon at:")
    print(next)
    print(f"At: {next.moon.signize()}")
    print(f"Nakshatra: {next.moon.nakshatra()}")


def print_next_full_moon(panch=Panchanga()):
    next = panch.next_full_moon()  # return the Panchanga of the next full moon
    print("\nNext full moon at:")
    print(next)
    print(f"At: {next.moon.signize()}")
    print(f"Nakshatra: {next.moon.nakshatra()}")


def print_dhruva_equ_ecl():
    eo = putil.ecliptic_obliquity(JulianDay().year())
    nak = pglob.nak
    output = PrettyTable(["Equatorial", "Ecliptic"])
    thisrow = []
    for i in range(27):
        thisrow.append(round(nak * i, 3))
        thisrow.append(round(swe.cotrans((i * nak, 0, 1), eo)[0], 3))
        output.add_row(thisrow)
        thisrow = []

    print(output)
