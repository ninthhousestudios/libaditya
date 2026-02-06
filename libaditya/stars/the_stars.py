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

from libaditya import constants as const
from libaditya import utils

"""
FixedStars populated from ephe/sefstars.txt
this is most of the stars in there
some have more than one traditional name; in that case only one appears here
unless I have manually added a different one

my additions are first; not a lot of them
"""

import swisseph as swe

from libaditya.objects import EphContext

from .fixed_star import FixedStar
from .stellarium import Stellarium

class GalacticCenter(FixedStar): # ,SgrA*

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",SgrA*", context=context)

class GalacticPole(FixedStar): # ,GPol

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",GPol", context=context)

class Sirius(FixedStar): # ,alCMa

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",alCMa", context=context)

class Kerb(FixedStar): # ,taPeg

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",taPeg", context=context)

class DenebKaitos(FixedStar): # ,ioCet

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",ioCet", context=context)

class Algenib(FixedStar): # ,gaPeg

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",gaPeg", context=context)

class Alpheratz(FixedStar): # ,alAnd
    
    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",alAnd", context=context)

class Erakis(FixedStar): # ,muCep

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",muCep", context=context)

# these are stars used in True Sidereal midpoint method

class Acubens(FixedStar): # ,alCnc

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",alCnc", context=context)

class Denebola(FixedStar): # ,beLeo

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",beLeo", context=context)

class RijlAlAwwa(FixedStar): # ,muVir

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",muVir", context=context)

class Zubenelgenubi(FixedStar): # ,al-2Lib

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",al-2Lib", context=context)

class Dschubba(FixedStar): # ,deSco

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",deSco", context=context)

class Alnasl(FixedStar): # ,ga-2Sgr

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",ga-2Sgr", context=context)

# below is all the stars in .../ephe/sefstars.txt
# generated with libaditya/legacy/create_fixed_stars.py

class Aldebaran(FixedStar): # ,alTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alTau", context=context)

class Algol(FixedStar): # ,bePer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bePer", context=context)

class Jyeshtha(FixedStar): # ,alSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alSco", context=context)

class Magha(FixedStar): # ,alLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alLeo", context=context)

class Lubdhaka(FixedStar): # ,alCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCMa", context=context)

class Citra(FixedStar): # ,alVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alVir", context=context)

class Trappist1(FixedStar): # ,Trappist-1

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Trappist-1", context=context)

class GalacticCenter(FixedStar): # ,SgrA*

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SgrA*", context=context)

class GreatAttractor(FixedStar): # ,GA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GA", context=context)

class VirgoCluster(FixedStar): # ,VC

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",VC", context=context)

class AndromedaGalaxy(FixedStar): # ,M31

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M31", context=context)

class PraesepeCluster(FixedStar): # ,M44

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M44", context=context)

class Polaris(FixedStar): # ,alUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alUMi", context=context)

class Messier87(FixedStar): # ,M87

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M87", context=context)

class A3558(FixedStar): # ,ACO3558

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ACO3558", context=context)

class Deneb(FixedStar): # ,alCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCyg", context=context)

class Rigel(FixedStar): # ,beOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beOri", context=context)

class Mira(FixedStar): # ,omiCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiCet", context=context)

class Ain(FixedStar): # ,epTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epTau", context=context)

class Segin(FixedStar): # ,epCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCas", context=context)

class Sirrah(FixedStar): # ,alAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alAnd", context=context)

class Mirach(FixedStar): # ,beAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beAnd", context=context)

class Almach(FixedStar): # ,ga-1And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ga-1And", context=context)

class deAnd(FixedStar): # ,deAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deAnd", context=context)

class epAnd(FixedStar): # ,epAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epAnd", context=context)

class zeAnd(FixedStar): # ,zeAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeAnd", context=context)

class ioAnd(FixedStar): # ,ioAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioAnd", context=context)

class kaAnd(FixedStar): # ,kaAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaAnd", context=context)

class laAnd(FixedStar): # ,laAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laAnd", context=context)

class muAnd(FixedStar): # ,muAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muAnd", context=context)

class nuAnd(FixedStar): # ,nuAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuAnd", context=context)

class Adhil(FixedStar): # ,xiAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiAnd", context=context)

class omiAnd(FixedStar): # ,omiAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiAnd", context=context)

class piAnd(FixedStar): # ,piAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piAnd", context=context)

class rhAnd(FixedStar): # ,rhAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhAnd", context=context)

class siAnd(FixedStar): # ,siAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siAnd", context=context)

class Titawin(FixedStar): # ,upAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upAnd", context=context)

class psAnd(FixedStar): # ,psAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psAnd", context=context)

class omeAnd(FixedStar): # ,omeAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeAnd", context=context)

class Veritate(FixedStar): # ,And14

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",And14", context=context)

class Nembus(FixedStar): # ,And51

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",And51", context=context)

class alAnt(FixedStar): # ,alAnt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alAnt", context=context)

class epAnt(FixedStar): # ,epAnt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epAnt", context=context)

class thAnt(FixedStar): # ,thAnt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thAnt", context=context)

class ioAnt(FixedStar): # ,ioAnt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioAnt", context=context)

class alAps(FixedStar): # ,alAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alAps", context=context)

class beAps(FixedStar): # ,beAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beAps", context=context)

class gaAps(FixedStar): # ,gaAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaAps", context=context)

class de1Aps(FixedStar): # ,de-1Aps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",de-1Aps", context=context)

class thAps(FixedStar): # ,thAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thAps", context=context)

class ioAps(FixedStar): # ,ioAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioAps", context=context)

class ka1Aps(FixedStar): # ,ka-1Aps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ka-1Aps", context=context)

class Shravana(FixedStar): # ,alAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alAql", context=context)

class Alshain(FixedStar): # ,beAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beAql", context=context)

class Tarazed(FixedStar): # ,gaAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaAql", context=context)

class AlMizan(FixedStar): # ,deAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deAql", context=context)

class DenebelOkabBorealis(FixedStar): # ,epAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epAql", context=context)

class Dheneb(FixedStar): # ,zeAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeAql", context=context)

class Bazak(FixedStar): # ,etAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etAql", context=context)

class TseenFoo(FixedStar): # ,thAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thAql", context=context)

class AlThalimaimPosterior(FixedStar): # ,ioAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioAql", context=context)

class kaAql(FixedStar): # ,kaAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaAql", context=context)

class AlThalimaimAnterior(FixedStar): # ,laAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laAql", context=context)

class muAql(FixedStar): # ,muAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muAql", context=context)

class rhAql(FixedStar): # ,rhAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhAql", context=context)

class taAql(FixedStar): # ,taAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taAql", context=context)

class ome1Aql(FixedStar): # ,ome-1Aql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome-1Aql", context=context)

class Libertas(FixedStar): # ,xiAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiAql", context=context)

class Bered(FixedStar): # ,Aql12

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Aql12", context=context)

class Sadalmelik(FixedStar): # ,alAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alAqr", context=context)

class Sadalsuud(FixedStar): # ,beAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beAqr", context=context)

class Sadachbia(FixedStar): # ,gaAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaAqr", context=context)

class Skat(FixedStar): # ,deAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deAqr", context=context)

class Altager(FixedStar): # ,epAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epAqr", context=context)

class Sadaltager(FixedStar): # ,ze-1Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ze-1Aqr", context=context)

class Deli(FixedStar): # ,etAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etAqr", context=context)

class Ancha(FixedStar): # ,thAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thAqr", context=context)

class ioAqr(FixedStar): # ,ioAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioAqr", context=context)

class Situla(FixedStar): # ,kaAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaAqr", context=context)

class Shatabhishak(FixedStar): # ,laAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laAqr", context=context)

class muAqr(FixedStar): # ,muAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muAqr", context=context)

class Albulaan(FixedStar): # ,nuAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuAqr", context=context)

class Seat(FixedStar): # ,piAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piAqr", context=context)

class siAqr(FixedStar): # ,siAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siAqr", context=context)

class ta2Aqr(FixedStar): # ,ta-2Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-2Aqr", context=context)

class phAqr(FixedStar): # ,phAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phAqr", context=context)

class Bunda(FixedStar): # ,xiAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiAqr", context=context)

class upAqr(FixedStar): # ,upAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upAqr", context=context)

class ps1Aqr(FixedStar): # ,ps-1Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ps-1Aqr", context=context)

class ps3Aqr(FixedStar): # ,ps-3Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ps-3Aqr", context=context)

class ome2Aqr(FixedStar): # ,ome-2Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome-2Aqr", context=context)

class Aqr3(FixedStar): # ,Aqr3

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Aqr3", context=context)

class Aqr88(FixedStar): # ,Aqr88

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Aqr88", context=context)

class Aqr98(FixedStar): # ,Aqr98

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Aqr98", context=context)

class Ara(FixedStar): # ,alAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alAra", context=context)

class beAra(FixedStar): # ,beAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beAra", context=context)

class gaAra(FixedStar): # ,gaAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaAra", context=context)

class deAra(FixedStar): # ,deAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deAra", context=context)

class ep1Ara(FixedStar): # ,ep-1Ara

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ep-1Ara", context=context)

class zeAra(FixedStar): # ,zeAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeAra", context=context)

class etAra(FixedStar): # ,etAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etAra", context=context)

class thAra(FixedStar): # ,thAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thAra", context=context)

class Cervantes(FixedStar): # ,muAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muAra", context=context)

class Hamal(FixedStar): # ,alAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alAri", context=context)

class Ashvini(FixedStar): # ,beAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beAri", context=context)

class Mesarthim(FixedStar): # ,gaAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaAri", context=context)

class Botein(FixedStar): # ,deAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deAri", context=context)

class zeAri(FixedStar): # ,zeAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeAri", context=context)

class thAri(FixedStar): # ,thAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thAri", context=context)

class nuAri(FixedStar): # ,nuAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuAri", context=context)

class siAri(FixedStar): # ,siAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siAri", context=context)

class ta1Ari(FixedStar): # ,ta-1Ari

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-1Ari", context=context)

class LiliiBorea(FixedStar): # ,Ari39

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Ari39", context=context)

class Bharani(FixedStar): # ,Ari41

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Ari41", context=context)

class Brahmahridaya(FixedStar): # ,alAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alAur", context=context)

class Menkalinan(FixedStar): # ,beAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beAur", context=context)

class Prijipati(FixedStar): # ,deAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deAur", context=context)

class AlAnz(FixedStar): # ,epAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epAur", context=context)

class Saclateni(FixedStar): # ,zeAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeAur", context=context)

class Haedus(FixedStar): # ,etAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etAur", context=context)

class Mahasim(FixedStar): # ,thAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thAur", context=context)

class AlKhabdhilinan(FixedStar): # ,ioAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioAur", context=context)

class kaAur(FixedStar): # ,kaAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaAur", context=context)

class laAur(FixedStar): # ,laAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laAur", context=context)

class muAur(FixedStar): # ,muAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muAur", context=context)

class nuAur(FixedStar): # ,nuAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuAur", context=context)

class xiAur(FixedStar): # ,xiAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiAur", context=context)

class omiAur(FixedStar): # ,omiAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiAur", context=context)

class chAur(FixedStar): # ,chAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chAur", context=context)

class ps1Aur(FixedStar): # ,ps-1Aur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ps-1Aur", context=context)

class ps5Aur(FixedStar): # ,ps-5Aur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ps-5Aur", context=context)

class ps6Aur(FixedStar): # ,ps-6Aur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ps-6Aur", context=context)

class Svati(FixedStar): # ,alBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alBoo", context=context)

class Nekkar(FixedStar): # ,beBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beBoo", context=context)

class Haris(FixedStar): # ,gaBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaBoo", context=context)

class Princeps(FixedStar): # ,deBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deBoo", context=context)

class Pulcherrima(FixedStar): # ,epBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epBoo", context=context)

class zeBoo(FixedStar): # ,zeBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeBoo", context=context)

class Muphrid(FixedStar): # ,etBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etBoo", context=context)

class AsellusPrimus(FixedStar): # ,thBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thBoo", context=context)

class AsellusSecundus(FixedStar): # ,ioBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioBoo", context=context)

class AsellusTertius(FixedStar): # ,ka-2Boo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ka-2Boo", context=context)

class Xuange(FixedStar): # ,laBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laBoo", context=context)

class Alkalurops(FixedStar): # ,mu-1Boo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu-1Boo", context=context)

class nu1Boo(FixedStar): # ,nu-1Boo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu-1Boo", context=context)

class AlHamalain(FixedStar): # ,rhBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhBoo", context=context)

class HemeleinSecunda(FixedStar): # ,siBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siBoo", context=context)

class taBoo(FixedStar): # ,taBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taBoo", context=context)

class Ceginus(FixedStar): # ,phBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phBoo", context=context)

class psBoo(FixedStar): # ,psBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psBoo", context=context)

class Merga(FixedStar): # ,Boo38

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Boo38", context=context)

class alCae(FixedStar): # ,alCae

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCae", context=context)

class beCae(FixedStar): # ,beCae

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCae", context=context)

class deCae(FixedStar): # ,deCae

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCae", context=context)

class alCam(FixedStar): # ,alCam

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCam", context=context)

class beCam(FixedStar): # ,beCam

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCam", context=context)

class gaCam(FixedStar): # ,gaCam

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCam", context=context)

class Cam2(FixedStar): # ,Cam2

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Cam2", context=context)

class Cam7(FixedStar): # ,Cam7

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Cam7", context=context)

class Tonatiuh(FixedStar): # ,HR4609

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HR4609", context=context)

class GiediPrima(FixedStar): # ,al-1Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",al-1Cap", context=context)

class GiediSecunda(FixedStar): # ,al-2Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",al-2Cap", context=context)

class Dabih(FixedStar): # ,beCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCap", context=context)

class Dabih(FixedStar): # ,be-1Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",be-1Cap", context=context)

class Nashira(FixedStar): # ,gaCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCap", context=context)

class DenebAlgedi(FixedStar): # ,deCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCap", context=context)

class Castra(FixedStar): # ,epCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCap", context=context)

class Marakk(FixedStar): # ,zeCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCap", context=context)

class Armus(FixedStar): # ,etCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCap", context=context)

class Dorsum(FixedStar): # ,thCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCap", context=context)

class ioCap(FixedStar): # ,ioCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioCap", context=context)

class laCap(FixedStar): # ,laCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laCap", context=context)

class muCap(FixedStar): # ,muCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muCap", context=context)

class Alshat(FixedStar): # ,nuCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuCap", context=context)

class Oculus(FixedStar): # ,piCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piCap", context=context)

class Bos(FixedStar): # ,rhCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhCap", context=context)

class Pazhan(FixedStar): # ,psCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psCap", context=context)

class upCap(FixedStar): # ,upCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upCap", context=context)

class BatenAlgiedi(FixedStar): # ,omeCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeCap", context=context)

class Cap24(FixedStar): # ,Cap24

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Cap24", context=context)

class Cap36(FixedStar): # ,Cap36

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Cap36", context=context)

class Agastya(FixedStar): # ,alCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCar", context=context)

class Miaplacidus(FixedStar): # ,beCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCar", context=context)

class Avior(FixedStar): # ,epCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCar", context=context)

class Foramen(FixedStar): # ,etCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCar", context=context)

class VathorzPosterior(FixedStar): # ,thCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCar", context=context)

class Aspidiske(FixedStar): # ,ioCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioCar", context=context)

class Drys(FixedStar): # ,chCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chCar", context=context)

class Simiram(FixedStar): # ,omeCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeCar", context=context)

class VathorzPrior(FixedStar): # ,upCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upCar", context=context)

class qCar(FixedStar): # ,qCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",qCar", context=context)

class Schedir(FixedStar): # ,alCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCas", context=context)

class Caph(FixedStar): # ,beCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCas", context=context)

class Cih(FixedStar): # ,gaCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCas", context=context)

class Rucha(FixedStar): # ,deCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCas", context=context)

class Fulu(FixedStar): # ,zeCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCas", context=context)

class Achird(FixedStar): # ,etCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCas", context=context)

class kaCas(FixedStar): # ,kaCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaCas", context=context)

class Marfak(FixedStar): # ,muCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muCas", context=context)

class omiCas(FixedStar): # ,omiCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiCas", context=context)

class rhCas(FixedStar): # ,rhCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhCas", context=context)

class psCas(FixedStar): # ,psCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psCas", context=context)

class Castula(FixedStar): # ,up-2Cas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",up-2Cas", context=context)

class ProximaCentauri(FixedStar): # ,alCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCen", context=context)

class Agena(FixedStar): # ,beCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCen", context=context)

class Muhlifain(FixedStar): # ,gaCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCen", context=context)

class deCen(FixedStar): # ,deCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCen", context=context)

class Birdun(FixedStar): # ,epCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCen", context=context)

class zeCen(FixedStar): # ,zeCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCen", context=context)

class etCen(FixedStar): # ,etCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCen", context=context)

class Menkent(FixedStar): # ,thCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCen", context=context)

class Alhakim(FixedStar): # ,ioCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioCen", context=context)

class KeKwan(FixedStar): # ,kaCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaCen", context=context)

class Mati(FixedStar): # ,laCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laCen", context=context)

class muCen(FixedStar): # ,muCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muCen", context=context)

class KabkentSecunda(FixedStar): # ,nuCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuCen", context=context)

class xi2Cen(FixedStar): # ,xi-2Cen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xi-2Cen", context=context)

class piCen(FixedStar): # ,piCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piCen", context=context)

class siCen(FixedStar): # ,siCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siCen", context=context)

class KabkentTertia(FixedStar): # ,phCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phCen", context=context)

class psCen(FixedStar): # ,psCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psCen", context=context)

class dCen(FixedStar): # ,dCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dCen", context=context)

class rhCen(FixedStar): # ,rhCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhCen", context=context)

class ProximaCentauri(FixedStar): # ,V645 Cen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",V645 Cen", context=context)

class Alderamin(FixedStar): # ,alCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCep", context=context)

class Alfirk(FixedStar): # ,beCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCep", context=context)

class Errai(FixedStar): # ,gaCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCep", context=context)

class Alredif(FixedStar): # ,deCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCep", context=context)

class Phicareus(FixedStar): # ,epCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCep", context=context)

class Kurhah(FixedStar): # ,zeCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCep", context=context)

class Alagemin(FixedStar): # ,etCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCep", context=context)

class Alkidr(FixedStar): # ,thCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCep", context=context)

class Alvahet(FixedStar): # ,ioCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioCep", context=context)

class kaCep(FixedStar): # ,kaCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaCep", context=context)

class TheGarnetStar(FixedStar): # ,muCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muCep", context=context)

class nuCep(FixedStar): # ,nuCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuCep", context=context)

class Alkurhah(FixedStar): # ,xiCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiCep", context=context)

class AlKalbalRai(FixedStar): # ,rhCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhCep", context=context)

class Menkar(FixedStar): # ,alCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCet", context=context)

class Difda(FixedStar): # ,beCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCet", context=context)

class Kaffaljidhma(FixedStar): # ,gaCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCet", context=context)

class Phycochroma(FixedStar): # ,deCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCet", context=context)

class BatenKaitos(FixedStar): # ,zeCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCet", context=context)

class DenebAlgenubi(FixedStar): # ,etCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCet", context=context)

class Altawk(FixedStar): # ,thCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCet", context=context)

class Shemali(FixedStar): # ,ioCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioCet", context=context)

class Menkar(FixedStar): # ,laCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laCet", context=context)

class muCet(FixedStar): # ,muCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muCet", context=context)

class nuCet(FixedStar): # ,nuCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuCet", context=context)

class xi1Cet(FixedStar): # ,xi-1Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xi-1Cet", context=context)

class xi2Cet(FixedStar): # ,xi-2Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xi-2Cet", context=context)

class AlSadralKetus(FixedStar): # ,piCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piCet", context=context)

class rhCet(FixedStar): # ,rhCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhCet", context=context)

class siCet(FixedStar): # ,siCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siCet", context=context)

class taCet(FixedStar): # ,taCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taCet", context=context)

class AbyssusAqueus(FixedStar): # ,upCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upCet", context=context)

class AlNitham(FixedStar): # ,ph-1Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ph-1Cet", context=context)

class ph2Cet(FixedStar): # ,ph-2Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ph-2Cet", context=context)

class chCet(FixedStar): # ,chCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chCet", context=context)

class alCha(FixedStar): # ,alCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCha", context=context)

class beCha(FixedStar): # ,beCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCha", context=context)

class gaCha(FixedStar): # ,gaCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCha", context=context)

class de2Cha(FixedStar): # ,de-2Cha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",de-2Cha", context=context)

class etCha(FixedStar): # ,etCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCha", context=context)

class thCha(FixedStar): # ,thCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCha", context=context)

class piCha(FixedStar): # ,piCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piCha", context=context)

class alCir(FixedStar): # ,alCir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCir", context=context)

class beCir(FixedStar): # ,beCir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCir", context=context)

class Murzims(FixedStar): # ,beCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCMa", context=context)

class Isis(FixedStar): # ,gaCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCMa", context=context)

class Wezen(FixedStar): # ,deCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCMa", context=context)

class Adhara(FixedStar): # ,epCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCMa", context=context)

class Furud(FixedStar): # ,zeCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCMa", context=context)

class Aludra(FixedStar): # ,etCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCMa", context=context)

class kaCMa(FixedStar): # ,kaCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaCMa", context=context)

class xi2CMa(FixedStar): # ,xi-2CMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xi-2CMa", context=context)

class omi2CMa(FixedStar): # ,omi-2CMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omi-2CMa", context=context)

class Unurgunite(FixedStar): # ,siCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siCMa", context=context)

class thCMa(FixedStar): # ,thCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCMa", context=context)

class Procyon(FixedStar): # ,alCMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCMi", context=context)

class Gomeisa(FixedStar): # ,beCMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCMi", context=context)

class zeCMi(FixedStar): # ,zeCMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCMi", context=context)

class Ashlesha(FixedStar): # ,alCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCnc", context=context)

class AlTarf(FixedStar): # ,beCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCnc", context=context)

class AsellusBorealis(FixedStar): # ,gaCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCnc", context=context)

class Pushya(FixedStar): # ,deCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCnc", context=context)

class Meleph(FixedStar): # ,epCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCnc", context=context)

class Tegmine(FixedStar): # ,zeCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCnc", context=context)

class etCnc(FixedStar): # ,etCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCnc", context=context)

class Decapoda(FixedStar): # ,ioCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioCnc", context=context)

class kaCnc(FixedStar): # ,kaCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaCnc", context=context)

class xiCnc(FixedStar): # ,xiCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiCnc", context=context)

class si3Cnc(FixedStar): # ,si-3Cnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",si-3Cnc", context=context)

class chCnc(FixedStar): # ,chCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chCnc", context=context)

class ome1Cnc(FixedStar): # ,ome-1Cnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome-1Cnc", context=context)

class Copernicus(FixedStar): # ,Cnc55

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Cnc55", context=context)

class Phact(FixedStar): # ,alCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCol", context=context)

class Wazn(FixedStar): # ,beCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCol", context=context)

class GhusnalZaitun(FixedStar): # ,deCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCol", context=context)

class gaCol(FixedStar): # ,gaCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCol", context=context)

class etCol(FixedStar): # ,etCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCol", context=context)

class AlKurud(FixedStar): # ,kaCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaCol", context=context)

class Tsze(FixedStar): # ,laCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laCol", context=context)

class omiCol(FixedStar): # ,omiCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiCol", context=context)

class epCol(FixedStar): # ,epCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCol", context=context)

class Diadem(FixedStar): # ,alCom

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCom", context=context)

class Aldafirah(FixedStar): # ,beCom

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCom", context=context)

class Kissin(FixedStar): # ,gaCom

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCom", context=context)

class Gemma(FixedStar): # ,alCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCrB", context=context)

class Nusakan(FixedStar): # ,beCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCrB", context=context)

class epCrB(FixedStar): # ,epCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCrB", context=context)

class thCrB(FixedStar): # ,thCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCrB", context=context)

class kaC1GrB(FixedStar): # ,kaC1GrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaC1GrB", context=context)

class BlazeStar(FixedStar): # ,tCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tCrB", context=context)

class taCrB(FixedStar): # ,taCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taCrB", context=context)

class gaCrB(FixedStar): # ,gaCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCrB", context=context)

class deCrB(FixedStar): # ,deCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCrB", context=context)

class ioCrB(FixedStar): # ,ioCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioCrB", context=context)

class Meridiana(FixedStar): # ,alCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCrA", context=context)

class et1CrA(FixedStar): # ,et-1CrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",et-1CrA", context=context)

class thCrA(FixedStar): # ,thCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCrA", context=context)

class epCrA(FixedStar): # ,epCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCrA", context=context)

class gaCrA(FixedStar): # ,gaCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCrA", context=context)

class beCrA(FixedStar): # ,beCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCrA", context=context)

class deCrA(FixedStar): # ,deCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCrA", context=context)

class zeCrA(FixedStar): # ,zeCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCrA", context=context)

class Alkes(FixedStar): # ,alCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCrt", context=context)

class Alsharasif(FixedStar): # ,beCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCrt", context=context)

class gaCrt(FixedStar): # ,gaCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCrt", context=context)

class Labrum(FixedStar): # ,deCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCrt", context=context)

class epCrt(FixedStar): # ,epCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCrt", context=context)

class etCrt(FixedStar): # ,etCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCrt", context=context)

class thCrt(FixedStar): # ,thCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCrt", context=context)

class zeCrt(FixedStar): # ,zeCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCrt", context=context)

class Mimosa(FixedStar): # ,beCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCru", context=context)

class Gacrux(FixedStar): # ,gaCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCru", context=context)

class Decrux(FixedStar): # ,deCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCru", context=context)

class Ginan(FixedStar): # ,epCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCru", context=context)

class Alchita(FixedStar): # ,alCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alCrv", context=context)

class Kraz(FixedStar): # ,beCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCrv", context=context)

class GienahCorvi(FixedStar): # ,gaCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCrv", context=context)

class Hasta(FixedStar): # ,deCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCrv", context=context)

class Minkar(FixedStar): # ,epCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCrv", context=context)

class AvisSatyra(FixedStar): # ,etCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCrv", context=context)

class CorCaroli(FixedStar): # ,al-2CVn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",al-2CVn", context=context)

class Chara(FixedStar): # ,beCVn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beCVn", context=context)

class Albireo(FixedStar): # ,be-1Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",be-1Cyg", context=context)

class Sadr(FixedStar): # ,gaCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaCyg", context=context)

class AlFawaris(FixedStar): # ,deCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deCyg", context=context)

class Aljanah(FixedStar): # ,epCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epCyg", context=context)

class zeCyg(FixedStar): # ,zeCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeCyg", context=context)

class etCyg(FixedStar): # ,etCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etCyg", context=context)

class thCyg(FixedStar): # ,thCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thCyg", context=context)

class io2Cyg(FixedStar): # ,io-2Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",io-2Cyg", context=context)

class kaCyg(FixedStar): # ,kaCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaCyg", context=context)

class nuCyg(FixedStar): # ,nuCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuCyg", context=context)

class xiCyg(FixedStar): # ,xiCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiCyg", context=context)

class Azelfafage(FixedStar): # ,pi-1Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-1Cyg", context=context)

class pi2Cyg(FixedStar): # ,pi-2Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-2Cyg", context=context)

class rhCyg(FixedStar): # ,rhCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhCyg", context=context)

class siCyg(FixedStar): # ,siCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siCyg", context=context)

class upCyg(FixedStar): # ,upCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upCyg", context=context)

class RuchbahI(FixedStar): # ,ome-1Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome-1Cyg", context=context)

class RuchbahII(FixedStar): # ,ome-2Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome-2Cyg", context=context)

class Cyg61(FixedStar): # ,Cyg61

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Cyg61", context=context)

class CygA61(FixedStar): # ,CygA61

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",CygA61", context=context)

class Cyg34(FixedStar): # ,Cyg34

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Cyg34", context=context)

class Sualocin(FixedStar): # ,alDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alDel", context=context)

class Shravishtha(FixedStar): # ,beDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beDel", context=context)

class ga2Del(FixedStar): # ,ga-2Del

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ga-2Del", context=context)

class deDel(FixedStar): # ,deDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deDel", context=context)

class Aldulfin(FixedStar): # ,epDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epDel", context=context)

class kaDel(FixedStar): # ,kaDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaDel", context=context)

class Musica(FixedStar): # ,Del18

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Del18", context=context)

class alDor(FixedStar): # ,alDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alDor", context=context)

class beDor(FixedStar): # ,beDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beDor", context=context)

class gaDor(FixedStar): # ,gaDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaDor", context=context)

class deDor(FixedStar): # ,deDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deDor", context=context)

class zeDor(FixedStar): # ,zeDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeDor", context=context)

class thDor(FixedStar): # ,thDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thDor", context=context)

class nuDor(FixedStar): # ,nuDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuDor", context=context)

class Sanduleak(FixedStar): # ,SN1987A

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SN1987A", context=context)

class Dhruva(FixedStar): # ,alDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alDra", context=context)

class Rastaban(FixedStar): # ,beDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beDra", context=context)

class Etamin(FixedStar): # ,gaDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaDra", context=context)

class Altais(FixedStar): # ,deDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deDra", context=context)

class Tyl(FixedStar): # ,epDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epDra", context=context)

class Aldhibah(FixedStar): # ,zeDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeDra", context=context)

class thDra(FixedStar): # ,thDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thDra", context=context)

class EdAsich(FixedStar): # ,ioDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioDra", context=context)

class Ketu(FixedStar): # ,kaDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaDra", context=context)

class Gianfar(FixedStar): # ,laDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laDra", context=context)

class Alrakis(FixedStar): # ,muDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muDra", context=context)

class Kuma(FixedStar): # ,nu-1Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu-1Dra", context=context)

class Kuma(FixedStar): # ,nu-2Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu-2Dra", context=context)

class Grumium(FixedStar): # ,xiDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiDra", context=context)

class omiDra(FixedStar): # ,omiDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiDra", context=context)

class Athafi(FixedStar): # ,siDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siDra", context=context)

class taDra(FixedStar): # ,taDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taDra", context=context)

class upDra(FixedStar): # ,upDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upDra", context=context)

class BatentabanBorealis(FixedStar): # ,chDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chDra", context=context)

class Dziban(FixedStar): # ,ps-1Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ps-1Dra", context=context)

class omeDra(FixedStar): # ,omeDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeDra", context=context)

class Athebyne(FixedStar): # ,etDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etDra", context=context)

class BatentabanAustralis(FixedStar): # ,phDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phDra", context=context)

class Tianyi(FixedStar): # ,Dra7

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Dra7", context=context)

class Taiyi(FixedStar): # ,Dra8

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Dra8", context=context)

class Fafnir(FixedStar): # ,Dra42

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Dra42", context=context)

class Kitalpha(FixedStar): # ,alEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alEqu", context=context)

class gaEqu(FixedStar): # ,gaEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaEqu", context=context)

class deEqu(FixedStar): # ,deEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deEqu", context=context)

class beEqu(FixedStar): # ,beEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beEqu", context=context)

class Achernar(FixedStar): # ,alEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alEri", context=context)

class Cursa(FixedStar): # ,beEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beEri", context=context)

class Zaurak(FixedStar): # ,gaEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaEri", context=context)

class Rana(FixedStar): # ,deEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deEri", context=context)

class Ran(FixedStar): # ,epEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epEri", context=context)

class Azha(FixedStar): # ,etEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etEri", context=context)

class Acamar(FixedStar): # ,th-1Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",th-1Eri", context=context)

class Zibal(FixedStar): # ,zeEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeEri", context=context)

class ioEri(FixedStar): # ,ioEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioEri", context=context)

class kaEri(FixedStar): # ,kaEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaEri", context=context)

class laEri(FixedStar): # ,laEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laEri", context=context)

class muEri(FixedStar): # ,muEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muEri", context=context)

class nuEri(FixedStar): # ,nuEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuEri", context=context)

class xiEri(FixedStar): # ,xiEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiEri", context=context)

class Beid(FixedStar): # ,omi-1Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omi-1Eri", context=context)

class Keid(FixedStar): # ,omi-2Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omi-2Eri", context=context)

class phEri(FixedStar): # ,phEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phEri", context=context)

class ta1Eri(FixedStar): # ,ta-1Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-1Eri", context=context)

class Angetenar(FixedStar): # ,ta-2Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-2Eri", context=context)

class ta3Eri(FixedStar): # ,ta-3Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-3Eri", context=context)

class ta4Eri(FixedStar): # ,ta-4Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-4Eri", context=context)

class ta5Eri(FixedStar): # ,ta-5Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-5Eri", context=context)

class ta6Eri(FixedStar): # ,ta-6Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-6Eri", context=context)

class ta8Eri(FixedStar): # ,ta-8Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-8Eri", context=context)

class ta9Eri(FixedStar): # ,ta-9Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-9Eri", context=context)

class up1Eri(FixedStar): # ,up-1Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",up-1Eri", context=context)

class Theemin(FixedStar): # ,up-2Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",up-2Eri", context=context)

class Beemim(FixedStar): # ,up-3Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",up-3Eri", context=context)

class up4Eri(FixedStar): # ,up-4Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",up-4Eri", context=context)

class chEri(FixedStar): # ,chEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chEri", context=context)

class Sceptrum(FixedStar): # ,Eri53

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Eri53", context=context)

class omeEri(FixedStar): # ,omeEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeEri", context=context)

class piEri(FixedStar): # ,piEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piEri", context=context)

class gEri(FixedStar): # ,gEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gEri", context=context)

class fEri(FixedStar): # ,fEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",fEri", context=context)

class yEri(FixedStar): # ,yEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",yEri", context=context)

class eEri(FixedStar): # ,eEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eEri", context=context)

class sEri(FixedStar): # ,sEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sEri", context=context)

class Dalim(FixedStar): # ,alFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alFor", context=context)

class beFor(FixedStar): # ,beFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beFor", context=context)

class deFor(FixedStar): # ,deFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deFor", context=context)

class kaFor(FixedStar): # ,kaFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaFor", context=context)

class la1For(FixedStar): # ,la-1For

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",la-1For", context=context)

class muFor(FixedStar): # ,muFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muFor", context=context)

class nuFor(FixedStar): # ,nuFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuFor", context=context)

class taFor(FixedStar): # ,taFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taFor", context=context)

class Castor(FixedStar): # ,alGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alGem", context=context)

class Punarvasu(FixedStar): # ,beGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beGem", context=context)

class Almeisan(FixedStar): # ,gaGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaGem", context=context)

class Wasat(FixedStar): # ,deGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deGem", context=context)

class Mebsuta(FixedStar): # ,epGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epGem", context=context)

class Mekbuda(FixedStar): # ,zeGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeGem", context=context)

class PropusetaGem(FixedStar): # ,etGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etGem", context=context)

class Nageba(FixedStar): # ,thGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thGem", context=context)

class PropusiotGem(FixedStar): # ,ioGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioGem", context=context)

class AlKrikab(FixedStar): # ,kaGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaGem", context=context)

class Alkibash(FixedStar): # ,laGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laGem", context=context)

class Tejat(FixedStar): # ,muGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muGem", context=context)

class nuGem(FixedStar): # ,nuGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuGem", context=context)

class Alzirr(FixedStar): # ,xiGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiGem", context=context)

class Jishui(FixedStar): # ,omiGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiGem", context=context)

class piGem(FixedStar): # ,piGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piGem", context=context)

class rhGem(FixedStar): # ,rhGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhGem", context=context)

class siGem(FixedStar): # ,siGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siGem", context=context)

class taGem(FixedStar): # ,taGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taGem", context=context)

class upGem(FixedStar): # ,upGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upGem", context=context)

class phGem(FixedStar): # ,phGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phGem", context=context)

class chGem(FixedStar): # ,chGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chGem", context=context)

class omeGem(FixedStar): # ,omeGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeGem", context=context)

class Alnair(FixedStar): # ,alGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alGru", context=context)

class Tiaki(FixedStar): # ,beGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beGru", context=context)

class RasAlkurki(FixedStar): # ,gaGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaGru", context=context)

class de1Gru(FixedStar): # ,de-1Gru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",de-1Gru", context=context)

class de2Gru(FixedStar): # ,de-2Gru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",de-2Gru", context=context)

class epGru(FixedStar): # ,epGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epGru", context=context)

class thGru(FixedStar): # ,thGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thGru", context=context)

class zeGru(FixedStar): # ,zeGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeGru", context=context)

class ioGru(FixedStar): # ,ioGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioGru", context=context)

class laGru(FixedStar): # ,laGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laGru", context=context)

class nuGru(FixedStar): # ,nuGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuGru", context=context)

class omiGru(FixedStar): # ,omiGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiGru", context=context)

class Kornephoros(FixedStar): # ,beHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beHer", context=context)

class Rasalgethi(FixedStar): # ,alHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alHer", context=context)

class al1Her(FixedStar): # ,al-1Her

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",al-1Her", context=context)

class Rutilicus(FixedStar): # ,zeHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeHer", context=context)

class gaHer(FixedStar): # ,gaHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaHer", context=context)

class Sarin(FixedStar): # ,deHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deHer", context=context)

class KajamepsHer(FixedStar): # ,epHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epHer", context=context)

class Sofian(FixedStar): # ,etHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etHer", context=context)

class RukbalgethiGenubi(FixedStar): # ,thHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thHer", context=context)

class AlJathiyah(FixedStar): # ,ioHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioHer", context=context)

class Marsic(FixedStar): # ,kaHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaHer", context=context)

class Maasym(FixedStar): # ,laHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laHer", context=context)

class Melkarth(FixedStar): # ,muHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muHer", context=context)

class xiHer(FixedStar): # ,xiHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiHer", context=context)

class omiHer(FixedStar): # ,omiHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiHer", context=context)

class Fudail(FixedStar): # ,piHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piHer", context=context)

class siHer(FixedStar): # ,siHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siHer", context=context)

class RukbalgethiShemali(FixedStar): # ,taHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taHer", context=context)

class phHer(FixedStar): # ,phHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phHer", context=context)

class chHer(FixedStar): # ,chHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chHer", context=context)

class Cujam(FixedStar): # ,omeHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeHer", context=context)

class rhHer(FixedStar): # ,rhHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhHer", context=context)

class Ogma(FixedStar): # ,HD149026

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HD149026", context=context)

class Apex(FixedStar): # ,Apex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Apex", context=context)

class alHor(FixedStar): # ,alHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alHor", context=context)

class zeHor(FixedStar): # ,zeHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeHor", context=context)

class laHor(FixedStar): # ,laHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laHor", context=context)

class muHor(FixedStar): # ,muHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muHor", context=context)

class ioHor(FixedStar): # ,ioHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioHor", context=context)

class etHor(FixedStar): # ,etHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etHor", context=context)

class beHor(FixedStar): # ,beHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beHor", context=context)

class CorHydrae(FixedStar): # ,alHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alHya", context=context)

class beHya(FixedStar): # ,beHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beHya", context=context)

class DhanabalShuja(FixedStar): # ,gaHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaHya", context=context)

class Mautinah(FixedStar): # ,deHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deHya", context=context)

class Ashlesha(FixedStar): # ,epHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epHya", context=context)

class Hydrobius(FixedStar): # ,zeHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeHya", context=context)

class etHya(FixedStar): # ,etHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etHya", context=context)

class thHya(FixedStar): # ,thHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thHya", context=context)

class ioHya(FixedStar): # ,ioHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioHya", context=context)

class kaHya(FixedStar): # ,kaHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaHya", context=context)

class laHya(FixedStar): # ,laHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laHya", context=context)

class muHya(FixedStar): # ,muHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muHya", context=context)

class Pleura(FixedStar): # ,nuHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuHya", context=context)

class xiHya(FixedStar): # ,xiHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiHya", context=context)

class omiHya(FixedStar): # ,omiHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiHya", context=context)

class Sataghni(FixedStar): # ,piHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piHya", context=context)

class Minchir(FixedStar): # ,siHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siHya", context=context)

class Ukdahprima(FixedStar): # ,ta-1Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-1Hya", context=context)

class Ukdahsecunda(FixedStar): # ,ta-2Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-2Hya", context=context)

class Zhang(FixedStar): # ,up-1Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",up-1Hya", context=context)

class up2Hya(FixedStar): # ,up-2Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",up-2Hya", context=context)

class ch1Hya(FixedStar): # ,ch-1Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ch-1Hya", context=context)

class alHyi(FixedStar): # ,alHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alHyi", context=context)

class beHyi(FixedStar): # ,beHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beHyi", context=context)

class gaHyi(FixedStar): # ,gaHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaHyi", context=context)

class deHyi(FixedStar): # ,deHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deHyi", context=context)

class epHyi(FixedStar): # ,epHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epHyi", context=context)

class et2Hyi(FixedStar): # ,et-2Hyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",et-2Hyi", context=context)

class thHyi(FixedStar): # ,thHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thHyi", context=context)

class ioHyi(FixedStar): # ,ioHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioHyi", context=context)

class kaHyi(FixedStar): # ,kaHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaHyi", context=context)

class laHyi(FixedStar): # ,laHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laHyi", context=context)

class muHyi(FixedStar): # ,muHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muHyi", context=context)

class alInd(FixedStar): # ,alInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alInd", context=context)

class beInd(FixedStar): # ,beInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beInd", context=context)

class gaInd(FixedStar): # ,gaInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaInd", context=context)

class deInd(FixedStar): # ,deInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deInd", context=context)

class epInd(FixedStar): # ,epInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epInd", context=context)

class etInd(FixedStar): # ,etInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etInd", context=context)

class thInd(FixedStar): # ,thInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thInd", context=context)

class omiInd(FixedStar): # ,omiInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiInd", context=context)

class rhInd(FixedStar): # ,rhInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhInd", context=context)

class alLac(FixedStar): # ,alLac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alLac", context=context)

class beLac(FixedStar): # ,beLac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beLac", context=context)

class Lac1(FixedStar): # ,Lac1

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lac1", context=context)

class Lac2(FixedStar): # ,Lac2

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lac2", context=context)

class Lac4(FixedStar): # ,Lac4

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lac4", context=context)

class Lac5(FixedStar): # ,Lac5

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lac5", context=context)

class Lac6(FixedStar): # ,Lac6

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lac6", context=context)

class Uttaraphalguni(FixedStar): # ,beLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beLeo", context=context)

class Algieba(FixedStar): # ,ga-1Leo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ga-1Leo", context=context)

class Purvaphalguni(FixedStar): # ,deLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deLeo", context=context)

class RasElasedAustralis(FixedStar): # ,epLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epLeo", context=context)

class Adhafera(FixedStar): # ,zeLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeLeo", context=context)

class AlJabhah(FixedStar): # ,etLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etLeo", context=context)

class TszeTseang(FixedStar): # ,ioLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioLeo", context=context)

class AlMinliaralAsad(FixedStar): # ,kaLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaLeo", context=context)

class Alterf(FixedStar): # ,laLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laLeo", context=context)

class Rasalas(FixedStar): # ,muLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muLeo", context=context)

class xiLeo(FixedStar): # ,xiLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiLeo", context=context)

class Subra(FixedStar): # ,omiLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiLeo", context=context)

class Shishimai(FixedStar): # ,siLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siLeo", context=context)

class Chort(FixedStar): # ,thLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thLeo", context=context)

class piLeo(FixedStar): # ,piLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piLeo", context=context)

class Shir(FixedStar): # ,rhLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhLeo", context=context)

class taLeo(FixedStar): # ,taLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taLeo", context=context)

class upLeo(FixedStar): # ,upLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upLeo", context=context)

class phLeo(FixedStar): # ,phLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phLeo", context=context)

class chLeo(FixedStar): # ,chLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chLeo", context=context)

class psLeo(FixedStar): # ,psLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psLeo", context=context)

class Arneb(FixedStar): # ,alLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alLep", context=context)

class Nihal(FixedStar): # ,beLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beLep", context=context)

class gaLep(FixedStar): # ,gaLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaLep", context=context)

class deLep(FixedStar): # ,deLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deLep", context=context)

class Sasin(FixedStar): # ,epLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epLep", context=context)

class zeLep(FixedStar): # ,zeLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeLep", context=context)

class etLep(FixedStar): # ,etLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etLep", context=context)

class laLep(FixedStar): # ,laLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laLep", context=context)

class muLep(FixedStar): # ,muLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muLep", context=context)

class al1Lib(FixedStar): # ,al-1Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",al-1Lib", context=context)

class ZubenElgenubi(FixedStar): # ,al-2Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",al-2Lib", context=context)

class ZubenEschamali(FixedStar): # ,beLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beLib", context=context)

class ZubenElakrab(FixedStar): # ,gaLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaLib", context=context)

class ZubenElakribi(FixedStar): # ,deLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deLib", context=context)

class ze1Lib(FixedStar): # ,ze-1Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ze-1Lib", context=context)

class io1Lib(FixedStar): # ,io-1Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",io-1Lib", context=context)

class kaLib(FixedStar): # ,kaLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaLib", context=context)

class laLib(FixedStar): # ,laLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laLib", context=context)

class ZubenHakrabi(FixedStar): # ,nuLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuLib", context=context)

class xi2Lib(FixedStar): # ,xi-2Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xi-2Lib", context=context)

class Brachium(FixedStar): # ,siLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siLib", context=context)

class taLib(FixedStar): # ,taLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taLib", context=context)

class upLib(FixedStar): # ,upLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upLib", context=context)

class beLMi(FixedStar): # ,beLMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beLMi", context=context)

class Praecipua(FixedStar): # ,LMi46

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",LMi46", context=context)

class LMi21(FixedStar): # ,LMi21

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",LMi21", context=context)

class Men(FixedStar): # ,alLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alLup", context=context)

class Kekouan(FixedStar): # ,beLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beLup", context=context)

class Thusia(FixedStar): # ,gaLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaLup", context=context)

class Hilasmus(FixedStar): # ,deLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deLup", context=context)

class epLup(FixedStar): # ,epLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epLup", context=context)

class etLup(FixedStar): # ,etLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etLup", context=context)

class zeLup(FixedStar): # ,zeLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeLup", context=context)

class thLup(FixedStar): # ,thLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thLup", context=context)

class ka1Lup(FixedStar): # ,ka-1Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ka-1Lup", context=context)

class ka2Lup(FixedStar): # ,ka-2Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ka-2Lup", context=context)

class ph1Lup(FixedStar): # ,ph-1Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ph-1Lup", context=context)

class ph2Lup(FixedStar): # ,ph-2Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ph-2Lup", context=context)

class ta1Lup(FixedStar): # ,ta-1Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-1Lup", context=context)

class chLup(FixedStar): # ,chLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chLup", context=context)

class AlFahd(FixedStar): # ,alLyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alLyn", context=context)

class Mabsuthat(FixedStar): # ,Lyn31

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lyn31", context=context)

class Mabsuthat(FixedStar): # ,kaLyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaLyn", context=context)

class Maculata(FixedStar): # ,Lyn38

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lyn38", context=context)

class Lyn21(FixedStar): # ,Lyn21

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lyn21", context=context)

class Lyn15(FixedStar): # ,Lyn15

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lyn15", context=context)

class Lyn2(FixedStar): # ,Lyn2

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Lyn2", context=context)

class Abhijit(FixedStar): # ,alLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alLyr", context=context)

class Sheliak(FixedStar): # ,beLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beLyr", context=context)

class Sulafat(FixedStar): # ,gaLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaLyr", context=context)

class Aladfar(FixedStar): # ,etLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etLyr", context=context)

class thLyr(FixedStar): # ,thLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thLyr", context=context)

class ioLyr(FixedStar): # ,ioLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioLyr", context=context)

class kaLyr(FixedStar): # ,kaLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaLyr", context=context)

class AlAthfar(FixedStar): # ,muLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muLyr", context=context)

class ze2Lyr(FixedStar): # ,ze-2Lyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ze-2Lyr", context=context)

class de2Lyr(FixedStar): # ,de-2Lyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",de-2Lyr", context=context)

class ep2Lyr(FixedStar): # ,ep-2Lyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ep-2Lyr", context=context)

class alMen(FixedStar): # ,alMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alMen", context=context)

class beMen(FixedStar): # ,beMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beMen", context=context)

class gaMen(FixedStar): # ,gaMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaMen", context=context)

class deMen(FixedStar): # ,deMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deMen", context=context)

class etMen(FixedStar): # ,etMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etMen", context=context)

class zeMen(FixedStar): # ,zeMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeMen", context=context)

class muMen(FixedStar): # ,muMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muMen", context=context)

class xiMen(FixedStar): # ,xiMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiMen", context=context)

class alMic(FixedStar): # ,alMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alMic", context=context)

class gaMic(FixedStar): # ,gaMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaMic", context=context)

class epMic(FixedStar): # ,epMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epMic", context=context)

class zeMic(FixedStar): # ,zeMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeMic", context=context)

class th1Mic(FixedStar): # ,th-1Mic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",th-1Mic", context=context)

class ioMic(FixedStar): # ,ioMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioMic", context=context)

class alMon(FixedStar): # ,alMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alMon", context=context)

class beMon(FixedStar): # ,beMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beMon", context=context)

class gaMon(FixedStar): # ,gaMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaMon", context=context)

class deMon(FixedStar): # ,deMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deMon", context=context)

class epMon(FixedStar): # ,epMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epMon", context=context)

class zeMon(FixedStar): # ,zeMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeMon", context=context)

class Mon18(FixedStar): # ,Mon18

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Mon18", context=context)

class Mon13(FixedStar): # ,Mon13

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Mon13", context=context)

class alMus(FixedStar): # ,alMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alMus", context=context)

class beMus(FixedStar): # ,beMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beMus", context=context)

class gaMus(FixedStar): # ,gaMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaMus", context=context)

class deMus(FixedStar): # ,deMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deMus", context=context)

class epMus(FixedStar): # ,epMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epMus", context=context)

class etMus(FixedStar): # ,etMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etMus", context=context)

class laMus(FixedStar): # ,laMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laMus", context=context)

class muMus(FixedStar): # ,muMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muMus", context=context)

class ga2Nor(FixedStar): # ,ga-2Nor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ga-2Nor", context=context)

class deNor(FixedStar): # ,deNor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deNor", context=context)

class epNor(FixedStar): # ,epNor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epNor", context=context)

class etNor(FixedStar): # ,etNor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etNor", context=context)

class kaNor(FixedStar): # ,kaNor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaNor", context=context)

class alOct(FixedStar): # ,alOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alOct", context=context)

class beOct(FixedStar): # ,beOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beOct", context=context)

class ga1Oct(FixedStar): # ,ga-1Oct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ga-1Oct", context=context)

class deOct(FixedStar): # ,deOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deOct", context=context)

class etOct(FixedStar): # ,etOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etOct", context=context)

class epOct(FixedStar): # ,epOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epOct", context=context)

class thOct(FixedStar): # ,thOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thOct", context=context)

class zeOct(FixedStar): # ,zeOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeOct", context=context)

class ioOct(FixedStar): # ,ioOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioOct", context=context)

class kaOct(FixedStar): # ,kaOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaOct", context=context)

class nuOct(FixedStar): # ,nuOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuOct", context=context)

class rhOct(FixedStar): # ,rhOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhOct", context=context)

class PolarisAustralis(FixedStar): # ,siOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siOct", context=context)

class taOct(FixedStar): # ,taOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taOct", context=context)

class upOct(FixedStar): # ,upOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upOct", context=context)

class chOct(FixedStar): # ,chOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chOct", context=context)

class Rasalhague(FixedStar): # ,alOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alOph", context=context)

class KelbAlrai(FixedStar): # ,beOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beOph", context=context)

class AlDurajah(FixedStar): # ,gaOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaOph", context=context)

class YedPrior(FixedStar): # ,deOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deOph", context=context)

class YedPosterior(FixedStar): # ,epOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epOph", context=context)

class Han(FixedStar): # ,zeOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeOph", context=context)

class Sabik(FixedStar): # ,etOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etOph", context=context)

class Imad(FixedStar): # ,thOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thOph", context=context)

class ioOph(FixedStar): # ,ioOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioOph", context=context)

class Helkath(FixedStar): # ,kaOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaOph", context=context)

class Marfik(FixedStar): # ,laOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laOph", context=context)

class Sinistra(FixedStar): # ,nuOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuOph", context=context)

class xiOph(FixedStar): # ,xiOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiOph", context=context)

class siOph(FixedStar): # ,siOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siOph", context=context)

class Barnardsstar(FixedStar): # ,V2500 Oph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",V2500 Oph", context=context)

class Oph44(FixedStar): # ,Oph44

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Oph44", context=context)

class Oph45(FixedStar): # ,Oph45

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Oph45", context=context)

class Ardra(FixedStar): # ,alOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alOri", context=context)

class Durga(FixedStar): # ,gaOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaOri", context=context)

class Kumara(FixedStar): # ,deOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deOri", context=context)

class Ganesha(FixedStar): # ,epOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epOri", context=context)

class Iyappa(FixedStar): # ,zeOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeOri", context=context)

class Ensis(FixedStar): # ,etOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etOri", context=context)

class Trapezium(FixedStar): # ,th-1Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",th-1Ori", context=context)

class NairalSaif(FixedStar): # ,ioOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioOri", context=context)

class Saiph(FixedStar): # ,kaOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaOri", context=context)

class Mrigashirsha(FixedStar): # ,laOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laOri", context=context)

class muOri(FixedStar): # ,muOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muOri", context=context)

class nuOri(FixedStar): # ,nuOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuOri", context=context)

class xiOri(FixedStar): # ,xiOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiOri", context=context)

class omi1Ori(FixedStar): # ,omi-1Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omi-1Ori", context=context)

class pi1Ori(FixedStar): # ,pi-1Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-1Ori", context=context)

class pi2Ori(FixedStar): # ,pi-2Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-2Ori", context=context)

class Tabit(FixedStar): # ,pi-3Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-3Ori", context=context)

class Tabit(FixedStar): # ,pi-4Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-4Ori", context=context)

class pi5Ori(FixedStar): # ,pi-5Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-5Ori", context=context)

class pi6Ori(FixedStar): # ,pi-6Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-6Ori", context=context)

class taOri(FixedStar): # ,taOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taOri", context=context)

class Thabit(FixedStar): # ,upOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upOri", context=context)

class ph1Ori(FixedStar): # ,ph-1Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ph-1Ori", context=context)

class ch2Ori(FixedStar): # ,ch-2Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ch-2Ori", context=context)

class Ori71(FixedStar): # ,Ori71

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Ori71", context=context)

class Messier42(FixedStar): # ,M42

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M42", context=context)

class Peacock(FixedStar): # ,alPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alPav", context=context)

class bePav(FixedStar): # ,bePav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bePav", context=context)

class gaPav(FixedStar): # ,gaPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaPav", context=context)

class dePav(FixedStar): # ,dePav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dePav", context=context)

class epPav(FixedStar): # ,epPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epPav", context=context)

class zePav(FixedStar): # ,zePav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zePav", context=context)

class etPav(FixedStar): # ,etPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etPav", context=context)

class laPav(FixedStar): # ,laPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laPav", context=context)

class xiPav(FixedStar): # ,xiPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiPav", context=context)

class omiPav(FixedStar): # ,omiPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiPav", context=context)

class Ankaa(FixedStar): # ,alPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alPhe", context=context)

class bePhe(FixedStar): # ,bePhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bePhe", context=context)

class gaPhe(FixedStar): # ,gaPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaPhe", context=context)

class dePhe(FixedStar): # ,dePhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dePhe", context=context)

class epPhe(FixedStar): # ,epPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epPhe", context=context)

class etPhe(FixedStar): # ,etPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etPhe", context=context)

class Wurren(FixedStar): # ,zePhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zePhe", context=context)

class thPhe(FixedStar): # ,thPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thPhe", context=context)

class ioPhe(FixedStar): # ,ioPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioPhe", context=context)

class la1Phe(FixedStar): # ,la-1Phe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",la-1Phe", context=context)

class muPhe(FixedStar): # ,muPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muPhe", context=context)

class piPhe(FixedStar): # ,piPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piPhe", context=context)

class upPhe(FixedStar): # ,upPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upPhe", context=context)

class phPhe(FixedStar): # ,phPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phPhe", context=context)

class psPhe(FixedStar): # ,psPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psPhe", context=context)

class omePhe(FixedStar): # ,omePhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omePhe", context=context)

class Purvabhadra(FixedStar): # ,alPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alPeg", context=context)

class Scheat(FixedStar): # ,bePeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bePeg", context=context)

class Uttarabhadra(FixedStar): # ,gaPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaPeg", context=context)

class Enif(FixedStar): # ,epPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epPeg", context=context)

class Homam(FixedStar): # ,zePeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zePeg", context=context)

class Matar(FixedStar): # ,etPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etPeg", context=context)

class Baham(FixedStar): # ,thPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thPeg", context=context)

class ioPeg(FixedStar): # ,ioPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioPeg", context=context)

class Jih(FixedStar): # ,kaPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaPeg", context=context)

class Sadalbari(FixedStar): # ,laPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laPeg", context=context)

class muPeg(FixedStar): # ,muPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muPeg", context=context)

class xiPeg(FixedStar): # ,xiPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiPeg", context=context)

class piPeg(FixedStar): # ,piPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piPeg", context=context)

class pi1Peg(FixedStar): # ,pi-1Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-1Peg", context=context)

class pi2Peg(FixedStar): # ,pi-2Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi-2Peg", context=context)

class Salm(FixedStar): # ,taPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taPeg", context=context)

class Alkarab(FixedStar): # ,upPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upPeg", context=context)

class phPeg(FixedStar): # ,phPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phPeg", context=context)

class chPeg(FixedStar): # ,chPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chPeg", context=context)

class psPeg(FixedStar): # ,psPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psPeg", context=context)

class Peg1(FixedStar): # ,Peg1

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Peg1", context=context)

class Peg9(FixedStar): # ,Peg9

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Peg9", context=context)

class Helvetios(FixedStar): # ,Peg51

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Peg51", context=context)

class Mirphak(FixedStar): # ,alPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alPer", context=context)

class gaPer(FixedStar): # ,gaPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaPer", context=context)

class dePer(FixedStar): # ,dePer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dePer", context=context)

class epPer(FixedStar): # ,epPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epPer", context=context)

class zePer(FixedStar): # ,zePer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zePer", context=context)

class Miram(FixedStar): # ,etPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etPer", context=context)

class thPer(FixedStar): # ,thPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thPer", context=context)

class ioPer(FixedStar): # ,ioPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioPer", context=context)

class Misam(FixedStar): # ,kaPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaPer", context=context)

class laPer(FixedStar): # ,laPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laPer", context=context)

class muPer(FixedStar): # ,muPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muPer", context=context)

class nuPer(FixedStar): # ,nuPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuPer", context=context)

class Menkib(FixedStar): # ,xiPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiPer", context=context)

class Atiks(FixedStar): # ,omiPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiPer", context=context)

class GorgonaSecunda(FixedStar): # ,piPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piPer", context=context)

class GorgonaTertia(FixedStar): # ,rhPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhPer", context=context)

class siPer(FixedStar): # ,siPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siPer", context=context)

class taPer(FixedStar): # ,taPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taPer", context=context)

class phPer(FixedStar): # ,phPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phPer", context=context)

class GorgonaQuatra(FixedStar): # ,omePer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omePer", context=context)

class Per16(FixedStar): # ,Per16

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Per16", context=context)

class alPic(FixedStar): # ,alPic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alPic", context=context)

class bePic(FixedStar): # ,bePic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bePic", context=context)

class gaPic(FixedStar): # ,gaPic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaPic", context=context)

class dePic(FixedStar): # ,dePic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dePic", context=context)

class zePic(FixedStar): # ,zePic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zePic", context=context)

class et2Pic(FixedStar): # ,et-2Pic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",et-2Pic", context=context)

class Fomalhaut(FixedStar): # ,alPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alPsA", context=context)

class TienKang(FixedStar): # ,bePsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bePsA", context=context)

class gaPsA(FixedStar): # ,gaPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaPsA", context=context)

class Aboras(FixedStar): # ,dePsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dePsA", context=context)

class epPsA(FixedStar): # ,epPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epPsA", context=context)

class thPsA(FixedStar): # ,thPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thPsA", context=context)

class ioPsA(FixedStar): # ,ioPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioPsA", context=context)

class laPsA(FixedStar): # ,laPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laPsA", context=context)

class muPsA(FixedStar): # ,muPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muPsA", context=context)

class piPsA(FixedStar): # ,piPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piPsA", context=context)

class AlRescha(FixedStar): # ,alPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alPsc", context=context)
        self._name="AlRescha"

class Samakah(FixedStar): # ,bePsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bePsc", context=context)

class Simmah(FixedStar): # ,gaPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaPsc", context=context)

class Linteum(FixedStar): # ,dePsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dePsc", context=context)

class Kaht(FixedStar): # ,epPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epPsc", context=context)

class Revati(FixedStar): # ,zePscA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zePscA", context=context)

class Revati(FixedStar): # ,zePsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zePsc", context=context)

class AlPherg(FixedStar): # ,etPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etPsc", context=context)

class thPsc(FixedStar): # ,thPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thPsc", context=context)

class ioPsc(FixedStar): # ,ioPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioPsc", context=context)

class kaPsc(FixedStar): # ,kaPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaPsc", context=context)

class laPsc(FixedStar): # ,laPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laPsc", context=context)

class nuPsc(FixedStar): # ,nuPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuPsc", context=context)

class xiPsc(FixedStar): # ,xiPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiPsc", context=context)

class Torcular(FixedStar): # ,omiPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiPsc", context=context)

class piPsc(FixedStar): # ,piPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piPsc", context=context)

class Anunitum(FixedStar): # ,taPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taPsc", context=context)

class upPsc(FixedStar): # ,upPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upPsc", context=context)

class phPsc(FixedStar): # ,phPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phPsc", context=context)

class chPsc(FixedStar): # ,chPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chPsc", context=context)

class Vernalis(FixedStar): # ,omePsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omePsc", context=context)

class Psc7(FixedStar): # ,Psc7

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Psc7", context=context)

class Psc19(FixedStar): # ,Psc19

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Psc19", context=context)

class SuhailHadar(FixedStar): # ,zePup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zePup", context=context)

class Kaimana(FixedStar): # ,nuPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuPup", context=context)

class Azmidiske(FixedStar): # ,xiPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiPup", context=context)

class Ahadi(FixedStar): # ,piPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piPup", context=context)

class Tureis(FixedStar): # ,rhPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhPup", context=context)

class siPup(FixedStar): # ,siPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siPup", context=context)

class Anazitisi(FixedStar): # ,taPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taPup", context=context)

class pPup(FixedStar): # ,pPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pPup", context=context)

class P_Pup(FixedStar): # ,P_Pup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",P_Pup", context=context)

class k01Pup(FixedStar): # ,k01Pup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",k01Pup", context=context)

class J_Pup(FixedStar): # ,J_Pup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",J_Pup", context=context)

class alPyx(FixedStar): # ,alPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alPyx", context=context)

class bePyx(FixedStar): # ,bePyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bePyx", context=context)

class gaPyx(FixedStar): # ,gaPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaPyx", context=context)

class epPyx(FixedStar): # ,epPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epPyx", context=context)

class thPyx(FixedStar): # ,thPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thPyx", context=context)

class alRet(FixedStar): # ,alRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alRet", context=context)

class beRet(FixedStar): # ,beRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beRet", context=context)

class gaRet(FixedStar): # ,gaRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaRet", context=context)

class deRet(FixedStar): # ,deRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deRet", context=context)

class epRet(FixedStar): # ,epRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epRet", context=context)

class ze1Ret(FixedStar): # ,ze-1Ret

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ze-1Ret", context=context)

class etRet(FixedStar): # ,etRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etRet", context=context)

class ioRet(FixedStar): # ,ioRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioRet", context=context)

class kaRet(FixedStar): # ,kaRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaRet", context=context)

class piScl(FixedStar): # ,piScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piScl", context=context)

class alScl(FixedStar): # ,alScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alScl", context=context)

class beScl(FixedStar): # ,beScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beScl", context=context)

class gaScl(FixedStar): # ,gaScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaScl", context=context)

class deScl(FixedStar): # ,deScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deScl", context=context)

class epScl(FixedStar): # ,epScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epScl", context=context)

class thScl(FixedStar): # ,thScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thScl", context=context)

class ka2Scl(FixedStar): # ,ka-2Scl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ka-2Scl", context=context)

class la2Scl(FixedStar): # ,la-2Scl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",la-2Scl", context=context)

class muScl(FixedStar): # ,muScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muScl", context=context)

class siScl(FixedStar): # ,siScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siScl", context=context)

class Acrab(FixedStar): # ,be-1Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",be-1Sco", context=context)

class be2Sco(FixedStar): # ,be-2Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",be-2Sco", context=context)

class Anuradha(FixedStar): # ,deSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deSco", context=context)

class Larawag(FixedStar): # ,epSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epSco", context=context)

class ze2Sco(FixedStar): # ,ze-2Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ze-2Sco", context=context)

class etSco(FixedStar): # ,etSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etSco", context=context)

class Sargas(FixedStar): # ,thSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thSco", context=context)

class io1Sco(FixedStar): # ,io-1Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",io-1Sco", context=context)

class Girtab(FixedStar): # ,kaSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaSco", context=context)

class Mula(FixedStar): # ,laSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laSco", context=context)

class Xamidimura(FixedStar): # ,mu-1Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu-1Sco", context=context)

class Jabbah(FixedStar): # ,nuSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuSco", context=context)

class Grafias(FixedStar): # ,xiSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiSco", context=context)

class Fang(FixedStar): # ,piSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piSco", context=context)

class Iklil(FixedStar): # ,rhSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhSco", context=context)

class Alniyat(FixedStar): # ,siSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siSco", context=context)

class taSco(FixedStar): # ,taSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taSco", context=context)

class Lesath(FixedStar): # ,upSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upSco", context=context)

class JabhatalAkrab(FixedStar): # ,ome-1Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome-1Sco", context=context)

class JabhatalAkrab(FixedStar): # ,ome-2Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome-2Sco", context=context)

class Fuyue(FixedStar): # ,HR6630

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HR6630", context=context)

class Pipirima(FixedStar): # ,mu-2Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu-2Sco", context=context)

class alSct(FixedStar): # ,alSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alSct", context=context)

class beSct(FixedStar): # ,beSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beSct", context=context)

class gaSct(FixedStar): # ,gaSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaSct", context=context)

class deSct(FixedStar): # ,deSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deSct", context=context)

class epSct(FixedStar): # ,epSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epSct", context=context)

class zeSct(FixedStar): # ,zeSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeSct", context=context)

class CorSerpentis(FixedStar): # ,alSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alSer", context=context)

class Zhou(FixedStar): # ,beSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beSer", context=context)

class Ainalhai(FixedStar): # ,gaSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaSer", context=context)

class Chin(FixedStar): # ,deSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deSer", context=context)

class NullaPambu(FixedStar): # ,epSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epSer", context=context)

class Tang(FixedStar): # ,etSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etSer", context=context)

class Alya(FixedStar): # ,th-1Ser

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",th-1Ser", context=context)

class kaSer(FixedStar): # ,kaSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaSer", context=context)

class Leiolepidotus(FixedStar): # ,muSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muSer", context=context)

class nuSer(FixedStar): # ,nuSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuSer", context=context)

class Nehushtan(FixedStar): # ,xiSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiSer", context=context)

class omiSer(FixedStar): # ,omiSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiSer", context=context)

class siSer(FixedStar): # ,siSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siSer", context=context)

class ta1Ser(FixedStar): # ,ta-1Ser

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ta-1Ser", context=context)

class alSex(FixedStar): # ,alSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alSex", context=context)

class beSex(FixedStar): # ,beSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beSex", context=context)

class gaSex(FixedStar): # ,gaSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaSex", context=context)

class deSex(FixedStar): # ,deSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deSex", context=context)

class epSex(FixedStar): # ,epSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epSex", context=context)

class Sham(FixedStar): # ,alSge

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alSge", context=context)

class beSge(FixedStar): # ,beSge

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beSge", context=context)

class gaSge(FixedStar): # ,gaSge

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaSge", context=context)

class deSge(FixedStar): # ,deSge

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deSge", context=context)

class Rukbat(FixedStar): # ,alSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alSgr", context=context)

class ArkabPrior(FixedStar): # ,be-1Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",be-1Sgr", context=context)

class ArkabPosterior(FixedStar): # ,be-2Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",be-2Sgr", context=context)

class Alnasl(FixedStar): # ,gaSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaSgr", context=context)

class Nash(FixedStar): # ,ga-2Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ga-2Sgr", context=context)

class Purvashadha(FixedStar): # ,deSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deSgr", context=context)

class KausAustralis(FixedStar): # ,epSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epSgr", context=context)

class Ascella(FixedStar): # ,zeSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeSgr", context=context)

class IraFuroris(FixedStar): # ,etSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etSgr", context=context)

class th1Sgr(FixedStar): # ,th-1Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",th-1Sgr", context=context)

class th2Sgr(FixedStar): # ,th-2Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",th-2Sgr", context=context)

class ioSgr(FixedStar): # ,ioSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioSgr", context=context)

class ka1Sgr(FixedStar): # ,ka-1Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ka-1Sgr", context=context)

class KausBorealis(FixedStar): # ,laSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laSgr", context=context)

class Polis(FixedStar): # ,muSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muSgr", context=context)

class AinalRami(FixedStar): # ,nu-1Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu-1Sgr", context=context)

class xi2Sgr(FixedStar): # ,xi-2Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xi-2Sgr", context=context)

class Manubrium(FixedStar): # ,omiSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiSgr", context=context)

class Albaldah(FixedStar): # ,piSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piSgr", context=context)

class Uttarashadha(FixedStar): # ,siSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siSgr", context=context)

class Hecatebolus(FixedStar): # ,taSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taSgr", context=context)

class Nanto(FixedStar): # ,phSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phSgr", context=context)

class upSgr(FixedStar): # ,upSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upSgr", context=context)

class Terebellium(FixedStar): # ,omeSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeSgr", context=context)

class Sgr52(FixedStar): # ,Sgr52

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Sgr52", context=context)

class Sgr59(FixedStar): # ,Sgr59

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Sgr59", context=context)

class Sgr62(FixedStar): # ,Sgr62

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Sgr62", context=context)

class Alnath(FixedStar): # ,beTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beTau", context=context)

class HyadumI(FixedStar): # ,gaTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaTau", context=context)

class SecundaHyadum(FixedStar): # ,deTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deTau", context=context)

class HyadumII(FixedStar): # ,de-1Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",de-1Tau", context=context)

class Tianguan(FixedStar): # ,zeTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeTau", context=context)

class Krttika(FixedStar): # ,etTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etTau", context=context)

class Phaeo(FixedStar): # ,th-1Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",th-1Tau", context=context)

class Chamukuy(FixedStar): # ,th-2Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",th-2Tau", context=context)

class ioTau(FixedStar): # ,ioTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioTau", context=context)

class Althaur(FixedStar): # ,laTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laTau", context=context)

class Kattupothu(FixedStar): # ,muTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muTau", context=context)

class Furibundus(FixedStar): # ,nuTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuTau", context=context)

class Ushakaron(FixedStar): # ,xiTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiTau", context=context)

class OmicronTauri(FixedStar): # ,omiTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiTau", context=context)

class taTau(FixedStar): # ,taTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taTau", context=context)

class rhTau(FixedStar): # ,rhTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhTau", context=context)

class ome1Tau(FixedStar): # ,ome-1Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome-1Tau", context=context)

class Celeano(FixedStar): # ,Tau16

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau16", context=context)

class Electra(FixedStar): # ,Tau17

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau17", context=context)

class Taygeta(FixedStar): # ,Tau19

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau19", context=context)

class Maia(FixedStar): # ,Tau20

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau20", context=context)

class SteropeI(FixedStar): # ,Tau21

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau21", context=context)

class SteropeII(FixedStar): # ,Tau22

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau22", context=context)

class Merope(FixedStar): # ,Tau23

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau23", context=context)

class Atlas(FixedStar): # ,Tau27

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau27", context=context)

class Pleione(FixedStar): # ,Tau28

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Tau28", context=context)

class alTel(FixedStar): # ,alTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alTel", context=context)

class epTel(FixedStar): # ,epTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epTel", context=context)

class zeTel(FixedStar): # ,zeTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeTel", context=context)

class ioTel(FixedStar): # ,ioTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioTel", context=context)

class laTel(FixedStar): # ,laTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laTel", context=context)

class nuTel(FixedStar): # ,nuTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuTel", context=context)

class xiTel(FixedStar): # ,xiTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiTel", context=context)

class Atria(FixedStar): # ,alTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alTrA", context=context)

class beTrA(FixedStar): # ,beTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beTrA", context=context)

class gaTrA(FixedStar): # ,gaTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaTrA", context=context)

class deTrA(FixedStar): # ,deTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deTrA", context=context)

class epTrA(FixedStar): # ,epTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epTrA", context=context)

class zeTrA(FixedStar): # ,zeTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeTrA", context=context)

class Mothallah(FixedStar): # ,alTri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alTri", context=context)

class beTri(FixedStar): # ,beTri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beTri", context=context)

class gaTri(FixedStar): # ,gaTri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaTri", context=context)

class alTuc(FixedStar): # ,alTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alTuc", context=context)

class be2Tuc(FixedStar): # ,be-2Tuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",be-2Tuc", context=context)

class gaTuc(FixedStar): # ,gaTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaTuc", context=context)

class epTuc(FixedStar): # ,epTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epTuc", context=context)

class zeTuc(FixedStar): # ,zeTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeTuc", context=context)

class ioTuc(FixedStar): # ,ioTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioTuc", context=context)

class la2Tuc(FixedStar): # ,la-2Tuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",la-2Tuc", context=context)

class Kratu(FixedStar): # ,alUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alUMa", context=context)

class Pulaha(FixedStar): # ,beUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beUMa", context=context)

class Pulastya(FixedStar): # ,gaUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaUMa", context=context)

class Atri(FixedStar): # ,deUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deUMa", context=context)

class Angiras(FixedStar): # ,epUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epUMa", context=context)

class Vasishtha(FixedStar): # ,zeUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeUMa", context=context)

class Marichi(FixedStar): # ,etUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etUMa", context=context)

class AlHaud(FixedStar): # ,thUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thUMa", context=context)

class TalithaBorealis(FixedStar): # ,ioUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioUMa", context=context)

class Alkaphrah(FixedStar): # ,kaUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaUMa", context=context)

class TaniaBorealis(FixedStar): # ,laUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laUMa", context=context)

class TaniaAustralis(FixedStar): # ,muUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muUMa", context=context)

class AlulaBorealis(FixedStar): # ,nuUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuUMa", context=context)

class AlulaAustralis(FixedStar): # ,xiUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",xiUMa", context=context)

class Muscida(FixedStar): # ,omiUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiUMa", context=context)

class rhUMa(FixedStar): # ,rhUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhUMa", context=context)

class upUMa(FixedStar): # ,upUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upUMa", context=context)

class phUMa(FixedStar): # ,phUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phUMa", context=context)

class Taiyangshou(FixedStar): # ,chUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chUMa", context=context)

class psUMa(FixedStar): # ,psUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psUMa", context=context)

class UMa23(FixedStar): # ,UMa23

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",UMa23", context=context)

class UMa26(FixedStar): # ,UMa26

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",UMa26", context=context)

class Chalawan(FixedStar): # ,UMa47

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",UMa47", context=context)

class Saidak(FixedStar): # ,UMa80

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",UMa80", context=context)

class Alc0(FixedStar): # ,Uma80

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Uma80", context=context)

class Intercrus(FixedStar): # ,HR3743

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HR3743", context=context)

class Kochab(FixedStar): # ,beUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beUMi", context=context)

class Pherkad(FixedStar): # ,gaUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaUMi", context=context)

class Yildun(FixedStar): # ,deUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deUMi", context=context)

class Urodelus(FixedStar): # ,epUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epUMi", context=context)

class Pharkadain(FixedStar): # ,zeUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeUMi", context=context)

class AnwaralFarkadain(FixedStar): # ,etUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etUMi", context=context)

class laUMi(FixedStar): # ,laUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laUMi", context=context)

class PherkadMinor(FixedStar): # ,UMi11

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",UMi11", context=context)

class Regor(FixedStar): # ,ga-2Vel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ga-2Vel", context=context)

class KooShe(FixedStar): # ,deVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deVel", context=context)

class Markeb(FixedStar): # ,kaVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaVel", context=context)

class Suhail(FixedStar): # ,laVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laVel", context=context)

class Alherem(FixedStar): # ,muVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muVel", context=context)

class Xestus(FixedStar): # ,omiVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiVel", context=context)

class TseenKe(FixedStar): # ,phVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phVel", context=context)

class psVel(FixedStar): # ,psVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psVel", context=context)

class dVel(FixedStar): # ,dVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dVel", context=context)

class eVel(FixedStar): # ,eVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eVel", context=context)

class pVel(FixedStar): # ,pVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pVel", context=context)

class qVel(FixedStar): # ,qVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",qVel", context=context)

class tVel(FixedStar): # ,tVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tVel", context=context)

class Alaraph(FixedStar): # ,beVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beVir", context=context)

class Porrima(FixedStar): # ,gaVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gaVir", context=context)

class Mineluva(FixedStar): # ,deVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deVir", context=context)

class Vindemiatrix(FixedStar): # ,epVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epVir", context=context)

class Heze(FixedStar): # ,zeVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeVir", context=context)

class Zaniah(FixedStar): # ,etVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etVir", context=context)

class thVir(FixedStar): # ,thVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",thVir", context=context)

class Syrma(FixedStar): # ,ioVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioVir", context=context)

class Kang(FixedStar): # ,kaVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kaVir", context=context)

class Khambalia(FixedStar): # ,laVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",laVir", context=context)

class RilAlauva(FixedStar): # ,muVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",muVir", context=context)

class nuVir(FixedStar): # ,nuVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuVir", context=context)

class omiVir(FixedStar): # ,omiVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiVir", context=context)

class piVir(FixedStar): # ,piVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",piVir", context=context)

class rhVir(FixedStar): # ,rhVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhVir", context=context)

class siVir(FixedStar): # ,siVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",siVir", context=context)

class taVir(FixedStar): # ,taVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",taVir", context=context)

class phVir(FixedStar): # ,phVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phVir", context=context)

class chVir(FixedStar): # ,chVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chVir", context=context)

class psVir(FixedStar): # ,psVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psVir", context=context)

class Vir109(FixedStar): # ,Vir109

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Vir109", context=context)

class Lich(FixedStar): # ,PSRB1257+12

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",PSRB1257+12", context=context)

class Messier49(FixedStar): # ,M49

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M49", context=context)

class alVol(FixedStar): # ,alVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alVol", context=context)

class beVol(FixedStar): # ,beVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",beVol", context=context)

class ga2Vol(FixedStar): # ,ga-2Vol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ga-2Vol", context=context)

class deVol(FixedStar): # ,deVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",deVol", context=context)

class epVol(FixedStar): # ,epVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epVol", context=context)

class epVolA(FixedStar): # ,epVolA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epVolA", context=context)

class zeVol(FixedStar): # ,zeVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zeVol", context=context)

class ioVol(FixedStar): # ,ioVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ioVol", context=context)

class Anser(FixedStar): # ,alVul

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alVul", context=context)

class Vul2(FixedStar): # ,Vul2

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Vul2", context=context)

class Vul12(FixedStar): # ,Vul12

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Vul12", context=context)

class GCLiu(FixedStar): # ,GCLiu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GCLiu", context=context)

class GalPole(FixedStar): # ,GPol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GPol", context=context)

class GalPoleIAU1958(FixedStar): # ,GP1958

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GP1958", context=context)

class GalPlanePole(FixedStar): # ,GPPlan

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GPPlan", context=context)

class GalEqu(FixedStar): # ,GEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GEqu", context=context)

class InfraredDragon(FixedStar): # ,IDrag

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",IDrag", context=context)

class AA11_page_B73(FixedStar): # ,AA11     

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",AA11     ", context=context)

class GCRS00(FixedStar): # ,GCRS00

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GCRS00", context=context)

class Zero2000(FixedStar): # ,ZE200

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ZE200", context=context)

class ZerL2000(FixedStar): # ,ZL200

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ZL200", context=context)

class SunPole(FixedStar): # ,SunPole

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SunPole", context=context)

class Test(FixedStar): # ,Test

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Test", context=context)

class NGC4194(FixedStar): # ,NGC4194

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",NGC4194", context=context)

class Gliese710(FixedStar): # ,HD168442

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HD168442", context=context)

class Librae48(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",Lib48", context=context)

natural_stars = {
    ",SgrA*": GalacticCenter,
    ",GPol": GalPole,
    ",alCMa": Lubdhaka,
    ",taPeg": Salm,
    ",ioCet": Shemali,
    ",gaPeg": Uttarabhadra,
    ",alAnd": Sirrah,
    ",muCep": TheGarnetStar,
    ",alCnc": Ashlesha,
    ",beLeo": Uttaraphalguni,
    ",muVir": RilAlauva,
    ",al-2Lib": ZubenElgenubi,
    ",deSco": Anuradha,
    ",ga-2Sgr": Nash,
    ",alTau": Aldebaran,
    ",bePer": Algol,
    ",alSco": Jyeshtha,
    ",alLeo": Magha,
    ",alVir": Citra,
    ",Trappist-1": Trappist1,
    ",GA": GreatAttractor,
    ",VC": VirgoCluster,
    ",M31": AndromedaGalaxy,
    ",M44": PraesepeCluster,
    ",alUMi": Polaris,
    ",M87": Messier87,
    ",ACO3558": A3558,
    ",alCyg": Deneb,
    ",beOri": Rigel,
    ",omiCet": Mira,
    ",epTau": Ain,
    ",epCas": Segin,
    ",beAnd": Mirach,
    ",ga-1And": Almach,
    ",deAnd": deAnd,
    ",epAnd": epAnd,
    ",zeAnd": zeAnd,
    ",ioAnd": ioAnd,
    ",kaAnd": kaAnd,
    ",laAnd": laAnd,
    ",muAnd": muAnd,
    ",nuAnd": nuAnd,
    ",xiAnd": Adhil,
    ",omiAnd": omiAnd,
    ",piAnd": piAnd,
    ",rhAnd": rhAnd,
    ",siAnd": siAnd,
    ",upAnd": Titawin,
    ",psAnd": psAnd,
    ",omeAnd": omeAnd,
    ",And14": Veritate,
    ",And51": Nembus,
    ",alAnt": alAnt,
    ",epAnt": epAnt,
    ",thAnt": thAnt,
    ",ioAnt": ioAnt,
    ",alAps": alAps,
    ",beAps": beAps,
    ",gaAps": gaAps,
    ",de-1Aps": de1Aps,
    ",thAps": thAps,
    ",ioAps": ioAps,
    ",ka-1Aps": ka1Aps,
    ",alAql": Shravana,
    ",beAql": Alshain,
    ",gaAql": Tarazed,
    ",deAql": AlMizan,
    ",epAql": DenebelOkabBorealis,
    ",zeAql": Dheneb,
    ",etAql": Bazak,
    ",thAql": TseenFoo,
    ",ioAql": AlThalimaimPosterior,
    ",kaAql": kaAql,
    ",laAql": AlThalimaimAnterior,
    ",muAql": muAql,
    ",rhAql": rhAql,
    ",taAql": taAql,
    ",ome-1Aql": ome1Aql,
    ",xiAql": Libertas,
    ",Aql12": Bered,
    ",alAqr": Sadalmelik,
    ",beAqr": Sadalsuud,
    ",gaAqr": Sadachbia,
    ",deAqr": Skat,
    ",epAqr": Altager,
    ",ze-1Aqr": Sadaltager,
    ",etAqr": Deli,
    ",thAqr": Ancha,
    ",ioAqr": ioAqr,
    ",kaAqr": Situla,
    ",laAqr": Shatabhishak,
    ",muAqr": muAqr,
    ",nuAqr": Albulaan,
    ",piAqr": Seat,
    ",siAqr": siAqr,
    ",ta-2Aqr": ta2Aqr,
    ",phAqr": phAqr,
    ",xiAqr": Bunda,
    ",upAqr": upAqr,
    ",ps-1Aqr": ps1Aqr,
    ",ps-3Aqr": ps3Aqr,
    ",ome-2Aqr": ome2Aqr,
    ",Aqr3": Aqr3,
    ",Aqr88": Aqr88,
    ",Aqr98": Aqr98,
    ",alAra": Ara,
    ",beAra": beAra,
    ",gaAra": gaAra,
    ",deAra": deAra,
    ",ep-1Ara": ep1Ara,
    ",zeAra": zeAra,
    ",etAra": etAra,
    ",thAra": thAra,
    ",muAra": Cervantes,
    ",alAri": Hamal,
    ",beAri": Ashvini,
    ",gaAri": Mesarthim,
    ",deAri": Botein,
    ",zeAri": zeAri,
    ",thAri": thAri,
    ",nuAri": nuAri,
    ",siAri": siAri,
    ",ta-1Ari": ta1Ari,
    ",Ari39": LiliiBorea,
    ",Ari41": Bharani,
    ",alAur": Brahmahridaya,
    ",beAur": Menkalinan,
    ",deAur": Prijipati,
    ",epAur": AlAnz,
    ",zeAur": Saclateni,
    ",etAur": Haedus,
    ",thAur": Mahasim,
    ",ioAur": AlKhabdhilinan,
    ",kaAur": kaAur,
    ",laAur": laAur,
    ",muAur": muAur,
    ",nuAur": nuAur,
    ",xiAur": xiAur,
    ",omiAur": omiAur,
    ",chAur": chAur,
    ",ps-1Aur": ps1Aur,
    ",ps-5Aur": ps5Aur,
    ",ps-6Aur": ps6Aur,
    ",alBoo": Svati,
    ",beBoo": Nekkar,
    ",gaBoo": Haris,
    ",deBoo": Princeps,
    ",epBoo": Pulcherrima,
    ",zeBoo": zeBoo,
    ",etBoo": Muphrid,
    ",thBoo": AsellusPrimus,
    ",ioBoo": AsellusSecundus,
    ",ka-2Boo": AsellusTertius,
    ",laBoo": Xuange,
    ",mu-1Boo": Alkalurops,
    ",nu-1Boo": nu1Boo,
    ",rhBoo": AlHamalain,
    ",siBoo": HemeleinSecunda,
    ",taBoo": taBoo,
    ",phBoo": Ceginus,
    ",psBoo": psBoo,
    ",Boo38": Merga,
    ",alCae": alCae,
    ",beCae": beCae,
    ",deCae": deCae,
    ",alCam": alCam,
    ",beCam": beCam,
    ",gaCam": gaCam,
    ",Cam2": Cam2,
    ",Cam7": Cam7,
    ",HR4609": Tonatiuh,
    ",al-1Cap": GiediPrima,
    ",al-2Cap": GiediSecunda,
    ",beCap": Dabih,
    ",be-1Cap": Dabih,
    ",gaCap": Nashira,
    ",deCap": DenebAlgedi,
    ",epCap": Castra,
    ",zeCap": Marakk,
    ",etCap": Armus,
    ",thCap": Dorsum,
    ",ioCap": ioCap,
    ",laCap": laCap,
    ",muCap": muCap,
    ",nuCap": Alshat,
    ",piCap": Oculus,
    ",rhCap": Bos,
    ",psCap": Pazhan,
    ",upCap": upCap,
    ",omeCap": BatenAlgiedi,
    ",Cap24": Cap24,
    ",Cap36": Cap36,
    ",alCar": Agastya,
    ",beCar": Miaplacidus,
    ",epCar": Avior,
    ",etCar": Foramen,
    ",thCar": VathorzPosterior,
    ",ioCar": Aspidiske,
    ",chCar": Drys,
    ",omeCar": Simiram,
    ",upCar": VathorzPrior,
    ",qCar": qCar,
    ",alCas": Schedir,
    ",beCas": Caph,
    ",gaCas": Cih,
    ",deCas": Rucha,
    ",zeCas": Fulu,
    ",etCas": Achird,
    ",kaCas": kaCas,
    ",muCas": Marfak,
    ",omiCas": omiCas,
    ",rhCas": rhCas,
    ",psCas": psCas,
    ",up-2Cas": Castula,
    ",alCen": ProximaCentauri,
    ",beCen": Agena,
    ",gaCen": Muhlifain,
    ",deCen": deCen,
    ",epCen": Birdun,
    ",zeCen": zeCen,
    ",etCen": etCen,
    ",thCen": Menkent,
    ",ioCen": Alhakim,
    ",kaCen": KeKwan,
    ",laCen": Mati,
    ",muCen": muCen,
    ",nuCen": KabkentSecunda,
    ",xi-2Cen": xi2Cen,
    ",piCen": piCen,
    ",siCen": siCen,
    ",phCen": KabkentTertia,
    ",psCen": psCen,
    ",dCen": dCen,
    ",rhCen": rhCen,
    ",V645": ProximaCentauri,
    ",alCep": Alderamin,
    ",beCep": Alfirk,
    ",gaCep": Errai,
    ",deCep": Alredif,
    ",epCep": Phicareus,
    ",zeCep": Kurhah,
    ",etCep": Alagemin,
    ",thCep": Alkidr,
    ",ioCep": Alvahet,
    ",kaCep": kaCep,
    ",nuCep": nuCep,
    ",xiCep": Alkurhah,
    ",rhCep": AlKalbalRai,
    ",alCet": Menkar,
    ",beCet": Difda,
    ",gaCet": Kaffaljidhma,
    ",deCet": Phycochroma,
    ",zeCet": BatenKaitos,
    ",etCet": DenebAlgenubi,
    ",thCet": Altawk,
    ",laCet": Menkar,
    ",muCet": muCet,
    ",nuCet": nuCet,
    ",xi-1Cet": xi1Cet,
    ",xi-2Cet": xi2Cet,
    ",piCet": AlSadralKetus,
    ",rhCet": rhCet,
    ",siCet": siCet,
    ",taCet": taCet,
    ",upCet": AbyssusAqueus,
    ",ph-1Cet": AlNitham,
    ",ph-2Cet": ph2Cet,
    ",chCet": chCet,
    ",alCha": alCha,
    ",beCha": beCha,
    ",gaCha": gaCha,
    ",de-2Cha": de2Cha,
    ",etCha": etCha,
    ",thCha": thCha,
    ",piCha": piCha,
    ",alCir": alCir,
    ",beCir": beCir,
    ",beCMa": Murzims,
    ",gaCMa": Isis,
    ",deCMa": Wezen,
    ",epCMa": Adhara,
    ",zeCMa": Furud,
    ",etCMa": Aludra,
    ",kaCMa": kaCMa,
    ",xi-2CMa": xi2CMa,
    ",omi-2CMa": omi2CMa,
    ",siCMa": Unurgunite,
    ",thCMa": thCMa,
    ",alCMi": Procyon,
    ",beCMi": Gomeisa,
    ",zeCMi": zeCMi,
    ",beCnc": AlTarf,
    ",gaCnc": AsellusBorealis,
    ",deCnc": Pushya,
    ",epCnc": Meleph,
    ",zeCnc": Tegmine,
    ",etCnc": etCnc,
    ",ioCnc": Decapoda,
    ",kaCnc": kaCnc,
    ",xiCnc": xiCnc,
    ",si-3Cnc": si3Cnc,
    ",chCnc": chCnc,
    ",ome-1Cnc": ome1Cnc,
    ",Cnc55": Copernicus,
    ",alCol": Phact,
    ",beCol": Wazn,
    ",deCol": GhusnalZaitun,
    ",gaCol": gaCol,
    ",etCol": etCol,
    ",kaCol": AlKurud,
    ",laCol": Tsze,
    ",omiCol": omiCol,
    ",epCol": epCol,
    ",alCom": Diadem,
    ",beCom": Aldafirah,
    ",gaCom": Kissin,
    ",alCrB": Gemma,
    ",beCrB": Nusakan,
    ",epCrB": epCrB,
    ",thCrB": thCrB,
    ",kaC1GrB": kaC1GrB,
    ",tCrB": BlazeStar,
    ",taCrB": taCrB,
    ",gaCrB": gaCrB,
    ",deCrB": deCrB,
    ",ioCrB": ioCrB,
    ",alCrA": Meridiana,
    ",et-1CrA": et1CrA,
    ",thCrA": thCrA,
    ",epCrA": epCrA,
    ",gaCrA": gaCrA,
    ",beCrA": beCrA,
    ",deCrA": deCrA,
    ",zeCrA": zeCrA,
    ",alCrt": Alkes,
    ",beCrt": Alsharasif,
    ",gaCrt": gaCrt,
    ",deCrt": Labrum,
    ",epCrt": epCrt,
    ",etCrt": etCrt,
    ",thCrt": thCrt,
    ",zeCrt": zeCrt,
    ",beCru": Mimosa,
    ",gaCru": Gacrux,
    ",deCru": Decrux,
    ",epCru": Ginan,
    ",alCrv": Alchita,
    ",beCrv": Kraz,
    ",gaCrv": GienahCorvi,
    ",deCrv": Hasta,
    ",epCrv": Minkar,
    ",etCrv": AvisSatyra,
    ",al-2CVn": CorCaroli,
    ",beCVn": Chara,
    ",be-1Cyg": Albireo,
    ",gaCyg": Sadr,
    ",deCyg": AlFawaris,
    ",epCyg": Aljanah,
    ",zeCyg": zeCyg,
    ",etCyg": etCyg,
    ",thCyg": thCyg,
    ",io-2Cyg": io2Cyg,
    ",kaCyg": kaCyg,
    ",nuCyg": nuCyg,
    ",xiCyg": xiCyg,
    ",pi-1Cyg": Azelfafage,
    ",pi-2Cyg": pi2Cyg,
    ",rhCyg": rhCyg,
    ",siCyg": siCyg,
    ",upCyg": upCyg,
    ",ome-1Cyg": RuchbahI,
    ",ome-2Cyg": RuchbahII,
    ",Cyg61": Cyg61,
    ",CygA61": CygA61,
    ",Cyg34": Cyg34,
    ",alDel": Sualocin,
    ",beDel": Shravishtha,
    ",ga-2Del": ga2Del,
    ",deDel": deDel,
    ",epDel": Aldulfin,
    ",kaDel": kaDel,
    ",Del18": Musica,
    ",alDor": alDor,
    ",beDor": beDor,
    ",gaDor": gaDor,
    ",deDor": deDor,
    ",zeDor": zeDor,
    ",thDor": thDor,
    ",nuDor": nuDor,
    ",SN1987A": Sanduleak,
    ",alDra": Dhruva,
    ",beDra": Rastaban,
    ",gaDra": Etamin,
    ",deDra": Altais,
    ",epDra": Tyl,
    ",zeDra": Aldhibah,
    ",thDra": thDra,
    ",ioDra": EdAsich,
    ",kaDra": Ketu,
    ",laDra": Gianfar,
    ",muDra": Alrakis,
    ",nu-1Dra": Kuma,
    ",nu-2Dra": Kuma,
    ",xiDra": Grumium,
    ",omiDra": omiDra,
    ",siDra": Athafi,
    ",taDra": taDra,
    ",upDra": upDra,
    ",chDra": BatentabanBorealis,
    ",ps-1Dra": Dziban,
    ",omeDra": omeDra,
    ",etDra": Athebyne,
    ",phDra": BatentabanAustralis,
    ",Dra7": Tianyi,
    ",Dra8": Taiyi,
    ",Dra42": Fafnir,
    ",alEqu": Kitalpha,
    ",gaEqu": gaEqu,
    ",deEqu": deEqu,
    ",beEqu": beEqu,
    ",alEri": Achernar,
    ",beEri": Cursa,
    ",gaEri": Zaurak,
    ",deEri": Rana,
    ",epEri": Ran,
    ",etEri": Azha,
    ",th-1Eri": Acamar,
    ",zeEri": Zibal,
    ",ioEri": ioEri,
    ",kaEri": kaEri,
    ",laEri": laEri,
    ",muEri": muEri,
    ",nuEri": nuEri,
    ",xiEri": xiEri,
    ",omi-1Eri": Beid,
    ",omi-2Eri": Keid,
    ",phEri": phEri,
    ",ta-1Eri": ta1Eri,
    ",ta-2Eri": Angetenar,
    ",ta-3Eri": ta3Eri,
    ",ta-4Eri": ta4Eri,
    ",ta-5Eri": ta5Eri,
    ",ta-6Eri": ta6Eri,
    ",ta-8Eri": ta8Eri,
    ",ta-9Eri": ta9Eri,
    ",up-1Eri": up1Eri,
    ",up-2Eri": Theemin,
    ",up-3Eri": Beemim,
    ",up-4Eri": up4Eri,
    ",chEri": chEri,
    ",Eri53": Sceptrum,
    ",omeEri": omeEri,
    ",piEri": piEri,
    ",gEri": gEri,
    ",fEri": fEri,
    ",yEri": yEri,
    ",eEri": eEri,
    ",sEri": sEri,
    ",alFor": Dalim,
    ",beFor": beFor,
    ",deFor": deFor,
    ",kaFor": kaFor,
    ",la-1For": la1For,
    ",muFor": muFor,
    ",nuFor": nuFor,
    ",taFor": taFor,
    ",alGem": Castor,
    ",beGem": Punarvasu,
    ",gaGem": Almeisan,
    ",deGem": Wasat,
    ",epGem": Mebsuta,
    ",zeGem": Mekbuda,
    ",etGem": PropusetaGem,
    ",thGem": Nageba,
    ",ioGem": PropusiotGem,
    ",kaGem": AlKrikab,
    ",laGem": Alkibash,
    ",muGem": Tejat,
    ",nuGem": nuGem,
    ",xiGem": Alzirr,
    ",omiGem": Jishui,
    ",piGem": piGem,
    ",rhGem": rhGem,
    ",siGem": siGem,
    ",taGem": taGem,
    ",upGem": upGem,
    ",phGem": phGem,
    ",chGem": chGem,
    ",omeGem": omeGem,
    ",alGru": Alnair,
    ",beGru": Tiaki,
    ",gaGru": RasAlkurki,
    ",de-1Gru": de1Gru,
    ",de-2Gru": de2Gru,
    ",epGru": epGru,
    ",thGru": thGru,
    ",zeGru": zeGru,
    ",ioGru": ioGru,
    ",laGru": laGru,
    ",nuGru": nuGru,
    ",omiGru": omiGru,
    ",beHer": Kornephoros,
    ",alHer": Rasalgethi,
    ",al-1Her": al1Her,
    ",zeHer": Rutilicus,
    ",gaHer": gaHer,
    ",deHer": Sarin,
    ",epHer": KajamepsHer,
    ",etHer": Sofian,
    ",thHer": RukbalgethiGenubi,
    ",ioHer": AlJathiyah,
    ",kaHer": Marsic,
    ",laHer": Maasym,
    ",muHer": Melkarth,
    ",xiHer": xiHer,
    ",omiHer": omiHer,
    ",piHer": Fudail,
    ",siHer": siHer,
    ",taHer": RukbalgethiShemali,
    ",phHer": phHer,
    ",chHer": chHer,
    ",omeHer": Cujam,
    ",rhHer": rhHer,
    ",HD149026": Ogma,
    ",Apex": Apex,
    ",alHor": alHor,
    ",zeHor": zeHor,
    ",laHor": laHor,
    ",muHor": muHor,
    ",ioHor": ioHor,
    ",etHor": etHor,
    ",beHor": beHor,
    ",alHya": CorHydrae,
    ",beHya": beHya,
    ",gaHya": DhanabalShuja,
    ",deHya": Mautinah,
    ",epHya": Ashlesha,
    ",zeHya": Hydrobius,
    ",etHya": etHya,
    ",thHya": thHya,
    ",ioHya": ioHya,
    ",kaHya": kaHya,
    ",laHya": laHya,
    ",muHya": muHya,
    ",nuHya": Pleura,
    ",xiHya": xiHya,
    ",omiHya": omiHya,
    ",piHya": Sataghni,
    ",siHya": Minchir,
    ",ta-1Hya": Ukdahprima,
    ",ta-2Hya": Ukdahsecunda,
    ",up-1Hya": Zhang,
    ",up-2Hya": up2Hya,
    ",ch-1Hya": ch1Hya,
    ",alHyi": alHyi,
    ",beHyi": beHyi,
    ",gaHyi": gaHyi,
    ",deHyi": deHyi,
    ",epHyi": epHyi,
    ",et-2Hyi": et2Hyi,
    ",thHyi": thHyi,
    ",ioHyi": ioHyi,
    ",kaHyi": kaHyi,
    ",laHyi": laHyi,
    ",muHyi": muHyi,
    ",alInd": alInd,
    ",beInd": beInd,
    ",gaInd": gaInd,
    ",deInd": deInd,
    ",epInd": epInd,
    ",etInd": etInd,
    ",thInd": thInd,
    ",omiInd": omiInd,
    ",rhInd": rhInd,
    ",alLac": alLac,
    ",beLac": beLac,
    ",Lac1": Lac1,
    ",Lac2": Lac2,
    ",Lac4": Lac4,
    ",Lac5": Lac5,
    ",Lac6": Lac6,
    ",ga-1Leo": Algieba,
    ",deLeo": Purvaphalguni,
    ",epLeo": RasElasedAustralis,
    ",zeLeo": Adhafera,
    ",etLeo": AlJabhah,
    ",ioLeo": TszeTseang,
    ",kaLeo": AlMinliaralAsad,
    ",laLeo": Alterf,
    ",muLeo": Rasalas,
    ",xiLeo": xiLeo,
    ",omiLeo": Subra,
    ",siLeo": Shishimai,
    ",thLeo": Chort,
    ",piLeo": piLeo,
    ",rhLeo": Shir,
    ",taLeo": taLeo,
    ",upLeo": upLeo,
    ",phLeo": phLeo,
    ",chLeo": chLeo,
    ",psLeo": psLeo,
    ",alLep": Arneb,
    ",beLep": Nihal,
    ",gaLep": gaLep,
    ",deLep": deLep,
    ",epLep": Sasin,
    ",zeLep": zeLep,
    ",etLep": etLep,
    ",laLep": laLep,
    ",muLep": muLep,
    ",al-1Lib": al1Lib,
    ",beLib": ZubenEschamali,
    ",gaLib": ZubenElakrab,
    ",deLib": ZubenElakribi,
    ",ze-1Lib": ze1Lib,
    ",io-1Lib": io1Lib,
    ",kaLib": kaLib,
    ",laLib": laLib,
    ",nuLib": ZubenHakrabi,
    ",xi-2Lib": xi2Lib,
    ",siLib": Brachium,
    ",taLib": taLib,
    ",upLib": upLib,
    ",beLMi": beLMi,
    ",LMi46": Praecipua,
    ",LMi21": LMi21,
    ",alLup": Men,
    ",beLup": Kekouan,
    ",gaLup": Thusia,
    ",deLup": Hilasmus,
    ",epLup": epLup,
    ",etLup": etLup,
    ",zeLup": zeLup,
    ",thLup": thLup,
    ",ka-1Lup": ka1Lup,
    ",ka-2Lup": ka2Lup,
    ",ph-1Lup": ph1Lup,
    ",ph-2Lup": ph2Lup,
    ",ta-1Lup": ta1Lup,
    ",chLup": chLup,
    ",alLyn": AlFahd,
    ",Lyn31": Mabsuthat,
    ",kaLyn": Mabsuthat,
    ",Lyn38": Maculata,
    ",Lyn21": Lyn21,
    ",Lyn15": Lyn15,
    ",Lyn2": Lyn2,
    ",alLyr": Abhijit,
    ",beLyr": Sheliak,
    ",gaLyr": Sulafat,
    ",etLyr": Aladfar,
    ",thLyr": thLyr,
    ",ioLyr": ioLyr,
    ",kaLyr": kaLyr,
    ",muLyr": AlAthfar,
    ",ze-2Lyr": ze2Lyr,
    ",de-2Lyr": de2Lyr,
    ",ep-2Lyr": ep2Lyr,
    ",alMen": alMen,
    ",beMen": beMen,
    ",gaMen": gaMen,
    ",deMen": deMen,
    ",etMen": etMen,
    ",zeMen": zeMen,
    ",muMen": muMen,
    ",xiMen": xiMen,
    ",alMic": alMic,
    ",gaMic": gaMic,
    ",epMic": epMic,
    ",zeMic": zeMic,
    ",th-1Mic": th1Mic,
    ",ioMic": ioMic,
    ",alMon": alMon,
    ",beMon": beMon,
    ",gaMon": gaMon,
    ",deMon": deMon,
    ",epMon": epMon,
    ",zeMon": zeMon,
    ",Mon18": Mon18,
    ",Mon13": Mon13,
    ",alMus": alMus,
    ",beMus": beMus,
    ",gaMus": gaMus,
    ",deMus": deMus,
    ",epMus": epMus,
    ",etMus": etMus,
    ",laMus": laMus,
    ",muMus": muMus,
    ",ga-2Nor": ga2Nor,
    ",deNor": deNor,
    ",epNor": epNor,
    ",etNor": etNor,
    ",kaNor": kaNor,
    ",alOct": alOct,
    ",beOct": beOct,
    ",ga-1Oct": ga1Oct,
    ",deOct": deOct,
    ",etOct": etOct,
    ",epOct": epOct,
    ",thOct": thOct,
    ",zeOct": zeOct,
    ",ioOct": ioOct,
    ",kaOct": kaOct,
    ",nuOct": nuOct,
    ",rhOct": rhOct,
    ",siOct": PolarisAustralis,
    ",taOct": taOct,
    ",upOct": upOct,
    ",chOct": chOct,
    ",alOph": Rasalhague,
    ",beOph": KelbAlrai,
    ",gaOph": AlDurajah,
    ",deOph": YedPrior,
    ",epOph": YedPosterior,
    ",zeOph": Han,
    ",etOph": Sabik,
    ",thOph": Imad,
    ",ioOph": ioOph,
    ",kaOph": Helkath,
    ",laOph": Marfik,
    ",nuOph": Sinistra,
    ",xiOph": xiOph,
    ",siOph": siOph,
    ",V2500": Barnardsstar,
    ",Oph44": Oph44,
    ",Oph45": Oph45,
    ",alOri": Ardra,
    ",gaOri": Durga,
    ",deOri": Kumara,
    ",epOri": Ganesha,
    ",zeOri": Iyappa,
    ",etOri": Ensis,
    ",th-1Ori": Trapezium,
    ",ioOri": NairalSaif,
    ",kaOri": Saiph,
    ",laOri": Mrigashirsha,
    ",muOri": muOri,
    ",nuOri": nuOri,
    ",xiOri": xiOri,
    ",omi-1Ori": omi1Ori,
    ",pi-1Ori": pi1Ori,
    ",pi-2Ori": pi2Ori,
    ",pi-3Ori": Tabit,
    ",pi-4Ori": Tabit,
    ",pi-5Ori": pi5Ori,
    ",pi-6Ori": pi6Ori,
    ",taOri": taOri,
    ",upOri": Thabit,
    ",ph-1Ori": ph1Ori,
    ",ch-2Ori": ch2Ori,
    ",Ori71": Ori71,
    ",M42": Messier42,
    ",alPav": Peacock,
    ",bePav": bePav,
    ",gaPav": gaPav,
    ",dePav": dePav,
    ",epPav": epPav,
    ",zePav": zePav,
    ",etPav": etPav,
    ",laPav": laPav,
    ",xiPav": xiPav,
    ",omiPav": omiPav,
    ",alPhe": Ankaa,
    ",bePhe": bePhe,
    ",gaPhe": gaPhe,
    ",dePhe": dePhe,
    ",epPhe": epPhe,
    ",etPhe": etPhe,
    ",zePhe": Wurren,
    ",thPhe": thPhe,
    ",ioPhe": ioPhe,
    ",la-1Phe": la1Phe,
    ",muPhe": muPhe,
    ",piPhe": piPhe,
    ",upPhe": upPhe,
    ",phPhe": phPhe,
    ",psPhe": psPhe,
    ",omePhe": omePhe,
    ",alPeg": Purvabhadra,
    ",bePeg": Scheat,
    ",epPeg": Enif,
    ",zePeg": Homam,
    ",etPeg": Matar,
    ",thPeg": Baham,
    ",ioPeg": ioPeg,
    ",kaPeg": Jih,
    ",laPeg": Sadalbari,
    ",muPeg": muPeg,
    ",xiPeg": xiPeg,
    ",piPeg": piPeg,
    ",pi-1Peg": pi1Peg,
    ",pi-2Peg": pi2Peg,
    ",upPeg": Alkarab,
    ",phPeg": phPeg,
    ",chPeg": chPeg,
    ",psPeg": psPeg,
    ",Peg1": Peg1,
    ",Peg9": Peg9,
    ",Peg51": Helvetios,
    ",alPer": Mirphak,
    ",gaPer": gaPer,
    ",dePer": dePer,
    ",epPer": epPer,
    ",zePer": zePer,
    ",etPer": Miram,
    ",thPer": thPer,
    ",ioPer": ioPer,
    ",kaPer": Misam,
    ",laPer": laPer,
    ",muPer": muPer,
    ",nuPer": nuPer,
    ",xiPer": Menkib,
    ",omiPer": Atiks,
    ",piPer": GorgonaSecunda,
    ",rhPer": GorgonaTertia,
    ",siPer": siPer,
    ",taPer": taPer,
    ",phPer": phPer,
    ",omePer": GorgonaQuatra,
    ",Per16": Per16,
    ",alPic": alPic,
    ",bePic": bePic,
    ",gaPic": gaPic,
    ",dePic": dePic,
    ",zePic": zePic,
    ",et-2Pic": et2Pic,
    ",alPsA": Fomalhaut,
    ",bePsA": TienKang,
    ",gaPsA": gaPsA,
    ",dePsA": Aboras,
    ",epPsA": epPsA,
    ",thPsA": thPsA,
    ",ioPsA": ioPsA,
    ",laPsA": laPsA,
    ",muPsA": muPsA,
    ",piPsA": piPsA,
    ",alPsc": AlRescha,
    ",bePsc": Samakah,
    ",gaPsc": Simmah,
    ",dePsc": Linteum,
    ",epPsc": Kaht,
    ",zePscA": Revati,
    ",zePsc": Revati,
    ",etPsc": AlPherg,
    ",thPsc": thPsc,
    ",ioPsc": ioPsc,
    ",kaPsc": kaPsc,
    ",laPsc": laPsc,
    ",nuPsc": nuPsc,
    ",xiPsc": xiPsc,
    ",omiPsc": Torcular,
    ",piPsc": piPsc,
    ",taPsc": Anunitum,
    ",upPsc": upPsc,
    ",phPsc": phPsc,
    ",chPsc": chPsc,
    ",omePsc": Vernalis,
    ",Psc7": Psc7,
    ",Psc19": Psc19,
    ",zePup": SuhailHadar,
    ",nuPup": Kaimana,
    ",xiPup": Azmidiske,
    ",piPup": Ahadi,
    ",rhPup": Tureis,
    ",siPup": siPup,
    ",taPup": Anazitisi,
    ",pPup": pPup,
    ",P_Pup": P_Pup,
    ",k01Pup": k01Pup,
    ",J_Pup": J_Pup,
    ",alPyx": alPyx,
    ",bePyx": bePyx,
    ",gaPyx": gaPyx,
    ",epPyx": epPyx,
    ",thPyx": thPyx,
    ",alRet": alRet,
    ",beRet": beRet,
    ",gaRet": gaRet,
    ",deRet": deRet,
    ",epRet": epRet,
    ",ze-1Ret": ze1Ret,
    ",etRet": etRet,
    ",ioRet": ioRet,
    ",kaRet": kaRet,
    ",piScl": piScl,
    ",alScl": alScl,
    ",beScl": beScl,
    ",gaScl": gaScl,
    ",deScl": deScl,
    ",epScl": epScl,
    ",thScl": thScl,
    ",ka-2Scl": ka2Scl,
    ",la-2Scl": la2Scl,
    ",muScl": muScl,
    ",siScl": siScl,
    ",be-1Sco": Acrab,
    ",be-2Sco": be2Sco,
    ",epSco": Larawag,
    ",ze-2Sco": ze2Sco,
    ",etSco": etSco,
    ",thSco": Sargas,
    ",io-1Sco": io1Sco,
    ",kaSco": Girtab,
    ",laSco": Mula,
    ",mu-1Sco": Xamidimura,
    ",nuSco": Jabbah,
    ",xiSco": Grafias,
    ",piSco": Fang,
    ",rhSco": Iklil,
    ",siSco": Alniyat,
    ",taSco": taSco,
    ",upSco": Lesath,
    ",ome-1Sco": JabhatalAkrab,
    ",ome-2Sco": JabhatalAkrab,
    ",HR6630": Fuyue,
    ",mu-2Sco": Pipirima,
    ",alSct": alSct,
    ",beSct": beSct,
    ",gaSct": gaSct,
    ",deSct": deSct,
    ",epSct": epSct,
    ",zeSct": zeSct,
    ",alSer": CorSerpentis,
    ",beSer": Zhou,
    ",gaSer": Ainalhai,
    ",deSer": Chin,
    ",epSer": NullaPambu,
    ",etSer": Tang,
    ",th-1Ser": Alya,
    ",kaSer": kaSer,
    ",muSer": Leiolepidotus,
    ",nuSer": nuSer,
    ",xiSer": Nehushtan,
    ",omiSer": omiSer,
    ",siSer": siSer,
    ",ta-1Ser": ta1Ser,
    ",alSex": alSex,
    ",beSex": beSex,
    ",gaSex": gaSex,
    ",deSex": deSex,
    ",epSex": epSex,
    ",alSge": Sham,
    ",beSge": beSge,
    ",gaSge": gaSge,
    ",deSge": deSge,
    ",alSgr": Rukbat,
    ",be-1Sgr": ArkabPrior,
    ",be-2Sgr": ArkabPosterior,
    ",gaSgr": Alnasl,
    ",deSgr": Purvashadha,
    ",epSgr": KausAustralis,
    ",zeSgr": Ascella,
    ",etSgr": IraFuroris,
    ",th-1Sgr": th1Sgr,
    ",th-2Sgr": th2Sgr,
    ",ioSgr": ioSgr,
    ",ka-1Sgr": ka1Sgr,
    ",laSgr": KausBorealis,
    ",muSgr": Polis,
    ",nu-1Sgr": AinalRami,
    ",xi-2Sgr": xi2Sgr,
    ",omiSgr": Manubrium,
    ",piSgr": Albaldah,
    ",siSgr": Uttarashadha,
    ",taSgr": Hecatebolus,
    ",phSgr": Nanto,
    ",upSgr": upSgr,
    ",omeSgr": Terebellium,
    ",Sgr52": Sgr52,
    ",Sgr59": Sgr59,
    ",Sgr62": Sgr62,
    ",beTau": Alnath,
    ",gaTau": HyadumI,
    ",deTau": SecundaHyadum,
    ",de-1Tau": HyadumII,
    ",zeTau": Tianguan,
    ",etTau": Krttika,
    ",th-1Tau": Phaeo,
    ",th-2Tau": Chamukuy,
    ",ioTau": ioTau,
    ",laTau": Althaur,
    ",muTau": Kattupothu,
    ",nuTau": Furibundus,
    ",xiTau": Ushakaron,
    ",taTau": taTau,
    ",rhTau": rhTau,
    ",ome-1Tau": ome1Tau,
    ",Tau16": Celeano,
    ",Tau17": Electra,
    ",Tau19": Taygeta,
    ",Tau20": Maia,
    ",Tau21": SteropeI,
    ",Tau22": SteropeII,
    ",Tau23": Merope,
    ",Tau27": Atlas,
    ",Tau28": Pleione,
    ",alTel": alTel,
    ",epTel": epTel,
    ",zeTel": zeTel,
    ",ioTel": ioTel,
    ",laTel": laTel,
    ",nuTel": nuTel,
    ",xiTel": xiTel,
    ",alTrA": Atria,
    ",beTrA": beTrA,
    ",gaTrA": gaTrA,
    ",deTrA": deTrA,
    ",epTrA": epTrA,
    ",zeTrA": zeTrA,
    ",alTri": Mothallah,
    ",beTri": beTri,
    ",gaTri": gaTri,
    ",alTuc": alTuc,
    ",be-2Tuc": be2Tuc,
    ",gaTuc": gaTuc,
    ",epTuc": epTuc,
    ",zeTuc": zeTuc,
    ",ioTuc": ioTuc,
    ",la-2Tuc": la2Tuc,
    ",alUMa": Kratu,
    ",beUMa": Pulaha,
    ",gaUMa": Pulastya,
    ",deUMa": Atri,
    ",epUMa": Angiras,
    ",zeUMa": Vasishtha,
    ",etUMa": Marichi,
    ",thUMa": AlHaud,
    ",ioUMa": TalithaBorealis,
    ",kaUMa": Alkaphrah,
    ",laUMa": TaniaBorealis,
    ",muUMa": TaniaAustralis,
    ",nuUMa": AlulaBorealis,
    ",xiUMa": AlulaAustralis,
    ",omiUMa": Muscida,
    ",rhUMa": rhUMa,
    ",upUMa": upUMa,
    ",phUMa": phUMa,
    ",chUMa": Taiyangshou,
    ",psUMa": psUMa,
    ",UMa23": UMa23,
    ",UMa26": UMa26,
    ",UMa47": Chalawan,
    ",UMa80": Saidak,
    ",Uma80": Alc0,
    ",HR3743": Intercrus,
    ",beUMi": Kochab,
    ",gaUMi": Pherkad,
    ",deUMi": Yildun,
    ",epUMi": Urodelus,
    ",zeUMi": Pharkadain,
    ",etUMi": AnwaralFarkadain,
    ",laUMi": laUMi,
    ",UMi11": PherkadMinor,
    ",ga-2Vel": Regor,
    ",deVel": KooShe,
    ",kaVel": Markeb,
    ",laVel": Suhail,
    ",muVel": Alherem,
    ",omiVel": Xestus,
    ",phVel": TseenKe,
    ",psVel": psVel,
    ",dVel": dVel,
    ",eVel": eVel,
    ",pVel": pVel,
    ",qVel": qVel,
    ",tVel": tVel,
    ",beVir": Alaraph,
    ",gaVir": Porrima,
    ",deVir": Mineluva,
    ",epVir": Vindemiatrix,
    ",zeVir": Heze,
    ",etVir": Zaniah,
    ",thVir": thVir,
    ",ioVir": Syrma,
    ",kaVir": Kang,
    ",laVir": Khambalia,
    ",nuVir": nuVir,
    ",omiVir": omiVir,
    ",piVir": piVir,
    ",rhVir": rhVir,
    ",siVir": siVir,
    ",taVir": taVir,
    ",phVir": phVir,
    ",chVir": chVir,
    ",psVir": psVir,
    ",Vir109": Vir109,
    ",PSRB1257+12": Lich,
    ",M49": Messier49,
    ",alVol": alVol,
    ",beVol": beVol,
    ",ga-2Vol": ga2Vol,
    ",deVol": deVol,
    ",epVol": epVol,
    ",epVolA": epVolA,
    ",zeVol": zeVol,
    ",ioVol": ioVol,
    ",alVul": Anser,
    ",Vul2": Vul2,
    ",Vul12": Vul12,
    ",GCLiu": GCLiu,
    ",GP1958": GalPoleIAU1958,
    ",GPPlan": GalPlanePole,
    ",GEqu": GalEqu,
    ",IDrag": InfraredDragon,
    ",AA11": AA11_page_B73,
    ",GCRS00": GCRS00,
    ",ZE200": Zero2000,
    ",ZL200": ZerL2000,
    ",SunPole": SunPole,
    ",Test": Test,
    ",NGC4194": NGC4194,
    ",HD168442": Gliese710,
    # these are additions to faciliate ease of use
    # ,omiTau has the name "Atirsagne" in swe and i didnt like to search for omiTau
    "HIP 15900": OmicronTauri,
    ",48Lib": Librae48
}

class OneGeminorum(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",oneGem", context=context)

class KappaGeminorum(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",kapGem", context=context)

class ChiCancri(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",chiCnc", context=context)

class KappaLeonis(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",kapLeo", context=context)

class NuVirginis(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",nuVir", context=context)

class Paikauhale(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",tauSco", context=context)

class Ophiuci45(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",dOph", context=context)

class IotaAquarii(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",iotAqr", context=context)

class PhiAquarii(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",phiAqr", context=context)

class GammaPiscium(FixedStar): # ,oneGem

    def __init__(self, context = EphContext()): 
        super().__init__(swe_id = ",gamPsc", context=context)

natural_stars_ext = {
    ",oneGem": OneGeminorum,
    ",kapGem": KappaGeminorum,
    ",chiCnc": ChiCancri,
    ",kapLeo": KappaLeonis,
    ",nuVir": NuVirginis,
    ",tauSco": Paikauhale,
    ",dOph": Ophiuci45,
    ",iotAqr": IotaAquarii,
    ",phiAqr": PhiAquarii,
    ",gamPsc": GammaPiscium
}

# if you want a Stellarium star
# in clude "st:" at the beginning of swe_id
# and pass "rc", a stars.stellarium.stellarium.Stellarium instance, which is the connection to Stellarium

the_stars = natural_stars | natural_stars_ext

class Constellation:
    """
    class to model a constellation in true sidereal astrology
    needs to have a first star and a last star, which can be used to
    find a midpoint between this constellation and thus next, and thus the sign boundary on the ecliptic
    """

    def __init__(self, first_star: FixedStar, last_star: FixedStar, context=EphContext()):
        self._first_star = first_star
        self._last_star = last_star
        self.attributes = dict()

    def set_attribute(self, attrs):
        """
        attrs is a tuple ("attribute",value)
        add all of these to self.attributes
        attritube is a string that will be a dictionary key for value
        """
        key,value=attrs
        self.attributes[key] = value
        

    def first_star(self):
        return self._first_star

    def last_star(self):
        return self._last_star

    def name(self):
        return self._name

    def constellation_index(self):
        return self._constellation_index

    def constellation_number(self):
        return self.constellation_index()+1

    def beginning(self):
        return self.attributes["beginning"]

    def end(self):
        return self.attributes["end"]

class Aries(Constellation):

    def __init__(self, first_star = Mesarthim(), last_star = Botein(), context=EphContext()):
        self._name = "Aries"
        self._constellation_index = 0
        super().__init__(first_star,last_star,context)

class Taurus(Constellation):

    def __init__(self, first_star = OmicronTauri(), last_star = Tianguan(), context=EphContext()):
        self._name = "Taurus"
        self._constellation_index = 1
        super().__init__(first_star,last_star,context)

class Gemini(Constellation):

    def __init__(self, first_star = OneGeminorum(), last_star = KappaGeminorum(), context=EphContext()):
        self._name = "Gemini"
        self._constellation_index = 2
        super().__init__(first_star,last_star,context)

class Cancer(Constellation):

    def __init__(self, first_star = ChiCancri(), last_star = Acubens(), context=EphContext()):
        self._name = "Cancer"
        self._constellation_index = 3
        super().__init__(first_star,last_star,context)

class Leo(Constellation):

    def __init__(self, first_star = KappaLeonis(), last_star = Denebola(), context=EphContext()):
        self._name = "Leo"
        self._constellation_index = 4
        super().__init__(first_star,last_star,context)

class Virgo(Constellation):

    def __init__(self, first_star = NuVirginis(), last_star = RijlAlAwwa(), context=EphContext()):
        self._name = "Virgo"
        self._constellation_index = 5
        super().__init__(first_star,last_star,context)

class Libra(Constellation):

    def __init__(self, first_star = Zubenelgenubi(), last_star = Librae48(), context=EphContext()):
        self._name = "Libra"
        self._constellation_index = 6
        super().__init__(first_star,last_star,context)

class Scorpio(Constellation):

    def __init__(self, first_star = Dschubba(), last_star = Paikauhale(), context=EphContext()):
        self._name = "Scorpio"
        self._constellation_index = 7
        super().__init__(first_star,last_star,context)

class Ophiucus(Constellation):

    def __init__(self, first_star = Sabik(), last_star = Ophiuci45(), context=EphContext()):
        self._name = "Ophiucus"
        self._constellation_index = 8
        super().__init__(first_star,last_star,context)

class Sagittarius(Constellation):

    def __init__(self, first_star = Alnasl(), last_star = Terebellium(), context=EphContext()):
        self._name = "Sagittarius"
        self._constellation_index = 9
        super().__init__(first_star,last_star,context)

class Capricorn(Constellation):

    def __init__(self, first_star = Dabih(), last_star = DenebAlgedi(), context=EphContext()):
        self._name = "Capricorn"
        self._constellation_index = 10
        super().__init__(first_star,last_star,context)

class Aquarius(Constellation):

    def __init__(self, first_star = IotaAquarii(), last_star = PhiAquarii(), context=EphContext()):
        self._name = "Aquarius"
        self._constellation_index = 11 
        super().__init__(first_star,last_star,context)

class Pisces(Constellation):

    def __init__(self, first_star = GammaPiscium(), last_star = AlRescha(), context=EphContext()):
        self._name = "Pisces"
        self._constellation_index = 12
        super().__init__(first_star,last_star,context)

class Ecliptic:

    number_to_name = {
        1: "Aries",
        2: "Taurus",
        3: "Gemini",
        4: "Cancer",
        5: "Leo",
        6: "Virgo",
        7: "Libra",
        8: "Scorpio",
        9: "Ophiucus",
        10: "Sagittarius",
        11: "Capricorn",
        12: "Aquarius",
        13: "Pisces"
    }

    def __init__(self, context = EphContext()):
        self.context = context
        self.context.sysflg = const.SID
        self.context.ayanamsa = 97
        utils.set_swe_true_sidereal_ayanamsa()
        self._constellations = self.init_Constellations()
        self._boundaries = self.init_boundaries()

    def __iter__(self):
        return iter(self._constellations.values())

    def __getitem__(self,n):
        if isinstance(n,int):
            return self._constellations[self.number_to_name[n]]
        return self._constellations[n] 

    def init_Constellations(self):
        """
        intialize the 13 Constellation classes that make up the ecliptic, starting with Aries
        """
        consts = {}
        consts["Aries"] = Aries(Mesarthim(self.context),Botein(self.context),self.context)
        consts["Taurus"] = Taurus(OmicronTauri(self.context),Tianguan(self.context))
        consts["Gemini"] = Gemini(OneGeminorum(self.context),KappaGeminorum(self.context),self.context)
        consts["Cancer"] = Cancer(ChiCancri(self.context),Acubens(self.context),self.context)
        consts["Leo"] = Leo(KappaLeonis(self.context),Denebola(self.context),self.context)
        consts["Virgo"] = Virgo(NuVirginis(self.context),RijlAlAwwa(self.context),self.context)
        consts["Libra"] = Libra(Zubenelgenubi(self.context),Librae48(self.context),self.context)
        consts["Scorpio"] = Scorpio(Dschubba(self.context),Paikauhale(self.context),self.context)
        consts["Ophiucus"] = Ophiucus(Sabik(self.context),Ophiuci45(self.context),self.context)
        consts["Sagittarius"] = Sagittarius(Alnasl(self.context),Terebellium(self.context),self.context)
        consts["Capricorn"] = Capricorn(Dabih(self.context),DenebAlgedi(self.context),self.context)
        consts["Aquarius"] = Aquarius(IotaAquarii(self.context),PhiAquarii(self.context),self.context)
        consts["Pisces"] = Pisces(GammaPiscium(self.context),AlRescha(self.context),self.context)
        return consts

    def init_boundaries(self) -> [float]:
        """
        find the boundaries according to the midpoint method

        returns a list of boundaries, the beginning of Aries, of Taurus, etc.
        """
        # calculate in order, starting with the last start of Aries to first star of Taurus, etc.
        # then put the last element to the front; the last element being last star of Pisces to first star of Aries,
        # i.e., the beginning of the zodiac
        ret = []
        for constellation in self:
            if constellation.name() == "Pisces":
                next_star_key = "Aries"
                next_star = self[next_star_key].first_star()
                distance = constellation.last_star().degrees_apart(next_star.amsha_longitude())
            else:
                # how far the next star of next constellation is from last star of this constellation
                next_star_key = self.number_to_name[constellation.constellation_number()+1]
                next_star = self[next_star_key].first_star()
                distance = constellation.last_star().degrees_apart(next_star.amsha_longitude())
            # go forward half this distance from the star of this constellation; that is the end of this constellation
            # and the beginning of the next constellation
            midpoint = (constellation.last_star().amsha_longitude() + distance/2)%360
            constellation.set_attribute(("end",midpoint))
            self[next_star_key].set_attribute(("beginning",midpoint))
            ret.append(midpoint)
        # the last point between Pisces and Aries is actually the first, so put it there
        return ret[-1:] + ret[:-1]

    def boundaries(self):
        return self._boundaries

    def constellations(self):
        return self._constellations
    def aries(self):
        return self.constellations()["Aries"]
    def taurus(self):
        return self.constellations()["Taurus"]
    def gemini(self):
        return self.constellations()["Gemini"]
    def cancer(self):
        return self.constellations()["Cancer"]
    def leo(self):
        return self.constellations()["Leo"]
    def virgo(self):
        return self.constellations()["Virgo"]
    def libra(self):
        return self.constellations()["Libra"]
    def scorpio(self):
        return self.constellations()["Scorpio"]
    def ophiucus(self):
        return self.constellations()["Ophiucus"]
    def sagittarius(self):
        return self.constellations()["Sagittarius"]
    def capricorn(self):
        return self.constellations()["Capricorn"]
    def aquarius(self):
        return self.constellations()["Aquarius"]
    def pisces(self):
        return self.constellations()["Pisces"]


class TheStars:
    """
    represents all of the fixed stars
    should be the main interface through which to interact with the stars
    but you can also use fixed_stars.FixedStar()
    """

    def __init__(self, context=EphContext(), stellarium=False) -> dict:
        self.context = context
        # defined just above
        self._natural_stars = natural_stars
        self._the_stars = the_stars
        if stellarium:
            self.the_stellarium = self.init_Stellarium()

    def __getitem__(self,key):
        """
        keys:
        (,)noMen for swe objects
        other for stellarium; best is to use HIP object has it

        instantiate star denoted by key with this context
        so you can or not used "," for the (,)noMen name
        (,)noMen name is used by swisseph (swe)
        "HIP nnnnn" is used by Stellarium
        also, names with spaces, e.g., "M 31", which is a galaxy, can be instantiated into a FixedStar
        """
        if "HIP" in key or " " in key or key[0].isupper():
            # all of these indicate objects that can be found with Stellarium().info(key)
            # or in stars.the_stars.the_stars
            if self.the_stellarium:
                # the_stellarium is our Stellarium() object
                # the key is a we want from Stellarium, so we have to pass the "phone", so to speak
                if key in self._the_stars.keys():
                    return self._the_stars[key](self.context,self.the_stellarium)
                else:
                    # return whatever object Stellarium finds
                    return FixedStar(key,self.context,self.the_stellarium)
            print("Stellarium not available...")
            return
        elif not "," in key:
            key = ","+key
        return self._the_stars[key](self.context)

    def natural_stars(self):
        """
        this is the main interface here
        essentially is a dictionary, with the key being "nomenclature" name of the star
        the value is the traditional name of the star
        """
        return self._natural_stars

    def search_star_interactive(self, bitflags=swe.FLG_TROPICAL) -> FixedStar:
        """
        this returns a FixedStar class of the specific star, if there is one, else error
        e.g., to get Aldebaran:
        >>>  aldebaran = TheStars().search_star_interactive()
        enter "alde" (Enter)
        this gives you the constructor
        <class 'libaditya.stars.the_stars.Aldebaran'>
        a star by itself needs a context; you can use Chart().context to pass it the information for any chart
        you are working with and it will intialize accordingly
        """
        pattern = input("Enter first few letters of traditional name as appears in .../ephe/sefstars.txt: ")
        if not "," in pattern:
            # then they are searching a traditional name, so include wildcard
            pattern = f"{pattern}%"
        information, name, retflags = swe.fixstar2_ut(pattern,self.context.timeJD.jd_number(),bitflags)
        print(f"Star: {name} appears at {information[0]} longitude on {self.context.timeJD}")
        return self[name.split(",")[1]]

    def print_the_stars(self) -> None:
        for n,(nomen,constructor) in enumerate(self.natural_stars().items()):
            print(f"{n}\t{nomen}\t{constructor().name()}")


    def make_swe_star(self, names=[""]):
        """
        make an entry for ephe/sefstars.txt to add star "name" to that file, and thus to swe
        """
        import urllib
        from string import Template
        simbad_query = Template("https://simbad.cds.unistra.fr/simbad/sim-id?Ident=$swe_id&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit%20id&output.format=ASCII")
        swe_star_entry = Template("$trad_name,$nomen_name,$ra_hour,$ra_minute,$ra_sec,$dec_degree,$dec_minute,$dec_sec,$pmra,$pmde,$rad_vel,$parallax,$magnitude_V")
        if not isinstance(names,list):
            names=[names]
        ret = []
        for name in names:
            name = name.replace(" ","+")
            the_bytes = urllib.request.urlopen(simbad_query.substitute(swe_id=name))
#            lines=the_bytes.read().decode().split("\n")
#            for n,line in enumerate(lines):
#                print(n,line)
            # now parse bytes into all the variables needs for swe_star_entry
            trad_name,nomen_name,ra_hour,ra_minute,ra_sec,dec_degree,dec_minute,dec_sec,pmra,pmde,rad_vel,parallax,magV = utils.parse_simbad_ascii_response(the_bytes)
            ret.append(f"{trad_name}{nomen_name},ICRS,{ra_hour},{ra_minute},{ra_sec},{dec_degree},{dec_minute},{dec_sec},{pmra},{pmde},{rad_vel},{parallax},{magV}")
        return ret

    def stellarium(self):
        return self.the_stellarium

    def init_Stellarium(self, ip="127.0.0.1", port="8090", password=""):
        """
        if you are using this alot, assign the return value to a variable
        if not, it will reconnect each time, making each operation very slow
        so: not: chart(context).stars()["Andromeda"], chart(context).stars()["OmiTau"]
        but: thestars=chart(context).stars(), then thestars["Andromeda"], etc.
        note: both swe and stellarium objects can be instantiated using [] notation
        it works for any key,object pair in the dictionary stars.the_stars.the_stars=TheStars._the_stars

        if you get an http error, it is because stellarium is not on, or the RemoteControl plugin is not on
        start stellarium, press F2, go the rightmost tab, Plugins. on the left, go down to "Remote Control"
        bottom left of the information about the plugin:
        Options
        Load at startup
        if "Load at startup" is not checked, then check it and restart stellarium
        then go back to F2->Plugins->Remote Control
        then click "Configure"
        click "Server Enabled"; that will turn the server on, then you can use the default ip, port, and password options here
        if you want it to load automatically, check "Enable automatically on startup"
        """
        try:
            return Stellarium(self.context,ip,port,password) 
        except:
            print("Stellarium not available...")
            return
