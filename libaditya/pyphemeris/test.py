from libaditya import *

l=Location(long=-86.013,lat=39.956,placename="Fishers,IN")
con=EphContext(ayanamsa=98,location=l)
p=Planets(con)
c=Cusps(con)

pnaks=[]
for n in p:
    pnaks.append(Nakshatra(n))

cnaks=[]
for n in c:
    cnaks.append(Nakshatra(n))
