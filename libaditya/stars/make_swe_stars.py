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
import sys
import urllib.error
import urllib.request
from string import Template

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
        "g": "Gamma",
        "del": "Delta",
        "d": "Delta",
        "eps": "Epsilon",
        "zet": "Zeta",
        "eta": "Eta",
        "tet": "Theta",
        "iot": "Iota",
        "kap": "Kappa",
        "lam": "Lambda",
        "mu.": "Mu",
        "nu.": "Nu",
        "ksi": "Xi",
        "omi": "Omicron",
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
        "Ant": "Antliae",
        "Aps": "Apodis",
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
        "For": "Fornacis",
        "Cyg": "Cygni",
        "Gru": "Gruis",
        "Ori": "Orionis",
        "Cet": "Ceti",
        "Cha": "Chamaeleontis",
        "Cir": "Circini",
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
        "CMi": "Canis Minoris",
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
        "Tel": "Telescopii",
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
        "Pyx": "Pyxidis",
        "Ret": "Reticuli",
        "Scl": "Sculptoris",
        "Vel": "Velorum",
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

SIMBAD_URL = Template(
    "https://simbad.cds.unistra.fr/simbad/sim-id"
    "?Ident=$swe_id&NbIdent=1&Radius=2&Radius.unit=arcmin"
    "&submit=submit%20id&output.format=ASCII"
)

EXPECTED_FIELD_COUNT = 14


def main():
    args, argparser = get_args()

    if args.verify:
        verify_against_simbad(args.verify, args.output_file or "sefstars.txt")
        return

    if not args.stars and not args.input_file:
        argparser.print_help()
        return

    star_names = list(args.stars) if args.stars else []
    if args.input_file:
        star_names.extend(read_star_list(args.input_file))

    if not star_names:
        print("No star names provided.", file=sys.stderr)
        return

    existing_names = set()
    if args.output_file:
        existing_names = load_existing_names(args.output_file)

    stars = []
    for star in star_names:
        try:
            result = swe_make_star(star)
        except SimbadError as e:
            print(f"Error querying SIMBAD for '{star}': {e}", file=sys.stderr)
            continue

        entry_lines = build_entry_lines(result)

        skipped = []
        added = []
        for line in entry_lines:
            if line.startswith("#"):
                added.append(line)
                continue
            first_field = line.split(",")[0]
            if first_field in existing_names:
                skipped.append(first_field)
            else:
                added.append(line)
                existing_names.add(first_field)

        if skipped:
            print(f"Skipping duplicate names for '{star}': {', '.join(skipped)}", file=sys.stderr)

        if not validate_entry(added, star):
            continue

        if args.dry_run:
            print(f"--- {star} ---")
            print("".join(added))
        else:
            stars.extend(added)

    if args.dry_run:
        return

    if args.output_file:
        with open(args.output_file, "a") as outfd:
            outfd.writelines(stars)
    else:
        print("".join(stars))


class SimbadError(Exception):
    pass


def swe_make_star(name: str) -> dict:
    """
    Query SIMBAD for a star and return parsed data.
    Returns a dict with keys: ids, trad_name, nomen_name, coords, and raw response.
    """
    query_name = name.replace(" ", "+")
    try:
        response = urllib.request.urlopen(
            SIMBAD_URL.substitute(swe_id=query_name),
            timeout=30,
        )
        response_text = response.read().decode()
    except urllib.error.URLError as e:
        raise SimbadError(f"Network error: {e}") from e
    except urllib.error.HTTPError as e:
        raise SimbadError(f"HTTP {e.code}: {e.reason}") from e

    parsed = parse_simbad_ascii_response(response_text)
    if parsed is None:
        raise SimbadError(f"Could not parse SIMBAD response for '{name}'")

    return parsed


def build_entry_lines(parsed: dict) -> list[str]:
    """Build the multi-line sefstars.txt entry from parsed SIMBAD data."""
    nomen = parsed["nomen_name"]
    long_form = nomen_to_long_form(nomen)
    data_fields = (
        f"{nomen},ICRS,"
        f"{parsed['ra_hour']},{parsed['ra_minute']},{parsed['ra_sec']},"
        f"{parsed['dec_degree']},{parsed['dec_minute']},{parsed['dec_sec']},"
        f"{parsed['pmra']},{parsed['pmde']},{parsed['rad_vel']},"
        f"{parsed['parallax']},{parsed['magV']}"
    )

    ids = parsed["ids"]
    comment = f"#0# {nomen}, {long_form}"
    for ident in [ids["name"], ids["hipid"]]:
        if ident and ident != "no hip id":
            comment += f", {ident}"
    comment += "\n"

    lines = [comment]
    lines.append(f"{nomen},{data_fields}\n")
    lines.append(f"{long_form},{data_fields}\n")

    for ident in [ids["name"], ids["hipid"]]:
        if ident and ident != "no hip id":
            lines.append(f"{ident},{data_fields}\n")

    return lines


def validate_entry(lines: list[str], star_name: str) -> bool:
    """Check that data lines have the expected number of fields."""
    for line in lines:
        if line.startswith("#"):
            continue
        fields = line.strip().split(",")
        if len(fields) < EXPECTED_FIELD_COUNT:
            print(
                f"Warning: entry for '{star_name}' has {len(fields)} fields "
                f"(expected {EXPECTED_FIELD_COUNT}), skipping",
                file=sys.stderr,
            )
            return False
    return True


def parse_simbad_ascii_response(response_text: str) -> dict | None:
    """
    Parse SIMBAD ASCII response into a dict of astrometric data.
    Returns None if parsing fails.
    """
    lines = response_text.split("\n")
    magV = None
    parallax = None
    hipid = "no hip id"
    trad_name = ""
    nomen_name = "noMen"

    for n, line in enumerate(lines):
        if n > 28:
            for j in range(28, min(50, len(lines))):
                if "HIP" in lines[j]:
                    parts = lines[j].split()
                    for i, element in enumerate(parts):
                        if element == "HIP":
                            hipid = element + " " + parts[i + 1]
                if "NAME" in lines[j]:
                    parts = lines[j].split()
                    for i, element in enumerate(parts):
                        if element == "NAME":
                            trad_name = parts[i + 1]
            break
        match n:
            case 2:
                trad_name = str(line)
            case 5:
                tokens = line.split(" ")
                nomen_name = tokens[2] + tokens[3]
            case 7:
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
            case 12:
                para = line.split(" ")
                parallax = para[1]
            case 13:
                rad_vel = line.split(" ")
                rad_vel = rad_vel[2]
        if "Flux V" in line:
            flux = line.split(" ")
            magV = flux[3]

    if not magV:
        magV = 0

    try:
        return {
            "ids": {"hipid": hipid, "name": trad_name},
            "nomen_name": nomen_name,
            "ra_hour": ra_hour,
            "ra_minute": ra_minute,
            "ra_sec": ra_sec,
            "dec_degree": dec_degree,
            "dec_minute": dec_minute,
            "dec_sec": dec_sec,
            "pmra": pmra,
            "pmde": pmde,
            "rad_vel": rad_vel,
            "parallax": parallax,
            "magV": magV,
        }
    except UnboundLocalError:
        return None


def nomen_to_long_form(nomen: str) -> str:
    """
    Turn a nomenclature name into a long form version of itself.
    Bayer, Flamsteed, HIP, NGC, HD, HR, M (Messier Object).
    e.g., alfTau -> Alpha Tauri
    """
    if nomen[0] == ",":
        nomen = nomen[1:]
    if nomen[0].isnumeric():
        number = ""
        n = 0
        while nomen[n].isnumeric():
            number += nomen[n]
            n += 1
        constellation = nomen[n:]
        return star_names_short_to_long["constellations"][constellation] + number

    special_constellations = ["VC", "HD", "HR", "HIP", "NGC"]
    special = None
    number = ""
    for constellation in special_constellations:
        if constellation in nomen.upper() or (nomen.upper().startswith("M") and "mu." not in nomen):
            if nomen.upper().startswith("M"):
                special = "M"
                number = nomen[1:]
            else:
                special = constellation
                number = nomen[len(special):]
            break

    if number != "":
        return star_names_short_to_long["constellations"][special] + f" {number.strip()}"
    if special == "VC":
        return star_names_short_to_long["constellations"][special]

    greek = nomen[:3]
    latin = nomen[3:]
    number = ""
    if latin[:2].isnumeric():
        number = latin[:2]
        latin = latin[2:]
    if not greek.islower():
        return nomen
    if number:
        return star_names_short_to_long["greek"][greek] + " " + star_names_short_to_long["constellations"][latin] + f" {number}"
    return star_names_short_to_long["greek"][greek] + " " + star_names_short_to_long["constellations"][latin]


def load_existing_names(filepath: str) -> set[str]:
    """Load the first field of every data line in an existing sefstars.txt."""
    names = set()
    try:
        with open(filepath) as f:
            for line in f:
                if line.startswith("#") or not line.strip():
                    continue
                first_field = line.split(",")[0]
                names.add(first_field)
    except FileNotFoundError:
        pass
    return names


def read_star_list(filepath: str) -> list[str]:
    """Read star names from a file, one per line. Blank lines and # comments are skipped."""
    names = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                names.append(line)
    return names


def verify_against_simbad(nomen_names: list[str], sefstars_path: str):
    """
    Look up stars in sefstars.txt by nomen name, then query SIMBAD and compare
    coordinates. Reports any differences.
    """
    existing = {}
    try:
        with open(sefstars_path) as f:
            for line in f:
                if line.startswith("#") or not line.strip():
                    continue
                fields = line.strip().split(",")
                if len(fields) >= EXPECTED_FIELD_COUNT:
                    existing[fields[0]] = fields
    except FileNotFoundError:
        print(f"File not found: {sefstars_path}", file=sys.stderr)
        return

    for nomen in nomen_names:
        if nomen not in existing:
            print(f"  {nomen}: not found in {sefstars_path}")
            continue

        file_fields = existing[nomen]
        try:
            parsed = swe_make_star(nomen)
        except SimbadError as e:
            print(f"  {nomen}: SIMBAD error: {e}")
            continue

        simbad_ra = f"{parsed['ra_hour']},{parsed['ra_minute']},{parsed['ra_sec']}"
        simbad_dec = f"{parsed['dec_degree']},{parsed['dec_minute']},{parsed['dec_sec']}"
        file_ra = f"{file_fields[3]},{file_fields[4]},{file_fields[5]}"
        file_dec = f"{file_fields[6]},{file_fields[7]},{file_fields[8]}"

        if simbad_ra == file_ra and simbad_dec == file_dec:
            print(f"  {nomen}: OK (coordinates match)")
        else:
            print(f"  {nomen}: MISMATCH")
            print(f"    file:   RA={file_ra}  Dec={file_dec}")
            print(f"    simbad: RA={simbad_ra}  Dec={simbad_dec}")

        simbad_mag = str(parsed["magV"])
        file_mag = file_fields[13] if len(file_fields) > 13 else "?"
        if simbad_mag != file_mag:
            print(f"    mag V: file={file_mag} simbad={simbad_mag}")


def get_args():
    parser = argparse.ArgumentParser(
        prog="make_swe_stars.py",
        usage="%(prog)s [options] [stars...]",
        description="Generate sefstars.txt entries for fixed stars from SIMBAD data.",
    )
    parser.add_argument(
        "-o", "--output-file",
        help="append entries to this file (default: print to stdout)",
    )
    parser.add_argument(
        "-i", "--input-file",
        help="read star names from a file (one per line, # comments allowed)",
    )
    parser.add_argument(
        "-n", "--dry-run",
        action="store_true",
        help="show what would be generated without writing anything",
    )
    parser.add_argument(
        "--verify",
        nargs="+",
        metavar="NOMEN",
        help="verify existing sefstars.txt entries against current SIMBAD data",
    )
    parser.add_argument(
        "stars",
        nargs="*",
        help=(
            "star identifiers (Bayer, Flamsteed, HIP, name). "
            "Quote names with spaces: \"Alpha Ursae Minoris\""
        ),
    )
    args = parser.parse_args()
    return args, parser


if __name__ == "__main__":
    main()
