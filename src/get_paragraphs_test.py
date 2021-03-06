#encoding:UTF-8
#author:justry

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import unittest
import datetime
import get_paragraphs

class GetBackGroundColorTest(unittest.TestCase):
    
    def setUp(self):
        self.img = cv2.imread('banmian.jpg')
        self.result1 = [[('TIMES', [[80.77165358019708, 22.508089770465954], [614.0410692277652, 24.691171412228414], [613.5522613063541, 144.43777248312435], [80.28285325846376, 142.25468666132593]]), ('EEPaper', [[2137.073447501958, 88.55399821716732], [2388.244266537881, 96.29661022089344], [2386.189758635631, 162.61125565249375], [2135.018972024498, 154.86864060883974]]), ('WORLD', [[721.7191825080236, 240.78996530476488], [951.4052642545728, 241.69974304969355], [951.1003544456578, 318.131598285029], [721.4142598052532, 317.2218197201702]]), ('OPINION', [[1009.65112937545, 242.41826235690039], [1229.9085990656874, 242.9402031444177], [1229.73213729929, 316.8804293591682], [1009.4746350536409, 316.35848847528536]]), ('BIZ', [[531.2686443328857, 242.63340854644775], [725.8385353088379, 241.42938995361328], [726.2796764373779, 312.7156319618225], [531.7097368240356, 313.919650554657]]), ('LIFE', [[1263.1512508392334, 242.74722003936768], [1422.121976852417, 244.04501152038574], [1421.5814208984375, 310.2542152404785], [1262.610694885254, 308.95642375946045]]), ('sCI-TECH', [[1707.7829394722448, 243.21039807399157], [1931.675373389201, 244.19695905047672], [1931.3740107998435, 312.0026395354001], [1707.4817065843301, 311.01606234623466]]), ('CHINA', [[327.7576352738356, 244.77861851361862], [521.508707795212, 243.61837836022278], [521.9275439743623, 311.09256122686173], [328.176465372157, 312.2527953018536]]), ('ARTS', [[1462.6261314323235, 246.245093119464], [1639.5283767962915, 248.16836098914558], [1638.8440468591025, 311.1931855660163], [1461.9418339158083, 309.2699095903708]]), ('HOME', [[102.91033573762311, 246.2726016067572], [257.2972797778066, 244.99832177986383], [257.7833589646691, 304.3068886265336], [103.39642585165001, 305.58116867105497]]), ('ODD', [[1990.609166238734, 246.53783170026597], [2128.2513081613097, 246.86888866588018], [2128.1015992603857, 308.4060283434476], [1990.4593600601834, 308.07498353753664]]), ('SPORT', [[2190.618317146033, 253.75368891629492], [2369.807892961636, 254.1648211750181], [2369.685321360757, 309.54066820208493], [2190.4957941901566, 309.12953594336176]]), ('HOME >xCHINA', [[86.80410486907594, 415.31291302099197], [462.12013596795396, 412.91259959297753], [462.5070229170503, 473.13568053927025], [87.19099435899264, 475.535989916239]]), ('Xistressescentralizedleadership ofCPCoverforeignaffairs', [[71.37340153727575, 608.7470473492532], [2374.215104661544, 601.0314284990834], [2374.462147968825, 675.2876726100758], [71.62045185681757, 683.0032869748346]]), ('rtsim', [[1723.5763558886856, 771.7186747871253], [2131.596460054329, 765.0197934954786], [2132.4940182560103, 821.7306324164069], [1724.4739001944172, 828.4295137081962]]), ('By Xinhua-Global TimesSource:Xinhua-Global Times Published:2018/5/15', [[34.56056014415914, 787.6976133026382], [1755.1516623537416, 776.743424029029], [1755.4958667590709, 830.3053002684014], [34.90476630415956, 841.2594849096423]]), ('23:18:4O', [[66.37425316093302, 847.6313505587184], [262.96249226325347, 846.5014003033178], [263.2435153400015, 897.4993696802385], [66.65528110130371, 898.6293004797515]]), ('1Uinping,general secretary of the CentralCommiteeof theCommunistPattyofChinaICPC),onTuesday calleg', [[103.65638054740175, 996.669862899634], [2349.4360383100848, 986.7931527910006], [2349.6482952359274, 1034.2171880438152], [103.86863441720494, 1044.0938918012196]]), ('enhancing the centralized leadership ofthe CPC CentralCommitee oVerforeign afais andopening up new prOspg', [[81.9450684206033, 1057.994085503509], [2386.289282532536, 1051.2952012047285], [2386.4232584889896, 1096.0400071502588], [82.0790513592959, 1102.7388939720338]]), ('major-COuntry diplomacy with Chinese characteristicA', [[49.79986032681905, 1127.5620873228672], [1143.0628893991618, 1119.8172027080884], [1143.3704660035896, 1163.6251149367044], [50.107439620266334, 1171.3700045382923]]), ('。alsoChinese president,chairman of theCentraIMilitaryCommissionand headoftheForeigNAftairsCommission', [[127.57487061139707, 1256.8667736864952], [2413.758110922732, 1248.8097667428897], [2413.91432139712, 1292.6873844275403], [127.73109425132263, 1300.7443777158958]]), ('CPcCentralCommitee made the remarkS wWhen presiding Over the firstmeeting oftheForeiqnAfairsCommissio', [[94.78799084692689, 1319.35482636043], [2373.871259364203, 1309.295289499674], [2374.063866826525, 1352.3744634694708], [94.98061507617463, 1362.4340177809486]]), ('e World is witneSsing increased instability, and Chinasdevelopment willmeet bothopportunities and challenges,了', [[136.99170327023268, 1448.3695438811903], [2395.6600894977123, 1437.6923622407824], [2395.872052400573, 1481.790833585947], [137.20365603816, 1492.467995364008]]), ('ahina wiIlbo0st risk-preVention awarene5Sin diplomacy,S0 astofirmlySafeguardnationalsOVEreignty,5ecuTiy', [[100.40886195310954, 1514.9478088491678], [2296.78682493654, 1504.8374091696448], [2296.980319443709, 1545.9016840667546], [100.60234670032534, 1556.0120715740143]]), ('deVElopMentbeneits,he SE', [[73.84926377052874, 1583.6146123645951], [648.468311871003, 1575.3734977746135], [649.0414651937949, 1615.3599021704217], [74.42241119720939, 1623.601042862841]]), ('he meetingwas alsO attended byPremier LiKeqiang, alsomemberofthestandingCommiteeof the Political Bu', [[111.94421405860548, 1707.1319635348402], [2374.6558938480116, 1687.169618034212], [2375.060689969938, 1733.440031107829], [112.34901920550985, 1753.4023737541013]]), ('CPCCentral Committee and deputy headof thecommission, andVicePresidentWangQishAa,alsO amemberofth', [[85.22076358088144, 1767.1268244214077], [2391.146853527923, 1753.648105204072], [2391.408310290544, 1799.422399835767], [85.48221664326319, 1812.9010982090535]]), ('Commission', [[83.88825140262438, 1833.9128174606703], [346.59828420278444, 1831.1806280413582], [347.03007911589896, 1872.6932794851296], [84.32004175585837, 1875.4253959474302]]), ('Xinhua-GIobal Times', [[77.52353143212261, 1952.9912811308104], [628.9094096014095, 1951.1212854222717], [629.0604059379268, 1995.5119451608286], [77.67452168894441, 1997.3820057231997]]), ('Posted in:POLITICs,DIPLOMACYI', [[65.626744663621, 2112.0609626065166], [789.6188936663633, 2107.9363018186295], [789.8956268589216, 2155.135807469559], [65.90347785558163, 2159.2604844678963]]), ('blogComments powered byDisqus', [[80.43575773083461, 2359.1676661920114], [875.543461286385, 2358.0166801258492], [875.6086870842149, 2403.3323768840537], [80.50097189938859, 2404.4833410650017]]), ('BsG回', [[79.43402195548131, 2979.9933600476306], [743.4204044641639, 2980.40444012578], [743.3465403594369, 3102.180137106759], [79.36016089570477, 3101.768959699284]])]]
        self.result = [[('iOS应用安全攻防实战',
                         [[59.78621747551866, 135.6218263159274], 
                          [623.0198774792955, 140.36444230925], 
                          [622.5361483972592, 205.96141667028007], 
                          [59.3024898667437, 201.2188002004075]]), 
                        ('如果你是一位具有Objective-C基础的应用开发者,这本书绝对是', 
                         [[29.937588670403223, 235.68372050507926],
                          [1008.7678876639076, 244.22465668463232],
                          [1008.4558937736791, 284.4474900116233],
                          [29.62560211344037, 275.90655654599124]]),
                        ('必需的——你所在的公司的ioS应用受攻击的可能性很大。这是因',
                         [[21.464731635544343, 283.9499203885403],
                          [1004.5434579667772, 293.12195413213755],
                          [1004.2168908807222, 332.53181071609686],
                          [21.13816748925485, 323.3597748746859]]),
                        ('为恶意攻击者现在使用一系列的工具,采用大多数程序员想不到',
                         [[18.48238868222818, 330.12592132287995],
                          [995.3862736524919, 340.36429732466587],
                          [995.0238025737668, 379.19391233981946],
                          [18.1199128375185, 368.9555358539589]]),
                        ('的方式进行逆向工程、跟踪和操纵应用。',
                         [[59.749779215163784, 378.39637585858077],
                          [630.7081300076288, 384.3652410025017],
                          [630.3593772886742, 422.4070989428931],
                          [59.40102660885193, 416.438235430183]]),
                        ('本书演示了多重ioS攻击方式,以及黑客们常用的工具和技术。你',
                         [[55.202472240421116, 444.7308286486711],
                          [1001.4626857773266, 453.5754762063096],
                          [1001.1462504335094, 491.55744956489866],
                          [54.88603393245798, 482.71280199507487]]),
                        ('可以从中学到保护应用的最佳方式,并且意识到和你的对手一样',
                         [[44.81755084192809, 490.6068985668154],
                          [1009.4158453957203, 500.2019509319676],
                          [1009.0842780778581, 537.6940400844132],
                          [44.4859809828404, 528.0989832354753]]),
                        ('理解和制定策略是多么重要。', 
                         [[72.64875559314909, 537.7814486436074],
                          [473.69897336260436, 542.3185402986978],
                          [473.3424947798676, 578.040367373251],
                          [72.29227667197705, 573.5032775536531]]),
                        ('检查显示应用中的微小漏洞,并避免在你的应用中出现同',
                         [[140.16627429363186, 649.4546436716881],
                          [983.183645833079, 655.2670686804829],
                          [982.9761192275284, 689.8251447027932],
                          [139.95874176421742, 684.0127187376789]]),
                        ('样的问题',
                         [[157.60315042568607, 694.5492474933042],
                          [290.644940661628, 696.7117061856619],
                          [290.17326988898833, 729.7414346584416],
                          [157.13147477630673, 727.5789718047422]]),
                        ('了解黑客如何通过代码注入感染的恶意程序',
                         [[148.02778127049254, 751.7979527825186],
                          [750.2451472157366, 757.6832631071813],
                          [749.9600611154035, 790.6081909646178],
                          [147.74269477127615, 784.7228600075663]]),
                        ('明白攻击者如何破解iOS密钥链和数据加密保护',
                         [[145.07227055453976, 807.2233978694995], 
                          [803.750952871624, 814.6835511081048], 
                          [803.4206347545048, 847.8970977065591], 
                          [144.7419521216653, 840.436938081801]]), 
                        ('n 使用调试器和自定义注入代码操控运行时Objective-C环境', 
                         [[124.26701386340649, 862.9982491818829], 
                          [948.8992683769468, 871.2516054018769], 
                          [948.6009123475542, 904.6407379081452], 
                          [123.96865673059138, 896.3873805634769]]), 
                        ('阻止攻击者劫持SSL会话和窃取数据流量', 
                         [[144.1352424347252, 919.5385101042737], 
                          [720.0371168624229, 923.6567408649897], 
                          [719.8263458972665, 957.0946510510526], 
                          [143.92446802032302, 952.9764185783987]]), 
                        ('安全地删除文件,并设计应用防止数据泄露', 
                         [[139.18068249067494, 974.1856387090969], 
                          [757.3012800142311, 977.5978412804883], 
                          [757.1293268311946, 1012.8984851378375], 
                          [139.00872473158856, 1009.4862932349774]]), 
                        ('■ 避免滥用调试,验证运行时库健全性,确保你的代码难以', 
                         [[112.5294071280699, 1028.1280363524183], 
                          [967.668869842545, 1032.9847891672234], 
                          [967.5030054661829, 1067.6054464502333], 
                          [112.3635401746273, 1062.748698845908]]), 
                        ('跟踪', 
                         [[154.49259692772642, 1075.2820829837196], 
                          [225.0455592472421, 1074.966180509873], 
                          [225.1787522703269, 1109.476272781877], 
                          [154.62578995079846, 1109.792198144039]]), 
                        ('OREILLYi', 
                         [[685.1707395853338, 1474.260249835699], 
                          [1025.997601820871, 1473.2971015163027], 
                          [1026.1985607254067, 1553.9594113085916], 
                          [685.3717000789063, 1554.9225765823273]]), 
                        ('图书分类:]信息安全>软件应用安全', 
                         [[80.87229028324565, 1490.4309834012388], 
                          [503.4172765014459, 1480.4010920448138], 
                          [504.164170027917, 1516.263827122492], 
                          [81.61918313957469, 1526.2937270622847]]), 
                        ('策划编辑:刘皎', 
                         [[75.9521638402578, 1551.8400842342512], 
                          [276.9328529270003, 1546.7236568913847], 
                          [277.6698538061396, 1579.8438171292607], 
                          [76.68916374602362, 1584.9602551786256]]), 
                        ('oreilly.com.cn', 
                         [[693.4957442938465, 1555.1961008359567], 
                          [922.7602481780436, 1554.2248203089978], 
                          [922.9001527177799, 1592.0473357052067], 
                          [693.6356373910484, 1593.0186040254232]]), 
                        ('责任编辑:李利健', 
                         [[80.32604739722194, 1595.8481913851215], 
                          [309.380100084802, 1587.1962290592155], 
                          [310.4045184182995, 1618.000163870049], 
                          [81.35046975404106, 1626.6521338247928]]), 
                        ('o瓶瘾微m', 
                         [[827.7756177494589, 1657.5252555716593], 
                          [968.3821381401983, 1656.0197350681071], 
                          [968.699227403604, 1689.7666636369588], 
                          [828.0927008818059, 1691.2722233776153]]), 
                        ('i@博文视点Broadview', 
                         [[817.084542565747, 1701.7058090808168], 
                          [1023.4529881642062, 1697.3440011867806], 
                          [1023.9042416927556, 1721.5254579418572], 
                          [817.5357703447334, 1725.8872658352986]]), 
                        ('BroadvieW', 
                         [[170.66749069319965, 1705.5105259685852], 
                          [390.48508154043003, 1697.9873965307927], 
                          [391.4740317118885, 1730.7285038342402], 
                          [171.6564407573717, 1738.251688057182]]), 
                        ('博文视点Broadview', 
                         [[544.6505123233422, 1713.9257839153977], 
                          [720.2128561515256, 1707.759219186892], 
                          [720.9374030396848, 1731.2216243731293], 
                          [545.3750449064054, 1737.3882196198347]]), 
                        ('ma', 
                         [[79.4916527226064, 1750.1662837452902], 
                          [148.87357277047354, 1747.411188014487], 
                          [149.6656287530718, 1770.1009796186336], 
                          [80.28371138747086, 1772.8561669041233]]), 
                        ("O'Reilly Media, Inc.授权电子工业出版社出版", 
                         [[72.1035909397013, 1829.996417369044], 
                          [583.5022667944296, 1800.279066803084], 
                          [584.7620936839265, 1825.0530773391097], 
                          [73.36341863533805, 1854.7704222954894]]), 
                        ('此简体中文版仅限于中国大陆(不包含中国香港、澳门特别行政区和中国台湾地区)销售发行', 
                         [[23.222638980093958, 1878.977494377602], 
                          [888.9488203018128, 1828.0093986574345], 
                          [890.2356646646866, 1852.923527464592], 
                          [24.509485591847643, 1903.8916410463619]]), 
                        ('iwAmthorized Edition for sale in the mainland of China(excluding Hong Kong,MacaosARanc泛iM4n', 
                         [[-15.745226437460351, 1909.366934384874], 
                          [1013.358054502944, 1855.1177064803398], 
                          [1014.388022769067, 1877.5772771510788], 
                          [-14.715261418797317, 1931.8265725171505]])]]

    
    def tearDown(self):
        pass
    
    def test_0(self):
        a = get_paragraphs.put_chinese(self.img, self.result)
        #plt.imshow(a)
        #plt.show()
        #print('end')
    
    def test_1(self):
        box = np.array([[1, 0], [8, 7], [7, 8], [0, 1]])
        a = get_paragraphs.minimum_bounding_rectangle(box)
        theta = 1e-9
        delta = box - a
        self.assertTrue(np.all(delta<theta))
        box1 = np.array([[1, 0], [8, 7], [7, 8], [0, 1], [1, 0], [2, 2], [0, 1]])
        a = get_paragraphs.minimum_bounding_rectangle(box1)
        theta = 1e-9
        delta = box - a
        self.assertTrue(np.all(delta<theta))
        
    def test_2(self):
        start_time = datetime.datetime.now()
        for i in range(10000):
            points = np.random.rand(15, 2)
            points = 200 * points + 200
            box = get_paragraphs.minimum_bounding_rectangle(points)
        end_time = datetime.datetime.now()
        print('duration time is ', end_time - start_time)
        print(box)
        img = np.zeros((600, 600, 3), np.uint8)
        for i in points:
            img = cv2.circle(img, tuple(i.astype(np.int32).tolist()), 3, (0, 255, 0), -1)
        img = cv2.polylines(img.copy(), [box.astype(np.int32)], 1, (55, 155, 155), 1)
        plt.imshow(img)
        plt.show()
        print('end')
        
    def test_sorted_result(self):
        result = [('1', [[4, 5]]),
                  ('2', [[3, 2]]),
                  ('3', [[1, 0]])]
        ret = get_paragraphs.sorted_result(result)
        self.assertTrue(ret==result[::-1])
        
    def test_sorted_result_1(self):
        ret = get_paragraphs.sorted_result(self.result[0])
        print('end')
        
    def test_get_paragraphs(self):
        result = [('0', [[0, 0], [10, 0], [10, 2], [0, 2]]),
                  ('1', [[0, 3], [10, 3], [10, 5], [0, 5]]),
                  ('2', [[0, 6], [10, 6], [10, 8], [0, 8]]),
                  ('3', [[0, 9], [10, 9], [10, 11], [0, 11]]),
                  ('4', [[0, 15], [10, 15], [10, 17], [0, 17]])]
        paras = get_paragraphs.get_paragraphs(result)
        paras = get_paragraphs.get_paragraphs(self.result[0])
        paras = get_paragraphs.get_paragraphs(self.result1[0])
        for i in paras:
            print(len(i))        
        print('end')
        
    def test_put_chinese(self):
        img = get_paragraphs.put_chinese(self.img, self.result, False)
        #plt.imshow(img)
        #plt.show()
        
    def test_put_para_chinese(self):
        paras = get_paragraphs.get_paragraphs(self.result[0])
        result = [[(j.label, j.coord) for j in i] for i in paras]
        img = get_paragraphs.put_para_chinese(self.img, result)
        plt.imshow(img)
        plt.show()
        
    def test_divide_sentence(self):
        s = '的方式进行逆向工程、跟踪和操纵应用。'
        ret = get_paragraphs.divide_sentence(s, 3)
        print(ret)
        s = "If you're an application developer with an Objective-C foundation, this book is absolutely\
necessary-your company's IOS app is highly likely to be attacked. This is because\
malicious attackers now use a range of tools to reverse engineer, track, and manipulate\
applications in ways that most programmers do not think of."
        ret = get_paragraphs.divide_sentence(s, 56, False)
        print(ret)
        
class LineTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_0(self):
        a = np.array([[1, 0], [8, 7], [7, 8], [0, 1]])
        line = get_paragraphs.Line('', a)
        self.assertAlmostEqual(np.sqrt(49*2), line.w)
        self.assertAlmostEqual(np.sqrt(2), line.h)
    

def suite():
    suite = unittest.TestSuite()
    suite.addTest(GetBackGroundColorTest('test_0'))
    suite.addTest(GetBackGroundColorTest('test_1'))
    #suite.addTest(GetBackGroundColorTest('test_2'))
    suite.addTest(GetBackGroundColorTest('test_sorted_result'))
    suite.addTest(GetBackGroundColorTest('test_sorted_result_1'))
    suite.addTest(GetBackGroundColorTest('test_get_paragraphs'))
    suite.addTest(GetBackGroundColorTest('test_put_chinese'))
    suite.addTest(GetBackGroundColorTest('test_put_para_chinese'))
    suite.addTest(GetBackGroundColorTest('test_divide_sentence'))
    suite.addTest(LineTest('test_0'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')