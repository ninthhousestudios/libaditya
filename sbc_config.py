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
sbc_config.py

functions to read and write configuration files for sbc.py

read chart-template.sbc to get all the possible fields
store in a dictionary
return

then read a config and check against that config
then write a config
"""

import sbc_constants as sc
import pyphread as pread

def init_config(file=sc.config_base):
    input = open(file,'r')
    
    config = {} # empty dictionary

    for line in input:
       if not "=" in line or line.startswith('#'):
           continue # either a comment or not a variable if line doesnt have =
       field, value = line.split("=")
       field = field.strip().lower()
       value = value.strip()
       config[field]=value 
    input.close()
    return config

def init_chart_config(file):
    """
    initialize the dictionary for a chart
    includes birth info, transit info, theme and other options
    """
    input = open(file,'r')
    
    config = init_config() # empty dictionary

    for line in input:
       if not "=" in line or line.startswith('#'):
           continue # either a comment or not a variable if line doesnt have =
       field, value = line.split("=")
       field = field.strip().lower()
       value = value.strip()
       config[field]=value 
    input.close()
    return config

# user passed a chtk file, so deal with it
def init_chtk_config(file):
    name, placename, month, day, year, ephclock, lat, long = pread.read_chtk(file)

    config = init_config()

    config["name"]=name
    config["date"]=f"{month:02d}/{day:02d}/{year:04d}"
    config["place"]=placename
    config["time"]=pread.dec2dms(ephclock)
    config["lat"]=lat
    config["long"]=long
    config["tplace"]=placename
    config["tdate"]="now"
    config["ttime"]="now"
    config["tlat"]=lat
    config["tlong"]=long

    return config
