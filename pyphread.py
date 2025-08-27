import codecs

def read_pyph(infile):
    input = open(infile, "r")
    for line in input:
        if not "=" in line:
            continue
        field, value = line.split("=")
        field = field.strip()
        value = value.strip()
        if field.startswith("Na") or field.startswith("na"):
            name = value
        if field.startswith("Pla") or field.startswith("pla"):
            placename = value
        if field.startswith("Da") or field.startswith("da"):
            month, day, year = intize_date(value)
        if field.startswith("Ti") or field.startswith("ti"):
            ephclock = intize_time(value)
        if field.startswith("La") or field.startswith("la"):
            lat = float(value)
        if field.startswith("Lo") or field.startswith("lo"):
            long = float(value)
    return name, placename, month, day, year, ephclock, lat, long 

def read_chtk(infile):
    input = open(infile, "rb")
    lines = input.readlines()
    linenum = 0
    for line in lines:
        #print(f"{n}: {line.decode(errors='ignore')}")
        match linenum:
            case 0: # the functions used on the lines are all in chtk2pyph
                    # which i *-imported because im lazy
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
            case 13: # dst value
                dst = intize_line(codecs.decode(line))
        linenum+=1
    input.close() 
    placename = city + ", " + country
    ephclock = hour + min/60 + sec/3600
    return name, placename, month, day, year, ephclock+utcoff-dst, lat, long 


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

def intize_date(date):
    """
    take a string 'MM/DD/YYYY'
    and return a tuple of int (mm,dd,yyyy)
    """
    date = date.split('/')
    year = int(date[2]) 
    month = int(date[0])
    day = int(date[1])

    return (month, day, year)

def intize_time(time):
    """
    take a string 'HH:MM:SS'
    and return a float of that time
    """
    time = time.split(':')
    return int(time[0]) + int(time[1]) / 60 + int(time[2]) / 3600

