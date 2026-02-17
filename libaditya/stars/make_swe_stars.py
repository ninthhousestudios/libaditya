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

import argparse

# constants that need to be defined first

# if swe_id is lllUll then it is a Bayer designation
# where lll is a greek letter and Ull is a constellation abbreviation (for the Latin genitive)
# U(ll) is for other things, e.g., VC for Virgo Cluster, HIP for Hipparcos Catalogue number, etc.
# nnUll is a Flamsteed designation and will end up as ConstNN in Python
# e.g., ,48Lib becomes Librae48()
star_names_short_to_long = {
    "greek": {
        # note: simbad returns two-letter names with an additional "."
        # e.g., "mu.Sgr"
        # not all the letters of the greek alphabet
        # just those used in Bayer designations
        "alf": "Alpha",
        "bet": "Beta",
        "gam": "Gamma",
        # for one star that had some weird stuff happen to it
        "g": "Gamma",
        "del": "Delta",
        # for dOph -> d Ophiuci? just because?
        "d": "Delta",
        "eps": "Epsilon",
        "zet": "Zeta",
        "eta": "Eta", # but no stars with that letter
        "tet": "Theta",
        "iot": "Iota",
        "kap": "Kappa",
        "lam": "Lambda",
        "mu.": "Mu",
        "nu.": "Nu",
        "ksi": "Xi",
        "omi": "Omicron",
        # it seems simbad may use "pi." to have three letters?
        "pi.": "Pi",
        "rho": "Rho",
        "sig": "Sigma",
        "tau": "Tau",
        "ups": "Upsilon",
        "phi": "Phi",
        "chi": "Chi",
        "psi": "Psi",
        "ome": "Omega",
    },
    "constellations": {
        "Ari": "Arietis",
        "Tau": "Tauri",
        "Gem": "Geminorum",
        "Cnc": "Cancri",
        "Leo": "Leonis",
        "Vir": "Virginis",
        "Lib": "Librae",
        "Sco": "Scorpii",
        "Oph": "Ophiuci",
        "Sgr": "Sagittarii",
        "Cap": "Capricorni",
        "Aqr": "Aquarii",
        "And": "Andromedae",
        "Ant": "Antilae",
        "Aps": "Apodis", # Apus constellation
        "Ara": "Arae",
        "Psc": "Piscium",
        "Eri": "Eridani",
        "Cae": "Caeli",
        "Cam": "Camelopardalis",
        "Cas": "Cassiopeiae",
        "Cen": "Centauri",
        "Cep": "Cephei",
        "UMa": "Ursae Majoris",
        "UMi": "Ursae Minoris",
        "Aql": "Aquilae",
        "Hyd": "Hydrae",
        "Sct": "Scuti",
        "Sex": "Sextantis",
        "Sge": "Sagittae",
        "Boo": "Bootis",
        "Dra": "Draconis",
        "Del": "Delphini",
        "Dor": "Doradus",
        "Equ": "Equulei",
        "For": "Fornacis", # Fornax constellation
        "Cyg": "Cygni",
        "Gru": "Gruis",
        "Ori": "Orionis",
        "Cet": "Ceti",
        "Cha": "Chamaeleontis", # Chamaeleon constellation
        "Cir": "Circini", # Circinus constellation
        "Col": "Columbae",
        "Com": "Comae Berenices",
        "CrB": "Coronae Borealis",
        "CrA": "Coronae Australis",
        "TCrB": "TCoronae Borealis",
        "Crt": "Crateris",
        "Cru": "Crucis",
        "Crv": "Corvi",
        "CVn": "Canum Venaticorum",
        "CMa": "Canis Majoris",
        "CMi": "Canis Minors",
        "Aur": "Aurigae",
        "Car": "Carinae",
        "Lyr": "Lyrae",
        "Lep": "Leporis",
        "Men": "Mensae",
        "Mic": "Microscopii",
        "Mon": "Monocerotis",
        "Mus": "Muscae",
        "Nor": "Normae",
        "Oct": "Octantis",
        "Ind": "Indi",
        "Pav": "Pavonis",
        "Peg": "Pegasi",
        "Phe": "Phoenicis",
        "LMi": "Leonis Minoris",
        "Lup": "Lupi",
        "Lyn": "Lyncis",
        "Ser": "Serpentis",
        "Tel": "Telescopium",
        "TrA": "Trianguli Australis",
        "Tri": "Trianguli",
        "Tuc": "Tucanae",
        "Her": "Herculis",
        "Hor": "Horologii",
        "Hya": "Hydrae",
        "Hyi": "Hydri",
        "Lac": "Lacertae",
        "Per": "Persei",
        "Pic": "Pictoris",
        "PsA": "Piscis Austrini",
        "Pup": "Puppis",
        "Pyx": "Pyxis",
        "Ret": "Reticulum",
        "Scl": "Sculptoris",
        "Vel": "Velorum", # Vela, contains Vela supercluster
        "Vol": "Volantis",
        "Vul": "Vulpeculae",
        "VC": "Virgo Cluster",
        "M": "Messier Object",
        "NGC": "New General Catalogue",
        "HIP": "Hipparcos Catalogue",
        "HR": "Bright Star Catalogue",
        "HD": "Henry Draper Catalogue",
    }
}

def main():
    args = get_args()

    stars = []

    for star in args.stars:
        # only want the star lines; swe_make_star also returns the simbad ascii response
        swe_star = swe_make_star(star)[0]
        info_line = swe_star[0]
        star_line_long_form_nomen = swe_star[1]
        # now append the correct lines into outlines
        star_line_split = star_line_long_form_nomen.split(",")[1:]
        nomen = star_line_split[0]
        # append nomen line first, then long_form, the eac name on the info line in order
        stars.append(info_line)
        stars.append(",".join([nomen]+star_line_split))
        stars.append(star_line_long_form_nomen)
        for name in info_line.split(",")[1:]:
            # sometimes there are no more names, which appears as either empty string or a string of spaces, which .strip() converts to empty string, essentially
            if name.strip() == "":
                continue
            if name.strip() == "no hip id":
                continue
            stars.append(",".join([name.strip()]+star_line_split))

    if args.output_file:
        with open(args.output_file,"a") as outfd:
            outfd.writelines(stars)
        exit()

    print("".join(stars))


def swe_make_star(names=[""]) -> [str]:
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
        return star_names_short_to_long["constellations"][constellation]+number
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
        return star_names_short_to_long["constellations"][special]+f" {number.strip()}"
    if number == "":
        if special == "VC":
            return star_names_short_to_long["constellations"][special]
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
        return star_names_short_to_long["greek"][greek]+" "+star_names_short_to_long["constellations"][latin]+f" {number}"
    return star_names_short_to_long["greek"][greek]+" "+star_names_short_to_long["constellations"][latin]

def get_args():
    parser = argparse.ArgumentParser(
        prog="make_swe_stars.py",
        usage="%(prog)s [options]",
        description="make sefstars.txt entry for specified stars",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        help="write entries to output-file. otherwise, writes to stdout",
    )
#    parser.add_argument(
#        "-Z",
#        "--zodiac",
#        action="store_true",
#        help="toggle use of zodiac signs; can set default variable 'signs' in defaults.py",
#    )
    parser.add_argument("stars", nargs='*', help="stars to make entries for. you can enter multiple as a space separated list. if the name itself has a space in it, surround whole name with double-quotes: e.g., $ python make_swe_stars.py Sirius \"HIP 34567\" M87 \"Zeta Ursae Minoris\"") 
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()


