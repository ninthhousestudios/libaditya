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

import toml

from libaditya.objects import JulianDay, Location
from libaditya import read

def new_chart_interactive(outfile=None):
    """
    take user input and write out a new chart

    name: str (optional)
    date: MM/DD/YYYY
    hour: (HH:MM(:SS)) (UTC)
    utcoffset: float
    lat: N is positive
    long: E is positive
        three formats: 1) decimal
                       2) DD:MM(:SS)
                       3) 0DD(E/W)MM'SS(.SS)
                       3) DD(N/S)MM'SS(.SS)
    alt: float - meters
    placename: str (optional)
    """
    name = input("Name: ")
    date = input("Date (MM/DD/YYYY): ")
    hour = input("Hour (HH:MM(:SS)) (UTC): ")
    utcoffset = float(input("UTC offset: "))
    # lat and long are floats
    lat = read.parse_position_argument(input("Latitude (N is positive): "))
    long = read.parse_position_argument(input("Longitude (E is positive): "))
    alt = float(input("Altitude (meters): "))
    placename = input("Placename (optional): ")

    # name, placename, month, day, year, timedec, lat, long, utcoffset
    month, day, year = read.intize_date(date)
    timedec = read.intize_time(hour)
    timeJD = JulianDay((year,month,day,timedec),utcoffset)
    location = Location(lat, long, alt, placename, timeJD.mktimezone())
    d=dict()
    d["name"] = name.split(".")
    d["timeJD"] = dict()
    d["timeJD"]["jd"]=timeJD.jd_number()
    d["timeJD"]["utcoffset"]=timeJD.utcoffset
    d["location"]=location.__dict__

    if outfile is not None:
        # split in case they put extension on there
        name=outfile.split(".")
    with open(f"{name.lower().replace(' ','-')}.toml", "w") as fd:
        toml.dump(d,fd)
    return
