import configparser

global nakshatra

pyphpath = "/home/josh/w/astro/soft/pyphemeris/"
eng = pyphpath + "dict.eng"
iast = pyphpath + "dict.iast"
deva = pyphpath + "dict.deva"
mixed = pyphpath + "dict.mixed.sbc"
langfile = mixed

def init_sbcaditya_names(langfile=mixed):
    names = configparser.ConfigParser()
    names.read(langfile)

    global nakshatra
    nakshatra = []

    nnames = names["NAKSHATRA"]

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
    nakshatra.append(nnames["Abhijit"])
    nakshatra.append(nnames["Shravana"])
    nakshatra.append(nnames["Danishtha"])
    nakshatra.append(nnames["Shatabhisha"])
    nakshatra.append(nnames["Purva Bhadrapada"])
    nakshatra.append(nnames["Uttara Bhadrapada"])
    nakshatra.append(nnames["Revati"])
    nakshatra.append(nnames["Ashvini"])
    nakshatra.append(nnames["Bharani"])
    return nakshatra
