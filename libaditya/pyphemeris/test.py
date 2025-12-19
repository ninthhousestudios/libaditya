from libaditya import *

p=Planets()
c=Cusps()
con=EphContext()

signs=Signs(p,c,con)

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
