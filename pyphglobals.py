import configparser
import swisseph as swe
import pyphutils as putil

# defaults
pyphpath = "/home/josh/w/astro/soft/pyphemeris/"
ayanamsa = 98  # new code for dhruva equatorial
show_helios = 0
show_baryos = 1
show_topo = 0
show_adityas = 0
show_equ = 0
utcoffset = -4
timezone = "EDT"
lat = round(putil.dms2dec((39, 57, 22)), 3)
long = -round((putil.dms2dec((86, 0, 46))))
alt = 252  # swe requires meters
placename = "Fishers, IN"
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
langfile = eng
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
karana = []
nakshatra = []
vara = []
yogas = []
adityas = []
signs = []


def init_names(langfile="dict.eng"):
    names = configparser.ConfigParser()
    names.read(langfile)

    global planets
    global rasis
    global karana
    global nakshatra
    global vara
    global yogas
    global adityas
    global signs

    pnames = names["PLANETS"]
    rnames = names["RASIS"]
    knames = names["KARANA"]
    nnames = names["NAKSHATRA"]
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
