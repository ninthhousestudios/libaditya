#!/usr/bin/python

import argparse
import os
import codecs


def main():
    args = get_args()
    
    for file in args.file:
        if(len(file.split('.')) == 1):
            # not a chtk file
            continue
        if file.split('.')[1].strip().lower() != "chtk":
            # not a chtk file
            continue
        linenum=0
        foutname = file.split('.')[0].strip().replace(' ','-').replace(',','').lower()
        input = open(file, "rb")
        print(f"converting {file}")
        lines = input.readlines()
        for line in lines:
            #print(f"{n}: {line.decode(errors='ignore')}")
            match linenum:
                case 0:
                    name = clean_line(line)
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
                    country = clean_line(line)
                case 9:
                    city = clean_line(line)
                case 10:
                    long = long_to_float(clean_line(line))
                case 11:
                    lat = lat_to_float(clean_line(line))
                case 12:
                    # usually this line is HH:MM:SS
                    # someimtes it is just HH:MM
                    # sometimes it is just H, so deal with all of those
                    line = clean_line(line).split(":")
                    if(len(line)==1):
                        h = int(line[0])
                        m = s = 0
                    elif(len(line)==2):
                        h = int(line[0])
                        m = int(line[1])
                        s = 0
                    else:
                        h = int(line[0])
                        m = int(line[1])
                        s = int(line[2])
                    utcoff = int(h)+(int(m)/60) + (int(s)/3600)
            linenum+=1
        input.close() 
    #    print(name)
    #    print(f"{month:02d}/{day:02d}/{year}")
    #    print(f"{hour:02d}:{min:02d}:{sec:02d}")
    #    print(f"{"male" if sex==1 else "female"}")
    #    print(country)
    #    print(city)
    #    print(f"(lat,long): ({lat},{long})")
    #    print(utcoff)

        # time for config needs to be utc
        # so we take the time here and add utcoffset
        time = dms2dec((int(hour),int(min),int(sec))) # turn into float
        time += utcoff # utcoff is already a float
        time = dec2dms(time) # return the float as a string HH:MM:SS
    #    print(time)

        out = []
        out.append(f"Name = {name}\n")
        out.append(f"Date = {month:02d}/{day:02d}/{year}\n")
        out.append(f"Time = {time}\n")
        out.append(f"Place = {city}, {country}\n")
        out.append(f"Lat = {lat}\n")
        out.append(f"Long = {long}\n")
        fout = open(foutname+".pyph","w")
        fout.writelines(out)
        fout.close()


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
    # string is usually like this 030E44'00
    if(lat[3:4] == 'e'):
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
#    print(retval)
    return retval

def clean_line(line):
    """
    line is a line of bytes
    we remove all the space, carriage return, and newline characters, then
    can return the string as only a string
    """
    line=line.decode(errors='ignore')
    nochars = ["\x00","\r","\n"]
    count = 0
    line=list(line)
    while count < len(line):
        if(line[count] in nochars):
            del line[count]
            continue
        count+=1
    retval = ''.join(line)
#    print(retval)
    return retval

def dec2dms(dd):
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


def get_args():
    parser = argparse.ArgumentParser(
        prog="chtk2sbc",
        usage="%(prog)s [options]", 
        description=f"convert .chtk file .sbc format",
    )
    parser.add_argument("file", nargs='*', help=".chtk file(s) to convert") 
    args = parser.parse_args()
    return args

main()
