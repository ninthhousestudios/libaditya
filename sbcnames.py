import configparser

pyphpath = "/home/josh/w/astro/soft/pyphemeris/"
eng = pyphpath + "dict.eng"
iast = pyphpath + "dict.iast"
deva = pyphpath + "dict.deva"
mixed = pyphpath + "dict.mixed"
langfile = mixed


def init_sbc_names(langfile=mixed):
    names = configparser.ConfigParser()
    names.read(langfile)

    nakshatra = []
    nakshatraeq = []
    adityas = []
    tithi = []
    vara = []
    rasis = []

    nnames = names["NAKSHATRA"]
    neqnames = names["NAKSHATRAEQ"]
    anames = names["ADITYAS"]
    tnames = names["TITHI"]
    vnames = names["VARA"]
    rnames = names["RASIS"]

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

    tithi.append(tnames["Nanda"])
    tithi.append(tnames["Bhadra"])
    tithi.append(tnames["Jaya"])
    tithi.append(tnames["Rkta"])
    tithi.append(tnames["Purna"])

    vara.append(vnames["Ravivara"])
    vara.append(vnames["Somavara"])
    vara.append(vnames["Mangalavara"])
    vara.append(vnames["Budhavara"])
    vara.append(vnames["Guruvara"])
    vara.append(vnames["Shukravara"])
    vara.append(vnames["Shanivara"])

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

    return [nakshatraeq,nakshatra,adityas,tithi,vara,rasis]



