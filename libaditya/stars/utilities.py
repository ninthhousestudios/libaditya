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

from libaditya import constants as const

def read_swe_ids():
    with open(const.stars_file,"r") as infd:
        lines = infd.readlines()

    ids=[]
    for line in lines:
        if line.startswith("#"):
            continue
        ids.append(line.split(",")[1])
    return ids

def parse_simbad_ascii_response(response: str):
    """
    response is the http_response itself
    """
    lines = response.split("\n")
    #import pdb; pdb.set_trace()
    magV = None
    parallax = None
    hipid = "no hip id"
    name = ""
    nomen_name = ",noMen"
    for n,line in enumerate(lines):
        if n > 28:
            # find HIP id so we can return it first as well
            for n in range(28,50):
                if n >= len(lines):
                    break
                if "HIP" in lines[n]:
                    line = lines[n].split()
                    for i,element in enumerate(line):
                        if element == "HIP":
                            hipid = element+" "+line[i+1]
                if "NAME" in lines[n]:
                    line = lines[n].split()
                    for i,element in enumerate(line):
                        if element == "NAME":
                            name = line[i+1]
            break
        match n:
            case 2:
                trad_name = str(line)
            case 5:
                names = line.split(" ")
                # try to guess the ,noMen name
                nomen_name = ","+names[2]+names[3]
            case 7:
                # icrs coordinates
                icrs = line.split(" ")
                ra_hour = icrs[1]
                ra_minute = icrs[2]
                ra_sec = icrs[3]
                dec_degree = icrs[5]
                dec_minute = icrs[6]
                dec_sec = icrs[7]
            case 11:
                pm = line.split(" ")
                pmra = pm[2]
                pmde = pm[3]
            case 13:
                rad_vel = line.split(" ")
                rad_vel = rad_vel[2]
            case 12:
                para = line.split(" ")
                parallax = para[1]
        if "Flux V" in line:
            flux = line.split(" ")
            magV = flux[3]
    if not magV:
        magV = 0
    try:
        return [hipid,name],trad_name,nomen_name,ra_hour,ra_minute,ra_sec,dec_degree,dec_minute,dec_sec,pmra,pmde,rad_vel,parallax,magV
    except:
        return response

def swe_make_star(names=[""]) -> str:
    """
    make an entry for ephe/sefstars.txt to add star "name" to that file, and thus to swe
    returns a list [sefstars.txt_entry,simbad_response_str]
    """
    import urllib
    from string import Template
    simbad_query = Template("https://simbad.cds.unistra.fr/simbad/sim-id?Ident=$swe_id&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit%20id&output.format=ASCII")
    swe_star_entry = Template("$trad_name,$nomen_name,ICRS,$ra_hour,$ra_minute,$ra_sec,$dec_degree,$dec_minute,$dec_sec,$pmra,$pmde,$rad_vel,$parallax,$magnitude_V")
    if not isinstance(names,list):
        names=[names]
    ret = []
    for name in names:
        name = name.replace(" ","+")
        the_bytes = urllib.request.urlopen(simbad_query.substitute(swe_id=name))
        ascii = the_bytes.read().decode()
#            lines=the_bytes.read().decode().split("\n")
#            for n,line in enumerate(lines):
#                print(n,line)
        # now parse bytes into all the variables needs for swe_star_entry
        response = parse_simbad_ascii_response(ascii)
        try:
            ids,trad_name,nomen_name,ra_hour,ra_minute,ra_sec,dec_degree,dec_minute,dec_sec,pmra,pmde,rad_vel,parallax,magV = response
        except:
            print("Error: \n")
            print(response)
            return
        id_line = f"#0# {nomen_name.replace(",","")}, "
        id_line += str(ids[1]+", "+ids[0]+"\n")
        ret.append(id_line)
        ret.append(f"{nomen_to_long_form(nomen_name)}{nomen_name},ICRS,{ra_hour},{ra_minute},{ra_sec},{dec_degree},{dec_minute},{dec_sec},{pmra},{pmde},{rad_vel},{parallax},{magV}\n")
    return ret, ascii


def swe_write_stars(names=[""],outfile=""):
    """
    take a list of objects ids, names
    write out to a file their entries for ephe/sefstars.txt

    TODO: update to do multi-line output with each name
    """
    lines=[]
    for name in names:
        returns, ascii=swe_make_star(name)
#        print(f"sws: {returns[0]=} {returns[1]=}")
        lines.append(returns[0])
        lines.append(returns[1])
#    print(f"{lines=}")
    with open(outfile,"a") as fd:
        fd.writelines(lines)
    return

def swe_star_to_python(swe_star: str) -> str:
    """
    take a star line from ephe/sefstars.txt and produce a python object that inherits from FixedStar
    this is written in a .py file that can then be loaded, and we can use any of these stars then by name
    e.g., stars.the_stars.Fomalhaut(context)

    swe_star is like this:

    #0# swe_id, Common Name, HIP ID
    Galactic Center,SgrA*,ICRS,17,45,40.03599,-29,00,28.1699,-2.755718425, -5.547,  0.0,0.125,999.99,  0,    0

    (traditional/common) name,(,noMen) nomenclature name, equinox, ra_hour, ra_minute, ra_second, dec_degree, dec_minute, dec_second,
    ra of proper motion, dec of proper motion, radial velocity in km/s, annual parallax in .0001"", magnitude_V
    an example of what this produces:

    class GalacticCenter(FixedStar): # ,SgrA*

        def __init__(self, context = EphContext()): 
            super().__init__(swe_id = ",SgrA*", context=context)

    for new stars, this is the template I am trying to use:

    #0# alfAur, Capella, HIP 24608
    Alpha Auriga,alfAur,ICRS,05,16,41.35871,+45,59,52.7693,75.25,-426.89,29.19,76.20,0.08

    class AlphaAuriga(FixedStar): # ,alfAur

        def __init__(self, context = EphContext()): 
            super().__init__(swe_id = ",alfAur", context=context, swe_string="Alpha Auriga,alfAur,ICRS,05,16,41.35871,+45,59,52.7693,75.25,-426.89,29.19,76.20,0.08")
            self._other_names = ["Capella", "HIP 24608"]

    Capella = AlphaAuriga

    now, TheStars(context)["alfAur"] will return AlphaAuriga()
    but you can also do stars.the_stars.Capella(context)
    
    """
    lines=swe_star.split("\n")
    # since swe_star[1] has a \n at the end, lines will have 3 elements, the last being ""
    names = lines[0]
    names_split = names.split(",")
    common_names = []
    hip_name = ""
    # the swe_id, aka ",nomen" name
    id_swe_id = ","+names_split[0].split()[1]
    # dont need the first one anymore
    names_split = names_split[1:]
    for name in names_split:
        name=name.strip()
        if "HIP" in name:
            hip_name = f"{name.strip()}"
        if not "Messier" in names and not name.startswith("VC") and not name.startswith("NGC") and not name.startswith("HR") and not name.startswith("HD"):
            # get all the common names
            common_names.append(f"{name.strip()}")
    other_names = common_names
    if hip_name:
        other_names = common_names + [hip_name]

    swe_line = lines[1]
    swe_split = lines[1].split(",")

    long_form_name = swe_split[0].replace(" ","")
    star_swe_id = ","+swe_split[1]

    if id_swe_id != star_swe_id:
        print(f"Error swe_ids do not match: {id_swe_id} != {star_swe_id}\nLines out of order")
        return

    other_classes=""
    for common_name in common_names:
        other_classes += f"{common_name.replace(" ","")} = {long_form_name}\n"
    other_classes += "\n\n"

    if other_names is not None:
        tmp = []
        for name in other_names:
            if name in tmp:
                continue
            if name == "" or name == '""':
                continue
            tmp.append(name.replace("'",""))
        other_names = tmp

    ret=[]
    ret.append(f"class {long_form_name}(FixedStar): # {id_swe_id}\n")
    ret.append("\n")
    ret.append(f"    def __init__(self, context = EphContext()):\n")
    ret.append(f"        super().__init__(swe_id = \"{star_swe_id}\", context=context, swe_string=\"{swe_line}\")\n")
    ret.append(f"        self._other_names = {other_names}\n\n")
    ret.append(other_classes)
    return "".join(ret)

def swe_stars_to_py(infile,outfile):
    """
    take an input
    """
    with open(infile, "r") as infd:
        swe_stars = infd.readlines()

    with open(outfile, "a") as outfd:
        n = 0
        while n < len(swe_stars):
            # if line is blank
            if not swe_stars[n]:
                n+=1
                continue
            # if line has info for the next line
            if "#" in swe_stars[n] and "#0#" not in swe_stars[n]:
                n+=1
                continue
            star = swe_stars[n]
            n+=1
            if "#0#" in star:
                star += swe_stars[n]
                n+=1
            outfd.write(swe_star_to_python(star))

def convert_sefstars_first_pass(infile,outfile):
    """
    convert ephe/sefstars.txt to a different format
    i already manually changed all 2-letter greek abbreviations to 3-letter abbreviations manually
    so that is accounted for in this function
    """
    with open(infile, "r") as infd:
        inlines = infd.readlines()

    outlines = []
    for inline in inlines:
        if inline.startswith("#"):
            outlines.append(inline)
            continue
        star = inline.split(",")
        trad_name = star[0]
        nomen_name = star[1].replace("-","0")
        star[1] = nomen_name
        long_form_name = nomen_to_long_form(nomen_name)
        star[0]=long_form_name
        outlines.append(f"#0# {nomen_name}, {trad_name}\n")
        outlines.append(",".join(star).strip()+"\n")

    with open(outfile,"a") as outfd:
        outfd.writelines(outlines)


def nomen_to_long_form(nomen: str):
    """
    turn a nomenclature name into a long form version of itself
    nomenclature names, any of these designations:
    Bayer, Falmsteed, HIP, NGC, HD, HR, M (Messer Object)
    greek is lowercase greek letter, will use upper case in English
    Latin is genitive of Latin constellation name
    e.g., alfTau, Alpha Tauri, α Tauri
    """
    if nomen[0] == ",":
        nomen = nomen[1:]
    if nomen[0].isnumeric():
        # this means it is Flamsteed 
        # easiest to do this first
        number=""
        n=0
        while nomen[n].isnumeric():
            number+=nomen[n]
            n+=1
        constellation=""
        while n < len(nomen):
            constellation+=nomen[n]
            n+=1
        return const.star_names_short_to_long["constellations"][constellation]+number
    # check if this is a "special constellation"
    # not really constellations, but fill the same place in the nomen name, so are treated the same for this purpose
    special_constellations = ["VC","HD","HR","HIP","NGC"]
    # doesnt include "M" because that throws off other checks
    special = None
    for constellation in special_constellations:
        number=""
        if constellation in nomen.upper() or (nomen.upper().startswith("M") and "mu." not in nomen):
            # if one of these special tags is here, special will show us that it is
            if nomen.upper().startswith("M"):
                special = "M"
                number = nomen[1:]
            else:
                special = constellation
                # the rest of the string except the "constellation" names
                number = nomen[(len(special)):]
            break
    if number != "":
        return const.star_names_short_to_long["constellations"][special]+f" {number.strip()}"
    if number == "":
        if special == "VC":
            return const.star_names_short_to_long["constellations"][special]
    # now assume it is a Bayer designation
    # some in the original sefstars.txt have a hyphen "-" in the name
    # replace that with 0
    # first three letters are the greek
    greek = nomen[:3]
    # last three are the Latin constellation
    latin = nomen[3:]
    # sometimes there are two stars with the same name basically, one is, e.g., gam01Sgr, the other, gam02Sgr
    # this will be Gamma Sagittarii 1 and Gamma Sagittarii 2
    number = ""
    if latin[:2].isnumeric():
        number = latin[:2]
        latin = latin[2:]
    if not greek.islower():
        return nomen
    if number:
        return const.star_names_short_to_long["greek"][greek]+" "+const.star_names_short_to_long["constellations"][latin]+f" {number}"
    return const.star_names_short_to_long["greek"][greek]+" "+const.star_names_short_to_long["constellations"][latin]

# convert_sefstars_second_pass
def swe_consolidate_sefstars(infile,outfile):
    """
    right now, sefstars.txt has some stars line that are the same, e.g.,:
    Alpha Tauri,alfTau,ICRS,04,35,55.23907,+16,30,33.4885,63.45,-188.94,54.398,48.94,0.86
    appears three times
    the info line above it, starting with #0#, is different in each case
    so this function consolidates all of the names in the info line above just one entrance for each star/object
    consolidates what it reads from infile, writes to outfile
    """
    with open(infile,"r") as infd:
        lines = infd.readlines()

    # two-passes
    # one to put all info into dictionary
    # but i want all actual comment lines to remain more or less in the same place
    # the second read pass will also write out simultaneously

    # populate the dictionary of star information
    # stars_info = {
    #     "noMen": [swe_line,other_name,other_name,...]
    # }
    stars_info = swe_populate_stars(lines)

    with open(infile,"r") as infd:
        lines = infd.readlines()

    written = []
    outlines = []

    n=0
    for n in range(0,len(lines)):
        line=lines[n]
        if line.startswith("#") and not line.startswith("#0#"):
            outlines.append(line)
            continue
        if line.startswith("#0#"):
            info_line = line
            n+=1
            star_line = lines[n]
            # ready for the next loop
            n+=1
            # info_line = "#0# alfTau, Alpha Taurus, Aldebaran, HIP 21421"
            info_line = info_line.split(",")
            # indicator and nomen are in the first element of info_line
            # we want the other name, so remove the nomen name from the list
            nomen = info_line[0].split()[1]
            if nomen in written:
                continue
            written.append(nomen)
            info_to_write = f"#0# {nomen}"
            # stars_info[nomen] is a list [swe_star_entry,other_name,other_name,...]
            swe_star = stars_info[nomen][0]
            for n in range(1,len(stars_info[nomen])):
                info_to_write += f", {stars_info[nomen][n]}"
            outlines.append(info_to_write)
            outlines.append(swe_star)
    with open(outfile,"a") as outfd:
        outfd.writelines(outlines)


def swe_populate_stars(lines):
    """
    lines are the lines that have been read from sefstars.txt

     populate the dictionary of star information
     stars_info = {
         "noMen": [swe_line,other_name,other_name,...]
     }
    """
    stars_info = {}

    n=0
    for n in range(0,len(lines)):
        line=lines[n]
        if line.startswith("#") and not line.startswith("#0#"):
            # a comment only
            n+=1
            continue
        if line.startswith("#0#"):
            info_line = line
            n+=1
            star_line = lines[n]
            # ready for the next loop
            n+=1
            # info_line = "#0# alfTau, Alpha Taurus, Aldebaran, HIP 21421"
            info_line = info_line.split(",")
            # indicator and nomen are in the first element of info_line
            # we want the other name, so remove the nomen name from the list
            nomen = info_line[0].split()[1]
            info_line = info_line[1:]
            if nomen in stars_info.keys():
                # this entry is already here, so we only want to add new names if there are any
                for name in info_line:
                    if name in stars_info[nomen]:
                        continue
                    else:
                        stars_info[nomen].append(name.strip())
                        continue
            entry=[]
            if nomen != star_line.split(",")[1]:
                print(f"Error, lines out of order...\n{info_line=}\n{star_line=}")
            entry.append(star_line)
            for name in info_line:
                entry.append(name.strip())
            stars_info[nomen] = entry
    return stars_info

def swe_write_multiline_sefstars(infile,outfile):
    """
    take a sefstars.txt that has two entries per star, i.e.,:
    #0# noMen, other_name, other_name, ...
    long_form_nomen,nomen,frame,ra_hour,...

    and output a sefstars.txt that has the same info line as well as one entry for each name
    #0# noMen, other_name, other_name, ...
    nomen,nomen,frame,ra_hour,...
    long_form_nomen,nomen,frame,ra_hour,...
    other_name,nomen,frame,ra_hour,...


    #0# alfCMa,  Alpha Canis Major,  Sirius,  HIP 32349
    alfCMa,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.50,379.21,-1.46
    Alpha Canis Majoris,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.50,379.21,-1.46
    Alpha Canis Major,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.50,379.21,-1.46
    Sirius,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.50,379.21,-1.46
    HIP 32349,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.50,379.21,-1.46
    ...

    will try to make the first other_name be the "traditional" name if its has one
    this may not always work exactly as hoped
    """
    with open(infile) as infd:
        inlines=infd.readlines()


    # need to perserve comments and order, so we will do this with a manual n-based while loop

    # so we need to write out the original info line
    # we need to write out the original swe_string
    # all in the following order
    # as well as the same swe_string with these as the first parameter
    #   (traditional name) if this exists, it should be first
    #   long_form_nomen ; this is a written form of the nomen name, e.g., Alpha Canis Majoris
    #   other_name, etc.

    # this is where we put the lines to write out
    outlines = []

    # we go through the inlines manually so that we preserve the order of comments, etc.
    n=0
    for n in range(0,len(inlines)):
        line=inlines[n]
        if line.startswith("#") and not line.startswith("#0#"):
            # a comment only
            outlines.append(line)
            n+=1
            continue
        if line.startswith("#0#"):
            info_line = line
            outlines.append(info_line)
            n+=1
            star_line_long_form_nomen = inlines[n]
            # ready for the next loop
            n+=1

            # now append the correct lines into outlines
            star_line_split = star_line_long_form_nomen.split(",")[1:]
            nomen = star_line_split[0]
            # append nomen line first, then long_form, the eac name on the info line in order
            outlines.append(",".join([nomen]+star_line_split))
            outlines.append(star_line_long_form_nomen)
            for name in info_line.split(",")[1:]:
                # sometimes there are no more names, which appears as either empty string or a string of spaces, which .strip() converts to empty string, essentially
                if name.strip() == "":
                    continue
                if name.strip() == "no hip id":
                    continue
                outlines.append(",".join([name.strip()]+star_line_split))

    with open(outfile,"a") as outfd:
        outfd.writelines(outlines)

    return 0
