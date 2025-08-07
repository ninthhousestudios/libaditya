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

import configparser
import swisseph as swe
import pyphutils as putil

# defaults
pyphpath = "/home/josh/w/astro/soft/pyphemeris/"
ayanamsa = 98  # new code for dhruva equatorial
show_helios = 0
show_baryos = 0
show_topo = 0
show_adityas = 0
show_equ = 0
utcoffset = -4
timezone = "EDT"
lat = round(putil.dms2dec((39, 57, 22)), 3)
long = -round((putil.dms2dec((86, 0, 46))))
alt = 252  # swe requires meters
placename = ""
hsys = "C"
show_houses = 1
edir = "/home/josh/dev/swisseph/ephe/"
lang = "eng"
signs = []
sign_long = 1  # default to printing longitudes as "degrees Sign", e.g., 10.3 Capricorn
sign_func = putil.yessignize
eng = pyphpath + "dict.eng"
iast = pyphpath + "dict.iast"
deva = pyphpath + "dict.deva"
mixed = pyphpath + "dict.mixed"
langfile = mixed
flground = 1  # 1 to round, 0 to not round, ndigs is how much to round to
ndigs = 3
round_func = putil.yesround  # like with the signs, the function used to round
# constant constants for program functions
ECL = 0
EQU = swe.FLG_EQUATORIAL
HELIO = swe.FLG_HELCTR
BARY = swe.FLG_BARYCTR
sysflg = ECL  # default

# constant constants

onesecjd = 1.157401129603386e-05
oneminjd = onesecjd * 60
onehrjd = oneminjd * 60
onedayjd = onehrjd * 24
oneyearjd = onedayjd * 365
nak = 13.333333333333334
true_node = 11
rahu = 11
ketu = 10
earth = 12
calendardays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]
signglyph = ["♈︎", "♉︎", "♊︎", "♋︎", "♌︎", "♍︎", "♎︎", "♏︎", "♐︎", "♑︎", "♒︎", "♓︎"]


# inconstant constants, i.e., read from a file

planets = []
rasis = []
tithi = []
karana = []
nakshatra = []
nakshatraeq = []
vara = []
yogas = []
adityas = []
signs = []


def init_names(langfile=eng):
    names = configparser.ConfigParser()
    names.read(langfile)

    global planets
    global rasis
    global tithi
    global karana
    global nakshatra
    global nakshatraeq
    global vara
    global yogas
    global adityas
    global signs

    # because of importing and such things
    planets = []
    rasis = []
    tithi = []
    karana = []
    nakshatra = []
    nakshatraeq = []
    vara = []
    yogas = []
    adityas = []
    signs = []

    # because of needing these names in pyphclasses i called init_names()
    # there, which when i run the whole program thus initializes them twice
    # which causes the karana especially to not work right
    # so if planets is not an empty list, then we have already done the names
    # if planets != []:
    #    return

    pnames = names["PLANETS"]
    rnames = names["RASIS"]
    tnames = names["TITHI"]
    knames = names["KARANA"]
    nnames = names["NAKSHATRA"]
    neqnames = names["NAKSHATRAEQ"]
    vnames = names["VARA"]
    ynames = names["YOGAS"]
    anames = names["ADITYAS"]

    planets.append(pnames["Sun"])
    planets.append(pnames["Moon"])
    planets.append(pnames["Mercury"])
    planets.append(pnames["Venus"])
    planets.append(pnames["Mars"])
    planets.append(pnames["Jupiter"])
    planets.append(pnames["Saturn"])
    planets.append(pnames["Uranus"])
    planets.append(pnames["Neptune"])
    planets.append(pnames["Pluto"])
    planets.append(pnames["Rahu"])  # index 11
    planets.append(pnames["Ketu"])
    planets.append([])
    planets.append([])
    planets.append(pnames["Earth"])

    rasis.append(rnames["Aries"])
    rasis.append(rnames["Taurus"])
    rasis.append(rnames["Gemini"])
    rasis.append(rnames["Cancer"])
    rasis.append(rnames["Leo"])
    rasis.append(rnames["Virgo"])
    rasis.append(rnames["Libra"])
    rasis.append(rnames["Scorpio"])
    rasis.append(rnames["Sagittarius"])
    rasis.append(rnames["Capricorn"])
    rasis.append(rnames["Aquarius"])
    rasis.append(rnames["Pisces"])

    tithi.append(tnames["Nanda"])
    tithi.append(tnames["Bhadra"])
    tithi.append(tnames["Jaya"])
    tithi.append(tnames["Rkta"])
    tithi.append(tnames["Purna"])

    karana.append(knames["Kimtughna"])
    karana.append(knames["Bava"])
    karana.append(knames["Balava"])
    karana.append(knames["Kaulava"])
    karana.append(knames["Taitula"])
    karana.append(knames["Garija"])
    karana.append(knames["Vanija"])
    karana.append(knames["Vishti"])
    karana.append(knames["Shakuni"])
    karana.append(knames["Chatushpada"])
    karana.append(knames["Naga"])
    karana = organize_karana(karana)

    nakshatra.append(nnames["Ashvini"])
    nakshatra.append(nnames["Bharani"])
    nakshatra.append(nnames["Krittika"])
    nakshatra.append(nnames["Rohini"])
    nakshatra.append(nnames["Mrigashira"])
    nakshatra.append(nnames["Ardra"])
    nakshatra.append(nnames["Punarvasu"])
    nakshatra.append(nnames["Pushya"])
    nakshatra.append(nnames["Ashlesha"])
    nakshatra.append(nnames["Magha"])
    nakshatra.append(nnames["Purva Phalguni"])
    nakshatra.append(nnames["Uttara Phalguni"])
    nakshatra.append(nnames["Hasta"])
    nakshatra.append(nnames["Chitra"])
    nakshatra.append(nnames["Svati"])
    nakshatra.append(nnames["Vishakha"])
    nakshatra.append(nnames["Anuradha"])
    nakshatra.append(nnames["Jyeshtha"])
    nakshatra.append(nnames["Mula"])
    nakshatra.append(nnames["Purva Ashadha"])
    nakshatra.append(nnames["Uttara Ashadha"])
    nakshatra.append(nnames["Shravana"])
    nakshatra.append(nnames["Danishtha"])
    nakshatra.append(nnames["Shatabhisha"])
    nakshatra.append(nnames["Purva Bhadrapada"])
    nakshatra.append(nnames["Uttara Bhadrapada"])
    nakshatra.append(nnames["Revati"])

    vara.append(vnames["Ravivara"])
    vara.append(vnames["Somavara"])
    vara.append(vnames["Mangalavara"])
    vara.append(vnames["Budhavara"])
    vara.append(vnames["Guruvara"])
    vara.append(vnames["Shukravara"])
    vara.append(vnames["Shanivara"])

    yogas.append(ynames["Vishkambha"])
    yogas.append(ynames["Priti"])
    yogas.append(ynames["Ayushman"])
    yogas.append(ynames["Saubhagya"])
    yogas.append(ynames["Shobana"])
    yogas.append(ynames["Atiganda"])
    yogas.append(ynames["Sukarma"])
    yogas.append(ynames["Dhriti"])
    yogas.append(ynames["Shoola"])
    yogas.append(ynames["Ganda"])
    yogas.append(ynames["Vriddhi"])
    yogas.append(ynames["Dhruva"])
    yogas.append(ynames["Vyaghata"])
    yogas.append(ynames["Harshana"])
    yogas.append(ynames["Vajra"])
    yogas.append(ynames["Siddhi"])
    yogas.append(ynames["Vyatipata"])
    yogas.append(ynames["Variyan"])
    yogas.append(ynames["Parigha"])
    yogas.append(ynames["Shiva"])
    yogas.append(ynames["Siddha"])
    yogas.append(ynames["Sadhya"])
    yogas.append(ynames["Shubha"])
    yogas.append(ynames["Shukla"])
    yogas.append(ynames["Brahma"])
    yogas.append(ynames["Indra"])
    yogas.append(ynames["Vaidhriti"])

    adityas.append(anames["Aryama"])
    adityas.append(anames["Mitra"])
    adityas.append(anames["Varuna"])
    adityas.append(anames["Indra"])
    adityas.append(anames["Vivasvan"])
    adityas.append(anames["Tvashta"])
    adityas.append(anames["Vishnu"])
    adityas.append(anames["Amshu"])
    adityas.append(anames["Bhaga"])
    adityas.append(anames["Pusha"])
    adityas.append(anames["Parjanya"])
    adityas.append(anames["Dhata"])

    signs = rasis

    nakshatraeq.append(neqnames["Krittika"])
    nakshatraeq.append(neqnames["Rohini"])
    nakshatraeq.append(neqnames["Mrigashira"])
    nakshatraeq.append(neqnames["Ardra"])
    nakshatraeq.append(neqnames["Punarvasu"])
    nakshatraeq.append(neqnames["Pushya"])
    nakshatraeq.append(neqnames["Ashlesha"])
    nakshatraeq.append(neqnames["Magha"])
    nakshatraeq.append(neqnames["Purva Phalguni"])
    nakshatraeq.append(neqnames["Uttara Phalguni"])
    nakshatraeq.append(neqnames["Hasta"])
    nakshatraeq.append(neqnames["Chitra"])
    nakshatraeq.append(neqnames["Svati"])
    nakshatraeq.append(neqnames["Vishakha"])
    nakshatraeq.append(neqnames["Anuradha"])
    nakshatraeq.append(neqnames["Jyeshtha"])
    nakshatraeq.append(neqnames["Mula"])
    nakshatraeq.append(neqnames["Purva Ashadha"])
    nakshatraeq.append(neqnames["Uttara Ashadha"])
    nakshatraeq.append(neqnames["Abhijit"])
    nakshatraeq.append(neqnames["Shravana"])
    nakshatraeq.append(neqnames["Danishtha"])
    nakshatraeq.append(neqnames["Shatabhisha"])
    nakshatraeq.append(neqnames["Purva Bhadrapada"])
    nakshatraeq.append(neqnames["Uttara Bhadrapada"])
    nakshatraeq.append(neqnames["Revati"])
    nakshatraeq.append(neqnames["Ashvini"])
    nakshatraeq.append(neqnames["Bharani"])



# there are 11 karanas
# 4 happen once a lunar month
# the other 7 happen 8 times each a lunar month,
# repeating in a fixed pattern
# so the config just has 11 names
# and the function below is to organize them as
# as list of pairs in order that can easily be indexed when we know the tithi
def organize_karana(karana):
    # lets do them in order
    ret = []  # our return list or organized karana
    tmp = []  # build a list of two in tmp, then append to ret
    # then the 7 repeat in order eight times
    tmp.append(karana[0])
    for i in range(8):
        for n in range(7):
            # n+1 because, e.g., bava is at [1]
            if (
                i % 2 == 1
            ):  # i is odd, so we need to start a new pair first, if n is even
                if n % 2 == 0:
                    tmp.append(karana[n + 1])
                else:
                    tmp.append(karana[n + 1])
                    ret.append(tmp)
                    tmp = []
            else:
                if n % 2 == 0:  # n is even; append this karana to its first of the pair
                    tmp.append(karana[n + 1])
                    # this pair is done, so it can be added to ret
                    ret.append(tmp)
                    tmp = []
                else:  # n is odd; start a new pair list
                    tmp.append(karana[n + 1])
    tmp.append(karana[8])
    ret.append(tmp)
    ret.append([karana[9], karana[10]])
    return ret

