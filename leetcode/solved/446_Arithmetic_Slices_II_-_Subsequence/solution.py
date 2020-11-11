#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.

Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""
import sys
from functools import lru_cache
from collections import defaultdict
from typing import Tuple
from typing import Set
from typing import Dict
from typing import List
import pytest


class Solution:
    def _numberOfArithmeticSlices(self, A: List[int]) -> int:
        @lru_cache(None)
        def rec(i: int) -> Tuple[Dict[int, int], Dict[int, int]]:
            """The number of subsequence ending at i per gap
            and possible gaps and count"""
            ret_gaps = defaultdict(int)
            ret_pairs = defaultdict(int)
            for j in range(i):
                gaps, pairs = rec(j)
                for g, c in gaps.items():
                    if A[i]-A[j] == g:
                        ret_gaps[g] += c
                for g, c in pairs.items():
                    if A[i]-A[j] == g:
                        ret_gaps[g] += c
                ret_pairs[A[i]-A[j]] += 1
            return ret_gaps, ret_pairs

        ret = 0
        for i in range(len(A)):
            gaps, pairs = rec(i)
            ret += sum(gaps.values())
        return ret

    def _numberOfArithmeticSlices(self, A: List[int]) -> int:
        @lru_cache(None)
        def ends_with_gap(i: int, g: int):
            """Ending at i, gap is g"""
            ret = 0
            cnt = 0
            for j in range(i):
                if A[i] - A[j] == g:
                    ret += sum(ends_with_gap(j, g))
                    cnt += 1
            return ret, cnt
        ret = 0
        for i in range(len(A)):
            visited = set()
            for j in range(i):
                if A[i]-A[j] not in visited:
                    visited.add(A[i]-A[j])
                    ret += ends_with_gap(i, A[i]-A[j])[0]
        return ret

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ret = 0
        memo = [defaultdict(int) for _ in A]
        for i in range(len(A)):
            for j in range(i):
                g = A[i]-A[j]
                memo[i][g] += memo[j].get(g, 0) + 1
                ret += memo[j].get(g, 0)
        return ret


@pytest.mark.parametrize('A, expected', [
    ([2, 4, 6, 8, 10], 7),
    ([-27132718,-1026567091,-1096113402,1875897264,719631573,997805724,-1619930672,346753120,211237623,-1956889386,342725508,-91034266,-1214139569,-1588288781,1670860329,378309061,-238766940,644330323,242511466,-1025223707,1840859323,282435774,1385699764,789998790,-1769189553,-1544667666,-1772659494,1081067712,882781691,-1960293712,-2109022246,2088706652,-1183723158,833331357,440578407,-1668211865,-1137588055,277102514,-656983457,482676662,456062819,-1742391718,-900071735,-259773706,428579675,519323864,1214320590,-500470055,-499481385,-1427983600,155007844,1700710011,-766676125,1182550668,22766574,601638874,-90792153,32263579,-239160755,434824715,1036079352,1262329438,1558895459,792473917,518859435,1869733833,-662282156,-1925761028,-1545724268,-1760474762,307400072,1034770934,1197466420,610025050,1694125368,1468243914,509107662,-252645068,-651295571,-1303889311,1879182312,653655508,1853944141,-2064222956,-523821139,1906328643,1008764353,247849329,-1417071546,492851389,277660888,2022470916,-1129297029,2044353508,1390890927,-1455414881,1449232624,1729618072,380350795,-1952585922,405328770,1470357310,-1318390362,-802310179,1635863008,217289910,-15419812,342485600,793663008,1981898021,-918911759,1288807762,1825872671,-1564739100,-204745169,1311944748,1665421337,688192920,-427139678,2025335427,936476515,196259567,-710782819,2019870541,-424695778,1736122891,844062451,1301566407,-957516893,87843331,-1746472388,2039934360,1757385748,2010942248,628046897,-1933184090,1282938743,-608188006,-1308520366,1945253877,2062751447,-1095459179,1666576458,2019188466,-1478664559,-367837207,-518376619,-1557651286,-1535578135,-752267753,-442606703,829378080,-167655142,-1341056330,-23807124,-2121046104,1942193301,1349791796,-1320777038,709827676,528703422,-10222965,664482687,1980356476,-2131946583,1155371118,520619727,-2029709993,-1034682396,-1190439592,806534061,1212875733,739589195,-519508539,557740230,-811829676,1744757827,655590355,859021493,615533601,437945011,-1753288549,1428593308,1469987010,947227083,-1880417028,-1618659675,775209762,941121748,-1886726217,-619819813,-466168346,2127364859,956204467,988925076,-1906318955,1066330174,-1820912757,-1453012664,-154433079,-1274715851,1283646811,-1157670488,-997134050,-1832674170,1043177864,-234481033,1180834271,-1030283427,1598239457,-1052317568,-1374051468,-1141050064,-1544456125,1935288713,-1490991347,-581440845,-70449178,-755399812,-212973718,1250901124,-1310142019,-1670713027,-282713104,-1777134778,2040026634,1794419238,-62250948,-823963578,-1081348272,-883168380,923364891,-123753913,108033287,-1387099190,1835068556,-689428767,-710973249,-378302588,-229414445,430372249,392389984,1522678257,-1177693311,-242919592,-540740423,-1367430297,1360880690,-854949136,855099994,-2140778527,1843513080,-995907996,1400801327,409876833,-12209911,187232594,-1975709539,368170,-465817669,1465855391,-583508789,1333277353,1084257377,-755934352,-2001364095,-629742636,1595682946,1821336529,802709778,-971349072,1157563145,-1386143822,1735148286,-1243229077,-657725620,-1997731127,-1454721179,-1696766979,580397874,-301845957,-98712332,1757057913,929578591,343611098,-366909974,1914607272,-1103367014,1850675598,1113316919,-1878031655,-513261502,-1097168404,-1178634528,-1841353177,-637780003,728489980,-825761315,-2093518842,-1172713195,-775651376,-1940457401,-170186711,1747313966,-1720222322,96776084,1336612983,1533125705,-341613607,-1100575541,-1013097629,567113710,1602455754,253225075,-190145350,-1548405339,2040443761,-1348648860,-804649866,1199140895,-1609373231,-723359565,-308244794,-72388052,-242846629,1680436026,-1265603878,422131457,-704607718,647014891,1492244073,-893753672,-23636810,135621825,498605034,807059710,-811859310,-2127943572,-34534248,-1666921629,-576072366,-41669929,-292047878,1971955443,53423947,-506604655,1536774693,-545070753,1674958485,1050809155,-1945865642,-2101640713,523038540,91594349,-642321974,-131475196,1950119325,-442804531,696674704,-618350619,-1130110618,-1353440793,-48955990,-1374578253,268635546,971969062,634381,-226512395,1265880273,-1951852426,-1373637112,693900475,1671510877,1340711390,825864790,-1772662229,644094690,1681648752,1317233060,-977390500,-31915611,-1744042501,-1574215203,830928286,671287433,1506849896,-409896785,-864401510,-910263103,-349364131,1784621973,661157911,1081980244,1773932484,-715153743,-2055168987,1668024327,-849814112,2028257556,783023022,684901810,-2130596711,808057560,-521676994,-602110539,401185284,-384661836,-887940209,526921407,1493739383,-367884008,-285708456,336043390,-99391364,-1726699104,-105646349,1116344073,-904680153,1585885756,1186681001,199283624,-495548085,-1905042026,1188960248,-2040435539,-1876458629,-1085621664,823682688,-971450920,1771039078,238752562,-1653125719,1828540248,-422469468,268543081,733102714,1016158297,1124344772,-1922562008,-1009930131,158269188,-2129676492,1239234967,1381816626,-457256969,1123944805,-1055195552,-266843689,-1507315419,-1977161879,-1267994474,-476729144,-683147919,107093913,2011158994,-1448340111,2049723312,-679919372,-824535464,380409961,-2004549743,992081908,904599758,591922018,1350614660,1717783622,-663407650,-744811409,1704837595,641457836,-1644866894,-1503650246,786065885,-1731248620,339065084,1164775125,1222537918,934975123,-1773769066,-1694364822,-915250000,-2009564546,759013294,89871784,-137864331,-1468554311,229259228,1786837071,644510889,-227159919,-2124408492,1415175381,1602806294,-910786302,-1693450569,1435758658,-2140701717,2103651485,-15712787,292101890,-606088413,354289812,22967854,1886930660,362810460,-1119630365,41847849,-606093648,1828255783,1943054835,-21654263,-164583337,1515652794,-1447368125,2023750834,-1044385048,2003628028,-168088001,-104745620,834701907,138727408,-668308394,-1755997221,-2059635155,-973593503,-2018486228,854221681,-1116932990,385324491,-1559270433,1966228030,2121010124,165965705,-1488648490,-1305186584,1278949930,1493441128,-1661797010,-1222433221,1677471133,-1122936398,-96235501,2129622381,2120200970,-108302463,-735602082,-2143593971,-1565321883,-14743845,-1896647400,1458720834,463218066,-107031246,359277173,-1676516281,-1643762243,-1947115642,1759412951,963655433,1639196210,-1796260346,121092084,852866262,-606930532,490447533,-951635909,-1974871750,-33239234,593206609,1321915873,-1821469267,146771491,-1996514904,1367226949,-1792863995,850413622,-1943169254,434000260,-1857114395,1395396969,-813063079,-1786659788,-1942745731,-754208892,1621224758,94444760,1189480530,-893423788,-1294891285,-1400803646,-507163620,-1706471998,-1179303753,868374472,909074557,-1322151165,1746302252,1000312730,1952324398,1128688122,1221882528,-14525575,107412562,-1506353346,-1241054717,-247194973,-1591225083,1032586262,-209586778,-426821283,-1708381992,2079988020,-140087917,-1621651017,968610407,303646172,-87388465,-1011880516,1986604359,-1910322107,1899876581,-1879854736,-1770082595,1552514283,1302115021,-902329340,-42453242,1091247255,-2023712614,881643386,1179758735,-1189861050,-276951288,1594404893,-396818573,-1732518859,1693598899,1508567550,1026321075,-1190230686,173594817,1736303369,531701600,1364948197,1048217762,989549301,986914386,176858701,-1842180180,-1194154204,-1777497878,584021225,1071686401,708439864,-749949942,1502257639,1127363682,358623995,-1637631044,1918307279,-1091641884,-1463819336,1076601236,-1597715188,-416073419,-1905885894,2062804397,393075904,-108608766,771236013,808977481,1048491374,1539511840,879706352,591776675,30933692,682080610,-314335534,-589562519,-1898727477,1378186974,-977817596,-1355664593,1313895624,560710074,984278546,-1079769324,-1510583980,-42439714,-712863621,1103144701,1875140888,802438272,1980850081,976647698,-25665511,905412950,210013287,-1620512407,-443524968,1370682946,-1184015195,-1779586335,-433237578,50782020,-1440898126,-897384628,413897732,-1070200347,1598176610,-180626779,-569373295,458735235,-467585082,1215816276,-700198770,1766190649,-1248516480,1319361253,1950584576,-680228683,937694712,-111714399,-1454810974,1378601478,-713662758,-1730957920,2146665375,-1258658507,1548278544,-1664130748,1989423466,498210661,-1080344544,782729613,1949198627,-1565095949,351967009,-805294535,2068042187,-983283557,-794279174,298012865,-721483769,-1212381824,737325157,1165330059,-1666103919,1106024664,1279935469,1843945962,2024739049,-409717820,1617349593,1795578866,-478358032,969250933,-1475894927,1716594442,1257286717,1802891677,-2101129540,-1986016182,1636185618,-407146906,1294034797,1209774562,882424280,1045252823,-1969758574,968393291,-1541997802,-559672057,2061318491,1914349850,921510281,-741179070,116575670,1133286009,25137128,1645232401,2001157634,-1307797961,-1676722735,1233238258,1431575988,-1145471603,1114407888,1414350653,-1580288336,-1529066867,-992245185,-3357031,-1094014467,1954613265,-1007352758,380819173,1552198148,583413281,325514479,116466178,670429960,661201340,1014401358,-115453815,1460318522,-1890124262,253430844,500436308,-932389405,1517236539,-356845309,-2007448552,-1009879575,-2030288430,1039344115,-379695892,-1524956875,1470175074,-1302119333,-1805761615,-561813537,867447973,592875932,-852489405,1583786762,-1020228268,-1400396667,-1072521959,1912321309,-1072510543,748633794,611102785,-728997833,-1030305947,1357539834,784351104,1397564789,373748523,-1493886870,-313712164,-1902056832,-706089323,721481880,-659180898,1946715330,-1097183352,983956196,1713033373,1727430394,837897527,938828653,1581858162,2116105277,1622482671,-1039144028,-1009389533,175673140,-1480752013,819215770,-1258556416,-1447008907,-1670671303,1128408804,497313727,-84329478,681104898,588577064,982529321,442847637,1935145172,-2020007748,1399195966,-1018209685,1899367603,590137887,-2133141280,178764906,891191206,1919383477,-930483448,1429484395,-1756778181,-52231633,4517189,1832998310,1861335667,-1838854590,-811100284,-1728992444,579489701,-2043142492,-1467777542,1369096315,2141727144,-505173667,-1499101806,451932118,1383124275,-148620577,766055642,-1568746410,-1997619153,1296739937,1556614736,-1661786562,-1059735043,1223139095,1027109105,-975239172,902604110,1055157458,310281062,-689181640,-1119140372,1415635082,-1349281898,-481674041,441081467,922942206,-1493494629,-121048765,-337305779,-2067108881,-363878788,521610413,582947194,-1188699177,-1266897229,1123780806,-1730134534,661816289,1140919759,-78665847,139418485,-50251536,-1599889053,1964241534,-949488264,1523893491,214498010,-1441458070,197085722,1754806393,684002955,12639993,-168090132,-101781816,-1824075955,-187678925,1690582778,627287943,-1387176086,-1237937711,-268530943,537880767,219403876,1373862707,1409145245,-1317444693,627036045,38753605,-954294348,1986500718,1480275772,561120831,-186338879,-298358621,708205729,-1752930212,-673518669,-592268517,847917719,-846358484,1615570937,-2083538275,336880853,-164110066,1744617744,-113941639,2105195323,1823912581,429086404,2128061742,806727682,353974435,438230769,2099442142,1112439869,355590507,1342261108,129702060,-935838824,356539496,1824272289,897473504,497445152,1233975978,1342646955,1099277402], 0),
])
def test(A, expected):
    assert expected == Solution().numberOfArithmeticSlices(A)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
