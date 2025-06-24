#!/usr/bin/python

import argparse
import os
import codecs


def main():
    args = get_args()
    
    n=0
    fsize = os.path.getsize(args.file)
    input = open(args.file, "rb")
    lines = input.readlines()
    for line in lines:
        print(f"{n}: {line.decode(errors='ignore')}")
        match n:
            case 0:
                name = clean_line(line.decode(errors='ignore'))
            case 1:
                year = intize_line(codecs.decode(line))
            case 2:
                month = intize_line(codecs.decode(line))
            case 3:
                day = intize_line(codecs.decode(line))
            case 4:
                hour = intize_line(codecs.decode(line))
            case 5:
                min = intize_line(codecs.decode(line))
            case 6:
                sec = intize_line(codecs.decode(line))
            case 7:
                sex = intize_line(codecs.decode(line))
            case 8:
                country = clean_line(line.decode(errors='ignore'))
            case 9:
                city = clean_line(line.decode(errors='ignore'))
            case 10:
                long = long_to_float(clean_line(line.decode(errors='ignore')))
            case 11:
                lat = lat_to_float(clean_line(line.decode(errors='ignore')))
            case 12:
                h,m,s = clean_line(line.decode(errors='ignore')).split(":")
                utcoff = int(h)+(int(m)/60) + (int(s)/3600)
        n+=1
    input.close() 
    print(name)
    print(f"{month:02d}/{day:02d}/{year}")
    print(f"{hour:02d}:{min:02d}:{sec:02d}")
    print(f"{"male" if sex==1 else "female"}")
    print(country)
    print(city)
    print(f"(lat,long): ({lat},{long})")
    print(utcoff)

def lat_to_float(lat):
    """
    change kalas lat representation into a float
    """
    # string is like this 030E44'00
    if(lat[2:3] == 'N'):
        degs = int(lat[:2])
    else:
        degs = -int(lat[:2])
    mins = int(lat[3:5])
    secs = int(lat[6:8])
    return degs + (mins / 60) + (secs / 3600)

def long_to_float(lat):
    """
    change kalas long representation into a float
    """
    # string is like this 030E44'00
    if(lat[3:4] == 'E'):
        degs = int(lat[:3])
    else:
        degs = -int(lat[:3])
    mins = int(lat[4:6])
    secs = int(lat[7:9])
    return degs + (mins / 60) + (secs / 3600)

def intize_line(line):
    """
    line is a string (of decoded bytes)
    we remove all the space, etc. characters, then
    can return the integer of the string
    """
    nochars = ["\x00","\r","\n"]
    count = 0
    line=list(line)
    while count < len(line):
        if(line[count] in nochars):
            del line[count]
            continue
        count+=1
    retval = int(''.join(line))
    print(retval)
    return retval

def clean_line(line):
    """
    line is a string (of decoded bytes)
    we remove all the space, etc. characters, then
    can return the integer of the string
    """
    nochars = ["\x00","\r","\n"]
    count = 0
    line=list(line)
    while count < len(line):
        if(line[count] in nochars):
            del line[count]
            continue
        count+=1
    retval = ''.join(line)
    print(retval)
    return retval



def get_args():
    print("getting args")
    parser = argparse.ArgumentParser(
        prog="chtk2sbc",
        usage="%(prog)s [options]", 
        description=f"convert .chtk file .sbc format",
    )
    parser.add_argument("file", help=".chtk file to convert") 
    args = parser.parse_args()
    return args

main()
