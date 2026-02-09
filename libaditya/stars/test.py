class AlphaTauri(FixedStar): # ,alfTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTau", context=context, swe_string="Alpha Tauri,alfTau,ICRS,04,35,55.23907,+16,30,33.4885,63.45,-188.94,54.26,48.94,0.86, 16,  629")
        self._other_names = ['Aldebaran', 'Rohini']

Aldebaran = AlphaTauri
Rohini = AlphaTauri


class BetaPersei(FixedStar): # ,betPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPer", context=context, swe_string="Beta Persei,betPer,ICRS,03,08,10.13245,+40,57,20.3280,2.99,-1.66,4,36.27,2.12, 40,  673")
        self._other_names = ['Algol']

Algol = BetaPersei


class AlphaScorpii(FixedStar): # ,alfSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSco", context=context, swe_string="Alpha Scorpii,alfSco,ICRS,16,29,24.45970,-26,25,55.2094,-12.11,-23.3,-3.5,5.89,0.91,-26,11359")
        self._other_names = ['Antares']

Antares = AlphaScorpii


class AlphaLeonis(FixedStar): # ,alfLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLeo", context=context, swe_string="Alpha Leonis,alfLeo,ICRS,10,08,22.31099,+11,58,01.9516,-248.73,5.59,5.9,41.13,1.4, 12, 2149")
        self._other_names = ['Regulus']

Regulus = AlphaLeonis


class AlphaCanisMajoris(FixedStar): # ,alfCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCMa", context=context, swe_string="Alpha Canis Majoris,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.5,379.21,-1.46,-16, 1591")
        self._other_names = ['Sirius']

Sirius = AlphaCanisMajoris


class AlphaVirginis(FixedStar): # ,alfVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfVir", context=context, swe_string="Alpha Virginis,alfVir,ICRS,13,25,11.57937,-11,09,40.7501,-42.35,-30.67,1,13.06,0.97,-10, 3672")
        self._other_names = ['Spica']

Spica = AlphaVirginis


class Trappist1(FixedStar): # ,Trappist1

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Trappist1", context=context, swe_string="Trappist1,Trappist1,ICRS,23,06,29.36,-05,02,29.2,922.1,-471.9,-54,82.58,18.798,0,0")
        self._other_names = ['Trappist1']

Trappist1 = Trappist1


class AlphaHerculis(FixedStar): # ,alfHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfHer", context=context, swe_string="Alpha Herculis,alfHer,ICRS,17,14,38.8581,+14,23,25.226,-7.32,36.07,-32.09,9.07,3.06, 14, 3207")
        self._other_names = ['Rasalgethi']

Rasalgethi = AlphaHerculis


class GalacticCenter(FixedStar): # ,SgrA*

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SgrA*", context=context, swe_string="Galactic Center,SgrA*,ICRS,17,45,40.03599,-29,00,28.1699,-2.755718425, -5.547,  0.0,0.125,999.99,  0,    0")
        self._other_names = ['Galactic Center']

GalacticCenter = GalacticCenter


class GA(FixedStar): # ,GA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GA", context=context, swe_string="GA,GA,2000,16,15,02.836,-60,53,22.54,0.000,   0.00,  0.0,0.0000159,999.99,  0,    0")
        self._other_names = ['Great Attractor']

GreatAttractor = GA


class VirgoCluster(FixedStar): # ,VC

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",VC", context=context, swe_string="Virgo Cluster,VC,2000,12,30,47.3,12,20,13,0.000,   0.00,  0.0,0.0000,999.99,  0,    0")
        self._other_names = ['Virgo Cluster']

VirgoCluster = VirgoCluster


class MessierObject31(FixedStar): # ,M31

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M31", context=context, swe_string="Messier Object 31,M31,ICRS,00,42,44.330,+41,16,07.50,-35.99,-12.92,-301,0.00128205,3.44,  0,    0")
        self._other_names = ['Andromeda Galaxy']

AndromedaGalaxy = MessierObject31


class MessierObject44(FixedStar): # ,M44

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M44", context=context, swe_string="Messier Object 44,M44,2000,08,40,6.000,19,59,0.00,0.000,   0.00,  0.0,5.65,3.7,  0,    0")
        self._other_names = ['Praesepe Cluster']

PraesepeCluster = MessierObject44


class AlphaUrsaeMinoris(FixedStar): # ,alfUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfUMi", context=context, swe_string="Alpha Ursae Minoris,alfUMi,ICRS,02,31,49.09456,+89,15,50.7923,44.48,-11.85,-16.42,7.54,2.02, 88,    8")
        self._other_names = ['Polaris']

Polaris = AlphaUrsaeMinoris


class MessierObject87(FixedStar): # ,M87

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M87", context=context, swe_string="Messier Object 87,M87,ICRS,12,30,49.4233823,12,23,28.0438581,-8.029,10.734,1256,0.000061,8.63,  0,    0")
        self._other_names = []



class ShapleySupercluster(FixedStar): # ,ACO3558

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ACO3558", context=context, swe_string="Shapley Supercluster,ACO3558,ICRS,13,27,54.8,-31,29,32.0,0.0,0.0,13731,0.0000051,999.99,  0,    0")
        self._other_names = ['Shapley Supercluster']

ShapleySupercluster = ShapleySupercluster


class AlphaCygni(FixedStar): # ,alfCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCyg", context=context, swe_string="Alpha Cygni,alfCyg,ICRS,20,41,25.91514,+45,16,49.2197,2.01,1.85,-4.9,2.31,1.25, 44, 3541")
        self._other_names = ['Deneb']

Deneb = AlphaCygni


class AlphaCygni(FixedStar): # ,alfCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCyg", context=context, swe_string="Alpha Cygni,alfCyg,ICRS,20,41,25.91514,+45,16,49.2197,2.01,1.85,-4.9,2.31,1.25, 44, 3541")
        self._other_names = ['Deneb Adige']

DenebAdige = AlphaCygni


class BetaOrionis(FixedStar): # ,betOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betOri", context=context, swe_string="Beta Orionis,betOri,ICRS,05,14,32.27210,-08,12,05.8981,1.31,0.5,17.8,3.78,0.13,-08, 1063")
        self._other_names = ['Rigel']

Rigel = BetaOrionis


class OmicronCeti(FixedStar): # ,omiCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiCet", context=context, swe_string="Omicron Ceti,omiCet,ICRS,02,19,20.79210,-02,58,39.4956,9.33,-237.36,63.5,10.91,6.53,-03,  353")
        self._other_names = ['Mira']

Mira = OmicronCeti


class EpsilonTauri(FixedStar): # ,epsTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsTau", context=context, swe_string="Epsilon Tauri,epsTau,ICRS,04,28,36.99882,+19,10,49.5446,106.19,-37.84,38.5,22.24,3.53, 18,  640")
        self._other_names = ['Ain']

Ain = EpsilonTauri


class EpsilonCassiopeiae(FixedStar): # ,epsCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCas", context=context, swe_string="Epsilon Cassiopeiae,epsCas,ICRS,01,54,23.72567,+63,40,12.3628,32.09,-18.94,-8.3,7.92,3.37, 62,  320")
        self._other_names = ['Segin']

Segin = EpsilonCassiopeiae


class AlphaAndromedae(FixedStar): # ,alfAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAnd", context=context, swe_string="Alpha Andromedae,alfAnd,ICRS,00,08,23.25988,+29,05,25.5520,137.46,-163.44,-10.1,33.62,2.06, 28,    4")
        self._other_names = ['Alpheratz']

Alpheratz = AlphaAndromedae


class AlphaAndromedae(FixedStar): # ,alfAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAnd", context=context, swe_string="Alpha Andromedae,alfAnd,ICRS,00,08,23.25988,+29,05,25.5520,137.46,-163.44,-10.1,33.62,2.06, 28,    4")
        self._other_names = ['Sirrah']

Sirrah = AlphaAndromedae


class BetaAndromedae(FixedStar): # ,betAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAnd", context=context, swe_string="Beta Andromedae,betAnd,ICRS,01,09,43.92388,+35,37,14.0075,175.9,-112.2,0.06,16.52,2.05, 34,  198")
        self._other_names = ['Mirach']

Mirach = BetaAndromedae


class GammaAndromedae01(FixedStar): # ,gam01And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam01And", context=context, swe_string="Gamma Andromedae 01,gam01And,ICRS,02,03,53.9531,+42,19,47.009,43.08,-50.85,-11.7,9.19,2.1, 41,  395")
        self._other_names = ['Almaak']

Almaak = GammaAndromedae01


class GammaAndromedae01(FixedStar): # ,gam01And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam01And", context=context, swe_string="Gamma Andromedae 01,gam01And,ICRS,02,03,53.9531,+42,19,47.009,43.08,-50.85,-11.7,9.19,2.1, 41,  395")
        self._other_names = ['Almak']

Almak = GammaAndromedae01


class GammaAndromedae01(FixedStar): # ,gam01And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam01And", context=context, swe_string="Gamma Andromedae 01,gam01And,ICRS,02,03,53.9531,+42,19,47.009,43.08,-50.85,-11.7,9.19,2.1, 41,  395")
        self._other_names = ['Almac']

Almac = GammaAndromedae01


class GammaAndromedae01(FixedStar): # ,gam01And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam01And", context=context, swe_string="Gamma Andromedae 01,gam01And,ICRS,02,03,53.9531,+42,19,47.009,43.08,-50.85,-11.7,9.19,2.1, 41,  395")
        self._other_names = ['Almach']

Almach = GammaAndromedae01


class DeltaAndromedae(FixedStar): # ,delAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delAnd", context=context, swe_string="Delta Andromedae,delAnd,ICRS,00,39,19.67518,+30,51,39.6783,114.45,-84.02,-9.88,30.91,3.28, 30,   91")
        self._other_names = []

 = DeltaAndromedae


class EpsilonAndromedae(FixedStar): # ,epsAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsAnd", context=context, swe_string="Epsilon Andromedae,epsAnd,ICRS,00,38,33.34610,+29,18,42.3135,-229.04,-253.11,-84.43,19.91,4.38, 28,  103")
        self._other_names = []

 = EpsilonAndromedae


class ZetaAndromedae(FixedStar): # ,zetAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAnd", context=context, swe_string="Zeta Andromedae,zetAnd,ICRS,00,47,20.32547,+24,16,01.8408,-101.17,-81.77,-24.43,17.24,4.06, 23,  106")
        self._other_names = []

 = ZetaAndromedae


class IotaAndromedae(FixedStar): # ,iotAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAnd", context=context, swe_string="Iota Andromedae,iotAnd,ICRS,23,38,08.20130,+43,16,05.0649,27.64,-1.02,-0.5,6.53,4.29, 42, 4720")
        self._other_names = []

 = IotaAndromedae


class KappaAndromedae(FixedStar): # ,kapAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapAnd", context=context, swe_string="Kappa Andromedae,kapAnd,ICRS,23,40,24.50763,+44,20,02.1566,80.73,-18.7,-12.7,19.37,4.14, 43, 4522")
        self._other_names = []

 = KappaAndromedae


class LambdaAndromedae(FixedStar): # ,lamAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamAnd", context=context, swe_string="Lambda Andromedae,lamAnd,ICRS,23,37,33.84261,+46,27,29.3380,159.31,-422.38,6.84,37.87,3.82, 45, 4283")
        self._other_names = []

 = LambdaAndromedae


class MessierObjectu.And(FixedStar): # ,mu.And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.And", context=context, swe_string="Messier Object u.And,mu.And,ICRS,00,56,45.21211,+38,29,57.6380,153.48,36.49,7.2,25.14,3.87, 37,  175")
        self._other_names = []

 = MessierObjectu.And


class NuAndromedae(FixedStar): # ,nu.And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.And", context=context, swe_string="Nu Andromedae,nu.And,ICRS,00,49,48.84737,+41,04,44.0764,22.77,-18.35,-23.9,5.28,4.53, 40,  171")
        self._other_names = []

 = NuAndromedae


class XiAndromedae(FixedStar): # ,ksiAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiAnd", context=context, swe_string="Xi Andromedae,ksiAnd,ICRS,01,22,20.41924,+45,31,43.6003,31.45,8.83,-12.87,15.21,4.868, 44,  287")
        self._other_names = ['Adhil']

Adhil = XiAndromedae


class OmicronAndromedae(FixedStar): # ,omiAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiAnd", context=context, swe_string="Omicron Andromedae,omiAnd,ICRS,23,01,55.26459,+42,19,33.5334,22.99,0.88,-14,4.75,3.62, 41, 4664")
        self._other_names = []

 = OmicronAndromedae


class PiAndromedae(FixedStar): # ,pi.And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.And", context=context, swe_string="Pi Andromedae,pi.And,ICRS,00,36,52.84926,+33,43,09.6384,14.75,-3.51,8.2,5.45,4.36, 32,  101")
        self._other_names = []

 = PiAndromedae


class RhoAndromedae(FixedStar): # ,rhoAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoAnd", context=context, swe_string="Rho Andromedae,rhoAnd,ICRS,00,21,07.26951,+37,58,06.9804,58.93,-38.56,10.4,20.6,5.18, 37,   45")
        self._other_names = []

 = RhoAndromedae


class SigmaAndromedae(FixedStar): # ,sigAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigAnd", context=context, swe_string="Sigma Andromedae,sigAnd,ICRS,00,18,19.65745,+36,47,06.8107,-65.67,-42,-8.2,24.2,4.52, 35,   44")
        self._other_names = []

 = SigmaAndromedae


class UpsilonAndromedae(FixedStar): # ,upsAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsAnd", context=context, swe_string="Upsilon Andromedae,upsAnd,ICRS,01,36,47.84216,+41,24,19.6443,-173.33,-381.8,-28.59,74.12,4.1, 40,  332")
        self._other_names = ['Adhab']

Adhab = UpsilonAndromedae


class UpsilonAndromedae(FixedStar): # ,upsAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsAnd", context=context, swe_string="Upsilon Andromedae,upsAnd,ICRS,01,36,47.84216,+41,24,19.6443,-173.33,-381.8,-28.59,74.12,4.1, 40,  332")
        self._other_names = ['Titawin']

Titawin = UpsilonAndromedae


class PsiAndromedae(FixedStar): # ,psiAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiAnd", context=context, swe_string="Psi Andromedae,psiAnd,ICRS,23,46,02.04663,+46,25,12.9788,9.07,-7.83,-23.71,3.25,4.966, 45, 4321")
        self._other_names = []

 = PsiAndromedae


class OmegaAndromedae(FixedStar): # ,omeAnd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeAnd", context=context, swe_string="Omega Andromedae,omeAnd,ICRS,01,27,39.38177,+45,24,24.0727,356.99,-109.4,12.4,34.94,4.83, 44,  307")
        self._other_names = []

 = OmegaAndromedae


class Andromedae14(FixedStar): # ,14And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",14And", context=context, swe_string="Andromedae14,14And,ICRS,23,31,17.41346,+39,14,10.3092,286.72,-84.22,-59.99,12.63,5.22, 0,0")
        self._other_names = ['Veritate']

Veritate = Andromedae14


class Andromedae51(FixedStar): # ,51And

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",51And", context=context, swe_string="Andromedae51,51And,ICRS,01,37,59.55699,+48,37,41.5695,61.95,-112.15,16.21,18.41,3.57,0,0")
        self._other_names = ['Nembus']

Nembus = Andromedae51


class MessierObject31(FixedStar): # ,M31

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M31", context=context, swe_string="Messier Object 31,M31,ICRS,00,42,44.330,+41,16,07.50,-35.99,-12.92,-301,0.00128205,3.44,  0,    0")
        self._other_names = ['Andromeda Galaxy']

AndromedaGalaxy = MessierObject31


class AlphaAntilae(FixedStar): # ,alfAnt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAnt", context=context, swe_string="Alpha Antilae,alfAnt,ICRS,10,27,09.10037,-31,04,03.9961,-81.61,10.53,12.2,8.91,4.25,-30, 8465")
        self._other_names = []

 = AlphaAntilae


class EpsilonAntilae(FixedStar): # ,epsAnt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsAnt", context=context, swe_string="Epsilon Antilae,epsAnt,ICRS,09,29,14.71968,-35,57,04.8074,-24.69,5.04,22.2,4.59,4.51,-35, 5724")
        self._other_names = []

 = EpsilonAntilae


class ThetaAntilae(FixedStar): # ,tetAnt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAnt", context=context, swe_string="Theta Antilae,tetAnt,ICRS,09,44,12.09512,-27,46,10.1011,-53.23,37.24,24,9.61,4.79,-27, 6881")
        self._other_names = []

 = ThetaAntilae


class IotaAntilae(FixedStar): # ,iotAnt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAnt", context=context, swe_string="Iota Antilae,iotAnt,ICRS,10,56,43.05206,-37,08,15.9552,76.14,-124.43,-0.2,17.16,4.6,-36, 6808")
        self._other_names = []

 = IotaAntilae


class AlphaApodis(FixedStar): # ,alfAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAps", context=context, swe_string="Alpha Apodis,alfAps,ICRS,14,47,51.71203,-79,02,41.1032,-4.58,-15.88,-0.1,7.3,3.798,-78,  893")
        self._other_names = []

 = AlphaApodis


class BetaApodis(FixedStar): # ,betAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAps", context=context, swe_string="Beta Apodis,betAps,ICRS,16,43,04.65651,-77,31,02.7629,-282.7,-354.81,-30.3,20.78,4.24,0,0")
        self._other_names = []

 = BetaApodis


class GammaApodis(FixedStar): # ,gamAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamAps", context=context, swe_string="Gamma Apodis,gamAps,ICRS,16,33,27.08379,-78,53,49.7372,-125.51,-78.25,5.4,20.87,3.854,-78, 1103")
        self._other_names = []

 = GammaApodis


class DeltaApodis01(FixedStar): # ,del01Aps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del01Aps", context=context, swe_string="Delta Apodis 01,del01Aps,ICRS,16,20,20.80462,-78,41,44.6889,-10.23,-37.43,-12,4.28,4.68,-78, 1092")
        self._other_names = []

 = DeltaApodis01


class ThetaApodis(FixedStar): # ,tetAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAps", context=context, swe_string="Theta Apodis,tetAps,ICRS,14,05,19.87784,-76,47,48.3204,-87.54,-32.54,10.2,8.84,5.5,-76,  799")
        self._other_names = []

 = ThetaApodis


class IotaApodis(FixedStar): # ,iotAps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAps", context=context, swe_string="Iota Apodis,iotAps,ICRS,17,22,05.87559,-70,07,23.5400,-1.94,-10.99,-4.3,2.47,5.41,-69, 2719")
        self._other_names = []

 = IotaApodis


class KappaApodis01(FixedStar): # ,kap01Aps

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kap01Aps", context=context, swe_string="Kappa Apodis 01,kap01Aps,ICRS,15,31,30.82178,-73,23,22.5291,0.56,-18.4,62,2.63,5.49,-72, 1802")
        self._other_names = []

 = KappaApodis01


class AlphaAquilae(FixedStar): # ,alfAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAql", context=context, swe_string="Alpha Aquilae,alfAql,ICRS,19,50,46.99855,+08,52,05.9563,536.23,385.29,-26.6,194.95,0.76, 08, 4236")
        self._other_names = ['Altair']

Altair = AlphaAquilae


class AlphaAquilae(FixedStar): # ,alfAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAql", context=context, swe_string="Alpha Aquilae,alfAql,ICRS,19,50,46.99855,+08,52,05.9563,536.23,385.29,-26.6,194.95,0.76, 08, 4236")
        self._other_names = ['Shravana']

Shravana = AlphaAquilae


class BetaAquilae(FixedStar): # ,betAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAql", context=context, swe_string="Beta Aquilae,betAql,ICRS,19,55,18.79256,+06,24,24.3425,45.27,-481.91,-40.07,73,3.71, 06, 4357")
        self._other_names = ['Alshain']

Alshain = BetaAquilae


class GammaAquilae(FixedStar): # ,gamAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamAql", context=context, swe_string="Gamma Aquilae,gamAql,ICRS,19,46,15.58029,+10,36,47.7408,16.99,-2.98,-2.79,8.26,2.72, 10, 4043")
        self._other_names = ['Tarazed']

Tarazed = GammaAquilae


class DeltaAquilae(FixedStar): # ,delAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delAql", context=context, swe_string="Delta Aquilae,delAql,ICRS,19,25,29.90139,+03,06,53.2061,254.54,82.51,-34,64.41,3.36, 02, 3879")
        self._other_names = ['Delta Aquilae']

DeltaAquilae = DeltaAquilae


class DeltaAquilae(FixedStar): # ,delAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delAql", context=context, swe_string="Delta Aquilae,delAql,ICRS,19,25,29.90139,+03,06,53.2061,254.54,82.51,-34,64.41,3.36, 02, 3879")
        self._other_names = ['Al Mizan']

AlMizan = DeltaAquilae


class EpsilonAquilae(FixedStar): # ,epsAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsAql", context=context, swe_string="Epsilon Aquilae,epsAql,ICRS,18,59,37.35872,+15,04,05.8871,-50.75,-72.36,-45.9,21.05,4.02, 14, 3736")
        self._other_names = ['Deneb el Okab Borealis']

DenebelOkabBorealis = EpsilonAquilae


class ZetaAquilae(FixedStar): # ,zetAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAql", context=context, swe_string="Zeta Aquilae,zetAql,ICRS,19,05,24.60802,+13,51,48.5182,-7.25,-95.56,-25,39.28,2.99, 13, 3899")
        self._other_names = ['Deneb el Okab Australis']

DenebelOkabAustralis = ZetaAquilae


class ZetaAquilae(FixedStar): # ,zetAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAql", context=context, swe_string="Zeta Aquilae,zetAql,ICRS,19,05,24.60802,+13,51,48.5182,-7.25,-95.56,-25,39.28,2.99, 13, 3899")
        self._other_names = ['Dheneb']

Dheneb = ZetaAquilae


class EtaAquilae(FixedStar): # ,etaAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaAql", context=context, swe_string="Eta Aquilae,etaAql,ICRS,19,52,28.36775,+01,00,20.3696,6.91,-8.21,-25.1,2.36,3.8, 00, 4337")
        self._other_names = ['Bazak']

Bazak = EtaAquilae


class ThetaAquilae(FixedStar): # ,tetAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAql", context=context, swe_string="Theta Aquilae,tetAql,ICRS,20,11,18.266,-00,49,17.31,35.26,5.71,-28.02,11.39,3.22,-01, 3911")
        self._other_names = ['Tseen Foo']

TseenFoo = ThetaAquilae


class IotaAquilae(FixedStar): # ,iotAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAql", context=context, swe_string="Iota Aquilae,iotAql,ICRS,19,36,43.27606,-01,17,11.7611,-0.87,-20.39,-21.4,8.34,4.36,-01, 3782")
        self._other_names = ['Al Thalimaim Posterior']

AlThalimaimPosterior = IotaAquilae


class KappaAquilae(FixedStar): # ,kapAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapAql", context=context, swe_string="Kappa Aquilae,kapAql,ICRS,19,36,53.44952,-07,01,38.9176,1.63,-2.65,-19.4,1.94,4.96,-07, 5006")
        self._other_names = []

 = KappaAquilae


class LambdaAquilae(FixedStar): # ,lamAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamAql", context=context, swe_string="Lambda Aquilae,lamAql,ICRS,19,06,14.93898,-04,52,57.2007,-18.69,-91.02,-8.8,26.37,3.43,-05, 4876")
        self._other_names = ['Al Thalimaim Anterior']

AlThalimaimAnterior = LambdaAquilae


class MessierObjectu.Aql(FixedStar): # ,mu.Aql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Aql", context=context, swe_string="Messier Object u.Aql,mu.Aql,ICRS,19,34,05.35353,+07,22,44.1796,213.73,-156.55,-24.81,30.31,4.45, 07, 4132")
        self._other_names = []

 = MessierObjectu.Aql


class RhoAquilae(FixedStar): # ,rhoAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoAql", context=context, swe_string="Rho Aquilae,rhoAql,ICRS,20,14,16.61886,+15,11,51.3923,55.03,58.14,-23,21.75,4.946, 14, 4227")
        self._other_names = []

 = RhoAquilae


class TauAquilae(FixedStar): # ,tauAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauAql", context=context, swe_string="Tau Aquilae,tauAql,ICRS,20,04,08.31550,+07,16,40.6683,14.74,12.1,-29.52,7.06,5.508, 06, 4416")
        self._other_names = []

 = TauAquilae


class OmegaAquilae01(FixedStar): # ,ome01Aql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome01Aql", context=context, swe_string="Omega Aquilae 01,ome01Aql,ICRS,19,17,48.99903,+11,35,43.5291,0.94,13.84,-14.3,7.86,5.283, 11, 3790")
        self._other_names = []

 = OmegaAquilae01


class XiAquilae(FixedStar): # ,ksiAql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiAql", context=context, swe_string="Xi Aquilae,ksiAql,ICRS,19,54,14.88184,+08,27,41.2299,101.91,-81.2,-41.07,17.77,4.707, 0,0")
        self._other_names = ['Libertas']

Libertas = XiAquilae


class Aquilae12(FixedStar): # ,12Aql

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",12Aql", context=context, swe_string="Aquilae12,12Aql,ICRS,19,01,40.82707,-05,44,20.8134,-24.41,-39.66,-43.92,22.66,4.02, 0, 0")
        self._other_names = ['Bered']

Bered = Aquilae12


class AlphaAquarii(FixedStar): # ,alfAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAqr", context=context, swe_string="Alpha Aquarii,alfAqr,ICRS,22,05,47.036,-00,19,11.46,18.25,-9.39,6.85,6.23,2.94,-01, 4246")
        self._other_names = ['Sadalmelek']

Sadalmelek = AlphaAquarii


class AlphaAquarii(FixedStar): # ,alfAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAqr", context=context, swe_string="Alpha Aquarii,alfAqr,ICRS,22,05,47.036,-00,19,11.46,18.25,-9.39,6.85,6.23,2.94,-01, 4246")
        self._other_names = ['Sadalmelik']

Sadalmelik = AlphaAquarii


class BetaAquarii(FixedStar): # ,betAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAqr", context=context, swe_string="Beta Aquarii,betAqr,ICRS,21,31,33.53171,-05,34,16.2320,18.77,-8.21,6.28,6.07,2.89,-06, 5770")
        self._other_names = ['Sadalsuud']

Sadalsuud = BetaAquarii


class GammaAquarii(FixedStar): # ,gamAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamAqr", context=context, swe_string="Gamma Aquarii,gamAqr,ICRS,22,21,39.37542,-01,23,14.4031,129.53,7.77,-15.7,19.92,3.834,-02, 5741")
        self._other_names = ['Sadalachbia']

Sadalachbia = GammaAquarii


class GammaAquarii(FixedStar): # ,gamAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamAqr", context=context, swe_string="Gamma Aquarii,gamAqr,ICRS,22,21,39.37542,-01,23,14.4031,129.53,7.77,-15.7,19.92,3.834,-02, 5741")
        self._other_names = ['Sadachbia']

Sadachbia = GammaAquarii


class DeltaAquarii(FixedStar): # ,delAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delAqr", context=context, swe_string="Delta Aquarii,delAqr,ICRS,22,54,39.01351,-15,49,14.9782,-42.6,-27.89,17.4,20.31,3.28,-16, 6173")
        self._other_names = ['Skat']

Skat = DeltaAquarii


class EpsilonAquarii(FixedStar): # ,epsAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsAqr", context=context, swe_string="Epsilon Aquarii,epsAqr,ICRS,20,47,40.55260,-09,29,44.7877,33.98,-34.77,-15.3,15.7,3.77,-10, 5506")
        self._other_names = ['Albali']

Albali = EpsilonAquarii


class EpsilonAquarii(FixedStar): # ,epsAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsAqr", context=context, swe_string="Epsilon Aquarii,epsAqr,ICRS,20,47,40.55260,-09,29,44.7877,33.98,-34.77,-15.3,15.7,3.77,-10, 5506")
        self._other_names = ['Altager']

Altager = EpsilonAquarii


class ZetaAquarii01(FixedStar): # ,zet01Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zet01Aqr", context=context, swe_string="Zeta Aquarii 01,zet01Aqr,ICRS,22,28,49.759,-00,01,13.96,191,37,28.9,0,4.49,0, 0")
        self._other_names = ['Sadaltager']

Sadaltager = ZetaAquarii01


class EtaAquarii(FixedStar): # ,etaAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaAqr", context=context, swe_string="Eta Aquarii,etaAqr,ICRS,22,35,21.38126,-00,07,02.9888,89.74,-55.81,-5.5,19.43,4.03,-00, 4384")
        self._other_names = ['Hydria']

Hydria = EtaAquarii


class EtaAquarii(FixedStar): # ,etaAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaAqr", context=context, swe_string="Eta Aquarii,etaAqr,ICRS,22,35,21.38126,-00,07,02.9888,89.74,-55.81,-5.5,19.43,4.03,-00, 4384")
        self._other_names = ['Deli']

Deli = EtaAquarii


class ThetaAquarii(FixedStar): # ,tetAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAqr", context=context, swe_string="Theta Aquarii,tetAqr,ICRS,22,16,50.03635,-07,46,59.8480,118.8,-22.18,-13.77,17.4,4.16,-08, 5845")
        self._other_names = ['Ancha']

Ancha = ThetaAquarii


class IotaAquarii(FixedStar): # ,iotAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAqr", context=context, swe_string="Iota Aquarii,iotAqr,ICRS,22,06,26.22742,-13,52,10.8615,36.89,-58.99,-9,18.62,4.27,-14, 6209")
        self._other_names = []

 = IotaAquarii


class KappaAquarii(FixedStar): # ,kapAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapAqr", context=context, swe_string="Kappa Aquarii,kapAqr,ICRS,22,37,45.38049,-04,13,40.9939,-69.23,-119.67,7.31,15.25,5.03,-04, 5716")
        self._other_names = ['Situla']

Situla = KappaAquarii


class LambdaAquarii(FixedStar): # ,lamAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamAqr", context=context, swe_string="Lambda Aquarii,lamAqr,ICRS,22,52,36.87441,-07,34,46.5542,17.02,33.03,-10.46,8.47,3.79,-08, 5968")
        self._other_names = ['Ekkhysis']

Ekkhysis = LambdaAquarii


class LambdaAquarii(FixedStar): # ,lamAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamAqr", context=context, swe_string="Lambda Aquarii,lamAqr,ICRS,22,52,36.87441,-07,34,46.5542,17.02,33.03,-10.46,8.47,3.79,-08, 5968")
        self._other_names = ['Hydor']

Hydor = LambdaAquarii


class LambdaAquarii(FixedStar): # ,lamAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamAqr", context=context, swe_string="Lambda Aquarii,lamAqr,ICRS,22,52,36.87441,-07,34,46.5542,17.02,33.03,-10.46,8.47,3.79,-08, 5968")
        self._other_names = ['Shatabhishaj']

Shatabhishaj = LambdaAquarii


class LambdaAquarii(FixedStar): # ,lamAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamAqr", context=context, swe_string="Lambda Aquarii,lamAqr,ICRS,22,52,36.87441,-07,34,46.5542,17.02,33.03,-10.46,8.47,3.79,-08, 5968")
        self._other_names = ['Shatabhishak']

Shatabhishak = LambdaAquarii


class MessierObjectu.Aqr(FixedStar): # ,mu.Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Aqr", context=context, swe_string="Messier Object u.Aqr,mu.Aqr,ICRS,20,52,39.23277,-08,58,59.9499,45.75,-33.59,-9.1,20.74,4.717,-09, 5598")
        self._other_names = []

 = MessierObjectu.Aqr


class NuAquarii(FixedStar): # ,nu.Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Aqr", context=context, swe_string="Nu Aquarii,nu.Aqr,ICRS,21,09,35.64888,-11,22,18.0851,94.12,-14.62,-11.23,20.47,4.52,-11, 5538")
        self._other_names = ['Albulaan']

Albulaan = NuAquarii


class PiAquarii(FixedStar): # ,pi.Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Aqr", context=context, swe_string="Pi Aquarii,pi.Aqr,ICRS,22,25,16.62285,+01,22,38.6346,17.83,2.41,-4.9,4.17,4.64, 00, 4872")
        self._other_names = ['Seat']

Seat = PiAquarii


class SigmaAquarii(FixedStar): # ,sigAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigAqr", context=context, swe_string="Sigma Aquarii,sigAqr,ICRS,22,30,38.81546,-10,40,40.6238,0.3,-26.87,11.7,11.26,4.81,-11, 5850")
        self._other_names = []

 = SigmaAquarii


class TauAquarii02(FixedStar): # ,tau02Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau02Aqr", context=context, swe_string="Tau Aquarii 02,tau02Aqr,ICRS,22,49,35.50157,-13,35,33.4767,-13.71,-39.03,1.1,10.27,3.98,-14, 6354")
        self._other_names = []

 = TauAquarii02


class PhiAquarii(FixedStar): # ,phiAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiAqr", context=context, swe_string="Phi Aquarii,phiAqr,ICRS,23,14,19.35787,-06,02,56.3998,43.12,-194.45,2.48,16.14,4.22,-06, 6170")
        self._other_names = []

 = PhiAquarii


class XiAquarii(FixedStar): # ,ksiAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiAqr", context=context, swe_string="Xi Aquarii,ksiAqr,ICRS,21,37,45.10931,-07,51,15.1299,114.2,-25.03,-18,18.26,4.69,-08, 5701")
        self._other_names = ['Bunda']

Bunda = XiAquarii


class UpsilonAquarii(FixedStar): # ,upsAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsAqr", context=context, swe_string="Upsilon Aquarii,upsAqr,ICRS,22,34,41.63641,-20,42,29.5779,220.78,-146.76,-3.7,44.09,5.2,-21, 6251")
        self._other_names = []

 = UpsilonAquarii


class PsiAquarii01(FixedStar): # ,psi01Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psi01Aqr", context=context, swe_string="Psi Aquarii 01,psi01Aqr,ICRS,23,15,53.49482,-09,05,15.8546,368.78,-17.16,-25.88,21.77,4.25,-09, 6156")
        self._other_names = []

 = PsiAquarii01


class PsiAquarii03(FixedStar): # ,psi03Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psi03Aqr", context=context, swe_string="Psi Aquarii 03,psi03Aqr,ICRS,23,18,57.67658,-09,36,38.7054,43.33,-8.3,-10,12.47,5.003,-10, 6094")
        self._other_names = []

 = PsiAquarii03


class OmegaAquarii02(FixedStar): # ,ome02Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome02Aqr", context=context, swe_string="Omega Aquarii 02,ome02Aqr,ICRS,23,42,43.34473,-14,32,41.6523,99.28,-66.32,3.2,21.96,4.484,-15, 6476")
        self._other_names = []

 = OmegaAquarii02


class Aquarii3(FixedStar): # ,3Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",3Aqr", context=context, swe_string="Aquarii3,3Aqr,ICRS,20,47,44.23898,-05,01,39.7220,1.68,-40.06,-22,5.57,4.44,0, 0")
        self._other_names = []

 = Aquarii3


class Aquarii88(FixedStar): # ,88Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",88Aqr", context=context, swe_string="Aquarii88,88Aqr,ICRS,23,09,26.79681,-21,10,20.6812,55.4,30.49,21.3,12.05,3.64,0, 0")
        self._other_names = []

 = Aquarii88


class Aquarii98(FixedStar): # ,98Aqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",98Aqr", context=context, swe_string="Aquarii98,98Aqr,ICRS,23,22,58.22606,-20,06,02.0963,-121.28,-97.59,-6.1,19.96,3.98,0, 0")
        self._other_names = []

 = Aquarii98


class Trappist01(FixedStar): # ,Trappist01

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Trappist01", context=context, swe_string="Trappist01,Trappist01,ICRS,23,06,29.36,-05,02,29.2,922.1,-471.9,-54,82.58,18.798,0,0")
        self._other_names = ['Trappist-1']

Trappist-1 = Trappist01


class AlphaArae(FixedStar): # ,alfAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAra", context=context, swe_string="Alpha Arae,alfAra,ICRS,17,31,50.49153,-49,52,34.1220,-33.27,-67.22,0,12.2,2.95,-49,11511")
        self._other_names = ['Ara']

Ara = AlphaArae


class BetaArae(FixedStar): # ,betAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAra", context=context, swe_string="Beta Arae,betAra,ICRS,17,25,17.98835,-55,31,47.5868,-8.51,-25.24,-0.3,5.05,2.85,-55, 8100")
        self._other_names = []

 = BetaArae


class GammaArae(FixedStar): # ,gamAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamAra", context=context, swe_string="Gamma Arae,gamAra,ICRS,17,25,23.65931,-56,22,39.8148,-0.44,-15.77,-3,2.93,3.34,0,0")
        self._other_names = []

 = GammaArae


class DeltaArae(FixedStar): # ,delAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delAra", context=context, swe_string="Delta Arae,delAra,ICRS,17,31,05.91272,-60,41,01.8522,-54.01,-99.25,10,16.48,3.62,-60, 6842")
        self._other_names = []

 = DeltaArae


class EpsilonArae01(FixedStar): # ,eps01Ara

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eps01Ara", context=context, swe_string="Epsilon Arae 01,eps01Ara,ICRS,16,59,35.04880,-53,09,37.5713,2.16,22.04,23.85,9.04,4.05,-52,10372")
        self._other_names = []

 = EpsilonArae01


class ZetaArae(FixedStar): # ,zetAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAra", context=context, swe_string="Zeta Arae,zetAra,ICRS,16,58,37.21217,-55,59,24.5203,-17.8,-36.67,-6,6.71,3.076,-55, 7766")
        self._other_names = []

 = ZetaArae


class EtaArae(FixedStar): # ,etaAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaAra", context=context, swe_string="Eta Arae,etaAra,ICRS,16,49,47.15653,-59,02,28.9575,39.73,-24.91,9,10.9,3.744,-58, 6906")
        self._other_names = []

 = EtaArae


class ThetaArae(FixedStar): # ,tetAra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAra", context=context, swe_string="Theta Arae,tetAra,ICRS,18,06,37.87129,-50,05,29.3125,-8.27,-8.7,3.4,4.01,3.66,-50,11720")
        self._other_names = []

 = ThetaArae


class MessierObjectu.Ara(FixedStar): # ,mu.Ara

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Ara", context=context, swe_string="Messier Object u.Ara,mu.Ara,ICRS,17,44,08.70114,-51,50,02.5853,-16.85,-190.6,-9.36,64.47,5.15,-51,11094")
        self._other_names = ['Cervantes']

Cervantes = MessierObjectu.Ara


class AlphaArietis(FixedStar): # ,alfAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAri", context=context, swe_string="Alpha Arietis,alfAri,ICRS,02,07,10.40570,+23,27,44.7032,188.55,-148.08,-14.64,49.56,2.01, 22,  306")
        self._other_names = ['Hamal']

Hamal = AlphaArietis


class BetaArietis(FixedStar): # ,betAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAri", context=context, swe_string="Beta Arietis,betAri,ICRS,01,54,38.41099,+20,48,28.9133,98.74,-110.41,-3.1,55.6,2.65, 20,  306")
        self._other_names = ['Sheratan']

Sheratan = BetaArietis


class BetaArietis(FixedStar): # ,betAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAri", context=context, swe_string="Beta Arietis,betAri,ICRS,01,54,38.41099,+20,48,28.9133,98.74,-110.41,-3.1,55.6,2.65, 20,  306")
        self._other_names = ['Ashvini']

Ashvini = BetaArietis


class GammaArietis(FixedStar): # ,gamAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamAri", context=context, swe_string="Gamma Arietis,gamAri,ICRS,01,53,31.81479,+19,17,37.8790,79.2,-97.63,-0.6,19.88,3.88, 18,  243")
        self._other_names = ['Mesarthim']

Mesarthim = GammaArietis


class DeltaArietis(FixedStar): # ,delAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delAri", context=context, swe_string="Delta Arietis,delAri,ICRS,03,11,37.76465,+19,43,36.0397,153.33,-8.28,22.81,19.22,4.37, 19,  477")
        self._other_names = ['Botein']

Botein = DeltaArietis


class ZetaArietis(FixedStar): # ,zetAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAri", context=context, swe_string="Zeta Arietis,zetAri,ICRS,03,14,54.09731,+21,02,40.0103,-27.83,-74.59,7.3,12.44,4.869, 20,  527")
        self._other_names = []

 = ZetaArietis


class ThetaArietis(FixedStar): # ,tetAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAri", context=context, swe_string="Theta Arietis,tetAri,ICRS,02,18,07.53838,+19,54,04.1862,-13.19,0.72,2.3,7.29,5.572, 19,  340")
        self._other_names = []

 = ThetaArietis


class NuArietis(FixedStar): # ,nu.Ari

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Ari", context=context, swe_string="Nu Arietis,nu.Ari,ICRS,02,38,48.99425,+21,57,41.0616,-7.47,-15.9,8,9.68,5.451, 21,  362")
        self._other_names = []

 = NuArietis


class SigmaArietis(FixedStar): # ,sigAri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigAri", context=context, swe_string="Sigma Arietis,sigAri,ICRS,02,51,29.58609,+15,04,55.4500,30.13,-23.68,17,6.6,5.516, 14,  480")
        self._other_names = []

 = SigmaArietis


class TauArietis01(FixedStar): # ,tau01Ari

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau01Ari", context=context, swe_string="Tau Arietis 01,tau01Ari,ICRS,03,21,13.62411,+21,08,49.5150,20.98,-21.8,14.7,6.41,5.355, 20,  543")
        self._other_names = []

 = TauArietis01


class Arietis39(FixedStar): # ,39Ari

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",39Ari", context=context, swe_string="Arietis39,39Ari,ICRS,02,47,54.54142,+29,14,49.6132,149.47,-127.05,-15.53,19.01,4.51, 0,0")
        self._other_names = ['Lilii Borea']

LiliiBorea = Arietis39


class Arietis41(FixedStar): # ,41Ari

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",41Ari", context=context, swe_string="Arietis41,41Ari,ICRS,02,49,59.03324,+27,15,37.8260,66.81,-116.52,4,19.69,3.594, 20,  543")
        self._other_names = ['Bharani']

Bharani = Arietis41


class AlphaAurigae(FixedStar): # ,alfAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAur", context=context, swe_string="Alpha Aurigae,alfAur,ICRS,05,16,41.35871,+45,59,52.7693,75.25,-426.89,29.19,76.2,0.08, 45, 1077")
        self._other_names = ['Capella']

Capella = AlphaAurigae


class AlphaAurigae(FixedStar): # ,alfAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAur", context=context, swe_string="Alpha Aurigae,alfAur,ICRS,05,16,41.35871,+45,59,52.7693,75.25,-426.89,29.19,76.2,0.08, 45, 1077")
        self._other_names = ['Brahmahridaya']

Brahmahridaya = AlphaAurigae


class BetaAurigae(FixedStar): # ,betAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAur", context=context, swe_string="Beta Aurigae,betAur,ICRS,05,59,31.72293,+44,56,50.7573,-56.44,-0.95,-15.75,40.21,1.9, 44, 1328")
        self._other_names = ['Menkalinan']

Menkalinan = BetaAurigae


class DeltaAurigae(FixedStar): # ,delAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delAur", context=context, swe_string="Delta Aurigae,delAur,ICRS,05,59,31.63201,+54,17,04.7703,81.81,-132.98,9.75,25.88,3.72, 54,  970")
        self._other_names = ['Prijipati']

Prijipati = DeltaAurigae


class EpsilonAurigae(FixedStar): # ,epsAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsAur", context=context, swe_string="Epsilon Aurigae,epsAur,ICRS,05,01,58.13245,+43,49,23.9059,-0.86,-2.66,-10.4,1.53,2.99, 43, 1166")
        self._other_names = ['Maaz']

Maaz = EpsilonAurigae


class EpsilonAurigae(FixedStar): # ,epsAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsAur", context=context, swe_string="Epsilon Aurigae,epsAur,ICRS,05,01,58.13245,+43,49,23.9059,-0.86,-2.66,-10.4,1.53,2.99, 43, 1166")
        self._other_names = ['Almaaz']

Almaaz = EpsilonAurigae


class EpsilonAurigae(FixedStar): # ,epsAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsAur", context=context, swe_string="Epsilon Aurigae,epsAur,ICRS,05,01,58.13245,+43,49,23.9059,-0.86,-2.66,-10.4,1.53,2.99, 43, 1166")
        self._other_names = ['Al Anz']

AlAnz = EpsilonAurigae


class ZetaAurigae(FixedStar): # ,zetAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAur", context=context, swe_string="Zeta Aurigae,zetAur,ICRS,05,02,28.68739,+41,04,33.0200,9.45,-20.71,11.32,4.15,3.75, 40, 1142")
        self._other_names = ['Haedi']

Haedi = ZetaAurigae


class ZetaAurigae(FixedStar): # ,zetAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAur", context=context, swe_string="Zeta Aurigae,zetAur,ICRS,05,02,28.68739,+41,04,33.0200,9.45,-20.71,11.32,4.15,3.75, 40, 1142")
        self._other_names = ['Hoedus I']

HoedusI = ZetaAurigae


class ZetaAurigae(FixedStar): # ,zetAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAur", context=context, swe_string="Zeta Aurigae,zetAur,ICRS,05,02,28.68739,+41,04,33.0200,9.45,-20.71,11.32,4.15,3.75, 40, 1142")
        self._other_names = ['Sadatoni']

Sadatoni = ZetaAurigae


class ZetaAurigae(FixedStar): # ,zetAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetAur", context=context, swe_string="Zeta Aurigae,zetAur,ICRS,05,02,28.68739,+41,04,33.0200,9.45,-20.71,11.32,4.15,3.75, 40, 1142")
        self._other_names = ['Saclateni']

Saclateni = ZetaAurigae


class EtaAurigae(FixedStar): # ,etaAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaAur", context=context, swe_string="Eta Aurigae,etaAur,ICRS,05,06,30.89337,+41,14,04.1127,31.45,-67.87,7.3,13.4,3.18, 41, 1058")
        self._other_names = ['Hoedus II']

HoedusII = EtaAurigae


class EtaAurigae(FixedStar): # ,etaAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaAur", context=context, swe_string="Eta Aurigae,etaAur,ICRS,05,06,30.89337,+41,14,04.1127,31.45,-67.87,7.3,13.4,3.18, 41, 1058")
        self._other_names = ['Haedus']

Haedus = EtaAurigae


class ThetaAurigae(FixedStar): # ,tetAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAur", context=context, swe_string="Theta Aurigae,tetAur,ICRS,05,59,43.27012,+37,12,45.3047,43.63,-73.79,29.3,19.7,2.62, 41, 1058")
        self._other_names = ['Bogardus']

Bogardus = ThetaAurigae


class ThetaAurigae(FixedStar): # ,tetAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAur", context=context, swe_string="Theta Aurigae,tetAur,ICRS,05,59,43.27012,+37,12,45.3047,43.63,-73.79,29.3,19.7,2.62, 41, 1058")
        self._other_names = ['Manus']

Manus = ThetaAurigae


class ThetaAurigae(FixedStar): # ,tetAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetAur", context=context, swe_string="Theta Aurigae,tetAur,ICRS,05,59,43.27012,+37,12,45.3047,43.63,-73.79,29.3,19.7,2.62, 41, 1058")
        self._other_names = ['Mahasim']

Mahasim = ThetaAurigae


class IotaAurigae(FixedStar): # ,iotAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAur", context=context, swe_string="Iota Aurigae,iotAur,ICRS,04,56,59.62109,+33,09,57.9585,6.79,-14.88,17.78,6.61,2.69, 32,  855")
        self._other_names = ['Hasseleh']

Hasseleh = IotaAurigae


class IotaAurigae(FixedStar): # ,iotAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAur", context=context, swe_string="Iota Aurigae,iotAur,ICRS,04,56,59.62109,+33,09,57.9585,6.79,-14.88,17.78,6.61,2.69, 32,  855")
        self._other_names = ['Hassaleh']

Hassaleh = IotaAurigae


class IotaAurigae(FixedStar): # ,iotAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAur", context=context, swe_string="Iota Aurigae,iotAur,ICRS,04,56,59.62109,+33,09,57.9585,6.79,-14.88,17.78,6.61,2.69, 32,  855")
        self._other_names = ['Al Khabdhilinan']

AlKhabdhilinan = IotaAurigae


class KappaAurigae(FixedStar): # ,kapAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapAur", context=context, swe_string="Kappa Aurigae,kapAur,ICRS,06,15,22.68906,+29,29,53.0760,-70.88,-261.42,20.69,18.43,4.35, 29, 1154")
        self._other_names = []

 = KappaAurigae


class LambdaAurigae(FixedStar): # ,lamAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamAur", context=context, swe_string="Lambda Aurigae,lamAur,ICRS,05,19,08.47420,+40,05,56.5826,518.99,-665.06,66.57,79.17,4.71, 39, 1248")
        self._other_names = []

 = LambdaAurigae


class MessierObjectu.Aur(FixedStar): # ,mu.Aur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Aur", context=context, swe_string="Messier Object u.Aur,mu.Aur,ICRS,05,13,25.71733,+38,29,04.1879,-19.18,-72.93,26,21.32,4.821, 38, 1063")
        self._other_names = []

 = MessierObjectu.Aur


class NuAurigae(FixedStar): # ,nu.Aur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Aur", context=context, swe_string="Nu Aurigae,nu.Aur,ICRS,05,51,29.40040,+39,08,54.5428,10.33,1.73,9.92,14.16,3.95, 39, 1429")
        self._other_names = []

 = NuAurigae


class XiAurigae(FixedStar): # ,ksiAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiAur", context=context, swe_string="Xi Aurigae,ksiAur,ICRS,05,54,50.78082,+55,42,25.0084,-4.85,17.29,-11.8,13.69,4.96, 55, 1027")
        self._other_names = []

 = XiAurigae


class OmicronAurigae(FixedStar): # ,omiAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiAur", context=context, swe_string="Omicron Aurigae,omiAur,ICRS,05,45,54.04306,+49,49,34.6097,-6.97,-1.22,-7.7,7.89,5.46, 49, 1398")
        self._other_names = []

 = OmicronAurigae


class ChiAurigae(FixedStar): # ,chiAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiAur", context=context, swe_string="Chi Aurigae,chiAur,ICRS,05,32,43.67312,+32,11,31.2753,-1.52,-4.33,-0.2,0.01,4.79, 32, 1024")
        self._other_names = []

 = ChiAurigae


class PsiAurigae01(FixedStar): # ,psi01Aur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psi01Aur", context=context, swe_string="Psi Aurigae 01,psi01Aur,ICRS,06,24,53.90129,+49,17,16.4199,-0.66,-1.82,4.4,0.82,4.75, 49, 1488")
        self._other_names = []

 = PsiAurigae01


class PsiAurigae05(FixedStar): # ,psi05Aur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psi05Aur", context=context, swe_string="Psi Aurigae 05,psi05Aur,ICRS,06,46,44.33818,+43,34,38.7268,-1.07,164.25,-23.9,59.82,5.246, 43, 1595")
        self._other_names = []

 = PsiAurigae05


class PsiAurigae06(FixedStar): # ,psi06Aur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psi06Aur", context=context, swe_string="Psi Aurigae 06,psi06Aur,ICRS,06,47,39.57703,+48,47,22.1222,-4.32,7.19,-6.51,9.05,5.216, 48, 1436")
        self._other_names = []

 = PsiAurigae06


class AlphaBootis(FixedStar): # ,alfBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfBoo", context=context, swe_string="Alpha Bootis,alfBoo,ICRS,14,15,39.67207,+19,10,56.6730,-1093.39,-2000.06,-5.19,88.83,-0.05, 19, 2777")
        self._other_names = ['Arcturus', 'HIP 69673']

Arcturus = AlphaBootis
HIP69673 = AlphaBootis


class AlphaBootis(FixedStar): # ,alfBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfBoo", context=context, swe_string="Alpha Bootis,alfBoo,ICRS,14,15,39.67207,+19,10,56.6730,-1093.39,-2000.06,-5.19,88.83,-0.05, 19, 2777")
        self._other_names = ['Svati']

Svati = AlphaBootis


class BetaBootis(FixedStar): # ,betBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betBoo", context=context, swe_string="Beta Bootis,betBoo,ICRS,15,01,56.76238,+40,23,26.0406,-40.15,-28.86,-18.4,14.48,3.52, 40, 2840")
        self._other_names = ['Nekkar']

Nekkar = BetaBootis


class GammaBootis(FixedStar): # ,gamBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamBoo", context=context, swe_string="Gamma Bootis,gamBoo,ICRS,14,32,04.67180,+38,18,29.7043,-115.71,151.16,-32.4,37.58,3.02, 38, 2565")
        self._other_names = ['Seginus']

Seginus = GammaBootis


class GammaBootis(FixedStar): # ,gamBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamBoo", context=context, swe_string="Gamma Bootis,gamBoo,ICRS,14,32,04.67180,+38,18,29.7043,-115.71,151.16,-32.4,37.58,3.02, 38, 2565")
        self._other_names = ['Haris']

Haris = GammaBootis


class DeltaBootis(FixedStar): # ,delBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delBoo", context=context, swe_string="Delta Bootis,delBoo,ICRS,15,15,30.16295,+33,18,53.3926,84.74,-111.58,-12.29,26.78,3.49, 33, 2561")
        self._other_names = ['Princeps']

Princeps = DeltaBootis


class EpsilonBootis(FixedStar): # ,epsBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsBoo", context=context, swe_string="Epsilon Bootis,epsBoo,ICRS,14,44,59.21746,+27,04,27.2099,-50.95,21.07,-16.31,16.1,2.39, 27, 2417")
        self._other_names = ['Izar']

Izar = EpsilonBootis


class EpsilonBootis(FixedStar): # ,epsBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsBoo", context=context, swe_string="Epsilon Bootis,epsBoo,ICRS,14,44,59.21746,+27,04,27.2099,-50.95,21.07,-16.31,16.1,2.39, 27, 2417")
        self._other_names = ['Mirak']

Mirak = EpsilonBootis


class EpsilonBootis(FixedStar): # ,epsBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsBoo", context=context, swe_string="Epsilon Bootis,epsBoo,ICRS,14,44,59.21746,+27,04,27.2099,-50.95,21.07,-16.31,16.1,2.39, 27, 2417")
        self._other_names = ['Pulcherrima']

Pulcherrima = EpsilonBootis


class ZetaBootis(FixedStar): # ,zetBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetBoo", context=context, swe_string="Zeta Bootis,zetBoo,ICRS,14,41,08.95158,+13,43,41.8967,51.95,-11.08,-8.5,18.56,3.793,0,0")
        self._other_names = []

 = ZetaBootis


class EtaBootis(FixedStar): # ,etaBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaBoo", context=context, swe_string="Eta Bootis,etaBoo,ICRS,13,54,41.07892,+18,23,51.7946,-60.95,-356.29,0.7,87.75,2.68, 19, 2725")
        self._other_names = ['Mufrid']

Mufrid = EtaBootis


class EtaBootis(FixedStar): # ,etaBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaBoo", context=context, swe_string="Eta Bootis,etaBoo,ICRS,13,54,41.07892,+18,23,51.7946,-60.95,-356.29,0.7,87.75,2.68, 19, 2725")
        self._other_names = ['Muphrid']

Muphrid = EtaBootis


class ThetaBootis(FixedStar): # ,tetBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetBoo", context=context, swe_string="Theta Bootis,tetBoo,ICRS,14,25,11.79703,+51,51,02.6769,-235.4,-399.07,-11.6,68.82,4.05, 52, 1804")
        self._other_names = ['Asellus Primus']

AsellusPrimus = ThetaBootis


class IotaBootis(FixedStar): # ,iotBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotBoo", context=context, swe_string="Iota Bootis,iotBoo,ICRS,14,16,09.92995,+51,22,02.0267,-149.39,88.72,-18.7,34.4,4.75, 52, 1784")
        self._other_names = ['Asellus Secundus']

AsellusSecundus = IotaBootis


class KappaBootis02(FixedStar): # ,kap02Boo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kap02Boo", context=context, swe_string="Kappa Bootis 02,kap02Boo,ICRS,14,13,29.00737,+51,47,23.8856,61.03,-9.22,-15.6,19.96,4.51, 52, 1782")
        self._other_names = ['Asellus Tertius']

AsellusTertius = KappaBootis02


class LambdaBootis(FixedStar): # ,lamBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamBoo", context=context, swe_string="Lambda Bootis,lamBoo,ICRS,14,16,23.01880,+46,05,17.9005,-187.33,159.05,-7.9,32.94,4.18, 46, 1949")
        self._other_names = ['Xuange']

Xuange = LambdaBootis


class MessierObjectu.01Boo(FixedStar): # ,mu.01Boo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.01Boo", context=context, swe_string="Messier Object u.01Boo,mu.01Boo,ICRS,15,24,29.42836,+37,22,37.7577,-146.73,79.85,-8.6,28.83,4.296, 37, 2636")
        self._other_names = ['Alkalurops']

Alkalurops = MessierObjectu.01Boo


class NuBootis01(FixedStar): # ,nu.01Boo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.01Boo", context=context, swe_string="Nu Bootis 01,nu.01Boo,ICRS,15,30,55.75951,+40,49,58.9743,11.28,-8.11,-11.12,3.89,5.026, 41, 2609")
        self._other_names = []

 = NuBootis01


class RhoBootis(FixedStar): # ,rhoBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoBoo", context=context, swe_string="Rho Bootis,rhoBoo,ICRS,14,31,49.78962,+30,22,17.1781,-100.9,120.73,-13.57,20.37,3.59, 31, 2628")
        self._other_names = ['Hemelein Prima']

HemeleinPrima = RhoBootis


class RhoBootis(FixedStar): # ,rhoBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoBoo", context=context, swe_string="Rho Bootis,rhoBoo,ICRS,14,31,49.78962,+30,22,17.1781,-100.9,120.73,-13.57,20.37,3.59, 31, 2628")
        self._other_names = ['Al Hamalain']

AlHamalain = RhoBootis


class SigmaBootis(FixedStar): # ,sigBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigBoo", context=context, swe_string="Sigma Bootis,sigBoo,ICRS,14,34,40.81699,+29,44,42.4590,188.35,131.77,0.37,63.16,4.47, 30, 2536")
        self._other_names = ['Hemelein Secunda']

HemeleinSecunda = SigmaBootis


class TauBootis(FixedStar): # ,tauBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauBoo", context=context, swe_string="Tau Bootis,tauBoo,ICRS,13,47,15.74340,+17,27,24.8552,-479.53,53.49,-16.03,64.03,4.49, 18, 2782")
        self._other_names = []

 = TauBootis


class PhiBootis(FixedStar): # ,phiBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiBoo", context=context, swe_string="Phi Bootis,phiBoo,ICRS,15,37,49.59790,+40,21,12.3635,61.23,60.09,-10.62,19.22,5.254, 40, 2907")
        self._other_names = ['Ceginus']

Ceginus = PhiBootis


class PsiBootis(FixedStar): # ,psiBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiBoo", context=context, swe_string="Psi Bootis,psiBoo,ICRS,15,04,26.74234,+26,56,51.5399,-175.42,-4.06,-25.72,13.26,4.55, 27, 2447")
        self._other_names = []

 = PsiBootis


class Bootis38(FixedStar): # ,38Boo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",38Boo", context=context, swe_string="Bootis38,38Boo,ICRS,14,49,18.66977,+46,06,58.3417,-6.73,-77.06,-4.5,20.41,5.757, 46, 1993")
        self._other_names = ['Merga']

Merga = Bootis38


class AlphaCaeli(FixedStar): # ,alfCae

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCae", context=context, swe_string="Alpha Caeli,alfCae,ICRS,04,40,33.71305,-41,51,49.5075,-140.39,-74.82,-0.6,49.59,4.45,-42, 1587")
        self._other_names = []

 = AlphaCaeli


class BetaCaeli(FixedStar): # ,betCae

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCae", context=context, swe_string="Beta Caeli,betCae,ICRS,04,42,03.48029,-37,08,39.4641,46.59,193.56,26.8,34.88,5.05,-37, 1867")
        self._other_names = []

 = BetaCaeli


class DeltaCaeli(FixedStar): # ,delCae

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCae", context=context, swe_string="Delta Caeli,delCae,ICRS,04,30,50.09903,-44,57,13.5035,1.64,-3.09,14.2,4.63,5.059,-45, 1567")
        self._other_names = []

 = DeltaCaeli


class AlphaCamelopardalis(FixedStar): # ,alfCam

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCam", context=context, swe_string="Alpha Camelopardalis,alfCam,ICRS,04,54,03.01040,+66,20,33.6365,-0.13,6.89,6.1,0.52,4.29, 66,  358")
        self._other_names = []

 = AlphaCamelopardalis


class BetaCamelopardalis(FixedStar): # ,betCam

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCam", context=context, swe_string="Beta Camelopardalis,betCam,ICRS,05,03,25.08963,+60,26,32.0895,-6.5,-14.15,-1.9,3.74,4.02, 60,  856")
        self._other_names = []

 = BetaCamelopardalis


class GammaCamelopardalis(FixedStar): # ,gamCam

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCam", context=context, swe_string="Gamma Camelopardalis,gamCam,ICRS,03,50,21.50892,+71,19,56.1485,18.17,-42.85,0.2,9.09,4.604, 70,  259")
        self._other_names = []

 = GammaCamelopardalis


class Camelopardalis2(FixedStar): # ,2Cam

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",2Cam", context=context, swe_string="Camelopardalis2,2Cam,ICRS,04,39,58.07002,+53,28,22.9163,34.51,-84.7,20.1,22.49,5.376,0,0")
        self._other_names = []

 = Camelopardalis2


class Camelopardalis7(FixedStar): # ,7Cam

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",7Cam", context=context, swe_string="Camelopardalis7,7Cam,ICRS,04,57,17.19609,+53,45,07.5654,-24.51,7.71,-7.9,8.77,4.433,0,0")
        self._other_names = []

 = Camelopardalis7


class BrightStarCatalogue4609(FixedStar): # ,HR4609

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HR4609", context=context, swe_string="Bright Star Catalogue 4609,HR4609,ICRS,12,05,15.11890,+76,54,20.6475,147.68,-91.65,-20.19,10.3,5.785, 0,0")
        self._other_names = ['Tonatiuh']

Tonatiuh = BrightStarCatalogue4609


class AlphaCapricorni01(FixedStar): # ,alf01Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf01Cap", context=context, swe_string="Alpha Capricorni 01,alf01Cap,ICRS,20,17,38.86987,-12,30,29.5594,22.98,1.28,-25.79,5.73,4.27,-12, 5683")
        self._other_names = ['Algedi']

Algedi = AlphaCapricorni01


class AlphaCapricorni01(FixedStar): # ,alf01Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf01Cap", context=context, swe_string="Alpha Capricorni 01,alf01Cap,ICRS,20,17,38.86987,-12,30,29.5594,22.98,1.28,-25.79,5.73,4.27,-12, 5683")
        self._other_names = ['Giedi Prima']

GiediPrima = AlphaCapricorni01


class AlphaCapricorni02(FixedStar): # ,alf02Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf02Cap", context=context, swe_string="Alpha Capricorni 02,alf02Cap,ICRS,20,18,03.25595,-12,32,41.4684,62.63,2.66,0.7,30.82,3.58,-12, 5685")
        self._other_names = ['Algedi']

Algedi = AlphaCapricorni02


class AlphaCapricorni02(FixedStar): # ,alf02Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf02Cap", context=context, swe_string="Alpha Capricorni 02,alf02Cap,ICRS,20,18,03.25595,-12,32,41.4684,62.63,2.66,0.7,30.82,3.58,-12, 5685")
        self._other_names = ['Giedi Secunda']

GiediSecunda = AlphaCapricorni02


class BetaCapricorni(FixedStar): # ,betCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCap", context=context, swe_string="Beta Capricorni,betCap,ICRS,20,21,00.67326,-14,46,52.9791,44.92,7.38,-19,9.98,3.08,-15, 5629")
        self._other_names = ['Dabih']

Dabih = BetaCapricorni


class BetaCapricorni01(FixedStar): # ,bet01Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet01Cap", context=context, swe_string="Beta Capricorni 01,bet01Cap,ICRS,20,21,00.67326,-14,46,52.9791,44.92,7.38,-19,9.98,3.08,-15, 5629")
        self._other_names = ['Dabih']

Dabih = BetaCapricorni01


class GammaCapricorni(FixedStar): # ,gamCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCap", context=context, swe_string="Gamma Capricorni,gamCap,ICRS,21,40,05.45648,-16,39,44.3072,187.56,-22.45,-31.2,20.77,3.67,-17, 6340")
        self._other_names = ['Nashira']

Nashira = GammaCapricorni


class DeltaCapricorni(FixedStar): # ,delCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCap", context=context, swe_string="Delta Capricorni,delCap,ICRS,21,47,02.44424,-16,07,38.2335,261.7,-296.7,-3.4,84.27,2.83,-16, 5943")
        self._other_names = ['Deneb Algedi']

DenebAlgedi = DeltaCapricorni


class EpsilonCapricorni(FixedStar): # ,epsCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCap", context=context, swe_string="Epsilon Capricorni,epsCap,ICRS,21,37,04.83068,-19,27,57.6464,12.79,0.28,-23.7,3.09,4.55,-20, 6251")
        self._other_names = ['Castra']

Castra = EpsilonCapricorni


class ZetaCapricorni(FixedStar): # ,zetCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCap", context=context, swe_string="Zeta Capricorni,zetCap,ICRS,21,26,40.02634,-22,24,40.8042,-2.23,18.1,2.1,8.46,3.74,-22,15388")
        self._other_names = ['Marakk']

Marakk = ZetaCapricorni


class EtaCapricorni(FixedStar): # ,etaCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCap", context=context, swe_string="Eta Capricorni,etaCap,ICRS,21,04,24.30132,-19,51,17.9711,-37.62,-24.95,23.8,20.2,4.84,-20, 6115")
        self._other_names = ['Armus']

Armus = EtaCapricorni


class ThetaCapricorni(FixedStar): # ,tetCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCap", context=context, swe_string="Theta Capricorni,tetCap,ICRS,21,05,56.82783,-17,13,58.3021,79.33,-62.01,-10.9,20.11,4.07,-17, 6174")
        self._other_names = ['Dorsum']

Dorsum = ThetaCapricorni


class IotaCapricorni(FixedStar): # ,iotCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCap", context=context, swe_string="Iota Capricorni,iotCap,ICRS,21,22,14.79565,-16,50,04.3598,30,4.52,12.31,16.58,4.27,-17, 6245")
        self._other_names = []

 = IotaCapricorni


class LambdaCapricorni(FixedStar): # ,lamCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamCap", context=context, swe_string="Lambda Capricorni,lamCap,ICRS,21,46,32.09739,-11,21,57.4391,28.92,-9.66,-2.4,11.58,5.567,-12, 6087")
        self._other_names = []

 = LambdaCapricorni


class MessierObjectu.Cap(FixedStar): # ,mu.Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Cap", context=context, swe_string="Messier Object u.Cap,mu.Cap,ICRS,21,53,17.77054,-13,33,06.3679,311.22,13.46,-21.5,37.57,5.08,-14, 6149")
        self._other_names = []

 = MessierObjectu.Cap


class NuCapricorni(FixedStar): # ,nu.Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Cap", context=context, swe_string="Nu Capricorni,nu.Cap,ICRS,20,20,39.81562,-12,45,32.6844,14.74,-14.32,-1,12.88,4.76,-13, 5642")
        self._other_names = ['Alshat']

Alshat = NuCapricorni


class PiCapricorni(FixedStar): # ,pi.Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Cap", context=context, swe_string="Pi Capricorni,pi.Cap,ICRS,20,27,19.21088,-18,12,42.1980,11.89,-11.35,-13,5.98,5.25,-18, 5685")
        self._other_names = ['Oculus']

Oculus = PiCapricorni


class RhoCapricorni(FixedStar): # ,rhoCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoCap", context=context, swe_string="Rho Capricorni,rhoCap,ICRS,20,28,51.61448,-17,48,49.2693,-14.98,-7.29,18.4,33.04,4.803,-18, 5689")
        self._other_names = ['Bos']

Bos = RhoCapricorni


class PsiCapricorni(FixedStar): # ,psiCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiCap", context=context, swe_string="Psi Capricorni,psiCap,ICRS,20,46,05.73263,-25,16,15.2312,-51.96,-156.56,25.6,68.13,4.122,-25,15018")
        self._other_names = ['Pazan']

Pazan = PsiCapricorni


class PsiCapricorni(FixedStar): # ,psiCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiCap", context=context, swe_string="Psi Capricorni,psiCap,ICRS,20,46,05.73263,-25,16,15.2312,-51.96,-156.56,25.6,68.13,4.122,-25,15018")
        self._other_names = ['Pazhan']

Pazhan = PsiCapricorni


class UpsilonCapricorni(FixedStar): # ,upsCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsCap", context=context, swe_string="Upsilon Capricorni,upsCap,ICRS,20,40,02.94470,-18,08,19.1724,-22.41,-21.67,-12.3,5.62,5.1,-18, 5738")
        self._other_names = []

 = UpsilonCapricorni


class OmegaCapricorni(FixedStar): # ,omeCap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeCap", context=context, swe_string="Omega Capricorni,omeCap,ICRS,20,51,49.29084,-26,55,08.8574,-8.36,-0.36,9.1,3.87,4.12,-27,15082")
        self._other_names = ['Baten Algiedi']

BatenAlgiedi = OmegaCapricorni


class Capricorni24(FixedStar): # ,24Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",24Cap", context=context, swe_string="Capricorni24,24Cap,ICRS,21,07,07.66733,-25,00,21.0790,-28.09,-44.14,32.1,7.15,4.5,0,0")
        self._other_names = []

 = Capricorni24


class Capricorni36(FixedStar): # ,36Cap

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",36Cap", context=context, swe_string="Capricorni36,36Cap,ICRS,21,28,43.40070,-21,48,25.8504,134.83,-5.73,-22.2,19.06,4.5,0,0")
        self._other_names = []

 = Capricorni36


class AlphaCarinae(FixedStar): # ,alfCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCar", context=context, swe_string="Alpha Carinae,alfCar,ICRS,06,23,57.10988,-52,41,44.3810,19.93,23.24,20.3,10.55,-0.74,-52,  914")
        self._other_names = ['Canopus']

Canopus = AlphaCarinae


class AlphaCarinae(FixedStar): # ,alfCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCar", context=context, swe_string="Alpha Carinae,alfCar,ICRS,06,23,57.10988,-52,41,44.3810,19.93,23.24,20.3,10.55,-0.74,-52,  914")
        self._other_names = ['Agastya']

Agastya = AlphaCarinae


class BetaCarinae(FixedStar): # ,betCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCar", context=context, swe_string="Beta Carinae,betCar,ICRS,09,13,11.97746,-69,43,01.9473,-156.47,108.95,-5.1,28.82,1.69,-69, 1023")
        self._other_names = ['Miaplacidus']

Miaplacidus = BetaCarinae


class EpsilonCarinae(FixedStar): # ,epsCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCar", context=context, swe_string="Epsilon Carinae,epsCar,ICRS,08,22,30.83526,-59,30,34.1431,-25.52,22.06,11.6,5.39,1.953,-59, 1032")
        self._other_names = ['Avior']

Avior = EpsilonCarinae


class EtaCarinae(FixedStar): # ,etaCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCar", context=context, swe_string="Eta Carinae,etaCar,ICRS,10,45,03.546,-59,41,03.95,-11,4.1,-25,0,6.21,0, 0")
        self._other_names = ['Foramen']

Foramen = EtaCarinae


class ThetaCarinae(FixedStar): # ,tetCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCar", context=context, swe_string="Theta Carinae,tetCar,ICRS,10,42,57.40197,-64,23,40.0208,-18.36,12.03,20,7.16,2.76,-63, 1599")
        self._other_names = ['Vathorz Posterior']

VathorzPosterior = ThetaCarinae


class IotaCarinae(FixedStar): # ,iotCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCar", context=context, swe_string="Iota Carinae,iotCar,ICRS,09,17,05.40686,-59,16,30.8353,-18.86,11.98,12,4.26,2.26,-58, 1465")
        self._other_names = ['Scutulum']

Scutulum = IotaCarinae


class IotaCarinae(FixedStar): # ,iotCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCar", context=context, swe_string="Iota Carinae,iotCar,ICRS,09,17,05.40686,-59,16,30.8353,-18.86,11.98,12,4.26,2.26,-58, 1465")
        self._other_names = ['Aspidiske']

Aspidiske = IotaCarinae


class ChiCarinae(FixedStar): # ,chiCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiCar", context=context, swe_string="Chi Carinae,chiCar,ICRS,07,56,46.71398,-52,58,56.4700,-28.68,19.71,19.4,7.17,3.431,-52, 1343")
        self._other_names = ['Drus']

Drus = ChiCarinae


class ChiCarinae(FixedStar): # ,chiCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiCar", context=context, swe_string="Chi Carinae,chiCar,ICRS,07,56,46.71398,-52,58,56.4700,-28.68,19.71,19.4,7.17,3.431,-52, 1343")
        self._other_names = ['Drys']

Drys = ChiCarinae


class OmegaCarinae(FixedStar): # ,omeCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeCar", context=context, swe_string="Omega Carinae,omeCar,ICRS,10,13,44.21739,-70,02,16.4563,-36.01,7.09,10.4,9.54,3.33,-69, 1178")
        self._other_names = ['Simiram']

Simiram = OmegaCarinae


class UpsilonCarinae(FixedStar): # ,upsCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsCar", context=context, swe_string="Upsilon Carinae,upsCar,ICRS,09,47,06.12170,-65,04,19.2267,-11.51,4.71,13.6,2.27,2.96,0, 0")
        self._other_names = ['Vathorz Prior']

VathorzPrior = UpsilonCarinae


class qCar(FixedStar): # ,qCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",qCar", context=context, swe_string="qCar,qCar,ICRS,10,17,04.97530,-61,19,56.2883,-24.73,7.2,8.2,4.96,3.35,0, 0")
        self._other_names = []

 = qCar


class AlphaCassiopeiae(FixedStar): # ,alfCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCas", context=context, swe_string="Alpha Cassiopeiae,alfCas,ICRS,00,40,30.44107,+56,32,14.3922,50.88,-32.13,-4.31,14.29,2.23, 55,  139")
        self._other_names = ['Schedar']

Schedar = AlphaCassiopeiae


class AlphaCassiopeiae(FixedStar): # ,alfCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCas", context=context, swe_string="Alpha Cassiopeiae,alfCas,ICRS,00,40,30.44107,+56,32,14.3922,50.88,-32.13,-4.31,14.29,2.23, 55,  139")
        self._other_names = ['Shedir']

Shedir = AlphaCassiopeiae


class AlphaCassiopeiae(FixedStar): # ,alfCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCas", context=context, swe_string="Alpha Cassiopeiae,alfCas,ICRS,00,40,30.44107,+56,32,14.3922,50.88,-32.13,-4.31,14.29,2.23, 55,  139")
        self._other_names = ['Schedir']

Schedir = AlphaCassiopeiae


class BetaCassiopeiae(FixedStar): # ,betCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCas", context=context, swe_string="Beta Cassiopeiae,betCas,ICRS,00,09,10.68518,+59,08,59.2120,523.5,-179.77,4.3,59.58,2.27, 58,    3")
        self._other_names = ['Caph']

Caph = BetaCassiopeiae


class GammaCassiopeiae(FixedStar): # ,gamCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCas", context=context, swe_string="Gamma Cassiopeiae,gamCas,ICRS,00,56,42.5317,+60,43,00.265,25.65,-3.82,-6.8,5.32,2.39, 59,  144")
        self._other_names = ['Tsih']

Tsih = GammaCassiopeiae


class GammaCassiopeiae(FixedStar): # ,gamCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCas", context=context, swe_string="Gamma Cassiopeiae,gamCas,ICRS,00,56,42.5317,+60,43,00.265,25.65,-3.82,-6.8,5.32,2.39, 59,  144")
        self._other_names = ['Cih']

Cih = GammaCassiopeiae


class DeltaCassiopeiae(FixedStar): # ,delCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCas", context=context, swe_string="Delta Cassiopeiae,delCas,ICRS,01,25,48.95147,+60,14,07.0225,296.57,-49.22,6.7,32.81,2.68, 59,  248")
        self._other_names = ['Ruchbah']

Ruchbah = DeltaCassiopeiae


class DeltaCassiopeiae(FixedStar): # ,delCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCas", context=context, swe_string="Delta Cassiopeiae,delCas,ICRS,01,25,48.95147,+60,14,07.0225,296.57,-49.22,6.7,32.81,2.68, 59,  248")
        self._other_names = ['Rucha']

Rucha = DeltaCassiopeiae


class EpsilonCassiopeiae(FixedStar): # ,epsCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCas", context=context, swe_string="Epsilon Cassiopeiae,epsCas,ICRS,01,54,23.72567,+63,40,12.3628,32.09,-18.94,-8.3,7.92,3.37, 62,  320")
        self._other_names = ['Segin']

Segin = EpsilonCassiopeiae


class ZetaCassiopeiae(FixedStar): # ,zetCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCas", context=context, swe_string="Zeta Cassiopeiae,zetCas,ICRS,00,36,58.28419,+53,53,48.8673,17.38,-9.86,-0.2,5.5,3.66, 53,  105")
        self._other_names = ['Fulu']

Fulu = ZetaCassiopeiae


class EtaCassiopeiae(FixedStar): # ,etaCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCas", context=context, swe_string="Eta Cassiopeiae,etaCas,ICRS,00,49,06.29070,+57,48,54.6758,1086.59,-559.43,8.44,167.98,3.44, 57,  150")
        self._other_names = ['Achird']

Achird = EtaCassiopeiae


class KappaCassiopeiae(FixedStar): # ,kapCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapCas", context=context, swe_string="Kappa Cassiopeiae,kapCas,ICRS,00,32,59.99120,+62,55,54.4174,3.65,-2.07,0.3,0.73,4.16, 62,  102")
        self._other_names = []

 = KappaCassiopeiae


class MessierObjectu.Cas(FixedStar): # ,mu.Cas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Cas", context=context, swe_string="Messier Object u.Cas,mu.Cas,ICRS,01,08,16.39470,+54,55,13.2264,3422.23,-1598.93,-98.1,132.38,5.17, 54,  223")
        self._other_names = ['Marfak']

Marfak = MessierObjectu.Cas


class OmicronCassiopeiae(FixedStar): # ,omiCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiCas", context=context, swe_string="Omicron Cassiopeiae,omiCas,ICRS,00,44,43.51867,+48,17,03.7136,18.84,-7.18,-16.9,4.64,4.5, 47,  183")
        self._other_names = []

 = OmicronCassiopeiae


class RhoCassiopeiae(FixedStar): # ,rhoCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoCas", context=context, swe_string="Rho Cassiopeiae,rhoCas,ICRS,23,54,23.03246,+57,29,57.7733,-4.48,-3.73,-54.3,0.28,4.59, 56, 3111")
        self._other_names = []

 = RhoCassiopeiae


class PsiCassiopeiae(FixedStar): # ,psiCas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiCas", context=context, swe_string="Psi Cassiopeiae,psiCas,ICRS,01,25,56.02238,+68,07,48.0460,75.5,26.93,-12.83,16.72,4.727, 67,  123")
        self._other_names = []

 = PsiCassiopeiae


class UpsilonCassiopeiae02(FixedStar): # ,ups02Cas

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ups02Cas", context=context, swe_string="Upsilon Cassiopeiae 02,ups02Cas,ICRS,00,56,39.90501,+59,10,51.7991,-92.65,-45.5,-47.73,16.32,4.622, 0,  0")
        self._other_names = ['Castula']

Castula = UpsilonCassiopeiae02


class AlphaCentauri(FixedStar): # ,alfCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCen", context=context, swe_string="Alpha Centauri,alfCen,ICRS,14,39,36.204,-60,50,08.23,-3608,686,-22.3,742,-0.1,-60, 5483")
        self._other_names = ['Rigil Kentaurus']

RigilKentaurus = AlphaCentauri


class AlphaCentauri(FixedStar): # ,alfCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCen", context=context, swe_string="Alpha Centauri,alfCen,ICRS,14,39,36.204,-60,50,08.23,-3608,686,-22.3,742,-0.1,-60, 5483")
        self._other_names = ['Rigel Kentaurus']

RigelKentaurus = AlphaCentauri


class AlphaCentauri(FixedStar): # ,alfCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCen", context=context, swe_string="Alpha Centauri,alfCen,ICRS,14,39,36.204,-60,50,08.23,-3608,686,-22.3,742,-0.1,-60, 5483")
        self._other_names = ['Toliman']

Toliman = AlphaCentauri


class AlphaCentauri(FixedStar): # ,alfCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCen", context=context, swe_string="Alpha Centauri,alfCen,ICRS,14,39,36.204,-60,50,08.23,-3608,686,-22.3,742,-0.1,-60, 5483")
        self._other_names = ['Bungula']

Bungula = AlphaCentauri


class AlphaCentauri(FixedStar): # ,alfCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCen", context=context, swe_string="Alpha Centauri,alfCen,ICRS,14,39,36.204,-60,50,08.23,-3608,686,-22.3,742,-0.1,-60, 5483")
        self._other_names = ['Proxima Centauri']

ProximaCentauri = AlphaCentauri


class BetaCentauri(FixedStar): # ,betCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCen", context=context, swe_string="Beta Centauri,betCen,ICRS,14,03,49.40535,-60,22,22.9266,-33.27,-23.16,5.9,8.32,0.6,-59, 5365")
        self._other_names = ['Hadar']

Hadar = BetaCentauri


class BetaCentauri(FixedStar): # ,betCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCen", context=context, swe_string="Beta Centauri,betCen,ICRS,14,03,49.40535,-60,22,22.9266,-33.27,-23.16,5.9,8.32,0.6,-59, 5365")
        self._other_names = ['Agena']

Agena = BetaCentauri


class GammaCentauri(FixedStar): # ,gamCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCen", context=context, swe_string="Gamma Centauri,gamCen,ICRS,12,41,31.04008,-48,57,35.5375,-185.72,5.79,-5.5,25.06,2.17,-48, 7597")
        self._other_names = ['Muhlifain']

Muhlifain = GammaCentauri


class DeltaCentauri(FixedStar): # ,delCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCen", context=context, swe_string="Delta Centauri,delCen,ICRS,12,08,21.49764,-50,43,20.7386,-49.94,-7.19,11,7.86,2.52,-50, 6697")
        self._other_names = []

 = DeltaCentauri


class EpsilonCentauri(FixedStar): # ,epsCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCen", context=context, swe_string="Epsilon Centauri,epsCen,ICRS,13,39,53.25774,-53,27,59.0081,-15.3,-11.72,3,7.63,2.3,-52, 6655")
        self._other_names = ['Birdun']

Birdun = EpsilonCentauri


class ZetaCentauri(FixedStar): # ,zetCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCen", context=context, swe_string="Zeta Centauri,zetCen,ICRS,13,55,32.38565,-47,17,18.1482,-57.37,-44.55,6.5,8.54,2.55,-46, 8949")
        self._other_names = []

 = ZetaCentauri


class EtaCentauri(FixedStar): # ,etaCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCen", context=context, swe_string="Eta Centauri,etaCen,ICRS,14,35,30.42416,-42,09,28.1708,-34.73,-32.72,-0.2,10.67,2.31,-41, 8917")
        self._other_names = []

 = EtaCentauri


class ThetaCentauri(FixedStar): # ,tetCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCen", context=context, swe_string="Theta Centauri,tetCen,ICRS,14,06,40.94752,-36,22,11.8371,-520.53,-518.06,1.3,55.45,2.05,-35, 9260")
        self._other_names = ['Menkent']

Menkent = ThetaCentauri


class IotaCentauri(FixedStar): # ,iotCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCen", context=context, swe_string="Iota Centauri,iotCen,ICRS,13,20,35.81737,-36,42,44.2447,-341.11,-86.14,0.1,55.49,2.73,-36, 8497")
        self._other_names = ['Alhakim']

Alhakim = IotaCentauri


class KappaCentauri(FixedStar): # ,kapCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapCen", context=context, swe_string="Kappa Centauri,kapCen,ICRS,14,59,09.68494,-42,06,15.1069,-17.62,-22.51,8,8.51,3.13,-41, 9342")
        self._other_names = ['Ke Kwan']

KeKwan = KappaCentauri


class LambdaCentauri(FixedStar): # ,lamCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamCen", context=context, swe_string="Lambda Centauri,lamCen,ICRS,11,35,46.88530,-63,01,11.4313,-33.41,-7.08,-1.1,7.77,3.14,-62, 2127")
        self._other_names = ['Ma Ti']

MaTi = LambdaCentauri


class LambdaCentauri(FixedStar): # ,lamCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamCen", context=context, swe_string="Lambda Centauri,lamCen,ICRS,11,35,46.88530,-63,01,11.4313,-33.41,-7.08,-1.1,7.77,3.14,-62, 2127")
        self._other_names = ['Mati']

Mati = LambdaCentauri


class MessierObjectu.Cen(FixedStar): # ,mu.Cen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Cen", context=context, swe_string="Messier Object u.Cen,mu.Cen,ICRS,13,49,36.98863,-42,28,25.4296,-24.25,-18.64,9.2,6.45,3.43,-41, 8172")
        self._other_names = []

 = MessierObjectu.Cen


class NuCentauri(FixedStar): # ,nu.Cen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Cen", context=context, swe_string="Nu Centauri,nu.Cen,ICRS,13,49,30.27644,-41,41,15.7521,-26.77,-20.18,9,7.47,3.386,0, 0")
        self._other_names = ['Kabkent Secunda']

KabkentSecunda = NuCentauri


class XiCentauri02(FixedStar): # ,ksi02Cen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksi02Cen", context=context, swe_string="Xi Centauri 02,ksi02Cen,ICRS,13,06,54.63940,-49,54,22.4823,-26.15,-12.03,14.3,6.98,4.27,-49, 7644")
        self._other_names = []

 = XiCentauri02


class PiCentauri(FixedStar): # ,pi.Cen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Cen", context=context, swe_string="Pi Centauri,pi.Cen,ICRS,11,21,00.40615,-54,29,27.6654,-35.85,-1.72,9.4,9.12,3.9,-53, 4498")
        self._other_names = []

 = PiCentauri


class SigmaCentauri(FixedStar): # ,sigCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigCen", context=context, swe_string="Sigma Centauri,sigCen,ICRS,12,28,02.38208,-50,13,50.2872,-32.36,-12.51,8,7.92,3.91,-49, 7115")
        self._other_names = []

 = SigmaCentauri


class PhiCentauri(FixedStar): # ,phiCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiCen", context=context, swe_string="Phi Centauri,phiCen,ICRS,13,58,16.26680,-42,06,02.7143,-22.77,-20.13,5.3,6.21,3.802,0, 0")
        self._other_names = ['Kabkent Tertia']

KabkentTertia = PhiCentauri


class PsiCentauri(FixedStar): # ,psiCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiCen", context=context, swe_string="Psi Centauri,psiCen,ICRS,14,20,33.43229,-37,53,07.0551,-63.69,-10.65,1.8,12.6,4.034,-37, 9336")
        self._other_names = []

 = PsiCentauri


class dCen(FixedStar): # ,dCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dCen", context=context, swe_string="dCen,dCen,ICRS,13,31,02.65660,-39,24,26.2990,-15.67,-10.49,-2.4,3.6,3.88,0,0")
        self._other_names = []

 = dCen


class RhoCentauri(FixedStar): # ,rhoCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoCen", context=context, swe_string="Rho Centauri,rhoCen,ICRS,12,11,39.11770,-52,22,06.4432,-34.92,-16.81,15,8.61,3.96,0,0")
        self._other_names = []

 = RhoCentauri


class ACO3558(FixedStar): # ,ACO3558

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ACO3558", context=context, swe_string="ACO3558,ACO3558,ICRS,13,27,54.8,-31,29,32.0,0.0,0.0,13731,0.0000051,999.99,  0,    0")
        self._other_names = ['Shapley Supercluster']

ShapleySupercluster = ACO3558


class ACO3558(FixedStar): # ,ACO3558

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ACO3558", context=context, swe_string="ACO3558,ACO3558,ICRS,13,27,54.8,-31,29,32.0,0.0,0.0,13731,0.0000051,999.99,  0,    0")
        self._other_names = ['A3558']

A3558 = ACO3558


class AlphaCephei(FixedStar): # ,alfCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCep", context=context, swe_string="Alpha Cephei,alfCep,ICRS,21,18,34.77233,+62,35,08.0681,150.55,49.09,-15.8,66.5,2.46, 61, 2111")
        self._other_names = ['Alderamin']

Alderamin = AlphaCephei


class BetaCephei(FixedStar): # ,betCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCep", context=context, swe_string="Beta Cephei,betCep,ICRS,21,28,39.59685,+70,33,38.5747,12.54,8.39,-8.2,4.76,3.23, 69, 1173")
        self._other_names = ['Alphirk']

Alphirk = BetaCephei


class BetaCephei(FixedStar): # ,betCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCep", context=context, swe_string="Beta Cephei,betCep,ICRS,21,28,39.59685,+70,33,38.5747,12.54,8.39,-8.2,4.76,3.23, 69, 1173")
        self._other_names = ['Alfirk']

Alfirk = BetaCephei


class GammaCephei(FixedStar): # ,gamCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCep", context=context, swe_string="Gamma Cephei,gamCep,ICRS,23,39,20.85153,+77,37,56.1876,-47.96,126.59,-42.82,70.91,3.22, 76,  928")
        self._other_names = ['Alrai']

Alrai = GammaCephei


class GammaCephei(FixedStar): # ,gamCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCep", context=context, swe_string="Gamma Cephei,gamCep,ICRS,23,39,20.85153,+77,37,56.1876,-47.96,126.59,-42.82,70.91,3.22, 76,  928")
        self._other_names = ['Errai']

Errai = GammaCephei


class DeltaCephei(FixedStar): # ,delCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCep", context=context, swe_string="Delta Cephei,delCep,ICRS,22,29,10.26502,+58,24,54.7139,15.35,3.52,-24,3.77,3.75, 57, 2548")
        self._other_names = ['Alradif']

Alradif = DeltaCephei


class DeltaCephei(FixedStar): # ,delCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCep", context=context, swe_string="Delta Cephei,delCep,ICRS,22,29,10.26502,+58,24,54.7139,15.35,3.52,-24,3.77,3.75, 57, 2548")
        self._other_names = ['Alredif']

Alredif = DeltaCephei


class EpsilonCephei(FixedStar): # ,epsCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCep", context=context, swe_string="Epsilon Cephei,epsCep,ICRS,22,15,02.19530,+57,02,36.8771,481.53,46.04,-4.7,38.17,4.19, 0, 0")
        self._other_names = ['Phicares']

Phicares = EpsilonCephei


class EpsilonCephei(FixedStar): # ,epsCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCep", context=context, swe_string="Epsilon Cephei,epsCep,ICRS,22,15,02.19530,+57,02,36.8771,481.53,46.04,-4.7,38.17,4.19, 0, 0")
        self._other_names = ['Phicareus']

Phicareus = EpsilonCephei


class ZetaCephei(FixedStar): # ,zetCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCep", context=context, swe_string="Zeta Cephei,zetCep,ICRS,22,10,51.27691,+58,12,04.5456,13.52,5.24,-17.83,3.9,3.35, 57, 2475")
        self._other_names = ['Kurhah']

Kurhah = ZetaCephei


class EtaCephei(FixedStar): # ,etaCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCep", context=context, swe_string="Eta Cephei,etaCep,ICRS,20,45,17.37555,+61,50,19.6167,86.5,818.02,-87.45,70.1,3.41, 61, 2050")
        self._other_names = ['Alagemin']

Alagemin = EtaCephei


class ThetaCephei(FixedStar): # ,tetCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCep", context=context, swe_string="Theta Cephei,tetCep,ICRS,20,29,34.88506,+62,59,38.7835,45.07,-12.59,-6.8,23.9,4.22, 62, 1821")
        self._other_names = ['Alkidr']

Alkidr = ThetaCephei


class IotaCephei(FixedStar): # ,iotCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCep", context=context, swe_string="Iota Cephei,iotCep,ICRS,22,49,40.81694,+66,12,01.4636,-65.89,-125.17,-12.59,28.29,3.54,65,1814")
        self._other_names = ['Alvahet']

Alvahet = IotaCephei


class KappaCephei(FixedStar): # ,kapCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapCep", context=context, swe_string="Kappa Cephei,kapCep,ICRS,20,08,53.34826,+77,42,41.1151,11.57,24.34,-22.8,10.36,4.4, 77,  764")
        self._other_names = []

 = KappaCephei


class MessierObjectu.Cep(FixedStar): # ,mu.Cep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Cep", context=context, swe_string="Messier Object u.Cep,mu.Cep,ICRS,21,43,30.46106,+58,46,48.1602,5.36,-3.51,23,0.55,4.08, 58, 2316")
        self._other_names = ['Erakis']

Erakis = MessierObjectu.Cep


class MessierObjectu.Cep(FixedStar): # ,mu.Cep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Cep", context=context, swe_string="Messier Object u.Cep,mu.Cep,ICRS,21,43,30.46106,+58,46,48.1602,5.36,-3.51,23,0.55,4.08, 58, 2316")
        self._other_names = ['The Garnet Star']

TheGarnetStar = MessierObjectu.Cep


class NuCephei(FixedStar): # ,nu.Cep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Cep", context=context, swe_string="Nu Cephei,nu.Cep,ICRS,21,45,26.9250,+61,07,14.901,-3.578,-2.006,-25.9,0.48,4.29, 60, 2288")
        self._other_names = []

 = NuCephei


class XiCephei(FixedStar): # ,ksiCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiCep", context=context, swe_string="Xi Cephei,ksiCep,ICRS,22,03,47.45499,+64,37,40.7128,215.46,91.06,-10.74,33.79,6.5, 63, 1802")
        self._other_names = ['Kurdah']

Kurdah = XiCephei


class XiCephei(FixedStar): # ,ksiCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiCep", context=context, swe_string="Xi Cephei,ksiCep,ICRS,22,03,47.45499,+64,37,40.7128,215.46,91.06,-10.74,33.79,6.5, 63, 1802")
        self._other_names = ['Alkurhah']

Alkurhah = XiCephei


class RhoCephei(FixedStar): # ,rhoCep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoCep", context=context, swe_string="Rho Cephei,rhoCep,ICRS,22,29,52.9784,+78,49,27.432,3.417,-20.868,2.8,13.31,5.46, 78,  801")
        self._other_names = ['Al Kalb al Rai']

AlKalbalRai = RhoCephei


class AlphaCeti(FixedStar): # ,alfCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCet", context=context, swe_string="Alpha Ceti,alfCet,ICRS,03,02,16.77307,+04,05,23.0596,-10.41,-76.85,-26.08,13.09,2.53, 03,  419")
        self._other_names = ['Menkar']

Menkar = AlphaCeti


class BetaCeti(FixedStar): # ,betCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCet", context=context, swe_string="Beta Ceti,betCet,ICRS,00,43,35.37090,-17,59,11.7827,232.55,31.99,13.32,33.86,2.01,-18,  115")
        self._other_names = ['Diphda']

Diphda = BetaCeti


class BetaCeti(FixedStar): # ,betCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCet", context=context, swe_string="Beta Ceti,betCet,ICRS,00,43,35.37090,-17,59,11.7827,232.55,31.99,13.32,33.86,2.01,-18,  115")
        self._other_names = ['Difda']

Difda = BetaCeti


class GammaCeti(FixedStar): # ,gamCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCet", context=context, swe_string="Gamma Ceti,gamCet,ICRS,02,43,18.03910,+03,14,08.9390,-146.1,-146.12,-4.9,40.97,3.47, 02,  422")
        self._other_names = ['Kaffaljidhma']

Kaffaljidhma = GammaCeti


class DeltaCeti(FixedStar): # ,delCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCet", context=context, swe_string="Delta Ceti,delCet,ICRS,02,39,28.95579,+00,19,42.6345,12.85,-2.94,13,5.02,4.07,-00,  406")
        self._other_names = ['Phycochroma']

Phycochroma = DeltaCeti


class ZetaCeti(FixedStar): # ,zetCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCet", context=context, swe_string="Zeta Ceti,zetCet,ICRS,01,51,27.63482,-10,20,06.1289,40.8,-37.25,7.8,13.88,3.72,-11,  359")
        self._other_names = ['Baten Kaitos']

BatenKaitos = ZetaCeti


class EtaCeti(FixedStar): # ,etaCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCet", context=context, swe_string="Eta Ceti,etaCet,ICRS,01,08,35.39148,-10,10,56.1570,215.61,-139.02,11.74,26.32,3.45,-10,  240")
        self._other_names = ['Deneb Algenubi']

DenebAlgenubi = EtaCeti


class ThetaCeti(FixedStar): # ,tetCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCet", context=context, swe_string="Theta Ceti,tetCet,ICRS,01,24,01.40528,-08,10,59.7212,-77.94,-206.53,17.2,28.66,3.59,-08,  244")
        self._other_names = ['Altawk']

Altawk = ThetaCeti


class IotaCeti(FixedStar): # ,iotCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCet", context=context, swe_string="Iota Ceti,iotCet,ICRS,00,19,25.67416,-08,49,26.1111,-15.15,-37.11,19.35,11.88,3.55,-09,   48")
        self._other_names = ['Deneb Kaitos']

DenebKaitos = IotaCeti


class IotaCeti(FixedStar): # ,iotCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCet", context=context, swe_string="Iota Ceti,iotCet,ICRS,00,19,25.67416,-08,49,26.1111,-15.15,-37.11,19.35,11.88,3.55,-09,   48")
        self._other_names = ['Shemali']

Shemali = IotaCeti


class LambdaCeti(FixedStar): # ,lamCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamCet", context=context, swe_string="Lambda Ceti,lamCet,ICRS,02,59,42.89987,+08,54,26.4899,6.01,-17.7,10.2,5.66,4.7, 08,  455")
        self._other_names = ['Menkar']

Menkar = LambdaCeti


class MessierObjectu.Cet(FixedStar): # ,mu.Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Cet", context=context, swe_string="Messier Object u.Cet,mu.Cet,ICRS,02,44,56.54098,+10,06,50.9089,282.7,-32.53,30.4,38.8,4.2, 09,  359")
        self._other_names = []

 = MessierObjectu.Cet


class NuCeti(FixedStar): # ,nu.Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Cet", context=context, swe_string="Nu Ceti,nu.Cet,ICRS,02,35,52.47339,+05,35,35.6898,-26.51,-22.32,6.9,9.59,4.871, 04,  418")
        self._other_names = []

 = NuCeti


class XiCeti01(FixedStar): # ,ksi01Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksi01Cet", context=context, swe_string="Xi Ceti 01,ksi01Cet,ICRS,02,12,59.99513,+08,50,48.1584,-26.87,-17.23,-3.93,8.51,4.35, 08,  345")
        self._other_names = []

 = XiCeti01


class XiCeti02(FixedStar): # ,ksi02Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksi02Cet", context=context, swe_string="Xi Ceti 02,ksi02Cet,ICRS,02,28,09.54266,+08,27,36.2007,41.8,-13.55,11.9,16.89,4.3, 07,  388")
        self._other_names = []

 = XiCeti02


class OmicronCeti(FixedStar): # ,omiCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiCet", context=context, swe_string="Omicron Ceti,omiCet,ICRS,02,19,20.79210,-02,58,39.4956,9.33,-237.36,63.5,10.91,6.53,-03,  353")
        self._other_names = ['Mira']

Mira = OmicronCeti


class PiCeti(FixedStar): # ,pi.Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Cet", context=context, swe_string="Pi Ceti,pi.Cet,ICRS,02,44,07.34928,-13,51,31.3130,-8.62,-9.07,14.98,8.3,4.236,-14,  519")
        self._other_names = ['Al Sadr al Ketus']

AlSadralKetus = PiCeti


class RhoCeti(FixedStar): # ,rhoCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoCet", context=context, swe_string="Rho Ceti,rhoCet,ICRS,02,25,57.00560,-12,17,25.7104,-11.28,-9.48,18.9,7.15,4.866,-12,  451")
        self._other_names = []

 = RhoCeti


class SigmaCeti(FixedStar): # ,sigCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigCet", context=context, swe_string="Sigma Ceti,sigCet,ICRS,02,32,05.22884,-15,14,40.8278,-80.21,-146.29,-29.4,37.46,4.75,-15,  449")
        self._other_names = []

 = SigmaCeti


class TauCeti(FixedStar): # ,tauCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauCet", context=context, swe_string="Tau Ceti,tauCet,ICRS,01,44,04.08338,-15,56,14.9262,-1721.05,854.16,-16.68,273.96,3.5,-16,  295")
        self._other_names = []

 = TauCeti


class UpsilonCeti(FixedStar): # ,upsCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsCet", context=context, swe_string="Upsilon Ceti,upsCet,ICRS,02,00,00.30916,-21,04,40.1946,134.92,-24.59,18,11.14,4.02,-21,  358")
        self._other_names = ['Abyssus Aqueus']

AbyssusAqueus = UpsilonCeti


class PhiCeti01(FixedStar): # ,phi01Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phi01Cet", context=context, swe_string="Phi Ceti 01,phi01Cet,ICRS,00,44,11.40013,-10,36,34.3816,-8.96,-113.82,-0.3,13.96,4.767,-11,  153")
        self._other_names = ['Al Nitham']

AlNitham = PhiCeti01


class PhiCeti02(FixedStar): # ,phi02Cet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phi02Cet", context=context, swe_string="Phi Ceti 02,phi02Cet,ICRS,00,50,07.58963,-10,38,39.5835,-226.91,-229.75,8.22,63.48,5.19,-11,  153")
        self._other_names = []

 = PhiCeti02


class ChiCeti(FixedStar): # ,chiCet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiCet", context=context, swe_string="Chi Ceti,chiCet,ICRS,01,49,35.10316,-10,41,11.0674,-148.11,-93.43,-1.8,43.13,4.68,-11,  352")
        self._other_names = []

 = ChiCeti


class AlphaChamaeleontis(FixedStar): # ,alfCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCha", context=context, swe_string="Alpha Chamaeleontis,alfCha,ICRS,08,18,31.55319,-76,55,10.9964,111.12,107.49,-13.4,51.12,4.047,0,0")
        self._other_names = []

 = AlphaChamaeleontis


class BetaChamaeleontis(FixedStar): # ,betCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCha", context=context, swe_string="Beta Chamaeleontis,betCha,ICRS,12,18,20.82459,-79,18,44.0710,-37.97,11.15,23,10.93,4.229,-78,  741")
        self._other_names = []

 = BetaChamaeleontis


class GammaChamaeleontis(FixedStar): # ,gamCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCha", context=context, swe_string="Gamma Chamaeleontis,gamCha,ICRS,10,35,28.10720,-78,36,28.0321,-37.61,11.08,-22.4,7.81,4.12,-77,  622")
        self._other_names = []

 = GammaChamaeleontis


class DeltaChamaeleontis02(FixedStar): # ,del02Cha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del02Cha", context=context, swe_string="Delta Chamaeleontis 02,del02Cha,ICRS,10,45,47.00487,-80,32,24.6785,-36.86,5.9,22.6,9.3,4.433,-79,  556")
        self._other_names = []

 = DeltaChamaeleontis02


class EtaChamaeleontis(FixedStar): # ,etaCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCha", context=context, swe_string="Eta Chamaeleontis,etaCha,ICRS,08,41,19.51346,-78,57,48.0967,-28.89,27.21,14,10.53,5.453,-78,  372")
        self._other_names = []

 = EtaChamaeleontis


class ThetaChamaeleontis(FixedStar): # ,tetCha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCha", context=context, swe_string="Theta Chamaeleontis,tetCha,ICRS,08,20,38.54055,-77,29,04.1173,-129.05,40.89,21.7,21,4.337,-77,  383")
        self._other_names = []

 = ThetaChamaeleontis


class PiChamaeleontis(FixedStar): # ,pi.Cha

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Cha", context=context, swe_string="Pi Chamaeleontis,pi.Cha,ICRS,11,37,15.63631,-75,53,47.5626,-127.94,-1.82,-9.8,24.09,5.637,-75,  744")
        self._other_names = []

 = PiChamaeleontis


class AlphaCircini(FixedStar): # ,alfCir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCir", context=context, swe_string="Alpha Circini,alfCir,ICRS,14,42,30.41958,-64,58,30.4934,-192.53,-233.51,6.2,60.35,3.19,-64, 2977")
        self._other_names = []

 = AlphaCircini


class BetaCircini(FixedStar): # ,betCir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCir", context=context, swe_string="Beta Circini,betCir,ICRS,15,17,30.85016,-58,48,04.3373,-97.74,-134.15,9.6,32.73,4.057,-58, 5875")
        self._other_names = []

 = BetaCircini


class AlphaCanisMajoris(FixedStar): # ,alfCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCMa", context=context, swe_string="Alpha Canis Majoris,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.5,379.21,-1.46,-16, 1591")
        self._other_names = ['Sirius']

Sirius = AlphaCanisMajoris


class AlphaCanisMajoris(FixedStar): # ,alfCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCMa", context=context, swe_string="Alpha Canis Majoris,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.5,379.21,-1.46,-16, 1591")
        self._other_names = ['Lubdhaka']

Lubdhaka = AlphaCanisMajoris


class BetaCanisMajoris(FixedStar): # ,betCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCMa", context=context, swe_string="Beta Canis Majoris,betCMa,ICRS,06,22,41.98535,-17,57,21.3073,-3.23,-0.78,33.7,6.62,1.97,-17, 1467")
        self._other_names = ['Mirzam']

Mirzam = BetaCanisMajoris


class BetaCanisMajoris(FixedStar): # ,betCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCMa", context=context, swe_string="Beta Canis Majoris,betCMa,ICRS,06,22,41.98535,-17,57,21.3073,-3.23,-0.78,33.7,6.62,1.97,-17, 1467")
        self._other_names = ['Murzim']

Murzim = BetaCanisMajoris


class BetaCanisMajoris(FixedStar): # ,betCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCMa", context=context, swe_string="Beta Canis Majoris,betCMa,ICRS,06,22,41.98535,-17,57,21.3073,-3.23,-0.78,33.7,6.62,1.97,-17, 1467")
        self._other_names = ['Murzims']

Murzims = BetaCanisMajoris


class GammaCanisMajoris(FixedStar): # ,gamCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCMa", context=context, swe_string="Gamma Canis Majoris,gamCMa,ICRS,07,03,45.49305,-15,37,59.8300,-0.14,-11.36,32,7.38,4.12,-15, 1625")
        self._other_names = ['Muliphein']

Muliphein = GammaCanisMajoris


class GammaCanisMajoris(FixedStar): # ,gamCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCMa", context=context, swe_string="Gamma Canis Majoris,gamCMa,ICRS,07,03,45.49305,-15,37,59.8300,-0.14,-11.36,32,7.38,4.12,-15, 1625")
        self._other_names = ['Isis']

Isis = GammaCanisMajoris


class DeltaCanisMajoris(FixedStar): # ,delCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCMa", context=context, swe_string="Delta Canis Majoris,delCMa,ICRS,07,08,23.48405,-26,23,35.5185,-3.12,3.31,33.67,2.03,1.84,-26, 3916")
        self._other_names = ['Wezen']

Wezen = DeltaCanisMajoris


class EpsilonCanisMajoris(FixedStar): # ,epsCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCMa", context=context, swe_string="Epsilon Canis Majoris,epsCMa,ICRS,06,58,37.54876,-28,58,19.5102,3.24,1.33,27.3,8.05,1.5,-28, 3666")
        self._other_names = ['Adara']

Adara = EpsilonCanisMajoris


class EpsilonCanisMajoris(FixedStar): # ,epsCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCMa", context=context, swe_string="Epsilon Canis Majoris,epsCMa,ICRS,06,58,37.54876,-28,58,19.5102,3.24,1.33,27.3,8.05,1.5,-28, 3666")
        self._other_names = ['Adhara']

Adhara = EpsilonCanisMajoris


class ZetaCanisMajoris(FixedStar): # ,zetCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCMa", context=context, swe_string="Zeta Canis Majoris,zetCMa,ICRS,06,20,18.79204,-30,03,48.1202,7.32,4.03,32.2,9,3,-30, 3038")
        self._other_names = ['Furud']

Furud = ZetaCanisMajoris


class EtaCanisMajoris(FixedStar): # ,etaCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCMa", context=context, swe_string="Eta Canis Majoris,etaCMa,ICRS,07,24,05.70228,-29,18,11.1798,-4.14,5.81,41.1,1.64,2.45,-29, 4328")
        self._other_names = ['Aludra']

Aludra = EtaCanisMajoris


class KappaCanisMajoris(FixedStar): # ,kapCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapCMa", context=context, swe_string="Kappa Canis Majoris,kapCMa,ICRS,06,49,50.45933,-32,30,30.5225,-8.84,3.73,14,4.95,3.89,-32, 3404")
        self._other_names = []

 = KappaCanisMajoris


class XiCanisMajoris02(FixedStar): # ,ksi02CMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksi02CMa", context=context, swe_string="Xi Canis Majoris 02,ksi02CMa,ICRS,06,35,03.38869,-22,57,53.2375,13.95,18.56,26,7.39,4.5,-22, 1458")
        self._other_names = []

 = XiCanisMajoris02


class OmicronCanisMajoris02(FixedStar): # ,omi02CMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omi02CMa", context=context, swe_string="Omicron Canis Majoris 02,omi02CMa,ICRS,07,03,01.47211,-23,49,59.8523,-2.21,3.61,48.4,1.18,3.02,-23, 4797")
        self._other_names = []

 = OmicronCanisMajoris02


class SigmaCanisMajoris(FixedStar): # ,sigCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigCMa", context=context, swe_string="Sigma Canis Majoris,sigCMa,ICRS,07,01,43.14779,-27,56,05.3898,-5.98,4.59,22.11,2.91,3.47,-27, 3544")
        self._other_names = ['Unurgunite']

Unurgunite = SigmaCanisMajoris


class ThetaCanisMajoris(FixedStar): # ,tetCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCMa", context=context, swe_string="Theta Canis Majoris,tetCMa,ICRS,06,54,11.39877,-12,02,19.0674,-137.26,-15.37,96.2,12.51,4.08,-11, 1681")
        self._other_names = []

 = ThetaCanisMajoris


class AlphaCanisMinors(FixedStar): # ,alfCMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCMi", context=context, swe_string="Alpha Canis Minors,alfCMi,ICRS,07,39,18.11950,+05,13,29.9552,-714.59,-1036.8,-3.2,284.56,0.37, 05, 1739")
        self._other_names = ['Procyon']

Procyon = AlphaCanisMinors


class BetaCanisMinors(FixedStar): # ,betCMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCMi", context=context, swe_string="Beta Canis Minors,betCMi,ICRS,07,27,09.04174,+08,17,21.5368,-51.76,-38.29,22,20.17,2.89, 08, 1774")
        self._other_names = ['Gomeisa']

Gomeisa = BetaCanisMinors


class ZetaCanisMinors(FixedStar): # ,zetCMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCMi", context=context, swe_string="Zeta Canis Minors,zetCMi,ICRS,07,51,41.98835,+01,46,00.7395,-14.43,-2.4,32.3,5.23,5.16, 02, 1808")
        self._other_names = []

 = ZetaCanisMinors


class MessierObject44(FixedStar): # ,M44

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M44", context=context, swe_string="Messier Object 44,M44,2000,08,40,6.000,19,59,0.00,0.000,   0.00,  0.0,5.65,3.7,  0,    0")
        self._other_names = ['Praesepe Cluster']

PraesepeCluster = MessierObject44


class AlphaCancri(FixedStar): # ,alfCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCnc", context=context, swe_string="Alpha Cancri,alfCnc,ICRS,08,58,29.22272,+11,51,27.7212,43.23,-29.63,-12.1,17.32,4.249, 12, 1948")
        self._other_names = ['Acubens']

Acubens = AlphaCancri


class AlphaCancri(FixedStar): # ,alfCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCnc", context=context, swe_string="Alpha Cancri,alfCnc,ICRS,08,58,29.22272,+11,51,27.7212,43.23,-29.63,-12.1,17.32,4.249, 12, 1948")
        self._other_names = ['Ashlesha (Colebrook)']

Ashlesha(Colebrook) = AlphaCancri


class BetaCancri(FixedStar): # ,betCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCnc", context=context, swe_string="Beta Cancri,betCnc,ICRS,08,16,30.92101,+09,11,07.9579,-46.82,-49.24,22.94,10.75,3.52, 09, 1917")
        self._other_names = ['Al Tarf']

AlTarf = BetaCancri


class GammaCancri(FixedStar): # ,gamCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCnc", context=context, swe_string="Gamma Cancri,gamCnc,ICRS,08,43,17.14820,+21,28,06.6008,-103.51,-39.48,28.7,18,4.652, 21, 1895")
        self._other_names = ['Asellus Borealis']

AsellusBorealis = GammaCancri


class DeltaCancri(FixedStar): # ,delCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCnc", context=context, swe_string="Delta Cancri,delCnc,ICRS,08,44,41.09921,+18,09,15.5034,-17.67,-229.26,17.14,24.98,3.94, 18, 2027")
        self._other_names = ['Asellus Australis']

AsellusAustralis = DeltaCancri


class DeltaCancri(FixedStar): # ,delCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCnc", context=context, swe_string="Delta Cancri,delCnc,ICRS,08,44,41.09921,+18,09,15.5034,-17.67,-229.26,17.14,24.98,3.94, 18, 2027")
        self._other_names = ['Pushya']

Pushya = DeltaCancri


class EpsilonCancri(FixedStar): # ,epsCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCnc", context=context, swe_string="Epsilon Cancri,epsCnc,ICRS,08,40,27.0101,+19,32,41.322,-36.274,-11.979,29.9,5.56,6.29, 0,0")
        self._other_names = ['Meleph']

Meleph = EpsilonCancri


class ZetaCancri(FixedStar): # ,zetCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCnc", context=context, swe_string="Zeta Cancri,zetCnc,ICRS,08,12,12.71,+17,38,53.3,27.61,-151.73,-7.93,39.87,4.67, 18, 1867")
        self._other_names = ['Tegmen']

Tegmen = ZetaCancri


class ZetaCancri(FixedStar): # ,zetCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCnc", context=context, swe_string="Zeta Cancri,zetCnc,ICRS,08,12,12.71,+17,38,53.3,27.61,-151.73,-7.93,39.87,4.67, 18, 1867")
        self._other_names = ['Tegmine']

Tegmine = ZetaCancri


class EtaCancri(FixedStar): # ,etaCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCnc", context=context, swe_string="Eta Cancri,etaCnc,ICRS,08,32,42.49600,+20,26,28.1865,-46.33,-44.31,22.46,10.93,5.325, 20, 2109")
        self._other_names = []

 = EtaCancri


class IotaCancri(FixedStar): # ,iotCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCnc", context=context, swe_string="Iota Cancri,iotCnc,ICRS,08,46,41.81988,+28,45,35.6190,-21.58,-45.69,15.74,9.85,4.018, 29, 1824")
        self._other_names = ['Decapoda']

Decapoda = IotaCancri


class KappaCancri(FixedStar): # ,kapCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapCnc", context=context, swe_string="Kappa Cancri,kapCnc,ICRS,09,07,44.81176,+10,40,05.4933,-21.24,-9.28,24.5,6.14,5.24, 11, 1984")
        self._other_names = []

 = KappaCancri


class XiCancri(FixedStar): # ,ksiCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiCnc", context=context, swe_string="Xi Cancri,ksiCnc,ICRS,09,09,21.53325,+22,02,43.6053,-1,-0.52,-7.7,8.74,5.149, 22, 2061")
        self._other_names = []

 = XiCancri


class SigmaCancri03(FixedStar): # ,sig03Cnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sig03Cnc", context=context, swe_string="Sigma Cancri 03,sig03Cnc,ICRS,08,59,32.65432,+32,25,06.8093,-43.78,-35.03,20.82,11.03,5.22, 32, 1821")
        self._other_names = []

 = SigmaCancri03


class ChiCancri(FixedStar): # ,chiCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiCnc", context=context, swe_string="Chi Cancri,chiCnc,ICRS,08,20,03.86158,+27,13,03.7416,-16.36,-376.65,32.91,54.73,5.1, 27, 1589")
        self._other_names = []

 = ChiCancri


class OmegaCancri01(FixedStar): # ,ome01Cnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome01Cnc", context=context, swe_string="Omega Cancri 01,ome01Cnc,ICRS,08,00,55.8730,+25,23,34.215,16.652,7.18,1.9,4.92,5.853, 25, 1812")
        self._other_names = []

 = OmegaCancri01


class Cancri55(FixedStar): # ,55Cnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",55Cnc", context=context, swe_string="Cancri55,55Cnc,ICRS,08,52,35.81093,+28,19,50.9511,-485.8,-234.05,27.58,81.03,5.95, 0,0")
        self._other_names = ['Copernicus']

Copernicus = Cancri55


class AlphaColumbae(FixedStar): # ,alfCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCol", context=context, swe_string="Alpha Columbae,alfCol,ICRS,05,39,38.94103,-34,04,26.7950,1.58,-24.82,35,12.48,2.65,-34, 2375")
        self._other_names = ['Phact']

Phact = AlphaColumbae


class BetaColumbae(FixedStar): # ,betCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCol", context=context, swe_string="Beta Columbae,betCol,ICRS,05,50,57.59220,-35,46,05.9152,54.77,404.2,89.4,37.41,3.12,-35, 2546")
        self._other_names = ['Wazn']

Wazn = BetaColumbae


class DeltaColumbae(FixedStar): # ,delCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCol", context=context, swe_string="Delta Columbae,delCol,ICRS,06,22,06.82831,-33,26,11.0323,-24.23,-51.4,-2.6,13.94,3.85,0, 0")
        self._other_names = ['Ghusn al Zaitun']

GhusnalZaitun = DeltaColumbae


class GammaColumbae(FixedStar): # ,gamCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCol", context=context, swe_string="Gamma Columbae,gamCol,ICRS,05,57,32.20958,-35,16,59.8153,-3.24,10.21,24.2,3.75,4.36,-35, 2612")
        self._other_names = []

 = GammaColumbae


class EtaColumbae(FixedStar): # ,etaCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCol", context=context, swe_string="Eta Columbae,etaCol,ICRS,05,59,08.80519,-42,48,54.4822,18.39,-10.87,17,6.91,3.96,-42, 2266")
        self._other_names = []

 = EtaColumbae


class KappaColumbae(FixedStar): # ,kapCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapCol", context=context, swe_string="Kappa Columbae,kapCol,ICRS,06,16,33.13512,-35,08,25.8630,-0.28,87.94,24.2,17.87,4.37,-35, 2800")
        self._other_names = ['Al Kurud']

AlKurud = KappaColumbae


class LambdaColumbae(FixedStar): # ,lamCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamCol", context=context, swe_string="Lambda Columbae,lamCol,ICRS,05,53,06.88101,-33,48,04.9079,-4.72,31.32,30,9.75,4.87,-33, 2599")
        self._other_names = ['Tsze']

Tsze = LambdaColumbae


class OmicronColumbae(FixedStar): # ,omiCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiCol", context=context, swe_string="Omicron Columbae,omiCol,ICRS,05,17,29.08929,-34,53,42.7444,92.67,-336.23,21.1,30.82,4.83,-35, 2214")
        self._other_names = []

 = OmicronColumbae


class EpsilonColumbae(FixedStar): # ,epsCol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCol", context=context, swe_string="Epsilon Columbae,epsCol,ICRS,05,31,12.75540,-35,28,13.8730,27.9,-34.72,-4.9,12.39,3.87,0,0")
        self._other_names = []

 = EpsilonColumbae


class AlphaComaeBerenices(FixedStar): # ,alfCom

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCom", context=context, swe_string="Alpha Comae Berenices,alfCom,ICRS,13,09,59.28520,+17,31,46.0389,-433.13,141.24,-16.05,56.1,4.32, 18, 2697")
        self._other_names = ['Diadem']

Diadem = AlphaComaeBerenices


class BetaComaeBerenices(FixedStar): # ,betCom

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCom", context=context, swe_string="Beta Comae Berenices,betCom,ICRS,13,11,52.39379,+27,52,41.4535,-801.44,882.04,5.46,109.54,4.25, 28, 2193")
        self._other_names = ['Aldafirah']

Aldafirah = BetaComaeBerenices


class GammaComaeBerenices(FixedStar): # ,gamCom

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCom", context=context, swe_string="Gamma Comae Berenices,gamCom,ICRS,12,26,56.27207,+28,16,06.3211,-83.95,-81.13,3.38,19.5,4.34, 29, 2288")
        self._other_names = ['Kissin']

Kissin = GammaComaeBerenices


class AlphaCoronaeBorealis(FixedStar): # ,alfCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCrB", context=context, swe_string="Alpha Coronae Borealis,alfCrB,ICRS,15,34,41.26800,+26,42,52.8940,120.27,-89.58,1.7,43.46,2.24, 27, 2512")
        self._other_names = ['Alphecca']

Alphecca = AlphaCoronaeBorealis


class AlphaCoronaeBorealis(FixedStar): # ,alfCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCrB", context=context, swe_string="Alpha Coronae Borealis,alfCrB,ICRS,15,34,41.26800,+26,42,52.8940,120.27,-89.58,1.7,43.46,2.24, 27, 2512")
        self._other_names = ['Alphekka']

Alphekka = AlphaCoronaeBorealis


class AlphaCoronaeBorealis(FixedStar): # ,alfCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCrB", context=context, swe_string="Alpha Coronae Borealis,alfCrB,ICRS,15,34,41.26800,+26,42,52.8940,120.27,-89.58,1.7,43.46,2.24, 27, 2512")
        self._other_names = ['Gemma']

Gemma = AlphaCoronaeBorealis


class BetaCoronaeBorealis(FixedStar): # ,betCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCrB", context=context, swe_string="Beta Coronae Borealis,betCrB,ICRS,15,27,49.73153,+29,06,20.5224,-180.17,85.92,-26.9,29.17,3.68, 29, 2670")
        self._other_names = ['Nusakan']

Nusakan = BetaCoronaeBorealis


class EpsilonCoronaeBorealis(FixedStar): # ,epsCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCrB", context=context, swe_string="Epsilon Coronae Borealis,epsCrB,ICRS,15,57,35.25147,+26,52,40.3635,-77.07,-60.61,-32.42,14.73,4.13, 27, 2558")
        self._other_names = []

 = EpsilonCoronaeBorealis


class ThetaCoronaeBorealis(FixedStar): # ,tetCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCrB", context=context, swe_string="Theta Coronae Borealis,tetCrB,ICRS,15,32,55.78214,+31,21,32.8762,-20.15,-9.39,-25.7,8.69,4.13, 31, 2750")
        self._other_names = []

 = ThetaCoronaeBorealis


class KappaCoronaeBorealis(FixedStar): # ,kapCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapCrB", context=context, swe_string="Kappa Coronae Borealis,kapCrB,ICRS,15,51,13.93127,+35,39,26.5671,-8.55,-348.44,-25.16,32.79,4.82, 36, 2652")
        self._other_names = []

 = KappaCoronaeBorealis


class tCrB(FixedStar): # ,tCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tCrB", context=context, swe_string="tCrB,tCrB,ICRS,15,59,30.16221,+25,55,12.6130,-4.46,12.016,-27.79,1.09,10.8,0,0")
        self._other_names = ['Blaze Star']

BlazeStar = tCrB


class TauCoronaeBorealis(FixedStar): # ,tauCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauCrB", context=context, swe_string="Tau Coronae Borealis,tauCrB,ICRS,16,08,58.30151,+36,29,27.3740,-37.02,340.44,-18.4,27.95,4.76, 36, 2699")
        self._other_names = []

 = TauCoronaeBorealis


class GammaCoronaeBorealis(FixedStar): # ,gamCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCrB", context=context, swe_string="Gamma Coronae Borealis,gamCrB,ICRS,15,42,44.56551,+26,17,44.2847,-111.65,49.52,-12.1,22.33,3.84,0,0")
        self._other_names = []

 = GammaCoronaeBorealis


class DeltaCoronaeBorealis(FixedStar): # ,delCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCrB", context=context, swe_string="Delta Coronae Borealis,delCrB,ICRS,15,49,35.64682,+26,04,06.2065,-78.83,-65.28,-20.36,19.18,4.63,0,0")
        self._other_names = []

 = DeltaCoronaeBorealis


class IotaCoronaeBorealis(FixedStar): # ,iotCrB

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCrB", context=context, swe_string="Iota Coronae Borealis,iotCrB,ICRS,16,01,26.56488,+29,51,03.8243,-38.31,-6.56,-20.8,10.46,4.971,0,0")
        self._other_names = []

 = IotaCoronaeBorealis


class AlphaCoronaeAustralis(FixedStar): # ,alfCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCrA", context=context, swe_string="Alpha Coronae Australis,alfCrA,ICRS,19,09,28.34097,-37,54,16.1022,84.87,-95.99,-18.4,26.02,4.087,-38,13350")
        self._other_names = ['Alfecca Meridiana']

AlfeccaMeridiana = AlphaCoronaeAustralis


class AlphaCoronaeAustralis(FixedStar): # ,alfCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCrA", context=context, swe_string="Alpha Coronae Australis,alfCrA,ICRS,19,09,28.34097,-37,54,16.1022,84.87,-95.99,-18.4,26.02,4.087,-38,13350")
        self._other_names = ['Meridiana']

Meridiana = AlphaCoronaeAustralis


class EtaCoronaeAustralis01(FixedStar): # ,eta01CrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eta01CrA", context=context, swe_string="Eta Coronae Australis 01,eta01CrA,ICRS,18,48,50.48994,-43,40,48.1591,23.89,-19.32,-4,9.7,5.456,-43,12841")
        self._other_names = []

 = EtaCoronaeAustralis01


class ThetaCoronaeAustralis(FixedStar): # ,tetCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCrA", context=context, swe_string="Theta Coronae Australis,tetCrA,ICRS,18,33,30.18626,-42,18,45.0335,33.27,-20.72,-2.1,5.85,4.614,-42,13378")
        self._other_names = []

 = ThetaCoronaeAustralis


class EpsilonCoronaeAustralis(FixedStar): # ,epsCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCrA", context=context, swe_string="Epsilon Coronae Australis,epsCrA,ICRS,18,58,43.37714,-37,06,26.4865,-132.4,-110.62,57.9,33.13,4.83,0,0")
        self._other_names = []

 = EpsilonCoronaeAustralis


class GammaCoronaeAustralis(FixedStar): # ,gamCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCrA", context=context, swe_string="Gamma Coronae Australis,gamCrA,ICRS,19,06,25.11014,-37,03,48.3901,96.74,-281.71,-51.6,57.79,4.2,0,0")
        self._other_names = []

 = GammaCoronaeAustralis


class BetaCoronaeAustralis(FixedStar): # ,betCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCrA", context=context, swe_string="Beta Coronae Australis,betCrA,ICRS,19,10,01.75580,-39,20,26.8644,4.37,-36.65,2.7,6.88,4.095,0,0")
        self._other_names = []

 = BetaCoronaeAustralis


class DeltaCoronaeAustralis(FixedStar): # ,delCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCrA", context=context, swe_string="Delta Coronae Australis,delCrA,ICRS,19,08,20.96867,-40,29,48.1248,46.49,-26.18,20.3,18.27,4.571,0,0")
        self._other_names = []

 = DeltaCoronaeAustralis


class ZetaCoronaeAustralis(FixedStar): # ,zetCrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCrA", context=context, swe_string="Zeta Coronae Australis,zetCrA,ICRS,19,03,06.87698,-42,05,42.3858,56.41,-46.43,-13,16.89,4.725,0,0")
        self._other_names = []

 = ZetaCoronaeAustralis


class AlphaCraters(FixedStar): # ,alfCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCrt", context=context, swe_string="Alpha Craters,alfCrt,ICRS,10,59,46.46486,-18,17,55.6172,-462.26,129.49,47.54,20.49,4.07,-17, 3273")
        self._other_names = ['Alkes']

Alkes = AlphaCraters


class BetaCraters(FixedStar): # ,betCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCrt", context=context, swe_string="Beta Craters,betCrt,ICRS,11,11,39.48783,-22,49,33.0593,2.52,-100.22,5.6,9.59,4.449,-22, 3095")
        self._other_names = ['Alsharasif']

Alsharasif = BetaCraters


class GammaCraters(FixedStar): # ,gamCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCrt", context=context, swe_string="Gamma Craters,gamCrt,ICRS,11,24,52.92362,-17,41,02.4300,-97.42,3.65,1,39.62,4.08,-16, 3244")
        self._other_names = []

 = GammaCraters


class DeltaCraters(FixedStar): # ,delCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCrt", context=context, swe_string="Delta Craters,delCrt,ICRS,11,19,20.44756,-14,46,42.7413,-124.67,207.59,-4.94,17.56,3.56,-13, 3345")
        self._other_names = ['Labrum']

Labrum = DeltaCraters


class EpsilonCraters(FixedStar): # ,epsCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCrt", context=context, swe_string="Epsilon Craters,epsCrt,ICRS,11,24,36.59019,-10,51,33.5591,-25.65,24.96,2,8.67,4.802,0, 0")
        self._other_names = []

 = EpsilonCraters


class EtaCraters(FixedStar): # ,etaCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCrt", context=context, swe_string="Eta Craters,etaCrt,ICRS,11,56,00.95323,-17,09,02.9781,-49.74,-7.58,15,12.97,5.16,-16, 3358")
        self._other_names = []

 = EtaCraters


class ThetaCraters(FixedStar): # ,tetCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCrt", context=context, swe_string="Theta Craters,tetCrt,ICRS,11,36,40.91335,-09,48,08.0912,-59.38,2.55,1,11.63,4.673,-08, 3202")
        self._other_names = []

 = ThetaCraters


class ZetaCraters(FixedStar): # ,zetCrt

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCrt", context=context, swe_string="Zeta Craters,zetCrt,ICRS,11,44,45.77615,-18,21,02.4298,27.79,-24.86,-4.1,9.24,4.706,-17, 3460")
        self._other_names = []

 = ZetaCraters


class AlphaCrucis(FixedStar): # ,alfCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCru", context=context, swe_string="Alpha Crucis,alfCru,ICRS,12,26,35.89522,-63,05,56.7343,-35.83,-14.86,11.9,10.13,0.81,-62, 2745 # binary star system")
        self._other_names = ['Acrux']

Acrux = AlphaCrucis


class BetaCrucis(FixedStar): # ,betCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCru", context=context, swe_string="Beta Crucis,betCru,ICRS,12,47,43.26877,-59,41,19.5792,-42.97,-16.18,10.3,11.71,1.25,-59, 4451")
        self._other_names = ['Mimosa']

Mimosa = BetaCrucis


class GammaCrucis(FixedStar): # ,gamCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCru", context=context, swe_string="Gamma Crucis,gamCru,ICRS,12,31,09.95961,-57,06,47.5684,28.23,-265.08,21,36.83,1.64,-56, 5272")
        self._other_names = ['Gacrux']

Gacrux = GammaCrucis


class DeltaCrucis(FixedStar): # ,delCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCru", context=context, swe_string="Delta Crucis,delCru,ICRS,12,15,08.71673,-58,44,56.1369,-35.81,-10.36,22.2,9.45,2.752,-58, 4189")
        self._other_names = ['Decrux']

Decrux = DeltaCrucis


class EpsilonCrucis(FixedStar): # ,epsCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCru", context=context, swe_string="Epsilon Crucis,epsCru,ICRS,12,21,21.60936,-60,24,04.1291,-170.93,91.67,-4.6,14.19,3.59,0, 0")
        self._other_names = ['Juxta Crucem']

JuxtaCrucem = EpsilonCrucis


class EpsilonCrucis(FixedStar): # ,epsCru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCru", context=context, swe_string="Epsilon Crucis,epsCru,ICRS,12,21,21.60936,-60,24,04.1291,-170.93,91.67,-4.6,14.19,3.59,0, 0")
        self._other_names = ['Ginan']

Ginan = EpsilonCrucis


class AlphaCorvi(FixedStar): # ,alfCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCrv", context=context, swe_string="Alpha Corvi,alfCrv,ICRS,12,08,24.81652,-24,43,43.9504,99.52,-39.19,2.8,66.95,4,-24,10174")
        self._other_names = ['Alchiba']

Alchiba = AlphaCorvi


class AlphaCorvi(FixedStar): # ,alfCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCrv", context=context, swe_string="Alpha Corvi,alfCrv,ICRS,12,08,24.81652,-24,43,43.9504,99.52,-39.19,2.8,66.95,4,-24,10174")
        self._other_names = ['Alchita']

Alchita = AlphaCorvi


class BetaCorvi(FixedStar): # ,betCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCrv", context=context, swe_string="Beta Corvi,betCrv,ICRS,12,34,23.23484,-23,23,48.3374,1.11,-56.56,-7.34,22.39,2.64,-22, 3401")
        self._other_names = ['Kraz']

Kraz = BetaCorvi


class GammaCorvi(FixedStar): # ,gamCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCrv", context=context, swe_string="Gamma Corvi,gamCrv,ICRS,12,15,48.37081,-17,32,30.9496,-158.61,21.86,-4.2,21.23,2.58,-16, 3424")
        self._other_names = ['Gienah']

Gienah = GammaCorvi


class GammaCorvi(FixedStar): # ,gamCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCrv", context=context, swe_string="Gamma Corvi,gamCrv,ICRS,12,15,48.37081,-17,32,30.9496,-158.61,21.86,-4.2,21.23,2.58,-16, 3424")
        self._other_names = ['Gienah Corvi']

GienahCorvi = GammaCorvi


class DeltaCorvi(FixedStar): # ,delCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCrv", context=context, swe_string="Delta Corvi,delCrv,ICRS,12,29,51.85517,-16,30,55.5525,-210.49,-138.74,13.9,37.55,2.94,-15, 3482")
        self._other_names = ['Algorab']

Algorab = DeltaCorvi


class DeltaCorvi(FixedStar): # ,delCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCrv", context=context, swe_string="Delta Corvi,delCrv,ICRS,12,29,51.85517,-16,30,55.5525,-210.49,-138.74,13.9,37.55,2.94,-15, 3482")
        self._other_names = ['Hasta']

Hasta = DeltaCorvi


class EpsilonCorvi(FixedStar): # ,epsCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCrv", context=context, swe_string="Epsilon Corvi,epsCrv,ICRS,12,10,07.48058,-22,37,11.1620,-71.74,10.25,5,10.26,2.98,-21, 3487")
        self._other_names = ['Minkar']

Minkar = EpsilonCorvi


class EtaCorvi(FixedStar): # ,etaCrv

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCrv", context=context, swe_string="Eta Corvi,etaCrv,ICRS,12,32,04.22653,-16,11,45.6165,-425.17,-57.23,-2.8,54.7,4.31,0, 0")
        self._other_names = ['Avis Satyra']

AvisSatyra = EtaCorvi


class AlphaCanumVenaticorum02(FixedStar): # ,alf02CVn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf02CVn", context=context, swe_string="Alpha Canum Venaticorum 02,alf02CVn,ICRS,12,56,01.66622,+38,19,06.1541,-235.08,53.54,-4.1,28.41,2.88, 39, 2580")
        self._other_names = ['Cor Caroli']

CorCaroli = AlphaCanumVenaticorum02


class BetaCanumVenaticorum(FixedStar): # ,betCVn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCVn", context=context, swe_string="Beta Canum Venaticorum,betCVn,ICRS,12,33,44.54482,+41,21,26.9248,-704.75,292.74,6.52,118.49,4.25, 42, 2321")
        self._other_names = ['Asterion']

Asterion = BetaCanumVenaticorum


class BetaCanumVenaticorum(FixedStar): # ,betCVn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCVn", context=context, swe_string="Beta Canum Venaticorum,betCVn,ICRS,12,33,44.54482,+41,21,26.9248,-704.75,292.74,6.52,118.49,4.25, 42, 2321")
        self._other_names = ['Chara']

Chara = BetaCanumVenaticorum


class AlphaCygni(FixedStar): # ,alfCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCyg", context=context, swe_string="Alpha Cygni,alfCyg,ICRS,20,41,25.91514,+45,16,49.2197,2.01,1.85,-4.9,2.31,1.25, 44, 3541")
        self._other_names = ['Deneb']

Deneb = AlphaCygni


class BetaCygni01(FixedStar): # ,bet01Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet01Cyg", context=context, swe_string="Beta Cygni 01,bet01Cyg,ICRS,19,30,43.28052,+27,57,34.8483,-7.17,-6.15,-24.07,7.51,3.085, 27, 3410")
        self._other_names = ['Albireo']

Albireo = BetaCygni01


class GammaCygni(FixedStar): # ,gamCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCyg", context=context, swe_string="Gamma Cygni,gamCyg,ICRS,20,22,13.70184,+40,15,24.0450,2.39,-0.91,-6.4,1.78,2.23, 39, 4159")
        self._other_names = ['Sador']

Sador = GammaCygni


class GammaCygni(FixedStar): # ,gamCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCyg", context=context, swe_string="Gamma Cygni,gamCyg,ICRS,20,22,13.70184,+40,15,24.0450,2.39,-0.91,-6.4,1.78,2.23, 39, 4159")
        self._other_names = ['Sadir']

Sadir = GammaCygni


class GammaCygni(FixedStar): # ,gamCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCyg", context=context, swe_string="Gamma Cygni,gamCyg,ICRS,20,22,13.70184,+40,15,24.0450,2.39,-0.91,-6.4,1.78,2.23, 39, 4159")
        self._other_names = ['Sadr']

Sadr = GammaCygni


class DeltaCygni(FixedStar): # ,delCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCyg", context=context, swe_string="Delta Cygni,delCyg,ICRS,19,44,58.47854,+45,07,50.9161,44.07,48.66,-23.6,19.77,2.87, 0, 0")
        self._other_names = ['Ruc']

Ruc = DeltaCygni


class DeltaCygni(FixedStar): # ,delCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCyg", context=context, swe_string="Delta Cygni,delCyg,ICRS,19,44,58.47854,+45,07,50.9161,44.07,48.66,-23.6,19.77,2.87, 0, 0")
        self._other_names = ['Rukh']

Rukh = DeltaCygni


class DeltaCygni(FixedStar): # ,delCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCyg", context=context, swe_string="Delta Cygni,delCyg,ICRS,19,44,58.47854,+45,07,50.9161,44.07,48.66,-23.6,19.77,2.87, 0, 0")
        self._other_names = ['Urakhga']

Urakhga = DeltaCygni


class DeltaCygni(FixedStar): # ,delCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCyg", context=context, swe_string="Delta Cygni,delCyg,ICRS,19,44,58.47854,+45,07,50.9161,44.07,48.66,-23.6,19.77,2.87, 0, 0")
        self._other_names = ['Al Fawaris']

AlFawaris = DeltaCygni


class EpsilonCygni(FixedStar): # ,epsCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCyg", context=context, swe_string="Epsilon Cygni,epsCyg,ICRS,20,46,12.68236,+33,58,12.9250,355.66,330.6,-12.41,44.86,2.48, 33, 4018")
        self._other_names = ['Gienah Cygni']

GienahCygni = EpsilonCygni


class EpsilonCygni(FixedStar): # ,epsCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCyg", context=context, swe_string="Epsilon Cygni,epsCyg,ICRS,20,46,12.68236,+33,58,12.9250,355.66,330.6,-12.41,44.86,2.48, 33, 4018")
        self._other_names = ['Gienah Ghurab']

GienahGhurab = EpsilonCygni


class EpsilonCygni(FixedStar): # ,epsCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCyg", context=context, swe_string="Epsilon Cygni,epsCyg,ICRS,20,46,12.68236,+33,58,12.9250,355.66,330.6,-12.41,44.86,2.48, 33, 4018")
        self._other_names = ['Aljanah']

Aljanah = EpsilonCygni


class ZetaCygni(FixedStar): # ,zetCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetCyg", context=context, swe_string="Zeta Cygni,zetCyg,ICRS,21,12,56.18594,+30,13,36.8957,6.51,-68.21,16.72,22.79,3.21, 29, 4348")
        self._other_names = []

 = ZetaCygni


class EtaCygni(FixedStar): # ,etaCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCyg", context=context, swe_string="Eta Cygni,etaCyg,ICRS,19,56,18.37222,+35,05,00.3228,-33.61,-27.87,-25.87,24.17,3.88, 34, 3798")
        self._other_names = []

 = EtaCygni


class ThetaCygni(FixedStar): # ,tetCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetCyg", context=context, swe_string="Theta Cygni,tetCyg,ICRS,19,36,26.53436,+50,13,15.9646,-8.87,262.45,-26.9,54.54,4.48, 49, 3062")
        self._other_names = []

 = ThetaCygni


class IotaCygni02(FixedStar): # ,iot02Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iot02Cyg", context=context, swe_string="Iota Cygni 02,iot02Cyg,ICRS,19,29,42.35872,+51,43,47.2058,20.59,128.33,-19.5,26.88,3.755, 51, 2605")
        self._other_names = []

 = IotaCygni02


class KappaCygni(FixedStar): # ,kapCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapCyg", context=context, swe_string="Kappa Cygni,kapCyg,ICRS,19,17,06.16865,+53,22,06.4534,60.07,122.83,-29.36,26.27,3.76, 53, 2216")
        self._other_names = []

 = KappaCygni


class NuCygni(FixedStar): # ,nu.Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Cyg", context=context, swe_string="Nu Cygni,nu.Cyg,ICRS,20,57,10.41907,+41,10,01.6991,9.64,-22.75,-27.6,8.71,3.94, 40, 4364")
        self._other_names = []

 = NuCygni


class XiCygni(FixedStar): # ,ksiCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiCyg", context=context, swe_string="Xi Cygni,ksiCyg,ICRS,21,04,55.86229,+43,55,40.2644,7.97,0.06,-19.1,3.87,3.73, 43, 3800")
        self._other_names = []

 = XiCygni


class PiCygni01(FixedStar): # ,pi.01Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.01Cyg", context=context, swe_string="Pi Cygni 01,pi.01Cyg,ICRS,21,42,05.66458,+51,11,22.6415,5.29,-1.78,-8.2,1.89,4.66, 50, 3410")
        self._other_names = ['Azelfafage']

Azelfafage = PiCygni01


class PiCygni02(FixedStar): # ,pi.02Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.02Cyg", context=context, swe_string="Pi Cygni 02,pi.02Cyg,ICRS,21,46,47.60832,+49,18,34.4511,2.77,-2,-12.3,2.95,4.18, 48, 3504")
        self._other_names = []

 = PiCygni02


class RhoCygni(FixedStar): # ,rhoCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoCyg", context=context, swe_string="Rho Cygni,rhoCyg,ICRS,21,33,58.85298,+45,35,30.6179,-23.79,-93.7,6.88,26.39,4.02, 44, 3865")
        self._other_names = []

 = RhoCygni


class SigmaCygni(FixedStar): # ,sigCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigCyg", context=context, swe_string="Sigma Cygni,sigCyg,ICRS,21,17,24.95244,+39,23,40.8528,-0.13,-3.58,-5.3,1.13,4.24, 38, 4431")
        self._other_names = []

 = SigmaCygni


class UpsilonCygni(FixedStar): # ,upsCyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsCyg", context=context, swe_string="Upsilon Cygni,upsCyg,ICRS,21,17,55.07506,+34,53,48.8289,10.03,6.49,-0.7,5.08,4.42, 34, 4371")
        self._other_names = []

 = UpsilonCygni


class OmegaCygni01(FixedStar): # ,ome01Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome01Cyg", context=context, swe_string="Omega Cygni 01,ome01Cyg,ICRS,20,30,03.54116,+48,57,05.6446,10.63,7.22,-21.9,3.59,4.936, 48, 3142")
        self._other_names = ['Ruchbah I']

RuchbahI = OmegaCygni01


class OmegaCygni02(FixedStar): # ,ome02Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome02Cyg", context=context, swe_string="Omega Cygni 02,ome02Cyg,ICRS,20,31,18.81663,+49,13,13.0656,9.21,-31.88,-64.15,8.17,5.44, 48, 3154")
        self._other_names = ['Ruchbah II']

RuchbahII = OmegaCygni02


class Cygni61(FixedStar): # ,61Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",61Cyg", context=context, swe_string="Cygni61,61Cyg,ICRS,21,06,53.95249,+38,44,57.9854,4168.31,3269.2,-65.74,286.82,4.84, 38, 4343")
        self._other_names = []

 = Cygni61


class Cygni34(FixedStar): # ,34Cyg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",34Cyg", context=context, swe_string="Cygni34,34Cyg,ICRS,20,17,47.20208,+38,01,58.5527,-3.18,-6.45,-8.9,0.32,4.8,0,0")
        self._other_names = []

 = Cygni34


class AlphaDelphini(FixedStar): # ,alfDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfDel", context=context, swe_string="Alpha Delphini,alfDel,ICRS,20,39,38.28720,+15,54,43.4637,53.82,8.47,-3.4,12.85,3.8, 15, 4222")
        self._other_names = ['Sualocin']

Sualocin = AlphaDelphini


class BetaDelphini(FixedStar): # ,betDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betDel", context=context, swe_string="Beta Delphini,betDel,ICRS,20,37,32.94130,+14,35,42.3195,118.09,-48.06,-22.7,32.33,3.63, 14, 4369")
        self._other_names = ['Rotanev']

Rotanev = BetaDelphini


class BetaDelphini(FixedStar): # ,betDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betDel", context=context, swe_string="Beta Delphini,betDel,ICRS,20,37,32.94130,+14,35,42.3195,118.09,-48.06,-22.7,32.33,3.63, 14, 4369")
        self._other_names = ['Dhanishtha']

Dhanishtha = BetaDelphini


class BetaDelphini(FixedStar): # ,betDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betDel", context=context, swe_string="Beta Delphini,betDel,ICRS,20,37,32.94130,+14,35,42.3195,118.09,-48.06,-22.7,32.33,3.63, 14, 4369")
        self._other_names = ['Shravishtha']

Shravishtha = BetaDelphini


class GammaDelphini02(FixedStar): # ,gam02Del

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam02Del", context=context, swe_string="Gamma Delphini 02,gam02Del,ICRS,20,46,39.50341,+16,07,27.4403,-24.17,-199.96,-6.15,25.82,4.27, 15, 4255")
        self._other_names = []

 = GammaDelphini02


class DeltaDelphini(FixedStar): # ,delDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delDel", context=context, swe_string="Delta Delphini,delDel,ICRS,20,43,27.53338,+15,04,28.4773,-20.44,-43.33,9.3,14.61,4.417, 14, 4403")
        self._other_names = []

 = DeltaDelphini


class EpsilonDelphini(FixedStar): # ,epsDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsDel", context=context, swe_string="Epsilon Delphini,epsDel,ICRS,20,33,12.77192,+11,18,11.7412,11.96,-28.97,-19.4,9.87,4.03, 10, 4321")
        self._other_names = ['Deneb Dulphim']

DenebDulphim = EpsilonDelphini


class EpsilonDelphini(FixedStar): # ,epsDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsDel", context=context, swe_string="Epsilon Delphini,epsDel,ICRS,20,33,12.77192,+11,18,11.7412,11.96,-28.97,-19.4,9.87,4.03, 10, 4321")
        self._other_names = ['Aldulfin']

Aldulfin = EpsilonDelphini


class KappaDelphini(FixedStar): # ,kapDel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapDel", context=context, swe_string="Kappa Delphini,kapDel,ICRS,20,39,07.78430,+10,05,10.3383,323.83,21.8,-54.37,33.2,5.05, 09, 4600")
        self._other_names = []

 = KappaDelphini


class Delphini18(FixedStar): # ,18Del

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",18Del", context=context, swe_string="Delphini18,18Del,ICRS,20,58,25.93397,+10,50,21.4289,-48.75,-34.43,3.81,13.28,5.506, 0,0")
        self._other_names = ['Musica']

Musica = Delphini18


class AlphaDoradus(FixedStar): # ,alfDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfDor", context=context, swe_string="Alpha Doradus,alfDor,ICRS,04,33,59.77719,-55,02,41.9243,57.75,10.93,25.6,19.34,3.28,-55,  663")
        self._other_names = []

 = AlphaDoradus


class BetaDoradus(FixedStar): # ,betDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betDor", context=context, swe_string="Beta Doradus,betDor,ICRS,05,33,37.51729,-62,29,23.3692,0.79,12.74,7.2,3.24,3.76,-62,  487")
        self._other_names = []

 = BetaDoradus


class GammaDoradus(FixedStar): # ,gamDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamDor", context=context, swe_string="Gamma Doradus,gamDor,ICRS,04,16,01.58584,-51,29,11.9405,100.79,183.32,25.2,48.87,4.2,-51, 1066")
        self._other_names = []

 = GammaDoradus


class DeltaDoradus(FixedStar): # ,delDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delDor", context=context, swe_string="Delta Doradus,delDor,ICRS,05,44,46.37811,-65,44,07.9011,-28.91,5.17,-8.3,21.8,4.36,-65,  496")
        self._other_names = []

 = DeltaDoradus


class ZetaDoradus(FixedStar): # ,zetDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetDor", context=context, swe_string="Zeta Doradus,zetDor,ICRS,05,05,30.65677,-57,28,21.7362,-30.97,117.22,-1.3,85.87,4.708,-57,  735")
        self._other_names = []

 = ZetaDoradus


class ThetaDoradus(FixedStar): # ,tetDor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetDor", context=context, swe_string="Theta Doradus,tetDor,ICRS,05,13,45.4549,-67,11,06.927,18.71,37.949,10.5,6.64,4.801,-67,  401")
        self._other_names = []

 = ThetaDoradus


class NuDoradus(FixedStar): # ,nu.Dor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Dor", context=context, swe_string="Nu Doradus,nu.Dor,ICRS,06,08,44.26199,-68,50,36.2797,-50.84,19.01,17,10.88,5.038,-68,  474")
        self._other_names = []

 = NuDoradus


class SN1987A(FixedStar): # ,SN1987A

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SN1987A", context=context, swe_string="SN1987A,SN1987A,ICRS,05,35,28.020,-69,16,11.07,0.0,0.0,270,19.46,4.81, 0,    0")
        self._other_names = ['Sanduleak']

Sanduleak = SN1987A


class AlphaDraconis(FixedStar): # ,alfDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfDra", context=context, swe_string="Alpha Draconis,alfDra,ICRS,14,04,23.34995,+64,22,33.0619,-56.34,17.21,-13,10.76,3.68, 65,  978")
        self._other_names = ['Thuban']

Thuban = AlphaDraconis


class AlphaDraconis(FixedStar): # ,alfDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfDra", context=context, swe_string="Alpha Draconis,alfDra,ICRS,14,04,23.34995,+64,22,33.0619,-56.34,17.21,-13,10.76,3.68, 65,  978")
        self._other_names = ['Dhruva']

Dhruva = AlphaDraconis


class BetaDraconis(FixedStar): # ,betDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betDra", context=context, swe_string="Beta Draconis,betDra,ICRS,17,30,25.96170,+52,18,04.9993,-15.89,12.28,-21,8.58,2.81, 52, 2065")
        self._other_names = ['Alwaid']

Alwaid = BetaDraconis


class BetaDraconis(FixedStar): # ,betDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betDra", context=context, swe_string="Beta Draconis,betDra,ICRS,17,30,25.96170,+52,18,04.9993,-15.89,12.28,-21,8.58,2.81, 52, 2065")
        self._other_names = ['Rastaban']

Rastaban = BetaDraconis


class GammaDraconis(FixedStar): # ,gamDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamDra", context=context, swe_string="Gamma Draconis,gamDra,ICRS,17,56,36.36988,+51,29,20.0242,-8.48,-22.79,-27.91,21.14,2.23, 51, 2282")
        self._other_names = ['Eltanin']

Eltanin = GammaDraconis


class GammaDraconis(FixedStar): # ,gamDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamDra", context=context, swe_string="Gamma Draconis,gamDra,ICRS,17,56,36.36988,+51,29,20.0242,-8.48,-22.79,-27.91,21.14,2.23, 51, 2282")
        self._other_names = ['Etamin']

Etamin = GammaDraconis


class DeltaDraconis(FixedStar): # ,delDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delDra", context=context, swe_string="Delta Draconis,delDra,ICRS,19,12,33.30197,+67,39,41.5456,95.74,91.92,24.71,33.48,3.07, 67, 1129")
        self._other_names = ['Nodus II']

NodusII = DeltaDraconis


class DeltaDraconis(FixedStar): # ,delDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delDra", context=context, swe_string="Delta Draconis,delDra,ICRS,19,12,33.30197,+67,39,41.5456,95.74,91.92,24.71,33.48,3.07, 67, 1129")
        self._other_names = ['Altais']

Altais = DeltaDraconis


class EpsilonDraconis(FixedStar): # ,epsDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsDra", context=context, swe_string="Epsilon Draconis,epsDra,ICRS,19,48,10.35080,+70,16,04.5492,79.31,39.08,2.69,22.04,3.84, 69, 1070")
        self._other_names = ['Tyl']

Tyl = EpsilonDraconis


class ZetaDraconis(FixedStar): # ,zetDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetDra", context=context, swe_string="Zeta Draconis,zetDra,ICRS,17,08,47.19596,+65,42,52.8634,-20.43,19.61,-17.7,9.93,3.17, 65, 1170")
        self._other_names = ['Nodus I']

NodusI = ZetaDraconis


class ZetaDraconis(FixedStar): # ,zetDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetDra", context=context, swe_string="Zeta Draconis,zetDra,ICRS,17,08,47.19596,+65,42,52.8634,-20.43,19.61,-17.7,9.93,3.17, 65, 1170")
        self._other_names = ['Aldhibah']

Aldhibah = ZetaDraconis


class ThetaDraconis(FixedStar): # ,tetDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetDra", context=context, swe_string="Theta Draconis,tetDra,ICRS,16,01,53.34636,+58,33,54.9056,-319.51,334.97,-8.23,47.54,4, 58, 1608")
        self._other_names = []

 = ThetaDraconis


class IotaDraconis(FixedStar): # ,iotDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotDra", context=context, swe_string="Iota Draconis,iotDra,ICRS,15,24,55.77463,+58,57,57.8344,-8.36,17.08,-10.71,32.23,3.29, 59, 1654")
        self._other_names = ['Edasich']

Edasich = IotaDraconis


class IotaDraconis(FixedStar): # ,iotDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotDra", context=context, swe_string="Iota Draconis,iotDra,ICRS,15,24,55.77463,+58,57,57.8344,-8.36,17.08,-10.71,32.23,3.29, 59, 1654")
        self._other_names = ['Ed Asich']

EdAsich = IotaDraconis


class KappaDraconis(FixedStar): # ,kapDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapDra", context=context, swe_string="Kappa Draconis,kapDra,ICRS,12,33,28.94325,+69,47,17.6490,-58.79,10.68,-12,6.65,3.89, 70,  703")
        self._other_names = ['Ketu']

Ketu = KappaDraconis


class LambdaDraconis(FixedStar): # ,lamDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamDra", context=context, swe_string="Lambda Draconis,lamDra,ICRS,11,31,24.22075,+69,19,51.8696,-40.97,-19.19,6.6,9.79,3.85, 70,  665")
        self._other_names = ['Giansar']

Giansar = LambdaDraconis


class LambdaDraconis(FixedStar): # ,lamDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamDra", context=context, swe_string="Lambda Draconis,lamDra,ICRS,11,31,24.22075,+69,19,51.8696,-40.97,-19.19,6.6,9.79,3.85, 70,  665")
        self._other_names = ['Giausar']

Giausar = LambdaDraconis


class LambdaDraconis(FixedStar): # ,lamDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamDra", context=context, swe_string="Lambda Draconis,lamDra,ICRS,11,31,24.22075,+69,19,51.8696,-40.97,-19.19,6.6,9.79,3.85, 70,  665")
        self._other_names = ['Gianfar']

Gianfar = LambdaDraconis


class MessierObjectu.Dra(FixedStar): # ,mu.Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Dra", context=context, swe_string="Messier Object u.Dra,mu.Dra,ICRS,17,05,20.12403,+54,28,12.0994,-58.16,67.87,-17.3,36.45,4.92, 54, 1857")
        self._other_names = ['Arrakis']

Arrakis = MessierObjectu.Dra


class MessierObjectu.Dra(FixedStar): # ,mu.Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Dra", context=context, swe_string="Messier Object u.Dra,mu.Dra,ICRS,17,05,20.12403,+54,28,12.0994,-58.16,67.87,-17.3,36.45,4.92, 54, 1857")
        self._other_names = ['Alrakis']

Alrakis = MessierObjectu.Dra


class NuDraconis01(FixedStar): # ,nu.01Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.01Dra", context=context, swe_string="Nu Draconis 01,nu.01Dra,ICRS,17,32,10.56856,+55,11,03.2739,147.39,54.31,-15.2,33.06,4.867, 55, 1944")
        self._other_names = ['Kuma']

Kuma = NuDraconis01


class NuDraconis02(FixedStar): # ,nu.02Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.02Dra", context=context, swe_string="Nu Draconis 02,nu.02Dra,ICRS,17,32,16.02464,+55,10,22.6504,142.65,62.43,-16,32.8,4.833, 55, 1945")
        self._other_names = ['Kuma']

Kuma = NuDraconis02


class XiDraconis(FixedStar): # ,ksiDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiDra", context=context, swe_string="Xi Draconis,ksiDra,ICRS,17,53,31.72962,+56,52,21.5143,93.82,78.5,-26.46,28.98,3.75, 56, 2033")
        self._other_names = ['Grumium']

Grumium = XiDraconis


class OmicronDraconis(FixedStar): # ,omiDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiDra", context=context, swe_string="Omicron Draconis,omiDra,ICRS,18,51,12.09530,+59,23,18.0627,77.47,25.37,-19.52,9.54,4.636, 59, 1925")
        self._other_names = []

 = OmicronDraconis


class SigmaDraconis(FixedStar): # ,sigDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigDra", context=context, swe_string="Sigma Draconis,sigDra,ICRS,19,32,21.5899,+69,39,40.236,597.482,-1738.313,26.78,173.77,4.68, 69, 1053")
        self._other_names = ['Alsafi']

Alsafi = SigmaDraconis


class SigmaDraconis(FixedStar): # ,sigDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigDra", context=context, swe_string="Sigma Draconis,sigDra,ICRS,19,32,21.5899,+69,39,40.236,597.482,-1738.313,26.78,173.77,4.68, 69, 1053")
        self._other_names = ['Athafi']

Athafi = SigmaDraconis


class TauDraconis(FixedStar): # ,tauDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauDra", context=context, swe_string="Tau Draconis,tauDra,ICRS,19,15,33.05868,+73,21,19.6769,-115.29,103.23,-33.7,22.28,4.45, 73,  857")
        self._other_names = []

 = TauDraconis


class UpsilonDraconis(FixedStar): # ,upsDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsDra", context=context, swe_string="Upsilon Draconis,upsDra,ICRS,18,54,23.85632,+71,17,49.8906,49.53,42.11,-11.1,9.48,4.814, 71,  915")
        self._other_names = []

 = UpsilonDraconis


class ChiDraconis(FixedStar): # ,chiDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiDra", context=context, swe_string="Chi Draconis,chiDra,ICRS,18,21,03.38255,+72,43,58.2518,531.21,-349.71,31.9,124.11,3.58, 72,  839")
        self._other_names = ['Batentaban Borealis']

BatentabanBorealis = ChiDraconis


class PsiDraconis01(FixedStar): # ,psi01Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psi01Dra", context=context, swe_string="Psi Draconis 01,psi01Dra,ICRS,17,41,56.35536,+72,08,55.8481,25.32,-268.47,-13.3,43.79,4.56, 72,  804")
        self._other_names = ['Dziban']

Dziban = PsiDraconis01


class OmegaDraconis(FixedStar): # ,omeDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeDra", context=context, swe_string="Omega Draconis,omeDra,ICRS,17,36,57.09403,+68,45,28.6961,2.58,321.73,-13.98,43.17,4.8, 68,  949")
        self._other_names = []

 = OmegaDraconis


class EtaDraconis(FixedStar): # ,etaDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaDra", context=context, swe_string="Eta Draconis,etaDra,ICRS,16,23,59.48594,+61,30,51.1699,-17.02,56.95,-15.2,35.42,2.74, 0,  0")
        self._other_names = ['Aldhibain']

Aldhibain = EtaDraconis


class EtaDraconis(FixedStar): # ,etaDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaDra", context=context, swe_string="Eta Draconis,etaDra,ICRS,16,23,59.48594,+61,30,51.1699,-17.02,56.95,-15.2,35.42,2.74, 0,  0")
        self._other_names = ['Athebyne']

Athebyne = EtaDraconis


class PhiDraconis(FixedStar): # ,phiDra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiDra", context=context, swe_string="Phi Draconis,phiDra,ICRS,18,20,45.43224,+71,20,16.1499,-5.03,37.86,-16,10.77,4.22, 0,  0")
        self._other_names = ['Batentaban Australis']

BatentabanAustralis = PhiDraconis


class Draconis7(FixedStar): # ,7Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",7Dra", context=context, swe_string="Draconis7,7Dra,ICRS,12,47,34.3489,+66,47,25.086,5.089,-5.74,11.33,4.4,5.423, 0,0")
        self._other_names = ['Tianyi']

Tianyi = Draconis7


class Draconis8(FixedStar): # ,8Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",8Dra", context=context, swe_string="Draconis8,8Dra,ICRS,12,55,28.54827,+65,26,18.5073,-4.8,-30.09,9,34.14,5.225, 0,0")
        self._other_names = ['Taiyi']

Taiyi = Draconis8


class Draconis42(FixedStar): # ,42Dra

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",42Dra", context=context, swe_string="Draconis42,42Dra,ICRS,18,25,59.1383795957,+65,33,48.503958394,105.248,-25.104,31.79,11.0061,4.823, 0,0")
        self._other_names = ['Fafnir']

Fafnir = Draconis42


class AlphaEquulei(FixedStar): # ,alfEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfEqu", context=context, swe_string="Alpha Equulei,alfEqu,ICRS,21,15,49.43192,+05,14,52.2430,59.88,-94.09,-16.26,17.14,3.933, 04, 4635")
        self._other_names = ['Kitalpha']

Kitalpha = AlphaEquulei


class GammaEquulei(FixedStar): # ,gamEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamEqu", context=context, swe_string="Gamma Equulei,gamEqu,ICRS,21,10,20.50005,+10,07,53.6763,48.74,-153.03,-16.5,27.55,4.68, 09, 4732")
        self._other_names = []

 = GammaEquulei


class DeltaEquulei(FixedStar): # ,delEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delEqu", context=context, swe_string="Delta Equulei,delEqu,ICRS,21,14,28.81531,+10,00,25.1259,42.39,-304.19,-15.85,54.41,4.49,0,0")
        self._other_names = []

 = DeltaEquulei


class BetaEquulei(FixedStar): # ,betEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betEqu", context=context, swe_string="Beta Equulei,betEqu,ICRS,21,22,53.61344,+06,48,40.1070,53.98,11.34,-11.1,9.86,5.148,0,0")
        self._other_names = []

 = BetaEquulei


class AlphaEridani(FixedStar): # ,alfEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfEri", context=context, swe_string="Alpha Eridani,alfEri,ICRS,01,37,42.84548,-57,14,12.3101,87,-38.24,18.6,23.39,0.46,-57,  334")
        self._other_names = ['Achernar']

Achernar = AlphaEridani


class BetaEridani(FixedStar): # ,betEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betEri", context=context, swe_string="Beta Eridani,betEri,ICRS,05,07,50.98549,-05,05,11.2055,-82.82,-75.39,-6,36.5,2.79,-05, 1162")
        self._other_names = ['Cursa']

Cursa = BetaEridani


class GammaEridani(FixedStar): # ,gamEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamEri", context=context, swe_string="Gamma Eridani,gamEri,ICRS,03,58,01.76695,-13,30,30.6698,61.57,-113.11,60.81,16.04,2.94,-13,  781")
        self._other_names = ['Zaurak']

Zaurak = GammaEridani


class DeltaEridani(FixedStar): # ,delEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delEri", context=context, swe_string="Delta Eridani,delEri,ICRS,03,43,14.90088,-09,45,48.2084,-93.16,743.64,-6.28,110.61,3.54,-10,  728")
        self._other_names = ['Rana']

Rana = DeltaEridani


class EpsilonEridani(FixedStar): # ,epsEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsEri", context=context, swe_string="Epsilon Eridani,epsEri,ICRS,03,32,55.84496,-09,27,29.7312,-975.17,19.49,16.43,310.94,3.73,-09,  697")
        self._other_names = ['Ran']

Ran = EpsilonEridani


class EtaEridani(FixedStar): # ,etaEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaEri", context=context, swe_string="Eta Eridani,etaEri,ICRS,02,56,25.64948,-08,53,53.3221,77.36,-220.16,-20.32,23.89,3.87,-09,  553")
        self._other_names = ['Azha']

Azha = EtaEridani


class ThetaEridani01(FixedStar): # ,tet01Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet01Eri", context=context, swe_string="Theta Eridani 01,tet01Eri,ICRS,02,58,15.715,-40,18,17.03,-44.6,19,11.9,28,3.18,-40,  771")
        self._other_names = ['Acamar']

Acamar = ThetaEridani01


class ZetaEridani(FixedStar): # ,zetEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetEri", context=context, swe_string="Zeta Eridani,zetEri,ICRS,03,15,50.02656,-08,49,11.0220,-0.35,46.1,-5.8,29.72,4.8,-09,  624")
        self._other_names = ['Zibal']

Zibal = ZetaEridani


class IotaEridani(FixedStar): # ,iotEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotEri", context=context, swe_string="Iota Eridani,iotEri,ICRS,02,40,40.03501,-39,51,19.3541,135.92,-27.53,-9.3,21.65,4.116,-40,  689")
        self._other_names = []

 = IotaEridani


class KappaEridani(FixedStar): # ,kapEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapEri", context=context, swe_string="Kappa Eridani,kapEri,ICRS,02,26,59.12177,-47,42,13.8247,19.32,-5.54,25.5,6.42,4.25,-48,  637")
        self._other_names = []

 = KappaEridani


class LambdaEridani(FixedStar): # ,lamEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamEri", context=context, swe_string="Lambda Eridani,lamEri,ICRS,05,09,08.78315,-08,45,14.6908,0.25,-1.97,2,4.02,4.27,-08, 1040")
        self._other_names = []

 = LambdaEridani


class MessierObjectu.Eri(FixedStar): # ,mu.Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Eri", context=context, swe_string="Messier Object u.Eri,mu.Eri,ICRS,04,45,30.15038,-03,15,16.7765,15.94,-14.52,23.3,6.25,4,-03,  876")
        self._other_names = []

 = MessierObjectu.Eri


class NuEridani(FixedStar): # ,nu.Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Eri", context=context, swe_string="Nu Eridani,nu.Eri,ICRS,04,36,19.14144,-03,21,08.8567,1.53,-5.01,14.9,4.83,3.928,-03,  834")
        self._other_names = []

 = NuEridani


class XiEridani(FixedStar): # ,ksiEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiEri", context=context, swe_string="Xi Eridani,ksiEri,ICRS,04,23,40.85270,-03,44,43.6771,-47.36,-54.91,-4.5,15.6,5.165,-04,  818")
        self._other_names = []

 = XiEridani


class OmicronEridani01(FixedStar): # ,omi01Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omi01Eri", context=context, swe_string="Omicron Eridani 01,omi01Eri,ICRS,04,11,51.93956,-06,50,15.2864,10.76,81.92,11,26.8,4.026,-07,  764")
        self._other_names = ['Beid']

Beid = OmicronEridani01


class OmicronEridani02(FixedStar): # ,omi02Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omi02Eri", context=context, swe_string="Omicron Eridani 02,omi02Eri,ICRS,04,15,16.31963,-07,39,10.3404,-2240.12,-3420.27,-42.32,200.62,4.43,-07,  780")
        self._other_names = ['Keid']

Keid = OmicronEridani02


class PhiEridani(FixedStar): # ,phiEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiEri", context=context, swe_string="Phi Eridani,phiEri,ICRS,02,16,30.58563,-51,30,43.7955,91.03,-22.23,10.4,21.22,3.57,-52,  285")
        self._other_names = []

 = PhiEridani


class TauEridani01(FixedStar): # ,tau01Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau01Eri", context=context, swe_string="Tau Eridani 01,tau01Eri,ICRS,02,45,06.18710,-18,34,21.2149,334.2,37.19,25.9,70.32,4.46,0,0")
        self._other_names = []

 = TauEridani01


class TauEridani02(FixedStar): # ,tau02Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau02Eri", context=context, swe_string="Tau Eridani 02,tau02Eri,ICRS,02,51,02.32186,-21,00,14.4654,-38.52,-16.05,-5.9,17.45,4.77,-21,  509")
        self._other_names = ['Angetenar']

Angetenar = TauEridani02


class TauEridani03(FixedStar): # ,tau03Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau03Eri", context=context, swe_string="Tau Eridani 03,tau03Eri,ICRS,03,02,23.49939,-23,37,28.0936,-147.25,-55.28,-9.8,36.8,4.09,-24, 1387")
        self._other_names = []

 = TauEridani03


class TauEridani04(FixedStar): # ,tau04Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau04Eri", context=context, swe_string="Tau Eridani 04,tau04Eri,ICRS,03,19,31.00224,-21,45,28.3049,51.89,32.92,41.7,10.71,3.7,0,0")
        self._other_names = []

 = TauEridani04


class TauEridani05(FixedStar): # ,tau05Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau05Eri", context=context, swe_string="Tau Eridani 05,tau05Eri,ICRS,03,33,47.27613,-21,37,58.3830,44.94,-28.16,14,11.12,4.3,-22,  628")
        self._other_names = []

 = TauEridani05


class TauEridani06(FixedStar): # ,tau06Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau06Eri", context=context, swe_string="Tau Eridani 06,tau06Eri,ICRS,03,46,50.88819,-23,14,59.0046,-158.84,-528.95,7.98,56.73,4.2,-23, 1565")
        self._other_names = []

 = TauEridani06


class TauEridani08(FixedStar): # ,tau08Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau08Eri", context=context, swe_string="Tau Eridani 08,tau08Eri,ICRS,03,53,42.70302,-24,36,44.0309,31.28,-7.49,20.5,8.65,4.623,0,0")
        self._other_names = []

 = TauEridani08


class TauEridani09(FixedStar): # ,tau09Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau09Eri", context=context, swe_string="Tau Eridani 09,tau09Eri,ICRS,03,59,55.48381,-24,00,58.3798,12.12,16.48,25.5,9.96,4.66,0,0")
        self._other_names = []

 = TauEridani09


class UpsilonEridani01(FixedStar): # ,ups01Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ups01Eri", context=context, swe_string="Upsilon Eridani 01,ups01Eri,ICRS,04,33,30.55236,-29,45,59.3725,-114.78,-271.79,20.6,25.67,4.51,0,0")
        self._other_names = []

 = UpsilonEridani01


class UpsilonEridani02(FixedStar): # ,ups02Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ups02Eri", context=context, swe_string="Upsilon Eridani 02,ups02Eri,ICRS,04,35,33.03834,-30,33,44.4297,-49.27,-12.72,-4,15.25,3.82,-30, 1901")
        self._other_names = ['Theemin']

Theemin = UpsilonEridani02


class UpsilonEridani03(FixedStar): # ,ups03Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ups03Eri", context=context, swe_string="Upsilon Eridani 03,ups03Eri,ICRS,04,24,02.21725,-34,01,00.6542,73.77,56.7,24.1,11.01,3.96,0,0")
        self._other_names = ['Beemim']

Beemim = UpsilonEridani03


class UpsilonEridani04(FixedStar): # ,ups04Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ups04Eri", context=context, swe_string="Upsilon Eridani 04,ups04Eri,ICRS,04,17,53.66241,-33,47,54.0569,62.52,-7.24,17.6,18.33,3.56,0,0")
        self._other_names = []

 = UpsilonEridani04


class ChiEridani(FixedStar): # ,chiEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiEri", context=context, swe_string="Chi Eridani,chiEri,ICRS,01,55,57.47212,-51,36,32.0325,680.92,283.46,-6.3,56.02,3.7,-52,  241")
        self._other_names = []

 = ChiEridani


class Eridani53(FixedStar): # ,53Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",53Eri", context=context, swe_string="Eridani53,53Eri,ICRS,04,38,10.82486,-14,18,14.4600,-76.59,-176.78,43.33,29.69,3.87,-14,  933")
        self._other_names = ['Sceptrum']

Sceptrum = Eridani53


class OmegaEridani(FixedStar): # ,omeEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeEri", context=context, swe_string="Omega Eridani,omeEri,ICRS,04,52,53.66995,-05,27,09.6972,-17.86,25.57,-6,13.88,4.4,0,0")
        self._other_names = []

 = OmegaEridani


class PiEridani(FixedStar): # ,pi.Eri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Eri", context=context, swe_string="Pi Eridani,pi.Eri,ICRS,03,46,08.53581,-12,06,05.7282,55.98,59.28,45.2,6.78,4.42,0,0")
        self._other_names = []

 = PiEridani


class gEri(FixedStar): # ,gEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gEri", context=context, swe_string="gEri,gEri,ICRS,03,49,27.24528,-36,12,00.9041,-49.18,-57.01,2,15.54,4.17,0,0")
        self._other_names = []

 = gEri


class fEri(FixedStar): # ,fEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",fEri", context=context, swe_string="fEri,fEri,ICRS,03,48,35.87724,-37,37,12.5415,74.44,-9.09,15.60,19.71,4.26,0,0")
        self._other_names = []

 = fEri


class yEri(FixedStar): # ,yEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",yEri", context=context, swe_string="yEri,yEri,ICRS,02,05,34.18860,-57,08,38.9719,24.8,3.59,0,2.21,10.68,0,0")
        self._other_names = []

 = yEri


class eEri(FixedStar): # ,eEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eEri", context=context, swe_string="eEri,eEri,ICRS,03,19,55.65093,-43,04,11.2175,3038.34,726.58,87.4,165.47,4.27,0,0")
        self._other_names = []

 = eEri


class sEri(FixedStar): # ,sEri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sEri", context=context, swe_string="sEri,sEri,ICRS,04,59,55.73677,-12,32,14.6983,39.67,-87.04,-8.9,11.24,4.77,0,0")
        self._other_names = []

 = sEri


class AlphaFornacis(FixedStar): # ,alfFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfFor", context=context, swe_string="Alpha Fornacis,alfFor,ICRS,03,12,04.52736,-28,59,15.4336,370.87,611.33,-17.14,70.24,3.85,-29, 1177")
        self._other_names = ['Fornacis']

Fornacis = AlphaFornacis


class AlphaFornacis(FixedStar): # ,alfFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfFor", context=context, swe_string="Alpha Fornacis,alfFor,ICRS,03,12,04.52736,-28,59,15.4336,370.87,611.33,-17.14,70.24,3.85,-29, 1177")
        self._other_names = ['Dalim']

Dalim = AlphaFornacis


class BetaFornacis(FixedStar): # ,betFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betFor", context=context, swe_string="Beta Fornacis,betFor,ICRS,02,49,05.41885,-32,24,21.2319,86.01,158.81,16.8,18.89,4.46,-32, 1025")
        self._other_names = []

 = BetaFornacis


class DeltaFornacis(FixedStar): # ,delFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delFor", context=context, swe_string="Delta Fornacis,delFor,ICRS,03,42,14.90248,-31,56,18.1055,4.8,13.64,26,3.85,4.973,-32, 1430")
        self._other_names = []

 = DeltaFornacis


class KappaFornacis(FixedStar): # ,kapFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapFor", context=context, swe_string="Kappa Fornacis,kapFor,ICRS,02,22,32.54641,-23,48,58.7791,196.61,-4.98,16.7,45.53,5.19,-24, 1038")
        self._other_names = []

 = KappaFornacis


class LambdaFornacis01(FixedStar): # ,lam01For

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lam01For", context=context, swe_string="Lambda Fornacis 01,lam01For,ICRS,02,33,07.02628,-34,38,59.8890,-17.81,-18.82,13,8.94,5.889,-35,  877")
        self._other_names = []

 = LambdaFornacis01


class MessierObjectu.For(FixedStar): # ,mu.For

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.For", context=context, swe_string="Messier Object u.For,mu.For,ICRS,02,12,54.46962,-30,43,25.7732,14.1,6.85,10,10.18,5.26,-31,  882")
        self._other_names = []

 = MessierObjectu.For


class NuFornacis(FixedStar): # ,nu.For

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.For", context=context, swe_string="Nu Fornacis,nu.For,ICRS,02,04,29.43861,-29,17,48.5477,12.79,8.48,18.5,8.79,4.69,-29,  706")
        self._other_names = []

 = NuFornacis


class TauFornacis(FixedStar): # ,tauFor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauFor", context=context, swe_string="Tau Fornacis,tauFor,ICRS,03,38,47.6714,-27,56,34.991,21.16,26.295,39,8.49,6.01,-28, 1225")
        self._other_names = []

 = TauFornacis


class AlphaGeminorum(FixedStar): # ,alfGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfGem", context=context, swe_string="Alpha Geminorum,alfGem,ICRS,07,34,35.87319,+31,53,17.8160,-191.45,-145.19,5.4,64.12,1.58, 32, 1581")
        self._other_names = ['Castor']

Castor = AlphaGeminorum


class BetaGeminorum(FixedStar): # ,betGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betGem", context=context, swe_string="Beta Geminorum,betGem,ICRS,07,45,18.94987,+28,01,34.3160,-626.55,-45.8,3.23,96.54,1.14, 28, 1463")
        self._other_names = ['Pollux']

Pollux = BetaGeminorum


class BetaGeminorum(FixedStar): # ,betGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betGem", context=context, swe_string="Beta Geminorum,betGem,ICRS,07,45,18.94987,+28,01,34.3160,-626.55,-45.8,3.23,96.54,1.14, 28, 1463")
        self._other_names = ['Punarvasu']

Punarvasu = BetaGeminorum


class GammaGeminorum(FixedStar): # ,gamGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamGem", context=context, swe_string="Gamma Geminorum,gamGem,ICRS,06,37,42.71050,+16,23,57.4095,13.81,-54.96,-12.63,29.84,1.92, 16, 1223")
        self._other_names = ['Alhena']

Alhena = GammaGeminorum


class GammaGeminorum(FixedStar): # ,gamGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamGem", context=context, swe_string="Gamma Geminorum,gamGem,ICRS,06,37,42.71050,+16,23,57.4095,13.81,-54.96,-12.63,29.84,1.92, 16, 1223")
        self._other_names = ['Almeisan']

Almeisan = GammaGeminorum


class DeltaGeminorum(FixedStar): # ,delGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delGem", context=context, swe_string="Delta Geminorum,delGem,ICRS,07,20,07.37978,+21,58,56.3377,-15.13,-9.79,4.1,53.94,3.53, 22, 1645")
        self._other_names = ['Wasat']

Wasat = DeltaGeminorum


class EpsilonGeminorum(FixedStar): # ,epsGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsGem", context=context, swe_string="Epsilon Geminorum,epsGem,ICRS,06,43,55.92626,+25,07,52.0515,-5.57,-12.36,7.77,3.86,2.98, 25, 1406")
        self._other_names = ['Mebsuta']

Mebsuta = EpsilonGeminorum


class ZetaGeminorum(FixedStar): # ,zetGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetGem", context=context, swe_string="Zeta Geminorum,zetGem,ICRS,07,04,06.53079,+20,34,13.0739,-7.29,-0.41,2.8,2.37,3.79, 20, 1687")
        self._other_names = ['Mekbuda']

Mekbuda = ZetaGeminorum


class EtaGeminorum(FixedStar): # ,etaGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaGem", context=context, swe_string="Eta Geminorum,etaGem,ICRS,06,14,52.65715,+22,30,24.4596,-62.46,-12.12,22.39,8.48,3.28, 22, 1241")
        self._other_names = ['Propus']

Propus = EtaGeminorum


class EtaGeminorum(FixedStar): # ,etaGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaGem", context=context, swe_string="Eta Geminorum,etaGem,ICRS,06,14,52.65715,+22,30,24.4596,-62.46,-12.12,22.39,8.48,3.28, 22, 1241")
        self._other_names = ['Propus etaGem']

PropusetaGem = EtaGeminorum


class ThetaGeminorum(FixedStar): # ,tetGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetGem", context=context, swe_string="Theta Geminorum,tetGem,ICRS,06,52,47.33887,+33,57,40.5175,-1.66,-47.31,21,17.25,3.6, 34, 1481")
        self._other_names = ['Nageba']

Nageba = ThetaGeminorum


class IotaGeminorum(FixedStar): # ,iotGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotGem", context=context, swe_string="Iota Geminorum,iotGem,ICRS,07,25,43.59532,+27,47,53.0929,-122.66,-84.03,7.26,27.1,3.79, 28, 1385")
        self._other_names = ['Propus iotGem']

PropusiotGem = IotaGeminorum


class KappaGeminorum(FixedStar): # ,kapGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapGem", context=context, swe_string="Kappa Geminorum,kapGem,ICRS,07,44,26.85357,+24,23,52.7872,-23.39,-54.57,20.15,23.07,3.57, 24, 1759")
        self._other_names = ['Al Krikab']

AlKrikab = KappaGeminorum


class LambdaGeminorum(FixedStar): # ,lamGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamGem", context=context, swe_string="Lambda Geminorum,lamGem,ICRS,07,18,05.57977,+16,32,25.3905,-44.43,-36.61,-7.4,32.33,3.581, 16, 1443")
        self._other_names = ['Kebash']

Kebash = LambdaGeminorum


class LambdaGeminorum(FixedStar): # ,lamGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamGem", context=context, swe_string="Lambda Geminorum,lamGem,ICRS,07,18,05.57977,+16,32,25.3905,-44.43,-36.61,-7.4,32.33,3.581, 16, 1443")
        self._other_names = ['Alkibash']

Alkibash = LambdaGeminorum


class MessierObjectu.Gem(FixedStar): # ,mu.Gem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Gem", context=context, swe_string="Messier Object u.Gem,mu.Gem,ICRS,06,22,57.62686,+22,30,48.8979,56.39,-110.03,54.38,14.08,2.87, 22, 1304")
        self._other_names = ['Tejat']

Tejat = MessierObjectu.Gem


class NuGeminorum(FixedStar): # ,nu.Gem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Gem", context=context, swe_string="Nu Geminorum,nu.Gem,ICRS,06,28,57.78613,+20,12,43.6856,-6.82,-13.1,39.4,5.99,4.14, 20, 1441")
        self._other_names = []

 = NuGeminorum


class XiGeminorum(FixedStar): # ,ksiGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiGem", context=context, swe_string="Xi Geminorum,ksiGem,ICRS,06,45,17.36432,+12,53,44.1311,-115.73,-190.55,27.2,55.56,3.36, 13, 1396")
        self._other_names = ['Alzirr']

Alzirr = XiGeminorum


class OmicronGeminorum(FixedStar): # ,omiGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiGem", context=context, swe_string="Omicron Geminorum,omiGem,ICRS,07,39,09.93286,+34,35,03.6443,-33.42,-118.17,7.30,19.61,4.90,0,0")
        self._other_names = ['Jishui']

Jishui = OmicronGeminorum


class PiGeminorum(FixedStar): # ,pi.Gem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Gem", context=context, swe_string="Pi Geminorum,pi.Gem,ICRS,07,47,30.32300,+33,24,56.5034,-19.59,-29.33,-13.36,4.93,5.14, 33, 1585")
        self._other_names = []

 = PiGeminorum


class RhoGeminorum(FixedStar): # ,rhoGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoGem", context=context, swe_string="Rho Geminorum,rhoGem,ICRS,07,29,06.71887,+31,47,04.3773,159.09,193.29,-3.7,55.41,4.18, 32, 1562")
        self._other_names = []

 = RhoGeminorum


class SigmaGeminorum(FixedStar): # ,sigGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigGem", context=context, swe_string="Sigma Geminorum,sigGem,ICRS,07,43,18.72698,+28,53,00.6422,62.66,-230.32,44.15,26.08,4.29, 0, 0")
        self._other_names = []

 = SigmaGeminorum


class TauGeminorum(FixedStar): # ,tauGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauGem", context=context, swe_string="Tau Geminorum,tauGem,ICRS,07,11,08.37042,+30,14,42.5831,-31.21,-48.92,21.83,10.16,4.42, 0, 0")
        self._other_names = []

 = TauGeminorum


class UpsilonGeminorum(FixedStar): # ,upsGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsGem", context=context, swe_string="Upsilon Geminorum,upsGem,ICRS,07,35,55.34970,+26,53,44.6751,-34.12,-106.96,-21.61,12.04,4.06, 27, 1424")
        self._other_names = []

 = UpsilonGeminorum


class PhiGeminorum(FixedStar): # ,phiGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiGem", context=context, swe_string="Phi Geminorum,phiGem,ICRS,07,53,29.81390,+26,45,56.8252,-34.69,-30.1,8,14.66,4.963, 27, 1499")
        self._other_names = []

 = PhiGeminorum


class ChiGeminorum(FixedStar): # ,chiGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiGem", context=context, swe_string="Chi Geminorum,chiGem,ICRS,08,03,31.08225,+27,47,39.6243,-25.52,-31.89,-3.83,12.73,4.937, 28, 1532")
        self._other_names = []

 = ChiGeminorum


class OmegaGeminorum(FixedStar): # ,omeGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeGem", context=context, swe_string="Omega Geminorum,omeGem,ICRS,07,02,24.78033,+24,12,55.6051,-6.74,-0.25,-9.1,2.19,5.181, 24, 1502")
        self._other_names = []

 = OmegaGeminorum


class AlphaGruis(FixedStar): # ,alfGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfGru", context=context, swe_string="Alpha Gruis,alfGru,ICRS,22,08,13.98473,-46,57,39.5078,126.69,-147.47,10.9,32.29,1.71,-47,14063")
        self._other_names = ['Alnair']

Alnair = AlphaGruis


class BetaGruis(FixedStar): # ,betGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betGru", context=context, swe_string="Beta Gruis,betGru,ICRS,22,42,40.05027,-46,53,04.4752,135.16,-4.38,-0.3,18.43,2.11,-47,14308")
        self._other_names = ['Gruid']

Gruid = BetaGruis


class BetaGruis(FixedStar): # ,betGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betGru", context=context, swe_string="Beta Gruis,betGru,ICRS,22,42,40.05027,-46,53,04.4752,135.16,-4.38,-0.3,18.43,2.11,-47,14308")
        self._other_names = ['Tiaki']

Tiaki = BetaGruis


class GammaGruis(FixedStar): # ,gamGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamGru", context=context, swe_string="Gamma Gruis,gamGru,ICRS,21,53,55.72620,-37,21,53.4790,98.07,-13.22,0.1,15.45,3.01,-37,14536")
        self._other_names = ['Aldhanab']

Aldhanab = GammaGruis


class GammaGruis(FixedStar): # ,gamGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamGru", context=context, swe_string="Gamma Gruis,gamGru,ICRS,21,53,55.72620,-37,21,53.4790,98.07,-13.22,0.1,15.45,3.01,-37,14536")
        self._other_names = ['Al Dhanab']

AlDhanab = GammaGruis


class GammaGruis(FixedStar): # ,gamGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamGru", context=context, swe_string="Gamma Gruis,gamGru,ICRS,21,53,55.72620,-37,21,53.4790,98.07,-13.22,0.1,15.45,3.01,-37,14536")
        self._other_names = ['Ras Alkurki']

RasAlkurki = GammaGruis


class DeltaGruis01(FixedStar): # ,del01Gru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del01Gru", context=context, swe_string="Delta Gruis 01,del01Gru,ICRS,22,29,16.17481,-43,29,44.0245,25.72,-3.32,4.9,10.54,3.97,-44,14931")
        self._other_names = []

 = DeltaGruis01


class DeltaGruis02(FixedStar): # ,del02Gru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del02Gru", context=context, swe_string="Delta Gruis 02,del02Gru,ICRS,22,29,45.43402,-43,44,57.1968,-14.08,2.57,2.7,9.88,4.11,0,0")
        self._other_names = []

 = DeltaGruis02


class EpsilonGruis(FixedStar): # ,epsGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsGru", context=context, swe_string="Epsilon Gruis,epsGru,ICRS,22,48,33.29833,-51,19,00.7001,108.43,-64.83,-0.4,25.3,3.466,-51,13389")
        self._other_names = []

 = EpsilonGruis


class ThetaGruis(FixedStar): # ,tetGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetGru", context=context, swe_string="Theta Gruis,tetGru,ICRS,23,06,52.73046,-43,31,13.2857,-47.17,-13.49,9.6,24.73,4.332,0,0")
        self._other_names = []

 = ThetaGruis


class ZetaGruis(FixedStar): # ,zetGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetGru", context=context, swe_string="Zeta Gruis,zetGru,ICRS,23,00,52.81281,-52,45,14.8808,-63.96,-11.53,-1.1,29.96,4.115,-53,10382")
        self._other_names = []

 = ZetaGruis


class IotaGruis(FixedStar): # ,iotGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotGru", context=context, swe_string="Iota Gruis,iotGru,ICRS,23,10,21.53755,-45,14,48.1647,132.5,-26.66,-4.4,17.8,3.877,-45,14947")
        self._other_names = []

 = IotaGruis


class LambdaGruis(FixedStar): # ,lamGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamGru", context=context, swe_string="Lambda Gruis,lamGru,ICRS,22,06,06.88568,-39,32,36.0659,-23.8,-124.58,38.8,13.47,4.458,-40,14639")
        self._other_names = []

 = LambdaGruis


class NuGruis(FixedStar): # ,nu.Gru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Gru", context=context, swe_string="Nu Gruis,nu.Gru,ICRS,22,28,39.21012,-39,07,54.4477,37.43,-160.51,10.6,11.44,5.473,-39,14723")
        self._other_names = []

 = NuGruis


class OmicronGruis(FixedStar): # ,omiGru

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiGru", context=context, swe_string="Omicron Gruis,omiGru,ICRS,23,26,36.57748,-52,43,17.7656,34.52,130.66,22,32.5,5.522,-53,10461")
        self._other_names = []

 = OmicronGruis


class BetaHerculis(FixedStar): # ,betHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betHer", context=context, swe_string="Beta Herculis,betHer,ICRS,16,30,13.19955,+21,29,22.6008,-99.15,-15.39,-25.91,23.44,2.77, 21, 2934")
        self._other_names = ['Kornephoros']

Kornephoros = BetaHerculis


class AlphaHerculis(FixedStar): # ,alfHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfHer", context=context, swe_string="Alpha Herculis,alfHer,ICRS,17,14,38.85818,+14,23,25.2262,-7.32,36.07,-32.09,9.07,3.06, 14, 3207")
        self._other_names = ['Ras Algethi']

RasAlgethi = AlphaHerculis


class AlphaHerculis(FixedStar): # ,alfHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfHer", context=context, swe_string="Alpha Herculis,alfHer,ICRS,17,14,38.85818,+14,23,25.2262,-7.32,36.07,-32.09,9.07,3.06, 14, 3207")
        self._other_names = ['Rasalgethi']

Rasalgethi = AlphaHerculis


class AlphaHerculis01(FixedStar): # ,alf01Her

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf01Her", context=context, swe_string="Alpha Herculis 01,alf01Her,ICRS,17,14,38.853,+14,23,25.34,-17,47,-33.1,7,3.35, 0,0")
        self._other_names = []

 = AlphaHerculis01


class ZetaHerculis(FixedStar): # ,zetHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetHer", context=context, swe_string="Zeta Herculis,zetHer,ICRS,16,41,17.16104,+31,36,09.7873,-461.52,342.28,-67.8,93.32,2.8, 0, 0")
        self._other_names = ['Rutilicus']

Rutilicus = ZetaHerculis


class GammaHerculis(FixedStar): # ,gamHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamHer", context=context, swe_string="Gamma Herculis,gamHer,ICRS,16,21,55.21440,+19,09,11.2618,-47.39,43.81,-35.3,16.93,3.76, 19, 3086")
        self._other_names = []

 = GammaHerculis


class DeltaHerculis(FixedStar): # ,delHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delHer", context=context, swe_string="Delta Herculis,delHer,ICRS,17,15,01.91058,+24,50,21.1451,-21.18,-156.48,-40,43.41,3.13, 25, 3221")
        self._other_names = ['Sarin']

Sarin = DeltaHerculis


class EpsilonHerculis(FixedStar): # ,epsHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsHer", context=context, swe_string="Epsilon Herculis,epsHer,ICRS,17,00,17.37378,+30,55,35.0565,-47.69,26.9,-25.1,21.04,3.92, 31, 2947")
        self._other_names = ['Kajam epsHer']

KajamepsHer = EpsilonHerculis


class EtaHerculis(FixedStar): # ,etaHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaHer", context=context, swe_string="Eta Herculis,etaHer,ICRS,16,42,53.76509,+38,55,20.1129,35.41,-85.3,8.27,30.02,3.5, 39, 3029")
        self._other_names = ['Sofian']

Sofian = EtaHerculis


class ThetaHerculis(FixedStar): # ,tetHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetHer", context=context, swe_string="Theta Herculis,tetHer,ICRS,17,56,15.18054,+37,15,01.9343,2.67,6.47,-28.32,4.33,3.88, 37, 2982")
        self._other_names = ['Rukbalgethi Genubi']

RukbalgethiGenubi = ThetaHerculis


class IotaHerculis(FixedStar): # ,iotHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotHer", context=context, swe_string="Iota Herculis,iotHer,ICRS,17,39,27.88609,+46,00,22.8001,-7.48,4.53,-18.9,7.17,3.8, 46, 2349")
        self._other_names = ['Al Jathiyah']

AlJathiyah = IotaHerculis


class KappaHerculis(FixedStar): # ,kapHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapHer", context=context, swe_string="Kappa Herculis,kapHer,ICRS,16,08,04.52481,+17,02,49.1150,-35.55,-7.04,-10.5,8.87,4.994, 17, 2964")
        self._other_names = ['Marsik']

Marsik = KappaHerculis


class KappaHerculis(FixedStar): # ,kapHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapHer", context=context, swe_string="Kappa Herculis,kapHer,ICRS,16,08,04.52481,+17,02,49.1150,-35.55,-7.04,-10.5,8.87,4.994, 17, 2964")
        self._other_names = ['Marsic']

Marsic = KappaHerculis


class LambdaHerculis(FixedStar): # ,lamHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamHer", context=context, swe_string="Lambda Herculis,lamHer,ICRS,17,30,44.31022,+26,06,38.3213,18.81,16.62,-26.51,8.83,4.41, 26, 3034")
        self._other_names = ['Masym']

Masym = LambdaHerculis


class LambdaHerculis(FixedStar): # ,lamHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamHer", context=context, swe_string="Lambda Herculis,lamHer,ICRS,17,30,44.31022,+26,06,38.3213,18.81,16.62,-26.51,8.83,4.41, 26, 3034")
        self._other_names = ['Maasym']

Maasym = LambdaHerculis


class MessierObjectu.Her(FixedStar): # ,mu.Her

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Her", context=context, swe_string="Messier Object u.Her,mu.Her,ICRS,17,46,27.52667,+27,43,14.4379,-291.66,-749.6,-17.07,120.33,3.42, 27, 2888")
        self._other_names = ['Melkarth']

Melkarth = MessierObjectu.Her


class XiHerculis(FixedStar): # ,ksiHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiHer", context=context, swe_string="Xi Herculis,ksiHer,ICRS,17,57,45.88571,+29,14,52.3675,82.44,-18.73,-1.72,23.84,3.7, 29, 3156")
        self._other_names = []

 = XiHerculis


class OmicronHerculis(FixedStar): # ,omiHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiHer", context=context, swe_string="Omicron Herculis,omiHer,ICRS,18,07,32.55073,+28,45,44.9679,-0.02,8.55,-29.5,9.65,3.827, 28, 2925")
        self._other_names = []

 = OmicronHerculis


class PiHerculis(FixedStar): # ,pi.Her

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Her", context=context, swe_string="Pi Herculis,pi.Her,ICRS,17,15,02.83436,+36,48,32.9843,-27.29,2.82,-25.57,8.66,3.18, 36, 2844")
        self._other_names = ['Fudail']

Fudail = PiHerculis


class SigmaHerculis(FixedStar): # ,sigHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigHer", context=context, swe_string="Sigma Herculis,sigHer,ICRS,16,34,06.18334,+42,26,13.3455,-7.54,59.42,-10.9,10.36,4.196, 42, 2724")
        self._other_names = []

 = SigmaHerculis


class TauHerculis(FixedStar): # ,tauHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauHer", context=context, swe_string="Tau Herculis,tauHer,ICRS,16,19,44.43666,+46,18,48.1123,-13.33,38.48,-15.5,10.61,3.9, 46, 2169")
        self._other_names = ['Rukbalgethi Shemali']

RukbalgethiShemali = TauHerculis


class PhiHerculis(FixedStar): # ,phiHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiHer", context=context, swe_string="Phi Herculis,phiHer,ICRS,16,08,46.17745,+44,56,05.6663,-26.63,36.76,-16.3,15.99,4.27, 45, 2376")
        self._other_names = []

 = PhiHerculis


class ChiHerculis(FixedStar): # ,chiHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiHer", context=context, swe_string="Chi Herculis,chiHer,ICRS,15,52,40.54141,+42,27,05.4664,438.9,629.7,-55.88,62.92,4.62, 42, 2648")
        self._other_names = []

 = ChiHerculis


class OmegaHerculis(FixedStar): # ,omeHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeHer", context=context, swe_string="Omega Herculis,omeHer,ICRS,16,25,24.9536,+14,01,59.769,39.765,-59.974,-5.9,13.04,4.58, 14, 3049")
        self._other_names = ['Kajam omeHer']

KajamomeHer = OmegaHerculis


class OmegaHerculis(FixedStar): # ,omeHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeHer", context=context, swe_string="Omega Herculis,omeHer,ICRS,16,25,24.9536,+14,01,59.769,39.765,-59.974,-5.9,13.04,4.58, 14, 3049")
        self._other_names = ['Cujam']

Cujam = OmegaHerculis


class RhoHerculis(FixedStar): # ,rhoHer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoHer", context=context, swe_string="Rho Herculis,rhoHer,ICRS,17,23,40.94412,+37,08,45.3940,-39.38,7.71,-21,8.29,4.56,0,0")
        self._other_names = []

 = RhoHerculis


class HenryDraperCatalogue149026(FixedStar): # ,HD149026

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HD149026", context=context, swe_string="Henry Draper Catalogue 149026,HD149026,ICRS,16,30,29.6185,+38,20,50.308,-77.9,52.694,-18.02,13.04,8.14, 0,0")
        self._other_names = ['Ogma']

Ogma = HenryDraperCatalogue149026


class Apex(FixedStar): # ,Apex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Apex", context=context, swe_string="Apex,Apex,1950,18,03,50.2, 30,00,16.8,  0.000,   0.00,-16.5,0.0000,999.99,  0,    0")
        self._other_names = ['Apex']

Apex = Apex


class AlphaHorologii(FixedStar): # ,alfHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfHor", context=context, swe_string="Alpha Horologii,alfHor,ICRS,04,14,00.11445,-42,17,39.7232,42.02,-203.55,21.6,28.36,3.86,-42, 1425")
        self._other_names = []

 = AlphaHorologii


class ZetaHorologii(FixedStar): # ,zetHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetHor", context=context, swe_string="Zeta Horologii,zetHor,ICRS,02,40,39.61286,-54,32,59.6836,32.86,4.96,-1.1,20.37,5.21,-55,  446")
        self._other_names = []

 = ZetaHorologii


class LambdaHorologii(FixedStar): # ,lamHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamHor", context=context, swe_string="Lambda Horologii,lamHor,ICRS,02,24,53.91014,-60,18,43.0132,-71.69,-131.28,6,20.25,5.355,-60,  199")
        self._other_names = []

 = LambdaHorologii


class MessierObjectu.Hor(FixedStar): # ,mu.Hor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Hor", context=context, swe_string="Messier Object u.Hor,mu.Hor,ICRS,03,03,36.81891,-59,44,15.9925,-73.29,-64.06,17.3,23.04,5.122,-60,  236")
        self._other_names = []

 = MessierObjectu.Hor


class IotaHorologii(FixedStar): # ,iotHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotHor", context=context, swe_string="Iota Horologii,iotHor,ICRS,02,42,33.4666,-50,48,01.056,333.81,219.5,16.8,58.25,5.4,0,0")
        self._other_names = []

 = IotaHorologii


class EtaHorologii(FixedStar): # ,etaHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaHor", context=context, swe_string="Eta Horologii,etaHor,ICRS,02,37,24.37297,-52,32,35.0855,112.7,3.73,-3,21.95,5.293,0,0")
        self._other_names = []

 = EtaHorologii


class BetaHorologii(FixedStar): # ,betHor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betHor", context=context, swe_string="Beta Horologii,betHor,ICRS,02,58,47.79642,-64,04,16.6250,22.76,5.18,23.6,11.07,4.969,0,0")
        self._other_names = []

 = BetaHorologii


class AlphaHydrae(FixedStar): # ,alfHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfHya", context=context, swe_string="Alpha Hydrae,alfHya,ICRS,09,27,35.24270,-08,39,30.9583,-15.23,34.37,-4.27,18.09,1.97,-08, 2680")
        self._other_names = ['Alphard']

Alphard = AlphaHydrae


class AlphaHydrae(FixedStar): # ,alfHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfHya", context=context, swe_string="Alpha Hydrae,alfHya,ICRS,09,27,35.24270,-08,39,30.9583,-15.23,34.37,-4.27,18.09,1.97,-08, 2680")
        self._other_names = ['Cor Hydrae']

CorHydrae = AlphaHydrae


class BetaHydrae(FixedStar): # ,betHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betHya", context=context, swe_string="Beta Hydrae,betHya,ICRS,11,52,54.52149,-33,54,29.2672,-56.56,0.19,-1,10.53,4.28,0, 0")
        self._other_names = []

 = BetaHydrae


class GammaHydrae(FixedStar): # ,gamHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamHya", context=context, swe_string="Gamma Hydrae,gamHya,ICRS,13,18,55.29719,-23,10,17.4514,68.99,-41.85,-4.74,24.37,3,-22, 3554")
        self._other_names = ['Cauda Hydrae']

CaudaHydrae = GammaHydrae


class GammaHydrae(FixedStar): # ,gamHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamHya", context=context, swe_string="Gamma Hydrae,gamHya,ICRS,13,18,55.29719,-23,10,17.4514,68.99,-41.85,-4.74,24.37,3,-22, 3554")
        self._other_names = ['Dhanab al Shuja']

DhanabalShuja = GammaHydrae


class DeltaHydrae(FixedStar): # ,delHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delHya", context=context, swe_string="Delta Hydrae,delHya,ICRS,08,37,39.36627,+05,42,13.6057,-70.19,-7.9,11.3,20.34,4.131, 06, 2001")
        self._other_names = ['Mautinah']

Mautinah = DeltaHydrae


class EpsilonHydrae(FixedStar): # ,epsHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsHya", context=context, swe_string="Epsilon Hydrae,epsHya,ICRS,08,46,46.51223,+06,25,07.6855,-228.11,-43.82,36.4,25.23,3.38, 0, 0")
        self._other_names = ['Ashlesha']

Ashlesha = EpsilonHydrae


class ZetaHydrae(FixedStar): # ,zetHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetHya", context=context, swe_string="Zeta Hydrae,zetHya,ICRS,08,55,23.62614,+05,56,44.0354,-100.06,15.46,22.3,19.51,3.1, 06, 2060")
        self._other_names = ['Hydrobius']

Hydrobius = ZetaHydrae


class EtaHydrae(FixedStar): # ,etaHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaHya", context=context, swe_string="Eta Hydrae,etaHya,ICRS,08,43,13.47499,+03,23,55.1867,-19.39,-1.08,16.1,5.56,4.3, 0, 0")
        self._other_names = []

 = EtaHydrae


class ThetaHydrae(FixedStar): # ,tetHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetHya", context=context, swe_string="Theta Hydrae,tetHya,ICRS,09,14,21.86007,+02,18,51.3432,114.64,-313.94,-10.7,28.74,3.88, 02, 2167")
        self._other_names = []

 = ThetaHydrae


class IotaHydrae(FixedStar): # ,iotHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotHya", context=context, swe_string="Iota Hydrae,iotHya,ICRS,09,39,51.36145,-01,08,34.1135,46.96,-62.39,24.19,12.39,3.91,-00, 2231")
        self._other_names = []

 = IotaHydrae


class KappaHydrae(FixedStar): # ,kapHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapHya", context=context, swe_string="Kappa Hydrae,kapHya,ICRS,09,40,18.36496,-14,19,56.2675,-23.41,-21.1,20.6,7.48,5.052,-13, 2917")
        self._other_names = []

 = KappaHydrae


class LambdaHydrae(FixedStar): # ,lamHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamHya", context=context, swe_string="Lambda Hydrae,lamHya,ICRS,10,10,35.27667,-12,21,14.6938,-201.27,-99.63,19.4,28.98,3.61,-11, 2820")
        self._other_names = []

 = LambdaHydrae


class MessierObjectu.Hya(FixedStar): # ,mu.Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Hya", context=context, swe_string="Messier Object u.Hya,mu.Hya,ICRS,10,26,05.42630,-16,50,10.6429,-129.17,-79.76,40.81,13.93,3.81,-16, 3052")
        self._other_names = []

 = MessierObjectu.Hya


class NuHydrae(FixedStar): # ,nu.Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Hya", context=context, swe_string="Nu Hydrae,nu.Hya,ICRS,10,49,37.48875,-16,11,37.1360,93.35,198.88,-1.37,22.69,3.11,-15, 3138")
        self._other_names = ['Pleura']

Pleura = NuHydrae


class XiHydrae(FixedStar): # ,ksiHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiHya", context=context, swe_string="Xi Hydrae,ksiHya,ICRS,11,33,00.11505,-31,51,27.4435,-209.62,-40.84,-4.9,25.16,3.54,-31, 9083")
        self._other_names = []

 = XiHydrae


class OmicronHydrae(FixedStar): # ,omiHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiHya", context=context, swe_string="Omicron Hydrae,omiHya,ICRS,11,40,12.78970,-34,44,40.7733,-43.24,-1.61,5.9,7.27,4.7,-34, 7610")
        self._other_names = []

 = OmicronHydrae


class PiHydrae(FixedStar): # ,pi.Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Hya", context=context, swe_string="Pi Hydrae,pi.Hya,ICRS,14,06,22.29749,-26,40,56.5024,43.7,-141.18,27.2,32.3,3.28,-26,10095")
        self._other_names = ['Sataghni']

Sataghni = PiHydrae


class SigmaHydrae(FixedStar): # ,sigHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigHya", context=context, swe_string="Sigma Hydrae,sigHya,ICRS,08,38,45.43747,+03,20,29.1701,-19.48,-15.92,27.28,8.75,4.43, 03, 2026")
        self._other_names = ['Al Minliar al Shuja']

AlMinliaralShuja = SigmaHydrae


class SigmaHydrae(FixedStar): # ,sigHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigHya", context=context, swe_string="Sigma Hydrae,sigHya,ICRS,08,38,45.43747,+03,20,29.1701,-19.48,-15.92,27.28,8.75,4.43, 03, 2026")
        self._other_names = ['Minchir']

Minchir = SigmaHydrae


class TauHydrae01(FixedStar): # ,tau01Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau01Hya", context=context, swe_string="Tau Hydrae 01,tau01Hya,ICRS,09,29,08.89655,-02,46,08.2649,99.01,-2.67,10.48,57.69,4.6,-02, 2901")
        self._other_names = ['Ukdah']

Ukdah = TauHydrae01


class TauHydrae01(FixedStar): # ,tau01Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau01Hya", context=context, swe_string="Tau Hydrae 01,tau01Hya,ICRS,09,29,08.89655,-02,46,08.2649,99.01,-2.67,10.48,57.69,4.6,-02, 2901")
        self._other_names = ['Ukdah prima']

Ukdahprima = TauHydrae01


class TauHydrae02(FixedStar): # ,tau02Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau02Hya", context=context, swe_string="Tau Hydrae 02,tau02Hya,ICRS,09,31,58.92729,-01,11,04.7899,-12.6,-3.99,3.9,6.3,4.548,-00, 2211")
        self._other_names = ['Ukdah']

Ukdah = TauHydrae02


class TauHydrae02(FixedStar): # ,tau02Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau02Hya", context=context, swe_string="Tau Hydrae 02,tau02Hya,ICRS,09,31,58.92729,-01,11,04.7899,-12.6,-3.99,3.9,6.3,4.548,-00, 2211")
        self._other_names = ['Ukdah secunda']

Ukdahsecunda = TauHydrae02


class UpsilonHydrae01(FixedStar): # ,ups01Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ups01Hya", context=context, swe_string="Upsilon Hydrae 01,ups01Hya,ICRS,09,51,28.69384,-14,50,47.7710,18.88,-21.85,-14.34,12.36,4.11,0, 0")
        self._other_names = ['Zhang']

Zhang = UpsilonHydrae01


class UpsilonHydrae02(FixedStar): # ,ups02Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ups02Hya", context=context, swe_string="Upsilon Hydrae 02,ups02Hya,ICRS,10,05,07.46888,-13,03,52.6561,-39.39,19.65,24.3,10.4,4.588,-12, 3073")
        self._other_names = []

 = UpsilonHydrae02


class ChiHydrae01(FixedStar): # ,chi01Hya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chi01Hya", context=context, swe_string="Chi Hydrae 01,chi01Hya,ICRS,11,05,19.90766,-27,17,36.9957,-190.41,-5.96,19.1,23.13,4.94,-26, 8338")
        self._other_names = []

 = ChiHydrae01


class AlphaHydri(FixedStar): # ,alfHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfHyi", context=context, swe_string="Alpha Hydri,alfHyi,ICRS,01,58,46.19467,-61,34,11.4948,263.66,26.77,8.7,45.43,2.84,-62,  162")
        self._other_names = []

 = AlphaHydri


class BetaHydri(FixedStar): # ,betHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betHyi", context=context, swe_string="Beta Hydri,betHyi,ICRS,00,25,45.07036,-77,15,15.2860,2219.54,324.09,23.1,134.07,2.79,-77,   16")
        self._other_names = []

 = BetaHydri


class GammaHydri(FixedStar): # ,gamHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamHyi", context=context, swe_string="Gamma Hydri,gamHyi,ICRS,03,47,14.34062,-74,14,20.2686,50.85,114.74,15.8,15.24,3.26,-74,  276")
        self._other_names = []

 = GammaHydri


class DeltaHydri(FixedStar): # ,delHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delHyi", context=context, swe_string="Delta Hydri,delHyi,ICRS,02,21,44.94286,-68,39,33.9038,-49.95,2.48,6,23.35,4.09,-69,  113")
        self._other_names = []

 = DeltaHydri


class EpsilonHydri(FixedStar): # ,epsHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsHyi", context=context, swe_string="Epsilon Hydri,epsHyi,ICRS,02,39,35.36121,-68,16,01.0103,87.424,0.09,13.6,21.48,4.096,-68,  161")
        self._other_names = []

 = EpsilonHydri


class EtaHydri02(FixedStar): # ,eta02Hyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eta02Hyi", context=context, swe_string="Eta Hydri 02,eta02Hyi,ICRS,01,54,56.13169,-67,38,50.2939,76.22,72.94,-16.2,14.91,4.685,-68,  101")
        self._other_names = []

 = EtaHydri02


class ThetaHydri(FixedStar): # ,tetHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetHyi", context=context, swe_string="Theta Hydri,tetHyi,ICRS,03,02,15.44844,-71,54,08.8369,27.19,16.82,12.3,6.34,5.499,-72,  219")
        self._other_names = []

 = ThetaHydri


class IotaHydri(FixedStar): # ,iotHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotHyi", context=context, swe_string="Iota Hydri,iotHyi,ICRS,03,15,57.66176,-77,23,18.4341,113.72,62.1,19.4,33.66,5.506,-77,  134")
        self._other_names = []

 = IotaHydri


class KappaHydri(FixedStar): # ,kapHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapHyi", context=context, swe_string="Kappa Hydri,kapHyi,ICRS,02,22,52.30687,-73,38,44.8506,-80.75,11.97,22,10.28,5.987,-74,  194")
        self._other_names = []

 = KappaHydri


class LambdaHydri(FixedStar): # ,lamHyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamHyi", context=context, swe_string="Lambda Hydri,lamHyi,ICRS,00,48,35.41650,-74,55,24.3732,132.89,-34.29,9.5,15.4,5.083,-75,   64")
        self._other_names = []

 = LambdaHydri


class MessierObjectu.Hyi(FixedStar): # ,mu.Hyi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Hyi", context=context, swe_string="Messier Object u.Hyi,mu.Hyi,ICRS,02,31,40.54440,-79,06,33.7721,137.24,-54.22,-14.5,11.49,5.275,-79,   66")
        self._other_names = []

 = MessierObjectu.Hyi


class AlphaIndi(FixedStar): # ,alfInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfInd", context=context, swe_string="Alpha Indi,alfInd,ICRS,20,37,34.03201,-47,17,29.4026,49.24,66.53,-1.3,33.17,3.11,-47,13477")
        self._other_names = []

 = AlphaIndi


class BetaIndi(FixedStar): # ,betInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betInd", context=context, swe_string="Beta Indi,betInd,ICRS,20,54,48.60278,-58,27,14.9618,20.79,-25.2,-4.9,5.33,3.65,-58, 7788")
        self._other_names = []

 = BetaIndi


class GammaIndi(FixedStar): # ,gamInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamInd", context=context, swe_string="Gamma Indi,gamInd,ICRS,21,26,15.43925,-54,39,37.6477,1.11,39.38,10.4,14.96,6.082,-55, 9586")
        self._other_names = []

 = GammaIndi


class DeltaIndi(FixedStar): # ,delInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delInd", context=context, swe_string="Delta Indi,delInd,ICRS,21,57,55.07353,-54,59,33.2740,41.94,-3.93,9.4,17.34,4.4,-55, 9733")
        self._other_names = []

 = DeltaIndi


class EpsilonIndi(FixedStar): # ,epsInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsInd", context=context, swe_string="Epsilon Indi,epsInd,ICRS,22,03,21.65809,-56,47,09.5169,3960.93,-2539.23,-40,276.06,4.69,-57,10015")
        self._other_names = []

 = EpsilonIndi


class EtaIndi(FixedStar): # ,etaInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaInd", context=context, swe_string="Eta Indi,etaInd,ICRS,20,44,02.33404,-51,55,15.4970,155.8,-53.86,-1.6,41.37,4.495,-52,11752")
        self._other_names = []

 = EtaIndi


class ThetaIndi(FixedStar): # ,tetInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetInd", context=context, swe_string="Theta Indi,tetInd,ICRS,21,19,51.98955,-53,26,57.9315,107.9,-66.41,-14.5,33.02,4.4,0,0")
        self._other_names = []

 = ThetaIndi


class OmicronIndi(FixedStar): # ,omiInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiInd", context=context, swe_string="Omicron Indi,omiInd,ICRS,21,50,47.18681,-69,37,45.8967,-23.27,-4.65,20.2,6,5.505,-70, 2873")
        self._other_names = []

 = OmicronIndi


class RhoIndi(FixedStar): # ,rhoInd

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoInd", context=context, swe_string="Rho Indi,rhoInd,ICRS,22,54,39.48205,-70,04,25.3530,-43.89,73.04,-4,37.39,6.05,-70, 2971")
        self._other_names = []

 = RhoIndi


class AlphaLacertae(FixedStar): # ,alfLac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLac", context=context, swe_string="Alpha Lacertae,alfLac,ICRS,22,31,17.50131,+50,16,56.9682,137.51,17.01,-4.5,31.79,3.77, 49, 3875")
        self._other_names = []

 = AlphaLacertae


class BetaLacertae(FixedStar): # ,betLac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLac", context=context, swe_string="Beta Lacertae,betLac,ICRS,22,23,33.62375,+52,13,44.5646,-13.25,-186.77,-11.42,19.19,4.44, 51, 3358")
        self._other_names = []

 = BetaLacertae


class Lacertae1(FixedStar): # ,1Lac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",1Lac", context=context, swe_string="Lacertae1,1Lac,ICRS,22,15,58.17673,+37,44,55.4385,8.85,-0.72,-8.58,5.25,4.15,0,0")
        self._other_names = []

 = Lacertae1


class Lacertae2(FixedStar): # ,2Lac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",2Lac", context=context, swe_string="Lacertae2,2Lac,ICRS,22,21,01.54727,+46,32,11.6461,22.35,1.45,-9.5,5.88,4.54,0,0")
        self._other_names = []

 = Lacertae2


class Lacertae4(FixedStar): # ,4Lac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",4Lac", context=context, swe_string="Lacertae4,4Lac,ICRS,22,24,30.99068,+49,28,35.0176,-5.55,-2.85,-26,1.45,4.58,0,0")
        self._other_names = []

 = Lacertae4


class Lacertae5(FixedStar): # ,5Lac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",5Lac", context=context, swe_string="Lacertae5,5Lac,ICRS,22,29,31.82251,+47,42,24.7927,-0.37,-3.33,-12.93,1.98,4.37,0,0")
        self._other_names = []

 = Lacertae5


class Lacertae6(FixedStar): # ,6Lac

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",6Lac", context=context, swe_string="Lacertae6,6Lac,ICRS,22,30,29.26005,+43,07,24.1565,-1.98,-5.36,-8.7,1.9,4.511,0,0")
        self._other_names = []

 = Lacertae6


class AlphaLeonis(FixedStar): # ,alfLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLeo", context=context, swe_string="Alpha Leonis,alfLeo,ICRS,10,08,22.31099,+11,58,01.9516,-248.73,5.59,5.9,41.13,1.4, 12, 2149")
        self._other_names = ['Regulus']

Regulus = AlphaLeonis


class AlphaLeonis(FixedStar): # ,alfLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLeo", context=context, swe_string="Alpha Leonis,alfLeo,ICRS,10,08,22.31099,+11,58,01.9516,-248.73,5.59,5.9,41.13,1.4, 12, 2149")
        self._other_names = ['Magha']

Magha = AlphaLeonis


class BetaLeonis(FixedStar): # ,betLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLeo", context=context, swe_string="Beta Leonis,betLeo,ICRS,11,49,03.57834,+14,34,19.4090,-497.68,-114.67,-0.2,90.91,2.13, 15, 2383")
        self._other_names = ['Denebola', 'HIP 57632']

Denebola = BetaLeonis
HIP57632 = BetaLeonis


class BetaLeonis(FixedStar): # ,betLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLeo", context=context, swe_string="Beta Leonis,betLeo,ICRS,11,49,03.57834,+14,34,19.4090,-497.68,-114.67,-0.2,90.91,2.13, 15, 2383")
        self._other_names = ['Uttaraphalguni']

Uttaraphalguni = BetaLeonis


class GammaLeonis01(FixedStar): # ,gam01Leo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam01Leo", context=context, swe_string="Gamma Leonis 01,gam01Leo,ICRS,10,19,58.427,+19,50,28.53,294.9,-154,-36.98,25.96,1.98, 20, 2467")
        self._other_names = ['Algieba']

Algieba = GammaLeonis01


class DeltaLeonis(FixedStar): # ,delLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delLeo", context=context, swe_string="Delta Leonis,delLeo,ICRS,11,14,06.50142,+20,31,25.3853,143.42,-129.88,-20.9,55.82,2.53, 21, 2298")
        self._other_names = ['Zosma']

Zosma = DeltaLeonis


class DeltaLeonis(FixedStar): # ,delLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delLeo", context=context, swe_string="Delta Leonis,delLeo,ICRS,11,14,06.50142,+20,31,25.3853,143.42,-129.88,-20.9,55.82,2.53, 21, 2298")
        self._other_names = ['Dhur']

Dhur = DeltaLeonis


class DeltaLeonis(FixedStar): # ,delLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delLeo", context=context, swe_string="Delta Leonis,delLeo,ICRS,11,14,06.50142,+20,31,25.3853,143.42,-129.88,-20.9,55.82,2.53, 21, 2298")
        self._other_names = ['Purvaphalguni']

Purvaphalguni = DeltaLeonis


class EpsilonLeonis(FixedStar): # ,epsLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsLeo", context=context, swe_string="Epsilon Leonis,epsLeo,ICRS,09,45,51.07330,+23,46,27.3208,-45.61,-9.21,4.48,13.22,2.98, 24, 2129")
        self._other_names = ['Ras Elased Australis']

RasElasedAustralis = EpsilonLeonis


class ZetaLeonis(FixedStar): # ,zetLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetLeo", context=context, swe_string="Zeta Leonis,zetLeo,ICRS,10,16,41.41597,+23,25,02.3221,18.39,-6.84,-21.4,11.9,3.41, 24, 2209")
        self._other_names = ['Adhafera']

Adhafera = ZetaLeonis


class EtaLeonis(FixedStar): # ,etaLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaLeo", context=context, swe_string="Eta Leonis,etaLeo,ICRS,10,07,19.95186,+16,45,45.5803,-2.8,-1.82,1.4,2.57,3.41, 17, 2171")
        self._other_names = ['Al Jabhah']

AlJabhah = EtaLeonis


class IotaLeonis(FixedStar): # ,iotLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotLeo", context=context, swe_string="Iota Leonis,iotLeo,ICRS,11,23,55.45273,+10,31,46.2195,141.45,-79.14,-11.8,42.24,4, 11, 2348")
        self._other_names = ['Tse Tseng']

TseTseng = IotaLeonis


class IotaLeonis(FixedStar): # ,iotLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotLeo", context=context, swe_string="Iota Leonis,iotLeo,ICRS,11,23,55.45273,+10,31,46.2195,141.45,-79.14,-11.8,42.24,4, 11, 2348")
        self._other_names = ['Tsze Tseang']

TszeTseang = IotaLeonis


class KappaLeonis(FixedStar): # ,kapLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapLeo", context=context, swe_string="Kappa Leonis,kapLeo,ICRS,09,24,39.25874,+26,10,56.3650,-31.64,-48.2,27.94,16.2,4.46, 26, 1939")
        self._other_names = ['Alminhar']

Alminhar = KappaLeonis


class KappaLeonis(FixedStar): # ,kapLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapLeo", context=context, swe_string="Kappa Leonis,kapLeo,ICRS,09,24,39.25874,+26,10,56.3650,-31.64,-48.2,27.94,16.2,4.46, 26, 1939")
        self._other_names = ['Al Minliar al Asad']

AlMinliaralAsad = KappaLeonis


class LambdaLeonis(FixedStar): # ,lamLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamLeo", context=context, swe_string="Lambda Leonis,lamLeo,ICRS,09,31,43.22754,+22,58,04.6904,-20.17,-39.47,24.27,9.91,4.31, 23, 2107")
        self._other_names = ['Alterf']

Alterf = LambdaLeonis


class MessierObjectu.Leo(FixedStar): # ,mu.Leo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Leo", context=context, swe_string="Messier Object u.Leo,mu.Leo,ICRS,09,52,45.81654,+26,00,25.0319,-217.31,-54.26,13.63,26.28,3.88, 26, 2019")
        self._other_names = ['Ras Elased Borealis']

RasElasedBorealis = MessierObjectu.Leo


class MessierObjectu.Leo(FixedStar): # ,mu.Leo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Leo", context=context, swe_string="Messier Object u.Leo,mu.Leo,ICRS,09,52,45.81654,+26,00,25.0319,-217.31,-54.26,13.63,26.28,3.88, 26, 2019")
        self._other_names = ['Rasalas']

Rasalas = MessierObjectu.Leo


class XiLeonis(FixedStar): # ,ksiLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiLeo", context=context, swe_string="Xi Leonis,ksiLeo,ICRS,09,31,56.73886,+11,17,59.3933,-89.98,-81.85,35.83,15.13,4.963, 11, 2053")
        self._other_names = []

 = XiLeonis


class OmicronLeonis(FixedStar): # ,omiLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiLeo", context=context, swe_string="Omicron Leonis,omiLeo,ICRS,09,41,09.03305,+09,53,32.3102,-143.2,-37.2,26.18,25.03,3.52, 10, 2044")
        self._other_names = ['Subra']

Subra = OmicronLeonis


class SigmaLeonis(FixedStar): # ,sigLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigLeo", context=context, swe_string="Sigma Leonis,sigLeo,ICRS,11,21,08.19349,+06,01,45.5710,-92.97,-11.48,-5.3,14.82,4.04, 06, 2437")
        self._other_names = ['Shishimai']

Shishimai = SigmaLeonis


class ThetaLeonis(FixedStar): # ,tetLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetLeo", context=context, swe_string="Theta Leonis,tetLeo,ICRS,11,14,14.40446,+15,25,46.4541,-60.31,-79.1,7.3,19.76,3.35, 16, 2234")
        self._other_names = ['Coxa']

Coxa = ThetaLeonis


class ThetaLeonis(FixedStar): # ,tetLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetLeo", context=context, swe_string="Theta Leonis,tetLeo,ICRS,11,14,14.40446,+15,25,46.4541,-60.31,-79.1,7.3,19.76,3.35, 16, 2234")
        self._other_names = ['Chertan']

Chertan = ThetaLeonis


class ThetaLeonis(FixedStar): # ,tetLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetLeo", context=context, swe_string="Theta Leonis,tetLeo,ICRS,11,14,14.40446,+15,25,46.4541,-60.31,-79.1,7.3,19.76,3.35, 16, 2234")
        self._other_names = ['Cestan']

Cestan = ThetaLeonis


class ThetaLeonis(FixedStar): # ,tetLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetLeo", context=context, swe_string="Theta Leonis,tetLeo,ICRS,11,14,14.40446,+15,25,46.4541,-60.31,-79.1,7.3,19.76,3.35, 16, 2234")
        self._other_names = ['Chort']

Chort = ThetaLeonis


class PiLeonis(FixedStar): # ,pi.Leo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Leo", context=context, swe_string="Pi Leonis,pi.Leo,ICRS,10,00,12.80589,+08,02,39.2032,-31.41,-22.15,22.3,8.03,4.7, 08, 2301")
        self._other_names = []

 = PiLeonis


class RhoLeonis(FixedStar): # ,rhoLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoLeo", context=context, swe_string="Rho Leonis,rhoLeo,ICRS,10,32,48.67168,+09,18,23.7094,-5.93,-3.4,42,0.6,3.87, 10, 2166")
        self._other_names = ['Shir']

Shir = RhoLeonis


class TauLeonis(FixedStar): # ,tauLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauLeo", context=context, swe_string="Tau Leonis,tauLeo,ICRS,11,27,56.23976,+02,51,22.5609,16.89,-9.81,-8.9,5.8,4.943, 03, 2504")
        self._other_names = []

 = TauLeonis


class UpsilonLeonis(FixedStar): # ,upsLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsLeo", context=context, swe_string="Upsilon Leonis,upsLeo,ICRS,11,36,56.931,-00,49,25.49,1.76,43.37,1.79,17.97,4.3,-00, 2458")
        self._other_names = []

 = UpsilonLeonis


class PhiLeonis(FixedStar): # ,phiLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiLeo", context=context, swe_string="Phi Leonis,phiLeo,ICRS,11,16,39.69960,-03,39,05.7770,-110.37,-37.16,-3,17.71,4.45,-02, 3315")
        self._other_names = []

 = PhiLeonis


class ChiLeonis(FixedStar): # ,chiLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiLeo", context=context, swe_string="Chi Leonis,chiLeo,ICRS,11,05,01.02754,+07,20,09.6235,-344.28,-47.65,3.3,34.49,4.63, 08, 2455")
        self._other_names = []

 = ChiLeonis


class PsiLeonis(FixedStar): # ,psiLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiLeo", context=context, swe_string="Psi Leonis,psiLeo,ICRS,09,43,43.90499,+14,01,18.1033,5.81,-4.8,10.23,5.34,5.35, 14, 2136")
        self._other_names = []

 = PsiLeonis


class AlphaLeporis(FixedStar): # ,alfLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLep", context=context, swe_string="Alpha Leporis,alfLep,ICRS,05,32,43.81612,-17,49,20.2414,3.56,1.18,25.1,1.47,2.57,-17, 1166")
        self._other_names = ['Arneb']

Arneb = AlphaLeporis


class BetaLeporis(FixedStar): # ,betLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLep", context=context, swe_string="Beta Leporis,betLep,ICRS,05,28,14.72316,-20,45,33.9878,-5.02,-86.01,-14.2,20.34,2.84,-20, 1096")
        self._other_names = ['Nihal']

Nihal = BetaLeporis


class GammaLeporis(FixedStar): # ,gamLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamLep", context=context, swe_string="Gamma Leporis,gamLep,ICRS,05,44,27.79089,-22,26,54.1808,-291.67,-368.97,-9.29,112.02,3.6,-22, 1211")
        self._other_names = []

 = GammaLeporis


class DeltaLeporis(FixedStar): # ,delLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delLep", context=context, swe_string="Delta Leporis,delLep,ICRS,05,51,19.29613,-20,52,44.7232,229.49,-648.41,101.77,28.68,3.85,-20, 1211")
        self._other_names = []

 = DeltaLeporis


class EpsilonLeporis(FixedStar): # ,epsLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsLep", context=context, swe_string="Epsilon Leporis,epsLep,ICRS,05,05,27.66537,-22,22,15.7239,21.13,-73.11,1,15.29,3.18,-22, 1000")
        self._other_names = ['Sasin']

Sasin = EpsilonLeporis


class ZetaLeporis(FixedStar): # ,zetLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetLep", context=context, swe_string="Zeta Leporis,zetLep,ICRS,05,46,57.34096,-14,49,19.0199,-14.54,-1.07,24.7,46.28,3.525,-14, 1232")
        self._other_names = []

 = ZetaLeporis


class EtaLeporis(FixedStar): # ,etaLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaLep", context=context, swe_string="Eta Leporis,etaLep,ICRS,05,56,24.29300,-14,10,03.7189,-42.06,139.26,-2.14,67.21,3.72,-14, 1286")
        self._other_names = []

 = EtaLeporis


class LambdaLeporis(FixedStar): # ,lamLep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamLep", context=context, swe_string="Lambda Leporis,lamLep,ICRS,05,19,34.52405,-13,10,36.4408,-3.3,-4.91,20.2,3.83,4.29,-13, 1127")
        self._other_names = []

 = LambdaLeporis


class MessierObjectu.Lep(FixedStar): # ,mu.Lep

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Lep", context=context, swe_string="Messier Object u.Lep,mu.Lep,ICRS,05,12,55.90168,-16,12,19.6885,47.09,-16.39,27.1,17.54,3.29,-16, 1072")
        self._other_names = []

 = MessierObjectu.Lep


class AlphaLibrae01(FixedStar): # ,alf01Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf01Lib", context=context, swe_string="Alpha Librae 01,alf01Lib,ICRS,14,50,41.18097,-15,59,50.0482,-136.27,-59.04,-23.47,43.52,5.16,-15, 3965")
        self._other_names = []

 = AlphaLibrae01


class AlphaLibrae02(FixedStar): # ,alf02Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf02Lib", context=context, swe_string="Alpha Librae 02,alf02Lib,ICRS,14,50,52.71309,-16,02,30.3955,-105.68,-68.4,-10,43.03,2.75, -15, 3966")
        self._other_names = ['Zubenelgenubi']

Zubenelgenubi = AlphaLibrae02


class AlphaLibrae02(FixedStar): # ,alf02Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alf02Lib", context=context, swe_string="Alpha Librae 02,alf02Lib,ICRS,14,50,52.71309,-16,02,30.3955,-105.68,-68.4,-10,43.03,2.75, -15, 3966")
        self._other_names = ['Zuben Elgenubi']

ZubenElgenubi = AlphaLibrae02


class BetaLibrae(FixedStar): # ,betLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLib", context=context, swe_string="Beta Librae,betLib,ICRS,15,17,00.41382,-09,22,58.4919,-98.1,-19.65,-35.6,17.62,2.62,-08, 3935")
        self._other_names = ['Zubeneshamali']

Zubeneshamali = BetaLibrae


class BetaLibrae(FixedStar): # ,betLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLib", context=context, swe_string="Beta Librae,betLib,ICRS,15,17,00.41382,-09,22,58.4919,-98.1,-19.65,-35.6,17.62,2.62,-08, 3935")
        self._other_names = ['Zuben Eschamali']

ZubenEschamali = BetaLibrae


class GammaLibrae(FixedStar): # ,gamLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamLib", context=context, swe_string="Gamma Librae,gamLib,ICRS,15,35,31.57881,-14,47,22.3278,65.34,7.45,-26.71,19.99,3.91,-14, 4237")
        self._other_names = ['Zubenelakrab']

Zubenelakrab = GammaLibrae


class GammaLibrae(FixedStar): # ,gamLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamLib", context=context, swe_string="Gamma Librae,gamLib,ICRS,15,35,31.57881,-14,47,22.3278,65.34,7.45,-26.71,19.99,3.91,-14, 4237")
        self._other_names = ['Zubenelhakrabi']

Zubenelhakrabi = GammaLibrae


class GammaLibrae(FixedStar): # ,gamLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamLib", context=context, swe_string="Gamma Librae,gamLib,ICRS,15,35,31.57881,-14,47,22.3278,65.34,7.45,-26.71,19.99,3.91,-14, 4237")
        self._other_names = ['Zuben Elakrab']

ZubenElakrab = GammaLibrae


class DeltaLibrae(FixedStar): # ,delLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delLib", context=context, swe_string="Delta Librae,delLib,ICRS,15,00,58.35013,-08,31,08.2063,-63.46,-4.76,-38.7,11.11,4.93,-07, 3938")
        self._other_names = ['Zubenelakribi']

Zubenelakribi = DeltaLibrae


class DeltaLibrae(FixedStar): # ,delLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delLib", context=context, swe_string="Delta Librae,delLib,ICRS,15,00,58.35013,-08,31,08.2063,-63.46,-4.76,-38.7,11.11,4.93,-07, 3938")
        self._other_names = ['Zuben Elakribi']

ZubenElakribi = DeltaLibrae


class ZetaLibrae01(FixedStar): # ,zet01Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zet01Lib", context=context, swe_string="Zeta Librae 01,zet01Lib,ICRS,15,28,15.40806,-16,42,59.3552,16.3,-34.6,-21.4,4.16,5.626,-16, 4089")
        self._other_names = []

 = ZetaLibrae01


class IotaLibrae01(FixedStar): # ,iot01Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iot01Lib", context=context, swe_string="Iota Librae 01,iot01Lib,ICRS,15,12,13.29025,-19,47,30.1592,-35.4,-32.79,-11.6,8.59,4.54,-19, 4047")
        self._other_names = ['Vishakha']

Vishakha = IotaLibrae01


class IotaLibrae01(FixedStar): # ,iot01Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iot01Lib", context=context, swe_string="Iota Librae 01,iot01Lib,ICRS,15,12,13.29025,-19,47,30.1592,-35.4,-32.79,-11.6,8.59,4.54,-19, 4047")
        self._other_names = []

 = IotaLibrae01


class KappaLibrae(FixedStar): # ,kapLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapLib", context=context, swe_string="Kappa Librae,kapLib,ICRS,15,41,56.79858,-19,40,43.7745,-32.06,-103.15,-4.5,10.57,4.72,-19, 4188")
        self._other_names = []

 = KappaLibrae


class LambdaLibrae(FixedStar): # ,lamLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamLib", context=context, swe_string="Lambda Librae,lamLib,ICRS,15,53,20.05463,-20,10,01.4177,-9.81,-26.85,-2,10.54,5.027,-19, 4249")
        self._other_names = []

 = LambdaLibrae


class NuLibrae(FixedStar): # ,nu.Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Lib", context=context, swe_string="Nu Librae,nu.Lib,ICRS,15,06,37.59655,-16,15,24.5369,-35.9,-22.37,-15.1,4.69,5.2,-15, 4026")
        self._other_names = ['Zubenhakrabi']

Zubenhakrabi = NuLibrae


class NuLibrae(FixedStar): # ,nu.Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Lib", context=context, swe_string="Nu Librae,nu.Lib,ICRS,15,06,37.59655,-16,15,24.5369,-35.9,-22.37,-15.1,4.69,5.2,-15, 4026")
        self._other_names = ['Zuben Hakrabi']

ZubenHakrabi = NuLibrae


class XiLibrae02(FixedStar): # ,ksi02Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksi02Lib", context=context, swe_string="Xi Librae 02,ksi02Lib,ICRS,14,56,46.11227,-11,24,34.9384,8.63,9.35,14.6,5.94,5.45,-10, 3989")
        self._other_names = []

 = XiLibrae02


class SigmaLibrae(FixedStar): # ,sigLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigLib", context=context, swe_string="Sigma Librae,sigLib,ICRS,15,04,04.21608,-25,16,55.0606,-71.16,-43.34,-3.9,11.31,3.21,-24,11834")
        self._other_names = ['Brachium']

Brachium = SigmaLibrae


class TauLibrae(FixedStar): # ,tauLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauLib", context=context, swe_string="Tau Librae,tauLib,ICRS,15,38,39.36950,-29,46,39.8956,-22.08,-24.46,3.2,8.89,3.642,0,0")
        self._other_names = []

 = TauLibrae


class UpsilonLibrae(FixedStar): # ,upsLib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsLib", context=context, swe_string="Upsilon Librae,upsLib,ICRS,15,37,01.45020,-28,08,06.2926,-12.82,-4.15,-24.9,14.58,3.589,-27,10464")
        self._other_names = []

 = UpsilonLibrae


class BetaLeonisMinoris(FixedStar): # ,betLMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLMi", context=context, swe_string="Beta Leonis Minoris,betLMi,ICRS,10,27,52.99960,+36,42,25.9561,-127.68,-110.31,6.34,21.19,4.21, 37, 2080")
        self._other_names = []

 = BetaLeonisMinoris


class LeonisMinoris46(FixedStar): # ,46LMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",46LMi", context=context, swe_string="Leonis Minoris46,46LMi,ICRS,10,53,18.70487,+34,12,53.5375,92.02,-285.82,15.69,34.38,3.83, 34, 2172")
        self._other_names = ['Praecipua']

Praecipua = LeonisMinoris46


class LeonisMinoris21(FixedStar): # ,21LMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",21LMi", context=context, swe_string="Leonis Minoris21,21LMi,ICRS,10,07,25.76296,+35,14,40.8965,52.9,0.62,-11.4,35.41,4.49,0,0")
        self._other_names = []

 = LeonisMinoris21


class AlphaLupi(FixedStar): # ,alfLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLup", context=context, swe_string="Alpha Lupi,alfLup,ICRS,14,41,55.75579,-47,23,17.5155,-20.94,-23.67,5.4,7.02,2.286,-46, 9501")
        self._other_names = ['Kakkab']

Kakkab = AlphaLupi


class AlphaLupi(FixedStar): # ,alfLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLup", context=context, swe_string="Alpha Lupi,alfLup,ICRS,14,41,55.75579,-47,23,17.5155,-20.94,-23.67,5.4,7.02,2.286,-46, 9501")
        self._other_names = ['Men']

Men = AlphaLupi


class BetaLupi(FixedStar): # ,betLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLup", context=context, swe_string="Beta Lupi,betLup,ICRS,14,58,31.92536,-43,08,02.2699,-35.78,-39.83,0.2,8.52,2.68,-42, 9853")
        self._other_names = ['Kekouan']

Kekouan = BetaLupi


class GammaLupi(FixedStar): # ,gamLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamLup", context=context, swe_string="Gamma Lupi,gamLup,ICRS,15,35,08.44835,-41,10,00.3247,-15.62,-25.43,2.3,7.75,2.765,0,0")
        self._other_names = ['Thusia']

Thusia = GammaLupi


class DeltaLupi(FixedStar): # ,delLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delLup", context=context, swe_string="Delta Lupi,delLup,ICRS,15,21,22.32168,-40,38,51.0738,-19.49,-25.29,-2.4,3.69,3.19,-40, 9538")
        self._other_names = ['Hilasmus']

Hilasmus = DeltaLupi


class EpsilonLupi(FixedStar): # ,epsLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsLup", context=context, swe_string="Epsilon Lupi,epsLup,ICRS,15,22,40.86826,-44,41,22.6146,-22.86,-18.87,7.9,6.37,3.366,0,0")
        self._other_names = []

 = EpsilonLupi


class EtaLupi(FixedStar): # ,etaLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaLup", context=context, swe_string="Eta Lupi,etaLup,ICRS,16,00,07.32786,-38,23,48.1513,-16.96,-27.83,1,7.38,3.41,0,0")
        self._other_names = []

 = EtaLupi


class ZetaLupi(FixedStar): # ,zetLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetLup", context=context, swe_string="Zeta Lupi,zetLup,ICRS,15,12,17.09595,-52,05,57.2919,-112.92,-71.18,-10,27.8,3.41,-51, 8830")
        self._other_names = []

 = ZetaLupi


class ThetaLupi(FixedStar): # ,tetLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetLup", context=context, swe_string="Theta Lupi,tetLup,ICRS,16,06,35.54525,-36,48,08.2653,-15.33,-33.83,15.2,7.87,4.201,-36,10642")
        self._other_names = []

 = ThetaLupi


class KappaLupi01(FixedStar): # ,kap01Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kap01Lup", context=context, swe_string="Kappa Lupi 01,kap01Lup,ICRS,15,11,56.07286,-48,44,16.1692,-96.5,-49.86,-6.6,18.12,3.7,-48, 9704")
        self._other_names = []

 = KappaLupi01


class KappaLupi02(FixedStar): # ,kap02Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kap02Lup", context=context, swe_string="Kappa Lupi 02,kap02Lup,ICRS,15,11,57.6755,-48,44,37.268,-98.566,-43.729,0,17.5,5.498,0,0")
        self._other_names = []

 = KappaLupi02


class PhiLupi01(FixedStar): # ,phi01Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phi01Lup", context=context, swe_string="Phi Lupi 01,phi01Lup,ICRS,15,21,48.36967,-36,15,40.9525,-92.33,-85.67,-29.4,11.86,3.546,-35,10236")
        self._other_names = []

 = PhiLupi01


class PhiLupi02(FixedStar): # ,phi02Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phi02Lup", context=context, swe_string="Phi Lupi 02,phi02Lup,ICRS,15,23,09.35005,-36,51,30.5521,-18.24,-20.72,0.8,6.28,4.54,-36,10103")
        self._other_names = []

 = PhiLupi02


class TauLupi01(FixedStar): # ,tau01Lup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau01Lup", context=context, swe_string="Tau Lupi 01,tau01Lup,ICRS,14,26,08.22424,-45,13,17.1315,-13.09,-14.67,-215,2.99,4.553,-44, 9322")
        self._other_names = []

 = TauLupi01


class ChiLupi(FixedStar): # ,chiLup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiLup", context=context, swe_string="Chi Lupi,chiLup,ICRS,15,50,57.53829,-33,37,37.7953,-5.1,-24.85,-16.3,16.71,3.946,-33,10754")
        self._other_names = []

 = ChiLupi


class AlphaLyncis(FixedStar): # ,alfLyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLyn", context=context, swe_string="Alpha Lyncis,alfLyn,ICRS,09,21,03.30074,+34,23,33.2245,-223.63,15.18,38.47,16.06,3.14, 35, 1979")
        self._other_names = ['Alvashak']

Alvashak = AlphaLyncis


class AlphaLyncis(FixedStar): # ,alfLyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLyn", context=context, swe_string="Alpha Lyncis,alfLyn,ICRS,09,21,03.30074,+34,23,33.2245,-223.63,15.18,38.47,16.06,3.14, 35, 1979")
        self._other_names = ['Al Fahd']

AlFahd = AlphaLyncis


class Lyncis31(FixedStar): # ,31Lyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",31Lyn", context=context, swe_string="Lyncis31,31Lyn,ICRS,08,22,50.11000,+43,11,17.2724,-25.16,-99.23,24.56,8.53,4.25, 43, 1815")
        self._other_names = ['Alsciaukat']

Alsciaukat = Lyncis31


class Lyncis31(FixedStar): # ,31Lyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",31Lyn", context=context, swe_string="Lyncis31,31Lyn,ICRS,08,22,50.11000,+43,11,17.2724,-25.16,-99.23,24.56,8.53,4.25, 43, 1815")
        self._other_names = ['Mabsuthat']

Mabsuthat = Lyncis31


class KappaLyncis(FixedStar): # ,kapLyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapLyn", context=context, swe_string="Kappa Lyncis,kapLyn,ICRS,08,22,50.1096,+43,11,17.270,-25.62,-99.44,24.56,8.39,4.258, 43, 1815")
        self._other_names = ['Mabsuthat']

Mabsuthat = KappaLyncis


class Lyncis38(FixedStar): # ,38Lyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",38Lyn", context=context, swe_string="Lyncis38,38Lyn,ICRS,09,18,50.64384,+36,48,09.3331,-32.33,-125.64,4,26.13,3.82, 0, 0")
        self._other_names = ['Maculosa']

Maculosa = Lyncis38


class Lyncis38(FixedStar): # ,38Lyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",38Lyn", context=context, swe_string="Lyncis38,38Lyn,ICRS,09,18,50.64384,+36,48,09.3331,-32.33,-125.64,4,26.13,3.82, 0, 0")
        self._other_names = ['Maculata']

Maculata = Lyncis38


class Lyncis21(FixedStar): # ,21Lyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",21Lyn", context=context, swe_string="Lyncis21,21Lyn,ICRS,07,26,42.85187,+49,12,41.4907,-10.22,-49.29,26.8,11.92,4.61,0, 0")
        self._other_names = []

 = Lyncis21


class Lyncis15(FixedStar): # ,15Lyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",15Lyn", context=context, swe_string="Lyncis15,15Lyn,ICRS,06,57,16.60526,+58,25,21.9404,6.08,-122.83,1.28,18.29,4.35,0,0")
        self._other_names = []

 = Lyncis15


class Lyncis2(FixedStar): # ,2Lyn

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",2Lyn", context=context, swe_string="Lyncis2,2Lyn,ICRS,06,19,37.38458,+59,00,39.4683,-5.35,23.86,-2,20.83,4.434,0,0")
        self._other_names = []

 = Lyncis2


class AlphaLyrae(FixedStar): # ,alfLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLyr", context=context, swe_string="Alpha Lyrae,alfLyr,ICRS,18,36,56.33635,+38,47,01.2802,200.94,286.23,-20.6,130.23,0.03, 38, 3238")
        self._other_names = ['Vega']

Vega = AlphaLyrae


class AlphaLyrae(FixedStar): # ,alfLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLyr", context=context, swe_string="Alpha Lyrae,alfLyr,ICRS,18,36,56.33635,+38,47,01.2802,200.94,286.23,-20.6,130.23,0.03, 38, 3238")
        self._other_names = ['Abhijit']

Abhijit = AlphaLyrae


class BetaLyrae(FixedStar): # ,betLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLyr", context=context, swe_string="Beta Lyrae,betLyr,ICRS,18,50,04.79525,+33,21,45.6100,1.9,-3.53,2.2,3.39,3.42, 33, 3223")
        self._other_names = ['Sheliak']

Sheliak = BetaLyrae


class GammaLyrae(FixedStar): # ,gamLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamLyr", context=context, swe_string="Gamma Lyrae,gamLyr,ICRS,18,58,56.62241,+32,41,22.4003,-3.09,1.11,-20.2,5.26,3.25, 32, 3286")
        self._other_names = ['Sulaphat']

Sulaphat = GammaLyrae


class GammaLyrae(FixedStar): # ,gamLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamLyr", context=context, swe_string="Gamma Lyrae,gamLyr,ICRS,18,58,56.62241,+32,41,22.4003,-3.09,1.11,-20.2,5.26,3.25, 32, 3286")
        self._other_names = ['Sulafat']

Sulafat = GammaLyrae


class EtaLyrae(FixedStar): # ,etaLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaLyr", context=context, swe_string="Eta Lyrae,etaLyr,ICRS,19,13,45.48832,+39,08,45.4801,-0.6,-1.26,-8.1,2.35,4.398, 38, 3490")
        self._other_names = ['Aladfar']

Aladfar = EtaLyrae


class ThetaLyrae(FixedStar): # ,tetLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetLyr", context=context, swe_string="Theta Lyrae,tetLyr,ICRS,19,16,22.09487,+38,08,01.4234,-0.8,0.36,-27.42,3.92,4.38, 37, 3398")
        self._other_names = []

 = ThetaLyrae


class IotaLyrae(FixedStar): # ,iotLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotLyr", context=context, swe_string="Iota Lyrae,iotLyr,ICRS,19,07,18.12878,+36,06,00.5654,-1.04,-4.29,-26,3.64,5.253, 35, 3485")
        self._other_names = []

 = IotaLyrae


class KappaLyrae(FixedStar): # ,kapLyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapLyr", context=context, swe_string="Kappa Lyrae,kapLyr,ICRS,18,19,51.70908,+36,03,52.3691,-16.75,41.09,-24.36,12.96,4.34, 36, 3094")
        self._other_names = []

 = KappaLyrae


class MessierObjectu.Lyr(FixedStar): # ,mu.Lyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Lyr", context=context, swe_string="Messier Object u.Lyr,mu.Lyr,ICRS,18,24,13.78580,+39,30,26.0562,-21.14,-4.91,-24,7.43,5.12, 39, 3410")
        self._other_names = ['Alathfar']

Alathfar = MessierObjectu.Lyr


class MessierObjectu.Lyr(FixedStar): # ,mu.Lyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Lyr", context=context, swe_string="Messier Object u.Lyr,mu.Lyr,ICRS,18,24,13.78580,+39,30,26.0562,-21.14,-4.91,-24,7.43,5.12, 39, 3410")
        self._other_names = ['Al Athfar']

AlAthfar = MessierObjectu.Lyr


class ZetaLyrae02(FixedStar): # ,zet02Lyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zet02Lyr", context=context, swe_string="Zeta Lyrae 02,zet02Lyr,ICRS,18,44,48.20367,+37,35,40.6162,18.7,20.98,-25,20.97,5.585,39,3410")
        self._other_names = []

 = ZetaLyrae02


class DeltaLyrae02(FixedStar): # ,del02Lyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del02Lyr", context=context, swe_string="Delta Lyrae 02,del02Lyr,ICRS,18,54,30.28335,+36,53,55.0133,-7.36,4.06,-25.55,4.43,4.3,39,3410")
        self._other_names = []

 = DeltaLyrae02


class EpsilonLyrae02(FixedStar): # ,eps02Lyr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eps02Lyr", context=context, swe_string="Epsilon Lyrae 02,eps02Lyr,ICRS,18,44,22.78056,+39,36,45.7851,6.18,50.42,-24.4,20.97,4.59,0,0")
        self._other_names = []

 = EpsilonLyrae02


class AlphaMensae(FixedStar): # ,alfMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfMen", context=context, swe_string="Alpha Mensae,alfMen,ICRS,06,10,14.47353,-74,45,10.9583,121.8,-212.34,34.9,98.06,5.09,-74,  374")
        self._other_names = []

 = AlphaMensae


class BetaMensae(FixedStar): # ,betMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betMen", context=context, swe_string="Beta Mensae,betMen,ICRS,05,02,42.99714,-71,18,51.4842,-4.24,10.22,-11.4,4.11,5.294,-74,374")
        self._other_names = []

 = BetaMensae


class GammaMensae(FixedStar): # ,gamMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamMen", context=context, swe_string="Gamma Mensae,gamMen,ICRS,05,31,53.01393,-76,20,27.4779,142.5,286.85,56.7,31.89,5.2,-76,  333")
        self._other_names = []

 = GammaMensae


class DeltaMensae(FixedStar): # ,delMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delMen", context=context, swe_string="Delta Mensae,delMen,ICRS,04,17,59.2718,-80,12,50.511,27.719,61.679,-20,7.7,5.68,-80,  116")
        self._other_names = []

 = DeltaMensae


class EtaMensae(FixedStar): # ,etaMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaMen", context=context, swe_string="Eta Mensae,etaMen,ICRS,04,55,11.20309,-74,56,12.6705,28.27,61.52,25.8,4.88,5.449,-75,  290")
        self._other_names = []

 = EtaMensae


class ZetaMensae(FixedStar): # ,zetMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetMen", context=context, swe_string="Zeta Mensae,zetMen,ICRS,06,40,02.89028,-80,48,48.9399,-4.97,52.73,7,7.88,5.606,-80,  196")
        self._other_names = []

 = ZetaMensae


class MessierObjectu.Men(FixedStar): # ,mu.Men

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Men", context=context, swe_string="Messier Object u.Men,mu.Men,ICRS,04,43,03.96347,-70,55,51.6976,9.32,34.93,-0.2,6.64,5.511,-71,  282")
        self._other_names = []

 = MessierObjectu.Men


class XiMensae(FixedStar): # ,ksiMen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiMen", context=context, swe_string="Xi Mensae,ksiMen,ICRS,04,58,50.9671,-82,28,13.856,-4.56,2.926,-5,8.84,5.828,-82,  106")
        self._other_names = []

 = XiMensae


class AlphaMicroscopii(FixedStar): # ,alfMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfMic", context=context, swe_string="Alpha Microscopii,alfMic,ICRS,20,49,58.08012,-33,46,47.0068,0.76,-21.07,-14.5,8.62,4.89,0,0")
        self._other_names = []

 = AlphaMicroscopii


class GammaMicroscopii(FixedStar): # ,gamMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamMic", context=context, swe_string="Gamma Microscopii,gamMic,ICRS,21,01,17.46047,-32,15,27.9574,-1.73,0.41,17.6,14.24,4.654,-32,16353")
        self._other_names = []

 = GammaMicroscopii


class EpsilonMicroscopii(FixedStar): # ,epsMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsMic", context=context, swe_string="Epsilon Microscopii,epsMic,ICRS,21,17,56.28399,-32,10,21.1515,54.36,-23.29,7.2,17.9,4.708,-32,16498")
        self._other_names = []

 = EpsilonMicroscopii


class ZetaMicroscopii(FixedStar): # ,zetMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetMic", context=context, swe_string="Zeta Microscopii,zetMic,ICRS,21,02,57.95290,-38,37,53.2099,-29.16,-108.85,4.6,28.27,5.305,-39,14089")
        self._other_names = []

 = ZetaMicroscopii


class ThetaMicroscopii01(FixedStar): # ,tet01Mic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet01Mic", context=context, swe_string="Theta Microscopii 01,tet01Mic,ICRS,21,20,45.63900,-40,48,34.0512,71.92,20.38,2.3,16.54,4.82,-41,14475")
        self._other_names = []

 = ThetaMicroscopii01


class IotaMicroscopii(FixedStar): # ,iotMic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotMic", context=context, swe_string="Iota Microscopii,iotMic,ICRS,20,48,29.13901,-43,59,18.7397,172.34,-109.61,-14.9,28.23,5.13,-44,14145")
        self._other_names = []

 = IotaMicroscopii


class AlphaMonocerotis(FixedStar): # ,alfMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfMon", context=context, swe_string="Alpha Monocerotis,alfMon,ICRS,07,41,14.83257,-09,33,04.0711,-74.61,-19.59,11.66,22.07,3.93,-09, 2172")
        self._other_names = []

 = AlphaMonocerotis


class BetaMonocerotis(FixedStar): # ,betMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betMon", context=context, swe_string="Beta Monocerotis,betMon,ICRS,06,28,49.06971,-07,01,59.0101,-6.86,-2.76,17.2,4.82,3.74,0,0")
        self._other_names = []

 = BetaMonocerotis


class GammaMonocerotis(FixedStar): # ,gamMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamMon", context=context, swe_string="Gamma Monocerotis,gamMon,ICRS,06,14,51.33367,-06,16,29.1880,-4.69,-19.3,-4.8,6.55,3.96,0,0")
        self._other_names = []

 = GammaMonocerotis


class DeltaMonocerotis(FixedStar): # ,delMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delMon", context=context, swe_string="Delta Monocerotis,delMon,ICRS,07,11,51.860,-00,29,33.96,0.79,4.52,15,8.49,4.15,-00, 1636")
        self._other_names = []

 = DeltaMonocerotis


class EpsilonMonocerotis(FixedStar): # ,epsMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsMon", context=context, swe_string="Epsilon Monocerotis,epsMon,ICRS,06,23,46.08471,+04,35,34.3153,-22.06,10.91,13.1,26.67,4.398, 04, 1236")
        self._other_names = []

 = EpsilonMonocerotis


class ZetaMonocerotis(FixedStar): # ,zetMon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetMon", context=context, swe_string="Zeta Monocerotis,zetMon,ICRS,08,08,35.64663,-02,59,01.6361,-18.81,-4.5,29.8,3.08,4.33,0,0")
        self._other_names = []

 = ZetaMonocerotis


class Monocerotis18(FixedStar): # ,18Mon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",18Mon", context=context, swe_string="Monocerotis18,18Mon,ICRS,06,47,51.64956,+02,24,43.7737,-12.41,-12.12,11.29,8.86,4.47,0,0")
        self._other_names = []

 = Monocerotis18


class Monocerotis13(FixedStar): # ,13Mon

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",13Mon", context=context, swe_string="Monocerotis13,13Mon,ICRS,06,32,54.22948,+07,19,58.6942,-0.2,-3.48,11.8,0.83,4.5,0,0")
        self._other_names = []

 = Monocerotis13


class AlphaMuscae(FixedStar): # ,alfMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfMus", context=context, swe_string="Alpha Muscae,alfMus,ICRS,12,37,11.01789,-69,08,08.0332,-40.2,-12.8,13,10.34,2.649,-68, 1702")
        self._other_names = []

 = AlphaMuscae


class BetaMuscae(FixedStar): # ,betMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betMus", context=context, swe_string="Beta Muscae,betMus,ICRS,12,46,16.80410,-68,06,29.2164,-41.97,-8.89,42,9.55,3.07,0,0")
        self._other_names = []

 = BetaMuscae


class GammaMuscae(FixedStar): # ,gamMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamMus", context=context, swe_string="Gamma Muscae,gamMus,ICRS,12,32,28.01343,-72,07,58.7597,-51.34,-5.4,2.5,10.04,3.88,-71, 1336")
        self._other_names = []

 = GammaMuscae


class DeltaMuscae(FixedStar): # ,delMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delMus", context=context, swe_string="Delta Muscae,delMus,ICRS,13,02,16.26474,-71,32,55.8752,264.17,-22.75,36.5,35.88,3.62,-70, 1548")
        self._other_names = []

 = DeltaMuscae


class EpsilonMuscae(FixedStar): # ,epsMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsMus", context=context, swe_string="Epsilon Muscae,epsMus,ICRS,12,17,34.27716,-67,57,38.6486,-231.04,-26.39,7.1,10.82,4.02,0,0")
        self._other_names = []

 = EpsilonMuscae


class EtaMuscae(FixedStar): # ,etaMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaMus", context=context, swe_string="Eta Muscae,etaMus,ICRS,13,15,14.94123,-67,53,40.5276,-36.46,-11.36,-8,8.52,4.774,-67, 2224")
        self._other_names = []

 = EtaMuscae


class LambdaMuscae(FixedStar): # ,lamMus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamMus", context=context, swe_string="Lambda Muscae,lamMus,ICRS,11,45,36.41916,-66,43,43.5440,-100.35,33.49,15,25.65,3.65,-66, 1640")
        self._other_names = []

 = LambdaMuscae


class MessierObjectu.Mus(FixedStar): # ,mu.Mus

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Mus", context=context, swe_string="Messier Object u.Mus,mu.Mus,ICRS,11,48,14.53576,-66,48,53.6688,31.25,-15.25,37.4,7.59,4.728,0,0")
        self._other_names = []

 = MessierObjectu.Mus


class GammaNormae02(FixedStar): # ,gam02Nor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam02Nor", context=context, swe_string="Gamma Normae 02,gam02Nor,ICRS,16,19,50.42227,-50,09,19.8223,-159.71,-52.25,-28.9,25.33,4.02,-49,10536")
        self._other_names = []

 = GammaNormae02


class DeltaNormae(FixedStar): # ,delNor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delNor", context=context, swe_string="Delta Normae,delNor,ICRS,16,06,29.43692,-45,10,23.4518,16.19,38.45,-15.5,26.66,4.713,-44,10625")
        self._other_names = []

 = DeltaNormae


class EpsilonNormae(FixedStar): # ,epsNor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsNor", context=context, swe_string="Epsilon Normae,epsNor,ICRS,16,27,11.03611,-47,33,17.2226,-13.68,-19.89,-12.5,6.15,4.521,0,0")
        self._other_names = []

 = EpsilonNormae


class EtaNormae(FixedStar): # ,etaNor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaNor", context=context, swe_string="Eta Normae,etaNor,ICRS,16,03,12.89783,-49,13,46.9151,42.05,9.14,-0.3,14.86,4.643,0,0")
        self._other_names = []

 = EtaNormae


class KappaNormae(FixedStar): # ,kapNor

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapNor", context=context, swe_string="Kappa Normae,kapNor,ICRS,16,13,28.72926,-54,37,49.6865,-5.14,-22.86,-13.5,7.62,4.94,-54, 7245")
        self._other_names = []

 = KappaNormae


class AlphaOctantis(FixedStar): # ,alfOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfOct", context=context, swe_string="Alpha Octantis,alfOct,ICRS,21,04,43.06183,-77,01,25.5607,12.74,-369.24,85.9,22.97,5.15,-77, 1474")
        self._other_names = []

 = AlphaOctantis


class BetaOctantis(FixedStar): # ,betOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betOct", context=context, swe_string="Beta Octantis,betOct,ICRS,22,46,03.51098,-81,22,53.8120,-54.49,1.16,19,21.85,4.128,-82,  889")
        self._other_names = []

 = BetaOctantis


class GammaOctantis01(FixedStar): # ,gam01Oct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam01Oct", context=context, swe_string="Gamma Octantis 01,gam01Oct,ICRS,23,52,06.48895,-82,01,07.7489,-48.74,-21.16,15.4,12.3,5.106,0,0")
        self._other_names = []

 = GammaOctantis01


class DeltaOctantis(FixedStar): # ,delOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delOct", context=context, swe_string="Delta Octantis,delOct,ICRS,14,26,55.23244,-83,40,04.3868,-96.12,-13.27,4.6,10.91,4.304,0,0")
        self._other_names = []

 = DeltaOctantis


class EtaOctantis(FixedStar): # ,etaOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaOct", context=context, swe_string="Eta Octantis,etaOct,ICRS,10,59,13.7579,-84,35,38.017,-65.768,-8.319,-1.7,9.48,6.185,-83,  386")
        self._other_names = []

 = EtaOctantis


class EpsilonOctantis(FixedStar): # ,epsOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsOct", context=context, swe_string="Epsilon Octantis,epsOct,ICRS,22,20,01.67970,-80,26,23.0947,56.81,-43.47,11.7,11.22,5.177,-81,  995")
        self._other_names = []

 = EpsilonOctantis


class ThetaOctantis(FixedStar): # ,tetOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetOct", context=context, swe_string="Theta Octantis,tetOct,ICRS,00,01,35.70158,-77,03,56.6092,-57.3,-177.06,22.6,15.02,4.783,-77, 1596")
        self._other_names = []

 = ThetaOctantis


class ZetaOctantis(FixedStar): # ,zetOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetOct", context=context, swe_string="Zeta Octantis,zetOct,ICRS,08,56,40.98151,-85,39,47.3440,-116.93,34.19,-3.6,20.1,5.419,-85,  183")
        self._other_names = []

 = ZetaOctantis


class IotaOctantis(FixedStar): # ,iotOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotOct", context=context, swe_string="Iota Octantis,iotOct,ICRS,12,54,58.80949,-85,07,24.1041,67.2,24.76,53.4,9.27,5.519,-84,  407")
        self._other_names = []

 = IotaOctantis


class KappaOctantis(FixedStar): # ,kapOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapOct", context=context, swe_string="Kappa Octantis,kapOct,ICRS,13,40,55.47484,-85,47,09.7544,-88.24,-20.79,-9,11.94,5.555,-85,  384")
        self._other_names = []

 = KappaOctantis


class NuOctantis(FixedStar): # ,nu.Oct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Oct", context=context, swe_string="Nu Octantis,nu.Oct,ICRS,21,41,28.64977,-77,23,24.1563,66.41,-239.1,34.4,45.25,3.743,-77, 1510")
        self._other_names = []

 = NuOctantis


class RhoOctantis(FixedStar): # ,rhoOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoOct", context=context, swe_string="Rho Octantis,rhoOct,ICRS,15,43,16.93158,-84,27,54.9932,137.34,95.52,-11,15.12,5.568,-84,  510")
        self._other_names = []

 = RhoOctantis


class SigmaOctantis(FixedStar): # ,sigOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigOct", context=context, swe_string="Sigma Octantis,sigOct,ICRS,21,08,46.83929,-88,57,23.3966,25.75,4.98,11.9,11.61,5.42,-89,   47")
        self._other_names = ['Polaris Australis']

PolarisAustralis = SigmaOctantis


class TauOctantis(FixedStar): # ,tauOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauOct", context=context, swe_string="Tau Octantis,tauOct,ICRS,23,28,03.78961,-87,28,55.9695,16.83,11.56,31,6.71,5.49,-88,  204")
        self._other_names = []

 = TauOctantis


class UpsilonOctantis(FixedStar): # ,upsOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsOct", context=context, swe_string="Upsilon Octantis,upsOct,ICRS,22,31,37.52015,-85,58,02.1108,-37.08,61.28,19,10.06,5.752,-86,  406")
        self._other_names = []

 = UpsilonOctantis


class ChiOctantis(FixedStar): # ,chiOct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiOct", context=context, swe_string="Chi Octantis,chiOct,ICRS,18,54,47.13316,-87,36,21.0337,-36.88,-134.96,33.6,12.7,5.278,-87,  274")
        self._other_names = []

 = ChiOctantis


class AlphaOphiuci(FixedStar): # ,alfOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfOph", context=context, swe_string="Alpha Ophiuci,alfOph,ICRS,17,34,56.06945,+12,33,36.1346,108.07,-221.57,11.7,67.13,2.07, 12, 3252")
        self._other_names = ['Rasalhague']

Rasalhague = AlphaOphiuci


class BetaOphiuci(FixedStar): # ,betOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betOph", context=context, swe_string="Beta Ophiuci,betOph,ICRS,17,43,28.35265,+04,34,02.2955,-41.45,159.34,-12.53,39.85,2.75, 04, 3489")
        self._other_names = ['Celbalrai']

Celbalrai = BetaOphiuci


class BetaOphiuci(FixedStar): # ,betOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betOph", context=context, swe_string="Beta Ophiuci,betOph,ICRS,17,43,28.35265,+04,34,02.2955,-41.45,159.34,-12.53,39.85,2.75, 04, 3489")
        self._other_names = ['Cebalrai']

Cebalrai = BetaOphiuci


class BetaOphiuci(FixedStar): # ,betOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betOph", context=context, swe_string="Beta Ophiuci,betOph,ICRS,17,43,28.35265,+04,34,02.2955,-41.45,159.34,-12.53,39.85,2.75, 04, 3489")
        self._other_names = ['Kelb Alrai']

KelbAlrai = BetaOphiuci


class GammaOphiuci(FixedStar): # ,gamOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamOph", context=context, swe_string="Gamma Ophiuci,gamOph,ICRS,17,47,53.55973,+02,42,26.2000,-24.64,-74.42,-7.6,31.73,3.75, 02, 3403")
        self._other_names = ['Al Durajah']

AlDurajah = GammaOphiuci


class DeltaOphiuci(FixedStar): # ,delOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delOph", context=context, swe_string="Delta Ophiuci,delOph,ICRS,16,14,20.73853,-03,41,39.5612,-47.54,-142.73,-19.27,19.06,2.75,-03, 3903")
        self._other_names = ['Yed Prior']

YedPrior = DeltaOphiuci


class EpsilonOphiuci(FixedStar): # ,epsOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsOph", context=context, swe_string="Epsilon Ophiuci,epsOph,ICRS,16,18,19.28974,-04,41,33.0345,83.4,40.58,-9.18,30.64,3.23,-04, 4086")
        self._other_names = ['Yed Posterior']

YedPosterior = EpsilonOphiuci


class ZetaOphiuci(FixedStar): # ,zetOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetOph", context=context, swe_string="Zeta Ophiuci,zetOph,ICRS,16,37,09.53905,-10,34,01.5295,15.26,24.79,-9,8.91,2.56,-10, 4350")
        self._other_names = ['Han']

Han = ZetaOphiuci


class EtaOphiuci(FixedStar): # ,etaOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaOph", context=context, swe_string="Eta Ophiuci,etaOph,ICRS,17,10,22.68689,-15,43,29.6639,40.13,99.17,-2.4,36.91,2.42,-15, 4467")
        self._other_names = ['Sabik']

Sabik = EtaOphiuci


class ThetaOphiuci(FixedStar): # ,tetOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetOph", context=context, swe_string="Theta Ophiuci,tetOph,ICRS,17,22,00.57935,-24,59,58.3670,-7.37,-23.94,-2.1,7.48,3.26,-24,13292")
        self._other_names = ['Imad']

Imad = ThetaOphiuci


class IotaOphiuci(FixedStar): # ,iotOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotOph", context=context, swe_string="Iota Ophiuci,iotOph,ICRS,16,54,00.47151,+10,09,55.2982,-53.8,-34.04,-19,13.3,4.38, 10, 3092")
        self._other_names = []

 = IotaOphiuci


class KappaOphiuci(FixedStar): # ,kapOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapOph", context=context, swe_string="Kappa Ophiuci,kapOph,ICRS,16,57,40.09785,+09,22,30.1126,-292.13,-10.38,-55.85,35.66,3.2, 09, 3298")
        self._other_names = ['Helkath']

Helkath = KappaOphiuci


class LambdaOphiuci(FixedStar): # ,lamOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamOph", context=context, swe_string="Lambda Ophiuci,lamOph,ICRS,16,30,54.82314,+01,59,02.1209,-30.98,-73.42,-16,18.84,3.9, 02, 3118")
        self._other_names = ['Marfik']

Marfik = LambdaOphiuci


class NuOphiuci(FixedStar): # ,nu.Oph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Oph", context=context, swe_string="Nu Ophiuci,nu.Oph,ICRS,17,59,01.59191,-09,46,25.0798,-9.48,-116.69,13.19,21.64,3.34,-09, 4632")
        self._other_names = ['Sinistra']

Sinistra = NuOphiuci


class XiOphiuci(FixedStar): # ,ksiOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiOph", context=context, swe_string="Xi Ophiuci,ksiOph,ICRS,17,21,00.37520,-21,06,46.5663,263.84,-205.85,-9.1,57.62,4.39,0, 0")
        self._other_names = []

 = XiOphiuci


class SigmaOphiuci(FixedStar): # ,sigOph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigOph", context=context, swe_string="Sigma Ophiuci,sigOph,ICRS,17,26,30.88004,+04,08,25.2940,0.72,7.03,-27.81,3.62,4.31, 04, 3422")
        self._other_names = []

 = SigmaOphiuci


class Ophiuci44(FixedStar): # ,44Oph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",44Oph", context=context, swe_string="Ophiuci44,44Oph,ICRS,17,26,22.21749,-24,10,31.1190,0.1,-118.18,-37.2,39.22,4.153, 0, 0")
        self._other_names = []

 = Ophiuci44


class Ophiuci45(FixedStar): # ,45Oph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",45Oph", context=context, swe_string="Ophiuci45,45Oph,ICRS,17,27,21.27571,-29,52,01.3262,17.08,-138.02,38,29.23,4.269, 0, 0")
        self._other_names = []

 = Ophiuci45


class AlphaOrionis(FixedStar): # ,alfOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfOri", context=context, swe_string="Alpha Orionis,alfOri,ICRS,05,55,10.30536,+07,24,25.4304,27.54,11.3,21.91,6.55,0.42, 07, 1055")
        self._other_names = ['Betelgeuse']

Betelgeuse = AlphaOrionis


class AlphaOrionis(FixedStar): # ,alfOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfOri", context=context, swe_string="Alpha Orionis,alfOri,ICRS,05,55,10.30536,+07,24,25.4304,27.54,11.3,21.91,6.55,0.42, 07, 1055")
        self._other_names = ['Beteigeuse']

Beteigeuse = AlphaOrionis


class AlphaOrionis(FixedStar): # ,alfOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfOri", context=context, swe_string="Alpha Orionis,alfOri,ICRS,05,55,10.30536,+07,24,25.4304,27.54,11.3,21.91,6.55,0.42, 07, 1055")
        self._other_names = ['Ardra']

Ardra = AlphaOrionis


class BetaOrionis(FixedStar): # ,betOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betOri", context=context, swe_string="Beta Orionis,betOri,ICRS,05,14,32.27210,-08,12,05.8981,1.31,0.5,17.8,3.78,0.13,-08, 1063")
        self._other_names = ['Rigel']

Rigel = BetaOrionis


class GammaOrionis(FixedStar): # ,gamOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamOri", context=context, swe_string="Gamma Orionis,gamOri,ICRS,05,25,07.86325,+06,20,58.9318,-8.11,-12.88,18.2,12.92,1.64, 06,  919")
        self._other_names = ['Bellatrix']

Bellatrix = GammaOrionis


class GammaOrionis(FixedStar): # ,gamOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamOri", context=context, swe_string="Gamma Orionis,gamOri,ICRS,05,25,07.86325,+06,20,58.9318,-8.11,-12.88,18.2,12.92,1.64, 06,  919")
        self._other_names = ['Durga']

Durga = GammaOrionis


class DeltaOrionis(FixedStar): # ,delOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delOri", context=context, swe_string="Delta Orionis,delOri,ICRS,05,32,00.40009,-00,17,56.7424,0.64,-0.69,18.5,4.71,2.41,-00,  983")
        self._other_names = ['Mintaka']

Mintaka = DeltaOrionis


class DeltaOrionis(FixedStar): # ,delOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delOri", context=context, swe_string="Delta Orionis,delOri,ICRS,05,32,00.40009,-00,17,56.7424,0.64,-0.69,18.5,4.71,2.41,-00,  983")
        self._other_names = ['Kumara']

Kumara = DeltaOrionis


class EpsilonOrionis(FixedStar): # ,epsOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsOri", context=context, swe_string="Epsilon Orionis,epsOri,ICRS,05,36,12.81335,-01,12,06.9089,1.44,-0.78,27.3,1.65,1.69,-01,  969")
        self._other_names = ['Alnilam']

Alnilam = EpsilonOrionis


class EpsilonOrionis(FixedStar): # ,epsOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsOri", context=context, swe_string="Epsilon Orionis,epsOri,ICRS,05,36,12.81335,-01,12,06.9089,1.44,-0.78,27.3,1.65,1.69,-01,  969")
        self._other_names = ['Ganesha']

Ganesha = EpsilonOrionis


class ZetaOrionis(FixedStar): # ,zetOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetOri", context=context, swe_string="Zeta Orionis,zetOri,ICRS,05,40,45.52666,-01,56,33.2649,3.19,2.03,18.5,4.43,1.79,-02, 1338")
        self._other_names = ['Alnitak']

Alnitak = ZetaOrionis


class ZetaOrionis(FixedStar): # ,zetOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetOri", context=context, swe_string="Zeta Orionis,zetOri,ICRS,05,40,45.52666,-01,56,33.2649,3.19,2.03,18.5,4.43,1.79,-02, 1338")
        self._other_names = ['Iyappa']

Iyappa = ZetaOrionis


class EtaOrionis(FixedStar): # ,etaOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaOri", context=context, swe_string="Eta Orionis,etaOri,ICRS,05,42,28.61672,-02,23,49.7311,-0.71,-3.46,19.8,3.34,3.35,0, 0")
        self._other_names = ['Ensis']

Ensis = EtaOrionis


class ThetaOrionis01(FixedStar): # ,tet01Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet01Ori", context=context, swe_string="Theta Orionis 01,tet01Ori,ICRS,05,35,16.46375,-05,23,22.8486,-4.13,6.82,23.6,13,5.13,0, 0")
        self._other_names = ['Trapezium']

Trapezium = ThetaOrionis01


class IotaOrionis(FixedStar): # ,iotOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotOri", context=context, swe_string="Iota Orionis,iotOri,ICRS,05,35,25.98191,-05,54,35.6435,1.42,-0.46,21.5,1.4,2.77,-06, 1241")
        self._other_names = ['Hatsya']

Hatsya = IotaOrionis


class IotaOrionis(FixedStar): # ,iotOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotOri", context=context, swe_string="Iota Orionis,iotOri,ICRS,05,35,25.98191,-05,54,35.6435,1.42,-0.46,21.5,1.4,2.77,-06, 1241")
        self._other_names = ['Nair al Saif']

NairalSaif = IotaOrionis


class KappaOrionis(FixedStar): # ,kapOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapOri", context=context, swe_string="Kappa Orionis,kapOri,ICRS,05,47,45.38884,-09,40,10.5777,1.46,-1.28,20.5,5.04,2.06,-09, 1235")
        self._other_names = ['Saiph']

Saiph = KappaOrionis


class LambdaOrionis(FixedStar): # ,lamOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamOri", context=context, swe_string="Lambda Orionis,lamOri,ICRS,05,35,08.27761,+09,56,02.9611,-0.34,-2.94,30.1,2.97,3.66, 09,  879")
        self._other_names = ['Meissa']

Meissa = LambdaOrionis


class LambdaOrionis(FixedStar): # ,lamOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamOri", context=context, swe_string="Lambda Orionis,lamOri,ICRS,05,35,08.27761,+09,56,02.9611,-0.34,-2.94,30.1,2.97,3.66, 09,  879")
        self._other_names = ['Heka']

Heka = LambdaOrionis


class LambdaOrionis(FixedStar): # ,lamOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamOri", context=context, swe_string="Lambda Orionis,lamOri,ICRS,05,35,08.27761,+09,56,02.9611,-0.34,-2.94,30.1,2.97,3.66, 09,  879")
        self._other_names = ['Mrgashirsha']

Mrgashirsha = LambdaOrionis


class LambdaOrionis(FixedStar): # ,lamOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamOri", context=context, swe_string="Lambda Orionis,lamOri,ICRS,05,35,08.27761,+09,56,02.9611,-0.34,-2.94,30.1,2.97,3.66, 09,  879")
        self._other_names = ['Mrigashirsha']

Mrigashirsha = LambdaOrionis


class MessierObjectu.Ori(FixedStar): # ,mu.Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Ori", context=context, swe_string="Messier Object u.Ori,mu.Ori,ICRS,06,02,22.99668,+09,38,50.1820,10.43,-39.09,0,21.05,4.13, 14, 1152")
        self._other_names = []

 = MessierObjectu.Ori


class NuOrionis(FixedStar): # ,nu.Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Ori", context=context, swe_string="Nu Orionis,nu.Ori,ICRS,06,07,34.32588,+14,46,06.5061,6.78,-20.23,24.1,6.32,4.397, 0, 0")
        self._other_names = []

 = NuOrionis


class XiOrionis(FixedStar): # ,ksiOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiOri", context=context, swe_string="Xi Orionis,ksiOri,ICRS,06,11,56.39693,+14,12,31.5555,0.29,-20.12,19.3,5.37,4.48, 0, 0")
        self._other_names = []

 = XiOrionis


class OmicronOrionis01(FixedStar): # ,omi01Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omi01Ori", context=context, swe_string="Omicron Orionis 01,omi01Ori,ICRS,04,52,31.96357,+14,15,02.3215,-0.05,-54.81,-8.4,5.01,4.721, 14,  777")
        self._other_names = []

 = OmicronOrionis01


class PiOrionis01(FixedStar): # ,pi.01Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.01Ori", context=context, swe_string="Pi Orionis 01,pi.01Ori,ICRS,04,54,53.72877,+10,09,02.9952,41.49,-128.73,11.1,28.04,4.648, 0,  0")
        self._other_names = []

 = PiOrionis01


class PiOrionis02(FixedStar): # ,pi.02Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.02Ori", context=context, swe_string="Pi Orionis 02,pi.02Ori,ICRS,04,50,36.72298,+08,54,00.6493,1.41,-29.91,24.4,14.53,4.35, 0,  0")
        self._other_names = []

 = PiOrionis02


class PiOrionis03(FixedStar): # ,pi.03Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.03Ori", context=context, swe_string="Pi Orionis 03,pi.03Ori,ICRS,04,49,50.41091,+06,57,40.5883,464.06,11.21,22.41,123.94,3.19, 06,  762")
        self._other_names = ['Tabit']

Tabit = PiOrionis03


class PiOrionis04(FixedStar): # ,pi.04Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.04Ori", context=context, swe_string="Pi Orionis 04,pi.04Ori,ICRS,04,51,12.36472,+05,36,18.3723,-2.21,0.85,23.3,3.1,3.68, 05,  745")
        self._other_names = ['Tabit']

Tabit = PiOrionis04


class PiOrionis05(FixedStar): # ,pi.05Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.05Ori", context=context, swe_string="Pi Orionis 05,pi.05Ori,ICRS,04,54,15.09604,+02,26,26.4231,0.55,0.61,24.2,2.43,3.73, 02,  810")
        self._other_names = []

 = PiOrionis05


class PiOrionis06(FixedStar): # ,pi.06Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.06Ori", context=context, swe_string="Pi Orionis 06,pi.06Ori,ICRS,04,58,32.90210,+01,42,50.4582,-1.3,-7.67,15.36,3.45,4.459, 0,  0")
        self._other_names = []

 = PiOrionis06


class TauOrionis(FixedStar): # ,tauOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauOri", context=context, swe_string="Tau Orionis,tauOri,ICRS,05,17,36.38856,-06,50,39.8702,-17.61,-9.24,20.1,6.6,3.59,-07, 1028")
        self._other_names = []

 = TauOrionis


class UpsilonOrionis(FixedStar): # ,upsOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsOri", context=context, swe_string="Upsilon Orionis,upsOri,ICRS,05,31,55.86019,-07,18,05.5371,-0.1,-4.87,17.4,1.14,4.63,-07, 1106")
        self._other_names = ['Thabit']

Thabit = UpsilonOrionis


class PhiOrionis01(FixedStar): # ,phi01Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phi01Ori", context=context, swe_string="Phi Orionis 01,phi01Ori,ICRS,05,34,49.23804,+09,29,22.4878,0.27,-2.26,33.2,3,4.41, 09,  877")
        self._other_names = []

 = PhiOrionis01


class ChiOrionis02(FixedStar): # ,chi02Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chi02Ori", context=context, swe_string="Chi Orionis 02,chi02Ori,ICRS,06,03,55.18482,+20,08,18.4316,1.88,-2.1,16.8,1.81,4.63, 0,  0")
        self._other_names = []

 = ChiOrionis02


class Orionis71(FixedStar): # ,71Ori

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",71Ori", context=context, swe_string="Orionis71,71Ori,ICRS,06,14,50.87581,+19,09,23.1988,-97.29,-183.23,35.3,48.04,5.2, 0,  0")
        self._other_names = []

 = Orionis71


class MessierObject42(FixedStar): # ,M42

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M42", context=context, swe_string="Messier Object 42,M42,ICRS,05,35,17.3,-5,23,28.0,  1.67,  -0.30,  27.8,0.0,  3.7,0,  0")
        self._other_names = ['Orion Nebula']

OrionNebula = MessierObject42


class MessierObject42(FixedStar): # ,M42

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M42", context=context, swe_string="Messier Object 42,M42,ICRS,05,35,17.3,-5,23,28.0,  1.67,  -0.30,  27.8,0.0,  3.7,0,  0")
        self._other_names = []



class AlphaPavonis(FixedStar): # ,alfPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPav", context=context, swe_string="Alpha Pavonis,alfPav,ICRS,20,25,38.85705,-56,44,06.3230,6.9,-86.02,2,18.24,1.918,-57, 9674")
        self._other_names = ['Peacock']

Peacock = AlphaPavonis


class BetaPavonis(FixedStar): # ,betPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPav", context=context, swe_string="Beta Pavonis,betPav,ICRS,20,44,57.49399,-66,12,11.5708,-42.67,9.94,3.7,24.14,3.408,-66, 3501")
        self._other_names = []

 = BetaPavonis


class GammaPavonis(FixedStar): # ,gamPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPav", context=context, swe_string="Gamma Pavonis,gamPav,ICRS,21,26,26.60484,-65,21,58.3145,80.56,800.6,-30.7,107.97,4.22,-65, 3918")
        self._other_names = []

 = GammaPavonis


class DeltaPavonis(FixedStar): # ,delPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delPav", context=context, swe_string="Delta Pavonis,delPav,ICRS,20,08,43.60953,-66,10,55.4436,1211.03,-1130.05,-21.7,163.71,3.56,-66, 3474")
        self._other_names = []

 = DeltaPavonis


class EpsilonPavonis(FixedStar): # ,epsPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsPav", context=context, swe_string="Epsilon Pavonis,epsPav,ICRS,20,00,35.55558,-72,54,37.8198,81.78,-132.16,-6.7,31.04,3.94,-73, 2086")
        self._other_names = []

 = EpsilonPavonis


class ZetaPavonis(FixedStar): # ,zetPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPav", context=context, swe_string="Zeta Pavonis,zetPav,ICRS,18,43,02.13528,-71,25,41.2065,0.81,-158.15,-16.3,14.93,4.003,-71, 2353")
        self._other_names = []

 = ZetaPavonis


class EtaPavonis(FixedStar): # ,etaPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaPav", context=context, swe_string="Eta Pavonis,etaPav,ICRS,17,45,43.98605,-64,43,25.9394,-11.96,-56.57,-7.6,9.26,3.581,-64, 3662")
        self._other_names = []

 = EtaPavonis


class LambdaPavonis(FixedStar): # ,lamPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamPav", context=context, swe_string="Lambda Pavonis,lamPav,ICRS,18,52,13.03427,-62,11,15.3324,-1.86,-13.02,9,2.28,4.207,-62, 5983")
        self._other_names = []

 = LambdaPavonis


class XiPavonis(FixedStar): # ,ksiPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiPav", context=context, swe_string="Xi Pavonis,ksiPav,ICRS,18,23,13.62473,-61,29,38.0773,3.17,-2.21,12.2,6.96,4.367,-61, 6140")
        self._other_names = []

 = XiPavonis


class OmicronPavonis(FixedStar): # ,omiPav

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiPav", context=context, swe_string="Omicron Pavonis,omiPav,ICRS,21,13,20.50923,-70,07,34.5549,41.28,-19.69,-19,3.65,5.071,-70, 2835")
        self._other_names = []

 = OmicronPavonis


class AlphaPhoenicis(FixedStar): # ,alfPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPhe", context=context, swe_string="Alpha Phoenicis,alfPhe,ICRS,00,26,17.05140,-42,18,21.5539,233.05,-356.3,74.6,38.5,2.37,-42,  116")
        self._other_names = ['Ankaa']

Ankaa = AlphaPhoenicis


class BetaPhoenicis(FixedStar): # ,betPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPhe", context=context, swe_string="Beta Phoenicis,betPhe,ICRS,01,06,05.03952,-46,43,06.2785,-80.81,34.97,-1.1,0.12,3.3,0,0")
        self._other_names = []

 = BetaPhoenicis


class GammaPhoenicis(FixedStar): # ,gamPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPhe", context=context, swe_string="Gamma Phoenicis,gamPhe,ICRS,01,28,21.92727,-43,19,05.6502,-18.06,-208.63,25.8,13.96,3.41,-43,449")
        self._other_names = []

 = GammaPhoenicis


class DeltaPhoenicis(FixedStar): # ,delPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delPhe", context=context, swe_string="Delta Phoenicis,delPhe,ICRS,01,31,15.10475,-49,04,21.7308,138.38,153.89,-7.3,22.95,3.935,-49,  425")
        self._other_names = []

 = DeltaPhoenicis


class EpsilonPhoenicis(FixedStar): # ,epsPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsPhe", context=context, swe_string="Epsilon Phoenicis,epsPhe,ICRS,00,09,24.64154,-45,44,50.7315,121.52,-179.83,-9.2,22.62,3.87,-46,   18")
        self._other_names = []

 = EpsilonPhoenicis


class EtaPhoenicis(FixedStar): # ,etaPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaPhe", context=context, swe_string="Eta Phoenicis,etaPhe,ICRS,00,43,21.23841,-57,27,47.0073,-5.07,16.51,7.7,13.24,4.361,-58,   42")
        self._other_names = []

 = EtaPhoenicis


class ZetaPhoenicis(FixedStar): # ,zetPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPhe", context=context, swe_string="Zeta Phoenicis,zetPhe,ICRS,01,08,23.08150,-55,14,44.7289,20.87,30.64,15.4,10.92,4.014,0,0")
        self._other_names = ['Wurren']

Wurren = ZetaPhoenicis


class ThetaPhoenicis(FixedStar): # ,tetPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetPhe", context=context, swe_string="Theta Phoenicis,tetPhe,ICRS,23,39,27.94416,-46,38,16.0796,22.37,40.39,13.9,12.68,6.09,0,0")
        self._other_names = []

 = ThetaPhoenicis


class IotaPhoenicis(FixedStar): # ,iotPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotPhe", context=context, swe_string="Iota Phoenicis,iotPhe,ICRS,23,35,04.56417,-42,36,54.2709,42.31,10.67,19.4,13.11,4.71,-43,15420")
        self._other_names = []

 = IotaPhoenicis


class LambdaPhoenicis01(FixedStar): # ,lam01Phe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lam01Phe", context=context, swe_string="Lambda Phoenicis 01,lam01Phe,ICRS,00,31,24.98046,-48,48,12.6538,140.49,19.25,-2,18.88,4.77,-49,  115")
        self._other_names = []

 = LambdaPhoenicis01


class MessierObjectu.Phe(FixedStar): # ,mu.Phe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Phe", context=context, swe_string="Messier Object u.Phe,mu.Phe,ICRS,00,41,19.55229,-46,05,06.0184,-28.2,1.8,18.8,13.27,4.59,-46,  180")
        self._other_names = []

 = MessierObjectu.Phe


class PiPhoenicis(FixedStar): # ,pi.Phe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Phe", context=context, swe_string="Pi Phoenicis,pi.Phe,ICRS,23,58,55.77971,-52,44,44.9069,58.33,61.23,-14.1,11.35,5.133,-53,10561")
        self._other_names = []

 = PiPhoenicis


class UpsilonPhoenicis(FixedStar): # ,upsPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsPhe", context=context, swe_string="Upsilon Phoenicis,upsPhe,ICRS,01,07,47.8516,-41,29,12.841,32.604,15.128,9,17.56,5.207,-42,  391")
        self._other_names = []

 = UpsilonPhoenicis


class HipparcosCataloguePhe(FixedStar): # ,phiPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiPhe", context=context, swe_string="Hipparcos Catalogue Phe,phiPhe,ICRS,01,54,22.03347,-42,29,49.0183,-33.91,-28.17,5.5,10.63,5.109,-43,  583")
        self._other_names = []

 = HipparcosCataloguePhe


class PsiPhoenicis(FixedStar): # ,psiPhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiPhe", context=context, swe_string="Psi Phoenicis,psiPhe,ICRS,01,53,38.74103,-46,18,09.6048,-93.16,-91.17,2.9,9.54,4.41,-46,  552")
        self._other_names = []

 = PsiPhoenicis


class OmegaPhoenicis(FixedStar): # ,omePhe

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omePhe", context=context, swe_string="Omega Phoenicis,omePhe,ICRS,01,02, 1.8208,-57,00, 8.601,  0.0442667,   1.653,  13.0,0.00886,  6.109,-57,  220")
        self._other_names = []

 = OmegaPhoenicis


class AlphaPegasi(FixedStar): # ,alfPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPeg", context=context, swe_string="Alpha Pegasi,alfPeg,ICRS,23,04,45.65345,+15,12,18.9617,60.4,-41.3,-2.7,24.46,2.48, 14, 4926")
        self._other_names = ['Markab']

Markab = AlphaPegasi


class AlphaPegasi(FixedStar): # ,alfPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPeg", context=context, swe_string="Alpha Pegasi,alfPeg,ICRS,23,04,45.65345,+15,12,18.9617,60.4,-41.3,-2.7,24.46,2.48, 14, 4926")
        self._other_names = ['Purvabhadra']

Purvabhadra = AlphaPegasi


class BetaPegasi(FixedStar): # ,betPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPeg", context=context, swe_string="Beta Pegasi,betPeg,ICRS,23,03,46.45746,+28,04,58.0336,187.65,136.93,7.99,16.64,2.42, 27, 4480")
        self._other_names = ['Scheat']

Scheat = BetaPegasi


class GammaPegasi(FixedStar): # ,gamPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPeg", context=context, swe_string="Gamma Pegasi,gamPeg,ICRS,00,13,14.15123,+15,11,00.9368,1.98,-9.28,3.2,8.33,2.84, 14,   14")
        self._other_names = ['Algenib']

Algenib = GammaPegasi


class GammaPegasi(FixedStar): # ,gamPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPeg", context=context, swe_string="Gamma Pegasi,gamPeg,ICRS,00,13,14.15123,+15,11,00.9368,1.98,-9.28,3.2,8.33,2.84, 14,   14")
        self._other_names = ['Uttarabhadra']

Uttarabhadra = GammaPegasi


class EpsilonPegasi(FixedStar): # ,epsPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsPeg", context=context, swe_string="Epsilon Pegasi,epsPeg,ICRS,21,44,11.15614,+09,52,30.0311,26.92,0.44,3.39,4.73,2.39, 09, 4891")
        self._other_names = ['Enif']

Enif = EpsilonPegasi


class ZetaPegasi(FixedStar): # ,zetPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPeg", context=context, swe_string="Zeta Pegasi,zetPeg,ICRS,22,41,27.732,+10,49,52.64,77.22,-11.38,6.1,15.68,3.41, 10, 4797")
        self._other_names = ['Homam']

Homam = ZetaPegasi


class EtaPegasi(FixedStar): # ,etaPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaPeg", context=context, swe_string="Eta Pegasi,etaPeg,ICRS,22,43,00.13743,+30,13,16.4822,13.16,-25.67,4.17,15.22,2.95, 29, 4741")
        self._other_names = ['Matar']

Matar = EtaPegasi


class ThetaPegasi(FixedStar): # ,tetPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetPeg", context=context, swe_string="Theta Pegasi,tetPeg,ICRS,22,10,11.98528,+06,11,52.3078,282.18,30.46,-7.9,35.34,3.55, 05, 4961")
        self._other_names = ['Biham']

Biham = ThetaPegasi


class ThetaPegasi(FixedStar): # ,tetPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetPeg", context=context, swe_string="Theta Pegasi,tetPeg,ICRS,22,10,11.98528,+06,11,52.3078,282.18,30.46,-7.9,35.34,3.55, 05, 4961")
        self._other_names = ['Baham']

Baham = ThetaPegasi


class IotaPegasi(FixedStar): # ,iotPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotPeg", context=context, swe_string="Iota Pegasi,iotPeg,ICRS,22,07,00.66597,+25,20,42.4048,296.53,27.29,-5.5,85.28,3.77, 24, 4533")
        self._other_names = []

 = IotaPegasi


class KappaPegasi(FixedStar): # ,kapPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapPeg", context=context, swe_string="Kappa Pegasi,kapPeg,ICRS,21,44,38.73522,+25,38,42.1359,48.13,14.29,-0.8,29.22,4.135, 0, 0")
        self._other_names = ['Jih']

Jih = KappaPegasi


class LambdaPegasi(FixedStar): # ,lamPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamPeg", context=context, swe_string="Lambda Pegasi,lamPeg,ICRS,22,46,31.87786,+23,33,56.3561,55.75,-10.15,-4.15,8.93,3.93, 22, 4709")
        self._other_names = ['Sadalbari']

Sadalbari = LambdaPegasi


class MessierObjectu.Peg(FixedStar): # ,mu.Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Peg", context=context, swe_string="Messier Object u.Peg,mu.Peg,ICRS,22,50,00.19315,+24,36,05.6984,144.7,-41.87,13.54,30.74,3.48, 23, 4615")
        self._other_names = []

 = MessierObjectu.Peg


class XiPegasi(FixedStar): # ,ksiPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiPeg", context=context, swe_string="Xi Pegasi,ksiPeg,ICRS,22,46,41.58118,+12,10,22.3854,234.18,-493.29,-5.37,61.36,4.2,0,0")
        self._other_names = []

 = XiPegasi


class PiPegasi(FixedStar): # ,pi.Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Peg", context=context, swe_string="Pi Pegasi,pi.Peg,ICRS,22,09,59.24371,+33,10,41.5976,-12.87,-18.95,5.1,12.4,4.29, 32, 4352")
        self._other_names = []

 = PiPegasi


class PiPegasi01(FixedStar): # ,pi.01Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.01Peg", context=context, swe_string="Pi Pegasi 01,pi.01Peg,ICRS,22,09,13.63306,+33,10,20.4071,-61.14,-66.84,-8.3,11.3,5.582, 32, 4349")
        self._other_names = []

 = PiPegasi01


class PiPegasi02(FixedStar): # ,pi.02Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.02Peg", context=context, swe_string="Pi Pegasi 02,pi.02Peg,ICRS,22,09,59.24371,+33,10,41.5976,-12.87,-18.95,5.1,12.4,4.29, 32, 4352")
        self._other_names = []

 = PiPegasi02


class TauPegasi(FixedStar): # ,tauPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauPeg", context=context, swe_string="Tau Pegasi,tauPeg,ICRS,23,20,38.24188,+23,44,25.2098,29.45,-9.53,15.2,20.17,4.58, 22, 4810")
        self._other_names = ['Kerb']

Kerb = TauPegasi


class TauPegasi(FixedStar): # ,tauPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauPeg", context=context, swe_string="Tau Pegasi,tauPeg,ICRS,23,20,38.24188,+23,44,25.2098,29.45,-9.53,15.2,20.17,4.58, 22, 4810")
        self._other_names = ['Salm']

Salm = TauPegasi


class UpsilonPegasi(FixedStar): # ,upsPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsPeg", context=context, swe_string="Upsilon Pegasi,upsPeg,ICRS,23,25,22.78350,+23,24,14.7606,192.19,36.12,-8.59,19.14,4.4, 22, 4833")
        self._other_names = ['Alkarab']

Alkarab = UpsilonPegasi


class HipparcosCataloguePeg(FixedStar): # ,phiPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiPeg", context=context, swe_string="Hipparcos Catalogue Peg,phiPeg,ICRS,23,52,29.28762,+19,07,13.0218,-7.27,-35.4,-7.75,7.05,5.08, 18, 5231")
        self._other_names = []

 = HipparcosCataloguePeg


class HipparcosCataloguePeg(FixedStar): # ,chiPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiPeg", context=context, swe_string="Hipparcos Catalogue Peg,chiPeg,ICRS,00,14,36.16451,+20,12,24.1205,90.76,1.24,-46.6,8.86,4.8, 19,   27")
        self._other_names = []

 = HipparcosCataloguePeg


class PsiPegasi(FixedStar): # ,psiPeg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiPeg", context=context, swe_string="Psi Pegasi,psiPeg,ICRS,23,57,45.52681,+25,08,29.0480,-35.24,-31.6,-6.59,6.85,4.66, 24, 4865")
        self._other_names = []

 = PsiPegasi


class Pegasi1(FixedStar): # ,1Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",1Peg", context=context, swe_string="Pegasi1,1Peg,ICRS,21,22,05.199,+19,48,16.24,105.35,63.51,-10.8,20.93,4.09,0,0")
        self._other_names = []

 = Pegasi1


class Pegasi9(FixedStar): # ,9Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",9Peg", context=context, swe_string="Pegasi9,9Peg,ICRS,21,44,30.69581,+17,21,00.0571,8.66,-11.33,-23.11,3.52,4.35,0,0")
        self._other_names = []

 = Pegasi9


class Pegasi51(FixedStar): # ,51Peg

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",51Peg", context=context, swe_string="Pegasi51,51Peg,ICRS,22,57,27.98004,+20,46,07.7912,207.25,60.34,-33.02,64.07,5.46, 0,0")
        self._other_names = ['Helvetios']

Helvetios = Pegasi51


class AlphaPersei(FixedStar): # ,alfPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPer", context=context, swe_string="Alpha Persei,alfPer,ICRS,03,24,19.37009,+49,51,40.2455,23.75,-26.23,-2.04,6.44,1.79, 49,  917")
        self._other_names = ['Mirfak']

Mirfak = AlphaPersei


class AlphaPersei(FixedStar): # ,alfPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPer", context=context, swe_string="Alpha Persei,alfPer,ICRS,03,24,19.37009,+49,51,40.2455,23.75,-26.23,-2.04,6.44,1.79, 49,  917")
        self._other_names = ['Mirphak']

Mirphak = AlphaPersei


class BetaPersei(FixedStar): # ,betPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPer", context=context, swe_string="Beta Persei,betPer,ICRS,03,08,10.13245,+40,57,20.3280,2.99,-1.66,4,36.27,2.12, 40,  673")
        self._other_names = ['Algol', 'HIP 14576']

Algol = BetaPersei
HIP14576 = BetaPersei


class GammaPersei(FixedStar): # ,gamPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPer", context=context, swe_string="Gamma Persei,gamPer,ICRS,03,04,47.79074,+53,30,23.1687,0.51,-5.92,3.13,13.41,2.93, 52,  654")
        self._other_names = []

 = GammaPersei


class DeltaPersei(FixedStar): # ,delPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delPer", context=context, swe_string="Delta Persei,delPer,ICRS,03,42,55.50426,+47,47,15.1746,25.58,-43.06,4,6.32,3.01, 47,  876")
        self._other_names = []

 = DeltaPersei


class EpsilonPersei(FixedStar): # ,epsPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsPer", context=context, swe_string="Epsilon Persei,epsPer,ICRS,03,57,51.23205,+40,00,36.7752,14.06,-23.78,-1,5.11,2.89, 39,  895")
        self._other_names = []

 = EpsilonPersei


class ZetaPersei(FixedStar): # ,zetPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPer", context=context, swe_string="Zeta Persei,zetPer,ICRS,03,54,07.92248,+31,53,01.0812,5.77,-9.92,20.6,4.34,2.85, 31,  666")
        self._other_names = []

 = ZetaPersei


class EtaPersei(FixedStar): # ,etaPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaPer", context=context, swe_string="Eta Persei,etaPer,ICRS,02,50,41.80959,+55,53,43.7876,16.23,-13.54,-1.07,3.71,3.79, 55,  714")
        self._other_names = ['Miram']

Miram = EtaPersei


class ThetaPersei(FixedStar): # ,tetPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetPer", context=context, swe_string="Theta Persei,tetPer,ICRS,02,44,11.98704,+49,13,42.4111,334.66,-89.99,24.32,89.87,4.11, 48,  746")
        self._other_names = []

 = ThetaPersei


class IotaPersei(FixedStar): # ,iotPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotPer", context=context, swe_string="Iota Persei,iotPer,ICRS,03,09,04.01986,+49,36,47.7996,1262.41,-91.5,49.22,94.87,4.05, 49,  857")
        self._other_names = []

 = IotaPersei


class KappaPersei(FixedStar): # ,kapPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapPer", context=context, swe_string="Kappa Persei,kapPer,ICRS,03,09,29.77156,+44,51,27.1463,172.99,-143.4,29.4,28.93,3.81, 44,  631")
        self._other_names = ['Misam']

Misam = KappaPersei


class LambdaPersei(FixedStar): # ,lamPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamPer", context=context, swe_string="Lambda Persei,lamPer,ICRS,04,06,35.04360,+50,21,04.5500,-12.75,-35.6,6.1,7.73,4.29, 49, 1101")
        self._other_names = []

 = LambdaPersei


class MessierObjectu.Per(FixedStar): # ,mu.Per

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Per", context=context, swe_string="Messier Object u.Per,mu.Per,ICRS,04,14,53.86253,+48,24,33.5912,5.52,-17.37,26.46,3.62,4.16, 48, 1063")
        self._other_names = []

 = MessierObjectu.Per


class NuPersei(FixedStar): # ,nu.Per

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Per", context=context, swe_string="Nu Persei,nu.Per,ICRS,03,45,11.63204,+42,34,42.7829,-14.45,2.53,-12.1,5.86,3.8, 42,  815")
        self._other_names = []

 = NuPersei


class XiPersei(FixedStar): # ,ksiPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiPer", context=context, swe_string="Xi Persei,ksiPer,ICRS,03,58,57.90229,+35,47,27.7132,3.62,1.74,65.4,2.62,4.06, 35,  775")
        self._other_names = ['Menkib']

Menkib = XiPersei


class OmicronPersei(FixedStar): # ,omiPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiPer", context=context, swe_string="Omicron Persei,omiPer,ICRS,03,44,19.13204,+32,17,17.6929,8.18,-10.43,12.2,2.91,3.83, 31,  642")
        self._other_names = ['Atik']

Atik = OmicronPersei


class OmicronPersei(FixedStar): # ,omiPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiPer", context=context, swe_string="Omicron Persei,omiPer,ICRS,03,44,19.13204,+32,17,17.6929,8.18,-10.43,12.2,2.91,3.83, 31,  642")
        self._other_names = ['Atiks']

Atiks = OmicronPersei


class PiPersei(FixedStar): # ,pi.Per

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Per", context=context, swe_string="Pi Persei,pi.Per,ICRS,02,58,45.66985,+39,39,45.8141,25.65,-41.62,14.2,10.53,4.7, 39,  681")
        self._other_names = ['Gorgona Secunda']

GorgonaSecunda = PiPersei


class RhoPersei(FixedStar): # ,rhoPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoPer", context=context, swe_string="Rho Persei,rhoPer,ICRS,03,05,10.59385,+38,50,24.9943,129.22,-105.7,30.81,10.6,3.39, 38,  630")
        self._other_names = ['Gorgona Tertia']

GorgonaTertia = RhoPersei


class SigmaPersei(FixedStar): # ,sigPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigPer", context=context, swe_string="Sigma Persei,sigPer,ICRS,03,30,34.48545,+47,59,42.7808,3.56,18.48,14.36,9.07,4.36, 47,  843")
        self._other_names = []

 = SigmaPersei


class TauPersei(FixedStar): # ,tauPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauPer", context=context, swe_string="Tau Persei,tauPer,ICRS,02,54,15.46108,+52,45,44.9240,-1.26,-4.37,2.2,12.83,3.96, 52,  641")
        self._other_names = []

 = TauPersei


class HipparcosCataloguePer(FixedStar): # ,phiPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiPer", context=context, swe_string="Hipparcos Catalogue Per,phiPer,ICRS,01,43,39.63792,+50,41,19.4328,24.59,-14.01,0.8,4.54,4.06, 49,  444")
        self._other_names = []

 = HipparcosCataloguePer


class OmegaPersei(FixedStar): # ,omePer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omePer", context=context, swe_string="Omega Persei,omePer,ICRS,03,11,17.38161,+39,36,41.7014,-26.26,5.4,6.61,11.32,4.607, 39,  724")
        self._other_names = ['Gorgona Quatra']

GorgonaQuatra = OmegaPersei


class NewGeneralCatalogue869(FixedStar): # ,NGC869

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",NGC869", context=context, swe_string="New General Catalogue 869,NGC869,ICRS,02,19,00.0,+57,07,42,-0.41,-1.03,-39.82,0,3.7,0, 0 # NGC 869, from Simbad")
        self._other_names = ['Capulus']

Capulus = NewGeneralCatalogue869


class NewGeneralCatalogue869(FixedStar): # ,NGC869

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",NGC869", context=context, swe_string="New General Catalogue 869,NGC869,ICRS,02,18,57.0,+57,08,02,-0.6943,-1.0831,-62.164,0.3942,0")
        self._other_names = []



class MessierObject34(FixedStar): # ,M34

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M34", context=context, swe_string="Messier Object 34,M34,ICRS,02,42,05.0,+42,45,42,0.03,-7.43,-16.8,0,5.2,0, 0 # NGC 1039")
        self._other_names = []

 = MessierObject34


class Persei16(FixedStar): # ,16Per

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",16Per", context=context, swe_string="Persei16,16Per,ICRS,02,50,35.05979,+38,19,07.1080,195.77,-109.98,14,27.01,4.2,0, 0")
        self._other_names = []

 = Persei16


class AlphaPictoris(FixedStar): # ,alfPic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPic", context=context, swe_string="Alpha Pictoris,alfPic,ICRS,06,48,11.45512,-61,56,29.0008,-66.07,242.97,15.3,33.78,3.3,-61,  720")
        self._other_names = []

 = AlphaPictoris


class BetaPictoris(FixedStar): # ,betPic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPic", context=context, swe_string="Beta Pictoris,betPic,ICRS,05,47,17.08769,-51,03,59.4412,4.65,83.1,20,51.44,3.86,0,0")
        self._other_names = []

 = BetaPictoris


class GammaPictoris(FixedStar): # ,gamPic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPic", context=context, swe_string="Gamma Pictoris,gamPic,ICRS,05,49,49.66181,-56,09,59.9808,81.13,-71.12,15.7,18.45,4.494,-56,  946")
        self._other_names = []

 = GammaPictoris


class DeltaPictoris(FixedStar): # ,delPic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delPic", context=context, swe_string="Delta Pictoris,delPic,ICRS,06,10,17.90808,-54,58,07.1134,-4.9,7.41,30.6,2.51,4.81,-54,  980")
        self._other_names = []

 = DeltaPictoris


class ZetaPictoris(FixedStar): # ,zetPic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPic", context=context, swe_string="Zeta Pictoris,zetPic,ICRS,05,19,22.13548,-50,36,21.4820,23.64,227.43,42.52,28,5.45,-50, 1723")
        self._other_names = []

 = ZetaPictoris


class EtaPictoris02(FixedStar): # ,eta02Pic

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eta02Pic", context=context, swe_string="Eta Pictoris 02,eta02Pic,ICRS,05,04,58.01453,-49,34,40.2079,68.96,-2.2,36,7.35,5.01,-49, 1562")
        self._other_names = []

 = EtaPictoris02


class AlphaPiscisAustrini(FixedStar): # ,alfPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPsA", context=context, swe_string="Alpha Piscis Austrini,alfPsA,ICRS,22,57,39.04625,-29,37,20.0533,328.95,-164.67,6.5,129.81,1.16,-30,19370")
        self._other_names = ['Fomalhaut']

Fomalhaut = AlphaPiscisAustrini


class BetaPiscisAustrini(FixedStar): # ,betPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPsA", context=context, swe_string="Beta Piscis Austrini,betPsA,ICRS,22,31,30.33038,-32,20,45.8653,59.12,-18.83,5.5,22.84,4.29,-32,17126")
        self._other_names = ['Tien Kang']

TienKang = BetaPiscisAustrini


class GammaPiscisAustrini(FixedStar): # ,gamPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPsA", context=context, swe_string="Gamma Piscis Austrini,gamPsA,ICRS,22,52,31.53513,-32,52,31.8059,-32.73,-21.21,16.5,15.14,4.501,0,0")
        self._other_names = []

 = GammaPiscisAustrini


class DeltaPiscisAustrini(FixedStar): # ,delPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delPsA", context=context, swe_string="Delta Piscis Austrini,delPsA,ICRS,22,55,56.90026,-32,32,22.6335,11.98,33.64,-11.6,21.16,4.208,0,0")
        self._other_names = ['Aboras']

Aboras = DeltaPiscisAustrini


class EpsilonPiscisAustrini(FixedStar): # ,epsPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsPsA", context=context, swe_string="Epsilon Piscis Austrini,epsPsA,ICRS,22,40,39.34075,-27,02,37.0157,23.22,-0.16,1.1,6.7,4.177,-27,16010")
        self._other_names = []

 = EpsilonPiscisAustrini


class ThetaPiscisAustrini(FixedStar): # ,tetPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetPsA", context=context, swe_string="Theta Piscis Austrini,tetPsA,ICRS,21,47,44.14993,-30,53,53.9027,-34.4,-0.08,12.8,10.16,5.017,0,0")
        self._other_names = []

 = ThetaPiscisAustrini


class IotaPiscisAustrini(FixedStar): # ,iotPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotPsA", context=context, swe_string="Iota Piscis Austrini,iotPsA,ICRS,21,44,56.80944,-33,01,32.8180,31.1,-94.56,3,15.97,4.34,-33,15734")
        self._other_names = []

 = IotaPiscisAustrini


class LambdaPiscisAustrini(FixedStar): # ,lamPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamPsA", context=context, swe_string="Lambda Piscis Austrini,lamPsA,ICRS,22,14,18.75180,-27,46,00.8667,23.6,2.04,-6.2,6.51,5.43,-28,17653")
        self._other_names = []

 = LambdaPiscisAustrini


class MessierObjectu.PsA(FixedStar): # ,mu.PsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.PsA", context=context, swe_string="Messier Object u.PsA,mu.PsA,ICRS,22,08,23.00806,-32,59,18.4884,78.81,-29.1,11.6,24.01,4.5,-33,15922")
        self._other_names = []

 = MessierObjectu.PsA


class PiPiscisAustrini(FixedStar): # ,pi.PsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.PsA", context=context, swe_string="Pi Piscis Austrini,pi.PsA,ICRS,23,03,29.81356,-34,44,57.8814,71.46,84.55,-6,33.99,5.124,-35,15630")
        self._other_names = []

 = PiPiscisAustrini


class AlphaPiscium(FixedStar): # ,alfPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPsc", context=context, swe_string="Alpha Piscium,alfPsc,ICRS,02,02,02.81972,+02,45,49.5410,32.45,0.04,7.5,21.66,3.82, 02,  317")
        self._other_names = ['Alrischa']

Alrischa = AlphaPiscium


class AlphaPiscium(FixedStar): # ,alfPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPsc", context=context, swe_string="Alpha Piscium,alfPsc,ICRS,02,02,02.81972,+02,45,49.5410,32.45,0.04,7.5,21.66,3.82, 02,  317")
        self._other_names = ['Alrescha']

Alrescha = AlphaPiscium


class AlphaPiscium(FixedStar): # ,alfPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPsc", context=context, swe_string="Alpha Piscium,alfPsc,ICRS,02,02,02.81972,+02,45,49.5410,32.45,0.04,7.5,21.66,3.82, 02,  317")
        self._other_names = ['Al Rescha']

AlRescha = AlphaPiscium


class BetaPiscium(FixedStar): # ,betPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPsc", context=context, swe_string="Beta Piscium,betPsc,ICRS,23,03,52.61349,+03,49,12.1662,11.76,-9.85,0,7.99,4.52, 03, 4818")
        self._other_names = ['Fum Alsamakah']

FumAlsamakah = BetaPiscium


class BetaPiscium(FixedStar): # ,betPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPsc", context=context, swe_string="Beta Piscium,betPsc,ICRS,23,03,52.61349,+03,49,12.1662,11.76,-9.85,0,7.99,4.52, 03, 4818")
        self._other_names = ['Samakah']

Samakah = BetaPiscium


class GammaPiscium(FixedStar): # ,gamPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPsc", context=context, swe_string="Gamma Piscium,gamPsc,ICRS,23,17,09.93749,+03,16,56.2380,759.82,17.77,-14.49,23.64,3.7, 02, 4648")
        self._other_names = ['Simmah']

Simmah = GammaPiscium


class DeltaPiscium(FixedStar): # ,delPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delPsc", context=context, swe_string="Delta Piscium,delPsc,ICRS,00,48,40.94433,+07,35,06.2926,83.1,-49.58,32.45,10.48,4.44, 06,  107")
        self._other_names = ['Linteum']

Linteum = DeltaPiscium


class EpsilonPiscium(FixedStar): # ,epsPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsPsc", context=context, swe_string="Epsilon Piscium,epsPsc,ICRS,01,02,56.60862,+07,53,24.4855,-80.17,25.59,7.74,17.94,4.28, 07,  153")
        self._other_names = ['Kaht']

Kaht = EpsilonPiscium


class ZetaPiscium(FixedStar): # ,zetPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPsc", context=context, swe_string="Zeta Piscium,zetPsc,ICRS,01,13,43.88735,+07,34,31.2745,145,-55.69,15,18.76,5.187, 06,  174")
        self._other_names = ['Revati']

Revati = ZetaPiscium


class EtaPiscium(FixedStar): # ,etaPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaPsc", context=context, swe_string="Eta Piscium,etaPsc,ICRS,01,31,29.01026,+15,20,44.9685,27.14,-2.64,13.78,9.33,3.62, 14,  231")
        self._other_names = ['Al Pherg']

AlPherg = EtaPiscium


class ThetaPiscium(FixedStar): # ,tetPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetPsc", context=context, swe_string="Theta Piscium,tetPsc,ICRS,23,27,58.09529,+06,22,44.3720,-123.58,-43.23,5.73,21.96,4.3, 05, 5173")
        self._other_names = []

 = ThetaPiscium


class IotaPiscium(FixedStar): # ,iotPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotPsc", context=context, swe_string="Iota Piscium,iotPsc,ICRS,23,39,57.04138,+05,37,34.6475,377.15,-437.43,5.95,72.92,4.12, 04, 5035")
        self._other_names = []

 = IotaPiscium


class KappaPiscium(FixedStar): # ,kapPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapPsc", context=context, swe_string="Kappa Piscium,kapPsc,ICRS,23,26,55.95586,+01,15,20.1900,86.68,-94.29,-4.4,21.25,4.94, 00, 4998")
        self._other_names = []

 = KappaPiscium


class LambdaPiscium(FixedStar): # ,lamPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamPsc", context=context, swe_string="Lambda Piscium,lamPsc,ICRS,23,42,02.80612,+01,46,48.1484,-129.7,-154.8,10,30.59,4.51, 00, 5037")
        self._other_names = []

 = LambdaPiscium


class NuPiscium(FixedStar): # ,nu.Psc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Psc", context=context, swe_string="Nu Piscium,nu.Psc,ICRS,01,41,25.89391,+05,29,15.4062,-23.36,3.36,0.76,8.98,4.44, 04,  293")
        self._other_names = []

 = NuPiscium


class XiPiscium(FixedStar): # ,ksiPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiPsc", context=context, swe_string="Xi Piscium,ksiPsc,ICRS,01,53,33.35074,+03,11,15.1498,24.48,25.99,26.13,18.21,4.604, 02,  290")
        self._other_names = []

 = XiPiscium


class OmicronPiscium(FixedStar): # ,omiPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiPsc", context=context, swe_string="Omicron Piscium,omiPsc,ICRS,01,45,23.63185,+09,09,27.8530,72.98,39.3,12.16,11.67,4.26, 08,  273")
        self._other_names = ['Torcularis Septentrionalis']

TorcularisSeptentrionalis = OmicronPiscium


class OmicronPiscium(FixedStar): # ,omiPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiPsc", context=context, swe_string="Omicron Piscium,omiPsc,ICRS,01,45,23.63185,+09,09,27.8530,72.98,39.3,12.16,11.67,4.26, 08,  273")
        self._other_names = ['Torcular']

Torcular = OmicronPiscium


class PiPiscium(FixedStar): # ,pi.Psc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Psc", context=context, swe_string="Pi Piscium,pi.Psc,ICRS,01,37,05.91523,+12,08,29.5186,-77.29,9.13,-4.2,28.5,5.535, 11,  205")
        self._other_names = []

 = PiPiscium


class TauPiscium(FixedStar): # ,tauPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauPsc", context=context, swe_string="Tau Piscium,tauPsc,ICRS,01,11,39.63647,+30,05,22.6909,73.88,-38.3,35.2,19.32,4.511, 29,  190")
        self._other_names = ['Anunitum']

Anunitum = TauPiscium


class UpsilonPiscium(FixedStar): # ,upsPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsPsc", context=context, swe_string="Upsilon Piscium,upsPsc,ICRS,01,19,27.99289,+27,15,50.6155,22.98,-11.12,5.8,10.59,4.748, 26,  220")
        self._other_names = []

 = UpsilonPiscium


class HipparcosCataloguePsc(FixedStar): # ,phiPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiPsc", context=context, swe_string="Hipparcos Catalogue Psc,phiPsc,ICRS,01,13,44.94635,+24,35,01.3590,17.5,-22.04,7.08,7.31,4.66, 0,  0")
        self._other_names = []

 = HipparcosCataloguePsc


class HipparcosCataloguePsc(FixedStar): # ,chiPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiPsc", context=context, swe_string="Hipparcos Catalogue Psc,chiPsc,ICRS,01,11,27.21877,+21,02,04.7406,39.32,-10.48,15.04,8.5,4.658, 20,  172")
        self._other_names = []

 = HipparcosCataloguePsc


class OmegaPiscium(FixedStar): # ,omePsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omePsc", context=context, swe_string="Omega Piscium,omePsc,ICRS,23,59,18.69064,+06,51,47.9562,150.35,-112.12,2.9,31.26,4.012, 06, 5227")
        self._other_names = ['Vernalis']

Vernalis = OmegaPiscium


class Piscium7(FixedStar): # ,7Psc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",7Psc", context=context, swe_string="Piscium7,7Psc,ICRS,23,20,20.58314,+05,22,52.7012,78.47,-60,39.62,7.54,5.069, 0,  0")
        self._other_names = []

 = Piscium7


class Piscium19(FixedStar): # ,19Psc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",19Psc", context=context, swe_string="Piscium19,19Psc,ICRS,23,46,23.51708,+03,29,12.5244,-33.68,-24.49,-11,3.63,5.02, 0,  0")
        self._other_names = []

 = Piscium19


class ZetaPuppis(FixedStar): # ,zetPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPup", context=context, swe_string="Zeta Puppis,zetPup,ICRS,08,03,35.04754,-40,00,11.3321,-29.71,16.68,-23.9,3.01,2.25,-39, 3939")
        self._other_names = ['Naos']

Naos = ZetaPuppis


class ZetaPuppis(FixedStar): # ,zetPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPup", context=context, swe_string="Zeta Puppis,zetPup,ICRS,08,03,35.04754,-40,00,11.3321,-29.71,16.68,-23.9,3.01,2.25,-39, 3939")
        self._other_names = ['Suhail Hadar']

SuhailHadar = ZetaPuppis


class NuPuppis(FixedStar): # ,nu.Pup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Pup", context=context, swe_string="Nu Puppis,nu.Pup,ICRS,06,37,45.67135,-43,11,45.3602,-0.44,-3.87,30.9,8.78,3.17,-43, 2576")
        self._other_names = ['Kaimana']

Kaimana = NuPuppis


class XiPuppis(FixedStar): # ,ksiPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiPup", context=context, swe_string="Xi Puppis,ksiPup,ICRS,07,49,17.65567,-24,51,35.2305,-4.81,-0.89,2.8,2.72,3.3,-24, 6030")
        self._other_names = ['Azmidiske']

Azmidiske = XiPuppis


class PiPuppis(FixedStar): # ,pi.Pup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Pup", context=context, swe_string="Pi Puppis,pi.Pup,ICRS,07,17,08.55678,-37,05,50.8962,-10.05,6.47,15.8,4.04,2.7,-36, 3489")
        self._other_names = ['Ahadi']

Ahadi = PiPuppis


class RhoPuppis(FixedStar): # ,rhoPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoPup", context=context, swe_string="Rho Puppis,rhoPup,ICRS,08,07,32.64882,-24,18,15.5679,-83.35,46.23,45.8,51.33,2.81,-23, 6828")
        self._other_names = ['Turais']

Turais = RhoPuppis


class RhoPuppis(FixedStar): # ,rhoPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoPup", context=context, swe_string="Rho Puppis,rhoPup,ICRS,08,07,32.64882,-24,18,15.5679,-83.35,46.23,45.8,51.33,2.81,-23, 6828")
        self._other_names = ['Tureis']

Tureis = RhoPuppis


class SigmaPuppis(FixedStar): # ,sigPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigPup", context=context, swe_string="Sigma Puppis,sigPup,ICRS,07,29,13.83049,-43,18,05.1597,-59.55,188.31,87.3,16.84,3.25,-43, 3260")
        self._other_names = []

 = SigmaPuppis


class TauPuppis(FixedStar): # ,tauPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauPup", context=context, swe_string="Tau Puppis,tauPup,ICRS,06,49,56.16846,-50,36,52.4437,34.36,-69.11,34.4,17.92,2.93,-50, 2415")
        self._other_names = ['Al Rihla']

AlRihla = TauPuppis


class TauPuppis(FixedStar): # ,tauPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauPup", context=context, swe_string="Tau Puppis,tauPup,ICRS,06,49,56.16846,-50,36,52.4437,34.36,-69.11,34.4,17.92,2.93,-50, 2415")
        self._other_names = ['Rehla']

Rehla = TauPuppis


class TauPuppis(FixedStar): # ,tauPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauPup", context=context, swe_string="Tau Puppis,tauPup,ICRS,06,49,56.16846,-50,36,52.4437,34.36,-69.11,34.4,17.92,2.93,-50, 2415")
        self._other_names = ['Anazitisi']

Anazitisi = TauPuppis


class AlphaPyxis(FixedStar): # ,alfPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPyx", context=context, swe_string="Alpha Pyxis,alfPyx,ICRS,08,43,35.53756,-33,11,10.9898,-14.27,10.43,15.3,3.71,3.68,-32, 5651")
        self._other_names = []

 = AlphaPyxis


class BetaPyxis(FixedStar): # ,betPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPyx", context=context, swe_string="Beta Pyxis,betPyx,ICRS,08,40,06.14363,-35,18,30.0651,9.84,-20.8,-13.4,7.84,3.954,0,0")
        self._other_names = []

 = BetaPyxis


class GammaPyxis(FixedStar): # ,gamPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPyx", context=context, swe_string="Gamma Pyxis,gamPyx,ICRS,08,50,31.92282,-27,42,35.4421,-134.31,87.89,24.5,15.73,4.01,-27, 5986")
        self._other_names = []

 = GammaPyxis


class EpsilonPyxis(FixedStar): # ,epsPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsPyx", context=context, swe_string="Epsilon Pyxis,epsPyx,ICRS,09,09,56.41024,-30,21,55.4460,-1.93,-48.99,-9.7,15.39,5.593,-29, 7194")
        self._other_names = []

 = EpsilonPyxis


class ThetaPyxis(FixedStar): # ,tetPyx

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetPyx", context=context, swe_string="Theta Pyxis,tetPyx,ICRS,09,21,29.59085,-25,57,55.5803,-12.24,-9.29,20,6.49,4.72,-25, 7114")
        self._other_names = []

 = ThetaPyxis


class AlphaReticulum(FixedStar): # ,alfRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfRet", context=context, swe_string="Alpha Reticulum,alfRet,ICRS,04,14,25.48414,-62,28,25.8917,41.97,49.42,35.5,20.18,3.36,-62,  332")
        self._other_names = []

 = AlphaReticulum


class BetaReticulum(FixedStar): # ,betRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betRet", context=context, swe_string="Beta Reticulum,betRet,ICRS,03,44,11.97587,-64,48,24.8610,307.13,77.5,50.8,33.49,3.85,-65,  263")
        self._other_names = []

 = BetaReticulum


class GammaReticulum(FixedStar): # ,gamRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamRet", context=context, swe_string="Gamma Reticulum,gamRet,ICRS,04,00,53.80860,-62,09,33.4250,3.03,34.67,-7,6.95,4.5,0,0")
        self._other_names = []

 = GammaReticulum


class DeltaReticulum(FixedStar): # ,delRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delRet", context=context, swe_string="Delta Reticulum,delRet,ICRS,03,58,44.74945,-61,24,00.6673,9.8,-14.3,-1.4,6.2,4.57,-61,  290")
        self._other_names = []

 = DeltaReticulum


class EpsilonReticulum(FixedStar): # ,epsRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsRet", context=context, swe_string="Epsilon Reticulum,epsRet,ICRS,04,16,29.02921,-59,18,07.7614,-47.53,-167.58,29.3,54.83,4.44,0,0")
        self._other_names = []

 = EpsilonReticulum


class ZetaReticulum01(FixedStar): # ,zet01Ret

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zet01Ret", context=context, swe_string="Zeta Reticulum 01,zet01Ret,ICRS,03,17,46.16324,-62,34,31.1563,1337.57,649.12,12.3,83.28,5.54,-63,  217")
        self._other_names = []

 = ZetaReticulum01


class EtaReticulum(FixedStar): # ,etaRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaRet", context=context, swe_string="Eta Reticulum,etaRet,ICRS,04,21,53.3267,-63,23,10.998,85.239,175.621,45,8.48,5.24,-63,  324")
        self._other_names = []

 = EtaReticulum


class IotaReticulum(FixedStar): # ,iotRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotRet", context=context, swe_string="Iota Reticulum,iotRet,ICRS,04,01,18.15162,-61,04,43.7559,66.79,94.8,60.5,10.22,4.956,0,0")
        self._other_names = []

 = IotaReticulum


class KappaReticulum(FixedStar): # ,kapRet

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapRet", context=context, swe_string="Kappa Reticulum,kapRet,ICRS,03,29,22.67724,-62,56,15.0991,382.84,373.05,12.5,46.12,4.71,-63,  234")
        self._other_names = []

 = KappaReticulum


class PiSculptoris(FixedStar): # ,pi.Scl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Scl", context=context, swe_string="Pi Sculptoris,pi.Scl,ICRS,01,42,08.59623,-32,19,37.1331,-71.07,-51.06,10.4,15.18,5.256,-32,  666")
        self._other_names = []

 = PiSculptoris


class AlphaSculptoris(FixedStar): # ,alfScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfScl", context=context, swe_string="Alpha Sculptoris,alfScl,ICRS,00,58,36.35930,-29,21,26.8247,20.13,5.31,9.6,4.2,4.27,-30,  297")
        self._other_names = []

 = AlphaSculptoris


class BetaSculptoris(FixedStar): # ,betScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betScl", context=context, swe_string="Beta Sculptoris,betScl,ICRS,23,32,58.25898,-37,49,05.7570,95.97,38.29,0.4,18.74,4.37,-38,15527")
        self._other_names = []

 = BetaSculptoris


class GammaSculptoris(FixedStar): # ,gamScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamScl", context=context, swe_string="Gamma Sculptoris,gamScl,ICRS,23,18,49.44076,-32,31,55.2890,20.13,-77.72,15.6,17.9,4.406,-33,16476")
        self._other_names = []

 = GammaSculptoris


class DeltaSculptoris(FixedStar): # ,delScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delScl", context=context, swe_string="Delta Sculptoris,delScl,ICRS,23,48,55.54658,-28,07,48.9745,100.8,-105.34,8.7,23.73,4.57,-28,18353")
        self._other_names = []

 = DeltaSculptoris


class EpsilonSculptoris(FixedStar): # ,epsScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsScl", context=context, swe_string="Epsilon Sculptoris,epsScl,ICRS,01,45,38.75712,-25,03,09.4022,159.36,-73.17,13.1,35.57,5.31,-25,  704")
        self._other_names = []

 = EpsilonSculptoris


class ThetaSculptoris(FixedStar): # ,tetScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetScl", context=context, swe_string="Theta Sculptoris,tetScl,ICRS,00,11,44.00926,-35,07,59.2233,169.83,114.56,-1.6,47,5.239,-35,   42")
        self._other_names = []

 = ThetaSculptoris


class KappaSculptoris02(FixedStar): # ,kap02Scl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kap02Scl", context=context, swe_string="Kappa Sculptoris 02,kap02Scl,ICRS,00,11,34.41935,-27,47,59.0290,3.42,19.8,-5.6,4.11,5.404,-28,   26")
        self._other_names = []

 = KappaSculptoris02


class LambdaSculptoris02(FixedStar): # ,lam02Scl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lam02Scl", context=context, swe_string="Lambda Sculptoris 02,lam02Scl,ICRS,00,44,12.09871,-38,25,18.0704,246.29,120.53,26.5,9.63,5.96,-39,  181")
        self._other_names = []

 = LambdaSculptoris02


class MessierObjectu.Scl(FixedStar): # ,mu.Scl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Scl", context=context, swe_string="Messier Object u.Scl,mu.Scl,ICRS,23,40,38.14912,-32,04,23.2482,-91.3,-53.29,14.9,11.18,5.303,-32,17621")
        self._other_names = []

 = MessierObjectu.Scl


class SigmaSculptoris(FixedStar): # ,sigScl

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigScl", context=context, swe_string="Sigma Sculptoris,sigScl,ICRS,01,02,26.43280,-31,33,07.2237,80.5,14.64,-15.4,14.04,5.501,-32,  410")
        self._other_names = []

 = SigmaSculptoris


class AlphaScorpii(FixedStar): # ,alfSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSco", context=context, swe_string="Alpha Scorpii,alfSco,ICRS,16,29,24.45970,-26,25,55.2094,-12.11,-23.3,-3.5,5.89,0.91,-26,11359")
        self._other_names = ['Antares']

Antares = AlphaScorpii


class AlphaScorpii(FixedStar): # ,alfSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSco", context=context, swe_string="Alpha Scorpii,alfSco,ICRS,16,29,24.45970,-26,25,55.2094,-12.11,-23.3,-3.5,5.89,0.91,-26,11359")
        self._other_names = ['Jyeshtha']

Jyeshtha = AlphaScorpii


class BetaScorpii01(FixedStar): # ,bet01Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet01Sco", context=context, swe_string="Beta Scorpii 01,bet01Sco,ICRS,16,05,26.23198,-19,48,19.6300,-5.2,-24.04,-1,8.07,2.62,-19, 4307")
        self._other_names = ['Graffias']

Graffias = BetaScorpii01


class BetaScorpii01(FixedStar): # ,bet01Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet01Sco", context=context, swe_string="Beta Scorpii 01,bet01Sco,ICRS,16,05,26.23198,-19,48,19.6300,-5.2,-24.04,-1,8.07,2.62,-19, 4307")
        self._other_names = ['Akrab']

Akrab = BetaScorpii01


class BetaScorpii01(FixedStar): # ,bet01Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet01Sco", context=context, swe_string="Beta Scorpii 01,bet01Sco,ICRS,16,05,26.23198,-19,48,19.6300,-5.2,-24.04,-1,8.07,2.62,-19, 4307")
        self._other_names = ['Acrab']

Acrab = BetaScorpii01


class BetaScorpii02(FixedStar): # ,bet02Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet02Sco", context=context, swe_string="Beta Scorpii 02,bet02Sco,ICRS,16,05,26.57128,-19,48,06.8556,-5.07,-25.87,-5.6,8.19,4.89,0, 0")
        self._other_names = []

 = BetaScorpii02


class MessierObject6(FixedStar): # ,M6

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M6", context=context, swe_string="Messier Object 6,M6,ICRS,17,40,20.0,-32,15,12,-2.38,-7.19,-7.05,2.04,4.2,0, 0 # NGC 6405")
        self._other_names = ['Aculeus']

Aculeus = MessierObject6


class MessierObject7(FixedStar): # ,M7

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M7", context=context, swe_string="Messier Object 7,M7,ICRS,17,53,51.0,-34,47,36,2.58,-4.54,-21.38,0,3.3,0, 0 # NGC 6475")
        self._other_names = ['Acumen']

Acumen = MessierObject7


class DeltaScorpii(FixedStar): # ,delSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSco", context=context, swe_string="Delta Scorpii,delSco,ICRS,16,00,20.00528,-22,37,18.1431,-10.21,-35.41,-6,6.64,2.32,-22, 4068")
        self._other_names = ['Dschubba']

Dschubba = DeltaScorpii


class DeltaScorpii(FixedStar): # ,delSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSco", context=context, swe_string="Delta Scorpii,delSco,ICRS,16,00,20.00528,-22,37,18.1431,-10.21,-35.41,-6,6.64,2.32,-22, 4068")
        self._other_names = ['Anuradha']

Anuradha = DeltaScorpii


class EpsilonScorpii(FixedStar): # ,epsSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsSco", context=context, swe_string="Epsilon Scorpii,epsSco,ICRS,16,50,09.81081,-34,17,35.6337,-614.85,-255.98,-2.5,51.19,2.29,-34,11285")
        self._other_names = ['Wei']

Wei = EpsilonScorpii


class EpsilonScorpii(FixedStar): # ,epsSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsSco", context=context, swe_string="Epsilon Scorpii,epsSco,ICRS,16,50,09.81081,-34,17,35.6337,-614.85,-255.98,-2.5,51.19,2.29,-34,11285")
        self._other_names = ['Larawag']

Larawag = EpsilonScorpii


class ZetaScorpii02(FixedStar): # ,zet02Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zet02Sco", context=context, swe_string="Zeta Scorpii 02,zet02Sco,ICRS,16,54,35.00435,-42,21,40.7407,-127.72,-229.44,-18.7,24.65,3.62,0, 0")
        self._other_names = []

 = ZetaScorpii02


class EtaScorpii(FixedStar): # ,etaSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaSco", context=context, swe_string="Eta Scorpii,etaSco,ICRS,17,12,09.19565,-43,14,21.0905,24.47,-288.55,-27,44.39,3.33,-43,11485")
        self._other_names = []

 = EtaScorpii


class ThetaScorpii(FixedStar): # ,tetSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetSco", context=context, swe_string="Theta Scorpii,tetSco,ICRS,17,37,19.12985,-42,59,52.1808,5.54,-3.12,1.4,10.86,1.862,-42,12312")
        self._other_names = ['Sargas']

Sargas = ThetaScorpii


class IotaScorpii01(FixedStar): # ,iot01Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iot01Sco", context=context, swe_string="Iota Scorpii 01,iot01Sco,ICRS,17,47,35.08113,-40,07,37.1893,0.01,-6.24,-27.6,1.69,2.992,-40,11838")
        self._other_names = []

 = IotaScorpii01


class KappaScorpii(FixedStar): # ,kapSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapSco", context=context, swe_string="Kappa Scorpii,kapSco,ICRS,17,42,29.27520,-39,01,47.9391,-6.05,-25.54,-14,6.75,2.386,-38,12137")
        self._other_names = ['Girtab']

Girtab = KappaScorpii


class LambdaScorpii(FixedStar): # ,lamSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamSco", context=context, swe_string="Lambda Scorpii,lamSco,ICRS,17,33,36.52012,-37,06,13.7648,-8.53,-30.8,-3,5.71,1.62,-37,11673")
        self._other_names = ['Shaula']

Shaula = LambdaScorpii


class LambdaScorpii(FixedStar): # ,lamSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamSco", context=context, swe_string="Lambda Scorpii,lamSco,ICRS,17,33,36.52012,-37,06,13.7648,-8.53,-30.8,-3,5.71,1.62,-37,11673")
        self._other_names = ['Mula']

Mula = LambdaScorpii


class MessierObjectu.01Sco(FixedStar): # ,mu.01Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.01Sco", context=context, swe_string="Messier Object u.01Sco,mu.01Sco,ICRS,16,51,52.23111,-38,02,50.5694,-10.58,-22.06,-7.6,6.51,2.98,-37,11033")
        self._other_names = ['Xamidimura']

Xamidimura = MessierObjectu.01Sco


class NuScorpii(FixedStar): # ,nu.Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Sco", context=context, swe_string="Nu Scorpii,nu.Sco,ICRS,16,11,59.73568,-19,27,38.5361,-7.65,-23.71,2.4,6.88,4,-19, 4333")
        self._other_names = ['Jabbah']

Jabbah = NuScorpii


class XiScorpii(FixedStar): # ,ksiSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiSco", context=context, swe_string="Xi Scorpii,ksiSco,ICRS,16,04,22.191,-11,22,22.60,-63.2,-27,-36.33,0,4.17,-10, 4237")
        self._other_names = ['Grafias']

Grafias = XiScorpii


class PiScorpii(FixedStar): # ,pi.Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Sco", context=context, swe_string="Pi Scorpii,pi.Sco,ICRS,15,58,51.11324,-26,06,50.7886,-11.42,-26.83,-7.4,5.57,2.91,-25,11228")
        self._other_names = ['Fang']

Fang = PiScorpii


class RhoScorpii(FixedStar): # ,rhoSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoSco", context=context, swe_string="Rho Scorpii,rhoSco,ICRS,15,56,53.07624,-29,12,50.6612,-15.68,-24.88,-0.4,6.91,3.86,0,0")
        self._other_names = ['Iklil']

Iklil = RhoScorpii


class SigmaScorpii(FixedStar): # ,sigSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigSco", context=context, swe_string="Sigma Scorpii,sigSco,ICRS,16,21,11.31571,-25,35,34.0515,-10.6,-16.28,-0.4,4.68,2.89,-25,11485")
        self._other_names = ['Alniyat']

Alniyat = SigmaScorpii


class TauScorpii(FixedStar): # ,tauSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauSco", context=context, swe_string="Tau Scorpii,tauSco,ICRS,16,35,52.95285,-28,12,57.6615,-9.89,-22.83,2,6.88,2.81,-27,11015")
        self._other_names = []

 = TauScorpii


class UpsilonScorpii(FixedStar): # ,upsSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsSco", context=context, swe_string="Upsilon Scorpii,upsSco,ICRS,17,30,45.83712,-37,17,44.9285,-2.37,-30.09,8,5.66,2.7,-37,11638")
        self._other_names = ['Lesath']

Lesath = UpsilonScorpii


class OmegaScorpii01(FixedStar): # ,ome01Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome01Sco", context=context, swe_string="Omega Scorpii 01,ome01Sco,ICRS,16,06,48.42692,-20,40,09.0902,-8.98,-23.48,-4.4,6.92,3.97,-20, 4405")
        self._other_names = ['Jabhat al Akrab']

JabhatalAkrab = OmegaScorpii01


class OmegaScorpii02(FixedStar): # ,ome02Sco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome02Sco", context=context, swe_string="Omega Scorpii 02,ome02Sco,ICRS,16,07,24.32818,-20,52,07.5518,44.81,-45.42,-4.8,11.22,4.33,-20, 4408")
        self._other_names = ['Jabhat al Akrab']

JabhatalAkrab = OmegaScorpii02


class GScorpii(FixedStar): # ,gSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gSco", context=context, swe_string="G Scorpii,gSco,ICRS,17,49,51.4808976914,-37,02,35.794961894,41.717,11.975,24.70,24.7340,3.21")
        self._other_names = ['Fuyue', 'HIP 87261']

Fuyue = GScorpii
HIP87261 = GScorpii


class AlphaScuti(FixedStar): # ,alfSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSct", context=context, swe_string="Alpha Scuti,alfSct,ICRS,18,35,12.42776,-08,14,38.6529,-17,-313.52,36.5,16.38,3.83,-08, 4638")
        self._other_names = []

 = AlphaScuti


class BetaScuti(FixedStar): # ,betSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betSct", context=context, swe_string="Beta Scuti,betSct,ICRS,18,47,10.47250,-04,44,52.3271,-8.44,-16.37,-21.3,3.56,4.22,-04, 4582")
        self._other_names = []

 = BetaScuti


class GammaScuti(FixedStar): # ,gamSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamSct", context=context, swe_string="Gamma Scuti,gamSct,ICRS,18,29,11.85388,-14,33,56.9319,3.22,-4.02,-41,10.21,4.675,-14, 5071")
        self._other_names = []

 = GammaScuti


class DeltaScuti(FixedStar): # ,delSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSct", context=context, swe_string="Delta Scuti,delSct,ICRS,18,42,16.427,-09,03,09.18,9.21,0.82,-45.1,16.11,4.71,-09, 4796")
        self._other_names = []

 = DeltaScuti


class EpsilonScuti(FixedStar): # ,epsSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsSct", context=context, swe_string="Epsilon Scuti,epsSct,ICRS,18,43,31.252,-08,16,30.80,21.06,9.11,-9.8,6.06,4.889,-08, 4686")
        self._other_names = []

 = EpsilonScuti


class ZetaScuti(FixedStar): # ,zetSct

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetSct", context=context, swe_string="Zeta Scuti,zetSct,ICRS,18,23,39.58309,-08,56,03.7885,49.59,51.24,-5.02,15.78,4.664,0, 0")
        self._other_names = []

 = ZetaScuti


class AlphaSerpentis(FixedStar): # ,alfSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSer", context=context, swe_string="Alpha Serpentis,alfSer,ICRS,15,44,16.07431,+06,25,32.2633,133.84,44.81,2.63,44.1,2.63, 06, 3088")
        self._other_names = ['Unukalhai']

Unukalhai = AlphaSerpentis


class AlphaSerpentis(FixedStar): # ,alfSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSer", context=context, swe_string="Alpha Serpentis,alfSer,ICRS,15,44,16.07431,+06,25,32.2633,133.84,44.81,2.63,44.1,2.63, 06, 3088")
        self._other_names = ['Cor Serpentis']

CorSerpentis = AlphaSerpentis


class BetaSerpentis(FixedStar): # ,betSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betSer", context=context, swe_string="Beta Serpentis,betSer,ICRS,15,46,11.25435,+15,25,18.5959,65.38,-38.61,0.6,21.03,3.67, 15, 2911")
        self._other_names = ['Chow']

Chow = BetaSerpentis


class BetaSerpentis(FixedStar): # ,betSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betSer", context=context, swe_string="Beta Serpentis,betSer,ICRS,15,46,11.25435,+15,25,18.5959,65.38,-38.61,0.6,21.03,3.67, 15, 2911")
        self._other_names = ['Zhou']

Zhou = BetaSerpentis


class GammaSerpentis(FixedStar): # ,gamSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamSer", context=context, swe_string="Gamma Serpentis,gamSer,ICRS,15,56,27.18269,+15,39,41.8206,310.93,-1282.19,6.78,88.86,3.84, 16, 2849")
        self._other_names = ['Ainalhai']

Ainalhai = GammaSerpentis


class DeltaSerpentis(FixedStar): # ,delSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSer", context=context, swe_string="Delta Serpentis,delSer,ICRS,15,34,48.14762,+10,32,19.9248,-71.48,3.64,-41.5,14.3,3.79, 0,0")
        self._other_names = ['Qin']

Qin = DeltaSerpentis


class DeltaSerpentis(FixedStar): # ,delSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSer", context=context, swe_string="Delta Serpentis,delSer,ICRS,15,34,48.14762,+10,32,19.9248,-71.48,3.64,-41.5,14.3,3.79, 0,0")
        self._other_names = ['Chin']

Chin = DeltaSerpentis


class EpsilonSerpentis(FixedStar): # ,epsSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsSer", context=context, swe_string="Epsilon Serpentis,epsSer,ICRS,15,50,48.96622,+04,28,39.8311,128.19,62.16,-9.4,46.3,3.693, 04, 3069")
        self._other_names = ['Nulla Pambu']

NullaPambu = EpsilonSerpentis


class EtaSerpentis(FixedStar): # ,etaSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaSer", context=context, swe_string="Eta Serpentis,etaSer,ICRS,18,21,18.60056,-02,53,55.7766,-547.75,-701.42,9.83,53.93,3.25,-02, 4599")
        self._other_names = ['Tang']

Tang = EtaSerpentis


class ThetaSerpentis01(FixedStar): # ,tet01Ser

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet01Ser", context=context, swe_string="Theta Serpentis 01,tet01Ser,ICRS,18,56,13.18150,+04,12,12.9124,36.23,23.15,-48.7,21.09,4.62, 04, 3916")
        self._other_names = ['Alya']

Alya = ThetaSerpentis01


class KappaSerpentis(FixedStar): # ,kapSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapSer", context=context, swe_string="Kappa Serpentis,kapSer,ICRS,15,48,44.37676,+18,08,29.6342,-51.88,-88.1,-38.48,8.54,4.09, 18, 3074")
        self._other_names = []

 = KappaSerpentis


class MessierObjectu.Ser(FixedStar): # ,mu.Ser

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Ser", context=context, swe_string="Messier Object u.Ser,mu.Ser,ICRS,15,49,37.20696,-03,25,48.7358,-100.28,-25.99,-9.4,19.23,3.53,-02, 4052")
        self._other_names = ['Leiolepis']

Leiolepis = MessierObjectu.Ser


class MessierObjectu.Ser(FixedStar): # ,mu.Ser

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Ser", context=context, swe_string="Messier Object u.Ser,mu.Ser,ICRS,15,49,37.20696,-03,25,48.7358,-100.28,-25.99,-9.4,19.23,3.53,-02, 4052")
        self._other_names = ['Leiolepidotus']

Leiolepidotus = MessierObjectu.Ser


class NuSerpentis(FixedStar): # ,nu.Ser

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Ser", context=context, swe_string="Nu Serpentis,nu.Ser,ICRS,17,20,49.66149,-12,50,48.7533,43.4,2.61,4.8,16.05,4.324,0,0")
        self._other_names = []

 = NuSerpentis


class XiSerpentis(FixedStar): # ,ksiSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiSer", context=context, swe_string="Xi Serpentis,ksiSer,ICRS,17,37,35.19983,-15,23,54.7940,-42.1,-59.94,-42.8,30.98,3.519,-15, 4621")
        self._other_names = ['Nehushtan']

Nehushtan = XiSerpentis


class OmicronSerpentis(FixedStar): # ,omiSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiSer", context=context, swe_string="Omicron Serpentis,omiSer,ICRS,17,41,24.87286,-12,52,31.1086,-72.9,-55.55,-30.2,18.83,4.228,0,0")
        self._other_names = []

 = OmicronSerpentis


class SigmaSerpentis(FixedStar): # ,sigSer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigSer", context=context, swe_string="Sigma Serpentis,sigSer,ICRS,16,22,04.34753,+01,01,44.5534,-158.4,49.56,-49.3,36.67,4.817, 01, 3215")
        self._other_names = []

 = SigmaSerpentis


class TauSerpentis01(FixedStar): # ,tau01Ser

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tau01Ser", context=context, swe_string="Tau Serpentis 01,tau01Ser,ICRS,15,25,47.39750,+15,25,40.9307,-12.52,-7.41,-16.51,4.73,5.17, 15, 2858")
        self._other_names = []

 = TauSerpentis01


class AlphaSextantis(FixedStar): # ,alfSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSex", context=context, swe_string="Alpha Sextantis,alfSex,ICRS,10,07,56.287,-00,22,17.95,-25.83,-4.25,10,11.51,4.49,0,0")
        self._other_names = []

 = AlphaSextantis


class BetaSextantis(FixedStar): # ,betSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betSex", context=context, swe_string="Beta Sextantis,betSex,ICRS,10,30,17.481,-00,38,13.31,-39.23,-22.83,11.6,8.06,5.1,0,0")
        self._other_names = []

 = BetaSextantis


class GammaSextantis(FixedStar): # ,gamSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamSex", context=context, swe_string="Gamma Sextantis,gamSex,ICRS,09,52,30.43727,-08,06,18.1269,-57.28,-49.26,12.2,11.75,5.107,0,0")
        self._other_names = []

 = GammaSextantis


class DeltaSextantis(FixedStar): # ,delSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSex", context=context, swe_string="Delta Sextantis,delSex,ICRS,10,29,28.70222,-02,44,20.6862,-48.86,-13.43,19,10.13,5.18,-02, 3155")
        self._other_names = []

 = DeltaSextantis


class EpsilonSextantis(FixedStar): # ,epsSex

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsSex", context=context, swe_string="Epsilon Sextantis,epsSex,ICRS,10,17,37.80200,-08,04,08.0898,-160.57,2.91,15.2,16.86,5.24,-07, 3001")
        self._other_names = []

 = EpsilonSextantis


class AlphaSagittae(FixedStar): # ,alfSge

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSge", context=context, swe_string="Alpha Sagittae,alfSge,ICRS,19,40,05.79186,+18,00,50.0061,15.09,-19.65,1.72,7.67,4.38, 17, 4042")
        self._other_names = ['Sham']

Sham = AlphaSagittae


class BetaSagittae(FixedStar): # ,betSge

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betSge", context=context, swe_string="Beta Sagittae,betSge,ICRS,19,41,02.93907,+17,28,33.7528,8.74,-33.41,-22,7.42,4.38, 17, 4048")
        self._other_names = []

 = BetaSagittae


class GammaSagittae(FixedStar): # ,gamSge

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamSge", context=context, swe_string="Gamma Sagittae,gamSge,ICRS,19,58,45.42863,+19,29,31.7281,66.21,22.22,-34,12.62,3.47, 19, 4229")
        self._other_names = []

 = GammaSagittae


class DeltaSagittae(FixedStar): # ,delSge

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSge", context=context, swe_string="Delta Sagittae,delSge,ICRS,19,47,23.26253,+18,32,03.4401,-4.31,12.35,2.5,5.49,3.82, 18, 4240")
        self._other_names = []

 = DeltaSagittae


class AlphaSagittarii(FixedStar): # ,alfSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfSgr", context=context, swe_string="Alpha Sagittarii,alfSgr,ICRS,19,23,53.17483,-40,36,57.3705,30.49,-119.21,-0.7,17.94,3.943,-40,13245")
        self._other_names = ['Rukbat']

Rukbat = AlphaSagittarii


class BetaSagittarii01(FixedStar): # ,bet01Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet01Sgr", context=context, swe_string="Beta Sagittarii 01,bet01Sgr,ICRS,19,22,38.29770,-44,27,32.2458,13.67,-19.03,-10.7,10.4,4.01,-44,13277")
        self._other_names = ['Arkab Prior']

ArkabPrior = BetaSagittarii01


class BetaSagittarii02(FixedStar): # ,bet02Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet02Sgr", context=context, swe_string="Beta Sagittarii 02,bet02Sgr,ICRS,19,23,13.13745,-44,47,59.2051,93.45,-54.09,19,24.31,4.27,-45,13171")
        self._other_names = ['Arkab Posterior']

ArkabPosterior = BetaSagittarii02


class GammaSagittarii(FixedStar): # ,gamSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamSgr", context=context, swe_string="Gamma Sagittarii,gamSgr,ICRS,18,05,48.48810,-30,25,26.7235,-53.92,-180.9,22,33.67,2.99,-30,15215")
        self._other_names = ['Alnasl']

Alnasl = GammaSagittarii


class GammaSagittarii02(FixedStar): # ,gam02Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam02Sgr", context=context, swe_string="Gamma Sagittarii 02,gam02Sgr,ICRS,18,05,48.48810,-30,25,26.7235,-53.92,-180.9,22,33.67,2.99,-30,15215")
        self._other_names = ['Alnasl']

Alnasl = GammaSagittarii02


class GammaSagittarii02(FixedStar): # ,gam02Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam02Sgr", context=context, swe_string="Gamma Sagittarii 02,gam02Sgr,ICRS,18,05,48.48810,-30,25,26.7235,-53.92,-180.9,22,33.67,2.99,-30,15215")
        self._other_names = ['Nash']

Nash = GammaSagittarii02


class DeltaSagittarii(FixedStar): # ,delSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSgr", context=context, swe_string="Delta Sagittarii,delSgr,ICRS,18,20,59.64354,-29,49,41.1659,32.54,-25.57,-20.4,9.38,2.668,-29,14834")
        self._other_names = ['Kaus Media']

KausMedia = DeltaSagittarii


class DeltaSagittarii(FixedStar): # ,delSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSgr", context=context, swe_string="Delta Sagittarii,delSgr,ICRS,18,20,59.64354,-29,49,41.1659,32.54,-25.57,-20.4,9.38,2.668,-29,14834")
        self._other_names = ['Kaus Meridionalis']

KausMeridionalis = DeltaSagittarii


class DeltaSagittarii(FixedStar): # ,delSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delSgr", context=context, swe_string="Delta Sagittarii,delSgr,ICRS,18,20,59.64354,-29,49,41.1659,32.54,-25.57,-20.4,9.38,2.668,-29,14834")
        self._other_names = ['Purvashadha']

Purvashadha = DeltaSagittarii


class EpsilonSagittarii(FixedStar): # ,epsSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsSgr", context=context, swe_string="Epsilon Sagittarii,epsSgr,ICRS,18,24,10.31840,-34,23,04.6193,-39.42,-124.2,-15,22.76,1.85,-34, 12784")
        self._other_names = ['Kaus Australis']

KausAustralis = EpsilonSagittarii


class ZetaSagittarii(FixedStar): # ,zetSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetSgr", context=context, swe_string="Zeta Sagittarii,zetSgr,ICRS,19,02,36.73024,-29,52,48.2279,10.79,21.11,24.7,36.98,2.585,-30,16575")
        self._other_names = ['Ascella']

Ascella = ZetaSagittarii


class EtaSagittarii(FixedStar): # ,etaSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaSgr", context=context, swe_string="Eta Sagittarii,etaSgr,ICRS,18,17,37.63505,-36,45,42.0667,-129.56,-166.26,0.2,22.35,3.11,-36,12423")
        self._other_names = ['Sephdar']

Sephdar = EtaSagittarii


class EtaSagittarii(FixedStar): # ,etaSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaSgr", context=context, swe_string="Eta Sagittarii,etaSgr,ICRS,18,17,37.63505,-36,45,42.0667,-129.56,-166.26,0.2,22.35,3.11,-36,12423")
        self._other_names = ['Ira Furoris']

IraFuroris = EtaSagittarii


class ThetaSagittarii01(FixedStar): # ,tet01Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet01Sgr", context=context, swe_string="Theta Sagittarii 01,tet01Sgr,ICRS,19,59,44.17834,-35,16,34.7049,5.6,-25.81,0.9,6.29,4.37,-35,13831")
        self._other_names = []

 = ThetaSagittarii01


class ThetaSagittarii02(FixedStar): # ,tet02Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet02Sgr", context=context, swe_string="Theta Sagittarii 02,tet02Sgr,ICRS,19,59,51.35684,-34,41,52.0797,108.23,-69.51,-17.6,20.62,5.299,0,0")
        self._other_names = []

 = ThetaSagittarii02


class IotaSagittarii(FixedStar): # ,iotSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotSgr", context=context, swe_string="Iota Sagittarii,iotSgr,ICRS,19,55,15.69691,-41,52,05.8388,22.61,51.4,35.8,17.94,4.13,-42,14549")
        self._other_names = []

 = IotaSagittarii


class KappaSagittarii01(FixedStar): # ,kap01Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kap01Sgr", context=context, swe_string="Kappa Sagittarii 01,kap01Sgr,ICRS,20,22,27.50366,-42,02,58.3648,30.92,-80.91,-3.4,15.12,5.59,-42,14836")
        self._other_names = []

 = KappaSagittarii01


class LambdaSagittarii(FixedStar): # ,lamSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamSgr", context=context, swe_string="Lambda Sagittarii,lamSgr,ICRS,18,27,58.24072,-25,25,18.1146,-44.76,-185.66,-43.2,41.72,2.81,-25,13149")
        self._other_names = ['Kaus Borealis']

KausBorealis = LambdaSagittarii


class MessierObjectu.Sgr(FixedStar): # ,mu.Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Sgr", context=context, swe_string="Messier Object u.Sgr,mu.Sgr,ICRS,18,13,45.80884,-21,03,31.7941,0.3,-0.48,-6,0.09,3.85,-21, 4908")
        self._other_names = ['Polis']

Polis = MessierObjectu.Sgr


class NuSagittarii01(FixedStar): # ,nu.01Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.01Sgr", context=context, swe_string="Nu Sagittarii 01,nu.01Sgr,ICRS,18,54,10.17695,-22,44,41.4247,2.59,-8.41,-11.6,2.9,4.845,-22, 4907")
        self._other_names = ['Ainalrami']

Ainalrami = NuSagittarii01


class NuSagittarii01(FixedStar): # ,nu.01Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.01Sgr", context=context, swe_string="Nu Sagittarii 01,nu.01Sgr,ICRS,18,54,10.17695,-22,44,41.4247,2.59,-8.41,-11.6,2.9,4.845,-22, 4907")
        self._other_names = ['Ain al Rami']

AinalRami = NuSagittarii01


class XiSagittarii02(FixedStar): # ,ksi02Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksi02Sgr", context=context, swe_string="Xi Sagittarii 02,ksi02Sgr,ICRS,18,57,43.79908,-21,06,23.9613,31.72,-13.33,-20.1,8.93,3.51,-21, 5201")
        self._other_names = []

 = XiSagittarii02


class OmicronSagittarii(FixedStar): # ,omiSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiSgr", context=context, swe_string="Omicron Sagittarii,omiSgr,ICRS,19,04,40.98177,-21,44,29.3845,76.35,-58.12,26.1,22.96,3.77,-21, 5237")
        self._other_names = ['Manubrium']

Manubrium = OmicronSagittarii


class PiSagittarii(FixedStar): # ,pi.Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Sgr", context=context, swe_string="Pi Sagittarii,pi.Sgr,ICRS,19,09,45.83293,-21,01,25.0103,-1.36,-36.45,-9.8,6.4,2.88,-21, 5275")
        self._other_names = ['Albaldah']

Albaldah = PiSagittarii


class SigmaSagittarii(FixedStar): # ,sigSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigSgr", context=context, swe_string="Sigma Sagittarii,sigSgr,ICRS,18,55,15.92650,-26,17,48.2068,15.14,-53.43,-11.2,14.32,2.067,-26,13595")
        self._other_names = ['Nunki']

Nunki = SigmaSagittarii


class SigmaSagittarii(FixedStar): # ,sigSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigSgr", context=context, swe_string="Sigma Sagittarii,sigSgr,ICRS,18,55,15.92650,-26,17,48.2068,15.14,-53.43,-11.2,14.32,2.067,-26,13595")
        self._other_names = ['Uttarashadha']

Uttarashadha = SigmaSagittarii


class TauSagittarii(FixedStar): # ,tauSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauSgr", context=context, swe_string="Tau Sagittarii,tauSgr,ICRS,19,06,56.40897,-27,40,13.5189,-50.61,-249.8,45.4,26.82,3.31,-27,13564")
        self._other_names = ['Hecatebolus']

Hecatebolus = TauSagittarii


class PhiSagittarii(FixedStar): # ,phiSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiSgr", context=context, swe_string="Phi Sagittarii,phiSgr,ICRS,18,45,39.38610,-26,59,26.7944,50.61,1.22,21.5,13.63,3.14,-27,13170")
        self._other_names = ['Nanto']

Nanto = PhiSagittarii


class UpsilonSagittarii(FixedStar): # ,upsSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsSgr", context=context, swe_string="Upsilon Sagittarii,upsSgr,ICRS,19,21,43.62284,-15,57,18.0625,1.34,-6.25,8.9,1.83,4.61,-16, 5283")
        self._other_names = []

 = UpsilonSagittarii


class OmegaSagittarii(FixedStar): # ,omeSgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omeSgr", context=context, swe_string="Omega Sagittarii,omeSgr,ICRS,19,55,50.36119,-26,17,58.3215,209.41,62.39,-21,38.48,4.7,-26,14637")
        self._other_names = ['Terebellium']

Terebellium = OmegaSagittarii


class SgrA*(FixedStar): # ,SgrA*

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SgrA*", context=context, swe_string="SgrA*,SgrA*,ICRS,17,45,40.03599,-29,00,28.1699,-2.755718425, -5.547,  0.0,0.125,999.99,  0,    0")
        self._other_names = ['Gal. Center']

Gal.Center = SgrA*


class SgrA*(FixedStar): # ,SgrA*

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SgrA*", context=context, swe_string="SgrA*,SgrA*,ICRS,17,45,40.03599,-29,00,28.1699,-2.755718425, -5.547,  0.0,0.125,999.99,  0,    0")
        self._other_names = ['Galactic Center']

GalacticCenter = SgrA*


class SgrA*(FixedStar): # ,SgrA*

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SgrA*", context=context, swe_string="SgrA*,SgrA*,ICRS,17,45,40.03599,-29,00,28.1699,-2.755718425, -5.547,  0.0,0.125,999.99,  0,    0")
        self._other_names = ['Galactic Center']

GalacticCenter = SgrA*


class MessierObject22(FixedStar): # ,M22

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M22", context=context, swe_string="Messier Object 22,M22,ICRS,18,36,23.94,-23,54,17.1,4.72,-3.59,-148,0.3136,6.17,0, 0 # NGC 6656")
        self._other_names = ['Facies']

Facies = MessierObject22


class NewGeneralCatalogue6530(FixedStar): # ,NGC6530

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",NGC6530", context=context, swe_string="New General Catalogue 6530,NGC6530,ICRS,18,04,31.00,-24,21,30,0.91,-3.22,-13.32,0.6272,4.6,0, 0 # NGC 6530")
        self._other_names = ['Spiculum']

Spiculum = NewGeneralCatalogue6530


class Sagittarii52(FixedStar): # ,52Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",52Sgr", context=context, swe_string="Sagittarii52,52Sgr,ICRS,19,36,42.43288,-24,53,01.0288,68.3,-21.51,-19,17.2,4.598,0, 0")
        self._other_names = []

 = Sagittarii52


class Sagittarii59(FixedStar): # ,59Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",59Sgr", context=context, swe_string="Sagittarii59,59Sgr,ICRS,19,56,56.83165,-27,10,11.6409,10.46,-15.52,-16.2,3.92,4.528,0, 0")
        self._other_names = []

 = Sagittarii59


class Sagittarii62(FixedStar): # ,62Sgr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",62Sgr", context=context, swe_string="Sagittarii62,62Sgr,ICRS,20,02,39.48097,-27,42,35.4442,32.97,14,9.9,7.27,4.58,0, 0")
        self._other_names = []

 = Sagittarii62


class AlphaTauri(FixedStar): # ,alfTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTau", context=context, swe_string="Alpha Tauri,alfTau,ICRS,04,35,55.23907,+16,30,33.4885,63.45,-188.94,54.26,48.94,0.86, 16,  629")
        self._other_names = ['Aldebaran']

Aldebaran = AlphaTauri


class BetaTauri(FixedStar): # ,betTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betTau", context=context, swe_string="Beta Tauri,betTau,ICRS,05,26,17.51312,+28,36,26.8262,22.76,-173.58,9.2,24.36,1.65, 28,  795")
        self._other_names = ['Elnath']

Elnath = BetaTauri


class BetaTauri(FixedStar): # ,betTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betTau", context=context, swe_string="Beta Tauri,betTau,ICRS,05,26,17.51312,+28,36,26.8262,22.76,-173.58,9.2,24.36,1.65, 28,  795")
        self._other_names = ['El Nath']

ElNath = BetaTauri


class BetaTauri(FixedStar): # ,betTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betTau", context=context, swe_string="Beta Tauri,betTau,ICRS,05,26,17.51312,+28,36,26.8262,22.76,-173.58,9.2,24.36,1.65, 28,  795")
        self._other_names = ['Alnath']

Alnath = BetaTauri


class GammaTauri(FixedStar): # ,gamTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamTau", context=context, swe_string="Gamma Tauri,gamTau,ICRS,04,19,47.60385,+15,37,39.5154,115.46,-23.42,38.58,20.19,3.65, 15,  612")
        self._other_names = ['Prima Hyadum']

PrimaHyadum = GammaTauri


class GammaTauri(FixedStar): # ,gamTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamTau", context=context, swe_string="Gamma Tauri,gamTau,ICRS,04,19,47.60385,+15,37,39.5154,115.46,-23.42,38.58,20.19,3.65, 15,  612")
        self._other_names = ['Hyadum I']

HyadumI = GammaTauri


class DeltaTauri(FixedStar): # ,delTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delTau", context=context, swe_string="Delta Tauri,delTau,ICRS,04,22,56.09253,+17,32,33.0487,106.56,-29.18,37.91,20.96,3.76, 17,  712")
        self._other_names = ['Secunda Hyadum']

SecundaHyadum = DeltaTauri


class DeltaTauri01(FixedStar): # ,del01Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del01Tau", context=context, swe_string="Delta Tauri 01,del01Tau,ICRS,04,22,56.09253,+17,32,33.0487,106.56,-29.18,37.91,20.96,3.76, 17,  712")
        self._other_names = ['Secunda Hyadum']

SecundaHyadum = DeltaTauri01


class DeltaTauri01(FixedStar): # ,del01Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del01Tau", context=context, swe_string="Delta Tauri 01,del01Tau,ICRS,04,22,56.09253,+17,32,33.0487,106.56,-29.18,37.91,20.96,3.76, 17,  712")
        self._other_names = ['Hyadum II']

HyadumII = DeltaTauri01


class EpsilonTauri(FixedStar): # ,epsTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsTau", context=context, swe_string="Epsilon Tauri,epsTau,ICRS,04,28,36.99882,+19,10,49.5446,106.19,-37.84,38.5,22.24,3.53, 18,  640")
        self._other_names = ['Ain']

Ain = EpsilonTauri


class ZetaTauri(FixedStar): # ,zetTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetTau", context=context, swe_string="Zeta Tauri,zetTau,ICRS,05,37,38.68542,+21,08,33.1588,1.78,-20.07,20,7.33,3.03, 21,  908")
        self._other_names = ['Al Hecka']

AlHecka = ZetaTauri


class ZetaTauri(FixedStar): # ,zetTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetTau", context=context, swe_string="Zeta Tauri,zetTau,ICRS,05,37,38.68542,+21,08,33.1588,1.78,-20.07,20,7.33,3.03, 21,  908")
        self._other_names = ['Tianguan']

Tianguan = ZetaTauri


class EtaTauri(FixedStar): # ,etaTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaTau", context=context, swe_string="Eta Tauri,etaTau,ICRS,03,47,29.07655,+24,06,18.4883,19.34,-43.67,5.4,8.09,2.87, 23,  541")
        self._other_names = ['Alcyone']

Alcyone = EtaTauri


class EtaTauri(FixedStar): # ,etaTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaTau", context=context, swe_string="Eta Tauri,etaTau,ICRS,03,47,29.07655,+24,06,18.4883,19.34,-43.67,5.4,8.09,2.87, 23,  541")
        self._other_names = ['Krttika']

Krttika = EtaTauri


class ThetaTauri01(FixedStar): # ,tet01Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet01Tau", context=context, swe_string="Theta Tauri 01,tet01Tau,ICRS,04,28,34.49603,+15,57,43.8494,104.97,-15.14,38.79,21.13,3.84, 0,  0")
        self._other_names = ['Phaeo']

Phaeo = ThetaTauri01


class ThetaTauri02(FixedStar): # ,tet02Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet02Tau", context=context, swe_string="Theta Tauri 02,tet02Tau,ICRS,04,28,39.74070,+15,52,15.1745,108.42,-26.74,38.9,21.69,3.41, 21,  751")
        self._other_names = ['Phaesula']

Phaesula = ThetaTauri02


class ThetaTauri02(FixedStar): # ,tet02Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tet02Tau", context=context, swe_string="Theta Tauri 02,tet02Tau,ICRS,04,28,39.74070,+15,52,15.1745,108.42,-26.74,38.9,21.69,3.41, 21,  751")
        self._other_names = ['Chamukuy']

Chamukuy = ThetaTauri02


class IotaTauri(FixedStar): # ,iotTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotTau", context=context, swe_string="Iota Tauri,iotTau,ICRS,05,03,05.74725,+21,35,23.8627,68.88,-41.06,38.3,18.88,4.61, 21,  751")
        self._other_names = []

 = IotaTauri


class LambdaTauri(FixedStar): # ,lamTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamTau", context=context, swe_string="Lambda Tauri,lamTau,ICRS,04,00,40.81572,+12,29,25.2259,-8.02,-14.42,17.8,6.74,3.41, 12,  539")
        self._other_names = ['Althaur']

Althaur = LambdaTauri


class MessierObjectu.Tau(FixedStar): # ,mu.Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Tau", context=context, swe_string="Messier Object u.Tau,mu.Tau,ICRS,04,15,32.05667,+08,53,32.4825,19.46,-22.11,16.3,7.16,4.279, 08,  657")
        self._other_names = ['Kattupothu']

Kattupothu = MessierObjectu.Tau


class NuTauri(FixedStar): # ,nu.Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Tau", context=context, swe_string="Nu Tauri,nu.Tau,ICRS,04,03,09.37966,+05,59,21.4792,4.72,-3.78,-5.7,27.89,3.883, 05,  581")
        self._other_names = ['Furibundus']

Furibundus = NuTauri


class XiTauri(FixedStar): # ,ksiTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiTau", context=context, swe_string="Xi Tauri,ksiTau,ICRS,03,27,10.15071,+09,43,57.6343,50.58,-39.54,-2,15.6,3.75, 09,  439")
        self._other_names = ['Ushakaron']

Ushakaron = XiTauri


class OmicronTauri(FixedStar): # ,omiTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiTau", context=context, swe_string="Omicron Tauri,omiTau,ICRS,03,24,48.79796,+09,01,43.9489,-67.04,-78.04,-19.79,11.21,3.6, 08,  511")
        self._other_names = ['Atirsagne']

Atirsagne = OmicronTauri


class TauTauri(FixedStar): # ,tauTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauTau", context=context, swe_string="Tau Tauri,tauTau,ICRS,04,42,14.70161,+22,57,24.9214,-2.89,-21.86,14.6,8.19,4.258, 22,  739")
        self._other_names = []

 = TauTauri


class RhoTauri(FixedStar): # ,rhoTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoTau", context=context, swe_string="Rho Tauri,rhoTau,ICRS,04,33,50.91753,+14,50,39.9232,103.2,-26.48,33.3,20.61,4.65, 14,  720")
        self._other_names = []

 = RhoTauri


class OmegaTauri01(FixedStar): # ,ome01Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ome01Tau", context=context, swe_string="Omega Tauri 01,ome01Tau,ICRS,04,09,09.96680,+19,36,33.1745,107.12,-32.32,24.83,11.49,5.504, 19,  672")
        self._other_names = []

 = OmegaTauri01


class Tauri16(FixedStar): # ,16Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",16Tau", context=context, swe_string="Tauri16,16Tau,ICRS,03,44,48.21518,+24,17,22.0851,20.38,-44.81,5.5,8.65,5.46, 23,  505")
        self._other_names = ['Celaeno']

Celaeno = Tauri16


class Tauri16(FixedStar): # ,16Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",16Tau", context=context, swe_string="Tauri16,16Tau,ICRS,03,44,48.21518,+24,17,22.0851,20.38,-44.81,5.5,8.65,5.46, 23,  505")
        self._other_names = ['Celeano']

Celeano = Tauri16


class Tauri17(FixedStar): # ,17Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",17Tau", context=context, swe_string="Tauri17,17Tau,ICRS,03,44,52.53688,+24,06,48.0112,20.84,-46.06,6.7,8.06,3.7, 23,  507")
        self._other_names = ['Electra']

Electra = Tauri17


class Tauri19(FixedStar): # ,19Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",19Tau", context=context, swe_string="Tauri19,19Tau,ICRS,03,45,12.49578,+24,28,02.2097,21.24,-40.56,7.8,7.97,4.3, 24,  547")
        self._other_names = ['Taygeta']

Taygeta = Tauri19


class Tauri20(FixedStar): # ,20Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",20Tau", context=context, swe_string="Tauri20,20Tau,ICRS,03,45,49.60656,+24,22,03.8864,20.95,-45.98,7.4,8.51,3.87, 23,  516")
        self._other_names = ['Maia']

Maia = Tauri20


class Tauri21(FixedStar): # ,21Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",21Tau", context=context, swe_string="Tauri21,21Tau,ICRS,03,45,54.4768,+24,33,16.235,20.025,-45.949,6,8.77,5.76, 24,  553")
        self._other_names = ['Asterope']

Asterope = Tauri21


class Tauri21(FixedStar): # ,21Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",21Tau", context=context, swe_string="Tauri21,21Tau,ICRS,03,45,54.4768,+24,33,16.235,20.025,-45.949,6,8.77,5.76, 24,  553")
        self._other_names = ['Sterope I']

SteropeI = Tauri21


class Tauri22(FixedStar): # ,22Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",22Tau", context=context, swe_string="Tauri22,22Tau,ICRS,03,46,02.9003,+24,31,40.429,19.629,-44.876,6.9,8.58,6.421, 24,  556")
        self._other_names = ['Sterope II']

SteropeII = Tauri22


class Tauri23(FixedStar): # ,23Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",23Tau", context=context, swe_string="Tauri23,23Tau,ICRS,03,46,19.57384,+23,56,54.0812,21.13,-43.65,6.2,8.58,4.18, 23,  522")
        self._other_names = ['Merope']

Merope = Tauri23


class Tauri27(FixedStar): # ,27Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",27Tau", context=context, swe_string="Tauri27,27Tau,ICRS,03,49,09.74258,+24,03,12.3003,17.7,-44.18,8.5,8.53,3.63, 23,  557")
        self._other_names = ['Atlas']

Atlas = Tauri27


class Tauri28(FixedStar): # ,28Tau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",28Tau", context=context, swe_string="Tauri28,28Tau,ICRS,03,49,11.21575,+24,08,12.1590,18.07,-47.2,5.1,8.54,5.09, 0,  0")
        self._other_names = ['Pleione']

Pleione = Tauri28


class AlphaTelescopium(FixedStar): # ,alfTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTel", context=context, swe_string="Alpha Telescopium,alfTel,ICRS,18,26,58.41604,-45,58,06.4498,-16.95,-53.09,-0.2,11.74,3.463,-46,12379")
        self._other_names = []

 = AlphaTelescopium


class EpsilonTelescopium(FixedStar): # ,epsTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsTel", context=context, swe_string="Epsilon Telescopium,epsTel,ICRS,18,11,13.76324,-45,57,15.9029,-15.46,-37.16,-26.3,7.8,4.508,-45,12251")
        self._other_names = []

 = EpsilonTelescopium


class ZetaTelescopium(FixedStar): # ,zetTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetTel", context=context, swe_string="Zeta Telescopium,zetTel,ICRS,18,28,49.85980,-49,04,14.1122,139.1,-228.66,-30.6,25.84,4.13,0,0")
        self._other_names = []

 = ZetaTelescopium


class IotaTelescopium(FixedStar): # ,iotTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotTel", context=context, swe_string="Iota Telescopium,iotTel,ICRS,19,35,12.98725,-48,05,57.1241,-7.51,-37.19,22.3,8.8,4.879,-48,13161")
        self._other_names = []

 = IotaTelescopium


class LambdaTelescopium(FixedStar): # ,lamTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamTel", context=context, swe_string="Lambda Telescopium,lamTel,ICRS,18,58,27.76710,-52,56,19.0622,12.18,-8.76,-2,5.33,4.838,-53, 9402")
        self._other_names = []

 = LambdaTelescopium


class NuTelescopium(FixedStar): # ,nu.Tel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Tel", context=context, swe_string="Nu Telescopium,nu.Tel,ICRS,19,48,01.19882,-56,21,45.3958,92.25,-136.72,-12.4,20.18,5.33,-56, 9290")
        self._other_names = []

 = NuTelescopium


class XiTelescopium(FixedStar): # ,ksiTel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiTel", context=context, swe_string="Xi Telescopium,ksiTel,ICRS,20,07,23.15599,-52,52,50.8490,-12.98,7.5,36,3.02,4.94,-53, 9794")
        self._other_names = []

 = XiTelescopium


class AlphaTrianguliAustralis(FixedStar): # ,alfTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTrA", context=context, swe_string="Alpha Trianguli Australis,alfTrA,ICRS,16,48,39.89508,-69,01,39.7626,17.99,-31.58,-3,8.35,1.92,-68, 2822")
        self._other_names = ['Atria']

Atria = AlphaTrianguliAustralis


class BetaTrianguliAustralis(FixedStar): # ,betTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betTrA", context=context, swe_string="Beta Trianguli Australis,betTrA,ICRS,15,55,08.56206,-63,25,50.6155,-188.66,-401.85,0.4,80.79,2.85,-63, 3723")
        self._other_names = []

 = BetaTrianguliAustralis


class GammaTrianguliAustralis(FixedStar): # ,gamTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamTrA", context=context, swe_string="Gamma Trianguli Australis,gamTrA,ICRS,15,18,54.58198,-68,40,46.3654,-66.58,-32.31,-3.6,17.74,2.89,-68, 2383")
        self._other_names = []

 = GammaTrianguliAustralis


class DeltaTrianguliAustralis(FixedStar): # ,delTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delTrA", context=context, swe_string="Delta Trianguli Australis,delTrA,ICRS,16,15,26.26979,-63,41,08.4492,2.73,-12.92,-4.9,5.37,3.839,-63, 3854")
        self._other_names = []

 = DeltaTrianguliAustralis


class EpsilonTrianguliAustralis(FixedStar): # ,epsTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsTrA", context=context, swe_string="Epsilon Trianguli Australis,epsTrA,ICRS,15,36,43.22223,-66,19,01.3334,24.35,-54.47,-15.5,16.17,4.104,-65, 3102")
        self._other_names = []

 = EpsilonTrianguliAustralis


class ZetaTrianguliAustralis(FixedStar): # ,zetTrA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetTrA", context=context, swe_string="Zeta Trianguli Australis,zetTrA,ICRS,16,28,28.1441,-70,05,03.845,200.222,110.64,8.3,82.53,4.91,-69, 2558")
        self._other_names = []

 = ZetaTrianguliAustralis


class GA(FixedStar): # ,GA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GA", context=context, swe_string="GA,GA,2000,16,15,02.836,-60,53,22.54,0.000,   0.00,  0.0,0.0000159,999.99,  0,    0")
        self._other_names = ['Great Attractor']

GreatAttractor = GA


class AlphaTrianguli(FixedStar): # ,alfTri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTri", context=context, swe_string="Alpha Trianguli,alfTri,ICRS,01,53,04.90710,+29,34,43.7801,10.82,-234.24,-12.6,51.5,3.42, 28,  312")
        self._other_names = ['Ras Mutallah']

RasMutallah = AlphaTrianguli


class AlphaTrianguli(FixedStar): # ,alfTri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTri", context=context, swe_string="Alpha Trianguli,alfTri,ICRS,01,53,04.90710,+29,34,43.7801,10.82,-234.24,-12.6,51.5,3.42, 28,  312")
        self._other_names = ['Metallah']

Metallah = AlphaTrianguli


class AlphaTrianguli(FixedStar): # ,alfTri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTri", context=context, swe_string="Alpha Trianguli,alfTri,ICRS,01,53,04.90710,+29,34,43.7801,10.82,-234.24,-12.6,51.5,3.42, 28,  312")
        self._other_names = ['Mothallah']

Mothallah = AlphaTrianguli


class BetaTrianguli(FixedStar): # ,betTri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betTri", context=context, swe_string="Beta Trianguli,betTri,ICRS,02,09,32.62712,+34,59,14.2694,149.16,-39.1,12.3,25.71,3, 34,  381")
        self._other_names = []

 = BetaTrianguli


class GammaTrianguli(FixedStar): # ,gamTri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamTri", context=context, swe_string="Gamma Trianguli,gamTri,ICRS,02,17,18.86703,+33,50,49.8950,44.64,-52.57,9.9,29.04,4, 33,  397")
        self._other_names = []

 = GammaTrianguli


class AlphaTucanae(FixedStar): # ,alfTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTuc", context=context, swe_string="Alpha Tucanae,alfTuc,ICRS,22,18,30.09478,-60,15,34.5263,-70.72,-39.44,42.2,16.33,2.82,-60, 7561")
        self._other_names = []

 = AlphaTucanae


class BetaTucanae02(FixedStar): # ,bet02Tuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",bet02Tuc", context=context, swe_string="Beta Tucanae 02,bet02Tuc,ICRS,00,31,33.47660,-62,57,56.0254,93.97,-46.32,9.8,19.36,4.514,0,0")
        self._other_names = []

 = BetaTucanae02


class GammaTucanae(FixedStar): # ,gamTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamTuc", context=context, swe_string="Gamma Tucanae,gamTuc,ICRS,23,17,25.77222,-58,14,08.6287,-35.83,81.16,18.4,43.37,3.98,-58, 8062")
        self._other_names = []

 = GammaTucanae


class EpsilonTucanae(FixedStar): # ,epsTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsTuc", context=context, swe_string="Epsilon Tucanae,epsTuc,ICRS,23,59,54.97761,-65,34,37.6804,47.93,-22.95,8.8,8.74,4.47,-66, 3819")
        self._other_names = []

 = EpsilonTucanae


class ZetaTucanae(FixedStar): # ,zetTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetTuc", context=context, swe_string="Zeta Tucanae,zetTuc,ICRS,00,20,04.25995,-64,52,29.2549,1707.42,1164.3,8.8,116.46,4.23,-65,   13")
        self._other_names = []

 = ZetaTucanae


class IotaTucanae(FixedStar): # ,iotTuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotTuc", context=context, swe_string="Iota Tucanae,iotTuc,ICRS,01,07,18.66365,-61,46,31.0434,73.8,-11.55,-7.8,10.72,5.342,-62,   89")
        self._other_names = []

 = IotaTucanae


class LambdaTucanae02(FixedStar): # ,lam02Tuc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lam02Tuc", context=context, swe_string="Lambda Tucanae 02,lam02Tuc,ICRS,00,55,00.31170,-69,31,37.5057,7.37,-43.69,5.1,14.7,5.454,-70,   40")
        self._other_names = []

 = LambdaTucanae02


class AlphaUrsaeMajoris(FixedStar): # ,alfUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfUMa", context=context, swe_string="Alpha Ursae Majoris,alfUMa,ICRS,11,03,43.67152,+61,45,03.7249,-134.11,-34.7,-9.4,26.54,1.79, 62, 1161")
        self._other_names = ['Dubhe']

Dubhe = AlphaUrsaeMajoris


class AlphaUrsaeMajoris(FixedStar): # ,alfUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfUMa", context=context, swe_string="Alpha Ursae Majoris,alfUMa,ICRS,11,03,43.67152,+61,45,03.7249,-134.11,-34.7,-9.4,26.54,1.79, 62, 1161")
        self._other_names = ['Kratu']

Kratu = AlphaUrsaeMajoris


class BetaUrsaeMajoris(FixedStar): # ,betUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betUMa", context=context, swe_string="Beta Ursae Majoris,betUMa,ICRS,11,01,50.47654,+56,22,56.7339,81.43,33.49,-13.1,40.9,2.37, 57, 1302")
        self._other_names = ['Merak']

Merak = BetaUrsaeMajoris


class BetaUrsaeMajoris(FixedStar): # ,betUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betUMa", context=context, swe_string="Beta Ursae Majoris,betUMa,ICRS,11,01,50.47654,+56,22,56.7339,81.43,33.49,-13.1,40.9,2.37, 57, 1302")
        self._other_names = ['Pulaha']

Pulaha = BetaUrsaeMajoris


class GammaUrsaeMajoris(FixedStar): # ,gamUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamUMa", context=context, swe_string="Gamma Ursae Majoris,gamUMa,ICRS,11,53,49.84732,+53,41,41.1350,107.68,11.01,-11.9,39.21,2.44, 54, 1475")
        self._other_names = ['Phecda']

Phecda = GammaUrsaeMajoris


class GammaUrsaeMajoris(FixedStar): # ,gamUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamUMa", context=context, swe_string="Gamma Ursae Majoris,gamUMa,ICRS,11,53,49.84732,+53,41,41.1350,107.68,11.01,-11.9,39.21,2.44, 54, 1475")
        self._other_names = ['Pulastya']

Pulastya = GammaUrsaeMajoris


class DeltaUrsaeMajoris(FixedStar): # ,delUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delUMa", context=context, swe_string="Delta Ursae Majoris,delUMa,ICRS,12,15,25.56063,+57,01,57.4156,104.11,7.3,-15.3,40.51,3.32, 57, 1363")
        self._other_names = ['Megrez']

Megrez = DeltaUrsaeMajoris


class DeltaUrsaeMajoris(FixedStar): # ,delUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delUMa", context=context, swe_string="Delta Ursae Majoris,delUMa,ICRS,12,15,25.56063,+57,01,57.4156,104.11,7.3,-15.3,40.51,3.32, 57, 1363")
        self._other_names = ['Atri']

Atri = DeltaUrsaeMajoris


class EpsilonUrsaeMajoris(FixedStar): # ,epsUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsUMa", context=context, swe_string="Epsilon Ursae Majoris,epsUMa,ICRS,12,54,01.74959,+55,57,35.3627,111.91,-8.24,-12.7,39.51,1.77, 56, 1627")
        self._other_names = ['Alioth']

Alioth = EpsilonUrsaeMajoris


class EpsilonUrsaeMajoris(FixedStar): # ,epsUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsUMa", context=context, swe_string="Epsilon Ursae Majoris,epsUMa,ICRS,12,54,01.74959,+55,57,35.3627,111.91,-8.24,-12.7,39.51,1.77, 56, 1627")
        self._other_names = ['Angiras']

Angiras = EpsilonUrsaeMajoris


class ZetaUrsaeMajoris(FixedStar): # ,zetUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetUMa", context=context, swe_string="Zeta Ursae Majoris,zetUMa,ICRS,13,23,55.54048,+54,55,31.2671,119.01,-25.97,-6.31,38.01,2.27, 55, 1598")
        self._other_names = ['Mizar']

Mizar = ZetaUrsaeMajoris


class ZetaUrsaeMajoris(FixedStar): # ,zetUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetUMa", context=context, swe_string="Zeta Ursae Majoris,zetUMa,ICRS,13,23,55.5429 ,+54,55,31.302, 121.23,-22.01,-5.6, 41.73,2.27, 55, 1598")
        self._other_names = ['Miz0']

Miz0 = ZetaUrsaeMajoris


class ZetaUrsaeMajoris(FixedStar): # ,zetUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetUMa", context=context, swe_string="Zeta Ursae Majoris,zetUMa,ICRS,13,23,55.54048,+54,55,31.2671,119.01,-25.97,-6.31,38.01,2.27, 55, 1598")
        self._other_names = ['Vasishtha']

Vasishtha = ZetaUrsaeMajoris


class EtaUrsaeMajoris(FixedStar): # ,etaUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaUMa", context=context, swe_string="Eta Ursae Majoris,etaUMa,ICRS,13,47,32.43776,+49,18,47.7602,-121.17,-14.91,-13.4,31.38,1.86, 50, 2027")
        self._other_names = ['Alkaid']

Alkaid = EtaUrsaeMajoris


class EtaUrsaeMajoris(FixedStar): # ,etaUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaUMa", context=context, swe_string="Eta Ursae Majoris,etaUMa,ICRS,13,47,32.43776,+49,18,47.7602,-121.17,-14.91,-13.4,31.38,1.86, 50, 2027")
        self._other_names = ['Benetnash']

Benetnash = EtaUrsaeMajoris


class EtaUrsaeMajoris(FixedStar): # ,etaUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaUMa", context=context, swe_string="Eta Ursae Majoris,etaUMa,ICRS,13,47,32.43776,+49,18,47.7602,-121.17,-14.91,-13.4,31.38,1.86, 50, 2027")
        self._other_names = ['Marichi']

Marichi = EtaUrsaeMajoris


class ThetaUrsaeMajoris(FixedStar): # ,tetUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetUMa", context=context, swe_string="Theta Ursae Majoris,tetUMa,ICRS,09,32,51.43390,+51,40,38.2811,-947.46,-535.6,14.4,74.19,3.18, 52, 1401")
        self._other_names = ['Al Haud']

AlHaud = ThetaUrsaeMajoris


class IotaUrsaeMajoris(FixedStar): # ,iotUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotUMa", context=context, swe_string="Iota Ursae Majoris,iotUMa,ICRS,08,59,12.45362,+48,02,30.5741,-441.29,-215.32,9,68.92,3.14, 48, 1707")
        self._other_names = ['Talitha']

Talitha = IotaUrsaeMajoris


class IotaUrsaeMajoris(FixedStar): # ,iotUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotUMa", context=context, swe_string="Iota Ursae Majoris,iotUMa,ICRS,08,59,12.45362,+48,02,30.5741,-441.29,-215.32,9,68.92,3.14, 48, 1707")
        self._other_names = ['Talitha Borealis']

TalithaBorealis = IotaUrsaeMajoris


class KappaUrsaeMajoris(FixedStar): # ,kapUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapUMa", context=context, swe_string="Kappa Ursae Majoris,kapUMa,ICRS,09,03,37.52762,+47,09,23.4890,-36.19,-55.4,2.3,9.1,3.55, 47, 1633")
        self._other_names = ['Talitha Australis']

TalithaAustralis = KappaUrsaeMajoris


class KappaUrsaeMajoris(FixedStar): # ,kapUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapUMa", context=context, swe_string="Kappa Ursae Majoris,kapUMa,ICRS,09,03,37.52762,+47,09,23.4890,-36.19,-55.4,2.3,9.1,3.55, 47, 1633")
        self._other_names = ['Alkaphrah']

Alkaphrah = KappaUrsaeMajoris


class LambdaUrsaeMajoris(FixedStar): # ,lamUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamUMa", context=context, swe_string="Lambda Ursae Majoris,lamUMa,ICRS,10,17,05.78287,+42,54,51.6808,-180.65,-46.07,18.1,23.72,3.45, 43, 2005")
        self._other_names = ['Tania Borealis']

TaniaBorealis = LambdaUrsaeMajoris


class MessierObjectu.UMa(FixedStar): # ,mu.UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.UMa", context=context, swe_string="Messier Object u.UMa,mu.UMa,ICRS,10,22,19.73976,+41,29,58.2691,-81.47,35.34,-21.3,14.16,3.05, 42, 2115")
        self._other_names = ['Tania Australis']

TaniaAustralis = MessierObjectu.UMa


class NuUrsaeMajoris(FixedStar): # ,nu.UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.UMa", context=context, swe_string="Nu Ursae Majoris,nu.UMa,ICRS,11,18,28.73664,+33,05,39.5107,-26.84,28.69,-9.63,8.17,3.49, 33, 2098")
        self._other_names = ['Alula Borealis']

AlulaBorealis = NuUrsaeMajoris


class XiUrsaeMajoris(FixedStar): # ,ksiUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ksiUMa", context=context, swe_string="Xi Ursae Majoris,ksiUMa,ICRS,11,18,10.932,+31,31,45.44,-453.7,-591.4,-18.2,0,3.79, 32, 2132")
        self._other_names = ['Alula Australis']

AlulaAustralis = XiUrsaeMajoris


class OmicronUrsaeMajoris(FixedStar): # ,omiUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiUMa", context=context, swe_string="Omicron Ursae Majoris,omiUMa,ICRS,08,30,15.87064,+60,43,05.4115,-133.76,-107.45,19.8,18.21,3.42, 61, 1054")
        self._other_names = ['Muscida']

Muscida = OmicronUrsaeMajoris


class RhoUrsaeMajoris(FixedStar): # ,rhoUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoUMa", context=context, swe_string="Rho Ursae Majoris,rhoUMa,ICRS,09,02,32.69092,+67,37,46.6280,-22.83,18.13,4.75,10.37,4.76, 68,  551")
        self._other_names = []

 = RhoUrsaeMajoris


class UpsilonUrsaeMajoris(FixedStar): # ,upsUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",upsUMa", context=context, swe_string="Upsilon Ursae Majoris,upsUMa,ICRS,09,50,59.35700,+59,02,19.4486,-295.2,-151.73,27.3,28.06,3.81, 59, 1268")
        self._other_names = []

 = UpsilonUrsaeMajoris


class PhiUrsaeMajoris(FixedStar): # ,phiUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiUMa", context=context, swe_string="Phi Ursae Majoris,phiUMa,ICRS,09,52,06.35437,+54,03,51.5962,-6,19.16,-14.7,6.41,4.557,0,0")
        self._other_names = []

 = PhiUrsaeMajoris


class ChiUrsaeMajoris(FixedStar): # ,chiUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiUMa", context=context, swe_string="Chi Ursae Majoris,chiUMa,ICRS,11,46,03.01407,+47,46,45.8626,-138.29,28.57,-9.02,17.76,3.72, 48, 1966")
        self._other_names = ['El Kophrah']

ElKophrah = ChiUrsaeMajoris


class ChiUrsaeMajoris(FixedStar): # ,chiUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiUMa", context=context, swe_string="Chi Ursae Majoris,chiUMa,ICRS,11,46,03.01407,+47,46,45.8626,-138.29,28.57,-9.02,17.76,3.72, 48, 1966")
        self._other_names = ['Taiyangshou']

Taiyangshou = ChiUrsaeMajoris


class PsiUrsaeMajoris(FixedStar): # ,psiUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiUMa", context=context, swe_string="Psi Ursae Majoris,psiUMa,ICRS,11,09,39.80868,+44,29,54.5520,-62.02,-27.41,-3.39,22.57,3.01, 45, 1897")
        self._other_names = []

 = PsiUrsaeMajoris


class UrsaeMajoris23(FixedStar): # ,23UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",23UMa", context=context, swe_string="Ursae Majoris23,23UMa,ICRS,09,31,31.70873,+63,03,42.7013,107.99,27.15,-10.4,41.99,3.67,0,0")
        self._other_names = []

 = UrsaeMajoris23


class UrsaeMajoris26(FixedStar): # ,26UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",26UMa", context=context, swe_string="Ursae Majoris26,26UMa,ICRS,09,34,49.43259,+52,03,05.3165,-65.74,-37.32,22.2,12.44,4.463,0,0")
        self._other_names = []

 = UrsaeMajoris26


class UrsaeMajoris47(FixedStar): # ,47UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",47UMa", context=context, swe_string="Ursae Majoris47,47UMa,ICRS,10,59,27.97282,+40,25,48.9202,-317.01,54.64,11.45,71.11,5.04, 0,0")
        self._other_names = ['Chalawan']

Chalawan = UrsaeMajoris47


class UrsaeMajoris80(FixedStar): # ,80UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",80UMa", context=context, swe_string="Ursae Majoris80,80UMa,ICRS,13,25,13.53783,+54,59,16.6548,120.21,-16.04,-8.9,39.91,4.01, 55, 1603")
        self._other_names = ['Alcor']

Alcor = UrsaeMajoris80


class UrsaeMajoris80(FixedStar): # ,80UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",80UMa", context=context, swe_string="Ursae Majoris80,80UMa,ICRS,13,25,13.5379, +54,59,16.648, 120.35,-16.94,-8.9,40.19,4.010, 55, 1603")
        self._other_names = ['Alc0']

Alc0 = UrsaeMajoris80


class UrsaeMajoris80(FixedStar): # ,80UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",80UMa", context=context, swe_string="Ursae Majoris80,80UMa,ICRS,13,25,13.53783,+54,59,16.6548,120.21,-16.04,-8.9,39.91,4.01, 55, 1603")
        self._other_names = ['Arundhati']

Arundhati = UrsaeMajoris80


class UrsaeMajoris80(FixedStar): # ,80UMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",80UMa", context=context, swe_string="Ursae Majoris80,80UMa,ICRS,13,25,13.53783,+54,59,16.6548,120.21,-16.04,-8.9,39.91,4.01, 55, 1603")
        self._other_names = ['Saidak']

Saidak = UrsaeMajoris80


class BrightStarCatalogue3743(FixedStar): # ,HR3743

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HR3743", context=context, swe_string="Bright Star Catalogue 3743,HR3743,ICRS,09,28,39.98840,+45,36,05.3344,-7.5,-128.77,38.58,11.65,5.393, 0,0")
        self._other_names = ['Intercrus']

Intercrus = BrightStarCatalogue3743


class AlphaUrsaeMinoris(FixedStar): # ,alfUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfUMi", context=context, swe_string="Alpha Ursae Minoris,alfUMi,ICRS,02,31,49.09456,+89,15,50.7923,44.48,-11.85,-16.42,7.54,2.02, 88,    8")
        self._other_names = ['Polaris']

Polaris = AlphaUrsaeMinoris


class BetaUrsaeMinoris(FixedStar): # ,betUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betUMi", context=context, swe_string="Beta Ursae Minoris,betUMi,ICRS,14,50,42.32580,+74,09,19.8142,-32.61,11.42,16.96,24.91,2.08, 74,  595")
        self._other_names = ['Kochab']

Kochab = BetaUrsaeMinoris


class GammaUrsaeMinoris(FixedStar): # ,gamUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamUMi", context=context, swe_string="Gamma Ursae Minoris,gamUMi,ICRS,15,20,43.71604,+71,50,02.4596,-17.73,17.9,-3.9,6.7,3.002, 72,  679")
        self._other_names = ['Pherkad']

Pherkad = GammaUrsaeMinoris


class DeltaUrsaeMinoris(FixedStar): # ,delUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delUMi", context=context, swe_string="Delta Ursae Minoris,delUMi,ICRS,17,32,12.99671,+86,35,11.2584,10.17,53.97,-7.6,18.95,4.336, 86,  269")
        self._other_names = ['Yildun']

Yildun = DeltaUrsaeMinoris


class EpsilonUrsaeMinoris(FixedStar): # ,epsUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsUMi", context=context, swe_string="Epsilon Ursae Minoris,epsUMi,ICRS,16,45,58.24168,+82,02,14.1233,19.47,2.61,-10.57,10.73,4.212, 82,  498")
        self._other_names = ['Urodelus']

Urodelus = EpsilonUrsaeMinoris


class ZetaUrsaeMinoris(FixedStar): # ,zetUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetUMi", context=context, swe_string="Zeta Ursae Minoris,zetUMi,ICRS,15,44,03.51891,+77,47,40.1788,19.91,-1.99,-13.1,8.84,4.274, 78,  527")
        self._other_names = ['Alifa Al Farkadain']

AlifaAlFarkadain = ZetaUrsaeMinoris


class ZetaUrsaeMinoris(FixedStar): # ,zetUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetUMi", context=context, swe_string="Zeta Ursae Minoris,zetUMi,ICRS,15,44,03.51891,+77,47,40.1788,19.91,-1.99,-13.1,8.84,4.274, 78,  527")
        self._other_names = ['Farkadain']

Farkadain = ZetaUrsaeMinoris


class ZetaUrsaeMinoris(FixedStar): # ,zetUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetUMi", context=context, swe_string="Zeta Ursae Minoris,zetUMi,ICRS,15,44,03.51891,+77,47,40.1788,19.91,-1.99,-13.1,8.84,4.274, 78,  527")
        self._other_names = ['Pharkadain']

Pharkadain = ZetaUrsaeMinoris


class EtaUrsaeMinoris(FixedStar): # ,etaUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaUMi", context=context, swe_string="Eta Ursae Minoris,etaUMi,ICRS,16,17,30.28696,+75,45,19.1885,-90.3,257.66,-11,33.63,4.95,0,0")
        self._other_names = []

 = EtaUrsaeMinoris


class EtaUrsaeMinoris(FixedStar): # ,etaUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaUMi", context=context, swe_string="Eta Ursae Minoris,etaUMi,ICRS,16,17,30.28696,+75,45,19.1885,-90.3,257.66,-11,33.63,4.95, 76,  596")
        self._other_names = ['Anwar al Farkadain']

AnwaralFarkadain = EtaUrsaeMinoris


class LambdaUrsaeMinoris(FixedStar): # ,lamUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamUMi", context=context, swe_string="Lambda Ursae Minoris,lamUMi,ICRS,17,16,56.4202,+89,02,15.741,-24.167,-3.945,0.29,3.68,6.38, 88,  112")
        self._other_names = []

 = LambdaUrsaeMinoris


class UrsaeMinoris11(FixedStar): # ,11UMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",11UMi", context=context, swe_string="Ursae Minoris11,11UMi,ICRS,15,17,05.8892,+71,49,26.046,4.099,9.535,-17.87,8.19,5.015, 72,  678")
        self._other_names = ['Pherkad Minor']

PherkadMinor = UrsaeMinoris11


class GammaVelorum02(FixedStar): # ,gam02Vel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam02Vel", context=context, swe_string="Gamma Velorum 02,gam02Vel,ICRS,08,09,31.95013,-47,20,11.7108,-6.07,10.43,15,2.92,1.83,-46, 3847")
        self._other_names = ['Suhail al Muhlif']

SuhailalMuhlif = GammaVelorum02


class GammaVelorum02(FixedStar): # ,gam02Vel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam02Vel", context=context, swe_string="Gamma Velorum 02,gam02Vel,ICRS,08,09,31.95013,-47,20,11.7108,-6.07,10.43,15,2.92,1.83,-46, 3847")
        self._other_names = ['Regor']

Regor = GammaVelorum02


class DeltaVelorum(FixedStar): # ,delVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delVel", context=context, swe_string="Delta Velorum,delVel,ICRS,08,44,42.22658,-54,42,31.7493,28.99,-103.35,2.2,40.49,1.95,0, 0")
        self._other_names = ['Alsephina', 'HIP 42913']

Alsephina = DeltaVelorum
HIP42913 = DeltaVelorum


class DeltaVelorum01(FixedStar): # ,del01Vel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del01Vel", context=context, swe_string="Delta Velorum 01,del01Vel,ICRS,08,44,42.226383,-54,42,31.75567,28.8,-104.1,2.20,40.49,0")
        self._other_names = ['Delta1Velorum']

Delta1Velorum = DeltaVelorum01


class DeltaVelorum(FixedStar): # ,delVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delVel", context=context, swe_string="Delta Velorum,delVel,ICRS,08,44,42.22658,-54,42,31.7493,28.99,-103.35,2.2,40.49,1.95,0, 0")
        self._other_names = ['Koo She']

KooShe = DeltaVelorum


class KappaVelorum(FixedStar): # ,kapVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapVel", context=context, swe_string="Kappa Velorum,kapVel,ICRS,09,22,06.81761,-55,00,38.4017,-11.4,11.52,21.9,5.7,2.473,-54, 2219")
        self._other_names = ['Markeb']

Markeb = KappaVelorum


class LambdaVelorum(FixedStar): # ,lamVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamVel", context=context, swe_string="Lambda Velorum,lamVel,ICRS,09,07,59.75787,-43,25,57.3273,-24.01,13.52,17.6,5.99,2.21,-42, 4990")
        self._other_names = ['Alsuhail']

Alsuhail = LambdaVelorum


class LambdaVelorum(FixedStar): # ,lamVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamVel", context=context, swe_string="Lambda Velorum,lamVel,ICRS,09,07,59.75787,-43,25,57.3273,-24.01,13.52,17.6,5.99,2.21,-42, 4990")
        self._other_names = ['Suhail']

Suhail = LambdaVelorum


class MessierObjectu.Vel(FixedStar): # ,mu.Vel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Vel", context=context, swe_string="Messier Object u.Vel,mu.Vel,ICRS,10,46,46.17877,-49,25,12.9244,63.22,-54.21,6.2,27.84,2.69,0, 0")
        self._other_names = ['Peregrini']

Peregrini = MessierObjectu.Vel


class MessierObjectu.Vel(FixedStar): # ,mu.Vel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Vel", context=context, swe_string="Messier Object u.Vel,mu.Vel,ICRS,10,46,46.17877,-49,25,12.9244,63.22,-54.21,6.2,27.84,2.69,0, 0")
        self._other_names = ['Alherem']

Alherem = MessierObjectu.Vel


class OmicronVelorum(FixedStar): # ,omiVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiVel", context=context, swe_string="Omicron Velorum,omiVel,ICRS,08,40,17.58553,-52,55,18.8002,-24.42,34.44,16.1,6.61,3.63,-52, 1583")
        self._other_names = ['Xestus']

Xestus = OmicronVelorum


class PhiVelorum(FixedStar): # ,phiVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiVel", context=context, swe_string="Phi Velorum,phiVel,ICRS,09,56,51.74167,-54,34,04.0390,-13.08,3.55,13.9,2.05,3.45,-53, 3075")
        self._other_names = ['Tseen Ke']

TseenKe = PhiVelorum


class PsiVelorum(FixedStar): # ,psiVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiVel", context=context, swe_string="Psi Velorum,psiVel,ICRS,09,30,41.99958,-40,28,00.2616,-147.98,61.35,8.8,53.15,3.6,0,0")
        self._other_names = []

 = PsiVelorum


class dVel(FixedStar): # ,dVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",dVel", context=context, swe_string="dVel,dVel,ICRS,08,44,23.94754,-42,38,57.4007,-23.29,18.71,-2,14.25,4.046,0,0")
        self._other_names = []

 = dVel


class eVel(FixedStar): # ,eVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",eVel", context=context, swe_string="eVel,eVel,ICRS,08,37,38.63278,-42,59,20.6894,-10.75,9.66,19.3,1.79,4.14,0,0")
        self._other_names = []

 = eVel


class pVel(FixedStar): # ,pVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pVel", context=context, swe_string="pVel,pVel,ICRS,10,37,18.13995,-48,13,32.2349,-133.41,-1.82,21.2,37.26,3.84,0,0")
        self._other_names = []

 = pVel


class qVel(FixedStar): # ,qVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",qVel", context=context, swe_string="qVel,qVel,ICRS,10,14,44.15573,-42,07,18.9933,-150.09,49.44,7.4,32.18,3.85,0,0")
        self._other_names = []

 = qVel


class tVel(FixedStar): # ,tVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tVel", context=context, swe_string="tVel,tVel,ICRS,10,32,56.85985,-47,00,12.0737,-24.38,6.40,4.20,2.49,5.027,0,0")
        self._other_names = []

 = tVel


class AlphaVirginis(FixedStar): # ,alfVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfVir", context=context, swe_string="Alpha Virginis,alfVir,ICRS,13,25,11.57937,-11,09,40.7501,-42.35,-30.67,1,13.06,0.97,-10, 3672")
        self._other_names = ['Spica', 'HIP 65474']

Spica = AlphaVirginis
HIP65474 = AlphaVirginis


class AlphaVirginis(FixedStar): # ,alfVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfVir", context=context, swe_string="Alpha Virginis,alfVir,ICRS,13,25,11.57937,-11,09,40.7501,-42.35,-30.67,1,13.06,0.97,-10, 3672")
        self._other_names = ['Citra']

Citra = AlphaVirginis


class BetaVirginis(FixedStar): # ,betVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betVir", context=context, swe_string="Beta Virginis,betVir,ICRS,11,50,41.71824,+01,45,52.9910,740.23,-270.43,4.71,91.5,3.6, 02, 2489")
        self._other_names = ['Zavijava']

Zavijava = BetaVirginis


class BetaVirginis(FixedStar): # ,betVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betVir", context=context, swe_string="Beta Virginis,betVir,ICRS,11,50,41.71824,+01,45,52.9910,740.23,-270.43,4.71,91.5,3.6, 02, 2489")
        self._other_names = ['Alaraph']

Alaraph = BetaVirginis


class GammaVirginis(FixedStar): # ,gamVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamVir", context=context, swe_string="Gamma Virginis,gamVir,ICRS,12,41,39.64344,-01,26,57.7421,-614.76,61.34,-20.42,85.58,2.74,-00, 2601")
        self._other_names = ['Porrima']

Porrima = GammaVirginis


class DeltaVirginis(FixedStar): # ,delVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delVir", context=context, swe_string="Delta Virginis,delVir,ICRS,12,55,36.20861,+03,23,50.8932,-469.99,-52.83,-18.87,16.44,3.38, 04, 2669")
        self._other_names = ['Auva']

Auva = DeltaVirginis


class DeltaVirginis(FixedStar): # ,delVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delVir", context=context, swe_string="Delta Virginis,delVir,ICRS,12,55,36.20861,+03,23,50.8932,-469.99,-52.83,-18.87,16.44,3.38, 04, 2669")
        self._other_names = ['Mineluva']

Mineluva = DeltaVirginis


class EpsilonVirginis(FixedStar): # ,epsVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsVir", context=context, swe_string="Epsilon Virginis,epsVir,ICRS,13,02,10.59785,+10,57,32.9415,-273.8,19.96,-14.29,29.76,2.79, 11, 2529")
        self._other_names = ['Vindemiatrix']

Vindemiatrix = EpsilonVirginis


class ZetaVirginis(FixedStar): # ,zetVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetVir", context=context, swe_string="Zeta Virginis,zetVir,ICRS,13,34,41.745,-00,35,45.38,-280.48,49.05,-13.2,44.03,3.38, 00, 3076")
        self._other_names = ['Heze']

Heze = ZetaVirginis


class EtaVirginis(FixedStar): # ,etaVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaVir", context=context, swe_string="Eta Virginis,etaVir,ICRS,12,19,54.354,-00,40,00.46,-57.58,-25.19,5.24,12.29,3.9, 00, 2926")
        self._other_names = ['Zaniah']

Zaniah = EtaVirginis


class ThetaVirginis(FixedStar): # ,tetVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tetVir", context=context, swe_string="Theta Virginis,tetVir,ICRS,13,09,56.99067,-05,32,20.4185,-36.28,-31.22,-2.9,10.33,4.397,-04, 3430")
        self._other_names = []

 = ThetaVirginis


class IotaVirginis(FixedStar): # ,iotVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotVir", context=context, swe_string="Iota Virginis,iotVir,ICRS,14,16,00.86951,-06,00,01.9633,-26.31,-419.38,12.51,44.97,4.08,-05, 3843")
        self._other_names = ['Syrma']

Syrma = IotaVirginis


class KappaVirginis(FixedStar): # ,kapVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapVir", context=context, swe_string="Kappa Virginis,kapVir,ICRS,14,12,53.74538,-10,16,25.3340,7.25,139.88,-4.38,12.8,4.21,-09, 3878")
        self._other_names = ['Kang']

Kang = KappaVirginis


class LambdaVirginis(FixedStar): # ,lamVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamVir", context=context, swe_string="Lambda Virginis,lamVir,ICRS,14,19,06.59235,-13,22,15.9459,-15.91,28.92,-6.4,17.49,4.52,-12, 4018")
        self._other_names = ['Khambalia']

Khambalia = LambdaVirginis


class MessierObjectu.Vir(FixedStar): # ,mu.Vir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Vir", context=context, swe_string="Messier Object u.Vir,mu.Vir,ICRS,14,43,03.62282,-05,39,29.5327,103.28,-318.63,5.1,54.73,3.88,-05, 3936")
        self._other_names = ['Rijl al Awwa']

RijlalAwwa = MessierObjectu.Vir


class MessierObjectu.Vir(FixedStar): # ,mu.Vir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",mu.Vir", context=context, swe_string="Messier Object u.Vir,mu.Vir,ICRS,14,43,03.62282,-05,39,29.5327,103.28,-318.63,5.1,54.73,3.88,-05, 3936")
        self._other_names = ['Ril Alauva']

RilAlauva = MessierObjectu.Vir


class NuVirginis(FixedStar): # ,nu.Vir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nu.Vir", context=context, swe_string="Nu Virginis,nu.Vir,ICRS,11,45,51.55957,+06,31,45.7413,-18.96,-181.56,50.28,11.1,4.04, 07, 2479")
        self._other_names = []

 = NuVirginis


class OmicronVirginis(FixedStar): # ,omiVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiVir", context=context, swe_string="Omicron Virginis,omiVir,ICRS,12,05,12.54049,+08,43,58.7498,-218.69,57.76,-29.62,19.98,4.12, 09, 2583")
        self._other_names = []

 = OmicronVirginis


class PiVirginis(FixedStar): # ,pi.Vir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",pi.Vir", context=context, swe_string="Pi Virginis,pi.Vir,ICRS,12,00,52.39042,+06,36,51.5571,0.26,-30.1,-10.4,8.49,4.642, 07, 2502")
        self._other_names = []

 = PiVirginis


class RhoVirginis(FixedStar): # ,rhoVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",rhoVir", context=context, swe_string="Rho Virginis,rhoVir,ICRS,12,41,53.05658,+10,14,08.2548,82.67,-89.08,1.6,27.57,4.88, 11, 2485")
        self._other_names = []

 = RhoVirginis


class SigmaVirginis(FixedStar): # ,sigVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",sigVir", context=context, swe_string="Sigma Virginis,sigVir,ICRS,13,17,36.28327,+05,28,11.5221,-6.06,9.14,-28.26,4.83,4.8, 06, 2722")
        self._other_names = []

 = SigmaVirginis


class TauVirginis(FixedStar): # ,tauVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauVir", context=context, swe_string="Tau Virginis,tauVir,ICRS,14,01,38.79341,+01,32,40.3145,17.49,-21.27,-6.7,14.5,4.237, 02, 2761")
        self._other_names = []

 = TauVirginis


class PhiVirginis(FixedStar): # ,phiVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiVir", context=context, swe_string="Phi Virginis,phiVir,ICRS,14,28,12.13894,-02,13,40.6579,-139.53,-4.04,-9.88,27.58,4.844,-01, 2957")
        self._other_names = []

 = PhiVirginis


class ChiVirginis(FixedStar): # ,chiVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiVir", context=context, swe_string="Chi Virginis,chiVir,ICRS,12,39,14.76703,-07,59,44.0324,-77.13,-24.73,-18.11,11.11,4.643,-07, 3452")
        self._other_names = []

 = ChiVirginis


class PsiVirginis(FixedStar): # ,psiVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",psiVir", context=context, swe_string="Psi Virginis,psiVir,ICRS,12,54,21.16342,-09,32,20.3783,-18.08,-19.52,17.6,5.99,4.8,-08, 3449")
        self._other_names = []

 = PsiVirginis


class Virginis109(FixedStar): # ,109Vir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",109Vir", context=context, swe_string="Virginis109,109Vir,ICRS,14,46,14.92536,+01,53,34.3845,-114.03,-22.13,-6.1,24.25,3.73,0, 0")
        self._other_names = []

 = Virginis109


class PSRB1257+12(FixedStar): # ,PSRB1257+12

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",PSRB1257+12", context=context, swe_string="PSRB1257+12,PSRB1257+12,ICRS,13,00,03.1075,+12,40,55.155,46.44,-84.87,0,1.41,999.99, 0,0")
        self._other_names = ['Lich']

Lich = PSRB1257+12


class VirgoCluster(FixedStar): # ,VC

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",VC", context=context, swe_string="Virgo Cluster,VC,2000,12,26,32.1,12,43,24,0.000,   0.00,  0.0,0.0000,999.99,  0,    0")
        self._other_names = ['Virgo Cluster']

VirgoCluster = VirgoCluster


class MessierObject87(FixedStar): # ,M87

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M87", context=context, swe_string="Messier Object 87,M87,ICRS,12,30,49.4233823,12,23,28.0438581,-8.029,10.734,1256,0.000061,8.63,  0,    0")
        self._other_names = []



class MessierObject49(FixedStar): # ,M49

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",M49", context=context, swe_string="Messier Object 49,M49,ICRS,12,29,46.798,8,00,01.48,0.0,0.0,949,0.000000,12.17,  0,    0")
        self._other_names = []



class AlphaVolantis(FixedStar): # ,alfVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfVol", context=context, swe_string="Alpha Volantis,alfVol,ICRS,09,02,26.79592,-66,23,45.8727,-2,-95.51,7.6,26.11,3.99,-65, 1065")
        self._other_names = []

 = AlphaVolantis


class BetaVolantis(FixedStar): # ,betVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betVol", context=context, swe_string="Beta Volantis,betVol,ICRS,08,25,44.19472,-66,08,12.8050,-35.74,-152.22,27.4,30.33,3.759,-65,  933")
        self._other_names = []

 = BetaVolantis


class GammaVolantis02(FixedStar): # ,gam02Vol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gam02Vol", context=context, swe_string="Gamma Volantis 02,gam02Vol,ICRS,07,08,44.86718,-70,29,56.1620,24.29,107.03,2.8,23.33,3.746,-70,  600")
        self._other_names = []

 = GammaVolantis02


class DeltaVolantis(FixedStar): # ,delVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delVol", context=context, swe_string="Delta Volantis,delVol,ICRS,07,16,49.82387,-67,57,25.7484,-4.43,8.38,22.7,4.42,3.99,-67,  730")
        self._other_names = []

 = DeltaVolantis


class EpsilonVolantis(FixedStar): # ,epsVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsVol", context=context, swe_string="Epsilon Volantis,epsVol,ICRS,08,07,55.79420,-68,37,01.4350,-29.14,29.26,9,5.8,4.33,0,0")
        self._other_names = []

 = EpsilonVolantis


class ZetaVolantis(FixedStar): # ,zetVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetVol", context=context, swe_string="Zeta Volantis,zetVol,ICRS,07,41,49.26100,-72,36,21.9566,33.34,14.89,48.1,23.13,3.944,-72,  627")
        self._other_names = []

 = ZetaVolantis


class IotaVolantis(FixedStar): # ,iotVol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotVol", context=context, swe_string="Iota Volantis,iotVol,ICRS,06,51,26.98552,-70,57,48.2766,3.64,26.08,18.5,5.79,5.395,-70,  572")
        self._other_names = []

 = IotaVolantis


class AlphaVulpeculae(FixedStar): # ,alfVul

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfVul", context=context, swe_string="Alpha Vulpeculae,alfVul,ICRS,19,28,42.32996,+24,39,53.6525,-126.13,-107.44,-85.53,10.97,4.45, 24, 3759")
        self._other_names = ['Anser']

Anser = AlphaVulpeculae


class Vulpeculae2(FixedStar): # ,2Vul

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",2Vul", context=context, swe_string="Vulpeculae2,2Vul,ICRS,19,17,43.63655,+23,01,31.9524,2.04,-2.78,1,2.68,5.436,0,0")
        self._other_names = []

 = Vulpeculae2


class Vulpeculae12(FixedStar): # ,12Vul

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",12Vul", context=context, swe_string="Vulpeculae12,12Vul,ICRS,19,51,04.10821,+22,36,36.1732,23.02,-15.88,-24.9,5.18,4.96,0,0")
        self._other_names = []

 = Vulpeculae12


class GCLiu(FixedStar): # ,GCLiu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GCLiu", context=context, swe_string="GCLiu,GCLiu,ICRS,17,45,40.0400,-29,00,28.138,-2.755718425, -5.547,  0.0,0.125,999.99,  0,    0")
        self._other_names = ['GCLiu']

GCLiu = GCLiu


class GPol(FixedStar): # ,GPol

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GPol", context=context, swe_string="GPol,GPol,ICRS,12,51,36.7151981,27,06,11.193172,0.0,0.0,0.0,0.0,0.0,0,0")
        self._other_names = ['Gal.Pole']

Gal.Pole = GPol


class GP1958(FixedStar): # ,GP1958

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GP1958", context=context, swe_string="GP1958,GP1958,ICRS,12,51,26.27469,27,07,41.7087,0.0,0.0,0.0,0.0,0.0,0,0")
        self._other_names = ['Gal.Pole IAU1958']

Gal.PoleIAU1958 = GP1958


class GPPlan(FixedStar): # ,GPPlan

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GPPlan", context=context, swe_string="GPPlan,GPPlan,ICRS,12,51,5.731104,27,10,39.554849,0.0,0.0,0.0,0.0,0.0,0,0")
        self._other_names = ['Gal.Plane Pole']

Gal.PlanePole = GPPlan


class GEqu(FixedStar): # ,GEqu

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GEqu", context=context, swe_string="GEqu,GEqu,ICRS,18,0,19.90411,-23,26,21.3339,269.0,473.0,0.0,0.0,0.0,0,0")
        self._other_names = ['Gal.Equ']

Gal.Equ = GEqu


class IDrag(FixedStar): # ,IDrag

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",IDrag", context=context, swe_string="IDrag,IDrag, ICRS,13,48,0.0,-9,0,0.0,0,0,0,0,0.0, 19,  477")
        self._other_names = ['Infrared Dragon']

InfraredDragon = IDrag


class AA11(FixedStar): # ,AA11

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",AA11", context=context, swe_string="AA11,AA11,ICRS,14,39,36.4958,-60,50, 2.309,-3678.06,482.87,-21.6,742,0,0,0")
        self._other_names = ['AA11_page_B73']

AA11_page_B73 = AA11


class GCRS00(FixedStar): # ,GCRS00

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GCRS00", context=context, swe_string="GCRS00,GCRS00,ICRS,0,0,0.0,0,0, 0.0,0.0,  0.0, 0.0,0,0,0,0")
        self._other_names = ['GCRS00']

GCRS00 = GCRS00


class ZE200(FixedStar): # ,ZE200

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ZE200", context=context, swe_string="ZE200,ZE200,ICRS,0,0,0.0,+0,0,0.0,0,0,0,0,0.0,0,0")
        self._other_names = ['Zero2000']

Zero2000 = ZE200


class ZL200(FixedStar): # ,ZL200

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",ZL200", context=context, swe_string="ZL200,ZL200,ICRS,12,0,0.0,+0,0,0.0,0,0,0,0,0.0,0,0")
        self._other_names = ['ZerL2000']

ZerL2000 = ZL200


class SunPole(FixedStar): # ,SunPole

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",SunPole", context=context, swe_string="SunPole,SunPole,ICRS,19,4,31.2,63,52,12.0,0.0,0.0,0.0,0.0,0.0,0,0")
        self._other_names = ['Sun Pole']

SunPole = SunPole


class Test(FixedStar): # ,Test

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",Test", context=context, swe_string="Test,Test,ICRS,21,11,47.25986, 48,17,20.5855,0.0,0.0,0.0,0.0,0.0,0,0")
        self._other_names = ['Test']

Test = Test


class NewGeneralCatalogue4194(FixedStar): # ,NGC4194

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",NGC4194", context=context, swe_string="New General Catalogue 4194,NGC4194,ICRS,12,14,09.573,54,31,36.03,0.0,0.0,0.0,0.0,0.0,0,0")
        self._other_names = []



class HenryDraperCatalogue168442(FixedStar): # ,HD168442

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",HD168442", context=context, swe_string="Henry Draper Catalogue 168442,HD168442,ICRS,18,19,50.8412023907,-1,56,19.005321656,-0.460,-0.028,-13.8,52.5185,9.656,0,0")
        self._other_names = ['Gliese 710']

Gliese710 = HenryDraperCatalogue168442


class OmicronTauri(FixedStar): # ,omiTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",omiTau", context=context, swe_string="Omicron Tauri,omiTau,ICRS,03,24,48.79796,+09,01,43.9489,-67.04,-78.04,-19.79,11.21,3.6, 08,  511")
        self._other_names = ['Omicron Tauri']

OmicronTauri = OmicronTauri


class KappaGeminorum(FixedStar): # ,kapGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapGem", context=context, swe_string="Kappa Geminorum,kapGem,ICRS,07,44,26.8438122013,+24,23,52.787290890,-28.403,-50,675,20.15,22.0907,3.57")
        self._other_names = ['Kappa Geminorum']

KappaGeminorum = KappaGeminorum


class Geminorum1(FixedStar): # ,1Gem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",1Gem", context=context, swe_string="Geminorum1,1Gem,ICRS,06,04,07.25444,+23,15,48.0401,-1.61,-118.33,22.39,21.03,4.15")
        self._other_names = ['One Geminorum']

OneGeminorum = Geminorum1


class ChiCancri(FixedStar): # ,chiCnc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",chiCnc", context=context, swe_string="Chi Cancri,chiCnc,ICRS,08,20,03.8607602556,+27,13,03.738171893,-17.475,-377.072,32.629,54.8749,0")
        self._other_names = ['Chi Cancri']

ChiCancri = ChiCancri


class KappaLeonis(FixedStar): # ,kapLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapLeo", context=context, swe_string="Kappa Leonis,kapLeo,ICRS,09,24,39.2586717722,+26,10,56.367449863,-32.493,-47.421,27.81,16.3121,4.46")
        self._other_names = ['Kappa Leonis']

KappaLeonis = KappaLeonis


class NuVirginis(FixedStar): # ,nuVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",nuVir", context=context, swe_string="Nu Virginis,nuVir,ICRS,11,45,51.5595979999,+06,31,45.748996439,-21.086,-182.903,50.28,9.8446,4.04")
        self._other_names = ['Nu Virginis']

NuVirginis = NuVirginis


class Librae48(FixedStar): # ,48Lib

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",48Lib", context=context, swe_string="Librae48,48Lib,ICRS,15,58,11.3682502453,-14,16,45.681109093,-13.843,-16.271,-25.010,7.1540,4.87")
        self._other_names = ['48 Librae']

48Librae = Librae48


class TauScorpii(FixedStar): # ,tauSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",tauSco", context=context, swe_string="Tau Scorpii,tauSco,ICRS,16,35,52.9528530,-28,12,57.661515,-9.89,-22.83,-650.47,6.88,2.81")
        self._other_names = ['Tau Scorpii', 'Paikauhale']

TauScorpii = TauScorpii
Paikauhale = TauScorpii


class Ophiuci45(FixedStar): # ,45Oph

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",45Oph", context=context, swe_string="Ophiuci45,45Oph,ICRS,17,27,21.2756332194,-29,52,01.325368180,17.052,-137.966,37.70,29.1161,4.269")
        self._other_names = ['dOph', '45 Ophiuci']

dOph = Ophiuci45
45Ophiuci = Ophiuci45


class IotaAquarii(FixedStar): # ,iotAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotAqr", context=context, swe_string="Iota Aquarii,iotAqr,ICRS,22,06,26.2273404225,-13,52,10.850020077,42.210,-56.566,-11.95,15.4940,4.27")
        self._other_names = ['Iota Aquarii']

IotaAquarii = IotaAquarii


class PhiAquarii(FixedStar): # ,phiAqr

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",phiAqr", context=context, swe_string="Phi Aquarii,phiAqr,ICRS,23,14,19.3582404192,-06,02,56.423128812,36.575,-195.441,2.48,14.3482,4.22")
        self._other_names = ['Phi Aquarii']

PhiAquarii = PhiAquarii


class GammaPiscium(FixedStar): # ,gamPsc

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamPsc", context=context, swe_string="Gamma Piscium,gamPsc,ICRS,23,17,09.9371132484,+03,16,56.245688417,759.268,17.568,-14.48,24.1958,3.70")
        self._other_names = ['Gamma Piscium']

GammaPiscium = GammaPiscium


class GScorpii(FixedStar): # ,GSco

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",GSco", context=context, swe_string="G Scorpii,GSco,ICRS,17,49,51.4808976914,-37,02,35.794961894,41.717,11.975,24.70,24.7340,3.21")
        self._other_names = ['G Scorpii', 'Fuyue', 'HIP 87261']

GScorpii = GScorpii
Fuyue = GScorpii
HIP87261 = GScorpii


class BetaPersei(FixedStar): # ,betPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betPer", context=context, swe_string="Beta Persei,betPer,ICRS,03,08,10.1324535,+40,57,20.328013,2.99,-1.66,4.0,36.27,2.12")
        self._other_names = ['Beta Persus', 'Algol', 'HIP 14576']

BetaPersus = BetaPersei
Algol = BetaPersei
HIP14576 = BetaPersei


class AlphaPersei(FixedStar): # ,alfPer

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPer", context=context, swe_string="Alpha Persei,alfPer,ICRS,03,24,19.3700924,+49,51,40.245455,23.75,-26.23,-2.158,6.44,1.79")
        self._other_names = ['Alpha Perseus', 'Mirfak', 'no hip id']

AlphaPerseus = AlphaPersei
Mirfak = AlphaPersei
nohipid = AlphaPersei


class AlphaTauri(FixedStar): # ,alfTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfTau", context=context, swe_string="Alpha Tauri,alfTau,ICRS,04,35,55.23907,+16,30,33.4885,63.45,-188.94,54.398,48.94,0.86")
        self._other_names = ['Alpha Taurus', 'Aldebaran', 'HIP 21421']

AlphaTaurus = AlphaTauri
Aldebaran = AlphaTauri
HIP21421 = AlphaTauri


class BetaOrionis(FixedStar): # ,betOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betOri", context=context, swe_string="Beta Orionis,betOri,ICRS,05,14,32.27210,-08,12,05.8981,1.31,0.50,17.80,3.78,0.13")
        self._other_names = ['Beta Orion', 'Rigel', 'HIP 24436']

BetaOrion = BetaOrionis
Rigel = BetaOrionis
HIP24436 = BetaOrionis


class GammaOrionis(FixedStar): # ,gamOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamOri", context=context, swe_string="Gamma Orionis,gamOri,ICRS,05,25,07.86325,+06,20,58.9318,-8.11,-12.88,17.310,12.92,1.64")
        self._other_names = ['Gamma Orion', 'Bellatrix', 'HIP 25336']

GammaOrion = GammaOrionis
Bellatrix = GammaOrionis
HIP25336 = GammaOrionis


class AlphaAurigae(FixedStar): # ,alfAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfAur", context=context, swe_string="Alpha Aurigae,alfAur,ICRS,05,16,41.35871,+45,59,52.7693,75.25,-426.89,29.19,76.20,0.08")
        self._other_names = ['Alpha Auriga', 'Capella', 'HIP 24608']

AlphaAuriga = AlphaAurigae
Capella = AlphaAurigae
HIP24608 = AlphaAurigae


class DeltaOrionis(FixedStar): # ,delOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delOri", context=context, swe_string="Delta Orionis,delOri,ICRS,05,32,00.40009,-00,17,56.7424,0.64,-0.69,18.50,4.71,2.41")
        self._other_names = ['Delta Orion', 'Mintaka', 'HIP 25930']

DeltaOrion = DeltaOrionis
Mintaka = DeltaOrionis
HIP25930 = DeltaOrionis


class BetaTauri(FixedStar): # ,betTau

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betTau", context=context, swe_string="Beta Tauri,betTau,ICRS,05,26,17.51312,+28,36,26.8262,22.76,-173.58,9.2,24.36,1.65")
        self._other_names = ['Beta Taurus', 'Elnath', 'HIP 25428']

BetaTaurus = BetaTauri
Elnath = BetaTauri
HIP25428 = BetaTauri


class EpsilonOrionis(FixedStar): # ,epsOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsOri", context=context, swe_string="Epsilon Orionis,epsOri,ICRS,05,36,12.81335,-01,12,06.9089,1.44,-0.78,27.30,1.65,1.69")
        self._other_names = ['Epsilon Orion', 'Alnilam', 'HIP 26311']

EpsilonOrion = EpsilonOrionis
Alnilam = EpsilonOrionis
HIP26311 = EpsilonOrionis


class ZetaOrionis(FixedStar): # ,zetOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetOri", context=context, swe_string="Zeta Orionis,zetOri,ICRS,05,40,45.52666,-01,56,33.2649,3.19,2.03,18.50,4.43,1.77")
        self._other_names = ['Zeta Orion', 'Alnitak', 'HIP 26727']

ZetaOrion = ZetaOrionis
Alnitak = ZetaOrionis
HIP26727 = ZetaOrionis


class KappaOrionis(FixedStar): # ,kapOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapOri", context=context, swe_string="Kappa Orionis,kapOri,ICRS,05,47,45.3888404,-09,40,10.577707,1.46,-1.28,20.5,5.04,2.06")
        self._other_names = ['Kappa Orion', 'Saiph', 'HIP 27366']

KappaOrion = KappaOrionis
Saiph = KappaOrionis
HIP27366 = KappaOrionis


class AlphaUrsaeMinoris(FixedStar): # ,alfUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfUMi", context=context, swe_string="Alpha Ursae Minoris,alfUMi,ICRS,02,31,49.09456,+89,15,50.7923,44.48,-11.85,-16.42,7.54,2.02")
        self._other_names = ['Alpha Ursa Minor', 'North', 'HIP 11767']

AlphaUrsaMinor = AlphaUrsaeMinoris
North = AlphaUrsaeMinoris
HIP11767 = AlphaUrsaeMinoris


class AlphaOrionis(FixedStar): # ,alfOri

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfOri", context=context, swe_string="Alpha Orionis,alfOri,ICRS,05,55,10.30536,+07,24,25.4304,27.54,11.30,21.91,6.55,0.42")
        self._other_names = ['Alpha Orion', 'Betelgeuse', 'HIP 27989']

AlphaOrion = AlphaOrionis
Betelgeuse = AlphaOrionis
HIP27989 = AlphaOrionis


class BetaAurigae(FixedStar): # ,betAur

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betAur", context=context, swe_string="Beta Aurigae,betAur,ICRS,05,59,31.7229284,+44,56,50.757259,-56.44,-0.95,-15.75,40.21,1.90")
        self._other_names = ['Beta Auriga', 'Menkalinan', 'HIP 28360']

BetaAuriga = BetaAurigae
Menkalinan = BetaAurigae
HIP28360 = BetaAurigae


class BetaCanisMajoris(FixedStar): # ,betCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCMa", context=context, swe_string="Beta Canis Majoris,betCMa,ICRS,06,22,41.9853527,-17,57,21.307352,-3.23,-0.78,33.70,6.62,1.97")
        self._other_names = ['Beta Canis Major', 'Mirzam', 'HIP 30324']

BetaCanisMajor = BetaCanisMajoris
Mirzam = BetaCanisMajoris
HIP30324 = BetaCanisMajoris


class GammaGeminorum(FixedStar): # ,gamGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamGem", context=context, swe_string="Gamma Geminorum,gamGem,ICRS,06,37,42.71050,+16,23,57.4095,13.81,-54.96,-12.63,29.84,1.92")
        self._other_names = ['Gamma Gemini', 'Alhena', 'HIP 31681']

GammaGemini = GammaGeminorum
Alhena = GammaGeminorum
HIP31681 = GammaGeminorum


class AlphaCanisMajoris(FixedStar): # ,alfCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCMa", context=context, swe_string="Alpha Canis Majoris,alfCMa,ICRS,06,45,08.91728,-16,42,58.0171,-546.01,-1223.07,-5.50,379.21,-1.46")
        self._other_names = ['Alpha Canis Major', 'Sirius', 'HIP 32349']

AlphaCanisMajor = AlphaCanisMajoris
Sirius = AlphaCanisMajoris
HIP32349 = AlphaCanisMajoris


class AlphaCarinae(FixedStar): # ,alfCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCar", context=context, swe_string="Alpha Carinae,alfCar,ICRS,06,23,57.10988,-52,41,44.3810,19.93,23.24,20.30,10.55,-0.74")
        self._other_names = ['Alpha Carina', 'Canopus', 'HIP 30438']

AlphaCarina = AlphaCarinae
Canopus = AlphaCarinae
HIP30438 = AlphaCarinae


class AlphaPiscisAustrini(FixedStar): # ,alfPsA

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfPsA", context=context, swe_string="Alpha Piscis Austrini,alfPsA,ICRS,22,57,39.04625,-29,37,20.0533,328.95,-164.67,6.50,129.81,1.16")
        self._other_names = ['Alpha Piscis Austrini', 'Fomalhaut', 'HIP 113368']

AlphaPiscisAustrini = AlphaPiscisAustrini
Fomalhaut = AlphaPiscisAustrini
HIP113368 = AlphaPiscisAustrini


class AlphaGeminorum(FixedStar): # ,alfGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfGem", context=context, swe_string="Alpha Geminorum,alfGem,ICRS,07,34,35.87319,+31,53,17.8160,-191.45,-145.19,-11.230,64.12,1.58")
        self._other_names = ['Castor', 'HIP 36850']

Castor = AlphaGeminorum
HIP36850 = AlphaGeminorum


class EpsilonCanisMajoris(FixedStar): # ,epsCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCMa", context=context, swe_string="Epsilon Canis Majoris,epsCMa,ICRS,06,58,37.54876,-28,58,19.5102,3.24,1.33,27.30,8.05,1.50")
        self._other_names = ['Adhara', 'HIP 33579']

Adhara = EpsilonCanisMajoris
HIP33579 = EpsilonCanisMajoris


class BetaGeminorum(FixedStar): # ,betGem

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betGem", context=context, swe_string="Beta Geminorum,betGem,ICRS,07,45,18.94987,+28,01,34.3160,-626.55,-45.80,3.391,96.54,1.14")
        self._other_names = ['Pollux', 'HIP 37826']

Pollux = BetaGeminorum
HIP37826 = BetaGeminorum


class DeltaCanisMajoris(FixedStar): # ,delCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCMa", context=context, swe_string="Delta Canis Majoris,delCMa,ICRS,07,08,23.4840514,-26,23,35.518484,-3.12,3.31,33.67,2.03,1.84")
        self._other_names = ['Wezen', 'HIP 34444']

Wezen = DeltaCanisMajoris
HIP34444 = DeltaCanisMajoris


class AlphaCanisMinors(FixedStar): # ,alfCMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfCMi", context=context, swe_string="Alpha Canis Minors,alfCMi,ICRS,07,39,18.11950,+05,13,29.9552,-714.59,-1036.80,-4.505280,284.56,0.37")
        self._other_names = ['Procyon', 'HIP 37279']

Procyon = AlphaCanisMinors
HIP37279 = AlphaCanisMinors


class EtaCanisMajoris(FixedStar): # ,etaCMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaCMa", context=context, swe_string="Eta Canis Majoris,etaCMa,ICRS,07,24,05.70228,-29,18,11.1798,-4.14,5.81,41.1,1.64,2.45")
        self._other_names = ['Aludra', 'HIP 35904']

Aludra = EtaCanisMajoris
HIP35904 = EtaCanisMajoris


class BetaUrsaeMinoris(FixedStar): # ,betUMi

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betUMi", context=context, swe_string="Beta Ursae Minoris,betUMi,ICRS,14,50,42.32580,+74,09,19.8142,-32.61,11.42,16.96,24.91,2.08")
        self._other_names = ['Kochab', 'HIP 72607']

Kochab = BetaUrsaeMinoris
HIP72607 = BetaUrsaeMinoris


class AlphaUrsaeMajoris(FixedStar): # ,alfUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfUMa", context=context, swe_string="Alpha Ursae Majoris,alfUMa,ICRS,11,03,43.67152,+61,45,03.7249,-134.11,-34.70,-9.40,26.54,1.79")
        self._other_names = ['Dubhe', 'HIP 54061']

Dubhe = AlphaUrsaeMajoris
HIP54061 = AlphaUrsaeMajoris


class ZetaPuppis(FixedStar): # ,zetPup

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetPup", context=context, swe_string="Zeta Puppis,zetPup,ICRS,08,03,35.04754,-40,00,11.3321,-29.71,16.68,-23.90,3.01,2.25")
        self._other_names = ['Naos', 'HIP 39429']

Naos = ZetaPuppis
HIP39429 = ZetaPuppis


class BetaUrsaeMajoris(FixedStar): # ,betUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betUMa", context=context, swe_string="Beta Ursae Majoris,betUMa,ICRS,11,01,50.4797515135,+56,22,56.761138187,79.959,32.365,-13.10,38.6031,2.37")
        self._other_names = ['Merak', 'HIP 53910']

Merak = BetaUrsaeMajoris
HIP53910 = BetaUrsaeMajoris


class AlphaHydrae(FixedStar): # ,alfHya

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfHya", context=context, swe_string="Alpha Hydrae,alfHya,ICRS,09,27,35.24270,-08,39,30.9583,-15.23,34.37,-4.561,18.09,1.97")
        self._other_names = ['Alphard', 'HIP 46390']

Alphard = AlphaHydrae
HIP46390 = AlphaHydrae


class GammaLeonis(FixedStar): # ,gamLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamLeo", context=context, swe_string="Gamma Leonis,gamLeo,ICRS,10,19,58.35056,+19,50,29.3468,304.30,-154.28,-36.24,25.07,0")
        self._other_names = ['Algieba', 'no hip id']

Algieba = GammaLeonis
nohipid = GammaLeonis


class AlphaLeonis(FixedStar): # ,alfLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfLeo", context=context, swe_string="Alpha Leonis,alfLeo,ICRS,10,08,22.31099,+11,58,01.9516,-248.73,5.59,0.719522,41.13,1.40")
        self._other_names = ['Regulus', 'HIP 49669']

Regulus = AlphaLeonis
HIP49669 = AlphaLeonis


class GammaUrsaeMajoris(FixedStar): # ,gamUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamUMa", context=context, swe_string="Gamma Ursae Majoris,gamUMa,ICRS,11,53,49.8473166,+53,41,41.135025,107.68,11.01,-11.90,39.21,2.440")
        self._other_names = ['Phecda', 'HIP 58001']

Phecda = GammaUrsaeMajoris
HIP58001 = GammaUrsaeMajoris


class EpsilonUrsaeMajoris(FixedStar): # ,epsUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsUMa", context=context, swe_string="Epsilon Ursae Majoris,epsUMa,ICRS,12,54,01.7495922,+55,57,35.362645,111.91,-8.24,-12.70,39.51,1.77")
        self._other_names = ['Alioth', 'HIP 62956']

Alioth = EpsilonUrsaeMajoris
HIP62956 = EpsilonUrsaeMajoris


class LambdaVelorum(FixedStar): # ,lamVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",lamVel", context=context, swe_string="Lambda Velorum,lamVel,ICRS,09,07,59.75787,-43,25,57.3273,-24.01,13.52,17.60,5.99,2.21")
        self._other_names = ['Suhail', 'HIP 44816']

Suhail = LambdaVelorum
HIP44816 = LambdaVelorum


class DeltaLeonis(FixedStar): # ,delLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delLeo", context=context, swe_string="Delta Leonis,delLeo,ICRS,11,14,06.50142,+20,31,25.3853,143.42,-129.88,-20.90,55.82,2.53")
        self._other_names = ['Zosma', 'HIP 54872']

Zosma = DeltaLeonis
HIP54872 = DeltaLeonis


class ZetaUrsaeMajoris(FixedStar): # ,zetUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",zetUMa", context=context, swe_string="Zeta Ursae Majoris,zetUMa,ICRS,13,23,55.54048,+54,55,31.2671,119.01,-25.97,-6.31,38.01,0")
        self._other_names = ['Mizar', 'no hip id']

Mizar = ZetaUrsaeMajoris
nohipid = ZetaUrsaeMajoris


class DeltaVelorum01(FixedStar): # ,del01Vel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",del01Vel", context=context, swe_string="Delta Velorum 01,del01Vel,ICRS,08,44,42.226383,-54,42,31.75567,28.8,-104.1,2.20,40.49,0")
        self._other_names = ['HIP 42913']

 = DeltaVelorum01
HIP42913 = DeltaVelorum01


class BetaLeonis(FixedStar): # ,betLeo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betLeo", context=context, swe_string="Beta Leonis,betLeo,ICRS,11,49,03.57834,+14,34,19.4090,-497.68,-114.67,-0.20,90.91,2.13")
        self._other_names = ['Denebola', 'HIP 57632']

Denebola = BetaLeonis
HIP57632 = BetaLeonis


class EpsilonCarinae(FixedStar): # ,epsCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsCar", context=context, swe_string="Epsilon Carinae,epsCar,ICRS,08,22,30.83526,-59,30,34.1431,-25.52,22.06,11.60,5.39,1.86")
        self._other_names = ['Avior', 'HIP 41037']

Avior = EpsilonCarinae
HIP41037 = EpsilonCarinae


class EtaUrsaeMajoris(FixedStar): # ,etaUMa

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",etaUMa", context=context, swe_string="Eta Ursae Majoris,etaUMa,ICRS,13,47,32.43776,+49,18,47.7602,-121.17,-14.91,-13.40,31.38,1.86")
        self._other_names = ['Alcaid', 'HIP 67301']

Alcaid = EtaUrsaeMajoris
HIP67301 = EtaUrsaeMajoris


class KappaVelorum(FixedStar): # ,kapVel

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",kapVel", context=context, swe_string="Kappa Velorum,kapVel,ICRS,09,22,06.8176100,-55,00,38.401683,-11.40,11.52,21.9,5.70,2.473")
        self._other_names = ['Markeb', 'HIP 45941']

Markeb = KappaVelorum
HIP45941 = KappaVelorum


class IotaCarinae(FixedStar): # ,iotCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",iotCar", context=context, swe_string="Iota Carinae,iotCar,ICRS,09,17,05.4068572,-59,16,30.835305,-18.86,11.98,12.00,4.26,2.26")
        self._other_names = ['Aspidiske', 'Turais', 'HIP 45556']

Aspidiske = IotaCarinae
Turais = IotaCarinae
HIP45556 = IotaCarinae


class AlphaVirginis(FixedStar): # ,alfVir

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfVir", context=context, swe_string="Alpha Virginis,alfVir,ICRS,13,25,11.57937,-11,09,40.7501,-42.35,-30.67,-3.310,13.06,0.97")
        self._other_names = ['Spica', 'HIP 65474']

Spica = AlphaVirginis
HIP65474 = AlphaVirginis


class AlphaBootis(FixedStar): # ,alfBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",alfBoo", context=context, swe_string="Alpha Bootis,alfBoo,ICRS,14,15,39.67207,+19,10,56.6730,-1093.39,-2000.06,-5.229,88.83,-0.05")
        self._other_names = ['Arcturus', 'HIP 69673']

Arcturus = AlphaBootis
HIP69673 = AlphaBootis


class DeltaCentauri(FixedStar): # ,delCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",delCen", context=context, swe_string="Delta Centauri,delCen,ICRS,12,08,21.4976373,-50,43,20.738614,-42.613,-11.135,11.00,5.7179,2.52")
        self._other_names = ['HIP 59196']

 = DeltaCentauri
HIP59196 = DeltaCentauri


class EpsilonBootis(FixedStar): # ,epsBoo

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",epsBoo", context=context, swe_string="Epsilon Bootis,epsBoo,ICRS,14,44,59.2175581895,+27,04,27.200350832,-50.818,21.024,-16.6,13.8267,2.45")
        self._other_names = ['Izar', 'no hip id']

Izar = EpsilonBootis
nohipid = EpsilonBootis


class BetaCarinae(FixedStar): # ,betCar

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",betCar", context=context, swe_string="Beta Carinae,betCar,ICRS,09,13,11.97746,-69,43,01.9473,-156.47,108.95,-5.10,28.82,1.69")
        self._other_names = ['Miaplacidus', 'HIP 45238']

Miaplacidus = BetaCarinae
HIP45238 = BetaCarinae


class GammaCentauri(FixedStar): # ,gamCen

    def __init__(self, context = EphContext()):
        super().__init__(swe_id = ",gamCen", context=context, swe_string="Gamma Centauri,gamCen,ICRS,12,41,31.04008,-48,57,35.5375,-185.72,5.79,-5.50,25.06,2.17")
        self._other_names = ['HIP 61932']

 = GammaCentauri
HIP61932 = GammaCentauri


