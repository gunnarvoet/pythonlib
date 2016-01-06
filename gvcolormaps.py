#!/usr/bin/env python
# Filename: gvcolormaps.py

import numpy as np
import matplotlib as mpl
#import gvimport as gvi

__author__ = "Gunnar Voet"
__email__ = "gvoet@ucsd.edu"
__version__ = "0.1"

def ocean4jbm():
  cmap =  mpl.colors.ListedColormap(np.array([
    [0.19532446362340,   0.13796378116395,   0.15719499584055],
    [0.19923095289586,   0.14112254081445,   0.16238593878581],
    [0.20313744216833,   0.14430433496405,   0.16755384723197],
    [0.20704393144080,   0.14747625718546,   0.17273162760631],
    [0.21095042071327,   0.15062843555050,   0.17792915183702],
    [0.21485690998574,   0.15379377648646,   0.18311351349682],
    [0.21876339925820,   0.15697557063605,   0.18828142194298],
    [0.22266988853067,   0.16014091157201,   0.19346578360278],
    [0.22657637780314,   0.16329308993705,   0.19866330783349],
    [0.23048286707561,   0.17274355848413,   0.21077118179371],
    [0.23438935634808,   0.18534317212223,   0.22633423061868],
    [0.23829584562054,   0.19794278576033,   0.24189727944366],
    [0.24220233489301,   0.21054239939843,   0.25746032826864],
    [0.24610882416548,   0.22316833817836,   0.27302337709361],
    [0.25001531343795,   0.23579756760102,   0.28858642591859],
    [0.25392180271042,   0.24839718123912,   0.30414947474356],
    [0.25782829198288,   0.26099679487722,   0.31971252356854],
    [0.26173478125535,   0.27359640851532,   0.33527557239352],
    [0.26564127052782,   0.28619602215342,   0.35083862121849],
    [0.26954775980029,   0.29879563579152,   0.36640167004347],
    [0.27345424907276,   0.31139524942962,   0.38196471886844],
    [0.27736073834522,   0.32399486306772,   0.39752776769342],
    [0.28126722761769,   0.33659447670582,   0.41310397908931],
    [0.28517371689016,   0.34919409034392,   0.42869664369884],
    [0.28908020616263,   0.36179370398202,   0.44427285509473],
    [0.29298669543510,   0.37439331762012,   0.45983590391970],
    [0.29689318470756,   0.38701267511459,   0.47539895274468],
    [0.30079967398003,   0.39964190453724,   0.49096200156966],
    [0.30470616325250,   0.41224809946080,   0.50652505039463],
    [0.30861265252497,   0.42484771309890,   0.52208809921961],
    [0.31251914179744,   0.43744732673700,   0.53765114804458],
    [0.31642563106990,   0.45004694037510,   0.55321419686956],
    [0.32033212034237,   0.46264655401320,   0.56877724569453],
    [0.32423860961484,   0.47524616765130,   0.58434029451951],
    [0.32814509888731,   0.48784578128940,   0.59990334334449],
    [0.33205158815977,   0.50044539492750,   0.61151103961000],
    [0.33595807743224,   0.51304500856560,   0.60927500191740],
    [0.33986456670471,   0.52564462220370,   0.60703896422479],
    [0.34377105597718,   0.53824423584180,   0.60480292653219],
    [0.35138939024721,   0.54889578898472,   0.60258005141050],
    [0.36364753076420,   0.55711226650868,   0.60037362950245],
    [0.37590567128119,   0.56531229081899,   0.59815075438076],
    [0.38816381179818,   0.57349915255839,   0.59591471668816],
    [0.40042195231517,   0.58168601429779,   0.59367867899556],
    [0.41268009283216,   0.58987287603719,   0.59144264130296],
    [0.42493823334915,   0.59808277227568,   0.58920660361035],
    [0.43719637386613,   0.60629924979964,   0.58697056591775],
    [0.44945451438312,   0.61448940218177,   0.58473452822515],
    [0.46171265490011,   0.62267626392117,   0.58249849053255],
    [0.47397079541710,   0.63086312566056,   0.58026245283994],
    [0.48623222657682,   0.63905327804269,   0.57802970579007],
    [0.49851998287836,   0.64726975556665,   0.57582328388202],
    [0.51080115789445,   0.65547965180514,   0.57361028068852],
    [0.52305929841144,   0.66366651354454,   0.57137424299591],
    [0.53531743892843,   0.67185337528394,   0.56913820530331],
    [0.54757557944542,   0.68004023702334,   0.56690216761071],
    [0.55983371996241,   0.68824026133365,   0.56466612991810],
    [0.57209186047940,   0.69645673885761,   0.56243009222550],
    [0.58435000099638,   0.70465676316792,   0.56019405453290],
    [0.59660814151337,   0.71284362490732,   0.55795801684030],
    [0.60886628203036,   0.72103048664672,   0.55572197914769],
    [0.62112442254735,   0.72921734838612,   0.55348594145509],
    [0.63338256306434,   0.73742724462462,   0.55127293826159],
    [0.64564070358133,   0.74564372214857,   0.54906651635354],
    [0.65789884409832,   0.75383387453070,   0.54683376930366],
    [0.67015698461531,   0.76202073627010,   0.54459773161106],
    [0.68241512513230,   0.77023721379405,   0.54236169391846],
    [0.69467326564929,   0.77845040067528,   0.54012565622586],
    [0.70693140616627,   0.78663726241468,   0.53788961853325],
    [0.71871569413038,   0.79482412415408,   0.53751608462489],
    [0.72884149815941,   0.80301098589347,   0.54366131396136],
    [0.73897717411662,   0.81120771956106,   0.54980654329784],
    [0.74913259393020,   0.81942419708501,   0.55595177263431],
    [0.75927485117287,   0.82565312640105,   0.56209700197078],
    [0.76940065520190,   0.82939762045719,   0.56824223130726],
    [0.77952645923092,   0.83314211451334,   0.57438746064373],
    [0.78965226325995,   0.83688660856948,   0.58053268998020],
    [0.79977806728897,   0.84063110262562,   0.58667791931668],
    [0.80990387131800,   0.84437559668177,   0.59282314865315],
    [0.82002967534703,   0.84814312523701,   0.59894534349052],
    [0.83015547937605,   0.85191723507771,   0.60506095704244],
    [0.84030760854691,   0.85566501977658,   0.61120289573619],
    [0.85046302836049,   0.85940951383272,   0.61734812507266],
    [0.86058883238951,   0.86315400788887,   0.62349335440913],
    [0.87071463641854,   0.86689850194501,   0.62963858374561],
    [0.88084044044757,   0.87064299600115,   0.63578381308208],
    [0.89096624447659,   0.87439407134275,   0.64192904241855],
    [0.90109204850562,   0.87816818118345,   0.64807427175503],
    [0.91121785253464,   0.88193241909596,   0.65421950109150],
    [0.92134365656367,   0.88567691315211,   0.66036473042797],
    [0.93146946059270,   0.88942140720825,   0.66650995976445],
    [0.94159526462172,   0.89316590126439,   0.67265518910092],
    [0.95173752186439,   0.89691039532054,   0.67878396522375],
    [0.96189294167797,   0.90065488937668,   0.68489957877567],
    [0.96890342621721,   0.90441912728919,   0.69103493618396],
    [0.97512274097377,   0.90819323712989,   0.69718016552043],
    [0.98134205573033,   0.91194431247149,   0.70332539485691],
    [0.98756137048688,   0.91568880652764,   0.70947062419338],
    [0.99378068524344,   0.91943330058378,   0.71561585352985]]))
  return cmap
def ocean4jbm_r():
  cmap =  mpl.colors.ListedColormap(np.flipud(np.array([
    [0.19532446362340,   0.13796378116395,   0.15719499584055],
    [0.19923095289586,   0.14112254081445,   0.16238593878581],
    [0.20313744216833,   0.14430433496405,   0.16755384723197],
    [0.20704393144080,   0.14747625718546,   0.17273162760631],
    [0.21095042071327,   0.15062843555050,   0.17792915183702],
    [0.21485690998574,   0.15379377648646,   0.18311351349682],
    [0.21876339925820,   0.15697557063605,   0.18828142194298],
    [0.22266988853067,   0.16014091157201,   0.19346578360278],
    [0.22657637780314,   0.16329308993705,   0.19866330783349],
    [0.23048286707561,   0.17274355848413,   0.21077118179371],
    [0.23438935634808,   0.18534317212223,   0.22633423061868],
    [0.23829584562054,   0.19794278576033,   0.24189727944366],
    [0.24220233489301,   0.21054239939843,   0.25746032826864],
    [0.24610882416548,   0.22316833817836,   0.27302337709361],
    [0.25001531343795,   0.23579756760102,   0.28858642591859],
    [0.25392180271042,   0.24839718123912,   0.30414947474356],
    [0.25782829198288,   0.26099679487722,   0.31971252356854],
    [0.26173478125535,   0.27359640851532,   0.33527557239352],
    [0.26564127052782,   0.28619602215342,   0.35083862121849],
    [0.26954775980029,   0.29879563579152,   0.36640167004347],
    [0.27345424907276,   0.31139524942962,   0.38196471886844],
    [0.27736073834522,   0.32399486306772,   0.39752776769342],
    [0.28126722761769,   0.33659447670582,   0.41310397908931],
    [0.28517371689016,   0.34919409034392,   0.42869664369884],
    [0.28908020616263,   0.36179370398202,   0.44427285509473],
    [0.29298669543510,   0.37439331762012,   0.45983590391970],
    [0.29689318470756,   0.38701267511459,   0.47539895274468],
    [0.30079967398003,   0.39964190453724,   0.49096200156966],
    [0.30470616325250,   0.41224809946080,   0.50652505039463],
    [0.30861265252497,   0.42484771309890,   0.52208809921961],
    [0.31251914179744,   0.43744732673700,   0.53765114804458],
    [0.31642563106990,   0.45004694037510,   0.55321419686956],
    [0.32033212034237,   0.46264655401320,   0.56877724569453],
    [0.32423860961484,   0.47524616765130,   0.58434029451951],
    [0.32814509888731,   0.48784578128940,   0.59990334334449],
    [0.33205158815977,   0.50044539492750,   0.61151103961000],
    [0.33595807743224,   0.51304500856560,   0.60927500191740],
    [0.33986456670471,   0.52564462220370,   0.60703896422479],
    [0.34377105597718,   0.53824423584180,   0.60480292653219],
    [0.35138939024721,   0.54889578898472,   0.60258005141050],
    [0.36364753076420,   0.55711226650868,   0.60037362950245],
    [0.37590567128119,   0.56531229081899,   0.59815075438076],
    [0.38816381179818,   0.57349915255839,   0.59591471668816],
    [0.40042195231517,   0.58168601429779,   0.59367867899556],
    [0.41268009283216,   0.58987287603719,   0.59144264130296],
    [0.42493823334915,   0.59808277227568,   0.58920660361035],
    [0.43719637386613,   0.60629924979964,   0.58697056591775],
    [0.44945451438312,   0.61448940218177,   0.58473452822515],
    [0.46171265490011,   0.62267626392117,   0.58249849053255],
    [0.47397079541710,   0.63086312566056,   0.58026245283994],
    [0.48623222657682,   0.63905327804269,   0.57802970579007],
    [0.49851998287836,   0.64726975556665,   0.57582328388202],
    [0.51080115789445,   0.65547965180514,   0.57361028068852],
    [0.52305929841144,   0.66366651354454,   0.57137424299591],
    [0.53531743892843,   0.67185337528394,   0.56913820530331],
    [0.54757557944542,   0.68004023702334,   0.56690216761071],
    [0.55983371996241,   0.68824026133365,   0.56466612991810],
    [0.57209186047940,   0.69645673885761,   0.56243009222550],
    [0.58435000099638,   0.70465676316792,   0.56019405453290],
    [0.59660814151337,   0.71284362490732,   0.55795801684030],
    [0.60886628203036,   0.72103048664672,   0.55572197914769],
    [0.62112442254735,   0.72921734838612,   0.55348594145509],
    [0.63338256306434,   0.73742724462462,   0.55127293826159],
    [0.64564070358133,   0.74564372214857,   0.54906651635354],
    [0.65789884409832,   0.75383387453070,   0.54683376930366],
    [0.67015698461531,   0.76202073627010,   0.54459773161106],
    [0.68241512513230,   0.77023721379405,   0.54236169391846],
    [0.69467326564929,   0.77845040067528,   0.54012565622586],
    [0.70693140616627,   0.78663726241468,   0.53788961853325],
    [0.71871569413038,   0.79482412415408,   0.53751608462489],
    [0.72884149815941,   0.80301098589347,   0.54366131396136],
    [0.73897717411662,   0.81120771956106,   0.54980654329784],
    [0.74913259393020,   0.81942419708501,   0.55595177263431],
    [0.75927485117287,   0.82565312640105,   0.56209700197078],
    [0.76940065520190,   0.82939762045719,   0.56824223130726],
    [0.77952645923092,   0.83314211451334,   0.57438746064373],
    [0.78965226325995,   0.83688660856948,   0.58053268998020],
    [0.79977806728897,   0.84063110262562,   0.58667791931668],
    [0.80990387131800,   0.84437559668177,   0.59282314865315],
    [0.82002967534703,   0.84814312523701,   0.59894534349052],
    [0.83015547937605,   0.85191723507771,   0.60506095704244],
    [0.84030760854691,   0.85566501977658,   0.61120289573619],
    [0.85046302836049,   0.85940951383272,   0.61734812507266],
    [0.86058883238951,   0.86315400788887,   0.62349335440913],
    [0.87071463641854,   0.86689850194501,   0.62963858374561],
    [0.88084044044757,   0.87064299600115,   0.63578381308208],
    [0.89096624447659,   0.87439407134275,   0.64192904241855],
    [0.90109204850562,   0.87816818118345,   0.64807427175503],
    [0.91121785253464,   0.88193241909596,   0.65421950109150],
    [0.92134365656367,   0.88567691315211,   0.66036473042797],
    [0.93146946059270,   0.88942140720825,   0.66650995976445],
    [0.94159526462172,   0.89316590126439,   0.67265518910092],
    [0.95173752186439,   0.89691039532054,   0.67878396522375],
    [0.96189294167797,   0.90065488937668,   0.68489957877567],
    [0.96890342621721,   0.90441912728919,   0.69103493618396],
    [0.97512274097377,   0.90819323712989,   0.69718016552043],
    [0.98134205573033,   0.91194431247149,   0.70332539485691],
    [0.98756137048688,   0.91568880652764,   0.70947062419338],
    [0.99378068524344,   0.91943330058378,   0.71561585352985]])))
  return cmap
