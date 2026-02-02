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

"""
FixedStars populated from ephe/sefstars.txt
this is most of the stars in there
some have more than one traditional name; in that case only one appears here
unless I have manually added a different one
"""

import swisseph as swe

from libaditya.objects import EphContext

from .fixed_stars import TheStars, FixedStar

class GalacticCenter(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",SgrA*", context=context)

class GalacticPole(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",GPol", context=context)

class Sirius(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCMa", context=context)

class Kerb(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taPeg", context=context)

class DenebKaitos(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioCet", context=context)

class Algenib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPeg", context=context)

class Alpheratz(FixedStar):
    
    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAnd", context=context)

class Erakis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muCep", context=context)

# these are stars used in True Sidereal midpoint method


class Acubens(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCnc", context=context)

class Denebola(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beLeo", context=context)

class RijlAlAwwa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muVir", context=context)

class Zubenelgenubi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",al-2Lib", context=context)

class Dschubba(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deSco", context=context)

class Alnasl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-2Sgr", context=context)

# below is all the stars in .../ephe/sefstars.txt

class Aldebaran(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alTau", context=context)

class Algol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",bePer", context=context)

class Jyeshtha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alSco", context=context)

class Magha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alLeo", context=context)

class Lubdhaka(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCMa", context=context)

class Citra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alVir", context=context)

class Trappist1(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",Trappist-1", context=context)

class GalacticCenter(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",SgrA*", context=context)

class GreatAttractor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",GA", context=context)

class VirgoCluster(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",VC", context=context)

class AndromedaGalaxy(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",M31", context=context)

class PraesepeCluster(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",M44", context=context)

class Polaris(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alUMi", context=context)

class Messier87(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",M87", context=context)

class A3558(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ACO3558", context=context)

class Deneb(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCyg", context=context)

class Rigel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beOri", context=context)

class Mira(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiCet", context=context)

class Ain(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epTau", context=context)

class Segin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCas", context=context)

class Sirrah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAnd", context=context)

class Mirach(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beAnd", context=context)

class Almach(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-1And", context=context)

class deAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deAnd", context=context)

class epAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epAnd", context=context)

class zeAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeAnd", context=context)

class ioAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioAnd", context=context)

class kaAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaAnd", context=context)

class laAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laAnd", context=context)

class muAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muAnd", context=context)

class nuAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuAnd", context=context)

class Adhil(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiAnd", context=context)

class omiAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiAnd", context=context)

class piAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piAnd", context=context)

class rhAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhAnd", context=context)

class siAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siAnd", context=context)

class Titawin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upAnd", context=context)

class psAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psAnd", context=context)

class omeAnd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omeAnd", context=context)

class Veritate(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",14And", context=context)

class Nembus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",51And", context=context)

class alAnt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAnt", context=context)

class epAnt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epAnt", context=context)

class thAnt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thAnt", context=context)

class ioAnt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioAnt", context=context)

class alAps(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAps", context=context)

class beAps(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beAps", context=context)

class gaAps(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaAps", context=context)

class de1Aps(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",de-1Aps", context=context)

class thAps(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thAps", context=context)

class ioAps(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioAps", context=context)

class ka1Aps(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ka-1Aps", context=context)

class Shravana(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAql", context=context)

class Alshain(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beAql", context=context)

class Tarazed(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaAql", context=context)

class AlMizan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deAql", context=context)

class DenebelOkabBorealis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epAql", context=context)

class Dheneb(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeAql", context=context)

class Bazak(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etAql", context=context)

class TseenFoo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thAql", context=context)

class AlThalimaimPosterior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioAql", context=context)

class kaAql(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaAql", context=context)

class AlThalimaimAnterior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laAql", context=context)

class muAql(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muAql", context=context)

class rhAql(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhAql", context=context)

class taAql(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taAql", context=context)

class ome1Aql(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ome-1Aql", context=context)

class Libertas(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiAql", context=context)

class Bered(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",12Aql", context=context)

class Sadalmelik(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAqr", context=context)

class Sadalsuud(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beAqr", context=context)

class Sadachbia(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaAqr", context=context)

class Skat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deAqr", context=context)

class Altager(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epAqr", context=context)

class Sadaltager(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ze-1Aqr", context=context)

class Deli(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etAqr", context=context)

class Ancha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thAqr", context=context)

class ioAqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioAqr", context=context)

class Situla(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaAqr", context=context)

class Shatabhishak(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laAqr", context=context)

class muAqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muAqr", context=context)

class Albulaan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuAqr", context=context)

class Seat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piAqr", context=context)

class siAqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siAqr", context=context)

class ta2Aqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-2Aqr", context=context)

class phAqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phAqr", context=context)

class Bunda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiAqr", context=context)

class upAqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upAqr", context=context)

class ps1Aqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ps-1Aqr", context=context)

class ps3Aqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ps-3Aqr", context=context)

class ome2Aqr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ome-2Aqr", context=context)

class Aqr3(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",3Aqr", context=context)

class Aqr88(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",88Aqr", context=context)

class Aqr98(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",98Aqr", context=context)

class Ara(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAra", context=context)

class beAra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beAra", context=context)

class gaAra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaAra", context=context)

class deAra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deAra", context=context)

class ep1Ara(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ep-1Ara", context=context)

class zeAra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeAra", context=context)

class etAra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etAra", context=context)

class thAra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thAra", context=context)

class Cervantes(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muAra", context=context)

class Hamal(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAri", context=context)

class Ashvini(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beAri", context=context)

class Mesarthim(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaAri", context=context)

class Botein(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deAri", context=context)

class zeAri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeAri", context=context)

class thAri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thAri", context=context)

class nuAri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuAri", context=context)

class siAri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siAri", context=context)

class ta1Ari(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-1Ari", context=context)

class LiliiBorea(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",39Ari", context=context)

class Bharani(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",41Ari", context=context)

class Brahmahridaya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alAur", context=context)

class Menkalinan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beAur", context=context)

class Prijipati(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deAur", context=context)

class AlAnz(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epAur", context=context)

class Saclateni(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeAur", context=context)

class Haedus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etAur", context=context)

class Mahasim(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thAur", context=context)

class AlKhabdhilinan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioAur", context=context)

class kaAur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaAur", context=context)

class laAur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laAur", context=context)

class muAur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muAur", context=context)

class nuAur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuAur", context=context)

class xiAur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiAur", context=context)

class omiAur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiAur", context=context)

class chAur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chAur", context=context)

class ps1Aur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ps-1Aur", context=context)

class ps5Aur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ps-5Aur", context=context)

class ps6Aur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ps-6Aur", context=context)

class Svati(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alBoo", context=context)

class Nekkar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beBoo", context=context)

class Haris(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaBoo", context=context)

class Princeps(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deBoo", context=context)

class Pulcherrima(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epBoo", context=context)

class zeBoo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeBoo", context=context)

class Muphrid(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etBoo", context=context)

class AsellusPrimus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thBoo", context=context)

class AsellusSecundus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioBoo", context=context)

class AsellusTertius(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ka-2Boo", context=context)

class Xuange(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laBoo", context=context)

class Alkalurops(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",mu-1Boo", context=context)

class nu1Boo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nu-1Boo", context=context)

class AlHamalain(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhBoo", context=context)

class HemeleinSecunda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siBoo", context=context)

class taBoo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taBoo", context=context)

class Ceginus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phBoo", context=context)

class psBoo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psBoo", context=context)

class Merga(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",38Boo", context=context)

class alCae(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCae", context=context)

class beCae(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCae", context=context)

class deCae(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCae", context=context)

class alCam(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCam", context=context)

class beCam(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCam", context=context)

class gaCam(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCam", context=context)

class Cam2(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",2Cam", context=context)

class Cam7(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",7Cam", context=context)

class Tonatiuh(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",HR4609", context=context)

class GiediPrima(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",al-1Cap", context=context)

class GiediSecunda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",al-2Cap", context=context)

class Dabih(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCap", context=context)

class Dabih(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",be-1Cap", context=context)

class Nashira(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCap", context=context)

class DenebAlgedi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCap", context=context)

class Castra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCap", context=context)

class Marakk(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCap", context=context)

class Armus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCap", context=context)

class Dorsum(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCap", context=context)

class ioCap(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioCap", context=context)

class laCap(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laCap", context=context)

class muCap(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muCap", context=context)

class Alshat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuCap", context=context)

class Oculus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piCap", context=context)

class Bos(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhCap", context=context)

class Pazhan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psCap", context=context)

class upCap(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upCap", context=context)

class BatenAlgiedi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omeCap", context=context)

class Cap24(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",24Cap", context=context)

class Cap36(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",36Cap", context=context)

class Agastya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCar", context=context)

class Miaplacidus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCar", context=context)

class Avior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCar", context=context)

class Foramen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCar", context=context)

class VathorzPosterior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCar", context=context)

class Aspidiske(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioCar", context=context)

class Drys(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chCar", context=context)

class Simiram(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omeCar", context=context)

class VathorzPrior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upCar", context=context)

class qCar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",qCar", context=context)

class Schedir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCas", context=context)

class Caph(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCas", context=context)

class Cih(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCas", context=context)

class Rucha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCas", context=context)

class Fulu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCas", context=context)

class Achird(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCas", context=context)

class kaCas(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaCas", context=context)

class Marfak(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muCas", context=context)

class omiCas(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiCas", context=context)

class rhCas(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhCas", context=context)

class psCas(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psCas", context=context)

class Castula(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",up-2Cas", context=context)

class ProximaCentauri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCen", context=context)

class Agena(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCen", context=context)

class Muhlifain(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCen", context=context)

class deCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCen", context=context)

class Birdun(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCen", context=context)

class zeCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCen", context=context)

class etCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCen", context=context)

class Menkent(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCen", context=context)

class Alhakim(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioCen", context=context)

class KeKwan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaCen", context=context)

class Mati(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laCen", context=context)

class muCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muCen", context=context)

class KabkentSecunda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuCen", context=context)

class xi2Cen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xi-2Cen", context=context)

class piCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piCen", context=context)

class siCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siCen", context=context)

class KabkentTertia(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phCen", context=context)

class psCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psCen", context=context)

class dCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",dCen", context=context)

class rhCen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhCen", context=context)

class ProximaCentauri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",V645 Cen", context=context)

class Alderamin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCep", context=context)

class Alfirk(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCep", context=context)

class Errai(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCep", context=context)

class Alredif(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCep", context=context)

class Phicareus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCep", context=context)

class Kurhah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCep", context=context)

class Alagemin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCep", context=context)

class Alkidr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCep", context=context)

class Alvahet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioCep", context=context)

class kaCep(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaCep", context=context)

class TheGarnetStar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muCep", context=context)

class nuCep(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuCep", context=context)

class Alkurhah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiCep", context=context)

class AlKalbalRai(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhCep", context=context)

class Menkar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCet", context=context)

class Difda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCet", context=context)

class Kaffaljidhma(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCet", context=context)

class Phycochroma(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCet", context=context)

class BatenKaitos(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCet", context=context)

class DenebAlgenubi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCet", context=context)

class Altawk(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCet", context=context)

class Shemali(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioCet", context=context)

class Menkar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laCet", context=context)

class muCet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muCet", context=context)

class nuCet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuCet", context=context)

class xi1Cet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xi-1Cet", context=context)

class xi2Cet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xi-2Cet", context=context)

class AlSadralKetus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piCet", context=context)

class rhCet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhCet", context=context)

class siCet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siCet", context=context)

class taCet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taCet", context=context)

class AbyssusAqueus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upCet", context=context)

class AlNitham(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ph-1Cet", context=context)

class ph2Cet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ph-2Cet", context=context)

class chCet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chCet", context=context)

class alCha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCha", context=context)

class beCha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCha", context=context)

class gaCha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCha", context=context)

class de2Cha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",de-2Cha", context=context)

class etCha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCha", context=context)

class thCha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCha", context=context)

class piCha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piCha", context=context)

class alCir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCir", context=context)

class beCir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCir", context=context)

class Murzims(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCMa", context=context)

class Isis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCMa", context=context)

class Wezen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCMa", context=context)

class Adhara(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCMa", context=context)

class Furud(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCMa", context=context)

class Aludra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCMa", context=context)

class kaCMa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaCMa", context=context)

class xi2CMa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xi-2CMa", context=context)

class omi2CMa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omi-2CMa", context=context)

class Unurgunite(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siCMa", context=context)

class thCMa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCMa", context=context)

class Procyon(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCMi", context=context)

class Gomeisa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCMi", context=context)

class zeCMi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCMi", context=context)

class Ashlesha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCnc", context=context)

class AlTarf(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCnc", context=context)

class AsellusBorealis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCnc", context=context)

class Pushya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCnc", context=context)

class Meleph(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCnc", context=context)

class Tegmine(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCnc", context=context)

class etCnc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCnc", context=context)

class Decapoda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioCnc", context=context)

class kaCnc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaCnc", context=context)

class xiCnc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiCnc", context=context)

class si3Cnc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",si-3Cnc", context=context)

class chCnc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chCnc", context=context)

class ome1Cnc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ome-1Cnc", context=context)

class Copernicus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",55Cnc", context=context)

class Phact(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCol", context=context)

class Wazn(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCol", context=context)

class GhusnalZaitun(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCol", context=context)

class gaCol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCol", context=context)

class etCol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCol", context=context)

class AlKurud(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaCol", context=context)

class Tsze(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laCol", context=context)

class omiCol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiCol", context=context)

class epCol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCol", context=context)

class Diadem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCom", context=context)

class Aldafirah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCom", context=context)

class Kissin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCom", context=context)

class Gemma(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCrB", context=context)

class Nusakan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCrB", context=context)

class epCrB(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCrB", context=context)

class thCrB(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCrB", context=context)

class kaC1GrB(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaC1GrB", context=context)

class BlazeStar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",tCrB", context=context)

class taCrB(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taCrB", context=context)

class gaCrB(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCrB", context=context)

class deCrB(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCrB", context=context)

class ioCrB(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioCrB", context=context)

class Meridiana(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCrA", context=context)

class et1CrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",et-1CrA", context=context)

class thCrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCrA", context=context)

class epCrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCrA", context=context)

class gaCrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCrA", context=context)

class beCrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCrA", context=context)

class deCrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCrA", context=context)

class zeCrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCrA", context=context)

class Alkes(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCrt", context=context)

class Alsharasif(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCrt", context=context)

class gaCrt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCrt", context=context)

class Labrum(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCrt", context=context)

class epCrt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCrt", context=context)

class etCrt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCrt", context=context)

class thCrt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCrt", context=context)

class zeCrt(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCrt", context=context)

class Mimosa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCru", context=context)

class Gacrux(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCru", context=context)

class Decrux(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCru", context=context)

class Ginan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCru", context=context)

class Alchita(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alCrv", context=context)

class Kraz(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCrv", context=context)

class GienahCorvi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCrv", context=context)

class Hasta(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCrv", context=context)

class Minkar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCrv", context=context)

class AvisSatyra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCrv", context=context)

class CorCaroli(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",al-2CVn", context=context)

class Chara(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beCVn", context=context)

class Albireo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",be-1Cyg", context=context)

class Sadr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaCyg", context=context)

class AlFawaris(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deCyg", context=context)

class Aljanah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epCyg", context=context)

class zeCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeCyg", context=context)

class etCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etCyg", context=context)

class thCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thCyg", context=context)

class io2Cyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",io-2Cyg", context=context)

class kaCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaCyg", context=context)

class nuCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuCyg", context=context)

class xiCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiCyg", context=context)

class Azelfafage(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-1Cyg", context=context)

class pi2Cyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-2Cyg", context=context)

class rhCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhCyg", context=context)

class siCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siCyg", context=context)

class upCyg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upCyg", context=context)

class RuchbahI(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ome-1Cyg", context=context)

class RuchbahII(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ome-2Cyg", context=context)

class Cyg61(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",61Cyg", context=context)

class CygA61(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",61CygA", context=context)

class Sualocin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alDel", context=context)

class Shravishtha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beDel", context=context)

class ga2Del(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-2Del", context=context)

class deDel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deDel", context=context)

class Aldulfin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epDel", context=context)

class kaDel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaDel", context=context)

class Musica(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",18Del", context=context)

class alDor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alDor", context=context)

class beDor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beDor", context=context)

class gaDor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaDor", context=context)

class deDor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deDor", context=context)

class zeDor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeDor", context=context)

class thDor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thDor", context=context)

class nuDor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuDor", context=context)

class Sanduleak(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",SN1987A", context=context)

class Dhruva(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alDra", context=context)

class Rastaban(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beDra", context=context)

class Etamin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaDra", context=context)

class Altais(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deDra", context=context)

class Tyl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epDra", context=context)

class Aldhibah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeDra", context=context)

class thDra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thDra", context=context)

class EdAsich(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioDra", context=context)

class Ketu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaDra", context=context)

class Gianfar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laDra", context=context)

class Alrakis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muDra", context=context)

class Kuma(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nu-1Dra", context=context)

class Kuma(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nu-2Dra", context=context)

class Grumium(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiDra", context=context)

class omiDra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiDra", context=context)

class Athafi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siDra", context=context)

class taDra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taDra", context=context)

class upDra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upDra", context=context)

class BatentabanBorealis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chDra", context=context)

class Dziban(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ps-1Dra", context=context)

class omeDra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omeDra", context=context)

class Athebyne(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etDra", context=context)

class BatentabanAustralis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phDra", context=context)

class Tianyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",7Dra", context=context)

class Taiyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",8Dra", context=context)

class Fafnir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",42Dra", context=context)

class Kitalpha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alEqu", context=context)

class gaEqu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaEqu", context=context)

class deEqu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deEqu", context=context)

class beEqu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beEqu", context=context)

class Achernar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alEri", context=context)

class Cursa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beEri", context=context)

class Zaurak(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaEri", context=context)

class Rana(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deEri", context=context)

class Ran(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epEri", context=context)

class Azha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etEri", context=context)

class Acamar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",th-1Eri", context=context)

class Zibal(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeEri", context=context)

class ioEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioEri", context=context)

class kaEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaEri", context=context)

class laEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laEri", context=context)

class muEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muEri", context=context)

class nuEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuEri", context=context)

class xiEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiEri", context=context)

class Beid(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omi-1Eri", context=context)

class Keid(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omi-2Eri", context=context)

class phEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phEri", context=context)

class ta1Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-1Eri", context=context)

class Angetenar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-2Eri", context=context)

class ta3Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-3Eri", context=context)

class ta4Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-4Eri", context=context)

class ta5Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-5Eri", context=context)

class ta6Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-6Eri", context=context)

class ta8Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-8Eri", context=context)

class ta9Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-9Eri", context=context)

class up1Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",up-1Eri", context=context)

class Theemin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",up-2Eri", context=context)

class Beemim(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",up-3Eri", context=context)

class up4Eri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",up-4Eri", context=context)

class chEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chEri", context=context)

class Sceptrum(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",53Eri", context=context)

class omeEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omeEri", context=context)

class piEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piEri", context=context)

class gEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gEri", context=context)

class fEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",fEri", context=context)

class yEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",yEri", context=context)

class eEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",eEri", context=context)

class sEri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",sEri", context=context)

class Dalim(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alFor", context=context)

class beFor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beFor", context=context)

class deFor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deFor", context=context)

class kaFor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaFor", context=context)

class la1For(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",la-1For", context=context)

class muFor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muFor", context=context)

class nuFor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuFor", context=context)

class taFor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taFor", context=context)

class Castor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alGem", context=context)

class Punarvasu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beGem", context=context)

class Almeisan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaGem", context=context)

class Wasat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deGem", context=context)

class Mebsuta(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epGem", context=context)

class Mekbuda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeGem", context=context)

class PropusetaGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etGem", context=context)

class Nageba(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thGem", context=context)

class PropusiotGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioGem", context=context)

class AlKrikab(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaGem", context=context)

class Alkibash(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laGem", context=context)

class Tejat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muGem", context=context)

class nuGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuGem", context=context)

class Alzirr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiGem", context=context)

class Jishui(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiGem", context=context)

class piGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piGem", context=context)

class rhGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhGem", context=context)

class siGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siGem", context=context)

class taGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taGem", context=context)

class upGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upGem", context=context)

class phGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phGem", context=context)

class chGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chGem", context=context)

class omeGem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omeGem", context=context)

class Alnair(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alGru", context=context)

class Tiaki(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beGru", context=context)

class RasAlkurki(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaGru", context=context)

class de1Gru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",de-1Gru", context=context)

class de2Gru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",de-2Gru", context=context)

class epGru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epGru", context=context)

class thGru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thGru", context=context)

class zeGru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeGru", context=context)

class ioGru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioGru", context=context)

class laGru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laGru", context=context)

class nuGru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuGru", context=context)

class omiGru(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiGru", context=context)

class Kornephoros(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beHer", context=context)

class Rasalgethi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alHer", context=context)

class al1Her(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",al-1Her", context=context)

class Rutilicus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeHer", context=context)

class gaHer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaHer", context=context)

class Sarin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deHer", context=context)

class KajamepsHer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epHer", context=context)

class Sofian(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etHer", context=context)

class RukbalgethiGenubi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thHer", context=context)

class AlJathiyah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioHer", context=context)

class Marsic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaHer", context=context)

class Maasym(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laHer", context=context)

class Melkarth(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muHer", context=context)

class xiHer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiHer", context=context)

class omiHer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiHer", context=context)

class Fudail(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piHer", context=context)

class siHer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siHer", context=context)

class RukbalgethiShemali(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taHer", context=context)

class phHer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phHer", context=context)

class chHer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chHer", context=context)

class Cujam(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omeHer", context=context)

class rhHer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhHer", context=context)

class Ogma(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",HD149026", context=context)

class Apex(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",Apex", context=context)

class alHor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alHor", context=context)

class zeHor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeHor", context=context)

class laHor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laHor", context=context)

class muHor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muHor", context=context)

class ioHor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioHor", context=context)

class etHor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etHor", context=context)

class beHor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beHor", context=context)

class CorHydrae(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alHya", context=context)

class beHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beHya", context=context)

class DhanabalShuja(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaHya", context=context)

class Mautinah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deHya", context=context)

class Ashlesha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epHya", context=context)

class Hydrobius(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeHya", context=context)

class etHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etHya", context=context)

class thHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thHya", context=context)

class ioHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioHya", context=context)

class kaHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaHya", context=context)

class laHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laHya", context=context)

class muHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muHya", context=context)

class Pleura(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuHya", context=context)

class xiHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiHya", context=context)

class omiHya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiHya", context=context)

class Sataghni(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piHya", context=context)

class Minchir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siHya", context=context)

class Ukdahprima(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-1Hya", context=context)

class Ukdahsecunda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-2Hya", context=context)

class Zhang(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",up-1Hya", context=context)

class up2Hya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",up-2Hya", context=context)

class ch1Hya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ch-1Hya", context=context)

class alHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alHyi", context=context)

class beHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beHyi", context=context)

class gaHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaHyi", context=context)

class deHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deHyi", context=context)

class epHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epHyi", context=context)

class et2Hyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",et-2Hyi", context=context)

class thHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thHyi", context=context)

class ioHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioHyi", context=context)

class kaHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaHyi", context=context)

class laHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laHyi", context=context)

class muHyi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muHyi", context=context)

class alInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alInd", context=context)

class beInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beInd", context=context)

class gaInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaInd", context=context)

class deInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deInd", context=context)

class epInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epInd", context=context)

class etInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etInd", context=context)

class thInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thInd", context=context)

class omiInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiInd", context=context)

class rhInd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhInd", context=context)

class alLac(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alLac", context=context)

class beLac(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beLac", context=context)

class Lac1(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",1Lac", context=context)

class Lac2(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",2Lac", context=context)

class Lac4(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",4Lac", context=context)

class Lac5(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",5Lac", context=context)

class Lac6(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",6Lac", context=context)

class Uttaraphalguni(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beLeo", context=context)

class Algieba(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-1Leo", context=context)

class Purvaphalguni(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deLeo", context=context)

class RasElasedAustralis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epLeo", context=context)

class Adhafera(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeLeo", context=context)

class AlJabhah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etLeo", context=context)

class TszeTseang(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioLeo", context=context)

class AlMinliaralAsad(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaLeo", context=context)

class Alterf(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laLeo", context=context)

class Rasalas(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muLeo", context=context)

class xiLeo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiLeo", context=context)

class Subra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiLeo", context=context)

class Shishimai(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siLeo", context=context)

class Chort(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thLeo", context=context)

class piLeo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piLeo", context=context)

class Shir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhLeo", context=context)

class taLeo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taLeo", context=context)

class upLeo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upLeo", context=context)

class phLeo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phLeo", context=context)

class chLeo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chLeo", context=context)

class psLeo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psLeo", context=context)

class Arneb(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alLep", context=context)

class Nihal(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beLep", context=context)

class gaLep(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaLep", context=context)

class deLep(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deLep", context=context)

class Sasin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epLep", context=context)

class zeLep(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeLep", context=context)

class etLep(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etLep", context=context)

class laLep(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laLep", context=context)

class muLep(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muLep", context=context)

class al1Lib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",al-1Lib", context=context)

class ZubenElgenubi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",al-2Lib", context=context)

class ZubenEschamali(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beLib", context=context)

class ZubenElakrab(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaLib", context=context)

class ZubenElakribi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deLib", context=context)

class ze1Lib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ze-1Lib", context=context)

class io1Lib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",io-1Lib", context=context)

class kaLib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaLib", context=context)

class laLib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laLib", context=context)

class ZubenHakrabi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuLib", context=context)

class xi2Lib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xi-2Lib", context=context)

class Brachium(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siLib", context=context)

class taLib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taLib", context=context)

class upLib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upLib", context=context)

class beLMi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beLMi", context=context)

class Praecipua(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",46LMi", context=context)

class LMi21(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",21LMi", context=context)

class Men(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alLup", context=context)

class Kekouan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beLup", context=context)

class Thusia(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaLup", context=context)

class Hilasmus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deLup", context=context)

class epLup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epLup", context=context)

class etLup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etLup", context=context)

class zeLup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeLup", context=context)

class thLup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thLup", context=context)

class ka1Lup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ka-1Lup", context=context)

class ka2Lup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ka-2Lup", context=context)

class ph1Lup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ph-1Lup", context=context)

class ph2Lup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ph-2Lup", context=context)

class ta1Lup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-1Lup", context=context)

class chLup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chLup", context=context)

class AlFahd(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alLyn", context=context)

class Mabsuthat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",31Lyn", context=context)

class Mabsuthat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaLyn", context=context)

class Maculata(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",38Lyn", context=context)

class Lyn21(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",21Lyn", context=context)

class Lyn15(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",15Lyn", context=context)

class Lyn2(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",2Lyn", context=context)

class Abhijit(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alLyr", context=context)

class Sheliak(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beLyr", context=context)

class Sulafat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaLyr", context=context)

class Aladfar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etLyr", context=context)

class thLyr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thLyr", context=context)

class ioLyr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioLyr", context=context)

class kaLyr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaLyr", context=context)

class AlAthfar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muLyr", context=context)

class ze2Lyr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ze-2Lyr", context=context)

class de2Lyr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",de-2Lyr", context=context)

class ep2Lyr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ep-2Lyr", context=context)

class alMen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alMen", context=context)

class beMen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beMen", context=context)

class gaMen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaMen", context=context)

class deMen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deMen", context=context)

class etMen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etMen", context=context)

class zeMen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeMen", context=context)

class muMen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muMen", context=context)

class xiMen(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiMen", context=context)

class alMic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alMic", context=context)

class gaMic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaMic", context=context)

class epMic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epMic", context=context)

class zeMic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeMic", context=context)

class th1Mic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",th-1Mic", context=context)

class ioMic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioMic", context=context)

class alMon(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alMon", context=context)

class beMon(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beMon", context=context)

class gaMon(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaMon", context=context)

class deMon(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deMon", context=context)

class epMon(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epMon", context=context)

class zeMon(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeMon", context=context)

class Mon18(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",18Mon", context=context)

class Mon13(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",13Mon", context=context)

class alMus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alMus", context=context)

class beMus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beMus", context=context)

class gaMus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaMus", context=context)

class deMus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deMus", context=context)

class epMus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epMus", context=context)

class etMus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etMus", context=context)

class laMus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laMus", context=context)

class muMus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muMus", context=context)

class ga2Nor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-2Nor", context=context)

class deNor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deNor", context=context)

class epNor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epNor", context=context)

class etNor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etNor", context=context)

class kaNor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaNor", context=context)

class alOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alOct", context=context)

class beOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beOct", context=context)

class ga1Oct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-1Oct", context=context)

class deOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deOct", context=context)

class etOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etOct", context=context)

class epOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epOct", context=context)

class thOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thOct", context=context)

class zeOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeOct", context=context)

class ioOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioOct", context=context)

class kaOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaOct", context=context)

class nuOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuOct", context=context)

class rhOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhOct", context=context)

class PolarisAustralis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siOct", context=context)

class taOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taOct", context=context)

class upOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upOct", context=context)

class chOct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chOct", context=context)

class Rasalhague(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alOph", context=context)

class KelbAlrai(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beOph", context=context)

class AlDurajah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaOph", context=context)

class YedPrior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deOph", context=context)

class YedPosterior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epOph", context=context)

class Han(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeOph", context=context)

class Sabik(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etOph", context=context)

class Imad(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thOph", context=context)

class ioOph(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioOph", context=context)

class Helkath(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaOph", context=context)

class Marfik(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laOph", context=context)

class Sinistra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuOph", context=context)

class xiOph(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiOph", context=context)

class siOph(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siOph", context=context)

class BarnardsStar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",V2500 Oph", context=context)

class Oph44(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",44Oph", context=context)

class Oph45(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",45Oph", context=context)

class Ardra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alOri", context=context)

class Durga(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaOri", context=context)

class Kumara(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deOri", context=context)

class Ganesha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epOri", context=context)

class Iyappa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeOri", context=context)

class Ensis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etOri", context=context)

class Trapezium(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",th-1Ori", context=context)

class NairalSaif(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioOri", context=context)

class Saiph(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaOri", context=context)

class Mrigashirsha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laOri", context=context)

class muOri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muOri", context=context)

class nuOri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuOri", context=context)

class xiOri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiOri", context=context)

class omi1Ori(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omi-1Ori", context=context)

class pi1Ori(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-1Ori", context=context)

class pi2Ori(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-2Ori", context=context)

class Tabit(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-3Ori", context=context)

class Tabit(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-4Ori", context=context)

class pi5Ori(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-5Ori", context=context)

class pi6Ori(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-6Ori", context=context)

class taOri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taOri", context=context)

class Thabit(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upOri", context=context)

class ph1Ori(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ph-1Ori", context=context)

class ch2Ori(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ch-2Ori", context=context)

class Ori71(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",71Ori", context=context)

class Messier42(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",M42", context=context)

class Peacock(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alPav", context=context)

class bePav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",bePav", context=context)

class gaPav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPav", context=context)

class dePav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",dePav", context=context)

class epPav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epPav", context=context)

class zePav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zePav", context=context)

class etPav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etPav", context=context)

class laPav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laPav", context=context)

class xiPav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiPav", context=context)

class omiPav(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiPav", context=context)

class Ankaa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alPhe", context=context)

class bePhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",bePhe", context=context)

class gaPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPhe", context=context)

class dePhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",dePhe", context=context)

class epPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epPhe", context=context)

class etPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etPhe", context=context)

class Wurren(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zePhe", context=context)

class thPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thPhe", context=context)

class ioPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioPhe", context=context)

class la1Phe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",la-1Phe", context=context)

class muPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muPhe", context=context)

class piPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piPhe", context=context)

class upPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upPhe", context=context)

class phPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phPhe", context=context)

class psPhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psPhe", context=context)

class omePhe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omePhe", context=context)

class Purvabhadra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alPeg", context=context)

class Scheat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",bePeg", context=context)

class Uttarabhadra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPeg", context=context)

class Enif(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epPeg", context=context)

class Homam(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zePeg", context=context)

class Matar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etPeg", context=context)

class Baham(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thPeg", context=context)

class ioPeg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioPeg", context=context)

class Jih(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaPeg", context=context)

class Sadalbari(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laPeg", context=context)

class muPeg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muPeg", context=context)

class xiPeg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiPeg", context=context)

class piPeg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piPeg", context=context)

class pi1Peg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-1Peg", context=context)

class pi2Peg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pi-2Peg", context=context)

class Salm(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taPeg", context=context)

class Alkarab(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upPeg", context=context)

class phPeg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phPeg", context=context)

class chPeg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chPeg", context=context)

class psPeg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psPeg", context=context)

class Peg1(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",1Peg", context=context)

class Peg9(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",9Peg", context=context)

class Helvetios(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",51Peg", context=context)

class Mirphak(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alPer", context=context)

class gaPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPer", context=context)

class dePer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",dePer", context=context)

class epPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epPer", context=context)

class zePer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zePer", context=context)

class Miram(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etPer", context=context)

class thPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thPer", context=context)

class ioPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioPer", context=context)

class Misam(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaPer", context=context)

class laPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laPer", context=context)

class muPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muPer", context=context)

class nuPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuPer", context=context)

class Menkib(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiPer", context=context)

class Atiks(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiPer", context=context)

class GorgonaSecunda(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piPer", context=context)

class GorgonaTertia(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhPer", context=context)

class siPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siPer", context=context)

class taPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taPer", context=context)

class phPer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phPer", context=context)

class GorgonaQuatra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omePer", context=context)

class Per16(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",16Per", context=context)

class alPic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alPic", context=context)

class bePic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",bePic", context=context)

class gaPic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPic", context=context)

class dePic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",dePic", context=context)

class zePic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zePic", context=context)

class et2Pic(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",et-2Pic", context=context)

class Fomalhaut(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alPsA", context=context)

class TienKang(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",bePsA", context=context)

class gaPsA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPsA", context=context)

class Aboras(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",dePsA", context=context)

class epPsA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epPsA", context=context)

class thPsA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thPsA", context=context)

class ioPsA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioPsA", context=context)

class laPsA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laPsA", context=context)

class muPsA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muPsA", context=context)

class piPsA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piPsA", context=context)

class AlRescha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alPsc", context=context)

class Samakah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",bePsc", context=context)

class Simmah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPsc", context=context)

class Linteum(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",dePsc", context=context)

class Kaht(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epPsc", context=context)

class Revati(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zePscA", context=context)

class Revati(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zePsc", context=context)

class AlPherg(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etPsc", context=context)

class thPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thPsc", context=context)

class ioPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioPsc", context=context)

class kaPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaPsc", context=context)

class laPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laPsc", context=context)

class nuPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuPsc", context=context)

class xiPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiPsc", context=context)

class Torcular(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiPsc", context=context)

class piPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piPsc", context=context)

class Anunitum(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taPsc", context=context)

class upPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upPsc", context=context)

class phPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phPsc", context=context)

class chPsc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chPsc", context=context)

class Vernalis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omePsc", context=context)

class Psc7(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",7Psc", context=context)

class Psc19(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",19Psc", context=context)

class SuhailHadar(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zePup", context=context)

class Kaimana(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuPup", context=context)

class Azmidiske(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiPup", context=context)

class Ahadi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piPup", context=context)

class Tureis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhPup", context=context)

class siPup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siPup", context=context)

class Anazitisi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taPup", context=context)

class pPup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pPup", context=context)

class P_Pup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",P_Pup", context=context)

class k01Pup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",k01Pup", context=context)

class J_Pup(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",J_Pup", context=context)

class alPyx(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alPyx", context=context)

class bePyx(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",bePyx", context=context)

class gaPyx(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaPyx", context=context)

class epPyx(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epPyx", context=context)

class thPyx(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thPyx", context=context)

class alRet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alRet", context=context)

class beRet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beRet", context=context)

class gaRet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaRet", context=context)

class deRet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deRet", context=context)

class epRet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epRet", context=context)

class ze1Ret(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ze-1Ret", context=context)

class etRet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etRet", context=context)

class ioRet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioRet", context=context)

class kaRet(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaRet", context=context)

class piScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piScl", context=context)

class alScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alScl", context=context)

class beScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beScl", context=context)

class gaScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaScl", context=context)

class deScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deScl", context=context)

class epScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epScl", context=context)

class thScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thScl", context=context)

class ka2Scl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ka-2Scl", context=context)

class la2Scl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",la-2Scl", context=context)

class muScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muScl", context=context)

class siScl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siScl", context=context)

class Acrab(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",be-1Sco", context=context)

class be2Sco(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",be-2Sco", context=context)

class Anuradha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deSco", context=context)

class Larawag(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epSco", context=context)

class ze2Sco(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ze-2Sco", context=context)

class etSco(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etSco", context=context)

class Sargas(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thSco", context=context)

class io1Sco(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",io-1Sco", context=context)

class Girtab(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaSco", context=context)

class Mula(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laSco", context=context)

class Xamidimura(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",mu-1Sco", context=context)

class Jabbah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuSco", context=context)

class Grafias(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiSco", context=context)

class Fang(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piSco", context=context)

class Iklil(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhSco", context=context)

class Alniyat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siSco", context=context)

class taSco(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taSco", context=context)

class Lesath(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upSco", context=context)

class JabhatalAkrab(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ome-1Sco", context=context)

class JabhatalAkrab(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ome-2Sco", context=context)

class Fuyue(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",HR6630", context=context)

class Pipirima(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",mu-2Sco", context=context)

class alSct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alSct", context=context)

class beSct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beSct", context=context)

class gaSct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaSct", context=context)

class deSct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deSct", context=context)

class epSct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epSct", context=context)

class zeSct(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeSct", context=context)

class CorSerpentis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alSer", context=context)

class Zhou(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beSer", context=context)

class Ainalhai(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaSer", context=context)

class Chin(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deSer", context=context)

class NullaPambu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epSer", context=context)

class Tang(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etSer", context=context)

class Alya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",th-1Ser", context=context)

class kaSer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaSer", context=context)

class Leiolepidotus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muSer", context=context)

class nuSer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuSer", context=context)

class Nehushtan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiSer", context=context)

class omiSer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiSer", context=context)

class siSer(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siSer", context=context)

class ta1Ser(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ta-1Ser", context=context)

class alSex(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alSex", context=context)

class beSex(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beSex", context=context)

class gaSex(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaSex", context=context)

class deSex(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deSex", context=context)

class epSex(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epSex", context=context)

class Sham(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alSge", context=context)

class beSge(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beSge", context=context)

class gaSge(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaSge", context=context)

class deSge(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deSge", context=context)

class Rukbat(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alSgr", context=context)

class ArkabPrior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",be-1Sgr", context=context)

class ArkabPosterior(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",be-2Sgr", context=context)

class Alnasl(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaSgr", context=context)

class Nash(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-2Sgr", context=context)

class Purvashadha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deSgr", context=context)

class KausAustralis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epSgr", context=context)

class Ascella(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeSgr", context=context)

class IraFuroris(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etSgr", context=context)

class th1Sgr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",th-1Sgr", context=context)

class th2Sgr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",th-2Sgr", context=context)

class ioSgr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioSgr", context=context)

class ka1Sgr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ka-1Sgr", context=context)

class KausBorealis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laSgr", context=context)

class Polis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muSgr", context=context)

class AinalRami(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nu-1Sgr", context=context)

class xi2Sgr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xi-2Sgr", context=context)

class Manubrium(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiSgr", context=context)

class Albaldah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piSgr", context=context)

class Uttarashadha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siSgr", context=context)

class Hecatebolus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taSgr", context=context)

class Nanto(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phSgr", context=context)

class upSgr(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upSgr", context=context)

class Terebellium(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omeSgr", context=context)

class Sgr52(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",52Sgr", context=context)

class Sgr52(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",59Sgr", context=context)

class Sgr62(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",62Sgr", context=context)

class Alnath(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beTau", context=context)

class HyadumI(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaTau", context=context)

class SecundaHyadum(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deTau", context=context)

class HyadumII(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",de-1Tau", context=context)

class Tianguan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeTau", context=context)

class Krttika(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etTau", context=context)

class Phaeo(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",th-1Tau", context=context)

class Chamukuy(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",th-2Tau", context=context)

class ioTau(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioTau", context=context)

class Althaur(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laTau", context=context)

class Kattupothu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muTau", context=context)

class Furibundus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuTau", context=context)

class Ushakaron(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiTau", context=context)

class Atirsagne(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiTau", context=context)

class taTau(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taTau", context=context)

class rhTau(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhTau", context=context)

class ome1Tau(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ome-1Tau", context=context)

class Celeano(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",16Tau", context=context)

class Electra(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",17Tau", context=context)

class Taygeta(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",19Tau", context=context)

class Maia(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",20Tau", context=context)

class SteropeI(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",21Tau", context=context)

class SteropeII(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",22Tau", context=context)

class Merope(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",23Tau", context=context)

class Atlas(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",27Tau", context=context)

class Pleione(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",28Tau", context=context)

class alTel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alTel", context=context)

class epTel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epTel", context=context)

class zeTel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeTel", context=context)

class ioTel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioTel", context=context)

class laTel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laTel", context=context)

class nuTel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuTel", context=context)

class xiTel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiTel", context=context)

class Atria(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alTrA", context=context)

class beTrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beTrA", context=context)

class gaTrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaTrA", context=context)

class deTrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deTrA", context=context)

class epTrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epTrA", context=context)

class zeTrA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeTrA", context=context)

class Mothallah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alTri", context=context)

class beTri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beTri", context=context)

class gaTri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaTri", context=context)

class alTuc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alTuc", context=context)

class be2Tuc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",be-2Tuc", context=context)

class gaTuc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaTuc", context=context)

class epTuc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epTuc", context=context)

class zeTuc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeTuc", context=context)

class ioTuc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioTuc", context=context)

class la2Tuc(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",la-2Tuc", context=context)

class Kratu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alUMa", context=context)

class Pulaha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beUMa", context=context)

class Pulastya(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaUMa", context=context)

class Atri(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deUMa", context=context)

class Angiras(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epUMa", context=context)

class Vasishtha(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeUMa", context=context)

class Marichi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etUMa", context=context)

class AlHaud(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thUMa", context=context)

class TalithaBorealis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioUMa", context=context)

class Alkaphrah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaUMa", context=context)

class TaniaBorealis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laUMa", context=context)

class TaniaAustralis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muUMa", context=context)

class AlulaBorealis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuUMa", context=context)

class AlulaAustralis(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",xiUMa", context=context)

class Muscida(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiUMa", context=context)

class rhUMa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhUMa", context=context)

class upUMa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",upUMa", context=context)

class phUMa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phUMa", context=context)

class Taiyangshou(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chUMa", context=context)

class psUMa(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psUMa", context=context)

class UMa23(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",23UMa", context=context)

class UMa26(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",26UMa", context=context)

class Chalawan(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",47UMa", context=context)

class Saidak(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",80UMa", context=context)

class Alc0(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",80Uma", context=context)

class Intercrus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",HR3743", context=context)

class Kochab(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beUMi", context=context)

class Pherkad(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaUMi", context=context)

class Yildun(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deUMi", context=context)

class Urodelus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epUMi", context=context)

class Pharkadain(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeUMi", context=context)

class AnwaralFarkadain(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etUMi", context=context)

class laUMi(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laUMi", context=context)

class PherkadMinor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",11UMi", context=context)

class Regor(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-2Vel", context=context)

class KooShe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deVel", context=context)

class Markeb(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaVel", context=context)

class Suhail(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laVel", context=context)

class Alherem(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muVel", context=context)

class Xestus(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiVel", context=context)

class TseenKe(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phVel", context=context)

class psVel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psVel", context=context)

class dVel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",dVel", context=context)

class eVel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",eVel", context=context)

class pVel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",pVel", context=context)

class qVel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",qVel", context=context)

class tVel(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",tVel", context=context)

class Alaraph(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beVir", context=context)

class Porrima(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",gaVir", context=context)

class Mineluva(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deVir", context=context)

class Vindemiatrix(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epVir", context=context)

class Heze(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeVir", context=context)

class Zaniah(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",etVir", context=context)

class thVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",thVir", context=context)

class Syrma(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioVir", context=context)

class Kang(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",kaVir", context=context)

class Khambalia(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",laVir", context=context)

class RilAlauva(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",muVir", context=context)

class nuVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",nuVir", context=context)

class omiVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",omiVir", context=context)

class piVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",piVir", context=context)

class rhVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",rhVir", context=context)

class siVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",siVir", context=context)

class taVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",taVir", context=context)

class phVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",phVir", context=context)

class chVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",chVir", context=context)

class psVir(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",psVir", context=context)

class Vir109(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",109Vir", context=context)

class Lich(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",PSRB1257+12", context=context)

class Messier49(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",M49", context=context)

class alVol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alVol", context=context)

class beVol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",beVol", context=context)

class ga2Vol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ga-2Vol", context=context)

class deVol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",deVol", context=context)

class epVol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epVol", context=context)

class epVolA(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",epVolA", context=context)

class zeVol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",zeVol", context=context)

class ioVol(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ioVol", context=context)

class Anser(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",alVul", context=context)

class Vul2(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",2Vul", context=context)

class Vul12(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",12Vul", context=context)

class GCLiu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",GCLiu", context=context)

class GalPole(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",GPol", context=context)

class GalPoleIAU1958(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",GP1958", context=context)

class GalPlanePole(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",GPPlan", context=context)

class GalEqu(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",GEqu", context=context)

class InfraredDragon(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",IDrag", context=context)

class AA11_page_B73(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",AA11     ", context=context)

class GCRS00(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",GCRS00", context=context)

class Zero2000(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ZE200", context=context)

class ZerL2000(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",ZL200", context=context)

class SunPole(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",SunPole", context=context)

class Test(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",Test", context=context)

class NGC4194(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",NGC4194", context=context)

class Gliese710(FixedStar):

    def __init__(self, context = EphContext):
        super().__init__(swe_id = ",HD168442", context=context)

