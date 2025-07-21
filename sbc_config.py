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

def init_chart_config(file=sc.config_base):
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
