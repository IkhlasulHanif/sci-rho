from templates_001_050 import *
from templates_051_100 import *
from templates_101_150 import *
from templates_151_200 import *

class Mat001_multi(Mat001):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'对{self.total}人进行了关于饮料偏好的调查。结果显示在下方的韦恩图中。只喜欢咖啡或只喜欢茶的人数总和是多少？'
        self.description_arabic = f'تم استطلاع آراء {self.total} شخصًا حول تفضيلاتهم للمشروبات. تُعرض النتائج في مخطط فن أدناه. ما مجموع عدد الأشخاص الذين يفضلون القهوة فقط أو الشاي فقط؟'
        self.description_hindi = f'{self.total} लोगों से उनकी पेय पदार्थों की पसंद के बारे में सर्वेक्षण किया गया। परिणाम नीचे दिए गए वेन चित्र (Venn diagram) में प्रदर्शित हैं। केवल कॉफ़ी या केवल चाय पसंद करने वाले लोगों का योग क्या है?'
        self.description_kazakh = f'{self.total} адам өздеріннің сусын қалауы бойынша сауалнамаға қатысты. Нәтижелері төмендегі Венн диаграммасында көрсетілген. Тек Кофе немесе тек Шай қалайтын жалпы адам саны қанша?'
        self.description_swahili = f'Watu {self.total} walihojiwa kuhusu vinywaji wanavyopendelea. Matokeo yanaonyeshwa kwenye mchoro wa Venn hapa chini. Ni jumla ya watu wangapi wanaopendelea Kahawa pekee au Chai pekee?'

class Mat002_multi(Mat002):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'在一项对{self.total}名学生的调查中，收集了关于他们对数学、科学和英语三科偏好的以下信息。结果显示在下方的韦恩图中。有多少学生喜欢数学？'
        self.description_arabic = f'في استطلاع شمل {self.total} طالبًا، جُمعت المعلومات التالية حول تفضيلاتهم لثلاث مواد: الرياضيات، والعلوم، واللغة الإنجليزية. تُعرض النتائج في مخطط فن أدناه. كم عدد الطلاب الذين يفضلون الرياضيات؟'
        self.description_hindi = f'{self.total} छात्रों के एक सर्वेक्षण में, तीन विषयों - गणित, विज्ञान और अंग्रेजी - के प्रति उनकी पसंद के बारे में निम्नलिखित जानकारी एकत्र की गई। परिणाम नीचे दिए गए वेन चित्र में दिखाए गए हैं। कितने छात्रों को गणित पसंद है?'
        self.description_kazakh = f'{self.total} оқушы арасында жүргізілген сауалнамада олардың үш пәнге (Математика, Жаратылыстану және Ағылшын тілі) деген қалауы бойынша келесі ақпарат жиналды. Нәтижелер төмендегі Венн диаграммасында көрсетілген. Математиканы қанша оқушы жақсы көреді?'
        self.description_swahili = f'Katika utafiti wa wanafunzi {self.total}, taarifa zifuatazo zilikusanywa kuhusu masomo matatu wanayopendelea: Hisabati, Sayansi, na Kiingereza. Matokeo yanaonyeshwa kwenye mchoro wa Venn hapa chini. Ni wanafunzi wangapi wanapenda Hisabati?'

class Mat003_multi(Mat003):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'将各尺寸保留至1位有效数字，估算该长方体的体积。'
        self.description_arabic = f'بتقريب كل بُعد إلى رقم معنوي واحد، قدّر حجم الصندوق.'
        self.description_hindi = f'प्रत्येक आयाम को 1 सार्थक अंक (significant figure) तक पूर्णांकित करके, बॉक्स के आयतन का अनुमान लगाएँ।'
        self.description_kazakh = f'Әрбір өлшемді 1 мәнді цифрға дейін ықшамдап, қораптың көлемін есептеңіз.'
        self.description_swahili = f'Kwa kuzungusha kila kipimo hadi tarakimu 1 muhimu, kadiria ujazo wa sanduku.'

class Mat004_multi(Mat004):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，一个花园的各测量值均精确到最近的整米。试计算该花园面积的上界。'
        self.description_arabic = f'بالنظر إلى الحديقة أدناه التي قياساتها مضبوطة لأقرب متر، احسب الحد الأعلى لمساحة الحديقة.'
        self.description_hindi = f'नीचे दिए गए बगीचे के माप निकटतम मीटर तक सही हैं। बगीचे के क्षेत्रफल की ऊपरी सीमा (upper bound) की गणना कीजिए।'
        self.description_kazakh = f'Төменде берілген бақтын өлшемдері ең жақын метрге дейін дұрыс көрсетілген. Бақ ауданының жоғарғы шегін есептеңіз.'
        self.description_swahili = f'Zingatia bustani hapa chini ambayo vipimo vyake ni sahihi kwa mita ya karibu zaidi. Kokotoa kikomo cha juu cha eneo la bustani.'

class Mat005_multi(Mat005):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'哪个瓶子更物有所值？写出你的判断过程。'
        self.description_arabic = f'أي زجاجة تقدم قيمة أفضل مقابل المال؟ وضّح كيفية توصلت إلى ذلك.'
        self.description_hindi = f'कौन सी बोतल पैसे के लिए बेहतर मूल्य (value for money) प्रदान करती है? दिखाएँ कि आपने यह कैसे तय किया।'
        self.description_kazakh = f'Қай бөтелке ақша құны жағынан ен тиімді? Қалай шешкеніңізді көрсетіңіз.'
        self.description_swahili = f'Chupa ipi ina thamani bora zaidi kwa pesa? Onyesha hatua zako za utatuzi.'

class Mat006_multi(Mat006):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一名游客想使用公告牌上显示的汇率将{self.total_eur}欧元（EUR）兑换成日元（JPY）。他们将收到多少日元？结果保留两位小数。'
        self.description_arabic = f'يريد سائح تحويل {self.total_eur} يورو (EUR) إلى ين ياباني (JPY) باستخدام الأسعار المعروضة على اللوحة. كم ين سيحصل عليه؟ قرّب النتيجة إلى منزلتين عشريتين.'
        self.description_hindi = f'एक पर्यटक बोर्ड पर दिखाई गई दरों का उपयोग करके {self.total_eur} Euros (EUR) को Japanese Yen (JPY) में बदलना चाहते हैं। उन्हें कितने Yen मिलेंगे? परिणाम को दो दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Турист тақтада көрсетілген бағамдарды пайдаланып, {self.total_eur} Еуроны (EUR) Жапон Йеніне (JPY) айырбастағысы келеді. Олар қанша Йен алады? Нәтижені екі ондық таңбаға дейін ықшамданыз.'
        self.description_swahili = f'Mtalii anataka kubadilisha Euro {self.total_eur} (EUR) kuwa Yen ya Kijapani (JPY) akitumia viwango vilivyoonyeshwa kwenye ubao. Atapokea Yen ngapi? Zungusha jibu katika nafasi mbili za desimali.'

class Mat007_multi(Mat007):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算网格中阴影部分所占的百分比。结果精确至两位小数。'
        self.description_arabic = f'احسب النسبة المئوية للجزء المظلل من الشبكة. قرّب النتيجة إلى منزلتين عشريتين.'
        self.description_hindi = f'गणना करें कि ग्रिड का कितना प्रतिशत हिस्सा छायांकित है। परिणाम को दो दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Тордың қандай пайызы боялғанын есептеңіз. Нәтижені екі ондық таңбаға дейін ықшамданыз.'
        self.description_swahili = f'Kokotoa ni asilimia ngapi ya gridi imetiwa kivuli. Zungusha jibu katika nafasi mbili za desimali.'

class Mat008_multi(Mat008):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'时钟显示了一场数学考试的开始和结束时间。计算考试的总时长，以小时和分钟为单位。'
        self.description_arabic = f'تُظهر الساعات وقتي بدء وانتهاء امتحان الرياضيات. احسب المدة الكلية للامتحان بالساعات والدقائق.'
        self.description_hindi = f'घड़ियाँ गणित की परीक्षा के शुरू होने और समाप्त होने का समय दिखाती हैं। परीक्षा की कुल अवधि (total length) की घंटों और मिनटों में गणना करें।'
        self.description_kazakh = f'Сағаттар математика емтиханының басталу және аяқталу уақытын көрсетеді. Емтиханның жалпы ұзақтығын сағат және минутпен есептеңіз.'
        self.description_swahili = f'Saa hizi zinaonyesha muda wa kuanza na kumaliza wa mtihani wa hisabati. Kokotoa jumla ya muda wa mtihani katika saa na dakika.'

class Mat009_multi(Mat009):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"杰森在{self.departure_time}.00时离开A镇，骑车前往D镇。行程图显示了杰森的旅程。试求杰森从A到B和从C到D的平均速度之差。"
        self.description_arabic = f"يغادر جيسون المدينة A عند الساعة {self.departure_time}.00 ويتجه بالدراجة إلى المدينة D. يوضح الرسم البياني للحركة رحلة جيسون. أوجد الفرق بين متوسط سرعة جيسون من A إلى B ومن C إلى D."
        self.description_hindi = f"जेसन (Jason) शहर A से {self.departure_time}.00 बजे निकलता है और साइकिल से शहर D की ओर जाता है। यात्रा ग्राफ जेसन (Jason) की यात्रा को दर्शाता है। A से B और C से D तक जेसन की औसत गति (Average Speed) का अंतर ज्ञात कीजिए।"
        self.description_kazakh = f"Джейсон А қаласынан сағат {self.departure_time}.00-де шығып, D қаласына велосипедпен барады. Жол жүру графигі Джейсонның сапарын көрсетеді. Джейсонның А-дан В-ға және С-дан D-ға дейінгі орташа жылдамдықтарының айырмашылығын табыңыз."
        self.description_swahili = f"Jason anaondoka Mji A saa {self.departure_time}.00 na kuendesha baiskeli kuelekea Mji D. Grafu ya safari inaonyesha safari ya Jason. Tafuta tofauti ya Kasi ya Wastani ya Jason kutoka A hadi B na C hadi D."

class Mat010_multi(Mat010):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一段汽车旅程的速度-时间图。计算在这{self.t_end}秒内行驶的总距离。'
        self.description_arabic = f'يوضح الرسم البياني للسرعة مقابل الزمن جزءًا من رحلة سيارة. احسب المسافة الكلية المقطوعة خلال {self.t_end} ثانية.'
        self.description_hindi = f'चित्र में कार यात्रा के एक भाग का गति-समय ग्राफ दर्शाया गया है। {self.t_end} सेकंड के दौरान तय की गई कुल दूरी की गणना कीजिए।'
        self.description_kazakh = f'Диаграммада автокөлік сапарының бір бөлігінің жылдамдық-уақыт графигі көрсетілген. {self.t_end} секунд ішінде жүріп өткен жалпы қашықтықты есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya kasi-muda ya sehemu ya safari ya gari. Kokotoa jumla ya umbali uliosafiriwa katika sekunde {self.t_end}.'

class Mat011_multi(Mat011):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'凯从办公室骑车去开会，然后再骑回来。行程图显示了他在会议上的时间以及他返回的旅程。凯以{self.speed:.2f} km/h的恒定速度从办公室骑车去开会。凯什么时间离开他的办公室？'
        self.description_arabic = f'يقود كاي دراجته من مكتبه إلى اجتماع ثم يعود مرة أخرى. يوضح الرسم البياني للحركة الزمن الذي قضاه في الاجتماع ورحلة العودة. يسير كاي بسرعة ثابتة مقدارها {self.speed:.2f} كم/ساعة من مكتبه إلى الاجتماع. في أي وقت يغادر كاي مكتبه؟'
        self.description_hindi = f'Ky अपने कार्यालय से मीटिंग तक साइकिल से जाता है और वापस आता है। यात्रा ग्राफ में मीटिंग में बिताया गया समय और वापसी की यात्रा दर्शाई गई है। Ky अपने कार्यालय से मीटिंग तक {self.speed:.2f} km/h की स्थिर गति (constant speed) से साइकिल चलाता है। Ky अपने कार्यालय से किस समय निकलता है?'
        self.description_kazakh = f'Ки кеңсесінен жиналысқа дейін велосипедпен барып, қайта оралады. Жол жүру графигі оның жиналыста болған уақытын және қайтқан сапарын көрсетеді. Ки кеңсесінен жиналысқа {self.speed:.2f} км/сағ тұрақты жылдамдықпен барады. Ки кеңсесінен сағат нешеде шығады?'
        self.description_swahili = f'Ky anaendesha baiskeli kutoka ofisini kwake kuelekea kwenye mkutano na kurudi tena. Grafu ya safari inaonyesha muda wake mkutanoni na safari yake ya kurudi. Ky anaendesha baiskeli kutoka ofisini kwake kuelekea mkutanoni kwa kasi thabiti ya {self.speed:.2f} km/h. Ky aliondoka ofisini kwake saa ngapi?'

class Mat012_multi(Mat012):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中所示为二次函数的图像。首先确定图像的方程，然后用它来求解${self.target_eq}$。'
        self.description_arabic = f'يُعرض التمثيل البياني لدالة تربيعية على الشبكة. بعد تحديد معادلة التمثيل البياني أولًا، استخدمها لحل ${self.target_eq}$.'
        self.description_hindi = f'ग्रिड पर एक द्विघात फलन (quadratic function) का ग्राफ दिखाया गया है। पहले ग्राफ का समीकरण ज्ञात कीजिए और फिर उसका उपयोग करके ${self.target_eq}$ को हल कीजिए।'
        self.description_kazakh = f'Квадраттық функцияның графигі көрсетілген. Алдымен графиктің теңдеуін анықтай отырып, оны қолданып ${self.target_eq}$ шешіңіз.'
        self.description_swahili = f'Grafu ya kazi ya kipeo cha pili imeonyeshwa kwenye gridi. Kwa kuanza kutafuta mlinganyo wa grafu hiyo, utumie kutatua ${self.target_eq}$.'

class Mat013_multi(Mat013):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'通过在网格上画一条合适的直线，求解方程${self.target_eq_str}$。'
        self.description_arabic = f'برسم خط مستقيم مناسب على الشبكة، حل المعادلة ${self.target_eq_str}$.'
        self.description_hindi = f'ग्रिड पर एक उपयुक्त सीधी रेखा खींचकर, समीकरण ${self.target_eq_str}$ को हल करें।'
        self.description_kazakh = f'Торда сәйкес түзу сызықты салу арқылы ${self.target_eq_str}$ теңдеуін шешіңіз.'
        self.description_swahili = f'Kwa kuchora mstari mnyofu unaofaa kwenye gridi, tatua mlinganyo ${self.target_eq_str}$.'

class Mat014_multi(Mat014):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'细菌培养物中的数量 $P$在$t$小时后呈指数增长。\n该增长曲线如图所示。\n利用该曲线求出细菌数量达到 {round(float(self.k), 10)} 需要多少小时。'
        self.description_arabic = f'يزداد عدد أفراد مزرعة بكتيرية، $P$، أسيًا مع الزمن $t$ بالساعات.\nيُعرض التمثيل البياني لهذا النمو على الشبكة.\nاستخدم التمثيل البياني لإيجاد عدد الساعات اللازمة لوصول عدد البكتيريا إلى {round(float(self.k), 10)}.'
        self.description_hindi = f'एक जीवाणु संवर्धन (bacterial culture) की जनसंख्या, $P$, समय $t$ घंटों के साथ घातीय रूप से बढ़ती है।\nइस वृद्धि का ग्राफ ग्रिड पर दिखाया गया है।\nग्राफ का उपयोग करके पता लगाएँ कि जीवाणुओं की संख्या को {round(float(self.k), 10)} तक पहुँचने में कितने घंटे लगते हैं।'
        self.description_kazakh = f'Бактерия өсіндісінің популяциясы, $P$, $t$ сағат уақыт ішінде экспоненциалды түрде өседі.\nБұл өсімнің графигі торда көрсетілген.\nГрафикті пайдалана отырып, бактерия саны {round(float(self.k), 10)}-ге жетуі үшін қанша сағат қажет екенін табыңыз.'
        self.description_swahili = f'Idadi ya kundi la bakteria, $P$, inaongezeka kwa kielelezo kulingana na muda $t$ katika saa. Grafu ya ukuaji huu imeonyeshwa kwenye gridi. Tumia grafu hiyo kutafuta ni saa ngapi zinahitajika ili idadi ya bakteria ifikie {round(float(self.k), 10)}.'

class Mat015_multi(Mat015):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'放射性物质的质量$M$（克）随时间$t$（年）呈指数衰减。\n这种衰减的图像显示在网格上。\n使用该图求出质量达到{round(float(self.k), 10)}克需要多少年。'
        self.description_arabic = f'تتناقص الكتلة، $M$ جرامًا، لمادة مشعة أسيًا مع الزمن $t$ بالسنوات.\nيُعرض التمثيل البياني لهذا الاضمحلال على الشبكة.\nاستخدم التمثيل البياني لإيجاد عدد السنوات اللازمة لوصول الكتلة إلى {round(float(self.k), 10)} جرامًا.'
        self.description_hindi = f'एक रेडियोधर्मी पदार्थ (radioactive substance) का द्रव्यमान (mass), $M$ ग्राम, समय $t$ वर्षों में घातीय रूप से घटता है।\nइस क्षय का ग्राफ ग्रिड पर दिखाया गया है।\nग्राफ का उपयोग करके पता लगाएँ कि द्रव्यमान को {round(float(self.k), 10)} ग्राम तक पहुँचने में कितने वर्ष लगते हैं।'
        self.description_kazakh = f'Радиоактивті заттың массасы, $M$ грамм, $t$ жыл уақыт ішінде экспоненциалды түрде кемиді.\nБұл ыдыраудың графигі торда көрсетілген.\nГрафикті пайдалана отырып, массасы {round(float(self.k), 10)} граммға жетуі үшін қанша жыл қажет екенін табыңыз.'
        self.description_swahili = f'Masi, $M$ gramu, ya dutu nururifu inapungua kwa kielelezo kulingana na muda $t$ katika miaka.\nGrafu ya mivunjiko hii imeonyeshwa kwenye gridi.\nTumia grafu kutafuta ni miaka mingapi inahitajika ili masi ifikie gramu {round(float(self.k), 10)}.'

class Mat016_multi(Mat016):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个三次函数的图像，已标出其截距。图中画了一条垂直线。根据图中的信息，确定标记为$(k, ?)$的交点处的$y$值。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة تكعيبية مع تحديد نقاط تقاطعها. تم رسم خط عمودي. بناءً على المعلومات الواردة في التمثيل البياني، أوجد قيمة $y$ عند نقطة التقاطع $(k, ?)$.'
        self.description_hindi = f'चित्र में एक त्रिघात फलन (cubic function) का ग्राफ दर्शाया गया है, जिसके अंतःखंडों (intercepts) को अंकित किया गया है। एक ऊर्ध्वाधर रेखा खींची गई है। ग्राफ में दी गई जानकारी के आधार पर, अंकित प्रतिच्छेदन बिंदु $(k, ?)$ पर $y$ का मान ज्ञात कीजिए।'
        self.description_kazakh = f'Суретте қиылысу нүктелері белгіленген кубтық функцияның графигі көрсетілген. Тік сызық жүргізілген. Графиктегі ақпаратқа сүйене отырып, $(k, ?)$ деп белгіленген қиылысу нүктесіндегі $y$ мәнін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya kazi ya kikiu yenye makutano yake yaliyowekewa lebo. Mstari wa wima umechorwa. Kulingana na taarifa kwenye grafu, tambua thamani ya $y$ katika nukta ya makutano iliyowekewa lebo $(k, ?)$.'

class Mat017_multi(Mat017):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了形式为$y = \\frac{k}{x - p} + q$的反比例函数图像。垂直和水平渐近线显示为虚线，并且给出了曲线上的一点。根据图表提供的信息，求出指示点处缺失的$y$值。'
        self.description_arabic = 'يوضح الشكل التمثيل البياني لدالة مقلوب على الصورة $y = \\frac{k}{x - p} + q$. تظهر الخطوط التقاربية الرأسية والأفقية كخطوط متقطعة، وقد أُعطيت نقطة واحدة على المنحنى. بناءً على المعلومات المقدمة في الشكل، أوجد قيمة $y$ المجهولة عند النقطة المشار إليها.'
        self.description_hindi = 'चित्र में व्युत्क्रम फलन (reciprocal function) $y = \\frac{k}{x - p} + q$ का ग्राफ दर्शाया गया है। ऊर्ध्वाधर और क्षैतिज अनंतस्पर्शी (asymptotes) रेखाओं को खंडित रेखाओं के रूप में दर्शाया गया है, और वक्र पर एक बिंदु दिया गया है। आरेख में दी गई जानकारी के आधार पर, इंगित बिंदु पर लुप्त $y$-value ज्ञात कीजिए।'
        self.description_kazakh = 'Суретте $y = \\frac{k}{x - p} + q$ түріндегі кері пропорционалдық функциясының графигі көрсетілген. Тік және көлденең асимптоталар үзік сызықтармен көрсетілген және қисықта бір нүкте берілген. Диаграммада берілген ақпаратқа сүйене отырып, көрсетілген нүктедегі белгісіз $y$ мәнін табыңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha grafu ya kazi kinyume katika muundo wa $y = \\frac{k}{x - p} + q$. Asimptoti za wima na mlalo zinaonyeshwa kama mistari ya dashi, na nukta moja kwenye mchirizi imetolewa. Kulingana na taarifa kwenye mchoro, tafuta thamani ya $y$ inayokosekana katika nukta iliyoonyeshwa.'

class Mat018_multi(Mat018):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个三次函数的图像。点$M$是该曲线的局部{self.m_type}。根据该图，试求出$M$的{self.ask_for}坐标。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة تكعيبية. النقطة $M$ تمثل {self.m_type} محليًا للمنحنى. بناءً على الشكل، أوجد إحداثي {self.ask_for} للنقطة $M$.'
        self.description_hindi = f'चित्र एक त्रिघात फलन (cubic function) का ग्राफ दिखाता है। बिंदु $M$ वक्र का एक स्थानीय (local) {self.m_type} है। चित्र के आधार पर, $M$ का {self.ask_for}-निर्देशांक ज्ञात करें।'
        self.description_kazakh = f'Диаграммада кубтық функцияның графигі көрсетілген. $M$ нүктесі - қисықтың локальді {self.m_type}. Суреттегі ақпаратқа сүйене отырып, $M$ нүктесінің {self.ask_for}-координатасын табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya kazi ya kikiu. Nukta $M$ ni {self.m_type} ya ndani ya mchirizi. Kulingana na kielelezo, tafuta koatuneti ya {self.ask_for} ya $M$.'

class Mat019_multi(Mat019):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个三次函数的图像以及在点$M$处与曲线相切的切线$l$，如图所示。根据该图，试求出斜率$m$的值。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة تكعيبية وخطًا مماسًا $l$ يلامس المنحنى عند النقطة $M$ كما هو موضح في الشكل. بناءً على الشكل، أوجد قيمة الميل $m$.'
        self.description_hindi = f'चित्र एक त्रिघात फलन (cubic function) का ग्राफ और चित्र में दिखाए गए अनुसार बिंदु $M$ पर वक्र को छूने वाली एक स्पर्श रेखा $l$ को दिखाता है। चित्र के आधार पर, प्रवणता (gradient) $m$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада кубтық функцияның графигі және суретте көрсетілгендей $M$ нүктесінде қисыққа жанасатын $l$ жанамасы көрсетілген. Суреттегі ақпаратқа сүйене отырып, $m$ градиентінің мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya kazi ya kikiu na mstari wa tanjiti $l$ unaogusa mchirizi katika nukta $M$ kama inavyoonyeshwa kwenye kielelezo. Kulingana na kielelezo, tafuta thamani ya mwinuko $m$.'

class Mat020_multi(Mat020):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了抛物线$g(x)$的图像以及与曲线交于$A$、$B$两点的割线。曲线上存在一点$T$，该点处的切线平行于割线$AB$。根据图中提供的信息，求出点$T$的{self.ask_for}坐标。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني للقطع المكافئ $g(x)$ وخطًا قاطعًا يقطع المنحنى عند النقطتين $A$ و $B$. توجد نقطة $T$ على المنحنى يكون عندها المماس موازيًا للقاطع $AB$. بناءً على المعلومات المقدمة في الشكل، أوجد إحداثي {self.ask_for} للنقطة $T$.'
        self.description_hindi = f'चित्र परवलय $g(x)$ का ग्राफ और वक्र को बिंदु $A$ और $B$ पर प्रतिच्छेद करने वाली एक छेदक रेखा (secant line) दिखाता है। वक्र पर एक बिंदु $T$ है जहां स्पर्श रेखा छेदक $AB$ के समानांतर है। चित्र में दी गई जानकारी के आधार पर, बिंदु $T$ का {self.ask_for}-निर्देशांक ज्ञात करें।'
        self.description_kazakh = f'Диаграммада $g(x)$ параболасының графигі және қисықты $A$ және $B$ нүктелерінде қиып өтетін қиюшы сызық көрсетілген. Қисық бойында жанама сызық $AB$ қиюшысына параллель болатын $T$ нүктесі бар. Суретте берілген ақпаратқа сүйене отырып, $T$ нүктесінің {self.ask_for}-координатасын табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya parabola $g(x)$ na mstari wa sekanti unaokata mchirizi katika nukta $A$ na $B$. Kuna nukta $T$ kwenye mchirizi ambapo mstari wa tanjiti ni sambamba na sekanti $AB$. Kulingana na taarifa iliyotolewa kwenye kielelezo, tafuta koatuneti ya {self.ask_for} ya nukta $T$.'

class Mat021_multi(Mat021):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图将二次函数$f(x)$的图像显示为实线，将其反函数$f^{{-1}}(x)$显示为虚线。根据图中提供的坐标，试求出$f^{{-1}}({self.k})$的值。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة تربيعية $f(x)$ بخط متصل، ودالتها العكسية $f^{{-1}}(x)$ بخط متقطع. بناءً على الإحداثيات المقدمة في الشكل، أوجد قيمة $f^{{-1}}({self.k})$.'
        self.description_hindi = f'चित्र एक द्विघात फलन (quadratic function) $f(x)$ का ग्राफ एक ठोस रेखा के रूप में और इसके प्रतिलोम फलन (inverse function) $f^{{-1}}(x)$ को एक खंडित रेखा के रूप में दिखाता है। आरेख में दिए गए निर्देशांकों के आधार पर, $f^{{-1}}({self.k})$ का मान ज्ञात करें।'
        self.description_kazakh = f'Суретте тұтас сызықпен $f(x)$ квадраттық функциясының графигі және үзік сызықпен оның $f^{{-1}}(x)$ кері функциясы көрсетілген. Диаграммада берілген координаталарға сүйене отырып, $f^{{-1}}({self.k})$ мәнін табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya kazi ya kipeo cha pili $f(x)$ kama mstari mnyofu na kazi kinyume yake $f^{{-1}}(x)$ kama mstari wa dashi. Kulingana na koatuneti zilizotolewa kwenye mchoro, tafuta thamani ya $f^{{-1}}({self.k})$.'

class Mat022_multi(Mat022):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一家工厂使用两阶段处理系统。根据原材料的输入和每台机器的功能，确定最终产品的体积（单位：升）。'
        self.description_arabic = 'يستخدم مصنع نظام معالجة من مرحلتين كما هو موضح في الشكل. بناءً على مدخلات المواد الخام ووظائف كل آلة، أوجد قيمة الناتج النهائي باللتر.'
        self.description_hindi = 'एक कारखाना आरेख में दिखाए गए अनुसार दो-चरणीय प्रसंस्करण प्रणाली का उपयोग करता है। कच्चे माल के इनपुट और प्रत्येक मशीन के कार्यों के आधार पर, अंतिम उत्पाद का मान लीटर में निर्धारित करें।'
        self.description_kazakh = 'Зауыт диаграммада көрсетілгендей екі кезеңді өңдеу жүйесін пайдаланады. Шикізаттың кірісіне және әр машинаның функцияларына сүйене отырып, соңғы өнімнің мәнін литрмен анықтаңыз.'
        self.description_swahili = 'Kiwanda kinatumia mfumo wa uchakataji wa hatua mbili kama unavyoonyeshwa kwenye mchoro. Kulingana na ingizo la malighafi na kazi ya kila mashine, bainisha kiasi cha bidhaa ya mwisho katika lita.'

class Mat023_multi(Mat023):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了经过点$P$的反比例函数$f(x)$的图像。根据图表提供的信息，确定{self.target_text}。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة مقلوب $f(x)$ التي تمر بالنقطة $P$. بناءً على المعلومات المقدمة في الشكل، أوجد {self.target_text}.'
        self.description_hindi = f'चित्र एक व्युत्क्रम फलन (reciprocal function) $f(x)$ का ग्राफ दिखाता है जो बिंदु $P$ से होकर गुजरता है। आरेख में दी गई जानकारी के आधार पर, {self.target_text} निर्धारित करें।'
        self.description_kazakh = f'Суретте $P$ нүктесі арқылы өтетін $f(x)$ кері пропорционалдық функциясының графигі көрсетілген. Диаграммада берілген ақпаратқа сүйене отырып, {self.target_text} анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya kazi kinyume $f(x)$ inayopita katika nukta $P$. Kulingana na taarifa zilizotolewa kwenye mchoro, bainisha {self.target_text}.'

class Mat024_multi(Mat024):
    def __init__(self):
        super().__init__()
        self.description_chinese = "如图所示，一个机器人沿网格线从点$D$移动到点$E$。机器人的路径由水平和垂直步数组成，并且它单调移动（从不远离其目的地）。根据图表提供的坐标，求机器人移动的总距离。"
        self.description_arabic = "يتحرك روبوت من النقطة $D$ إلى النقطة $E$ على طول خطوط الشبكة كما هو موضح في الشكل. يتكون مسار الروبوت من خطوات أفقية ورأسية، ويتحرك بشكل رتيب (أي لا يبتعد عن وجهته). بناءً على الإحداثيات المقدمة في الشكل، أوجد المسافة الكلية التي يقطعها الروبوت."
        self.description_hindi = "एक रोबोट चित्र में दिखाए अनुसार ग्रिड लाइनों के साथ बिंदु $D$ से बिंदु $E$ तक यात्रा करता है। रोबोट के पथ में क्षैतिज और ऊर्ध्वाधर कदम शामिल हैं, और यह एकदिष्ट (monotonically) रूप से चलता है (यह कभी भी अपने गंतव्य से दूर नहीं जाता है)। आरेख में दिए गए निर्देशांकों के आधार पर, रोबोट द्वारा तय की गई कुल दूरी ज्ञात करें।"
        self.description_kazakh = "Робот суретте көрсетілгендей тор сызықтары бойымен $D$ нүктесінен $E$ нүктесіне дейін жүреді. Роботтың жолы көлденең және тік қадамдардан тұрады және ол монотонды түрде қозғалады (ол ешқашан барар жерінен алыстамайды). Диаграммада берілген координаталарға сүйене отырып, роботтың жүріп өткен жалпы қашықтығын табыңыз."
        self.description_swahili = 'Roboti inasafiri kutoka nukta $D$ hadi nukta $E$ kufuata mistari ya gridi kama inavyoonyeshwa kwenye kielelezo. Njia ya roboti inajumuisha hatua za mlalo na wima, na inasonga mfululizo (haisongi mbali na shabaha yake). Kulingana na koatuneti zilizotolewa kwenye mchoro, tafuta jumla ya umbali uliosafiriwa na roboti.'

class Mat025_multi(Mat025):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个直角三角形$MNO$。点$O$位于原点$(0,0)$，点$N$位于$x$轴上。三角形$MNO$的面积为{self.area}平方单位。根据图中显示的坐标，计算线段$MO$的斜率。'
        self.description_arabic = f'يوضح الشكل مثلثًا قائم الزاوية $MNO$. تقع النقطة $O$ عند نقطة الأصل $(0,0)$ وتقع النقطة $N$ على المحور $x$. مساحة المثلث $MNO$ هي {self.area} وحدة مربعة. بناءً على الإحداثيات الموضحة في الشكل، احسب ميل القطعة المستقيمة $MO$.'
        self.description_hindi = f'चित्र एक समकोण त्रिभुज $MNO$ दिखाता है। बिंदु $O$ मूल बिंदु $(0,0)$ पर है और बिंदु $N$ $x$-अक्ष पर है। त्रिभुज $MNO$ का क्षेत्रफल {self.area} वर्ग इकाई है। चित्र में दिखाए गए निर्देशांकों के आधार पर, रेखाखंड $MO$ की प्रवणता की गणना करें।'
        self.description_kazakh = f'Диаграммада тік бұрышты $MNO$ үшбұрышы көрсетілген. $O$ нүктесі координаталар басында $(0,0)$ орналасқан және $N$ нүктесі $x$ бойында жатыр. $MNO$ үшбұрышының ауданы - {self.area} квадрат бірлік. Суретте көрсетілген координаталарға сүйене отырып, $MO$ кесіндісінің градиентін есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha pembetatu mraba $MNO$. Nukta $O$ iko kwenye asili $(0,0)$ na nukta $N$ iko kwenye mhimili wa $x$. Eneo la pembetatu $MNO$ ni {self.area} kizio cha mraba. Kulingana na koatuneti zilizoonyeshwa kwenye kielelezo, kokotoa mwinuko wa kipande cha mstari $MO$.'

class Mat026_multi(Mat026):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中显示了坐标网格上的三个共线点 $P$、$Q$ 和 $R$。点 $P$ 的 $x$ 坐标 $k$ 未知。根据图中所示的坐标，计算$k$的值。'
        self.description_arabic = 'يوضح الشكل ثلاث نقاط على استقامة واحدة $P$ و $Q$ و $R$ على شبكة إحداثيات. للنقطة $P$ إحداثي $x$ غير معلوم مقداره $k$. بناءً على الإحداثيات الموضحة، احسب قيمة $k$.'
        self.description_hindi = 'दिए गए चित्र में निर्देशांक ग्रिड पर तीन संरेख बिंदु $P$, $Q$ और $R$ दर्शाए गए हैं। बिंदु $P$ का x-निर्देशांक $k$ अज्ञात है। दिए गए निर्देशांकों के आधार पर $k$ का मान ज्ञात कीजिए।'
        self.description_kazakh = 'Диаграммада координаталық тордағы үш коллинеар $P$, $Q$, $R$ нүктелері көрсетілген. $P$ нүктесінің $x$ координатасі белгісіз, $k$. Көрсетілген координаталарға сүйене отырып, $k$ мәнін есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha nukta tatu mstari $P$, $Q$, na $R$ kwenye gridi ya koatuneti. Nukta $P$ ina koatuneti ya $x$ isiyojulikana, $k$. Kulingana na koatuneti zilizoonyeshwa, kokotoa thamani ya $k$.'

class Mat027_multi(Mat027):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了经过点$A$和$B$的直线$L_1$。直线$L_2$垂直于$L_1$，且与$L_1$在同一点与$y$轴相交。根据该图，计算直线$L_2$的斜率。'
        self.description_arabic = 'يوضح الشكل المستقيم $L_1$ المار بالنقطتين $A$ و $B$. المستقيم $L_2$ عمودي على $L_1$ ويقطع المحور $y$ عند نفس نقطة تقاطع $L_1$. بناءً على الشكل، احسب ميل المستقيم $L_2$.'
        self.description_hindi = 'चित्र में रेखा $L_1$ बिंदुओं $A$ और $B$ से होकर गुजरती है। रेखा $L_2$, $L_1$ पर लंबवत है और $y$-अक्ष को उसी बिंदु पर काटती है जहाँ $L_1$ काटती है। चित्र के आधार पर रेखा $L_2$ की प्रवणता ज्ञात कीजिए।'
        self.description_kazakh = 'Диаграммада $A$ және $B$ нүктелері арқылы өтетін $L_1$ түзуі көрсетілген. $L_2$ түзуі $L_1$-ге перпендикуляр және $y$ осін $L_1$ түзуімен бірдей нүктеде қиып өтеді. Суреттегі ақпаратқа сүйене отырып, $L_2$ түзуінің градиентін есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha mstari $L_1$ unaopita katika nukta $A$ na $B$. Mstari $L_2$ ni sulubi kwa $L_1$ na unakata mhimili wa $y$ katika nukta sawa na $L_1$. Kulingana na kielelezo, kokotoa mwinuko wa mstari $L_2$.'

class Mat028_multi(Mat028):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了绘制在坐标网格上的三角形$ABC$。该三角形的面积为${self.area}$平方单位。根据该图，计算$k$的值。'
        self.description_arabic = f'يوضح الشكل المثلث $ABC$ مرسومًا على شبكة إحداثيات. مساحة المثلث هي ${self.area}$ وحدة مربعة. بناءً على الشكل، أوجد قيمة $k$.'
        self.description_hindi = f'चित्र एक समन्वय ग्रिड पर बने त्रिभुज $ABC$ को दिखाता है। त्रिभुज का क्षेत्रफल ${self.area}$ वर्ग इकाई है। चित्र के आधार पर, $k$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада координаталық торда салынған $ABC$ үшбұрышы көрсетілген. Үшбұрыштың ауданы - ${self.area}$ квадрат бірлік. Суреттегі ақпаратқа сүйене отырып, $k$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha pembetatu $ABC$ iliyochorwa kwenye gridi ya koatuneti. Eneo la pembetatu ni ${self.area}$ kizio cha mraba. Kulingana na kielelezo, tafuta thamani ya $k$.'

class Mat029_multi(Mat029):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一条线段$AB$。点$C$是$AB$的中点，点$D$是$AC$的中点，点$E$是$DB$的中点。根据图中提供的坐标，计算线段$AE$的长度。'
        self.description_arabic = 'يوضح الشكل قطعة مستقيمة $AB$. النقطة $C$ هي منتصف $AB$، والنقطة $D$ هي منتصف $AC$، والنقطة $E$ هي منتصف $DB$. بناءً على الإحداثيات المقدمة في الشكل، احسب طول القطعة $AE$.'
        self.description_hindi = 'चित्र एक रेखाखंड $AB$ दिखाता है। बिंदु $C$, $AB$ का मध्यबिंदु है, बिंदु $D$, $AC$ का मध्यबिंदु है, और बिंदु $E$, $DB$ का मध्यबिंदु है। चित्र में दिए गए निर्देशांकों के आधार पर, रेखाखंड $AE$ की लंबाई की गणना करें।'
        self.description_kazakh = 'Диаграммада $AB$ кесіндісі көрсетілген. $C$ нүктесі - $AB$-ның ортасы, $D$ нүктесі - $AC$-ның ортасы, ал $E$ нүктесі - $DB$-ның ортасы. Суретте берілген координаталарға сүйене отырып, $AE$ кесіндісінің ұзындығын есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha kipande cha mstari $AB$. Nukta $C$ ni nuktamati ya $AB$, nukta $D$ ni nuktamati ya $AC$, na nukta $E$ ni nuktamati ya $DB$. Kulingana na koatuneti zilizotolewa kwenye kielelezo, kokotoa urefu wa kipande $AE$.'

class Mat030_multi(Mat030):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了坐标平面上的线段$PQ$。根据该图，求出$PQ$中点到{self.target_axis}的垂直距离。'
        self.description_arabic = f'يوضح الشكل قطعة مستقيمة $PQ$ على مستوى إحداثي. بناءً على الشكل، أوجد المسافة العمودية من منتصف $PQ$ إلى {self.target_axis}.'
        self.description_hindi = f'चित्र एक समन्वय तल पर एक रेखाखंड $PQ$ दिखाता है। चित्र के आधार पर, $PQ$ के मध्यबिंदु से {self.target_axis} की लंबवत दूरी ज्ञात करें।'
        self.description_kazakh = f'Диаграммада координаталық жазықтықтағы $PQ$ кесіндісі көрсетілген. Суреттегі ақпаратқа сүйене отырып, $PQ$ ортасынан {self.target_axis} перпендикуляр қашықтықты табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha kipande cha mstari $PQ$ kwenye bapa ya koatuneti. Kulingana na kielelezo, tafuta umbali sulubi kutoka kwenye nuktamati ya $PQ$ hadi kwenye {self.target_axis}.'

class Mat031_multi(Mat031):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一条直线的图像。根据图表提供的信息，求出$y$截距$c$的值。'
        self.description_arabic = 'يوضح الشكل التمثيل البياني لخط مستقيم. بناءً على المعلومات المقدمة في الشكل، أوجد قيمة نقطة التقاطع مع المحور $y$، $c$.'
        self.description_hindi = 'चित्र एक सीधी रेखा का ग्राफ दिखाता है। चित्र में दी गई जानकारी के आधार पर, $y$-intercept, $c$ का मान ज्ञात करें।'
        self.description_kazakh = 'Суретте түзу сызықтың графигі көрсетілген. Диаграммада берілген ақпаратқа сүйене отырып, $y$-осімен қиылысу нүктесінің, $c$ мәнін табыңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha grafu ya mstari ulionyooka. Kulingana na taarifa zilizotolewa kwenye mchoro, tafuta thamani ya kikatwa cha $y$, $c$.'

class Mat032_multi(Mat032):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'直线L显示在网格上。求直线L的方程，形式为y = mx + c。'
        self.description_arabic = f'يوضح الشكل الخط $L$ على الشبكة. أوجد معادلة الخط $L$ على الصورة y = mx + c.'
        self.description_hindi = f'ग्रिड पर रेखा L दिखाई गई है। y = mx + c के रूप में रेखा L का समीकरण ज्ञात करें।'
        self.description_kazakh = f'Торда L түзуі көрсетілген. L түзуінің теңдеуін y = mx + c түрінде табыңыз.'
        self.description_swahili = f'Mstari $L$ unaonyeshwa kwenye gridi. Tafuta mlinganyo wa mstari $L$ katika muundo wa $y = mx + c$.'

class Mat033_multi(Mat033):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一条直线$L$和一条方程为${self.line_m_eq}$的虚线$M$。如图所示，求交点的${self.find_coord}$坐标。'
        self.description_arabic = f'يوضح الشكل خطًا مستقيمًا $L$ وخطًا متقطعًا $M$ معادلته ${self.line_m_eq}$. كما هو موضح في الشكل، أوجد الإحداثي ${self.find_coord}$ لنقطة التقاطع.'
        self.description_hindi = f'चित्र एक सीधी रेखा $L$ और समीकरण ${self.line_m_eq}$ के साथ एक खंडित रेखा $M$ प्रदर्शित करता है। जैसा कि चित्र में दिखाया गया है, प्रतिच्छेदन बिंदु का ${self.find_coord}$-निर्देशांक ज्ञात करें।'
        self.description_kazakh = f'Суретте $L$ түзу сызығы және теңдеуі ${self.line_m_eq}$ болатын $M$ үзік сызығы көрсетілген. Суретте көрсетілгендей, қиылысу нүктесінің ${self.find_coord}$-координатасын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mstari ulionyooka $L$ na mstari wa dashi $M$ wenye mlinganyo ${self.line_m_eq}$. Kama inavyoonyeshwa kwenye kielelezo, tafuta koatuneti ya ${self.find_coord}$ ya nukta ya makutano.'

class Mat034_multi(Mat034):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了两条平行线$L_1$和$L_2$。根据图表提供的信息，求出$L_2$上当{self.given_var}坐标为{self.const_val}时该点的{self.target_var}坐标。'
        self.description_arabic = f'يوضح الشكل خطين متوازيين، $L_1$ و $L_2$. بناءً على المعلومات المقدمة في الشكل، أوجد إحداثي {self.target_var} للنقطة على $L_2$ حيث يكون إحداثي {self.given_var} مساويًا لـ {self.const_val}.'
        self.description_hindi = f'चित्र दो समानांतर रेखाएँ, $L_1$ और $L_2$ दिखाता है। आरेख में दी गई जानकारी के आधार पर, $L_2$ पर उस बिंदु का {self.target_var}-निर्देशांक ज्ञात करें जहाँ {self.given_var}-निर्देशांक {self.const_val} है।'
        self.description_kazakh = f'Суретте екі параллель $L_1$ және $L_2$ түзулері көрсетілген. Диаграммада берілген ақпаратқа сүйене отырып, $L_2$ түзуінің бойындағы {self.given_var}-координатасы {self.const_val} болатын нүктенің {self.target_var}-координатасын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mistari miwili sambamba, $L_1$ na $L_2$. Kulingana na taarifa zilizotolewa kwenye mchoro, tafuta koatuneti ya {self.target_var} ya nukta kwenye $L_2$ ambapo koatuneti ya {self.given_var} ni {self.const_val}.'

class Mat035_multi(Mat035):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了两条直线，直线$k$和直线$m$，其中直线$m$平行于直线$k$。根据图中提供的坐标和信息，求出当直线$m$上的{self.given_var}坐标为{self.const_val}时该点的{self.target_var}坐标。'
        self.description_arabic = f'يوضح الشكل خطين، $k$ و $m$، حيث إن الخط $m$ موازٍ للخط $k$. بناءً على الإحداثيات والمعلومات المقدمة في الشكل، أوجد إحداثي {self.target_var} على الخط $m$ عندما يكون إحداثي {self.given_var} مساويًا لـ {self.const_val}.'
        self.description_hindi = f'चित्र दो रेखाएँ, रेखा $k$ और रेखा $m$ दिखाता है, जहाँ रेखा $m$ रेखा $k$ के समानांतर है। आरेख में दिए गए निर्देशांकों और जानकारी के आधार पर, जब {self.given_var}-निर्देशांक {self.const_val} हो तो रेखा $m$ पर {self.target_var}-निर्देशांक ज्ञात करें।'
        self.description_kazakh = f'Суретте $k$ және $m$ екі түзуі көрсетілген, мұндағы $m$ түзуі $k$ түзуіне параллель. Диаграммада берілген координаталар мен ақпаратқа сүйене отырып, $m$ түзуінің бойындағы {self.given_var}-координатасы {self.const_val} болған кездегі {self.target_var}-координатасын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mistari miwili, mstari $k$ na mstari $m$, ambapo mstari $m$ ni sambamba na mstari $k$. Kulingana na koatuneti na taarifa zilizotolewa kwenye mchoro, tafuta koatuneti ya {self.target_var} kwenye mstari $m$ wakati koatuneti ya {self.given_var} ni {self.const_val}.'

class Mat036_multi(Mat036):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，直线$M$垂直于直线$L$。求直线$M$与直线${self.given_line}$交点的{self.find_var}坐标。'
        self.description_arabic = f'كما هو موضح في الشكل، الخط $M$ عمودي على الخط $L$. أوجد إحداثي {self.find_var} للنقطة التي يتقاطع فيها الخط $M$ مع الخط ${self.given_line}$.'
        self.description_hindi = f'जैसा कि आरेख में दिखाया गया है, रेखा $M$ रेखा $L$ के लंबवत है। उस बिंदु का {self.find_var}-निर्देशांक ज्ञात करें जहाँ रेखा $M$ रेखा ${self.given_line}$ को प्रतिच्छेद करती है।'
        self.description_kazakh = f'Диаграммада көрсетілгендей, $M$ түзуі $L$ түзуіне перпендикуляр. $M$ түзуі ${self.given_line}$ түзуін қиып өтетін нүктенің {self.find_var}-координатасын табыңыз.'
        self.description_swahili = f'Kama inavyoonyeshwa kwenye mchoro, mstari $M$ ni sulubi kwa mstari $L$. Tafuta koatuneti ya {self.find_var} ya nukta ambapo mstari $M$ unakata mstari ${self.given_line}$.'

class Mat037_multi(Mat037):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了直线$L$和直线$P$，其中直线$P$垂直于直线$L$。根据图表提供的坐标，求出直线$P$上当{self.given_var}坐标为{self.const_val}时该点的{self.target_var}坐标。'
        self.description_arabic = f'يوضح الشكل الخط $L$ والخط $P$، حيث إن الخط $P$ عمودي على الخط $L$. بناءً على الإحداثيات المقدمة في الشكل، أوجد إحداثي {self.target_var} للنقطة على الخط $P$ حيث يكون إحداثي {self.given_var} مساويًا لـ {self.const_val}.'
        self.description_hindi = f'चित्र रेखा $L$ और रेखा $P$ दिखाता है, जहाँ रेखा $P$ रेखा $L$ के लंबवत है। आरेख में दिए गए निर्देशांकों के आधार पर, रेखा $P$ पर उस बिंदु का {self.target_var}-निर्देशांक ज्ञात करें जहाँ {self.given_var}-निर्देशांक {self.const_val} है।'
        self.description_kazakh = f'Суретте $L$ түзуі және $P$ түзуі көрсетілген, мұндағы $P$ түзуі $L$ түзуіне перпендикуляр. Диаграммада берілген координаталарға сүйене отырып, $P$ түзуінің бойындағы {self.given_var}-координатасы {self.const_val} болатын нүктенің {self.target_var}-координатасын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mstari $L$ na mstari $P$, ambapo mstari $P$ ni sulubi kwa mstari $L$. Kulingana na koatuneti zilizotolewa kwenye mchoro, tafuta koatuneti ya {self.target_var} ya nukta kwenye mstari $P$ ambapo koatuneti ya {self.given_var} ni {self.const_val}.'

class Mat038_multi(Mat038):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了两条相互垂直的直线，直线$k$和直线$l$，它们相交于点$C$。根据点$A$和$B$的坐标以及图中提供的方程，求三角形$ABC$的面积。'
        self.description_arabic = 'يوضح الشكل خطين متعامدين، $k$ و $l$، يتقاطعان عند النقطة $C$. بناءً على إحداثيات النقطتين $A$ و $B$ والمعادلات المقدمة في الشكل، أوجد مساحة المثلث $ABC$.'
        self.description_hindi = 'चित्र दो लंबवत रेखाएँ, रेखा $k$ और रेखा $l$ दिखाता है, जो एक बिंदु $C$ पर प्रतिच्छेद करती हैं। आरेख में दिए गए बिंदुओं $A$ और $B$ के निर्देशांकों और समीकरणों के आधार पर, त्रिभुज $ABC$ का क्षेत्रफल ज्ञात करें।'
        self.description_kazakh = 'Суретте $C$ нүктесінде қиылысатын екі перпендикуляр $k$ және $l$ түзулері көрсетілген. $A$ және $B$ нүктелерінің координаталарына және диаграммада берілген теңдеулерге сүйене отырып, $ABC$ үшбұрышының ауданын табыңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha mistari miwili sulubi, mstari $k$ na mstari $l$, inayokutana katika nukta $C$. Kulingana na koatuneti za nukta $A$ na $B$ na milinganyo iliyotolewa kwenye mchoro, tafuta eneo la pembetatu $ABC$.'

class Mat039_multi(Mat039):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'矩形$A$与矩形$B$在数学上相似。计算$x$的值。'
        self.description_arabic = f'المستطيل $A$ مشابه للمستطيل $B$ رياضيًا. أوجد قيمة $x$.'
        self.description_hindi = f'आयत $A$ गणितीय रूप से आयत $B$ के समरूप (similar) है। $x$ का मान ज्ञात करें।'
        self.description_kazakh = f'$A$ тіктөртбұрышы $B$ тіктөртбұрышына математикалық тұрғыдан ұқсас. $x$ мәнін есептеңіз.'
        self.description_swahili = f'Mstatili $A$ una ushabaha wa kihisabati na mstatili $B$. Kokotoa thamani ya $x$.'

class Mat040_multi(Mat040):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'立体图形 $A$ 在数学上与立体图形 $B$ 相似。图示显示了这两个立体图形的高度和表面积（$S_A$ 和 $S_B$）。计算立体$B$的高度$H$。'
        self.description_arabic = f'المجسم $A$ مشابه للمجسم $B$ رياضيًا. يوضح الشكل الارتفاعات ومساحات السطح ($S_A$ و $S_B$) لكلا المجسمين. احسب الارتفاع $H$ للمجسم $B$.'
        self.description_hindi = f'ठोस $A$ गणितीय रूप से ठोस $B$ के समान है। आरेख में दोनों ठोसों की ऊँचाई और पृष्ठीय क्षेत्रफल ($S_A$ और $S_B$) दर्शाए गए हैं। ठोस $B$ की ऊँचाई $H$ ज्ञात कीजिए।'
        self.description_kazakh = f'$A$ денесі $B$ денесіне математикалық тұрғыдан ұқсас. Диаграммада екі дененің биіктігі мен бетінің ауданы ($S_A$ және $S_B$) көрсетілген. $B$ денесінің $H$ биіктігін есептеңіз.'
        self.description_swahili = f'Umbo thabiti $A$ lina ushabaha wa kihisabati na umbo thabiti $B$. Kielelezo kinaonyesha kimo na eneo la uso ($S_A$ na $S_B$) kwa maumbo thabiti yote mawili. Kokotoa kimo, $H$, cha umbo thabiti $B$.'

class Mat041_multi(Mat041):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'立体$A$和立体$B$在数学上相似。该图显示了两个立体的高度和体积（$V_A$和$V_B$）。计算立体$B$的体积$V_B$。'
        self.description_arabic = f'المجسم $A$ والمجسم $B$ متشابهان رياضيًا. يوضح الشكل الارتفاعات والأحجام ($V_A$ و $V_B$) لكلا المجسمين. احسب الحجم $V_B$ للمجسم $B$.'
        self.description_hindi = f'ठोस $A$ और ठोस $B$ गणितीय रूप से समरूप हैं। आरेख दोनों ठोसों की ऊँचाई और आयतन ($V_A$ और $V_B$) दिखाता है। ठोस $B$ के आयतन, $V_B$, की गणना करें।'
        self.description_kazakh = f'$A$ денесі және $B$ денесі математикалық тұрғыдан ұқсас. Диаграммада екі дененің биіктіктері мен көлемдері ($V_A$ және $V_B$) көрсетілген. $B$ денесінің $V_B$ көлемін есептеңіз.'
        self.description_swahili = f'Umbo thabiti $A$ na umbo thabiti $B$ yana ushabaha wa kihisabati. Mchoro unaonyesha vimo na ujazo ($V_A$ na $V_B$) kwa maumbo thabiti yote mawili. Kokotoa ujazo, $V_B$, wa umbo thabiti $B$.'

class Mat042_multi(Mat042):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个四边等长的四边形。计算$a$的值。'
        self.description_arabic = f'يوضح الشكل شكلًا رباعيًا أضلاعه متساوية في الطول. أوجد قيمة $a$.'
        self.description_hindi = f'चित्र समान लंबाई की भुजाओं वाला एक चतुर्भुज (quadrilateral) दिखाता है। $a$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада қабырғаларының ұзындығы бірдей төртбұрыш көрсетілген. $a$ мәнін есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha pembenne yenye pande zenye urefu sawa. Kokotoa thamani ya $a$.'

class Mat043_multi(Mat043):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'$BDC$是一条直线，$AB = AC$，角$ABD = {round(self.angle_B, 2)}^\\circ$，角$ADC = {round(self.angle_ADC, 2)}^\\circ$。 \\\\ 计算角$DAC$。'
        self.description_arabic = f'$BDC$ خط مستقيم، و $AB = AC$، والزاوية $ABD = {round(self.angle_B, 2)}^\\circ$ والزاوية $ADC = {round(self.angle_ADC, 2)}^\\circ$. \\\\ أوجد الزاوية $DAC$.'
        self.description_hindi = f'$BDC$ एक सीधी रेखा है, $AB = AC$, कोण $ABD = {round(self.angle_B, 2)}^\\circ$ और कोण $ADC = {round(self.angle_ADC, 2)}^\\circ$ है। \\\\ कोण $DAC$ ज्ञात करें।'
        self.description_kazakh = f'$BDC$ - түзу сызық, $AB = AC$, $ABD$ бұрышы = {round(self.angle_B, 2)}^\\circ$ және $ADC$ бұрышы = {round(self.angle_ADC, 2)}^\\circ$. \\\\ $DAC$ бұрышын есептеңіз.'
        self.description_swahili = f'$BDC$ ni mstari ulionyooka, $AB = AC$, pembe $ABD = {round(self.angle_B, 2)}^\\circ$ na pembe $ADC = {round(self.angle_ADC, 2)}^\\circ$. Kokotoa pembe $DAC$.'

class Mat044_multi(Mat044):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'直线$AB$和$CD$平行。$EF$和$EG$是直线。在$EF$和$CD$交点处形成的角是{self.angle_top:.2f}°。求$a$的值。'
        self.description_arabic = f'الخطان $AB$ و $CD$ متوازيان. $EF$ و $EG$ خطان مستقيمان. الزاوية المتكونة عند تقاطع $EF$ و $CD$ هي {self.angle_top:.2f}°. أوجد قيمة $a$.'
        self.description_hindi = f'रेखाएँ $AB$ और $CD$ समानांतर हैं। $EF$ और $EG$ सीधी रेखाएँ हैं। $EF$ और $CD$ के प्रतिच्छेदन पर बना कोण {self.angle_top:.2f}° है। $a$ का मान ज्ञात करें।'
        self.description_kazakh = f'$AB$ және $CD$ түзулері параллель. $EF$ және $EG$ - түзу сызықтар. $EF$ пен $CD$ қиылысуында пайда болған бұрыш {self.angle_top:.2f}° тең. $a$ мәнін табыңыз.'
        self.description_swahili = f'Mistari $AB$ na $CD$ ni sambamba. $EF$ na $EG$ ni mistari ilionyooka. Pembe inayoundwa kwenye makutano ya $EF$ na $CD$ ni {self.angle_top:.2f}^\\circ$. Tafuta thamani ya $a$.'

class Mat045_multi(Mat045):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了{self.shape_name}的内角，用$x$表示。求$x$的值。'
        self.description_arabic = f'يوضح الشكل الزوايا الداخلية لـ {self.shape_name} مكتوبة بدلالة $x$. أوجد قيمة $x$.'
        self.description_hindi = f'चित्र एक {self.shape_name} के आंतरिक कोणों को दिखाता है, जिन्हें $x$ के पदों में लिखा गया है। $x$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада $x$ арқылы жазылған {self.shape_name} ішкі бұрыштары көрсетілген. $x$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha pembe za ndani za {self.shape_name}, zilizoelezwa kwa mtajo wa $x$. Tafuta thamani ya $x$.'

class Mat046_multi(Mat046):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个圆内接四边形$ABCD$。对角线$BD$和$AC$相交。角$BAD = {self.angle_bad}^\\circ$，角$BCA = {self.angle_bca}^\\circ$。求角$ABD$的值。'
        self.description_arabic = f'يوضح الشكل شكلًا رباعيًا دائريًا $ABCD$. يتقاطع القطران $BD$ و $AC$. الزاوية $BAD = {self.angle_bad}^\\circ$ والزاوية $BCA = {self.angle_bca}^\\circ$. أوجد قيمة الزاوية $ABD$.'
        self.description_hindi = f'चित्र एक चक्रीय चतुर्भुज (cyclic quadrilateral) $ABCD$ दिखाता है। विकर्ण $BD$ और $AC$ प्रतिच्छेद करते हैं। कोण $BAD = {self.angle_bad}^\\circ$ और कोण $BCA = {self.angle_bca}^\\circ$ है। कोण $ABD$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада $ABCD$ іштей сызылған төртбұрышы көрсетілген. $BD$ және $AC$ диагональдары қиылысады. $BAD$ бұрышы = {self.angle_bad}^\\circ$ және $BCA$ бұрышы = {self.angle_bca}^\\circ$. $ABD$ бұрышының мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha pembenne mduara $ABCD$. Nyalalo $BD$ na $AC$ zinapishana. Pembe $BAD = {self.angle_bad}^\\circ$ na pembe $BCA = {self.angle_bca}^\\circ$. Tafuta thamani ya pembe $ABD$.'

class Mat047_multi(Mat047):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个圆心为$O$的圆。$P$和$S$是圆上的点。$POR$是一条直线。$QRST$是圆在点$S$处的切线。角$OPS = {self.angle_ops}^\\circ$。求$y$的值。'
        self.description_arabic = f'يوضح الشكل دائرة مركزها $O$. النقطتان $P$ و $S$ تقعان على الدائرة. $POR$ خط مستقيم. $QRST$ مماس للدائرة عند $S$. الزاوية $OPS = {self.angle_ops}^\\circ$. أوجد قيمة $y$.'
        self.description_hindi = f'चित्र केंद्र $O$ वाला एक वृत्त दिखाता है। $P$ और $S$ वृत्त पर बिंदु हैं। $POR$ एक सीधी रेखा है। $QRST$ बिंदु $S$ पर वृत्त की स्पर्श रेखा है। कोण $OPS = {self.angle_ops}^\\circ$ है। $y$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. $P$ және $S$ - шеңбер бойындағы нүктелер. $POR$ - түзу сызық. $QRST$ - шеңберге $S$ нүктесінде жүргізілген жанама. $OPS$ бұрышы = {self.angle_ops}^\\circ$. $y$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha duara, kitovu $O$. $P$ na $S$ ni nukta kwenye duara. $POR$ ni mstari ulionyooka. $QRST$ ni tanjiti kwa duara kwenye $S$. Pembe $OPS = {self.angle_ops}^\\circ$. Tafuta thamani ya $y$.'

class Mat048_multi(Mat048):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个圆心为$O$的圆。$A$、$B$和$C$是圆上的三个点。角$ACO = {self.angle_aco}^\\circ$，角$BCO = {self.angle_bco}^\\circ$。求角$ABC$的值。'
        self.description_arabic = f'يوضح الشكل دائرة مركزها $O$. النقاط $A$ و $B$ و $C$ تقع على الدائرة. الزاوية $ACO = {self.angle_aco}^\\circ$ والزاوية $BCO = {self.angle_bco}^\\circ$. أوجد قيمة الزاوية $ABC$.'
        self.description_hindi = f'चित्र केंद्र $O$ वाला एक वृत्त दिखाता है। $A$, $B$ और $C$ वृत्त पर तीन बिंदु हैं। कोण $ACO = {self.angle_aco}^\\circ$ और कोण $BCO = {self.angle_bco}^\\circ$ है। कोण $ABC$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. $A$, $B$ және $C$ - шеңбер бойындағы үш нүкте. $ACO$ бұрышы = {self.angle_aco}^\\circ$ және $BCO$ бұрышы = {self.angle_bco}^\\circ$. $ABC$ бұрышының мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha duara, kitovu $O$. $A$, $B$ na $C$ ni nukta tatu kwenye duara. Pembe $ACO = {self.angle_aco}^\\circ$ na pembe $BCO = {self.angle_bco}^\\circ$. Tafuta thamani ya pembe $ABC$.'

class Mat049_multi(Mat049):
    def __init__(self):
        super().__init__()
        self.description_chinese = '点$A、B、C、D$和$E$位于一个圆上。$FG$是圆在点$C$处的切线。利用图中提供的信息，求角$DCG$的值。'
        self.description_arabic = 'تقع النقاط $A$ و $B$ و $C$ و $D$ و $E$ على دائرة. $FG$ مماس للدائرة عند $C$. باستخدام المعلومات المقدمة في الشكل، أوجد قيمة الزاوية $DCG$.'
        self.description_hindi = 'बिंदु $A, B, C, D$ और $E$ एक वृत्त पर स्थित हैं। $FG$ बिंदु $C$ पर वृत्त की स्पर्श रेखा है। आरेख में दी गई जानकारी का उपयोग करके, कोण $DCG$ का मान ज्ञात करें।'
        self.description_kazakh = ' $A, B, C, D$ және $E$ нүктелері шеңбер бойында жатыр. $FG$ - $C$ нүктесінде шеңберге жүргізілген жанама. Диаграммада берілген ақпаратты пайдалана отырып, $DCG$ бұрышының мәнін табыңыз.'
        self.description_swahili = 'Nukta $A, B, C, D$ na $E$ zipo kwenye duara. $FG$ ni tanjiti kwa duara kwenye $C$. Kwa kutumia taarifa zilizotolewa kwenye mchoro, tafuta thamani ya pembe $DCG$.'

class Mat050_multi(Mat050):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个圆心为$O$的圆。半径和弦$AB$的长度如图所示。计算从圆心到弦的最短距离。'
        self.description_arabic = f'يوضح الشكل دائرة مركزها $O$. نصف القطر والوتر $AB$ لهما أطوال كما هو موضح في الشكل. احسب أقصر مسافة من مركز الدائرة إلى الوتر.'
        self.description_hindi = f'चित्र केंद्र $O$ वाला एक वृत्त दिखाता है। त्रिज्या और जीवा (chord) $AB$ की लंबाई चित्र में दिखाए अनुसार है। वृत्त के केंद्र से जीवा तक की न्यूनतम दूरी की गणना करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. Радиус пен $AB$ хордасының ұзындықтары суретте көрсетілгендей. Шеңбер центрінен хордаға дейінгі ең қысқа қашықтықты есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha duara lenye kitovu $O$. Rediasi na kigwe $AB$ vina urefu kama inavyoonyeshwa kwenye picha. Kokotoa umbali mfupi zaidi kutoka kwenye kitovu cha duara hadi kwenye kigwe.'

class Mat051_multi(Mat051):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个圆心为$O$的圆。两条弦$AB$和$CD$的长度均为${round(self.c_len, 2)}$ cm。弦 $AB$ 到中心的距离为 ${round(self.d, 2)}$ cm。弦 $CD$ 到中心的距离为 $({self.expr.strip()})$ cm。求$x$的值。'
        self.description_arabic = f'يوضح الشكل دائرة مركزها $O$. الوتران $AB$ و $CD$، طول كل منهما ${round(self.c_len, 2)}$ سم. يبعد الوتر $AB$ مسافة ${round(self.d, 2)}$ سم عن المركز. المسافة من المركز إلى الوتر $CD$ هي $({self.expr.strip()})$ سم. أوجد قيمة $x$.'
        self.description_hindi = f'चित्र में केंद्र $O$ वाला एक वृत्त दर्शाया गया है। दो जीवाएँ $AB$ और $CD$ हैं, जिनमें से प्रत्येक की लंबाई ${round(self.c_len, 2)}$ cm है। जीवा $AB$ केंद्र से ${round(self.d, 2)}$ cm की दूरी पर है। केंद्र से जीवा $CD$ की दूरी $({self.expr.strip()})$ cm है। x का मान ज्ञात कीजिए।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. Екі $AB$ және $CD$ хордаларының әрқайсысының ұзындығы ${round(self.c_len, 2)}$ см. $AB$ хордасы центрден ${round(self.d, 2)}$ см қашықтықта орналасқан. Центрден $CD$ хордасына дейінгі қашықтық $({self.expr.strip()})$ см. $x$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha duara lenye kitovu $O$. Vigwe viwili, $AB$ na $CD$, kila kimoja kina urefu wa sm ${round(self.c_len, 2)}$. Kigwe $AB$ kipo umbali wa sm ${round(self.d, 2)}$ kutoka kwenye kitovu. Umbali kutoka kwenye kitovu hadi kwenye kigwe $CD$ ni sm $({self.expr.strip()})$. Tafuta thamani ya $x$.'

class Mat052_multi(Mat052):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个圆心为$O$的圆。$PA$和$PB$是从圆外一点$P$引出的圆的切线，分别切于点$A$和$B$。圆的半径为${self.radius}$ cm，且角$\\angle APB = {self.angle_apb}^\\circ$。计算切线$PA$的长度。'
        self.description_arabic = f'يوضح الشكل دائرة مركزها $O$. القطعتان $PA$ و $PB$ مماسان للدائرة من النقطة الخارجية $P$، وتمسان الدائرة عند $A$ و $B$. نصف قطر الدائرة هو ${self.radius}$ سم، والزاوية $\\angle APB = {self.angle_apb}^\\circ$. احسب طول المماس $PA$.'
        self.description_hindi = f'चित्र केंद्र $O$ वाला एक वृत्त दिखाता है। $PA$ और $PB$ एक बाहरी बिंदु $P$ से वृत्त पर स्पर्श रेखाएँ हैं, जो वृत्त को $A$ और $B$ पर छूती हैं। वृत्त की त्रिज्या ${self.radius}$ cm है और कोण $\\angle APB = {self.angle_apb}^\\circ$ है। स्पर्श रेखा $PA$ की लंबाई की गणना करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. $PA$ және $PB$ сыртқы $P$ нүктесінен шеңберді $A$ және $B$ нүктелерінде жанайтын жанамалар болып табылады. Шеңбердің радиусы ${self.radius}$ см және $\\angle APB = {self.angle_apb}^\\circ$ бұрышына тең. $PA$ жанамасының ұзындығын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha duara lenye kitovu $O$. $PA$ na $PB$ ni tanjiti kwa duara kutoka kwenye nukta ya nje $P$, zinazogusa duara kwenye $A$ na $B$. Rediasi ya duara ni sm ${self.radius}$ na pembe $\\angle APB = {self.angle_apb}^\\circ$. Kokotoa urefu wa tanjiti $PA$.'

class Mat053_multi(Mat053):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了三角形$ABC$的内切圆，切各边于$P$、$Q$和$R$。三角形$ABC$的周长为${self.perimeter:.1f}$ cm。已知切线段$AR = {self.x:.1f}$ cm 且 $BP = {self.y:.1f}$ cm，计算边$AC$的长度。'
        self.description_arabic = f'يوضح الشكل دائرة داخلة في المثلث $ABC$، وتمس الأضلاع عند $P$ و $Q$ و $R$. محيط المثلث $ABC$ هو ${self.perimeter:.1f}$ سم. علمًا بأن طولي المماسين $AR = {self.x:.1f}$ سم و $BP = {self.y:.1f}$ سم، احسب طول الضلع $AC$.'
        self.description_hindi = f'चित्र त्रिभुज $ABC$ के भीतर खुदा हुआ (inscribed) एक वृत्त दिखाता है, जो भुजाओं को $P$, $Q$, और $R$ पर छूता है। त्रिभुज $ABC$ का परिमाप ${self.perimeter:.1f}$ cm है। यह देखते हुए कि स्पर्श रेखा खंड $AR = {self.x:.1f}$ cm और $BP = {self.y:.1f}$ cm हैं, भुजा $AC$ की लंबाई की गणना करें।'
        self.description_kazakh = f'Диаграммада қабырғаларды $P$, $Q$ және $R$ нүктелерінде жанайтын, $ABC$ үшбұрышына іштей сызылған шеңбер көрсетілген. $ABC$ үшбұрышының периметрі ${self.perimeter:.1f}$ см. Жанама кесінділері $AR = {self.x:.1f}$ см және $BP = {self.y:.1f}$ см екені белгілі болса, $AC$ қабырғасының ұзындығын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha duara-ndani la pembetatu $ABC$, linalogusa pande kwenye $P$, $Q$, na $R$. Mzingo wa pembetatu $ABC$ ni sm ${self.perimeter:.1f}$. Ikipewa kwamba sehemu za tanjiti $AR = {self.x:.1f}$ sm na $BP = {self.y:.1f}$ sm, kokotoa urefu wa upande $AC$.'

class Mat054_multi(Mat054):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算所示图形的总面积。'
        self.description_arabic = f'احسب المساحة الكلية للشكل الموضح.'
        self.description_hindi = f'दिखाई गई आकृति के कुल क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Көрсетілген фигураның жалпы ауданын есептеңіз.'
        self.description_swahili = f'Kokotoa eneo lote la umbo lililoonyeshwa.'

class Mat055_multi(Mat055):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算平行四边形的面积。'
        self.description_arabic = f'احسب مساحة متوازي الأضلاع.'
        self.description_hindi = f'समांतर चतुर्भुज (parallelogram) के क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Параллелограммның ауданын есептеңіз.'
        self.description_swahili = f'Kokotoa eneo la msambamba.'

class Mat056_multi(Mat056):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算梯形的面积。'
        self.description_arabic = f'احسب مساحة شبه المنحرف.'
        self.description_hindi = f'समलंब चतुर्भुज (trapezium) के क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Трапецияның ауданын есептеңіз.'
        self.description_swahili = f'Kokotoa eneo la trapeza.'

class Mat057_multi(Mat057):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算小径的面积。'
        self.description_arabic = f'احسب مساحة المسار.'
        self.description_hindi = f'पथ के क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Жолдың ауданын есептеңіз.'
        self.description_swahili = f'Kokotoa eneo la njia.'

class Mat058_multi(Mat058):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算图形的周长。'
        self.description_arabic = f'احسب محيط الشكل.'
        self.description_hindi = f'आकृति के परिमाप (perimeter) की गणना करें।'
        self.description_kazakh = f'Фигураның периметрін есептеңіз.'
        self.description_swahili = f'Kokotoa mzingo wa umbo.'

class Mat059_multi(Mat059):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算阴影优角扇形的面积。结果用$\\pi$表示。结果保留2位小数。'
        self.description_arabic = f'احسب مساحة القطاع الدائري الأكبر المظلل. أعطِ إجابتك بدلالة $\\pi$. قرّب النتيجة إلى منزلتين عشريتين.'
        self.description_hindi = f'छायांकित दीर्घ त्रिज्यखंड (major sector) के क्षेत्रफल की गणना करें। अपना उत्तर $\\pi$ के पदों में दें। परिणाम को दो दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Боялған үлкен сектордың ауданын есептеңіз. Жауабыңызды $\\pi$ арқылы беріңіз. Нәтижені екі ондық таңбаға дейін дөңгелетіңіз.'
        self.description_swahili = f'Kokotoa eneo la sekta kuu iliyotiwa kivuli. Toa jibu lako kwa mtajo wa $\\pi$. Kadiria jibu hadi nafasi mbili za desimali.'

class Mat060_multi(Mat060):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算阴影扇形的弧长。{self.pi_instruction} 结果保留2位小数。'
        self.description_arabic = f'احسب طول قوس القطاع المظلل. {self.pi_instruction} أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'छायांकित त्रिज्यखंड के चाप (arc) की लंबाई की गणना करें। {self.pi_instruction} अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Боялған сектордың доғасының ұзындығын есептеңіз. {self.pi_instruction} Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa urefu wa tao la sekta iliyotiwa kivuli. {self.pi_instruction} Toa jibu lako hadi nafasi 2 za desimali.'

class Mat061_multi(Mat061):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算窗框的总周长。结果保留2位小数。'
        self.description_arabic = f'احسب المحيط الكلي لإطار النافذة. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'खिड़की के फ्रेम के कुल परिमाप की गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Терезе жақтауының жалпы периметрін есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa mzingo wote wa fremu ya dirisha. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat062_multi(Mat062):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算阴影部分的面积。结果用$\\pi$表示。'
        self.description_arabic = f'احسب مساحة المنطقة المظللة. اترك إجابتك بدلالة $\\pi$.'
        self.description_hindi = f'छायांकित क्षेत्र के क्षेत्रफल की गणना करें। अपना उत्तर $\\pi$ के पदों में छोड़ें।'
        self.description_kazakh = f'Боялған бөліктің ауданын есептеңіз. Жауабыңызды $\\pi$ арқылы қалдырыңыз.'
        self.description_swahili = f'Kokotoa eneo la sehemu iliyotiwa kivuli. Acha jibu lako kwa mtajo wa $\\pi$.'

class Mat063_multi(Mat063):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算雨刷清理挡风玻璃的面积。结果用$\\pi$表示。结果保留2位小数。'
        self.description_arabic = f'احسب مساحة الجزء من الزجاج الأمامي الذي تنظفه الشفرة. أعطِ إجابتك بدلالة $\\pi$. قرّب النتيجة إلى منزلتين عشريتين.'
        self.description_hindi = f'ब्लेड द्वारा साफ किए गए विंडशील्ड के क्षेत्रफल की गणना करें। अपना उत्तर $\\pi$ के पदों में दें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Тазалағыш тазартқан алдыңғы әйнек бетінің ауданын есептеңіз. Жауапты $\\pi$ саны арқылы беріңіз. Сондай-ақ жауапты үтірден кейін екі ондық таңбаға дейінгі дәлдікпен көрсетіңіз.'
        self.description_swahili = f'Kokotoa eneo la kioo cha mbele cha gari kilichosafishwa na wipa. Toa jibu lako kwa mtajo wa $\\pi$. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat064_multi(Mat064):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算筒仓的总体积。结果用$\\pi$表示。结果保留2位小数。'
        self.description_arabic = f'احسب الحجم الكلي للصومعة. أعطِ إجابتك بدلالة $\\pi$. قرّب النتيجة إلى منزلتين عشريتين.'
        self.description_hindi = f'साइलो (silo) के कुल आयतन की गणना करें। अपना उत्तर $\\pi$ के पदों में दें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Сүрлем мұнарасының жалпы көлемін есептеңіз. Жауабыңызды $\\pi$ арқылы беріңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa ujazo wote wa silo. Toa jibu lako kwa mtajo wa $\\pi$. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat065_multi(Mat065):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算水池的容量（立方米）。结果保留2位小数。'
        self.description_arabic = f'احسب سعة المسبح بالمتر المكعب. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'पूल की क्षमता (capacity) की घन मीटर (cubic meters) में गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Бассейннің сыйымдылығын куб метрмен есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa uwezo wa bwawa katika mita za ujazo. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat066_multi(Mat066):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算圆锥的总表面积。使用 $\\pi = 3.142$。结果保留2位小数。'
        self.description_arabic = f'احسب المساحة السطحية الكلية للمخروط. استخدم $\\pi = 3.142$. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'शंकु (cone) के कुल पृष्ठीय क्षेत्रफल की गणना करें। $\\pi = 3.142$ का उपयोग करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Конустың толық бетінің ауданын есептеңіз. $\\pi = 3.142$ мәнін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo lote la uso la pia. Tumia $\\pi = 3.142$. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat067_multi(Mat067):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算实心半球的总表面积。使用 $\\pi = 3.14$。结果保留2位小数。'
        self.description_arabic = f'احسب المساحة السطحية الكلية لنصف كرة مصمتة. استخدم $\\pi = 3.14$. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'ठोस अर्धगोले (solid hemisphere) का कुल पृष्ठीय क्षेत्रफल ज्ञात कीजिए। $\\pi = 3.14$ का प्रयोग कीजिए। उत्तर को 2 दशमलव स्थानों तक सही दीजिए।'
        self.description_kazakh = f'Тұтас жарты шардың толық бетінің ауданын есептеңіз. $\\pi = 3.14$ мәнін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo lote la uso la kizio-tufe imara. Tumia $\\pi = 3.14$. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat068_multi(Mat068):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算棱锥的垂直高度，然后用它来求体积。结果保留2位小数。'
        self.description_arabic = f'احسب الارتفاع العمودي للهرم، ثم استخدمه لإيجاد الحجم. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'पिरामिड की ऊर्ध्वाधर ऊँचाई (vertical height) की गणना करें और फिर इसका उपयोग आयतन ज्ञात करने के लिए करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Пирамиданың биіктігін есептеңіз және оны көлемді табу үшін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa kimo cha wima cha piramidi na kisha ukitumie kutafuta ujazo. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat069_multi(Mat069):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算图形的总周长。使用 $\\pi = 3.1416$。结果保留2位小数。'
        self.description_arabic = f'احسب المحيط الكلي للشكل. استخدم $\\pi = 3.1416$. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'आकृति के कुल परिमाप (perimeter) की गणना करें। $\\pi = 3.1416$ का उपयोग करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Фигураның жалпы периметрін есептеңіз. $\\pi = 3.1416$ мәнін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa mzingo wote wa umbo. Tumia $\\pi = 3.1416$. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat070_multi(Mat070):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算图形的总面积。使用 $\\pi = 3.1416$。结果保留2位小数。'
        self.description_arabic = f'احسب المساحة الكلية للشكل. استخدم $\\pi = 3.1416$. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'आकृति के कुल क्षेत्रफल की गणना करें। $\\pi = 3.1416$ का उपयोग करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Фигураның жалпы ауданын есептеңіз. $\\pi = 3.1416$ мәнін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo lote la umbo. Tumia $\\pi = 3.1416$. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat071_multi(Mat071):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算阴影部分的面积。结果保留2位小数。'
        self.description_arabic = f'احسب مساحة المنطقة المظللة. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'छायांकित क्षेत्र के क्षेत्रफल की गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Боялған бөліктің ауданын есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo la sehemu iliyotiwa kivuli. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat072_multi(Mat072):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算水箱的总体积。结果保留2位小数。'
        self.description_arabic = f'احسب الحجم الكلي للخزان. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'टैंक के कुल आयतन की गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Резервуардың жалпы көлемін есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa ujazo wote wa tangi. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat073_multi(Mat073):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算水箱的总外表面积（假设底部是平的且封闭）。结果保留2位小数。'
        self.description_arabic = f'احسب المساحة السطحية الخارجية الكلية للخزان (بافتراض أن القاعدة مسطحة ومغلقة). أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'टैंक के कुल बाहरी पृष्ठीय क्षेत्रफल की गणना करें (यह मानते हुए कि आधार सपाट और बंद है)। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Резервуардың толық сыртқы бетінің ауданын есептеңіз (табаны тегіс және жабық деп есептеп). Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo lote la uso wa nje wa tangi (ukichukulia kwamba kitako ni tambarare na kimefungwa). Toa jibu lako hadi nafasi 2 za desimali.'

class Mat074_multi(Mat074):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个直角三角形$ABC$。计算$BC$。'
        self.description_arabic = f'يوضح الشكل مثلثًا قائم الزاوية $ABC$. احسب $BC$.'
        self.description_hindi = f'चित्र एक समकोण त्रिभुज (right-angled triangle) $ABC$ दिखाता है। $BC$ की गणना करें।'
        self.description_kazakh = f'Диаграммада тік бұрышты $ABC$ үшбұрышы көрсетілген. $BC$ қабырғасын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha pembetatu mraba $ABC$. Kokotoa $BC$.'

class Mat075_multi(Mat075):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一把梯子靠在垂直的墙上。梯子的底部位于水平地面上，距墙底部${self.ground_dist}$ m。梯子达到墙面高度${self.wall_height}$ m处。计算梯子的长度。'
        self.description_arabic = f'يستند سلم إلى جدار عمودي. يبعد أسفل السلم مسافة ${self.ground_dist}$ م عن قاعدة الجدار على أرض أفقية. يصل السلم إلى ارتفاع ${self.wall_height}$ م على الجدار. احسب طول السلم.'
        self.description_hindi = f'एक सीढ़ी एक ऊर्ध्वाधर दीवार के सहारे टिकी है। क्षैतिज जमीन पर सीढ़ी का निचला सिरा दीवार के निचले सिरे से ${self.ground_dist}$ m दूर है। सीढ़ी दीवार पर ${self.wall_height}$ m ऊपर तक पहुँचती है। सीढ़ी की लंबाई की गणना करें।'
        self.description_kazakh = f'Саты тік қабырғаға сүйеулі тұр. Сатының төменгі жағы көлденең жерде, қабырғаның төменгі жағынан ${self.ground_dist}$ м қашықтықта орналасқан. Саты қабырға бойымен ${self.wall_height}$ м биіктікке жетеді. Сатының ұзындығын есептеңіз.'
        self.description_swahili = f'Ngazi imeegemezwa kwenye ukuta wa wima. Sehemu ya chini ya ngazi ipo umbali wa m ${self.ground_dist}$ kutoka chini ya ukuta, kwenye ardhi ya mlalo. Ngazi inafika urefu wa m ${self.wall_height}$ kwenda juu ya ukuta. Kokotoa urefu wa ngazi.'

class Mat076_multi(Mat076):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个长方体，其长、宽、高如图所示（单位：cm）。计算从角$A$到角$G$的内部对角线长度。'
        self.description_arabic = f'يوضح الشكل متوازي مستطيلات أبعاده (الطول والعرض والارتفاع) بالسنتيمتر كما هو موضح. احسب طول القطر الداخلي من النقطة $A$ إلى النقطة $G$.'
        self.description_hindi = f'आरेख एक घनाभ (cuboid) दिखाता है जिसकी लंबाई, चौड़ाई, ऊँचाई चित्र में दिखाए अनुसार cm में है। कोने $A$ से कोने $G$ तक आंतरिक विकर्ण (internal diagonal) की लंबाई की गणना करें।'
        self.description_kazakh = f'Диаграммада ұзындығы, ені, биіктігі суретте көрсетілгендей см болатын кубоид көрсетілген. $A$ бұрышынан $G$ бұрышына дейінгі ішкі диагональдың ұзындығын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha mchestatili wenye urefu, upana, na kimo kama inavyoonyeshwa kwenye kielelezo katika sm. Kokotoa urefu wa ulalo wa ndani kutoka pembe $A$ hadi pembe $G$.'

class Mat077_multi(Mat077):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个直角三角形。计算$x$的值。'
        self.description_arabic = 'يوضح الشكل مثلثًا قائم الزاوية. احسب قيمة $x$.'
        self.description_hindi = 'आरेख एक समकोण त्रिभुज (right-angled triangle) दिखाता है। $x$ के मान की गणना करें।'
        self.description_kazakh = 'Диаграммада тік бұрышты үшбұрыш көрсетілген. $x$ мәнін есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha pembetatu mraba. Kokotoa thamani ya $x$.'

class Mat078_multi(Mat078):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"一个身高为{self.person_height} m的人站在水平地面上，距离垂直塔的底部{self.distance} m。从该人眼睛到塔顶的仰角为{self.angle_elevation}^\\circ。计算塔的总高度。"
        self.description_arabic = f'يقف شخص طوله {self.person_height} م على أرض أفقية، وعلى بعد {self.distance} م من قاعدة برج عمودي. زاوية الارتفاع من عيني الشخص إلى قمة البرج هي {self.angle_elevation}^\\circ. احسب الارتفاع الكلي للبرج.'
        self.description_hindi = f"क्षैतिज जमीन पर {self.person_height} m ऊँचाई वाला एक व्यक्ति, एक ऊर्ध्वाधर टावर के आधार से {self.distance} m की दूरी पर खड़ा है। व्यक्ति की आँखों से टावर के शीर्ष का उन्नयन कोण (angle of elevation) {self.angle_elevation}^\\circ है। टावर की कुल ऊँचाई की गणना करें।"
        self.description_kazakh = f"Бойы {self.person_height} м адам тік мұнараның негізінен {self.distance} м қашықтықта көлденең жерде тұр. Адамның көзінен мұнараның төбесіне дейінгі көтерілу бұрышы {self.angle_elevation}^\\circ тең. Мұнараның толық биіктігін есептеңіз."
        self.description_swahili = f'Mtu mwenye urefu wa m {self.person_height} amesimama kwenye ardhi ya mlalo, umbali wa m {self.distance} kutoka kwenye kitako cha mnara wa wima. Pembe mwinuko kutoka machoni mwa mtu huyo hadi kilele cha mnara ni {self.angle_elevation}^\\circ. Kokotoa kimo chote cha mnara.'

class Mat079_multi(Mat079):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'在三角形$ABC$中，$AC = {self.side_ac}$ cm 和 $BC = {self.side_bc}$ cm。角 $BAC = {self.angle_a}^\\circ$。从点$C$作垂线交$AB$于$D$。计算$AB$的长度。'
        self.description_arabic = f'في المثلث $ABC$، $AC = {self.side_ac}$ سم و $BC = {self.side_bc}$ سم. الزاوية $BAC = {self.angle_a}^\\circ$. أُسقط عمود من $C$ على $AB$ عند النقطة $D$. احسب طول $AB$.'
        self.description_hindi = f'त्रिभुज $ABC$ में, $AC = {self.side_ac}$ cm और $BC = {self.side_bc}$ cm है। कोण $BAC = {self.angle_a}^\\circ$ है। $C$ से $AB$ पर $D$ पर एक लंब डाला जाता है। $AB$ की लंबाई ज्ञात कीजिए।'
        self.description_kazakh = f'$ABC$ үшбұрышында $AC = {self.side_ac}$ см және $BC = {self.side_bc}$ см. Бұрыш $BAC = {self.angle_a}^\\circ$. $AB$-мен $D$ нүктесінде қиылысатындай $C$ нүктесінен перпендикуляр түсірілген. $AB$ ұзындығын есептеңіз.'
        self.description_swahili = f'Katika pembetatu $ABC$, $AC = {self.side_ac}$ sm na $BC = {self.side_bc}$ sm. Pembe $BAC = {self.angle_a}^\\circ$. Mstari wa wima umechorwa kutoka $C$ ili kukutana na $AB$ katika $D$. Kokotoa urefu wa $AB$.'

class Mat080_multi(Mat080):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了形式为$y = a {self.func_name}(bx + c) + d$的三角函数图像。求$a$、$b$、$c$和$d$的值。（请按以下格式提供答案：a, b, c, d。例如：1, 2, 3, 4）'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة مثلثية على الصورة $y = a {self.func_name}(bx + c) + d$. أوجد قيم $a$ و $b$ و $c$ و $d$. (اكتب الإجابة بالترتيب: a, b, c, d. مثال: 1, 2, 3, 4)'
        self.description_hindi = f'आरेख $y = a {self.func_name}(bx + c) + d$ के रूप के एक त्रिकोणमितीय फलन (trigonometric function) का ग्राफ दिखाता है। $a$, $b$, $c$, और $d$ के मान ज्ञात करें। (अपना उत्तर इस प्रारूप में दें: a, b, c, d. उदाहरण: 1, 2, 3, 4)'
        self.description_kazakh = f'Диаграммада $y = a {self.func_name}(bx + c) + d$ түріндегі тригонометриялық функцияның графигі көрсетілген. $a$, $b$, $c$ және $d$ мәндерін табыңыз. (Жауабыңызды мына форматта беріңіз: a, b, c, d. Мысалы: 1, 2, 3, 4)'
        self.description_swahili = f'Mchoro unaonyesha grafu ya fanyio la trigonometria la muundo $y = a {self.func_name}(bx + c) + d$. Tafuta thamani za $a$, $b$, $c$, na $d$. (Toa jibu lako katika muundo huu: a, b, c, d. Mfano: 1, 2, 3, 4)'

class Mat081_multi(Mat081):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了$y = f(x)$的图像，其中$f(x) = {self.func_display}$。利用提供的视觉信息，在$0^\\circ \\leqslant x \\leqslant 360^\\circ$的范围内求${self.implicit_eq}$的所有解。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لـ $y = f(x)$ حيث $f(x) = {self.func_display}$. باستخدام المعلومات المعطاة، أوجد جميع حلول ${self.implicit_eq}$ في المجال $0^\\circ \\leqslant x \\leqslant 360^\\circ$.'
        self.description_hindi = f'आरेख $y = f(x)$ का ग्राफ दिखाता है जहाँ $f(x) = {self.func_display}$ है। दी गई दृश्य जानकारी का उपयोग करते हुए, $0^\\circ \\leqslant x \\leqslant 360^\\circ$ की सीमा में ${self.implicit_eq}$ के लिए सभी हल ज्ञात करें।'
        self.description_kazakh = f'Диаграммада $f(x) = {self.func_display}$ болатын $y = f(x)$ графигі көрсетілген. Берілген визуалды ақпаратты пайдалана отырып, $0^\\circ \\leqslant x \\leqslant 360^\\circ$ аралығындағы ${self.implicit_eq}$ үшін барлық шешімдерді табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya $y = f(x)$ ambapo $f(x) = {self.func_display}$. Kwa kutumia taarifa kwenye grafu, tafuta suluhu zote za ${self.implicit_eq}$ katika masafa ya $0^\\circ \\leqslant x \\leqslant 360^\\circ$.'

class Mat082_multi(Mat082):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'根据图像，计算$\\sin x$的值。'
        self.description_arabic = f'بناءً على الشكل، احسب قيمة $\\sin x$.'
        self.description_hindi = f'इमेज के आधार पर, $\\sin x$ के मान की गणना करें।'
        self.description_kazakh = f'Суретке сүйене отырып, $\\sin x$ мәнін есептеңіз.'
        self.description_swahili = f'Kulingana na mchoro, kokotoa thamani ya $\\sin x$.'

class Mat083_multi(Mat083):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了三个点$A$、$B$和$C$的位置。根据图中的信息，计算距离$AB$。'
        self.description_arabic = 'يوضح الشكل مواقع ثلاث نقاط $A$ و $B$ و $C$. بناءً على المعلومات الواردة في الشكل، احسب المسافة $AB$.'
        self.description_hindi = 'आरेख तीन बिंदुओं $A$, $B$ और $C$ की स्थिति दिखाता है। चित्र में दी गई जानकारी के आधार पर, दूरी $AB$ की गणना करें।'
        self.description_kazakh = 'Диаграммада үш $A$, $B$ және $C$ нүктелерінің орындары көрсетілген. Суреттегі ақпаратқа сүйене отырып, $AB$ қашықтығын есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha nafasi za nukta tatu $A$, $B$ na $C$. Kulingana na taarifa kwenye kielelezo, kokotoa umbali wa $AB$.'

class Mat084_multi(Mat084):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个四边形$ABCD$。根据图中提供的信息计算四边形$ABCD$的面积。'
        self.description_arabic = 'يوضح الشكل شكلًا رباعيًا $ABCD$. احسب مساحة الشكل الرباعي $ABCD$ بناءً على المعلومات المقدمة في الشكل.'
        self.description_hindi = 'आरेख एक चतुर्भुज $ABCD$ दिखाता है। चित्र में दी गई जानकारी के आधार पर चतुर्भुज $ABCD$ के क्षेत्रफल की गणना करें।'
        self.description_kazakh = 'Диаграммада $ABCD$ төртбұрышы көрсетілген. Суретте берілген ақпаратқа сүйене отырып, $ABCD$ төртбұрышының ауданын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha pembenne $ABCD$. Kokotoa eneo la pembenne $ABCD$ kulingana na taarifa zilizotolewa kwenye kielelezo.'

class Mat085_multi(Mat085):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据该图，计算钝角$BDC$。'
        self.description_arabic = 'بناءً على الشكل، احسب قياس الزاوية المنفرجة $BDC$.'
        self.description_hindi = 'दिए गए चित्र के आधार पर, अधिक कोण $BDC$ की गणना करें।'
        self.description_kazakh = 'Доғал $BDC$ бұрышын есептеңіз.'
        self.description_swahili = f'Kulingana na mchoro, kokotoa pembe butu $BDC$.'

class Mat086_multi(Mat086):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个长方体。计算$AB$与长方体水平底面之间的夹角。'
        self.description_arabic = 'يوضح الشكل متوازي مستطيلات. احسب الزاوية بين $AB$ والقاعدة الأفقية لمتوازي المستطيلات.'
        self.description_hindi = 'आरेख एक घनाभ दिखाता है। $AB$ और घनाभ के क्षैतिज आधार के बीच के कोण की गणना करें।'
        self.description_kazakh = 'Диаграммада кубоид көрсетілген. $AB$ мен кубоидтің көлденең табаны арасындағы бұрышты есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha mchestatili. Kokotoa pembe kati ya $AB$ na kitako cha mlalo cha mchestatili.'

class Mat087_multi(Mat087):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个具有正方形底面$ABCD$的棱锥$OABCD$。顶点$O$位于底面中心$M$的正上方。计算$OA$与底面的夹角。'
        self.description_arabic = 'يوضح الشكل هرمًا $OABCD$ بقاعدة مربعة $ABCD$. تقع النقطة $O$ عموديًا فوق مركز القاعدة $M$. احسب الزاوية التي يصنعها $OA$ مع القاعدة.'
        self.description_hindi = 'आरेख एक वर्गाकार आधार $ABCD$ वाला एक पिरामिड $OABCD$ दिखाता है। शीर्ष (vertex) $O$ आधार के केंद्र, $M$ के ऊर्ध्वाधर ऊपर है। $OA$ आधार के साथ जो कोण बनाता है, उसकी गणना करें।'
        self.description_kazakh = 'Диаграммада табаны квадрат $ABCD$ болатын $OABCD$ пирамидасы көрсетілген. $O$ төбесі табанның центрі $M$ нүктесінен тік жоғары орналасқан. $OA$ мен табанның арасындағы бұрышты есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha piramidi $OABCD$ yenye kitako cha mraba $ABCD$. Kilele $O$ kipo wima juu ya kitovu cha kitako, $M$. Kokotoa pembe ambayo $OA$ inaunda na kitako.'

class Mat088_multi(Mat088):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个由半球和圆锥组成的立体，两者的半径相同。根据图中显示的测量值，计算立体的总体积。'
        self.description_arabic = 'يوضح الشكل مجسمًا مكوّنًا من نصف كرة ومخروط لهما نفس نصف القطر. بناءً على القياسات الموضحة، احسب الحجم الكلي للمجسم.'
        self.description_hindi = 'आरेख एक अर्धगोले और एक शंकु से बना एक ठोस दिखाता है, दोनों की त्रिज्या समान है। चित्र में दिखाए गए मापों के आधार पर, ठोस के कुल आयतन की गणना करें।'
        self.description_kazakh = 'Диаграммада радиустары бірдей жарты шар мен конустан тұратын дене көрсетілген. Суретте көрсетілген өлшемдерге сүйене отырып, дененің жалпы көлемін есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha umbo thabiti lililoundwa kwa nusu-tufe na pia, yote yakiwa na nusukipenyo sawa. Kulingana na vipimo vilivyoonyeshwa kwenye kielelezo, kokotoa ujazo wote wa umbo hilo.'

class Mat089_multi(Mat089):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'放大倍数是多少？'
        self.description_arabic = f'ما معامل التكبير؟'
        self.description_hindi = f'विस्तार (enlargement) का स्केल फैक्टर (scale factor) क्या है?'
        self.description_kazakh = f'Үлкейтудің (созудың) масштабтық коэффициенті қандай?'
        self.description_swahili = f'Ni kipi kipengeo cha uwiano cha ukuzaji huu?'

class Mat090_multi(Mat090):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图形Q的面积是多少$cm^2$？结果保留2位小数。'
        self.description_arabic = f'ما مساحة الشكل $Q$ بوحدة $cm^2$؟ أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'आकृति Q का क्षेत्रफल $cm^2$ में क्या है?, अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Q фигурасының ауданы $cm^2$-мен есептегенде қанша? Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Tafuta eneo la umbo Q katika $cm^2$. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat091_multi(Mat091):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"点$A'$的新$y$坐标是多少？"
        self.description_arabic = f"ما إحداثي $y$ الجديد للنقطة $A'$؟"
        self.description_hindi = f"बिंदु $A'$ का नया $y$-निर्देशांक क्या है?"
        self.description_kazakh = f"$A'$ нүктесінің жаңа $y$-координатасы қандай?"
        self.description_swahili = f'Je, ni ipi koordinati mpya ya $y$ ya nukta $A\'$?'

class Mat092_multi(Mat092):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'原始三角形的一个顶点被高亮显示。在它被平移后，新顶点的$x$和$y$坐标之和是多少？'
        self.description_arabic = f'تم إبراز أحد رؤوس المثلث الأصلي. بعد إجراء الانسحاب، ما مجموع إحداثيي $x$ و $y$ للرأس الجديد؟'
        self.description_hindi = f'मूल त्रिभुज के शीर्षों (vertices) में से एक को हाइलाइट किया गया है। इसके स्थानांतरण (translation) के बाद, नए शीर्ष के $x$ और $y$ निर्देशांकों का योग क्या है?'
        self.description_kazakh = f'Бастапқы үшбұрыш төбелерінің бірі ерекшеленген. Оны параллель көшіргеннен кейін, жаңа төбенің $x$ және $y$ координаталарының қосындысы қандай болады?'
        self.description_swahili = f'Kilele kimoja cha pembetatu ya asili kimeangaziwa. Baada ya pembetatu hiyo kutafsiriwa (translated), ni ipi jumla ya koordinati za $x$ na $y$ za kilele hicho kipya?'

class Mat093_multi(Mat093):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"在{self.line['desc']}反射后的图像的{self.ask_for}坐标是多少？"
        self.description_arabic = f'ما إحداثي {self.ask_for} لصورة النقطة $A$ بعد انعكاسها حول {self.line["desc"]}؟'
        self.description_hindi = f"{self.line['desc']} में परावर्तन के बाद बिंदु A की इमेज का {self.ask_for}-निर्देशांक क्या है?"
        self.description_kazakh = f"А нүктесін {self.line['desc']} түзуіне қатысты шағылдырғаннан кейін пайда болған бейненің {self.ask_for}-координатасы неге тең?"
        self.description_swahili = f"Ni ipi koordinati ya {self.ask_for} ya taswira ya nukta A baada ya akisi (reflection) kwenye {self.line['desc']}?"

class Mat094_multi(Mat094):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'合向量$\\mathbf{{r}}$的x分量的值是多少？'
        self.description_arabic = f'ما قيمة المركبة $x$ للمتجه المحصل $\\mathbf{{r}}$؟'
        self.description_hindi = f'परिणामी सदिश (resultant vector) $\\mathbf{{r}}$ के x-घटक (x-component) का मान क्या है?'
        self.description_kazakh = f'Қорытынды $\\mathbf{{r}}$ векторының x-компонентінің мәні қандай?'
        self.description_swahili = f'Ni ipi thamani ya kijenzi cha $x$ cha vekta tokeo $\\mathbf{{r}}$?'

class Mat095_multi(Mat095):
    def __init__(self):
        super().__init__()
        self.description_chinese = '在图中，网格上显示了向量$\\mathbf{p}$和$\\mathbf{q}$。如果$\\mathbf{p}$和$\\mathbf{q}$平行，求$k$的值。'
        self.description_arabic = 'في الشكل، تظهر المتجهات $\\mathbf{p}$ و $\\mathbf{q}$ على شبكة. إذا كان $\\mathbf{p}$ و $\\mathbf{q}$ متوازيين، فأوجد قيمة $k$.'
        self.description_hindi = 'आरेख में, सदिश $\\mathbf{p}$ और $\\mathbf{q}$ एक ग्रिड पर दिखाए गए हैं। यदि $\\mathbf{p}$ और $\\mathbf{q}$ समानांतर हैं, तो $k$ का मान ज्ञात करें।'
        self.description_kazakh = 'Диаграммада $\\mathbf{p}$ және $\\mathbf{q}$ векторлары торда көрсетілген. Егер $\\mathbf{p}$ және $\\mathbf{q}$ параллель болса, $k$ мәнін табыңыз.'
        self.description_swahili = 'Kwenye mchoro, vekta $\\mathbf{{p}}$ na $\\mathbf{{q}}$ zinaonyeshwa kwenye gridi. Ikiwa $\\mathbf{{p}}$ na $\\mathbf{{q}}$ ni sambamba, tafuta thamani ya $k$.'

class Mat096_multi(Mat096):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算向量的大小（长度）。结果保留2位小数。'
        self.description_arabic = f'احسب مقدار (طول) المتجه. أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'सदिश के परिमाण (लंबाई) की गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Вектордың ұзындығын есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa ukubwa (urefu) wa vekta hiyo. Toa jibu lako hadi nafasi 2 za desimali.'

class Mat097_multi(Mat097):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'利用向量，求标量$k$的值，使得点$A$、$B$和$C$共线。'
        self.description_arabic = f'باستخدام المتجهات، أوجد قيمة الكمية القياسية $k$ بحيث تقع النقاط $A$ و $B$ و $C$ على استقامة واحدة.'
        self.description_hindi = f'सदिशों का उपयोग करते हुए, अदिश (scalar) $k$ का मान इस प्रकार ज्ञात करें कि बिंदु $A$, $B$, और $C$ संरेख (collinear) हों।'
        self.description_kazakh = f'Векторларды пайдаланып, $A$, $B$ және $C$ нүктелері коллинеар болатындай $k$ скалярының мәнін табыңыз.'
        self.description_swahili = f'Kwa kutumia vekta, tafuta thamani ya skala $k$ ili nukta $A$, $B$, na $C$ ziwe kolinia (kwenye mstari mmoja).'

class Mat098_multi(Mat098):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'在图中，$OABC$是一个梯形，其中$OA$平行于$CB$。点$P$位于线段$AB$上。已知$\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$，求$k$的值。结果保留3位小数。'
        self.description_arabic = f'في الشكل، $OABC$ شبه منحرف حيث $OA$ موازٍ لـ $CB$. تقع النقطة $P$ على القطعة $AB$. أوجد قيمة $k$ علمًا بأن $\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'आरेख में, $OABC$ एक समलंब चतुर्भुज है जहाँ $OA$, $CB$ के समानांतर है। बिंदु $P$ रेखाखंड $AB$ पर स्थित है। $k$ का मान ज्ञात करें, यह देखते हुए कि $\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$ है। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Диаграммада $OABC$ трапеция, мұндағы $OA$ мен $CB$ параллель. $P$ нүктесі $AB$ кесіндісінде жатыр. Егер $\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$ екені белгілі болса, $k$ мәнін табыңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kwenye mchoro, $OABC$ ni trapeza ambapo $OA$ ni sambamba na $CB$. Nukta $P$ ipo kwenye kipande cha mstari $AB$. Tafuta thamani ya $k$ ikiwa $\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat099_multi(Mat099):
    def __init__(self):
        super().__init__()
        self.description_chinese = '利用向量图中的信息求正标量$k$的值。'
        self.description_arabic = 'باستخدام المعلومات في مخطط المتجهات، أوجد قيمة الكمية القياسية الموجبة $k$.'
        self.description_hindi = 'धनात्मक अदिश $k$ का मान ज्ञात करने के लिए सदिश आरेख में दी गई जानकारी का उपयोग करें।'
        self.description_kazakh = 'Оң $k$ скалярының мәнін табу үшін векторлық диаграммадағы ақпаратты пайдаланыңыз.'
        self.description_swahili = f'Tumia taarifa kwenye mchoro wa vekta kutafuta thamani ya skala chanya $k$.'

class Mat100_multi(Mat100):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'在三角形$OAB$中，向量$\\vec{{OA}} = \\mathbf{{a}}$，向量$\\vec{{OB}} = \\mathbf{{b}}$。已知$\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$，求$k$的值。结果保留3位小数。'
        self.description_arabic = f'في المثلث $OAB$، المتجه $\\vec{{OA}} = \\mathbf{{a}}$ والمتجه $\\vec{{OB}} = \\mathbf{{b}}$. إذا كان $\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$، فأوجد قيمة $k$. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'त्रिभुज $OAB$ में, सदिश $\\vec{{OA}} = \\mathbf{{a}}$ और सदिश $\\vec{{OB}} = \\mathbf{{b}}$ है। यह देखते हुए कि $\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$ है, $k$ का मान ज्ञात करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'$OAB$ үшбұрышында $\\vec{{OA}} = \\mathbf{{a}}$ және $\\vec{{OB}} = \\mathbf{{b}}$ векторлары берілген. Егер $\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$ екені белгілі болса, $k$ мәнін табыңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Katika pembetatu $OAB$, vekta $\\vec{{OA}} = \\mathbf{{a}}$ na vekta $\\vec{{OB}} = \\mathbf{{b}}$. Ikiwa $\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$, tafuta thamani ya $k$. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat101_multi(Mat101):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'根据图中的结果，转盘停在颜色{self.target_color}上的相对频率是多少？结果保留3位小数。'
        self.description_arabic = f'بناءً على النتائج في الشكل، ما التكرار النسبي لوقوع المؤشر الدوار على اللون {self.target_color}؟ أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'चित्र में परिणामों के आधार पर, स्पिनर के रंग {self.target_color} पर रुकने की सापेक्ष आवृत्ति क्या है? अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Суреттегі нәтижелерге сүйене отырып, спиннердің {self.target_color} түсіне тоқтауының салыстырмалы жиілігі қандай? Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kulingana na matokeo kwenye kielelezo, ni upi mzunguko wa uwiano (relative frequency) wa spina kutua kwenye rangi ya {self.target_color}? Toa jibu lako hadi nafasi 3 za desimali.'

class Mat102_multi(Mat102):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'利用图表中的相对频率，计算如果掷骰子{self.total_rolls_scenario}次，掷出{self.target_face}的期望频率。'
        self.description_arabic = f'باستخدام التكرار النسبي من المخطط، احسب التكرار المتوقع لظهور {self.target_face} عند رمي حجر النرد {self.total_rolls_scenario} مرة.'
        self.description_hindi = f'चार्ट से सापेक्ष आवृत्ति का उपयोग करते हुए, यदि पासा {self.total_rolls_scenario} बार फेंका जाता है तो {self.target_face} आने की अपेक्षित आवृत्ति की गणना करें।'
        self.description_kazakh = f'Диаграммадағы салыстырмалы жиілікті пайдалана отырып, егер сүйек {self.total_rolls_scenario} рет лақтырылса, {self.target_face} түсуінің күтілетін жиілігін есептеңіз.'
        self.description_swahili = f'Kwa kutumia marudio ya uwiano kutoka kwenye chati, kokotoa marudio yanayotarajiwa ya kupata {self.target_face} ikiwa kete itarushwa mara {self.total_rolls_scenario}.'

class Mat103_multi(Mat103):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'护林员从湖中捕获了{self.M}条鱼，给它们打上标签，然后释放。后来，护林员捕获了一个新样本（如上图所示）。利用第二次捕获中带标记鱼的相对频率，估计湖中鱼的预期总数。'
        self.description_arabic = f'يصطاد حارس {self.M} سمكة من البحيرة، ويضع عليها علامة ثم يطلقها. لاحقًا، يصطاد عينة جديدة (كما هو موضح في الشكل). باستخدام التكرار النسبي للأسماك المعلمة في الصيد الثاني، قدّر العدد الكلي المتوقع للأسماك في البحيرة.'
        self.description_hindi = f'एक रेंजर झील से {self.M} मछलियाँ पकड़ता है, उन्हें एक टैग से चिह्नित करता है, और उन्हें छोड़ देता है। बाद में, रेंजर एक नया नमूना पकड़ता है (ऊपर चित्र में दिखाया गया है)। दूसरी पकड़ में चिह्नित मछलियों की सापेक्ष आवृत्ति का उपयोग करते हुए, झील में मछलियों की कुल अपेक्षित संख्या का अनुमान लगाएँ।'
        self.description_kazakh = f'Қорықшы көлден {self.M} балық ұстап, оларға белгі салып, қайтадан босатады. Кейінірек қорықшы жаңа үлгі ұстайды (жоғарыдағы суретте көрсетілген). Екінші аулаудағы белгіленген балықтардың салыстырмалы жиілігін пайдалана отырып, көлдегі балықтардың жалпы күтілетін санын бағалаңыз.'
        self.description_swahili = f'Mhifadhi anavua samaki {self.M} kutoka ziwani, anawawekea alama, na kisha anawaachia. Baadaye, mhifadhi anavua sampuli mpya (kama inavyoonekana kwenye kielelezo hapo juu). Kwa kutumia marudio ya uwiano wa samaki waliotiwa alama kwenye vuo la pili, kadiria jumla ya idadi ya samaki wanaotarajiwa kuwa ziwani.'

class Mat104_multi(Mat104):
    def __init__(self):
        super().__init__()
        self.description_chinese = '利用图中的数据，确定加入艺术俱乐部（用$x$表示）的10年级学生人数。'
        self.description_arabic = 'باستخدام البيانات في الشكل، أوجد عدد طلاب الصف العاشر الذين انضموا إلى نادي الفنون (الممثل بـ $x$).'
        self.description_hindi = 'चित्र में दिए गए डेटा का उपयोग करते हुए, ग्रेड 10 में उन छात्रों की संख्या निर्धारित करें जो Art Club में शामिल हुए (जिसे $x$ द्वारा दर्शाया गया है)।'
        self.description_kazakh = 'Суреттегі деректерді пайдалана отырып, Өнер клубына қосылған 10-сынып оқушыларының санын ($x$ арқылы белгіленген) анықтаңыз.'
        self.description_swahili = f'Kwa kutumia takwimu kwenye kielelezo, bainisha idadi ya wanafunzi wa Gredi 10 waliojiunga na Klabu ya Sanaa (inayowakilishwa na $x$).'

class Mat105_multi(Mat105):
    def __init__(self):
        super().__init__()
        self.description_chinese = '上方的折线图代表某城市8小时内每两小时记录一次的温度。计算记录的最高温度与16:00温度之间的总降温（单位：摄氏度）。'
        self.description_arabic = 'يمثل الرسم البياني الخطي أعلاه درجة الحرارة المسجلة كل ساعتين في مدينة خلال فترة 8 ساعات. احسب مقدار الانخفاض الكلي في درجة الحرارة، بالدرجات المئوية، بين أعلى درجة حرارة مسجلة ودرجة الحرارة عند الساعة 16:00.'
        self.description_hindi = 'ऊपर दिया गया रेखा ग्राफ 8 घंटे की अवधि में एक शहर में हर दो घंटे में दर्ज किए गए तापमान को दर्शाता है। दर्ज किए गए सबसे गर्म बिंदु और 16:00 बजे के तापमान के बीच, डिग्री सेल्सियस में, कुल गिरावट की गणना करें।'
        self.description_kazakh = 'Жоғарыдағы сызықтық график қаладағы 8 сағаттық кезең ішінде әр екі сағат сайын тіркелген температураны көрсетеді. Тіркелген ең ыстық нүкте мен сағат 16:00-дегі температура арасындағы температураның жалпы төмендеуін Цельсий градусымен есептеңіз.'
        self.description_swahili = f'Grafu ya mstari hapo juu inawakilisha halijoto iliyorekodiwa kila baada ya saa mbili katika jiji kwa kipindi cha saa 8. Kokotoa jumla ya kushuka kwa halijoto, katika nyuzi Selsiasi, kati ya kiwango cha juu zaidi kilichorekodiwa na halijoto iliyokuwa saa 16:00.'

class Mat106_multi(Mat106):
    def __init__(self):
        super().__init__()
        self.description_chinese = '利用该图，计算在整个三周期间内，商店A售出的笔记本电脑总数与商店B售出的笔记本电脑总数之差。'
        self.description_arabic = 'باستخدام الشكل، احسب الفرق بين إجمالي عدد الحواسيب المحمولة المباعة في المتجر A والمتجر B خلال فترة الثلاثة أسابيع.'
        self.description_hindi = 'चित्र का उपयोग करते हुए, पूरे तीन सप्ताह की अवधि में Store A द्वारा बेचे गए लैपटॉप की कुल संख्या और Store B द्वारा बेचे गए लैपटॉप की कुल संख्या के बीच के अंतर की गणना करें।'
        self.description_kazakh = 'Суретті пайдалана отырып, толық үш апталық кезең ішінде А дүкені сатқан ноутбуктердің жалпы саны мен В дүкені сатқан ноутбуктердің жалпы саны арасындағы айырмашылықты есептеңіз.'
        self.description_swahili = f'Kwa kutumia kielelezo, kokotoa tofauti kati ya jumla ya kompyuta mpakato zilizouzwa na Duka A na jumla ya kompyuta mpakato zilizouzwa na Duka B katika kipindi chote cha wiki tatu.'

class Mat107_multi(Mat107):
    def __init__(self):
        super().__init__()
        self.description_chinese ='参考该图。列出了 11 名学生的考试成绩，按升序排列。计算此数据集的四分位距（IQR）。'
        self.description_arabic = 'بالرجوع إلى الشكل الذي يعرض درجات 11 طالبًا مرتبة تصاعديًا، احسب المدى الربيعي (IQR) لهذه البيانات.'
        self.description_hindi = 'चित्र को देखें, जिसमें 11 छात्रों के परीक्षा अंकों को आरोही क्रम में सूचीबद्ध किया गया है। इस डेटा सेट का अंतरचतुर्थक रेंज (IQR) ज्ञात करें।'
        self.description_kazakh = 'Өсу ретімен орналастырылған 11 оқушының тест ұпайлары көрсетілген суретке (сызбаға) назар аударыңыз. Осы мәліметтер жиынтығының интерквартильдік ауқымын (IQR) есептеңіз.'
        self.description_swahili = f'Rejelea kielelezo kinachoorodhesha alama za mtihani za wanafunzi 11 zilizopangwa kwa mpangilio wa kupanda. Kokotoa Masafa ya Baina ya Kuataili (Interquartile Range - IQR) ya seti hii ya takwimu.'

class Mat108_multi(Mat108):
    def __init__(self):
        super().__init__()
        self.description_chinese = '参考该图。计算学生阅读书籍的平均数量。结果保留3位小数。'
        self.description_arabic = 'بالرجوع إلى الشكل، احسب المتوسط الحسابي لعدد الكتب التي قرأها الطلاب. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र देखें। छात्रों द्वारा पढ़ी गई पुस्तकों की माध्य संख्या की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретке назар аударыңыз. Оқушылар оқыған кітаптардың орташа санын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Rejelea kielelezo. Kokotoa wastani wa idadi ya vitabu vilivyosomwa na wanafunzi. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat109_multi(Mat109):
    def __init__(self):
        super().__init__()
        self.description_chinese = '参考显示树苗高度的图。计算树苗的估计平均高度。结果保留3位小数。'
        self.description_arabic = 'بالرجوع إلى الشكل الذي يوضح أطوال الشتلات، احسب المتوسط الحسابي التقديري لأطوال الشتلات. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र देखें, जो पौधों की ऊँचाई दिखाता है। पौधों की अनुमानित माध्य ऊँचाई की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Көшеттердің биіктігі көрсетілген суретке назар аударыңыз. Көшеттердің бағаланған орташа биіктігін есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Rejelea kielelezo kinachoonyesha kimo cha miche. Kokotoa makadirio ya wastani wa kimo cha miche hiyo. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat110_multi(Mat110):
    def __init__(self):
        super().__init__()
        self.description_chinese = '下方的茎叶图显示了读书俱乐部成员的年龄。利用提供的图例，计算年龄的极差。'
        self.description_arabic = 'يعرض مخطط الساق والورقة أدناه أعمار الأعضاء في نادي كتاب. باستخدام المفتاح المعطى، احسب مدى الأعمار.'
        self.description_hindi = 'नीचे दिया गया स्टेम-एंड-लीफ़ आरेख एक बुक क्लब में सदस्यों की आयु प्रदर्शित करता है। प्रदान की गई कुंजी का उपयोग करके, आयु की सीमा की गणना करें।'
        self.description_kazakh = 'Төмендегі сабақ-жапырақ диаграммасы кітап клубы мүшелерінің жасын көрсетеді. Берілген кілтті пайдалана отырып, жастардың диапазонын есептеңіз.'
        self.description_swahili = f'Mchoro wa shina-na-jani hapa chini unaonyesha umri wa wanachama wa klabu ya vitabu. Kwa kutumia ufunguo uliotolewa, kokotoa masafa ya umri huo.'

class Mat111_multi(Mat111):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"下方的复合条形图显示了一家商店三天的总收入。在星期五，条形图的总高度代表${self.friday_total}。那天的'Drink'销售额是多少？"
        self.description_arabic = f"يوضح المخطط الشريطي المركب أدناه الإيرادات الإجمالية لمتجر على مدار ثلاثة أيام. في يوم الجمعة، يمثل الارتفاع الإجمالي للشريط ${self.friday_total}. ما قيمة مبيعات 'المشروبات' في ذلك اليوم؟"
        self.description_hindi = f"नीचे दिया गया मिश्रित दंड आरेख तीन दिनों में एक स्टोर का कुल राजस्व दिखाता है। शुक्रवार को, बार की कुल ऊँचाई ${self.friday_total} का प्रतिनिधित्व करती है। उस दिन के लिए 'Drink' की बिक्री का मूल्य क्या है?"
        self.description_kazakh = f"Төмендегі құрама бағаналы диаграмма дүкеннің үш күн ішіндегі жалпы табысын көрсетеді. Жұма күні бағананың жалпы биіктігі ${self.friday_total} құрайды. Ол күнгі 'Drink' сатылымының мәні қандай?"
        self.description_swahili = f"Chati mseto ya miraba hapa chini inaonyesha jumla ya mapato ya duka kwa muda wa siku tatu. Siku ya Ijumaa, urefu wa mraba unawakilisha ${self.friday_total}. Tafuta thamani ya mauzo ya 'Vinywaji' (Drink) kwa siku hiyo."

class Mat112_multi(Mat112):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'象形图显示了四个晚上售出的比萨饼。图例表明，一个完整的符号代表{self.key_value}个比萨饼。星期二售出了多少个比萨？'
        self.description_arabic = f'يوضح المخطط الرمزي عدد البيتزا المباعة في أربع أمسيات. يشير المفتاح إلى أن الرمز الكامل الواحد يمثل {self.key_value} بيتزا. كم عدد البيتزا التي بيعت يوم الثلاثاء؟'
        self.description_hindi = f'चित्रलेख चार शामों में बेचे गए पिज्जा दिखाता है। कुंजी इंगित करती है कि एक पूर्ण प्रतीक {self.key_value} पिज्जा का प्रतिनिधित्व करता है। मंगलवार को कितने पिज्जा बेचे गए?'
        self.description_kazakh = f'Пиктограмма төрт кеш бойы сатылған пиццаларды көрсетеді. Кілт бір толық таңбаның {self.key_value} пиццаны білдіретінін көрсетеді. Сейсенбіде қанша пицца сатылды?'
        self.description_swahili = f'Piktogramu hii inaonyesha piza zilizouzwa katika jioni nne tofauti. Ufunguo unaonyesha kwamba alama moja kamili inawakilisha piza {self.key_value}. Je, ni piza ngapi zilizouzwa siku ya Jumanne?'

class Mat113_multi(Mat113):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'根据散点图，由点P代表的车龄为{self.target_age}年的汽车的转售价值（以千美元为单位）是多少？'
        self.description_arabic = f'وفقًا لمخطط الانتشار، ما قيمة إعادة البيع (بآلاف الدولارات) للسيارة البالغة من العمر {self.target_age} سنوات والممثلة بالنقطة $P$؟'
        self.description_hindi = f'प्रकीर्ण आरेख के अनुसार, बिंदु P द्वारा दर्शाई गई {self.target_age}-वर्ष पुरानी कार का पुनर्विक्रय मूल्य (हजारों डॉलर में) क्या है?'
        self.description_kazakh = f'Шашыраңқы диаграммаға сәйкес, P нүктесімен көрсетілген {self.target_age} жылдық көліктің қайта сатылу құны (мың доллармен) қандай?'
        self.description_swahili = f'Kulingana na mchoro wa mtawanyo (scatter diagram), tafuta thamani ya kuuza tena (katika maelfu ya dola) ya gari la umri wa miaka {self.target_age} linalowakilishwa na nukta P.'

class Mat114_multi(Mat114):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'利用图中显示的最佳拟合线，计算使用{self.x_query}克肥料时植物的预测高度（单位：cm）。结果保留3位小数。'
        self.description_arabic = f'باستخدام خط أفضل مطابقة الموضح في الشكل، احسب الطول المتوقع (بالسنتيمتر) لنبتة عند استخدام {self.x_query} جرامًا من السماد. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'चित्र में दिखाई गई सबसे उपयुक्त रेखा का उपयोग करते हुए, जब {self.x_query} ग्राम उर्वरक का उपयोग किया जाता है तो एक पौधे की अनुमानित ऊँचाई (cm में) की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Суретте көрсетілген ең жақсы сәйкестік түзуін пайдалана отырып, {self.x_query} грамм тыңайтқыш пайдаланылған кездегі өсімдіктің болжамды биіктігін (см-мен) есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kwa kutumia mstari unaofaa zaidi ulioonyeshwa kwenye kielelezo, kokotoa kimo kilichotabiriwa (katika sm) cha mmea wakati gramu {self.x_query} za mbolea zinapotumiwa. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat115_multi(Mat115):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"学生A的实际物理分数与最佳拟合线根据数学分数{self.student_a_x}预测的分数之间的垂直差异（残差）是多少？结果保留3位小数。"
        self.description_arabic = f'ما الفرق الرأسي (الباقي) بين درجة الطالب $A$ الفعلية في الفيزياء والدرجة المتوقعة من خط أفضل مطابقة لدرجة رياضيات مقدارها {self.student_a_x}؟ أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f"छात्र A के वास्तविक भौतिकी अंक और {self.student_a_x} के गणित अंक के लिए सर्वोत्तम फिट रेखा द्वारा अनुमानित अंक के बीच ऊर्ध्वाधर अंतर (अवशेष) क्या है? अपना उत्तर 3 दशमलव स्थानों तक सही दें।"
        self.description_kazakh = f"А оқушысының Физикадан нақты балы мен {self.student_a_x} Математика балы үшін ең жақсы сәйкестік түзуімен болжанған балдың арасындағы тік айырмашылық (қалдық) қандай? Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз."
        self.description_swahili = f"Ni upi utofauti wa wima (residual) kati ya alama halisi ya Fizikia ya Mwanafunzi A na alama iliyotabiriwa na mstari unaofaa zaidi kwa alama ya Hisabati ya {self.student_a_x}? Toa jibu lako hadi nafasi 3 za desimali."

class Mat116_multi(Mat116):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'利用图中提供的坐标点，确定学生的分数中位数。结果保留1位小数。'
        self.description_arabic = f'باستخدام نقاط الإحداثيات المقدمة في الشكل، أوجد الوسيط لدرجات الطلاب. أعطِ إجابتك مقربة إلى منزلة عشرية واحدة.'
        self.description_hindi = f'चित्र में दिए गए समन्वय बिंदुओं का उपयोग करते हुए, छात्रों के लिए माध्यिका अंक निर्धारित करें।अपना उत्तर 1 दशमलव स्थान तक सही दें।'
        self.description_kazakh = f'Суретте берілген координаталық нүктелерді пайдалана отырып, оқушылардын медиана бағасын анықтаңыз. Жауабыңызды 1 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kwa kutumia viwianishi (coordinate points) vilivyotolewa kwenye kielelezo, bainisha alama ya mediani kwa wanafunzi. Toa jibu lako hadi nafasi 1 ya desimali.'

class Mat117_multi(Mat117):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'根据图中提供的数据，计算植物高度的四分位距（IQR）。'
        self.description_arabic = f'احسب المدى الربيعي (IQR) لأطوال النباتات بناءً على البيانات المقدمة في الشكل.'
        self.description_hindi = f'चित्र में दिए गए डेटा के आधार पर पौधों की ऊँचाई की इंटरक्वार्टाइल रेंज (IQR) की गणना करें।'
        self.description_kazakh = f'Суретте берілген деректер негізінде өсімдік биіктіктерінің квартиль аралық құлашын (IQR) есептеңіз.'
        self.description_swahili = f'Kokotoa Masafa ya Baina ya Kuataili (Interquartile Range - IQR) ya vimo vya mimea kulingana na takwimu zilizotolewa kwenye kielelezo.'

class Mat118_multi(Mat118):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'计算该条形所代表的数据的频率。结果保留1位小数。'
        self.description_arabic = f'احسب تكرار البيانات الممثلة بهذا الشريط. أعطِ إجابتك مقربة إلى منزلة عشرية واحدة.'
        self.description_hindi = f'इस बार द्वारा दर्शाए गए डेटा की आवृत्ति की गणना करें। अपना उत्तर 1 दशमलव स्थान तक सही दें।'
        self.description_kazakh = f'Осы бағанамен көрсетілген деректердің жиілігін есептеңіз. Жауабыңызды 1 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa marudio ya takwimu yanayowakilishwa na mstatili huu. Toa jibu lako hadi nafasi 1 ya desimali.'

class Mat119_multi(Mat119):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'这三个条形所代表的数据的总频率是多少？'
        self.description_arabic = f'ما التكرار الكلي للبيانات الممثلة بهذه الأشرطة الثلاثة؟'
        self.description_hindi = f'इन तीन बारों द्वारा दर्शाए गए डेटा की कुल आवृत्ति क्या है?'
        self.description_kazakh = f'Осы үш бағанамен көрсетілген деректердің жалпы жиілігі қандай?'
        self.description_swahili = f'Ni ipi jumla ya marudio ya takwimu yanayowakilishwa na miraba hii mitatu?'

class Mat120_multi(Mat120):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如果将这些组绘制在同一个直方图上，B组和A组的条形高度之间的正差是多少？'
        self.description_arabic = f'إذا مُثلت هذه المجموعات على نفس المدرج التكراري، فما الفرق الموجب بين ارتفاع الشريط للمجموعة $B$ والمجموعة $A$؟'
        self.description_hindi = f'यदि इन समूहों को एक ही आयतचित्र पर आलेखित किया जाता है, तो Group B और Group A के लिए बार की ऊँचाई के बीच धनात्मक अंतर क्या है?'
        self.description_kazakh = f'Егер осы топтар бір гистограммада салынса, В тобы мен А тобына арналған бағаналар биіктігінің арасындағы оң айырмашылық қандай болады?'
        self.description_swahili = f'Ikiwa makundi haya yatachorwa kwenye histogramu moja, ni upi utofauti chanya kati ya urefu wa mstatili wa Kundi B na Kundi A?'

class Mat121_multi(Mat121):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'利用图中所描述的图像，计算复合函数$f(g({self.start_x}))$。'
        self.description_arabic = f'باستخدام الرسوم البيانية الموضحة في الشكل، أوجد قيمة الدالة المركبة $f(g({self.start_x}))$.'
        self.description_hindi = f'चित्र में वर्णित ग्राफों का उपयोग करते हुए, संयुक्त फलन (composite function) $f(g({self.start_x}))$ का मूल्यांकन करें।'
        self.description_kazakh = f'Суретте сипатталған графиктерді пайдалана отырып, $f(g({self.start_x}))$ күрделі функциясының мәнін есептеңіз.'
        self.description_swahili = f'Kwa kutumia grafu zilizofafanuliwa kwenye kielelezo, tathmini fumbuo mseto (composite function) $f(g({self.start_x}))$.'

class Mat122_multi(Mat122):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'根据图中显示的函数与其反函数之间的关系，确定使得$f^{{-1}}(x) = {self.a}$的$x$的值。'
        self.description_arabic = f'بناءً على العلاقة بين الدالة ومعكوسها الموضحة في الشكل، أوجد قيمة $x$ بحيث $f^{{-1}}(x) = {self.a}$.'
        self.description_hindi = f'चित्र में दिखाए गए फलन और उसके प्रतिलोम के बीच के संबंध के आधार पर, $x$ का मान इस प्रकार निर्धारित करें कि $f^{{-1}}(x) = {self.a}$ हो।'
        self.description_kazakh = f'Суретте көрсетілген функция мен оның кері функциясы арасындағы байланысқа сүйене отырып, $f^{{-1}}(x) = {self.a}$ болатындай $x$ мәнін анықтаңыз.'
        self.description_swahili = f'Kulingana na uhusiano kati ya fumbuo na kinyume chake ulioonyeshwa kwenye kielelezo, bainisha thamani ya $x$ ili $f^{{-1}}(x) = {self.a}$.'

class Mat123_multi(Mat123):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图展示了二次函数$y = f(x)$的图像，它在坐标$({self.h}, {self.k})$处有一个最小转向点。该图还指示了代表变换{self.label_g}的第二条虚线曲线。计算变换后图像$g(x)$的最小点的$y$坐标。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة تربيعية $y = f(x)$ ولها نقطة صغرى عند الإحداثي $({self.h}, {self.k})$. كما يوضح منحنى متقطع يمثل التحويل {self.label_g}. احسب إحداثي $y$ للنقطة الصغرى للتمثيل البياني المحول $g(x)$.'
        self.description_hindi = f'चित्र एक द्विघात फलन (quadratic function) $y = f(x)$ के ग्राफ को दर्शाता है जिसका निर्देशांक $({self.h}, {self.k})$ पर एक न्यूनतम टर्निंग पॉइंट है। चित्र एक दूसरा खंडित वक्र भी इंगित करता है जो एक रूपांतरण {self.label_g} का प्रतिनिधित्व करता है। रूपांतरित ग्राफ $g(x)$ के न्यूनतम बिंदु के $y$-निर्देशांक की गणना करें।'
        self.description_kazakh = f'Суретте $({self.h}, {self.k})$ координатасында минималды бұрылу нүктесі бар $y = f(x)$ квадраттық функциясының графигі көрсетілген. Сурет сондай-ақ {self.label_g} түрлендіруін білдіретін екінші үзік сызықты қисықты көрсетеді. Түрлендірілген $g(x)$ графигінің минималды нүктесінің $y$-координатасын есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya fumbuo ya kipeo cha pili $y = f(x)$ ambayo ina nukta kilele ya chini kwenye viwianishi $({self.h}, {self.k})$. Kielelezo pia kinaonyesha mzingo wa pili wa mchirizo unaowakilisha mageuzi (transformation) {self.label_g}. Kokotoa kiwianishi cha $y$ cha nukta ya chini kabisa ya grafu iliyobadilishwa $g(x)$.'

class Mat124_multi(Mat124):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了函数 ${self.equation_latex}$ 的完整抛物线。对称轴 $x = {self.h}$ 用虚线标出。求最小整数 $k$，使得函数 $f(x)$ 在定义域 $x \\ge k$ 上是单射函数。'
        self.description_arabic = f'يوضح الشكل القطع المكافئ الكامل للدالة: ${self.equation_latex}$. محور التماثل $x = {self.h}$ ممثل بخط متقطع. أوجد أصغر قيمة صحيحة لـ $k$ بحيث تكون الدالة $f(x)$ متباينة على المجال $x \\ge k$.'
        self.description_hindi = f'चित्र फलन का पूर्ण परवलय दिखाता है: ${self.equation_latex}$। सबसे छोटा पूर्णांक मान निर्धारित करें ताकि फलन $f(x)$ डोमेन $x \\ge k$ के लिए एकैकी फलन हो।'
        self.description_kazakh = f'Суретте ${self.equation_latex}$ функциясының толық параболасы көрсетілген. $x = {self.h}$ симметрия осі үзік сызықпен белгіленген. $x \ge k$ анықталу облысында $f(x)$ функциясы өзара бірмәнді (инъективті) болуы үшін, $k$-ның ең кіші бүтін мәнін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha parabola kamili ya fumbuo: ${self.equation_latex}$. Mhimili wa ulinganifu $x = {self.h}$ umewekewa alama ya mstari wa vitone. Bainisha thamani ndogo zaidi ya namba kamili kwa $k$ ili fumbuo $f(x)$ iwe fumbuo ya moja-kwa-moja (one-one function) kwa uga $x \\ge k$.'

class Mat125_multi(Mat125):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中的蓝色实线显示了$y = h(x)$的图像，它在$x = {self.original_intercept}$处与正x轴相交。红色虚线代表变换$y = h({self.k}x)$。求变换后图像$y = h({self.k}x)$的x截距。'
        self.description_arabic = f'يعرض الخط الأزرق المتصل في الشكل التمثيل البياني لـ $y = h(x)$، والذي يقطع محور $x$ الموجب عند $x = {self.original_intercept}$. يمثل الخط الأحمر المتقطع التحويل $y = h({self.k}x)$. أوجد نقطة التقاطع مع محور $x$ للتمثيل البياني المحول.'
        self.description_hindi = f'चित्र में नीली ठोस रेखा $y = h(x)$ का ग्राफ प्रदर्शित करती है, जो धनात्मक x-अक्ष को $x = {self.original_intercept}$ पर प्रतिच्छेद करती है। लाल खंडित रेखा रूपांतरण $y = h({self.k}x)$ का प्रतिनिधित्व करती है। रूपांतरित ग्राफ $y = h({self.k}x)$ का x-अंतःखंड ज्ञात करें।'
        self.description_kazakh = f'Суреттегі көк тұтас сызық оң x-осін $x = {self.original_intercept}$ нүктесінде қиып өтетін $y = h(x)$ графигін көрсетеді. Қызыл үзік сызық $y = h({self.k}x)$ түрлендіруін білдіреді. Түрлендірілген $y = h({self.k}x)$ графигінің x-осімен қиылысу нүктесін табыңыз.'
        self.description_swahili = f'Mstari wa bluu usiopungua katika kielelezo unaonyesha grafu ya $y = h(x)$, ambayo hukata mhimili chanya wa x kwenye $x = {self.original_intercept}$. Mstari mwekundu wa mchirizo unawakilisha mageuzi (transformation) $y = h({self.k}x)$. Tafuta kigawa-x cha grafu iliyobadilishwa $y = h({self.k}x)$.'

class Mat126_multi(Mat126):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个圆由方程$(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$定义。一条切线在点$P({self.px}, {self.py})$处与该圆相切。确定这条切线的$y$截距。结果保留3位小数。'
        self.description_arabic = f'تُعرّف دائرة بالمعادلة $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$. يمس خط مماس هذه الدائرة عند النقطة $P({self.px}, {self.py})$. أوجد نقطة التقاطع مع محور $y$ لهذا المماس. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'एक वृत्त समीकरण $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$ द्वारा परिभाषित है। एक स्पर्श रेखा इस वृत्त को बिंदु $P({self.px}, {self.py})$ पर छूती है। इस स्पर्श रेखा का $y$-अंतःखंड निर्धारित करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Шеңбер $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$ теңдеуімен анықталады. Жанама сызық бұл шеңберді $P({self.px}, {self.py})$ нүктесінде жанайды. Осы жанама сызықтың $y$-осімен қиылысу нүктесін анықтаңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Duara linafafanuliwa na mlinganyo $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$. Mstari wa tanjiti unagusa duara hili kwenye nukta $P({self.px}, {self.py})$. Bainisha kigawa-y cha mstari huu wa tanjiti. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat127_multi(Mat127):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'直线${self.line_eq}$与圆${self.circle_eq}$相交于两个不同的点$A$和$B$。计算弦$AB$的长度的平方（即求$AB^2$）。结果保留3位小数。'
        self.description_arabic = f'يتقاطع الخط المستقيم ${self.line_eq}$ مع الدائرة ${self.circle_eq}$ في نقطتين مختلفتين $A$ و $B$. احسب مربع طول الوتر $AB$. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'सीधी रेखा ${self.line_eq}$ वृत्त ${self.circle_eq}$ को दो अलग-अलग बिंदुओं, $A$ और $B$ पर प्रतिच्छेद करती है। जीवा $AB$ की वर्गित लंबाई की गणना करें (अर्थात, $AB^2$ ज्ञात करें)। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'${self.line_eq}$ түзу сызығы ${self.circle_eq}$ шеңберін екі әртүрлі $A$ және $B$ нүктелерінде қиып өтеді. $AB$ хордасының квадратталған ұзындығын есептеңіз (яғни, $AB^2$ табыңыз). Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Mstari mnyoofu ${self.line_eq}$ unakata duara ${self.circle_eq}$ katika nukta mbili tofauti, $A$ na $B$. Kokotoa kipeo cha pili cha urefu wa kigwe $AB$ (yaani, tafuta $AB^2$). Toa jibu lako hadi nafasi 3 za desimali.'

class Mat128_multi(Mat128):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'考虑连接点 A({self.x1}, {self.y1}) 和 B({self.x2}, {self.y2}) 的线段 AB。线段 AB 的垂直平分线与 x 轴交于点 P。求点 P 的 x 坐标。答案精确到小数点后三位。'
        self.description_arabic = f'اعتبر القطعة المستقيمة الواصلة بين النقطتين $A({self.x1}, {self.y1})$ و $B({self.x2}, {self.y2})$. المنصف العمودي للقطعة $AB$ يقطع محور $x$ عند النقطة $P$. أوجد الإحداثي $x$ للنقطة $P$. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'बिंदुओं $A({self.x1}, {self.y1})$ और $B({self.x2}, {self.y2})$ को जोड़ने वाले रेखाखंड पर विचार करें। रेखाखंड $AB$ का लंब समद्विभाजक (perpendicular bisector) x-अक्ष को बिंदु $P$ पर काटता है। बिंदु $P$ का x-निर्देशांक ज्ञात कीजिए। अपना उत्तर 3 दशमलव स्थानों तक सही दीजिए।'
        self.description_kazakh = f'$A({self.x1}, {self.y1})$ және $B({self.x2}, {self.y2})$ нүктелерін қосатын кесіндіні қарастырыңыз. $AB$ кесіндісінің орта перпендикуляры $x$ осін $P$ нүктесінде қиып өтеді. $P$ нүктесінің $x$-координатасын (абсциссасын) анықтаңыз. Жауапты үтірден кейін үш ондық таңбаға дейінгі дәлдікпен көрсетіңіз.'
        self.description_swahili = f'Zingatia kipande cha mstari kinachounganisha nukta $A({self.x1}, {self.y1})$ na $B({self.x2}, {self.y2})$. Kigawanyi perpendicular cha kipande cha mstari $AB$ hukata mhimili wa x kwenye nukta $P$. Bainisha kiwianishi cha x cha $P$. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat129_multi(Mat129):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'方程为$(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$的圆完全位于第一象限，且与y轴恰好相切于一点。求$k$的值。'
        self.description_arabic = f'تقع دائرة معادلتها $(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ بالكامل في الربع الأول وتمس محور $y$ عند نقطة واحدة فقط. أوجد قيمة $k$.'
        self.description_hindi = f'समीकरण $(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ वाला एक वृत्त पूरी तरह से प्रथम चतुर्थांश में स्थित है और y-अक्ष को ठीक एक बिंदु पर छूता है। $k$ का मान ज्ञात करें।'
        self.description_kazakh = f'$(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ теңдеуімен берілген шеңбер толығымен бірінші ширекте жатыр және y-осін дәл бір нүктеде жанайды. $k$ мәнін табыңыз.'
        self.description_swahili = f'Duara lenye mlinganyo $(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ lipo kabisa ndani ya robo-duara ya kwanza na linagusa mhimili wa y kwenye nukta moja tu. Tafuta thamani ya $k$.'

class Mat130_multi(Mat130):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个三角形由顶点$A({self.ax}, {self.ay})$、$B({self.bx}, {self.by})$和$C({self.cx}, {self.cy})$构成。计算三角形$ABC$的精确面积。'
        self.description_arabic = f'يتكون مثلث من الرؤوس $A({self.ax}, {self.ay})$ و $B({self.bx}, {self.by})$ و $C({self.cx}, {self.cy})$. احسب المساحة الدقيقة للمثلث $ABC$.'
        self.description_hindi = f'शीर्षों $A({self.ax}, {self.ay})$, $B({self.bx}, {self.by})$, और $C({self.cx}, {self.cy})$ द्वारा एक त्रिभुज बनता है। त्रिभुज $ABC$ के सटीक क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Үшбұрыш $A({self.ax}, {self.ay})$, $B({self.bx}, {self.by})$ және $C({self.cx}, {self.cy})$ төбелерінен құралған. $ABC$ үшбұрышының дәл ауданын есептеңіз.'
        self.description_swahili = f'Pembetatu inaundwa na vilele $A({self.ax}, {self.ay})$, $B({self.bx}, {self.by})$, na $C({self.cx}, {self.cy})$. Kokotoa eneo kamili la pembetatu $ABC$.'

class Mat131_multi(Mat131):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个圆扇形和一个正方形。该正方形的构建使得其总周长完全等于扇形的总周长。确定正方形的面积（单位：cm$^2$）。结果保留3位小数。'
        self.description_arabic = 'يوضح الشكل قطاعًا دائريًا ومربعًا. صُمم المربع بحيث يكون محيطه مساويًا تمامًا لمحيط القطاع. أوجد مساحة المربع بوحدة $cm^2$. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र एक वृत्त का एक त्रिज्यखंड और एक वर्ग दिखाता है। वर्ग इस प्रकार बनाया गया है कि इसका कुल परिमाप त्रिज्यखंड के कुल परिमाप के बिल्कुल बराबर है। वर्ग का क्षेत्रफल cm$^2$ में निर्धारित करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте шеңбер секторы және квадрат көрсетілген. Квадрат оның жалпы периметрі сектордың жалпы периметріне дәл тең болатындай етіп салынған. Квадраттың ауданын см$^2$-мен анықтаңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha sekta ya duara na mraba. Mraba umeundwa kiasi kwamba mzingo wake wote ni sawa kabisa na mzingo wote wa sekta hiyo. Bainisha eneo la mraba katika cm$^2$. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat132_multi(Mat132):
    def __init__(self):
        super().__init__()
        self.description_chinese = '汽车的后窗雨刷清理出一个形状像部分圆环的区域，如图中阴影区域所示。该区域由两个具有相同圆心角$\\theta$的同心圆弧组成。被清理区域的内半径为$r$ cm。利用图中提供的信息，计算内半径$r$的值。'
        self.description_arabic = 'تنظف ماسحة النافذة الخلفية لسيارة منطقة على شكل جزء من حلقة كما هو موضح. تتكون المنطقة من قوسين متحدي المركز لهما نفس الزاوية المركزية $\\theta$. نصف القطر الداخلي هو $r$ سم. احسب قيمة $r$.'
        self.description_hindi = 'कार के लिए एक रियर विंडो वाइपर एक क्षेत्र को साफ करता है जिसका आकार एक एनलस (एक वलय) के हिस्से जैसा होता है, जैसा कि चित्र के छायांकित क्षेत्र में दिखाया गया है। यह क्षेत्र समान केंद्रीय कोण $\\theta$ वाले दो संकेंद्रित चापों द्वारा बनता है। साफ किए गए क्षेत्र की आंतरिक त्रिज्या $r$ cm है। चित्र में दी गई जानकारी का उपयोग करते हुए, आंतरिक त्रिज्या $r$ के मान की गणना करें।'
        self.description_kazakh = 'Көліктің артқы әйнек тазалағышы суреттің боялған бөлігінде көрсетілгендей сақинаның (аннулус) бір бөлігі тәрізді аймақты тазартады. Аймақ бірдей орталық $\\theta$ бұрышы бар екі концентрлік доғадан құралған. Тазартылған аймақтың ішкі радиусы - $r$ см. Суретте берілген ақпаратты пайдалана отырып, ішкі $r$ радиусының мәнін есептеңіз.'
        self.description_swahili = 'Wipa wa kioo cha nyuma cha gari husafisha sehemu yenye umbo kama kipande cha anulasi (pete), kama inavyoonyeshwa kwenye eneo lililotiwa kivuli kielelezoni. Sehemu hiyo inaundwa na matao mawili kitovu-mamoja yenye pembe kuu sawa $\\theta$. Rediasi ya ndani ya sehemu iliyosafishwa ni $r$ sm. Kwa kutumia taarifa zilizotolewa kwenye kielelezo, kokotoa thamani ya rediasi ya ndani $r$.'

class Mat133_multi(Mat133):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示剪下一个纸扇形。将该扇形的直边（半径）无重叠地连接在一起，形成直圆锥的曲面。计算所得圆锥的底面半径（$r$）（单位：cm）。结果保留3位小数。'
        self.description_arabic = 'قُطع قطاع ورقي كما هو موضح. تُجمع الحواف المستقيمة دون تداخل لتكوين السطح الجانبي لمخروط دائري قائم. احسب نصف قطر القاعدة $r$ بالسنتيمتر. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'कागज का एक त्रिज्यखंड काटा जाता है जैसा कि चित्र में दिखाया गया है। त्रिज्यखंड के सीधे किनारों (त्रिज्याओं) को बिना किसी ओवरलैप के एक साथ जोड़ा जाता है ताकि एक लंब वृत्तीय शंकु का घुमावदार पृष्ठ बन सके। परिणामी शंकु की आधार त्रिज्या ($r$) की cm में गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Қағаз секторы суретте көрсетілгендей қиылып алынған. Сектордың түзу жиектері (радиустары) тік дөңгелек конустың қисық бетін құру үшін бір-біріне қабаттаспай біріктіріледі. Пайда болған конустың табан радиусын ($r$) см-мен есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Sekta ya karatasi inakatwa kama inavyoonyeshwa kwenye kielelezo. Kingo mnyoofu (rediasi) za sekta hiyo zinaunganishwa bila kupishana ili kuunda uso uliopinda wa pia duara ya wima. Kokotoa rediasi ya kitako ($r$) ya pia inayotokana katika sm. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat134_multi(Mat134):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了第一象限中的曲线$y = f(x)$。在点$P$处绘制了该曲线的一条法线。此法线与x轴交于点$A$，与y轴交于点$B$，与坐标轴形成三角形$AOB$。计算三角形$AOB$的面积。结果保留3位小数。'
        self.description_arabic = 'يعرض الشكل منحنى $y = f(x)$ في الربع الأول. رُسم عمود (ناظم) على المنحنى عند النقطة $P$، ويقطع المحورين عند $A$ و $B$ مكوِّنًا المثلث $AOB$. احسب مساحة المثلث $AOB$. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र प्रथम चतुर्थांश में एक वक्र $y = f(x)$ प्रदर्शित करता है। बिंदु $P$ पर वक्र के लिए एक अभिलंब रेखा खींची जाती है। यह अभिलंब रेखा x-अक्ष को बिंदु $A$ पर और y-अक्ष को बिंदु $B$ पर प्रतिच्छेद करती है, जिससे समन्वय अक्षों के साथ एक त्रिभुज $AOB$ बनता है। त्रिभुज $AOB$ के क्षेत्रफल की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте бірінші ширектегі $y = f(x)$ қисығы көрсетілген. Қисыққа $P$ нүктесінде нормаль сызық жүргізілген. Бұл нормаль сызық x-осін $A$ нүктесінде және y-осін $B$ нүктесінде қиып өтіп, координата осьтерімен $AOB$ үшбұрышын құрайды. $AOB$ үшбұрышының ауданын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mzingo $y = f(x)$ katika robo-duara ya kwanza. Mstari wa kawaida (normal line) umechora kwenye mzingo huo katika nukta $P$. Mstari huu wa kawaida hukata mhimili wa x kwenye nukta $A$ na mhimili wa y kwenye nukta $B$, na kuunda pembetatu $AOB$ pamoja na mihimili ya viwianishi. Kokotoa eneo la pembetatu $AOB$. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat135_multi(Mat135):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图展示了海面上的圆形漏油。漏油正在扩散，其半径$r$以恒定速率增加。利用图表中提供的测量值，求在这一瞬间面积的增加率（$dA/dt$）（单位：m$^2$/s）。（将最终答案除以$\\pi$）。结果保留2位小数。'
        self.description_arabic = 'يوضح الشكل بقعة زيت دائرية تتسع بحيث يزداد نصف قطرها $r$ بمعدل ثابت. باستخدام المعطيات، أوجد معدل تغير المساحة $dA/dt$ بوحدة m$^2$/s. (اقسم إجابتك على $\\pi$). أعطِ إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = 'चित्र समुद्र की सतह पर एक गोलाकार तेल रिसाव को दर्शाता है। रिसाव इस प्रकार फैल रहा है कि इसकी त्रिज्या $r$ एक निरंतर दर से बढ़ रही है। चित्र में दिए गए मापों का उपयोग करते हुए, इस क्षण में क्षेत्रफल में वृद्धि की दर ($dA/dt$) m$^2$/s में ज्ञात करें। (अपने अंतिम उत्तर को $\\pi$ से विभाजित करें)। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте мұхит бетіндегі дөңгелек мұнай төгіндісі көрсетілген. Төгінді кеңейіп жатыр, оның $r$ радиусы тұрақты жылдамдықпен өсуде. Суретте берілген өлшемдерді пайдалана отырып, осы сәттегі ауданның өсу жылдамдығын ($dA/dt$) м$^2$/с-пен табыңыз. (Соңғы жауабыңызды $\\pi$-ге бөліңіз). Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mwagiko wa mafuta wa duara juu ya uso wa bahari. Mwagiko unapanuka kiasi kwamba rediasi yake $r$ inaongezeka kwa kiwango thabiti. Kwa kutumia vipimo vilivyotolewa kwenye kielelezo, tafuta kiwango cha kuongezeka kwa eneo ($dA/dt$) katika m$^2$/s wakati huo mahususi. (Gawanya jibu lako la mwisho kwa $\\pi$). Toa jibu lako hadi nafasi 2 za desimali.'

class Mat136_multi(Mat136):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个无盖盒子的展开图，该盒子由一块方形金属板制成，在其四个角切去边长为$x$的相等正方形并将折翼向上折叠而成。根据图中提供的尺寸，求使体积$V$最大时的$x$值。结果保留3位小数。'
        self.description_arabic = 'يوضح الشكل شبكة لصندوق مفتوح من الأعلى ناتج عن قطع مربعات ضلعها $x$ من الزوايا ثم طي الجوانب. أوجد قيمة $x$ التي تجعل الحجم أعظميًا. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र धातु की एक वर्गाकार शीट से कोनों से $x$ भुजा वाले समान वर्गों को काटकर और फ्लैप्स को ऊपर मोड़कर बनाए गए एक खुले शीर्ष वाले बॉक्स के लिए एक नेट दिखाता है। चित्र में दिए गए आयामों के आधार पर, $x$ का वह मान ज्ञात करें जिसके लिए आयतन $V$ अधिकतम हो। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте металлдың квадрат парағының бұрыштарынан қабырғасы $x$ болатын бірдей квадраттарды қиып алып, жапқыштарын жоғары бүгу арқылы жасалған үсті ашық қораптың жазбасы көрсетілген. Суретте берілген өлшемдерге сүйене отырып, $V$ көлемі максималды болатындай $x$ мәнін табыңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mchoro wa mparandiko wa sanduku lisilo na kifuniko lililotengenezwa kutokana na bapa la mraba la chuma kwa kukata miraba sawa ya upande $x$ kwenye kila kona na kukunja kuta zake. Kulingana na vipimo vilivyotolewa kwenye kielelezo, tafuta thamani ya $x$ inayofanya ujazo $V$ kuwa mkubwa kabisa (maximum). Toa jibu lako hadi nafasi 3 za desimali.'

class Mat137_multi(Mat137):
    def __init__(self):
        super().__init__()
        self.description_chinese = "该图显示了两个线性函数，$f(x)$和$g(x)$。令$h(x) = f(g(x))$。利用坐标和图中指示的点，计算在标记的$x$值处$h'(x)$的值。结果保留3位小数。"
        self.description_arabic = "يعرض الشكل دالتين $f(x)$ و $g(x)$. لتكن $h(x) = f(g(x))$. باستخدام المعطيات، احسب قيمة $h'(x)$ عند القيمة المحددة. أعطِ إجابتك مقربة إلى 3 منازل عشرية."
        self.description_hindi = "चित्र दो रैखिक फलन, $f(x)$ और $g(x)$ प्रदर्शित करता है। मान लीजिए $h(x) = f(g(x))$ है। चित्र में निर्देशांकों और इंगित बिंदु का उपयोग करते हुए, चिह्नित $x$-मान पर $h'(x)$ के मान की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।"
        self.description_kazakh = "Суретте екі сызықтық $f(x)$ және $g(x)$ функциялары көрсетілген. $h(x) = f(g(x))$ болсын. Координаталарды және суретте көрсетілген нүктені пайдалана отырып, белгіленген $x$ мәніндегі $h'(x)$ мәнін есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз."
        self.description_swahili = 'Kielelezo kinaonyesha fumbuo mnyoofu mbili, $f(x)$ na $g(x)$. Iwe $h(x) = f(g(x))$. Kwa kutumia viwianishi na nukta iliyoonyeshwa kwenye kielelezo, kokotoa thamani ya $h\'(x)$ kwenye thamani ya $x$ iliyowekewa alama. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat138_multi(Mat138):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了第一象限内的一个阴影区域，上方由抛物线函数$f(x)$围成，下方由x轴围成。利用图中提供的信息和函数，计算阴影区域的总面积。结果保留3位小数。'
        self.description_arabic = 'يعرض الشكل منطقة مظللة في الربع الأول يحدها منحنى قطع مكافئ ومحور $x$. احسب المساحة الكلية للمنطقة. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र प्रथम चतुर्थांश में एक छायांकित क्षेत्र प्रदर्शित करता है जो ऊपर से एक परवलीय फलन $f(x)$ द्वारा और नीचे से x-अक्ष द्वारा परिबद्ध है। चित्र में दी गई जानकारी और फलन का उपयोग करते हुए, छायांकित क्षेत्र के कुल क्षेत्रफल की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте бірінші ширектегі жоғарыдан параболалық $f(x)$ функциясымен, ал төменнен x-осімен шектелген боялған аймақ көрсетілген. Суретте берілген ақпаратты және функцияны пайдалана отырып, боялған аймақтың жалпы ауданын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha eneo lililotiwa kivuli katika robo-duara ya kwanza lililofungwa juu na fumbuo ya parabola $f(x)$ na chini na mhimili wa x. Kwa kutumia taarifa na fumbuo iliyotolewa kwenye kielelezo, kokotoa jumla ya eneo la sehemu iliyotiwa kivuli. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat139_multi(Mat139):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一段时间内速度函数$v(t)$（单位：m/s）的图像。利用速度-时间图中提供的坐标，计算物体在显示的整个持续时间内的总位移。'
        self.description_arabic = 'يوضح الشكل التمثيل البياني لدالة السرعة $v(t)$. باستخدام مخطط السرعة-الزمن، احسب الإزاحة الكلية خلال الفترة المعطاة.'
        self.description_hindi = 'चित्र समय के एक अंतराल पर एक वेग फलन $v(t)$ (m/s में) का ग्राफ दिखाता है। वेग-समय ग्राफ में दिए गए निर्देशांकों का उपयोग करते हुए, दिखाई गई संपूर्ण अवधि में वस्तु के कुल विस्थापन की गणना करें।'
        self.description_kazakh = 'Суретте уақыт аралығындағы $v(t)$ жылдамдық функциясының (м/с-пен) графигі көрсетілген. Жылдамдық-уақыт графигінде берілген координаталарды пайдалана отырып, көрсетілген толық уақыт ішіндегі объектінің жалпы орын ауыстыруын есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya fumbuo ya velositi $v(t)$ (katika m/s) kwa kipindi fulani cha muda. Kwa kutumia viwianishi vilivyotolewa kwenye grafu ya velositi dhidi ya muda, kokotoa jumla ya msoguo (total displacement) wa kitu hicho kwa muda wote ulioonyeshwa.'

class Mat140_multi(Mat140):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图说明了通过将特定的2D区域绕x轴旋转而形成的立体3D图形。根据图中指示的函数、垂直线和旋转，计算所得立体的体积。结果保留3位小数。（以$\\pi \\approx 3.14159$）。'
        self.description_arabic = 'يوضح الشكل مجسمًا ثلاثي الأبعاد ناتجًا عن دوران منطقة ثنائية الأبعاد حول محور $x$. بناءً على الدالة والخط العمودي والدوران الموضح في الشكل، احسب حجم المجسم الناتج. أعطِ إجابتك كعدد عشري مقرب إلى ثلاثة منازل. (استخدم $\\pi \\approx 3.14159$).'
        self.description_hindi = 'चित्र एक विशिष्ट 2D क्षेत्र को x-अक्ष के चारों ओर घुमाकर बनाए गए एक ठोस 3D आकार को दर्शाता है। चित्र में इंगित फलन, ऊर्ध्वाधर रेखा, और घूर्णन के आधार पर, परिणामी ठोस के आयतन की गणना करें। अपना उत्तर तीन स्थानों तक पूर्णांकित दशमलव के रूप में दें। ($\\pi \\approx 3.14159$ का उपयोग करें)।'
        self.description_kazakh = 'Суретте белгілі бір 2D аймағын x-осінен айналдыру арқылы пайда болған тұтас 3D фигурасы көрсетілген. Суретте көрсетілген функцияға, тік сызыққа және айналдыруға сүйене отырып, пайда болған дененің көлемін есептеңіз. Жауабыңызды үш ондық таңбаға дейін дөңгелетілген бөлшек түрінде беріңіз. ($\\pi \\approx 3.14159$ пайдаланыңыз).'
        self.description_swahili = f'Kielelezo kinaonyesha umbo thabiti la 3D lililoundwa kwa kuzungusha sehemu maalum ya 2D kuzunguka mhimili wa x. Kulingana na fumbuo, mstari wa wima, na mzunguko ulioonyeshwa kwenye kielelezo, kokotoa ujazo wa umbo thabiti linalotokana. Toa jibu lako kama desimali iliyokadiriwa hadi nafasi tatu. (Tumia $\\pi \\approx 3.14159$).'

class Mat141_multi(Mat141):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'变量$x$和$y$满足关系式$y = k a^x$，其中$k$和$a$是常数。如图所示，$\\ln y$对$x$的图像是一条经过点$({self.x1}, {self.lny1})$和$({self.x2}, {self.lny2})$的直线。求$a$的值。'
        self.description_arabic = f'المتغيران $x$ و $y$ يحققان العلاقة $y = k a^x$، حيث $k$ و $a$ ثابتان. كما هو موضح في الشكل، فإن التمثيل البياني لـ $\\ln y$ بدلالة $x$ خط مستقيم يمر بالنقطتين $({self.x1}, {self.lny1})$ و $({self.x2}, {self.lny2})$. أوجد قيمة $a$.'
        self.description_hindi = f'चर $x$ और $y$ संबंध $y = k a^x$ को संतुष्ट करते हैं, जहाँ $k$ और $a$ स्थिरांक हैं। जैसा कि चित्र में दिखाया गया है, $x$ के विरुद्ध $\\ln y$ का ग्राफ एक सीधी रेखा है जो बिंदुओं $({self.x1}, {self.lny1})$ और $({self.x2}, {self.lny2})$ से होकर गुजरती है। $a$ का मान ज्ञात करें।'
        self.description_kazakh = f'$x$ және $y$ айнымалылары $y = k a^x$ байланысын қанағаттандырады, мұндағы $k$ және $a$ - тұрақтылар. Суретте көрсетілгендей, $\\ln y$-тің $x$-ке тәуелділік графигі $({self.x1}, {self.lny1})$ және $({self.x2}, {self.lny2})$ нүктелері арқылы өтетін түзу сызық болып табылады. $a$ мәнін табыңыз.'
        self.description_swahili = f'Vigezo $x$ na $y$ vinakidhi uhusiano $y = k a^x$, ambapo $k$ na $a$ ni konstanti. Kama inavyoonyeshwa kwenye kielelezo, grafu ya $\\ln y$ dhidi ya $x$ ni mstari mnyoofu unaopita kwenye nukta $({self.x1}, {self.lny1})$ na $({self.x2}, {self.lny2})$. Tafuta thamani ya $a$.'

class Mat142_multi(Mat142):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，细菌培养物的增长通过模型$N = {self.n0} \\times {self.b}^{{{self.k}t}}$表示，其中$N$是$t$小时后的细菌数量。根据该图，求出使种群数量超过{self.threshold}的最小整数值$t$。'
        self.description_arabic = f'كما هو موضح في الشكل، يُنمذج نمو مزرعة بكتيرية بواسطة $N = {self.n0} \\times {self.b}^{{{self.k}t}}$، حيث $N$ هو عدد البكتيريا بعد $t$ ساعة. بناءً على الشكل، أوجد أصغر قيمة صحيحة لـ $t$ يتجاوز عندها عدد البكتيريا {self.threshold}.'
        self.description_hindi = f'जैसा कि चित्र में दिखाया गया है, एक जीवाणु संवर्धन की वृद्धि को $N = {self.n0} \\times {self.b}^{{{self.k}t}}$ द्वारा प्रतिरूपित किया गया है, जहाँ $t$ घंटों के बाद बैक्टीरिया की संख्या $N$ है। चित्र के आधार पर, $t$ का सबसे छोटा पूर्णांक मान ज्ञात करें जिसके लिए जनसंख्या {self.threshold} से अधिक हो जाती है।'
        self.description_kazakh = f'Суретте көрсетілгендей, бактерия өсіндісінің өсуі $N = {self.n0} \\times {self.b}^{{{self.k}t}}$ формуласымен модельденеді, мұндағы $N$ - $t$ сағаттан кейінгі бактериялар саны. Суретке сүйене отырып, популяция {self.threshold} мәнінен асатындай $t$-ның ең кіші бүтін мәнін табыңыз.'
        self.description_swahili = f'Kama inavyoonyeshwa kwenye kielelezo, ukuaji wa kundi la bakteria unabainishwa na mlinganyo $N = {self.n0} \\times {self.b}^{{{self.k}t}}$, ambapo $N$ ni idadi ya bakteria baada ya saa $t$. Kulingana na kielelezo, tafuta thamani ndogo zaidi ya namba nzima ya $t$ ambayo inafanya idadi hiyo kuzidi {self.threshold}.'

class Mat143_multi(Mat143):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，放射性物质按照模型$N = 100e^{{-\\lambda t}}$衰变，其中$N$是$t$年后剩余物质的百分比。根据曲线上指示点的坐标，求衰变常数$\\lambda$的值。结果保留4位小数。'
        self.description_arabic = f'كما هو موضح في الشكل، تضمحل مادة مشعة وفقًا للنموذج $N = 100e^{{-\\lambda t}}$، حيث $N$ هي النسبة المئوية للمادة المتبقية بعد $t$ سنة. بناءً على إحداثي النقطة المشار إليها على المنحنى، أوجد قيمة ثابت الاضمحلال $\\lambda$. أعطِ إجابتك مقربة إلى أربعة منازل عشرية.'
        self.description_hindi = f'जैसा कि चित्र में दिखाया गया है, एक रेडियोधर्मी पदार्थ मॉडल $N = 100e^{{-\\lambda t}}$ के अनुसार क्षय होता है, जहाँ $t$ वर्षों के बाद शेष बचे पदार्थ का प्रतिशत $N$ है। वक्र पर इंगित बिंदु के निर्देशांक के आधार पर, क्षय नियतांक $\\lambda$ का मान ज्ञात करें। अपना उत्तर चार दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Суретте көрсетілгендей, радиоактивті зат $N = 100e^{{-\\lambda t}}$ моделіне сәйкес ыдырайды, мұндағы $N$ - $t$ жылдан кейін қалған заттың пайызы. Қисықта көрсетілген нүктенің координатасына сүйене отырып, ыдырау тұрақтысы $\\lambda$ мәнін табыңыз. Жауабыңызды төрт ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kama inavyoonyeshwa kwenye kielelezo, dutu nururifu hufifia kulingana na mlinganyo $N = 100e^{{-\\lambda t}}$, ambapo $N$ ni asilimia ya dutu inayobaki baada ya miaka $t$. Kulingana na kiwianishi cha nukta iliyoonyeshwa kwenye mzingo huo, tafuta thamani ya konstanti ya mfifio $\\lambda$. Toa jibu lako hadi nafasi nne za desimali.'

class Mat144_multi(Mat144):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个由曲线、$x$轴和两条垂直线围成的区域。求这个阴影区域的精确面积。'
        self.description_arabic = 'يوضح الشكل منطقة يحدها منحنى ومحور $x$ وخطان عموديان. أوجد المساحة الدقيقة لهذه المنطقة المظللة.'
        self.description_hindi = 'चित्र एक वक्र, $x$-अक्ष, और दो ऊर्ध्वाधर रेखाओं द्वारा परिबद्ध एक क्षेत्र दिखाता है। इस छायांकित क्षेत्र का सटीक क्षेत्रफल ज्ञात करें।'
        self.description_kazakh = 'Суретте қисықпен, $x$-осімен және екі тік сызықпен шектелген аймақ көрсетілген. Осы боялған аймақтың дәл ауданын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha eneo lililofungwa na mzingo, mhimili wa $x$, na mistari miwili ya wima. Tafuta eneo kamili la sehemu hii iliyotiwa kivuli.'

class Mat145_multi(Mat145):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了一个3次多项式函数$y = f(x)$的图像。利用图上显示的点的坐标，使用{self.n}个区间的梯形法则估计定积分$\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$的值。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة كثيرة الحدود $y = f(x)$ من الدرجة 3. باستخدام إحداثيات النقاط الموضحة، استخدم قاعدة شبه المنحرف مع {self.n} فترات لتقدير قيمة التكامل المحدود $\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$.'
        self.description_hindi = f'चित्र 3 डिग्री के एक बहुपद फलन $y = f(x)$ का ग्राफ दिखाता है। ग्राफ पर दिखाए गए बिंदुओं के निर्देशांकों का उपयोग करते हुए, निश्चित समाकलन $\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$ के मान का अनुमान लगाने के लिए {self.n} अंतरालों के साथ समलंब नियम का उपयोग करें।'
        self.description_kazakh = f'Суретте 3-дәрежелі $y = f(x)$ көпмүшелік функциясының графигі көрсетілген. Графикте көрсетілген нүктелердің координаталарын пайдаланып, $\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$ анықталған интегралының мәнін бағалау үшін {self.n} аралығы бар трапеция ережесін қолданыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya fumbuo ya polinomiali $y = f(x)$ ya shahada ya 3. Kwa kutumia viwianishi vya nukta zilizoonyeshwa kwenye grafu, tumia kanuni ya trapeza yenye vipindi {self.n} kukadiria thamani ya integreto maalum $\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$.'

class Mat146_multi(Mat146):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中所示曲线为 $y = f(x)$。区域 $R$ 由曲线 $y = f(x)$、$x$ 轴以及直线 $x=0$ 和 $x=k$ 所围成。若区域 $R$ 的面积恰好为 $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$，求 $k$ 的值。'
        self.description_arabic = f'يوضح الشكل المنحنى $y = f(x)$. المنطقة $R$ محصورة بين المنحنى ومحور $x$ والخطين $x = 0$ و $x = k$. إذا كانت مساحة المنطقة $R$ تساوي $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$، فأوجد قيمة $k$.'
        self.description_hindi = f'आकृति में वक्र $y = f(x)$ दर्शाया गया है। क्षेत्र $R$ वक्र, $x$-अक्ष और रेखाओं $x=0$ तथा $x=k$ से घिरा हुआ है। यदि क्षेत्र $R$ का क्षेत्रफल ठीक $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$ है, तो $k$ का मान ज्ञात करें।'
        self.description_kazakh = f'Сызбада $y = f(x)$ қисығы көрсетілген. $R$ аймағы осы қисықпен, $x$ осімен және $x=0$, $x=k$ түзулерімен шектелген. Егер $R$ аймағының ауданы дәл $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$ мәніне тең болса, $k$-ның мәнін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mzingo $y = f(x)$. Sehemu $R$ imefungwa na mzingo huo, mhimili wa $x$, na mistari $x=0$ na $x=k$. Ikiwa eneo la sehemu $R$ ni $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$ kamili, bainisha thamani ya $k$.'

class Mat147_multi(Mat147):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了当$x \\ge 0$时周期函数$y = f(x)$的图像。计算由曲线和$x$轴围成的从$x = 0$到指示上限的阴影区域的面积。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة دورية $y = f(x)$ حيث $x \\ge 0$. احسب مساحة المنطقة المظللة المحصورة بين المنحنى ومحور $x$ من $x = 0$ حتى الحد المشار إليه.'
        self.description_hindi = f'चित्र $x \\ge 0$ के लिए एक आवर्ती फलन $y = f(x)$ का ग्राफ दिखाता है। वक्र और $x = 0$ से इंगित सीमा तक $x$-अक्ष द्वारा परिबद्ध छायांकित क्षेत्र के क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Суретте $x \\ge 0$ үшін периодты $y = f(x)$ функциясының графигі көрсетілген. $x = 0$-ден көрсетілген шекке дейін қисықпен және $x$-осімен шектелген боялған аймақтың ауданын есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya fumbuo kigeugeu $y = f(x)$ kwa $x \\ge 0$. Kokotoa eneo la sehemu iliyotiwa kivuli lililofungwa na mzingo na mhimili wa $x$ kutoka $x = 0$ hadi kwenye kikomo kilichoonyeshwa.'

class Mat148_multi(Mat148):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了连续函数 $y = f(x)$ 在局部区域上的图像。确定图中所示的整数 $n$，使得方程 $f(x) = 0$ 的根存在于区间 $[n, n+1]$ 内。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة متصلة $y = f(x)$ على مجال محدد. حدّد العدد الصحيح {self.extremum_type} $n$ بحيث يوجد جذر للمعادلة $f(x) = 0$ في الفترة $[n, n+1]$.'
        self.description_hindi = f'चित्र में एक सतत फलन $y = f(x)$ का स्थानीय डोमेन पर ग्राफ दर्शाया गया है। चित्र में दिखाई देने वाले उस **{self.extremum_type}** पूर्णांक $n$ को पहचानिए जिसके लिए अंतराल $[n, n+1]$ में समीकरण $f(x) = 0$ का एक मूल मौजूद हो।'
        self.description_kazakh = f'Сызбада $y = f(x)$ үздіксіз функциясының белгілі бір аралықтағы графигі көрсетілген. $f(x) = 0$ теңдеуінің түбірі $[n, n+1]$ аралығында жататындай сызбадағы {self.extremum_type} $n$ бүтін санын анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya fumbuo endelevu $y = f(x)$ katika kikoa mahususi. Tambua namba nzima $n$ ya **{self.extremum_type}** inayoonekana kwenye kielelezo kiasi kwamba mzizi wa mlinganyo $f(x) = 0$ upo katika muda $[n, n+1]$.'

class Mat149_multi(Mat149):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了不动点迭代的蛛网图，用于近似$x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$的正根。从图中显示的$x_0$值开始，求{self.k_iterations}次迭代后的根的近似值。结果保留10位小数。'
        self.description_arabic = f'يوضح الشكل مخطط نسيج العنكبوت لتكرار نقطة ثابتة لتقريب الجذر الموجب للمعادلة $x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$. بدءًا من القيمة $x_0$ الموضحة في الشكل، أوجد تقريب الجذر بعد {self.k_iterations} تكرار. أعطِ إجابتك مقربة إلى 10 منازل عشرية.'
        self.description_hindi = f'चित्र $x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$ के धनात्मक मूल का अनुमान लगाने के लिए एक निश्चित-बिंदु पुनरावृत्ति के लिए एक कॉबवेब आरेख दिखाता है। ग्राफ में दिखाए गए मान $x_0$ से शुरू करते हुए, {self.k_iterations} पुनरावृत्तियों के बाद मूल का अनुमान ज्ञात करें। अपना उत्तर 10 दशमलव स्थानों तक दें।'
        self.description_kazakh = f'Суретте $x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$ теңдеуінің оң түбірін жуықтау үшін қозғалмайтын нүкте итерациясына арналған өрмекші торы тәрізді диаграмма көрсетілген. Графикте көрсетілген $x_0$ мәнінен бастап, {self.k_iterations} итерациядан кейінгі түбірдің жуық мәнін табыңыз. Жауабыңызды 10 ондық таңбаға дейін беріңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mchoro wa utando wa buibui (cobweb diagram) wa mikarara ya nukta thabiti kukadiria mzizi chanya wa $x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$. Kuanzia na thamani $x_0$ inayoonyeshwa kwenye grafu, tafuta makadirio ya mzizi baada ya mikarara (iterations) {self.k_iterations}. Toa jibu lako hadi nafasi 10 za desimali.'

class Mat150_multi(Mat150):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，对于从 $x_0$ 开始的迭代 $x_{{n+1}} = g(x_n)$，​​确定序列移出整数范围 $[{self.range_a}, {self.range_b}]$ 所需的迭代次数。'
        self.description_arabic = f'كما هو موضح في مخطط نسيج العنكبوت للتكرار $x_{{n+1}} = g(x_n)$ بدءًا من $x_0$، حدّد عدد التكرارات اللازمة لكي تخرج المتتالية من النطاق $[{self.range_a}, {self.range_b}]$.'
        self.description_hindi = f'जैसा कि $x_0$ से शुरू होने वाले पुनरावृति $x_{{n+1}} = g(x_n)$ के लिए कोबवेब आरेख में दिखाया गया है, अनुक्रम को पूर्णांक सीमा $[{self.range_a}, {self.range_b}]$ से बाहर जाने के लिए आवश्यक पुनरावृति की संख्या निर्धारित करें।'
        self.description_kazakh = f'Сызбадағы $x_0$ нүктесінен басталатын $x_{{n+1}} = g(x_n)$ итерациясына арналған өрмекші торы тәрізді диаграммаға қарап, тізбектің $[{self.range_a}, {self.range_b}]$ бүтін сандар аралығынан тыс шығуы үшін қажетті итерациялар санын анықтаңыз.'
        self.description_swahili = f'Kama inavyoonyeshwa kwenye mchoro wa utando wa buibui (cobweb diagram) wa mkarara $x_{{n+1}} = g(x_n)$ kuanzia $x_0$, bainisha idadi ya mikarara inayohitajika ili mfuatano uende nje ya masafa ya namba nzima $[{self.range_a}, {self.range_b}]$.'

class Mat151_multi(Mat151):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'变量$x$和$y$由方程$y = k e^{{ax}}$关联，其中$k$和$a$是常数。一条直线图像绘制在标记为$x$（水平）和$\\ln y$（垂直）的轴上。利用图中的线性图上标记的点，确定常数$a$的值。'
        self.description_arabic = f'يرتبط المتغيران $x$ و $y$ بالمعادلة $y = k e^{{ax}}$، حيث $k$ و $a$ ثابتان. يُرسم تمثيل بياني خطي على محاور مسماة $x$ (أفقي) و $\\ln y$ (رأسي). باستخدام النقاط الموضحة، أوجد قيمة $a$.'
        self.description_hindi = f'चर $x$ और $y$ समीकरण $y = k e^{{ax}}$ द्वारा संबंधित हैं, जहाँ $k$ और $a$ स्थिरांक हैं। लेबल किए गए $x$ (क्षैतिज) और $\\ln y$ (ऊर्ध्वाधर) अक्षों पर एक सीधी रेखा का ग्राफ आलेखित किया गया है। चित्र में रैखिक ग्राफ पर चिह्नित बिंदुओं का उपयोग करते हुए, स्थिरांक $a$ का मान निर्धारित करें।'
        self.description_kazakh = f'$x$ және $y$ айнымалылары $y = k e^{{ax}}$ теңдеуімен байланысқан, мұндағы $k$ және $a$ - тұрақтылар. $x$ (көлденең) және $\\ln y$ (тігінен) деп белгіленген осьтерде түзу сызық графигі сызылған. Суреттегі сызықтық графикте белгіленген нүктелерді пайдалана отырып, $a$ тұрақтысының мәнін анықтаңыз.'
        self.description_swahili = f'Vigezo $x$ na $y$ vinahusiana kwa mlinganyo $y = k e^{{ax}}$, ambapo $k$ na $a$ ni konstanti. Grafu ya mstari mnyoofu imechorwa kwenye mihimili yenye lebo ya $x$ (mlalo) na $\\ln y$ (wima). Kwa kutumia nukta zilizowekewa alama kwenye grafu hiyo ya mstari mnyoofu, bainisha thamani ya konstanti $a$.'

class Mat152_multi(Mat152):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'变量$x$和$y$满足关系式$y = Ax^n$。该图显示了一条绘制在标记为$\\lg x$（水平）和$\\lg y$（垂直）的轴上的直线，其中$\\lg$表示$\\log_{{10}}$。利用图中指示的点，求$n$的值。结果保留3位小数。'
        self.description_arabic = f'المتغيران $x$ و $y$ يحققان العلاقة $y = A x^n$. يوضح الشكل خطًا مستقيمًا مرسومًا على محاور مسماة $\\lg x$ (أفقي) و $\\lg y$ (رأسي)، حيث تشير $\\lg$ إلى $\\log_{{10}}$. باستخدام النقاط المشار إليها، أوجد قيمة $n$. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'चर $x$ और $y$ संबंध $y = Ax^n$ को संतुष्ट करते हैं। चित्र $\\lg x$ (क्षैतिज) और $\\lg y$ (ऊर्ध्वाधर) लेबल वाले अक्षों पर आलेखित एक सीधी रेखा को दिखाता है, जहाँ $\\lg$, $\\log_{{10}}$ को दर्शाता है। चित्र में इंगित बिंदुओं का उपयोग करते हुए, $n$ का मान ज्ञात करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'$x$ және $y$ айнымалылары $y = Ax^n$ байланысын қанағаттандырады. Суретте $\\lg x$ (көлденең) және $\\lg y$ (тігінен) деп белгіленген осьтерде салынған түзу сызық көрсетілген, мұндағы $\\lg$ - $\\log_{{10}}$ білдіреді. Суретте көрсетілген нүктелерді пайдалана отырып, $n$ мәнін табыңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Vigezo $x$ na $y$ vinakidhi uhusiano $y = Ax^n$. Kielelezo kinaonyesha mstari mnyoofu uliopangwa kwenye mihimili yenye lebo ya $\\lg x$ (mlalo) na $\\lg y$ (wima), ambapo $\\lg$ inawakilisha $\\log_{{10}}$. Kwa kutumia nukta zilizoonyeshwa kwenye kielelezo, tafuta thamani ya $n$. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat153_multi(Mat153):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中的矩形的长度、宽度和面积用$x$表示。根据图中提供的信息，计算$x$的数值。'
        self.description_arabic = 'يوضح الشكل مستطيلاً أبعاده ومساحته معبر عنها بدلالة $x$. بناءً على المعطيات في الشكل، أوجد القيمة العددية لـ $x$.'
        self.description_hindi = 'चित्र में एक आयत दिखाया गया है जिसकी लंबाई, चौड़ाई और क्षेत्रफल $x$ के पदों में व्यक्त किए गए हैं। आरेख में दिए गए लेबलों के आधार पर, $x$ के संख्यात्मक मान की गणना करें।'
        self.description_kazakh = 'Суретте ұзындығы, ені және ауданы $x$ арқылы өрнектелген тіктөртбұрыш көрсетілген. Диаграммада берілген белгілерге сүйене отырып, $x$-тің сандық мәнін есептеңіз.'
        self.description_swahili = f'Mstatili unaonyeshwa kwenye kielelezo ambapo urefu, upana, na eneo lake vimeelezwa kwa vigezo vya $x$. Kulingana na lebo zilizotolewa kwenye mchoro, kokotoa thamani ya namba ya $x$.'

class Mat154_multi(Mat154):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中所示为对数函数的图像。图像有一条用虚线表示的垂直渐近线，且渐近线经过图中标记的点。利用图中提供的信息，求$k$的值。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة لوغاريتمية لها مقارب عمودي ممثل بخط متقطع وتمر بنقطة معلّمة. باستخدام المعلومات في الشكل، أوجد قيمة $k$.'
        self.description_hindi = f'चित्र एक लघुगणकीय फलन का ग्राफ दिखाता है। ग्राफ में एक खंडि होकर गुजरता है। चित्र में दी गई जानकारी का उपयोग करते हुए, $k$ का मान निर्धारित करें।'
        self.description_kazakh = f'Сызбада логарифмдік функцияның графигі көрсетілген. Графиктің пунктир сызықпен белгіленген вертикаль асимптотасы бар және ол белгіленген нүкте арқылы өтеді. Сызбада берілген мәліметтерді пайдалана отырып, $k$-ның мәнін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya fumbuo ya logariti. Grafu hiyo ina asimptoti ya wima iliyoonyeshwa kwa mstari wa dashi na inapita kwenye nukta iliyowekewa alama. Kwa kutumia taarifa iliyotolewa kwenye kielelezo, bainisha thamani ya $k$.'

class Mat155_multi(Mat155):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了指数曲线$y = e^{kx}$和阴影区域$R$。该区域由曲线、坐标轴和图中标记的一条垂直线围成。计算阴影区域$R$的精确面积。结果保留3位小数。'
        self.description_arabic = 'يوضح الشكل منحنى أسيًا $y = e^{kx}$ ومنطقة مظللة $R$. المنطقة محصورة بين المنحنى والمحورين وخط رأسي. احسب المساحة الدقيقة للمنطقة $R$. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र एक चरघातांकी वक्र $y = e^{kx}$ और एक छायांकित क्षेत्र $R$ प्रदर्शित करता है। यह क्षेत्र वक्र, अक्षों और चित्र में चिह्नित एक ऊर्ध्वाधर रेखा द्वारा परिबद्ध है। छायांकित क्षेत्र $R$ के सटीक क्षेत्रफल की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте $y = e^{kx}$ экспоненциалдық қисығы және боялған $R$ аймағы көрсетілген. Аймақ қисықпен, осьтермен және суретте белгіленген тік сызықпен шектелген. Боялған $R$ аймағының дәл ауданын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mzingo wa kipeo $y = e^{{kx}}$ na sehemu iliyotiwa kivuli $R$. Sehemu hiyo imefungwa na mzingo huo, mihimili, na mstari wa wima uliowekewa alama kwenye kielelezo. Kokotoa eneo kamili la sehemu iliyotiwa kivuli $R$. Toa jibu lako hadi nafasi 3 za desimali.'

class Mat156_multi(Mat156):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一条曲线及其下方的一个阴影区域。阴影区域位于曲线和x轴之间，从原点到标记的上限。利用图中的信息，求阴影区域的面积。结果保留3位小数。'
        self.description_arabic = 'يوضح الشكل منحنى ومنطقة مظللة تحته. تقع المنطقة بين المنحنى ومحور $x$ من نقطة الأصل حتى حد علوي محدد. أوجد مساحة المنطقة المظللة. أعطِ إجابتك كعدد عشري مقرب إلى ثلاثة منازل عشرية.'
        self.description_hindi = 'चित्र एक वक्र और उसके नीचे एक छायांकित क्षेत्र दिखाता है। छायांकित क्षेत्र वक्र और x-अक्ष के बीच, मूल बिंदु से एक चिह्नित ऊपरी सीमा तक स्थित है। चित्र में दी गई जानकारी का उपयोग करते हुए, छायांकित क्षेत्र का क्षेत्रफल ज्ञात करें। अपना उत्तर तीन दशमलव स्थानों तक पूर्णांकित दशमलव के रूप में दें।'
        self.description_kazakh = 'Суретте қисық және оның астындағы боялған аймақ көрсетілген. Боялған аудан координаталар басынан белгіленген жоғарғы шекке дейін қисық пен x-осінің арасында орналасқан. Суреттегі ақпаратты пайдалана отырып, боялған аймақтың ауданын табыңыз. Жауабыңызды үш ондық таңбаға дейін дөңгелетілген бөлшек түрінде беріңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mzingo na sehemu iliyotiwa kivuli chini yake. Eneo lililotiwa kivuli lipo kati ya mzingo na mhimili wa $x$, kuanzia asili hadi kwenye kikomo cha juu kilichowekewa alama. Kwa kutumia taarifa katika kielelezo, tafuta eneo la sehemu iliyotiwa kivuli. Toa jibu lako kama desimali iliyokadiriwa hadi nafasi tatu za desimali.'

class Mat157_multi(Mat157):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图描绘了有理函数$f(x)$的图像。感兴趣的区域带有阴影，并由曲线、x轴和两条垂直线围成。根据图中的视觉信息，计算$f(x)$在阴影区间上的定积分。结果保留3位小数。'
        self.description_arabic = 'يوضح الشكل التمثيل البياني لدالة كسرية $f(x)$. المنطقة المظللة محصورة بين المنحنى ومحور $x$ وخطين عموديين. احسب التكامل المحدود للدالة على الفترة المظللة. قرّب إجابتك إلى ثلاثة منازل عشرية.'
        self.description_hindi = 'चित्र एक परिमेय फलन $f(x)$ का ग्राफ दर्शाता है। रुचि का क्षेत्र छायांकित है और वक्र, x-अक्ष और दो ऊर्ध्वाधर रेखाओं द्वारा परिबद्ध है। चित्र में दृश्य जानकारी के आधार पर, छायांकित अंतराल पर $f(x)$ के निश्चित समाकलन की गणना करें। अपने उत्तर को तीन दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = 'Суретте рационал $f(x)$ функциясының графигі бейнеленген. Қарастырылып отырған аудан боялған және қисықпен, x-осімен және екі тік сызықпен шектелген. Суреттегі визуалды ақпаратқа сүйене отырып, боялған аралықтағы $f(x)$ функциясының анықталған интегралын есептеңіз. Жауабыңызды үш ондық таңбаға дейін дөңгелетіңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya fumbuo wiano $f(x)$. Eneo linalohitajika limetiwa kivuli na limefungwa na mzingo, mhimili wa $x$, na mistari miwili ya wima. Kulingana na taarifa za kuonekana katika kielelezo, kokotoa integreto maalum ya $f(x)$ katika kipindi kilichotiwa kivuli. Kadiria jibu lako hadi nafasi tatu za desimali.'

class Mat158_multi(Mat158):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了第一象限中的一条曲线以及一个由曲线、x轴和垂直上限围成的阴影区域。利用图中提供的信息，确定阴影区域的面积。结果保留3位小数。'
        self.description_arabic = 'يوضح الشكل منحنى في الربع الأول ومنطقة مظللة يحدها المنحنى ومحور $x$ وحد رأسي. أوجد مساحة المنطقة المظللة. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र प्रथम चतुर्थांश में एक वक्र और वक्र, x-अक्ष, और एक ऊर्ध्वाधर सीमा द्वारा परिबद्ध एक छायांकित क्षेत्र दिखाता है। चित्र में दी गई जानकारी का उपयोग करते हुए, छायांकित क्षेत्र का क्षेत्रफल निर्धारित करें। अपने उत्तर को 3 दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = 'Суретте бірінші ширектегі қисық және қисықпен, x-осімен және тік шекпен шектелген боялған аймақ көрсетілген. Суретте берілген ақпаратты пайдалана отырып, боялған аймақтың ауданын анықтаңыз. Жауабыңызды 3 ондық таңбаға дейін дөңгелетіңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mzingo katika obo la kwanza na sehemu iliyotiwa kivuli iliyofungwa na mzingo huo, mhimili wa $x$, na kikomo cha wima. Kwa kutumia taarifa zilizotolewa kwenye kielelezo, bainisha eneo la sehemu iliyotiwa kivuli. Kadiria jibu lako hadi nafasi 3 za desimali.'

class Mat159_multi(Mat159):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图展示了一条钟形曲线及其下方从y轴延伸到一条标记的垂直线的阴影区域。根据图表中显示的函数和限制，计算该区域的面积。结果保留3位小数。'
        self.description_arabic = 'يوضح الشكل منحنى على شكل جرس ومنطقة مظللة تحته تمتد من محور $y$ إلى خط رأسي محدد. احسب مساحة هذه المنطقة. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र एक घंटी के आकार का वक्र और उसके नीचे y-अक्ष से चिह्नित ऊर्ध्वाधर रेखा तक फैला हुआ एक छायांकित क्षेत्र दर्शाता है। आरेख में दिखाए गए फलन और सीमा के आधार पर, इस क्षेत्र के क्षेत्रफल की गणना करें। अपने उत्तर को 3 दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = 'Суретте қоңырау тәрізді қисық және оның астындағы y-осінен белгіленген тік сызыққа дейін созылатын боялған аймақ көрсетілген. Диаграммада көрсетілген функцияға және шекке сүйене отырып, осы аймақтың ауданын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дөңгелетіңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mzingo wenye umbo la kengele na sehemu iliyotiwa kivuli chini yake kuanzia kwenye mhimili wa $y$ hadi kwenye mstari wa wima uliowekewa alama. Kulingana na fumbuo na kikomo kilichoonyeshwa kwenye mchoro, kokotoa eneo la sehemu hii. Kadiria jibu lako hadi nafasi 3 za desimali.'

class Mat160_multi(Mat160):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图显示了在一个阴影区间内三角函数$y = f(x)$的图像。求曲线下方阴影区域的面积。结果保留3位小数。'
        self.description_arabic = f'يوضح الشكل التمثيل البياني لدالة مثلثية $y = f(x)$ على فترة مظللة. أوجد مساحة المنطقة المظللة تحت المنحنى. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = f'चित्र एक छायांकित अंतराल पर एक त्रिकोणमितीय फलन (trigonometric function) $y = f(x)$ का ग्राफ दिखाता है। वक्र के नीचे छायांकित क्षेत्र का क्षेत्रफल ज्ञात करें। अपने उत्तर को 3 दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Суретте боялған аралықтағы тригонометриялық $y = f(x)$ функциясының графигі көрсетілген. Қисықтың астындағы боялған аймақтың ауданын табыңыз. Жауабыңызды 3 ондық таңбаға дейін дөңгелетіңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya fumbuo ya trigonomia $y = f(x)$ katika kipindi kilichotiwa kivuli. Tafuta eneo la sehemu iliyotiwa kivuli chini ya mzingo. Kadiria jibu lako hadi nafasi 3 za desimali.'

class Mat161_multi(Mat161):
    def __init__(self):
        super().__init__()
        self.description_chinese = "该图显示了当$x > 0$时$y = x$和$y = f(x)$的图像。一个‘蛛网’序列说明了从轴上标记的初始值$x_1$开始的迭代过程$x_{n+1} = f(x_n)$的收敛性。利用图中显示的迭代公式和初始值，计算第三次迭代的值$x_3$，结果保留3位小数。"
        self.description_arabic = "يوضح الشكل التمثيلين البيانيين لـ $y = x$ و $y = f(x)$ حيث $x > 0$. توضح متتالية 'نسيج العنكبوت' تقارب عملية تكرارية $x_{n+1} = f(x_n)$ بدءًا من قيمة ابتدائية $x_1$. باستخدام الصيغة التكرارية والقيمة الابتدائية الموضحة في الشكل، احسب قيمة التكرار الثالث $x_3$، مقربًا إلى 3 منازل عشرية."
        self.description_hindi = "आरेख $x > 0$ के लिए $y = x$ और $y = f(x)$ के ग्राफ दिखाता है। एक 'कॉबवेब' अनुक्रम अक्ष पर चिह्नित प्रारंभिक मान $x_1$ से शुरू होने वाली पुनरावृत्तीय प्रक्रिया $x_{n+1} = f(x_n)$ के अभिसरण को दर्शाता है। चित्र में दिखाए गए पुनरावृत्तीय सूत्र और प्रारंभिक मान का उपयोग करते हुए, 3 दशमलव स्थानों तक पूर्णांकित करके तीसरी पुनरावृत्ति, $x_3$, के मान की गणना करें।"
        self.description_kazakh = "Диаграммада $x > 0$ үшін $y = x$ және $y = f(x)$ графиктері көрсетілген. 'Өрмекші торы' тізбегі осьте белгіленген бастапқы $x_1$ мәнінен басталатын $x_{n+1} = f(x_n)$ итерациялық процесінің жинақтылығын бейнелейді. Суретте көрсетілген итерациялық формуланы және бастапқы мәнді пайдалана отырып, үшінші итерацияның, яғни $x_3$ мәнін 3 ондық таңбаға дейін дөңгелете отырып есептеңіз."
        self.description_swahili = f"Mchoro unaonyesha grafu za $y = x$ na $y = f(x)$ kwa $x > 0$. Mfuatano wa 'utando wa buibui' unaonyesha usikilio wa mchakato wa mikarara $x_{{n+1}} = f(x_n)$ kuanzia thamani ya awali $x_1$ iliyowekewa alama kwenye mhimili. Kwa kutumia kanuni ya mkarara na thamani ya awali iliyoonyeshwa kwenye kielelezo, kokotoa thamani ya mkarara wa tatu, $x_3$, ukikadiria hadi nafasi 3 za desimali."

class Mat162_multi(Mat162):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了曲线$y = a\\ln(x) - x + b$的草图。该曲线在两点处与$x$轴相交。较大的根$\\alpha$显示位于以单位间隔标记的$x$轴网格上的两个连续整数之间。根据图中较大根的视觉位置，识别整数$n$，使得$n < \\alpha < n+1$。'
        self.description_arabic = 'يوضح الشكل رسمًا تقريبيًا للمنحنى $y = a\\ln(x) - x + b$. يتقاطع المنحنى مع محور $x$ في نقطتين. يقع الجذر الأكبر $\\alpha$ بين عددين صحيحين متتاليين على محور $x$. بناءً على الشكل، حدد العدد الصحيح $n$ بحيث $n < \\alpha < n+1$.'
        self.description_hindi = 'चित्र वक्र $y = a\\ln(x) - x + b$ का एक रेखाचित्र दिखाता है। वक्र $x$-अक्ष को दो बिंदुओं पर प्रतिच्छेद करता है। बड़ा मूल, $\\alpha$, $x$-अक्ष ग्रिड पर दो लगातार पूर्णांकों के बीच स्थित दिखाया गया है, जिसे इकाई अंतरालों के साथ चिह्नित किया गया है। चित्र में बड़े मूल के दृश्य स्थान के आधार पर, पूर्णांक $n$ की पहचान करें ताकि $n < \\alpha < n+1$ हो।'
        self.description_kazakh = 'Суретте $y = a\\ln(x) - x + b$ қисығының нобайы көрсетілген. Қисық $x$-осін екі нүктеде қиып өтеді. Үлкенірек $\\alpha$ түбірі бірлік аралықтармен белгіленген $x$-осі торындағы екі қатар орналасқан бүтін санның арасында жатқаны көрсетілген. Суреттегі үлкенірек түбірдің визуалды орналасуына сүйене отырып, $n < \\alpha < n+1$ болатындай $n$ бүтін санын анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mchoro wa mzingo $y = a\\ln(x) - x + b$. Mzingo unakata mhimili wa $x$ katika nukta mbili. Mzizi mkubwa zaidi, $\\alpha$, unaonyeshwa kuwa upo kati ya namba nzima mbili zinazofuatana kwenye gridi ya mhimili wa $x$, ambayo imewekewa alama za vipindi vya uniti moja. Kulingana na mahali mzizi mkubwa zaidi unapoonekana kwenye kielelezo, tambua namba nzima $n$ kiasi kwamba $n < \\alpha < n+1$.'

class Mat163_multi(Mat163):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了源自3D空间中公共点$O$的两个向量。向量$\\mathbf{a}$和向量$\\mathbf{b}$如图中标注。这些向量由直角符号指示为垂直。利用图中的信息，计算常数$p$的值。'
        self.description_arabic = 'يعرض الشكل متجهين ينطلقان من نقطة مشتركة $O$ في فضاء ثلاثي الأبعاد. المتجهان $\\mathbf{a}$ و $\\mathbf{b}$ موضحان في الشكل، وهما متعامدان. باستخدام المعلومات المعطاة، احسب قيمة الثابت $p$.'
        self.description_hindi = 'चित्र 3D अंतरिक्ष में एक सामान्य बिंदु $O$ से उत्पन्न होने वाले दो सदिशों को प्रदर्शित करता है। सदिश $\\mathbf{a}$ और सदिश $\\mathbf{b}$ को आरेख में लेबल किया गया है। सदिशों को समकोण प्रतीक द्वारा लंबवत होने का संकेत दिया गया है। चित्र में दी गई जानकारी का उपयोग करते हुए, स्थिरांक $p$ के मान की गणना करें।'
        self.description_kazakh = 'Суретте 3D кеңістігіндегі ортақ $O$ нүктесінен басталатын екі вектор көрсетілген. $\\mathbf{a}$ векторы және $\\mathbf{b}$ векторы диаграммада белгіленгендей. Векторлардың перпендикуляр екендігі тік бұрыш таңбасымен көрсетілген. Суреттегі ақпаратты пайдалана отырып, $p$ тұрақтысының мәнін есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha vekta mbili zinazoanzia kwenye nukta moja $O$ katika anga la 3D. Vekta $\\mathbf{{a}}$ na vekta $\\mathbf{{b}}$ zimewekewa lebo kama kwenye mchoro. Vekta hizo zinaonyeshwa kusulubiana kwa ishara ya pembe mraba. Kwa kutumia taarifa katika kielelezo, kokotoa thamani ya konstanti $p$.'

class Mat164_multi(Mat164):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图表显示了在3D空间中相交于点$X$的两条直线$L_1$和$L_2$。直线$L_1$经过点$A$且平行于向量$\\mathbf{d_1}$。直线$L_2$经过点$B$且平行于向量$\\mathbf{d_2}$。利用图中标注的坐标和分量，求解这些直线的交点以确定常数$m$的数值。'
        self.description_arabic = 'يوضح الشكل خطين مستقيمين $L_1$ و $L_2$ يتقاطعان عند النقطة $X$ في فضاء ثلاثي الأبعاد. يمر الخط $L_1$ بالنقطة $A$ ويوازي المتجه $\\mathbf{d_1}$، ويمر الخط $L_2$ بالنقطة $B$ ويوازي المتجه $\\mathbf{d_2}$. باستخدام المعطيات، أوجد قيمة الثابت $m$.'
        self.description_hindi = 'एक आरेख 3D अंतरिक्ष में बिंदु $X$ पर प्रतिच्छेद करने वाली दो सीधी रेखाएँ $L_1$ और $L_2$ दिखाता है। रेखा $L_1$ बिंदु $A$ से होकर गुजरती है और सदिश $\\mathbf{d_1}$ के समानांतर है। रेखा $L_2$ बिंदु $B$ से होकर गुजरती है और सदिश $\\mathbf{d_2}$ के समानांतर है। आरेख में लेबल किए गए निर्देशांकों और घटकों का उपयोग करते हुए, स्थिरांक $m$ का संख्यात्मक मान निर्धारित करने के लिए इन रेखाओं के प्रतिच्छेदन को हल करें।'
        self.description_kazakh = 'Диаграммада 3D кеңістігіндегі $X$ нүктесінде қиылысатын екі $L_1$ және $L_2$ түзу сызықтары көрсетілген. $L_1$ түзуі $A$ нүктесі арқылы өтеді және $\\mathbf{d_1}$ векторына параллель. $L_2$ түзуі $B$ нүктесі арқылы өтеді және $\\mathbf{d_2}$ векторына параллель. Диаграммада белгіленген координаталар мен құраушыларды пайдалана отырып, $m$ тұрақтысының сандық мәнін анықтау үшін осы түзулердің қиылысуын шешіңіз.'
        self.description_swahili = f'Mchoro unaonyesha mistari miwili mnyoofu $L_1$ na $L_2$ inayokutana kwenye nukta $X$ katika anga la 3D. Mstari $L_1$ unapita kwenye nukta $A$ na uko sambamba na vekta $\\mathbf{{d_1}}$. Mstari $L_2$ unapita kwenye nukta $B$ na uko sambamba na vekta $\\mathbf{{d_2}}$. Kwa kutumia viwianishi na vipengele vilivyowekewa lebo kwenye mchoro, tatua makutano ya mistari hii ili kubainisha thamani ya namba ya konstanti $m$.'

class Mat165_multi(Mat165):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，三棱锥$OABC$的原点位于$O(0,0,0)$。顶点$A、B$和$C$的位置向量如图所示。点$M$是边$AB$的精确中点。向量$\\vec{MC}$将$M$连接到顶点$C$。计算向量$\\vec{MC}$的大小的平方（即计算$|\\vec{MC}|^2$）。'
        self.description_arabic = 'يوضح الشكل هرمًا ثلاثي الأبعاد $OABC$ حيث نقطة الأصل عند $O(0,0,0)$. متجهات الموضع للرؤوس $A$ و $B$ و $C$ موضحة. النقطة $M$ هي منتصف القطعة $AB$. احسب مربع مقدار المتجه $\\vec{MC}$.'
        self.description_hindi = 'एक त्रिकोणीय पिरामिड $OABC$ दिखाया गया है जिसका मूल बिंदु $O(0,0,0)$ पर है। शीर्षों $A, B,$ और $C$ के स्थिति सदिश आरेख में दिखाए गए अनुसार हैं। बिंदु $M$ किनारे $AB$ का सटीक मध्यबिंदु है। एक सदिश $\\vec{MC}$, $M$ को शीर्ष $C$ से जोड़ता है। सदिश $\\vec{MC}$ के वर्गित परिमाण की गणना करें (अर्थात, $|\\vec{MC}|^2$ की गणना करें)।'
        self.description_kazakh = 'Координаталар басы $O(0,0,0)$ нүктесінде болатын $OABC$ үшбұрышты пирамидасы көрсетілген. $A, B$ және $C$ төбелерінің радиус-векторлары диаграммада көрсетілгендей. $M$ нүктесі - $AB$ қырының дәл ортасы. $\\vec{MC}$ векторы $M$-ді $C$ төбесімен қосады. $\\vec{MC}$ векторының квадратталған ұзындығын есептеңіз (яғни, $|\\vec{MC}|^2$ есептеңіз).'
        self.description_swahili = f'Piramidi ya pembetatu $OABC$ inaonyeshwa na asili kwenye $O(0,0,0)$. Vekta nafasi za vilele $A, B,$ na $C$ zimeonyeshwa kwenye mchoro. Nukta $M$ ni nukta ya katikati kabisa ya ukingo $AB$. Vekta $\\vec{{MC}}$ inaunganisha $M$ na kilele $C$. Kokotoa mraba wa ukubwa wa vekta $\\vec{{MC}}$ (yaani, tafuta $|\\vec{{MC}}|^2$).'

class Mat166_multi(Mat166):
    def __init__(self):
        super().__init__()
        self.description_chinese = '在3D坐标系中绘制了平行四边形$ABCD$。其中三个顶点$A、B$和$C$的坐标在图中标注。第四个顶点$D$标注了未知坐标$(x, y, z)$。利用平行四边形的向量加减法性质，求顶点$D$的坐标之和（即计算$x + y + z$）。'
        self.description_arabic = 'يوضح الشكل متوازي الأضلاع $ABCD$ في نظام إحداثي ثلاثي الأبعاد. إحداثيات الرؤوس $A$ و $B$ و $C$ معطاة، بينما إحداثيات الرأس $D$ غير معروفة. باستخدام خواص المتجهات، أوجد قيمة $x + y + z$.'
        self.description_hindi = 'एक 3D समन्वय प्रणाली में एक समांतर चतुर्भुज $ABCD$ आलेखित किया गया है। तीन शीर्षों $A, B,$ और $C$ के निर्देशांक आरेख में लेबल किए गए हैं। चौथे शीर्ष $D$ को अज्ञात निर्देशांकों $(x, y, z)$ के साथ लेबल किया गया है। एक समांतर चतुर्भुज के लिए सदिश जोड़/घटाव गुणों का उपयोग करते हुए, शीर्ष $D$ के निर्देशांकों का योग ज्ञात करें (अर्थात, $x + y + z$ की गणना करें)।'
        self.description_kazakh = '$ABCD$ параллелограмы 3D координаталар жүйесінде салынған. Үш $A, B$ және $C$ төбелерінің координаталары диаграммада белгіленген. Төртінші $D$ төбесі белгісіз $(x, y, z)$ координаталарымен белгіленген. Параллелограмм үшін векторларды қосу/азайту қасиеттерін пайдалана отырып, $D$ төбесі координаталарының қосындысын табыңыз (яғни, $x + y + z$ есептеңіз).'
        self.description_swahili = f'Msambamba $ABCD$ umechorwa katika mfumo wa viwianishi vya 3D. Viwianishi vya vilele vitatu $A, B,$ na $C$ vimeonyeshwa kwenye mchoro. Kilele cha nne $D$ kina viwianishi zisizojulikana $(x, y, z)$. Kwa kutumia sifa za kujumlisha au kutoa vekta kwa msambamba, tafuta jumla ya viwianishi vya kilele $D$ (yaani, kokotoa $x + y + z$).'

class Mat167_multi(Mat167):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了阿干图中的一个正方形，其顶点按逆时针顺序标记为$O$、$P$、$Q$和$R$。$O$是原点。如标签中规定，顶点$P$代表复数$z_1$。\n\n如果这些顶点构成正方形$OPQR$，确定由顶点$R$代表的复数的虚部。'
        self.description_arabic = 'يوضح الشكل مربعًا في مخطط أرجاند برؤوس $O$ و $P$ و $Q$ و $R$ بترتيب عكس اتجاه عقارب الساعة، حيث $O$ هي نقطة الأصل و $P$ يمثل العدد المركب $z_1$. أوجد الجزء التخيلي للعدد المركب الذي يمثله الرأس $R$.'
        self.description_hindi = 'आकृति में आर्गंड (Argand) आरेख में एक वर्ग दिखाया गया है जिसके शीर्षों को वामावर्त क्रम में $O$, $P$, $Q$ और $R$ से अंकित किया गया है। $O$ मूल बिंदु है। शीर्ष $P$ जटिल संख्या $z_1$ को दर्शाता है, जैसा कि लेबल में निर्दिष्ट है।\n\nयदि शीर्ष एक वर्ग $OPQR$ बनाते हैं, तो शीर्ष $R$ द्वारा दर्शाई गई जटिल संख्या का काल्पनिक भाग ज्ञात करें।'
        self.description_kazakh = 'Суретте сағат тіліне қарсы бағытта $O$, $P$, $Q$ және $R$ деп белгіленген төбелері бар Арганд диаграммасындағы квадрат көрсетілген. $O$ - координаталар басы. $P$ төбесі белгіде көрсетілгендей $z_1$ кешен санын білдіреді.\n\nЕгер төбелер $OPQR$ квадратын құраса, $R$ төбесі білдіретін кешен санның жорамал бөлігін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mraba katika mchoro wa Argand wenye vilele vilivyowekewa lebo $O, P, Q,$ na $R$ kinyume cha mwelekeo wa saa. $O$ ni asili. Kilele $P$ kinawakilisha namba changamano $z_1$, kama ilivyoainishwa kwenye lebo.\n\nIkiwa vilele hivyo vinaunda mraba $OPQR$, bainisha sehemu dhahania ya namba changamano inayowakilishwa na kilele $R$.'

class Mat168_multi(Mat168):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个带有圆和垂直线的阿干图。该圆代表由$|z - c| = r$定义的轨迹。该直线代表$\\text{Re}(z) = k$的点的轨迹。该直线在圆的右侧与圆相切。根据图中的标签，确定$k$的值。'
        self.description_arabic = 'يوضح الشكل مخطط أرجاند يحتوي على دائرة وخط عمودي. تمثل الدائرة المحل الهندسي $|z - c| = r$، ويمثل الخط المحل الهندسي حيث $\\text{Re}(z) = k$. الخط مماس للدائرة من الجهة اليمنى. أوجد قيمة $k$.'
        self.description_hindi = 'चित्र एक वृत्त और एक ऊर्ध्वाधर रेखा के साथ एक आर्गंड (Argand) आरेख प्रदर्शित करता है। वृत्त $|z - c| = r$ द्वारा परिभाषित बिंदु पथ का प्रतिनिधित्व करता है। रेखा उन बिंदुओं के पथ का प्रतिनिधित्व करती है जहाँ $\\text{Re}(z) = k$ है। रेखा वृत्त के दाहिने हिस्से पर स्पर्श रेखा है। आरेख में लेबलों के आधार पर, $k$ का मान निर्धारित करें।'
        self.description_kazakh = 'Суретте шеңбер және тік сызық бар Арганд диаграммасы көрсетілген. Шеңбер $|z - c| = r$ арқылы анықталатын геометриялық орынды білдіреді. Сызық $\\text{Re}(z) = k$ болатын нүктелердің геометриялық орнын білдіреді. Сызық шеңберді оның оң жағынан жанайды. Диаграммадағы белгілерге сүйене отырып, $k$ мәнін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mchoro wa Argand wenye duara na mstari wa wima. Duara linawakilisha loko (locus) inayofafanuliwa na $|z - c| = r$. Mstari unawakilisha loko ya nukta ambapo $\\text{{Re}}(z) = k$. Mstari huo ni tanjiti kwa duara kwenye upande wake wa kulia. Kulingana na lebo kwenye mchoro, bainisha thamani ya $k$.'

class Mat169_multi(Mat169):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个有三个点的阿干图：原点$O$、代表复数$z$的点$A$和代表其共轭复数$\\bar{z}$的点$B$。一个阴影三角形连接了这些点。利用图中标记的$z$值，计算阴影三角形的面积。'
        self.description_arabic = 'يوضح الشكل مخطط أرجاند بثلاث نقاط: $O$ نقطة الأصل، و $A$ تمثل العدد المركب $z$، و $B$ تمثل مرافقه $\\bar{z}$. احسب مساحة المثلث المحدد بهذه النقاط.'
        self.description_hindi = 'चित्र तीन बिंदुओं के साथ एक आर्गंड आरेख दिखाता है: मूल बिंदु $O$, सम्मिश्र संख्या $z$ का प्रतिनिधित्व करने वाला बिंदु $A$, और इसके संयुग्मी $\\bar{z}$ का प्रतिनिधित्व करने वाला बिंदु $B$। एक छायांकित त्रिभुज इन बिंदुओं को जोड़ता है। चित्र में लेबल किए गए $z$ के मान का उपयोग करते हुए, छायांकित त्रिभुज के क्षेत्रफल की गणना करें।'
        self.description_kazakh = 'Суретте үш нүктесі бар Арганд диаграммасы көрсетілген: координаталар басы $O$, $z$ кешен санын білдіретін $A$ нүктесі және оның түйіндесі $\\bar{z}$ білдіретін $B$ нүктесі. Боялған үшбұрыш осы нүктелерді қосады. Суретте белгіленген $z$ мәнін пайдалана отырып, боялған үшбұрыштың ауданын есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mchoro wa Argand wenye nukta tatu: asili $O$, nukta $A$ inayowakilisha namba changamano $z$, na nukta $B$ inayowakilisha pacha wake (conjugate) $\\bar{{z}}$. Pembetatu iliyotiwa kivuli inaunganisha nukta hizi. Kwa kutumia thamani ya $z$ iliyowekewa lebo kwenye kielelezo, kokotoa eneo la pembetatu iliyotiwa kivuli.'

class Mat170_multi(Mat170):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了复平面中代表轨迹的射线（半直线）。该射线起源于虚轴上的点$A$，具有如图所示的特定辐角。求该轨迹穿过实轴的$x$截距的值。结果保留3位小数。'
        self.description_arabic = 'يوضح الشكل شعاعًا يمثل محلاً هندسيًا في المستوى المركب. ينطلق الشعاع من النقطة $A$ على المحور التخيلي وله زاوية محددة. أوجد نقطة تقاطعه مع محور $x$. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र सम्मिश्र तल में एक बिंदु पथ का प्रतिनिधित्व करने वाली एक किरण दिखाता है। किरण काल्पनिक अक्ष पर बिंदु $A$ से उत्पन्न होती है और इसका एक विशिष्ट कोणांक है, जैसा कि आरेख में दिखाया गया है। $x$-अंतःखंड का वह मान ज्ञात करें जहाँ यह बिंदु पथ वास्तविक अक्ष को पार करता है। 3 दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = 'Суретте кешен жазықтықтағы геометриялық орынды білдіретін сәуле (жартылай түзу) көрсетілген. Сәуле жорамал осьтегі $A$ нүктесінен басталады және диаграммада көрсетілгендей белгілі бір аргумент бұрышына ие. Осы геометриялық орын нақты осьті қиып өтетін $x$-осімен қиылысу нүктесінің мәнін табыңыз. 3 ондық таңбаға дейін дөңгелетіңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mwale (nusu mstari) unaowakilisha loko (locus) katika bapa changamano. Mwale huo unaanzia kwenye nukta $A$ kwenye mhimili dhahania na una hoja ya pembe maalum, kama inavyoonyeshwa kwenye mchoro. Tafuta thamani ya makata ya $x$ ambapo loko hii inavuka mhimili halisi. Kadiria hadi nafasi 3 za desimali.'

class Mat171_multi(Mat171):
    def __init__(self):
        super().__init__()
        self.description_chinese = '三个共面力在如图所示的方向上作用于一点。已知力处于平衡状态，求$X$的值。'
        self.description_arabic = 'تؤثر ثلاث قوى في مستوى واحد عند نقطة في الاتجاهات الموضحة في الشكل. علمًا بأن القوى في حالة اتزان، أوجد قيمة $X$.'
        self.description_hindi = 'तीन समतलीय बल आरेख में दिखाई गई दिशाओं में एक बिंदु पर कार्य करते हैं। यह देखते हुए कि बल संतुलन में हैं, $X$ का मान ज्ञात करें।'
        self.description_kazakh = 'Бір жазықтықта жатқан үш күш бір нүктеде диаграммада көрсетілген бағыттарда әсер етеді. Күштер тепе-теңдікте екені белгілі болса, $X$ мәнін табыңыз.'
        self.description_swahili = f'Nguvu tatu sambapa zinatenda kwenye nukta moja katika mwelekeo uliOonyeshwa kwenye mchoro. Kwa kuwa nguvu hizo ziko kwenye msawazo, tafuta thamani ya $X$.'

class Mat172_multi(Mat172):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了对粒子运动进行建模的速度-时间图。粒子离开$O$，并最终在时间$T$返回$O$。根据图表和提供的信息，求$T$的值。'
        self.description_arabic = 'يوضح الشكل تمثيلًا بيانيًا للسرعة-الزمن لنمذجة حركة جسيم. يغادر الجسيم النقطة $O$ ويعود إليها عند الزمن $T$. أوجد قيمة $T$.'
        self.description_hindi = 'आरेख एक वेग-समय ग्राफ दिखाता है जो एक कण की गति को प्रतिरूपित करता है। कण $O$ से निकलता है और अंततः समय $T$ पर $O$ पर वापस आ जाता है। चित्र और दी गई जानकारी के आधार पर, $T$ का मान ज्ञात करें।'
        self.description_kazakh = 'Диаграмма бөлшектің қозғалысын модельдейтін жылдамдық-уақыт графигін көрсетеді. Бөлшек $O$ нүктесінен шығып, ақырында $T$ уақытында $O$-ға қайта оралады. Суретке және берілген ақпаратқа сүйене отырып, $T$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya velositi dhidi ya muda inayofafanua mwendo wa chembe. Chembe hiyo inaondoka $O$ na hatimaye inarudi $O$ katika muda $T$. Kulingana na kielelezo na taarifa iliyotolewa, tafuta thamani ya $T$.'

class Mat173_multi(Mat173):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，三个粒子$P、Q$和$R$在光滑水平面上同一直线处于静止状态。$P$的质量是$m_P$，$Q$是$m_Q$，$R$是$m_R$。$P$以初始速度直接向$Q$投射。$P$和$Q$碰撞后，$P$以减小的速度继续沿相同方向运动。在随后$Q$和$R$之间的碰撞中，这些粒子合并。求第二次碰撞后合并粒子的速度。'
        self.description_arabic = 'توجد ثلاثة جسيمات $P$ و $Q$ و $R$ على خط مستقيم على مستوى أفقي أملس. كتلتها $m_P$ و $m_Q$ و $m_R$. يُقذف $P$ نحو $Q$ بسرعة ابتدائية، وبعد التصادم الأول يستمر بحركة أبطأ. في التصادم الثاني بين $Q$ و $R$ يندمجان. أوجد سرعة الجسيم الناتج.'
        self.description_hindi = 'चित्र में दिखाए गए अनुसार एक चिकने क्षैतिज तल पर एक सीधी रेखा में तीन कण $P, Q$ और $R$ विरामावस्था में हैं। $P$ का द्रव्यमान $m_P$, $Q$ का $m_Q$, और $R$ का $m_R$ है। $P$ को एक प्रारंभिक गति के साथ सीधे $Q$ की ओर प्रक्षेपित किया जाता है। $P$ और $Q$ के टकराने के बाद, $P$ कम गति के साथ उसी दिशा में आगे बढ़ता रहता है। $Q$ और $R$ के बीच बाद की टक्कर में, ये कण आपस में मिल जाते हैं। इस दूसरी टक्कर के बाद संयुक्त कण की गति ज्ञात करें।'
        self.description_kazakh = 'Суретте көрсетілгендей, тегіс көлденең жазықтықта үш $P, Q$ және $R$ бөлшектері бір түзу бойында тыныштықта тұр. $P$ массасы - $m_P$, $Q$ - $m_Q$ және $R$ - $m_R$. $P$ тікелей $Q$-ға қарай бастапқы жылдамдықпен ұшырылады. $P$ және $Q$ соқтығысқаннан кейін, $P$ төмендеген жылдамдықпен сол бағытта қозғалуын жалғастырады. $Q$ мен $R$ арасындағы келесі соқтығыста бұл бөлшектер бірігіп кетеді. Осы екінші соқтығысудан кейінгі біріккен бөлшектің жылдамдығын табыңыз.'
        self.description_swahili = f'Chembe tatu $P, Q$ na $R$ ziko tuli katika mstari mnyoofu kwenye bapa laini la mlalo kama inavyoonyeshwa kwenye kielelezo. Masi ya $P$ ni $m_{{P}}$, $Q$ ni $m_{{Q}}$, na $R$ ni $m_{{R}}$. $P$ inarushwa moja kwa moja kuelekea $Q$ kwa kasi ya awali. Baada ya $P$ na $Q$ kugongana, $P$ inaendelea kusonga katika mwelekeo ule ule kwa kasi iliyopungua. Katika mgongano unaofuata kati ya $Q$ na $R$, chembe hizi zinaungana. Tafuta kasi ya chembe iliyounganishwa baada ya mgongano huu wa pili.'

class Mat174_multi(Mat174):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据该图，将一个木块放在与水平面成$\\alpha$角的粗糙斜面上。对木块施加一个沿斜面向上的恒力。求木块从静止开始沿斜面向下移动指定距离所需的时间。'
        self.description_arabic = 'توضع كتلة على مستوى خشن يميل بزاوية $\\alpha$ على الأفقي. تؤثر قوة ثابتة لأعلى المستوى. أوجد الزمن اللازم لقطع المسافة المحددة.'
        self.description_hindi = 'चित्र के आधार पर, एक ब्लॉक क्षैतिज से $\\alpha$ कोण पर झुके हुए एक खुरदरे तल पर रखा गया है। ब्लॉक पर सीधे तल के ऊपर की ओर एक निरंतर बल लगाया जाता है। वह समय ज्ञात करें जो ब्लॉक को विरामावस्था से तल के नीचे निर्दिष्ट दूरी तक जाने में लगता है।'
        self.description_kazakh = 'Суретке сүйенсек, блок көлденеңге $\\alpha$ бұрышымен көлбеу орналасқан кедір-бұдыр жазықтыққа қойылған. Блокқа жазықтық бойымен тікелей жоғары қарай тұрақты күш түсіріледі. Блоктың тыныштық күйінен жазықтық бойымен төмен қарай көрсетілген қашықтыққа жылжуына кететін уақытты табыңыз.'
        self.description_swahili = f'Kulingana na kielelezo, kizuizi kimewekwa kwenye bapa mwinamo korofi lililoinama kwa pembe $\\alpha$ kwa mlalo. Nguvu thabiti inatumiwa kwenye kizuizi hicho kuelekea juu ya bapa. Tafuta muda utakaotumiwa na kizuizi kusonga kutoka hali tuli kwa umbali uliobainishwa kuelekea chini ya bapa.'

class Mat175_multi(Mat175):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了粗糙滑水道的垂直横截面$ABC$。一个被建模为粒子的人从$A$处静止开始向下滑动。根据图中提供的信息，求人从$B$移动到$C$时克服阻力所做的功。'
        self.description_arabic = 'يوضح الشكل المقطع العرضي الرأسي $ABC$ لمنزلق مائي خشن. ينزلق رجل من السكون عند $A$. أوجد الشغل المبذول ضد قوة المقاومة من $B$ إلى $C$.'
        self.description_hindi = 'आरेख एक खुरदरे वॉटरस्लाइड का ऊर्ध्वाधर क्रॉस-सेक्शन $ABC$ दिखाता है। एक कण के रूप में प्रतिरूपित एक व्यक्ति $A$ से विरामावस्था से नीचे खिसकता है। चित्र में दी गई जानकारी के आधार पर, व्यक्ति के $B$ से $C$ तक जाने पर प्रतिरोध बल के विरुद्ध किए गए कार्य को ज्ञात करें।'
        self.description_kazakh = 'Диаграммада кедір-бұдыр су сырғанағының $ABC$ тік көлденең қимасы көрсетілген. Бөлшек ретінде модельденген адам $A$ нүктесінде тыныштық күйінен төмен сырғиды. Суретте берілген ақпаратқа сүйене отырып, адам $B$-дан $C$-ға қозғалған кездегі кедергі күшіне қарсы жасалған жұмысты табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha mkato wa msalaba wa wima $ABC$ wa kutelezea maji korofi. Mwanamume anayechukuliwa kama chembe anateleza chini kutoka hali tuli kwenye $A$. Kulingana na taarifa iliyotolewa kwenye kielelezo, tafuta kazi iliyofanywa dhidi ya nguvu ya ukinzani mwanamume huyo anaposonga kutoka $B$ hadi $C$.'

class Mat176_multi(Mat176):
    def __init__(self):
        super().__init__()
        self.description_chinese = '据该图，计算B班分数中位数与A班分数中位数之间的正差值。'
        self.description_arabic = 'يوضح مخطط الساق والورقة المزدوج درجات طلاب الفصلين $A$ و $B$. احسب الفرق الموجب بين الوسيطين.'
        self.description_hindi = 'बैक-टू-बैक स्टेम-एंड-लीफ़ आरेख Class A और Class B के  माध्यिका अंक और Class A के माध्यिका अंक के बीच धनात्मक अंतर की गणना करें।'
        self.description_kazakh = 'Сабақ-жапырақ диаграммасында А және В сыныптарындағы оқушылардың тест ұпайлары көрсетілген. Сызбаға сүйене отырып, В сыныбының медианалық ұпайы мен А сыныбының медианалық ұпайы арасындағы оң айырманы есептеңіз.'
        self.description_swahili = f'Mchoro wa shina na jani uliogongana unaonyesha alama za mtihani za wanafunzi katika Darasa A na Darasa B. Kulingana na kielelezo, kokotoa tofauti chanya kati ya mediani ya Darasa B na mediani ya Darasa A.'

class Mat177_multi(Mat177):
    def __init__(self):
        super().__init__()
        self.description_chinese = '箱线图总结了特定植物物种的高度。根据该图，计算植物高度达到根据标准$Q_3 + 1.5 \\times (IQR)$准则被视为异常值所需的最小数值。'
        self.description_arabic = 'يوضح مخطط الصندوق والشاربين أطوال نباتات. احسب الحد الأدنى للقيمة المتطرفة وفقًا للمعيار $Q_3 + 1.5 \\times (IQR)$.'
        self.description_hindi = 'बॉक्स-एंड-विस्कर प्लॉट एक विशिष्ट पौधे की प्रजाति की ऊँचाइयों को सारांशित करता है। चित्र के आधार पर, मानक $Q_3 + 1.5 \\ (IQR)$ मानदंड के अनुसार एक आउटलायर माने जाने के लिए पौधे की ऊँचाई का न्यूनतम संख्यात्मक मान क्या होना चाहिए, इसकी गणना करें।'
        self.description_kazakh = 'Қорап-және-мұрт сызбасы белгілі бір өсімдік түрлерінің биіктіктерін жинақтайды. Суретке сүйене отырып, өсімдік биіктігі стандартты $Q_3 + 1.5 \\times (IQR)$ критерийіне сәйкес ауытқу болып саналуы үшін жетуі тиіс минималды сандық мәнді есептеңіз.'
        self.description_swahili = f'Mchoro wa kisanduku na sharubu unatoa muhtasari wa vimo vya spishi fulani ya mmea. Kulingana na kielelezo, kokotoa thamani ndogo zaidi ya namba ambayo kimo cha mmea kinapaswa kufikia ili kuzingatiwa kama kipekee (outlier) kulingana na kigezo sanifu cha $Q_3 + 1.5 \\times (IQR)$.'

class Mat178_multi(Mat178):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'累积频率图显示了{self.total_students}名学生在家庭作业上花费的时间。根据该图，估计此分布的第{self.percentile_rank}个百分位数时间。'
        self.description_arabic = f'يوضح المنحنى التكراري المتجمع الزمن الذي قضاه {self.total_students} طالبًا. قدّر زمن المئين {self.percentile_rank}.'
        self.description_hindi = f'संचयी आवृत्ति ग्राफ {self.total_students} छात्रों द्वारा एक होमवर्क असाइनमेंट पर बिताए गए समय को प्रदर्शित करता है। चित्र के आधार पर, इस वितरण के लिए {self.percentile_rank}वें पर्सेंटाइल समय का अनुमान लगाएँ।'
        self.description_kazakh = f'Кумулятивтік жиілік графигі {self.total_students} оқушының үй тапсырмасына жұмсаған уақытын көрсетеді. Суретке сүйене отырып, осы үлестірім үшін {self.percentile_rank}-ші процентиль уақытын бағалаңыз.'
        self.description_swahili = f'Grafu ya marudio ya limbiko inaonyesha muda uliotumiwa na wanafunzi {self.total_students} kwenye kazi ya nyumbani. Kulingana na kielelezo, kadiria muda wa pasentaili ya {self.percentile_rank} kwa usambazaji huu.'

class Mat179_multi(Mat179):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'直方图说明了快递仓库中一组{self.total_n}个包裹的质量分布。根据该图，计算最后一个组距的频率密度。'
        self.description_arabic = f'يوضح المدرج التكراري توزيع الكتل لـ {self.total_n} طردًا. احسب الكثافة التكرارية للفئة الأخيرة.'
        self.description_hindi = f'आयतचित्र एक डिलीवरी वेयरहाउस में {self.total_n} पार्सल के सेट के लिए द्रव्यमान के वितरण को दर्शाता है। चित्र के आधार पर, अंतिम वर्ग अंतराल के आवृत्ति घनत्व की गणना करें।'
        self.description_kazakh = f'Гистограмма жеткізу қоймасындағы {self.total_n} сәлемдеме жиынтығына арналған массалардың үлестірімін бейнелейді. Суретке сүйене отырып, соңғы класс интервалының жиілік тығыздығын есептеңіз.'
        self.description_swahili = f'Histogramu inaonyesha usambazaji wa masi kwa seti ya vifurushi {self.total_n} katika ghala la uwasilishaji. Kulingana na kielelezo, kokotoa msongamano wa marudio (frequency density) wa muda wa darasa la mwisho.'

class Mat180_multi(Mat180):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一组学生将坐在如图所示的一排椅子上。在这群学生中有一对双胞胎，他们不能挨着坐。求所有学生就座且双胞胎分开的不同排列方式总数。'
        self.description_arabic = f'ستجلس مجموعة من الطلاب في صف الكراسي الموضح في الشكل. من بين الطلاب توأمان يجب ألا يجلسا متجاورين. أوجد العدد الكلي للطرق المختلفة لترتيب جلوس الطلاب بحيث يكون التوأمان منفصلين.'
        self.description_hindi = f'छात्रों के एक समूह को चित्र में दिखाई गई कुर्सियों की पंक्ति में बैठाया जाना है। छात्रों में जुड़वा बच्चों की एक जोड़ी है जिन्हें एक दूसरे के बगल में नहीं बैठना चाहिए। जुड़वा बच्चों को अलग रखते हुए सभी छात्रों को बैठाए जा सकने वाले अलग-अलग तरीकों की कुल संख्या ज्ञात करें।'
        self.description_kazakh = f'Бір топ оқушылар суретте көрсетілген орындықтар қатарына отыруы керек. Оқушылар арасында бірге отыруға болмайтын бір жұп егіздер бар. Егіздер бөлек отыратындай барлық оқушыларды отырғызудың әртүрлі тәсілдерінің жалпы санын табыңыз.'
        self.description_swahili = f'Kundi la wanafunzi linapaswa kukalishwa kwenye safu ya viti kama inavyoonyeshwa kwenye kielelezo. Miongoni mwa wanafunzi hao, kuna mapacha wawili ambao hawapaswi kukaa karibu mmoja na mweziwe. Tafuta jumla ya idadi ya njia tofauti ambazo wanafunzi wote wanaweza kukalishwa ili mapacha hao wawe wametenganishwa.'

class Mat181_multi(Mat181):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'从图中所示的人员中选出一个委员会。委员会必须恰好由{self.req_women}名女性和{self.req_men}名男性组成。确定选择该委员会的不同方式数。'
        self.description_arabic = f'سيتم اختيار لجنة من مجموعة الأشخاص الموضحة في الشكل. يجب أن تتكون اللجنة من {self.req_women} نساء و {self.req_men} رجال بالضبط. أوجد عدد الطرق المختلفة لاختيار هذه اللجنة.'
        self.description_hindi = f'चित्र में दर्शाए गए लोगों के समूह में से एक समिति का चयन किया जाना है। समिति में ठीक {self.req_women} महिलाएं और {self.req_men} पुरुष होने चाहिए। इस समिति के चयन के विभिन्न तरीकों की संख्या ज्ञात करें।'
        self.description_kazakh = f'Комитет суретте көрсетілген адамдар тобынан таңдалуы тиіс. Комитет құрамында дәл {self.req_women} әйел және {self.req_men} ер адам болуы тиіс.Осы комитетті таңдаудың әртүрлі тәсілдерінің санын анықтаңыз.'
        self.description_swahili = f'Kamati inapaswa kuchaguliwa kutoka kwa kundi la watu linaloonyeshwa kwenye kielelezo. Kamati hiyo lazima iwe na idadi kamili ya wanawake {self.req_women} na wanaume {self.req_men}. Bainisha idadi ya njia tofauti ambazo kamati hii inaweza kuchaguliwa.'

class Mat182_multi(Mat182):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一组{self.n}个独特的装饰品正被排列在展示架的直线上。由图中彩色标签指示的两个特定装饰品必须始终并排放置。确定这些装饰品可以排列的不同方式总数。'
        self.description_arabic = f'يتم ترتيب مجموعة مكونة من {self.n} من الزخارف المختلفة في صف مستقيم على رف عرض. يجب أن توضع زخرفتان محددتان، كما هو موضح في الشكل، جنبًا إلى جنب دائمًا. أوجد عدد طرق الترتيب الممكنة.'
        self.description_hindi = f'एक डिस्प्ले शेल्फ पर एक सीधी रेखा में {self.n} अद्वितीय आभूषणों का एक सेट व्यवस्थित किया जा रहा है। चित्र में रंगीन लेबलों द्वारा इंगित दो विशिष्ट आभूषणों को हमेशा अगल-बगल रखा जाना चाहिए। आभूषणों को व्यवस्थित करने के अलग-अलग तरीकों की कुल संख्या निर्धारित करें।'
        self.description_kazakh = f'{self.n} бірегей әшекейлер жиынтығы көрме сөресінде бір түзу бойымен орналастырылуда. Суретте түрлі-түсті белгілермен көрсетілген екі нақты әшекей әрқашан қатар қойылуы керек. Әшекейлерді орналастырудың әртүрлі тәсілдерінің жалпы санын анықтаңыз.'
        self.description_swahili = f'Seti ya mapambo ya kipekee {self.n} inapangwa katika mstari mnyoofu kwenye rafu. Mapambo mawili maalum, yaliyoonyeshwa na lebo za rangi kwenye kielelezo, lazima kila wakati yawekwe pamoja (side-by-side). Bainisha jumla ya idadi ya njia tofauti ambazo mapambo hayo yanaweza kupangwa.'

class Mat183_multi(Mat183):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一群董事会成员（包括一名主席和一名秘书）正在图中所示的长桌上开会。在这次特定的会议中，主席和秘书必须坐在相邻的座位上。计算成员就座的不同方式总数。'
        self.description_arabic = 'تجتمع مجموعة من أعضاء مجلس الإدارة، بمن فيهم رئيس وسكرتير، حول الطاولة الطويلة الموضحة في الشكل. يجب أن يجلس الرئيس والسكرتير في مقعدين متجاورين. أوجد عدد طرق الجلوس الممكنة.'
        self.description_hindi = 'एक अध्यक्ष और एक सचिव सहित बोर्ड के सदस्यों का एक समूह चित्र में दिखाई गई लंबी मेज पर बैठक कर रहा है। इस विशिष्ट बैठक के लिए, अध्यक्ष और सचिव को आसन्न सीटों पर बैठना चाहिए। सदस्यों को बैठाए जा सकने वाले अलग-अलग तरीकों की कुल संख्या की गणना करें।'
        self.description_kazakh = 'Төраға мен хатшыны қоса алғанда, басқарма мүшелері тобы суретте көрсетілген ұзын үстел басында жиналыс өткізуде. Осы нақты жиналыс үшін Төраға мен Хатшы көршілес орындарда отыруы тиіс. Мүшелерді отырғызудың әртүрлі тәсілдерінің жалпы санын есептеңіз.'
        self.description_swahili = f'Kundi la wajumbe wa bodi, likijumuisha Mwenyekiti na Katibu, wanafanya mkutano kwenye meza ndefu inayoonyeshwa kwenye kielelezo. Kwa mkutano huu maalum, Mwenyekiti na Katibu lazima wakae kwenye viti vinavyofuatana. Kokotoa jumla ya idadi ya njia tofauti ambazo wajumbe hao wanaweza kukalishwa.'

class Mat184_multi(Mat184):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了离散随机变量$X$的概率质量函数。根据显示的线段高度，计算方差$Var(X)$。'
        self.description_arabic = 'يوضح الشكل دالة الكتلة الاحتمالية لمتغير عشوائي منفصل $X$. بناءً على القيم الموضحة، احسب التباين $Var(X)$.'
        self.description_hindi = 'चित्र एक असतत यादृच्छिक चर $X$ के प्रायिकता द्रव्यमान फलन को प्रदर्शित करता है। दिखाए गए खंडों की ऊँचाई के आधार पर, प्रसरण $Var(X)$ की गणना करें।'
        self.description_kazakh = 'Суретте $X$ дискретті кездейсоқ шамасының ықтималдық массалық функциясы көрсетілген. Көрсетілген сегменттердің биіктіктеріне сүйене отырып, $Var(X)$ дисперсиясын есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha kazi ya masi ya uwezekano (probability mass function) ya kigezo nasibu cha kipekee $X$. Kulingana na vimo vya vipande vilivyoonyeshwa, kokotoa nyumbuko (variance) $Var(X)$.'

class Mat185_multi(Mat185):
    def __init__(self):
        super().__init__()
        self.description_chinese = '离散随机变量 $X$ 表示图中所示的加权四面转盘的得分。如果转盘旋转一次，求期望值 $E(X)$。'
        self.description_arabic = 'يمثل المتغير العشوائي المنفصل $X$ النتيجة على قرص دوار كما هو موضح في الشكل. إذا تم تدوير القرص مرة واحدة، أوجد القيمة المتوقعة $E(X)$.'
        self.description_hindi = 'चित्र में दर्शाए गए भारित चार-पक्षीय स्पिनर पर प्राप्त अंक को एक असतत यादृच्छिक चर (discrete random variable) $X$ द्वारा दर्शाया गया है। यदि स्पिनर को एक बार घुमाया जाता है, तो अपेक्षित मान $E(X)$ ज्ञात करें।'
        self.description_kazakh = ' $X$ дискретті кездейсоқ шамасы сызбада көрсетілген төрт жақты салмақталған айналмалы спиннердегі ұпайларды білдіреді. Егер спиннер бір рет айналдырылса, $E(X)$ математикалық күтілімін табыңыз.'
        self.description_swahili = f'Kigezo nasibu cha kipekee $X$ kinawakilisha alama kwenye spina yenye pande nne na yenye uzani (weighted) inayoonyeshwa kwenye kielelezo. Ikiwa spina hiyo itazungushwa mara moja, tafuta thamani inayotarajiwa $E(X)$.'

class Mat186_multi(Mat186):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'离散随机变量$X$服从几何分布$X \\sim \\text{{Geo}}(p)$。该图显示了前几个$x$值的概率质量函数。根据该图，确定$p$的小数值。'
        self.description_arabic = f'يتبع متغير عشوائي منفصل $X$ توزيعًا هندسيًا $X \\sim \\text{{Geo}}(p)$. يوضح الشكل دالة الكتلة الاحتمالية للقيم الأولى لـ $x$. بناءً على الشكل، أوجد قيمة $p$ كعدد عشري.'
        self.description_hindi = f'एक असतत यादृच्छिक चर (discrete random variable) $X$ एक ज्यामितीय वितरण $X \\sim \\text{{Geo}}(p)$ का अनुसरण करता है। चित्र $x$ के पहले कुछ मानों के लिए प्रायिकता द्रव्यमान फलन दिखाता है। चित्र के आधार पर, $p$ का मान दशमलव के रूप में निर्धारित करें।'
        self.description_kazakh = f'$X$ дискретті кездейсоқ шамасы $X \\sim \\text{{Geo}}(p)$ геометриялық үлестіріміне бағынады. Суретте $x$-тің алғашқы бірнеше мәніне арналған ықтималдық массалық функциясы көрсетілген. Суретке сүйене отырып, $p$ мәнін ондық бөлшек түрінде анықтаңыз.'
        self.description_swahili = f'Kigezo nasibu cha kipekee $X$ kinafuata usambazaji wa kijiometria $X \\sim \\text{{Geo}}(p)$. Kielelezo kinaonyesha kazi ya masi ya uwezekano kwa thamani chache za kwanza za $x$. Kulingana na kielelezo, bainisha thamani ya $p$ kama desimali.'

class Mat187_multi(Mat187):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该直方图显示了离散随机变量 $W$ 的概率分布，其中 $W \\sim B(n, p)$。根据图中所示的柱状图高度，求出成功概率 $p$ 的数值。'
        self.description_arabic = f'يوضح المدرج التكراري التوزيع الاحتمالي لمتغير عشوائي منفصل $W$ حيث $W \\sim B(n, p)$. بناءً على ارتفاعات الأشرطة في الشكل، أوجد قيمة احتمال النجاح $p$.'
        self.description_hindi = f'हिस्टोग्राम असतत यादृच्छिक चर (discrete random variable) $W$ के प्रायिकता वितरण को दर्शाता है, जहाँ $W$, $W \\sim B(n, p)$ है। चित्र में दर्शाए गए बार की ऊँचाई के आधार पर, सफलता की प्रायिकता $p$ का संख्यात्मक मान ज्ञात करें।'
        self.description_kazakh = f'Гистограммада $W \\sim B(n, p)$ болатын $W$ дискретті кездейсоқ шамасының ықтималдықтар таралуы көрсетілген. Сызбадағы бағандардың биіктігіне сүйене отырып, $p$ сәттілік ықтималдығының сандық мәнін табыңыз.'
        self.description_swahili = f'Histogramu inaonyesha usambazaji wa uwezekano wa kigezo nasibu cha kipekee $W$ ambapo $W \\sim B(n, p)$. Kulingana na vimo vya miraba iliyoonyeshwa kwenye kielelezo, tafuta thamani ya namba ya uwezekano wa kufaulu $p$.'

class Mat188_multi(Mat188):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图说明一个服从正态分布的连续随机变量$X$。根据图表中显示的参数和阴影区域，计算指示概率的值。'
        self.description_arabic = 'يوضح الشكل متغيرًا عشوائيًا متصلاً $X$ يتبع توزيعًا طبيعيًا. باستخدام المعلمات والمنطقة المظللة، احسب قيمة الاحتمال المشار إليه.'
        self.description_hindi = 'चित्र एक सतत यादृच्छिक चर $X$ को दर्शाता है जो एक सामान्य वितरण का अनुसरण करता है। आरेख में दिखाए गए मापदंडों और छायांकित क्षेत्र के आधार पर, इंगित प्रायिकता के मान की गणना करें।'
        self.description_kazakh = 'Суретте қалыпты үлестірімге бағынатын үзіліссіз $X$ кездейсоқ шамасы бейнеленген. Диаграммада көрсетілген параметрлер мен боялған аймаққа сүйене отырып, көрсетілген ықтималдықтың мәнін есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha kigezo nasibu kinachoendelea $X$ kinachofuata usambazaji wa kawaida. Kulingana na vigezo na sehemu iliyotiwa kivuli inayoonyeshwa kwenye mchoro, kokotoa thamani ya uwezekano uliobainishwa.'

class Mat189_multi(Mat189):
    def __init__(self):
        super().__init__()
        self.description_chinese = '随机变量$X$服从均值如图所示的正态分布。已知阴影区域代表的概率，计算标准差$\\sigma$的值。'
        self.description_arabic = 'يتبع المتغير العشوائي $X$ توزيعًا طبيعيًا بمتوسط حسابي موضح في الشكل. باستخدام الاحتمال الممثل بالمنطقة المظللة، احسب قيمة الانحراف المعياري $\\sigma$.'
        self.description_hindi = 'एक यादृच्छिक चर (random variable) $X$ चित्र में दिखाए गए माध्य के साथ एक सामान्य वितरण का अनुसरण करता है। छायांकित क्षेत्र द्वारा दर्शाई गई प्रायिकता को देखते हुए, मानक विचलन $\\sigma$ के मान की गणना करें।'
        self.description_kazakh = ' $X$ кездейсоқ шамасы суретте көрсетілген орташа мәні бар қалыпты үлестірімге бағынады. Боялған ауданмен берілген ықтималдықты ескере отырып, $\\sigma$ стандартты ауытқуының мәнін есептеңіз.'
        self.description_swahili = f'Kigezo nasibu $X$ kinafuata usambazaji wa kawaida wenye wastani ulioonyeshwa kwenye kielelezo. Kwa kuzingatia uwezekano unaowakilishwa na eneo lililotiwa kivuli, kokotoa thamani ya mkengeuko sanifu (standard deviation) $\\sigma$.'

class Mat190_multi(Mat190):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个正态分布，其中阴影区域代表特定概率。根据阴影区域的边界值和分布的方差，求均值$\\mu$的值。'
        self.description_arabic = 'يوضح الشكل توزيعًا طبيعيًا حيث تمثل المنطقة المظللة احتمالًا معينًا. باستخدام حدود المنطقة وتباين التوزيع، أوجد قيمة المتوسط الحسابي $\\mu$.'
        self.description_hindi = 'चित्र एक सामान्य वितरण दिखाता है जहाँ छायांकित क्षेत्र एक विशिष्ट प्रायिकता का प्रतिनिधित्व करता है। छायांकित क्षेत्र के सीमा मानों और वितरण के प्रसरण के आधार पर, माध्य $\\mu$ का मान ज्ञात करें।'
        self.description_kazakh = 'Суретте боялған аймақ нақты ықтималдықты білдіретін қалыпты үлестірім көрсетілген. Боялған аймақтың шекаралық мәндеріне және үлестірімнің дисперсиясына сүйене отырып, $\\mu$ орташа мәнін табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha usambazaji wa kawaida ambapo sehemu iliyotiwa kivuli inawakilisha uwezekano maalum. Kulingana na thamani za mipaka ya eneo lililotiwa kivuli na nyumbuko (variance) wa usambazaji huo, tafuta thamani ya wastani $\\mu$.'

class Mat191_multi(Mat191):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'该图说明了从均值为$\\mu$且方差为$\\sigma^2$的正态分布总体中抽取样本量为$n = {self.n}$的样本，其样本均值$\\overline{{X}}$的概率密度函数。根据图中显示的参数，计算总体的标准差$\\sigma$。'
        self.description_arabic = f'يوضح الشكل دالة الكثافة الاحتمالية لمتوسط العينة $\\overline{{X}}$ لعينات بحجم $n = {self.n}$ مأخوذة من مجتمع يتبع توزيعًا طبيعيًا بمتوسط $\\mu$ وتباين $\\sigma^2$. أوجد قيمة الانحراف المعياري $\\sigma$.'
        self.description_hindi = f'चित्र माध्य $\\mu$ और प्रसरण $\\sigma^2$ के साथ सामान्य रूप से वितरित जनसंख्या से लिए गए आकार $n = {self.n}$ के नमूनों के लिए नमूना माध्य $\\overline{{X}}$ के प्रायिकता घनत्व फलन को दर्शाता है। चित्र में दिखाए गए मापदंडों के आधार पर, जनसंख्या के मानक विचलन, $\\sigma$, की गणना करें।'
        self.description_kazakh = f'Суретте орташа мәні $\\mu$ және дисперсиясы $\\sigma^2$ болатын қалыпты үлестірімдегі генералды жиынтықтан алынған $n = {self.n}$ көлеміндегі таңдамалар үшін $\\overline{{X}}$ таңдамалық орташа мәннің ықтималдық тығыздығы функциясы бейнеленген. Суретте көрсетілген параметрлерге сүйене отырып, генералды жиынтықтың стандартты ауытқуын, $\\sigma$, есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha kazi ya msongamano wa uwezekano (probability density function) ya wastani wa sampuli $\\overline{{X}}$ kwa sampuli za ukubwa wa $n = {self.n}$ zilizochukuliwa kutoka kwenye populashi iliyosambazwa kwa kawaida yenye wastani $\\mu$ na nyumbuko $\\sigma^2$. Kulingana na vigezo vilivyoonyeshwa, kokotoa mkengeuko sanifu wa populashi, $\\sigma$.'

class Mat192_multi(Mat192):
    def __init__(self):
        super().__init__()
        self.description_chinese = '点图显示了鸟类随机样本的翼展测量值（单位：cm）。根据图中提供的视觉数据，计算总体方差的无偏估计值（$s^2$）。'
        self.description_arabic = 'يوضح المخطط النقطي قياسات باع الجناحين (بالسنتيمتر) لعينة عشوائية من الطيور. باستخدام البيانات، احسب التقدير غير المتحيز لتباين المجتمع $s^2$.'
        self.description_hindi = 'डॉट प्लॉट पक्षियों के एक यादृच्छिक नमूने के पंखों के फैलाव के माप (cm में) दिखाता है। चित्र में दिए गए दृश्य डेटा के आधार पर, जनसंख्या प्रसरण के निष्पक्ष अनुमान ($s^2$) की गणना करें।'
        self.description_kazakh = 'Нүктелік диаграмма құстардың кездейсоқ таңдамасының қанат құлашының өлшемдерін (см-мен) көрсетеді. Суретте берілген визуалды деректерге сүйене отырып, генералды жиынтық дисперсиясының ығыспаған бағасын ($s^2$) есептеңіз.'
        self.description_swahili = f'Mchoro wa doti (dot plot) unaonyesha vipimo vya upana wa mabawa (katika sm) ya sampuli nasibu ya ndege. Kulingana na data inayoonekana kwenye kielelezo, kokotoa makadirio yasiyopendelea ya nyumbuko wa populashi ($s^2$).'

class Mat193_multi(Mat193):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个总体的分布以及相应的样本量为$n$的样本均值$\\overline{X}$的抽样分布。根据图中提供的统计参数，确定样本量$n$的值。'
        self.description_arabic = 'يوضح الشكل توزيع مجتمع إحصائي وتوزيع المعاينة المقابل لمتوسط العينة $\\overline{X}$ لعينات بحجم $n$. باستخدام المعطيات، أوجد قيمة $n$.'
        self.description_hindi = 'चित्र एक जनसंख्या के वितरण और नमूना आकार $n$ के लिए नमूना माध्य $\\overline{X}$ के संबंधित नमूनाकरण वितरण को दिखाता है। चित्र में दिए गए सांख्यिकीय मापदंडों के आधार पर, नमूना आकार $n$ का मान निर्धारित करें।'
        self.description_kazakh = 'Суретте генералды жиынтықтың үлестірімі және көлемі $n$ болатын таңдамалар үшін $\\overline{X}$ таңдамалық орташаның сәйкес таңдамалық үлестірімі көрсетілген. Суретте берілген статистикалық параметрлерге сүйене отырып, $n$ таңдама көлемінің мәнін анықтаңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha usambazaji wa populashi na usambazaji wa sampuli unaolingana wa wastani wa sampuli $\\overline{X}$ kwa sampuli za ukubwa $n$. Kulingana na vigezo vya kitakwimu vilivyotolewa kwenye kielelezo, bainisha thamani ya ukubwa wa sampuli $n$.'

class Mat194_multi(Mat194):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了用于确定置信区间的临界值$z$的标准正态分布。根据阴影尾部中指示的面积，计算区间的置信水平百分比。'
        self.description_arabic = 'يوضح الشكل توزيعًا طبيعيًا معياريًا لتحديد القيمة الحرجة $z$ لفترة ثقة. بناءً على المساحة المظللة في الأطراف، احسب مستوى الثقة كنسبة مئوية.'
        self.description_hindi = 'चित्र एक विश्वास अंतराल के लिए महत्वपूर्ण मान $z$ निर्धारित करने के लिए उपयोग किए जाने वाले मानक सामान्य वितरण को दिखाता है। छायांकित पुच्छों में इंगित क्षेत्र के आधार पर, अंतराल के विश्वास स्तर की प्रतिशत के रूप में गणना करें।'
        self.description_kazakh = 'Суретте сенімділік интервалы үшін $z$ критикалық мәнін анықтауға қолданылатын стандартты қалыпты үлестірім көрсетілген. Боялған құйрықтардағы көрсетілген ауданға сүйене отырып, интервалдың сенімділік деңгейін пайызбен есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha usambazaji wa kawaida sanifu (standard normal distribution) unaotumika kubainisha thamani muhimu $z$ kwa muda wa uaminifu. Kulingana na eneo lililobainishwa katika mikia iliyotiwa kivuli, kokotoa kiwango cha uaminifu cha muda huo kama asilimia.'

class Mat195_multi(Mat195):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据一个大样本计算出某种植物平均高度的置信区间。根据图中显示的正态分布曲线和区间，求用于构建该区间的样本均值$\\overline{x}$。'
        self.description_arabic = 'تم حساب فترة ثقة لمتوسط طول نوع من النباتات من عينة كبيرة. باستخدام الشكل، أوجد متوسط العينة $\\overline{x}$.'
        self.description_hindi = 'एक पौधे की प्रजाति की माध्य ऊँचाई के लिए एक विश्वास अंतराल एक बड़े नमूने से गणना की गई थी। सामान्य वितरण वक्र और चित्र में दिखाए गए अंतराल के आधार पर, इस अंतराल के निर्माण के लिए उपयोग किए गए नमूना माध्य $\\overline{x}$ को ज्ञात करें।'
        self.description_kazakh = 'Өсімдік түрлерінің орташа биіктігіне арналған сенімділік интервалы үлкен таңдамадан есептелді. Суретте көрсетілген қалыпты үлестірім қисығына және интервалға сүйене отырып, осы интервалды құру үшін пайдаланылған $\\overline{x}$ таңдамалық орташа мәнін табыңыз.'
        self.description_swahili = 'Muda wa uaminifu kwa wastani wa kimo cha spishi ya mmea ulikokotolewa kutoka kwa sampuli kubwa. Kulingana na mkunjo wa usambazaji wa kawaida na muda ulioonyeshwa kwenye kielelezo, tafuta wastani wa sampuli $\\overline{x}$ uliotumiwa kuunda muda huo.'

class Mat196_multi(Mat196):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了用于特定置信区间的标准正态曲线下的面积。根据阴影面积和给定的标准误（SE），计算总体均值$\\mu$的置信区间宽度。'
        self.description_arabic = 'يوضح الشكل المساحات تحت المنحنى الطبيعي المعياري لفترة ثقة معينة. باستخدام المساحة المظللة والخطأ المعياري، احسب عرض فترة الثقة لمتوسط المجتمع $\\mu$.'
        self.description_hindi = 'चित्र एक विशिष्ट विश्वास अंतराल के लिए मानक सामान्य वक्र के अंतर्गत क्षेत्रों को दिखाता है। छायांकित क्षेत्र और दी गई मानक त्रुटि (SE) के आधार पर, जनसंख्या माध्य $\\mu$ के लिए विश्वास अंतराल की चौड़ाई की गणना करें।'
        self.description_kazakh = 'Суретте нақты сенімділік интервалы үшін пайдаланылатын стандартты қалыпты қисық астындағы аудандар көрсетілген. Боялған аймаққа және берілген стандартты қателікке (SE) сүйене отырып, генералды жиынтықтың орташа мәні $\\mu$ үшін сенімділік интервалының енін есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha maeneo chini ya mkunjo wa kawaida sanifu yanayotumika kwa muda maalum wa uaminifu. Kulingana na eneo lililotiwa kivuli na kosa sanifu (SE) lililotolewa, kokotoa upana wa muda wa uaminifu kwa wastani wa populashi $\\mu$.'

class Mat197_multi(Mat197):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了对于相同的总体均值但具有不同样本量$n_A$和$n_B$的两个抽样分布$A$和$B$。根据显示的关系和图例中的参数，计算$n_B$的值。'
        self.description_arabic = 'يوضح الشكل توزيعي معاينة $A$ و $B$ لنفس متوسط المجتمع ولكن بأحجام عينات مختلفة $n_A$ و $n_B$. أوجد قيمة $n_B$.'
        self.description_hindi = 'चित्र समान जनसंख्या माध्य के लिए दो नमूनाकरण वितरणों, $A$ और $B$ को दिखाता है, लेकिन अलग-अलग नमूना आकारों, $n_A$ और $n_B$ के साथ। दिखाए गए संबंध और लेजेंड में मापदंडों के आधार पर, $n_B$ के मान की गणना करें।'
        self.description_kazakh = 'Суретте бірдей генералды жиынтықтың орташа мәніне арналған, бірақ көлемі әртүрлі $n_A$ және $n_B$ болатын екі таңдамалық $A$ және $B$ үлестірімдері көрсетілген. Көрсетілген байланысқа және аңыздағы параметрлерге сүйене отырып, $n_B$ мәнін есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha usambazaji wa sampuli mbili, $A$ na $B$, kwa wastani wa populashi ileile lakini wenye ukubwa tofauti wa sampuli, $n_A$ na $n_B$. Kulingana na uhusiano ulioonyeshwa na vigezo kwenye maelezo ya kielelezo, kokotoa thamani ya $n_B$.'

class Mat198_multi(Mat198):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图说明了调查结果的误差幅度（$E$）与样本量（$n$）之间的关系。根据图例中提供的参数和曲线上的标记点，确定所需的样本量$n$。'
        self.description_arabic = 'يوضح الشكل العلاقة بين هامش الخطأ $E$ وحجم العينة $n$. باستخدام النقطة المحددة، أوجد حجم العينة المطلوب.'
        self.description_hindi = 'चित्र एक सर्वेक्षण परिणाम के लिए त्रुटि के मार्जिन ($E$) और नमूना आकार ($n$) के बीच संबंध को दर्शाता है। चित्र लेजेंड में दिए गए मापदंडों और वक्र पर चिह्नित बिंदु के आधार पर, आवश्यक नमूना आकार $n$ निर्धारित करें।'
        self.description_kazakh = 'Сурет сауалнама нәтижесі үшін қателік шегі ($E$) мен таңдама көлемі ($n$) арасындағы байланысты бейнелейді. Сурет аңызында берілген параметрлерге және қисықта белгіленген нүктеге сүйене отырып, қажетті $n$ таңдама көлемін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha uhusiano kati ya upeo wa makosa ($E$) na ukubwa wa sampuli ($n$) kwa matokeo ya utafiti. Kulingana na vigezo vilivyotolewa kwenye maelezo ya kielelezo na nukta iliyowekwa alama kwenye mkunjo, bainisha ukubwa wa sampuli unaohitajika $n$.'

class Mat199_multi(Mat199):
    def __init__(self):
        super().__init__()
        self.description_chinese = '从同一总体中抽取了两个独立样本。根据图例中提供的箱线图和样本量，通过组合所有观测值来计算总体均值的无偏估计值。'
        self.description_arabic = 'تم أخذ عينتين مستقلتين من نفس المجتمع. باستخدام مخططات الصندوق وأحجام العينات، احسب التقدير غير المتحيز لمتوسط المجتمع.'
        self.description_hindi = 'समान जनसंख्या से दो स्वतंत्र नमूने लिए गए हैं। चित्र लेजेंड में दिए गए बॉक्सप्लॉट और नमूना आकारों के आधार पर, सभी अवलोकनों को मिलाकर जनसंख्या माध्य के निष्पक्ष अनुमान की गणना करें।'
        self.description_kazakh = 'Бір генералды жиынтықтан екі тәуелсіз таңдама алынды. Қорап сызбаларына және сурет аңызында берілген таңдама көлемдеріне сүйене отырып, барлық бақылауларды біріктіру арқылы генералды жиынтықтың орташа мәнінің ығыспаған бағасын есептеңіз.'
        self.description_swahili = f'Sampuli mbili huru zimechukuliwa kutoka kwenye populashi ileile. Kulingana na michoro ya kisanduku na ukubwa wa sampuli uliotolewa kwenye maelezo ya kielelezo, kokotoa makadirio yasiyopendelea ya wastani wa populashi kwa kujumuisha uchunguzi wote.'

class Mat200_multi(Mat200):
    def __init__(self):
        super().__init__()
        self.description_chinese = "一项大样本量的调查已完成。频率条形图说明了‘成功’和‘失败’结果的计数。根据该图，计算总体比例$p$的无偏点估计值。"
        self.description_arabic = "تم إجراء مسح بعينة كبيرة. يوضح المخطط الشريطي عدد نتائج 'النجاح' و 'الفشل'. احسب التقدير النقطي لنسبة المجتمع $p$."
        self.description_hindi = "बड़े नमूने के आकार के साथ एक सर्वेक्षण किया गया था। आवृत्ति दंड आरेख 'success' और 'failure' परिणामों की गिनती को दर्शाता है। चित्र के आधार पर, जनसंख्या अनुपात $p$ के लिए निष्पक्ष बिंदु अनुमान की गणना करें।"
        self.description_kazakh = "Үлкен көлемді таңдамамен сауалнама жүргізілді. Жиілік бағаналы диаграммасы 'сәттілік' және 'сәтсіздік' нәтижелерінің санын көрсетеді. Суретке сүйене отырып, генералды жиынтық үлесі $p$ үшін ығыспаған нүктелік бағаны есептеңіз."
        self.description_swahili = f"Utafiti ulifanywa kwa kutumia sampuli kubwa. Grafu ya miraba ya marudio inaonyesha idadi ya matokeo ya 'mafanikio' na 'kushindwa'. Kulingana na kielelezo, kokotoa makadirio ya nukta yasiyopendelea ya uwiano wa populashi $p$."

class Mat201_multi(Mat201):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图说明了总体$X$的分布以及样本量为$n = ' + str(self.n) + '$的样本均值$\\bar{X}$的分布。根据显示的统计属性，确定$E(\\bar{X})$的值。'
        self.description_arabic = 'يوضح الشكل توزيع مجتمع $X$ وتوزيع متوسط العينة $\\bar{X}$ لعينة بحجم $n = ' + str(self.n) + '$. أوجد قيمة $E(\\bar{X})$.'
        self.description_hindi = 'चित्र एक जनसंख्या $X$ के वितरण और नमूना आकार $n = ' + str(self.n) + '$ के लिए नमूना माध्य $\\bar{X}$ के वितरण को दर्शाता है। दिखाए गए सांख्यिकीय गुणों के आधार पर, $E(\\bar{X})$ का मान निर्धारित करें।'
        self.description_kazakh = 'Суретте $X$ генералды жиынтығының үлестірімі және $n = ' + str(self.n) + '$ таңдама көлемі үшін $\\bar{X}$ таңдамалық орташаның үлестірімі бейнеленген. Көрсетілген статистикалық қасиеттерге сүйене отырып, $E(\\bar{X})$ мәнін анықтаңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha usambazaji wa populashi $X$ na usambazaji wa wastani wa sampuli $\\bar{X}$ kwa ukubwa wa sampuli $n = ' + str(self.n) + '$. Kulingana na sifa za kitakwimu zinazoonyeshwa, bainisha thamani ya $E(\\bar{X})$.'

