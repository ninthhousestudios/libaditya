import swisseph as swe
import pyphglobals as pglob

"""
module of utility functions for pyphemeris
"""


def sign_index(long):
    return int(long / 30)


def nakshatra_index(sidlong, n=0):
    """
    sidlong is the sidereal longitude of a planet
    finds the proper index for the nakshatra array
    n is the index since this is a recursive function;
    needs to be called with n=0 the first time
    """
    if (n * pglob.nak) <= sidlong and sidlong <= ((n + 1) * pglob.nak):
        return n
    else:
        return nakshatra_index(sidlong, n + 1)

def nakshatra_tropkrt28_index(long):
    return int((long/(360/28))%28)


def dhruvecl_index(sidlong, year=2025, n=0):
    """
    generate the nakshatra index for dhruva ecliptic
    with dhruva eclitpic, the nakshatra boundaries have been projected
    onto the eclitpic from the equator, so dhruva nakshatras are not
    equal on the ecliptic, thus we cant index with nakshatra_index,
    we need to actually build the index of where the nakshatras are,
    then we can find the right index
    """
    ecl_points = build_dhruvecl_boundaries(year)
    return dindex(sidlong, ecl_points, year, 0)


def dindex(sidlong, ecl_points, year=2025, n=0):
    # print(f"dindex n={n}")
    # print(f"sidlong = {sidlong}")
    # print(f"{ecl_points[n]} <= {sidlong} <= {ecl_points[n + 1]}")
    if ecl_points[n] <= sidlong and sidlong <= ecl_points[n + 1]:
        return n
    else:
        return dindex(sidlong, ecl_points, year, n + 1)


def build_dhruvecl_boundaries(year=2025):
    eo = ecliptic_obliquity(year)
    nak = pglob.nak
    ecl_points = []
    for i in range(27):
        ecl_points.append(swe.cotrans((i * nak, 0, 1), eo)[0])
    ecl_points.append(360)
    return ecl_points


def ketuize(long):
    """
    take rahus longitude and make it ketus
    """
    return (long - 180) % 360


def ecliptic_obliquity(year):
    return dms2dec((23, 27, 8.26)) - 0.4684 * (year - 1900)


def yessignize(long):
    """
    return a string with 360degree longitude long given with
    long (sign), with long being in the sign
    signs contains the signs to be used, which might be adityas
    """
    rasi = int(
        (long % 360) / 30
    )  # mod 360 in case long=360...but it probably wouldnt with swe, right?
    inlong = pglob.round_func(long - (rasi * 30), 4)
    return f"{dec2deg(inlong)} {pglob.signs[rasi]}"


def nosignize(long):
    """
    return the long which was passed
    user wants longitudes raw, so this function
    helps do that
    """
    return long


def yesround(long, nd=3):
    return round(long, nd)


def noround(long, nd=3):
    return long


def tmod_to_jd(now):
    """
    time a struct from the time module
    and convert it to julian day float
    """
    return swe.julday(
        now.tm_year,
        now.tm_mon,
        now.tm_mday,
        now.tm_hour + now.tm_min / 60 + now.tm_sec / 3600,
    )


def dec2dms(dd):
    """dd is a float that wants to be turned into degs,mins,secs; returns (deg,min,sec)"""
    dd = abs(dd)
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    return (degrees, minutes, seconds)


def dec2deg(dd):
    """
    take a decimal dd and return the equivalent DD:MM:SS as a string
    """
    dd = abs(dd)
    minutes, seconds = divmod(dd * 3600, 60)
    degrees, minutes = divmod(minutes, 60)
    return f"{round(degrees):02d}:{round(minutes):02d}:{round(seconds):02d}"


def dms2dec(dms):
    """
    dms is a tuple (hour,minutes,seconds) that wants to be turned into a float
    """
    return dms[0] + (dms[1] / 60) + (dms[2] / 3600)


def intize_date(date):
    """
    take a string 'MM/DD/YYYY'
    and return a tuple of int (mm,dd,yyyy)
    """
    year = int(date[6:10])
    month = int(date[0:2])
    day = int(date[3:5])

    return (month, day, year)


def intize_time(time):
    """
    take a string 'HH:MM:SS'
    and return a float of that time
    """
    return int(time[0:2]) + int(time[3:5]) / 60 + int(time[6:8]) / 3600


def date2str(date):
    """date is a revjul-tuple (year,month,day,hour); return a string 'month/day/year'"""
    return f"{date[1]:02d}/{date[2]:02d}/{date[0]:02d}"


def time2str(time):
    """time is a dec2dms tupel (deg,min,sec); returns a string 'HH:MM:SS'"""
    return f"{str(int(time[0])).zfill(2)}:{str(int(time[1])).zfill(2)}:{str(int(time[2])).zfill(2)}"
