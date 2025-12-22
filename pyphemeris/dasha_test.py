from libaditya import *

joshcon=EphContext(timeJD=JulianDay(2447679.3388888887,utcoffset=-5,timezone="EST"),
                location=Location(lat=39.95611111111111,long=-86.01277777777777,placename="Fishers, IN",timezone="EST"),
                circle=Circle.ADITYA)
now=JulianDay()
jm=Moon(joshcon)

result = current_vimshottari_dasha(jm,now,dlevels=3)


print(result)

