
# dont want outer planets in the vargas
planets_index = [0,1,2,3,4,5,6,11,10]

def amsa_long(sign_long,amsa_width):
    """
    find the longitude in a varga sign
    sign_long is the longitude in the rashi sign of the planet
    amsa_width is the size of the amsa we are converting to
    """
    if sign_long < amsa_width:
        amsa_long(sign-long-amsa_width,amsa_width)
    else:
        # varga longitude is proportional to in-amsa longitude of the planet
        # in the rashi chart
        return (sign_long*30)/amsa_width

def d2_bphs(planets):
    """
    find the d2 according to bphs
    a planet in the first half of a sign stays in that sign
    a planet in the second half goes to the opposite sign
    """
    for i in planets_index:
        long = planets[i].longitude()
        rlong = divmod(long,30) # returns longitude as (# of rashis,longitude in current rashi)
        if rlong[1] < 15:
            # stay in same sign
            vsign = rlong[0] 
            vlong = amsa_long(rlong[1],15) # get longitude for the planet in the varga sign
        else:
            # go to opposite sign
            vsign = (rlong[0]+6)%12
            vlong = amsa_long(rlong[1],15)
        planets[i].set_varga_long((vsign*30)+vlong) # convert back to degree longitude

def d2_bphs_cusps(cusps):
    """
    find the d2 according to bphs
    a planet in the first half of a sign stays in that sign
    a planet in the second half goes to the opposite sign
    """
    for cusp in cusps: # cusps is a 12-tuple of longitudes, so cusp is a longitude
        rlong = divmod(cusp,30) # returns longitude as (# of rashis,longitude in current rashi)
        if rlong[1] < 15:
            # stay in same sign
            vsign = rlong[0] 
            vlong = amsa_long(rlong[1],15) # get longitude for the planet in the varga sign
        else:
            # go to opposite sign
            vsign = (rlong[0]+6)%12
            vlong = amsa_long(rlong[1],15)
        planets[i].set_varga_long((vsign*30)+vlong) # convert back to degree longitude
