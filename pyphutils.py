import swisseph as swe
import pyphglobals as pglob

"""
module of utility functions for pyphemeris
"""


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
    return f"{inlong} {pglob.signs[rasi]}"


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
    return f"{date[1]}/{date[2]}/{date[0]}"


def time2str(time):
    """time is a dec2dms tupel (deg,min,sec); returns a string 'HH:MM:SS'"""
    return f"{str(int(time[0])).zfill(2)}:{str(int(time[1])).zfill(2)}:{str(int(time[2])).zfill(2)}"
