from libaditya import *

lang_file = "/home/josh/soft/libaditya/libaditya/dict/dict.abrev"

planet_names, zodiac, tithis, karanas, nakshatras, varas, yogas, adityas = read.init_names(lang_file)

acon=EphContext(timeJD=JulianDay(utcoffset=-5,timezone="EST"),
                location=Location(lat=39.95611111111111,long=-86.01277777777777,placename="Fishers, IN",timezone="EST"),
                circle=Circle.ADITYA,names=Names(nakshatras=nakshatras))
zcon=EphContext(timeJD=JulianDay(utcoffset=-5,timezone="EST"),
                location=Location(lat=39.95611111111111,long=-86.01277777777777,placename="Fishers, IN",timezone="EST"),
                circle=Circle.ZODIAC,names=Names(sign_names=const.zodiac,nakshatras=nakshatras))
bcon=EphContext(timeJD=JulianDay(utcoffset=-5,timezone="EST"),
                location=Location(lat=39.95611111111111,long=-86.01277777777777,placename="Fishers, IN",timezone="EST"),
                circle=Circle.ADITYA,sysflg=const.BARY)
bp=Planets(bcon)
bc=Cusps(bcon)
br=Rashi(bp,bc,bcon)

hcon=EphContext(timeJD=JulianDay(utcoffset=-5,timezone="EST"),
                location=Location(lat=39.95611111111111,long=-86.01277777777777,placename="Fishers, IN",timezone="EST"),
                circle=Circle.ADITYA,sysflg=const.HELIO)
hp=Planets(hcon)
hc=Cusps(hcon)
hr=Rashi(hp,hc,hcon)

joshcon=EphContext(timeJD=JulianDay(2447679.3388888887,utcoffset=-5,timezone="EST"),
                location=Location(lat=39.95611111111111,long=-86.01277777777777,placename="Fishers, IN",timezone="EST"),
                circle=Circle.ADITYA)
now=JulianDay()
jm=Moon(joshcon)

ap=Planets(acon)
ac=Cusps(acon)

zp=Planets(zcon)
zc=Cusps(zcon)

asigns=Signs(ap,ac,acon)
zsigns=Signs(zp,zc,zcon)

r=Rashi(ap,ac,acon)
zr=Rashi(zp,zc,zcon)

l=Location(long=-86.013,lat=39.956,placename="Fishers,IN",timezone="EST")
con=EphContext(ayanamsa=98,location=l)
p=Planets(con)
c=Cusps(con)

pnaks=[]
for n in p:
    pnaks.append(Nakshatra(n))

cnaks=[]
for n in c:
    cnaks.append(Nakshatra(n))
