from templates_001_050 import *
from templates_051_100 import *
from templates_101_150 import *
from templates_151_200 import *

class Mat001_multi(Mat001):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'{self.total} orang disurvei mengenai preferensi minuman mereka. Hasilnya ditampilkan dalam diagram Venn di bawah ini. Berapakah jumlah orang yang hanya memilih Kopi atau hanya memilih Teh?'
        self.description_chinese = f'对{self.total}人的饮料偏好进行了调查。结果显示在下方的韦恩图中。只喜欢咖啡或只喜欢茶的人数总和是多少？'
        self.description_arabic = f'تم استطلاع رأي {self.total} شخصًا حول تفضيلاتهم من المشروبات. يتم عرض النتائج في مخطط فن أدناه. ما هو مجموع الأشخاص الذين يفضلون القهوة فقط أو الشاي فقط؟'
        self.description_hindi = f'{self.total} लोगों का उनके पेय पदार्थों की प्राथमिकताओं के बारे में सर्वेक्षण किया गया था। परिणाम नीचे वेन आरेख (Venn diagram) में प्रदर्शित किए गए हैं। केवल Coffee या केवल Tea पसंद करने वाले लोगों का योग क्या है?'
        self.description_kazakh = f'{self.total} адамнан сусындарға қатысты қалауы бойынша сауалнама алынды. Нәтижелері төмендегі Венн диаграммасында көрсетілген. Тек кофені немесе тек шайды қалайтын адамдардың қосындысы қанша?'
        self.description_swahili = f'Watu {self.total} walihojiwa kuhusu vinywaji wanavyopendelea. Matokeo yanaonyeshwa kwenye mchoro wa Venn hapa chini. Je, ni jumla gani ya watu wanaopendelea Kahawa pekee au Chai pekee?'

class Mat002_multi(Mat002):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Dalam survei terhadap {self.total} siswa, informasi berikut dikumpulkan mengenai preferensi mereka terhadap tiga mata pelajaran: Matematika, Sains, dan Bahasa Inggris. Hasilnya ditunjukkan dalam diagram Venn di bawah ini. Berapa banyak siswa yang menyukai Matematika?'
        self.description_chinese = f'在一项对{self.total}名学生的调查中，收集了关于他们对数学、科学和英语这三个科目的偏好信息。结果显示在下方的韦恩图中。有多少名学生喜欢数学？'
        self.description_arabic = f'في استطلاع شمل {self.total} طالبًا، تم جمع المعلومات التالية بخصوص تفضيلهم لثلاث مواد: الرياضيات والعلوم واللغة الإنجليزية. يتم عرض النتائج في مخطط فن أدناه. كم عدد الطلاب الذين يحبون الرياضيات؟'
        self.description_hindi = f'{self.total} छात्रों के एक सर्वेक्षण में, तीन विषयों: Math, Science और English के लिए उनकी प्राथमिकता के संबंध में निम्नलिखित जानकारी एकत्र की गई थी। परिणाम नीचे वेन आरेख में दिखाए गए हैं। कितने छात्रों को Math पसंद है?'
        self.description_kazakh = f'{self.total} студент арасында жүргізілген сауалнамада олардың үш пәнге: математика, жаратылыстану және ағылшын тіліне деген қалауы туралы келесі ақпарат жиналды. Нәтижелері төмендегі Венн диаграммасында көрсетілген. Математиканы қанша студент ұнатады?'
        self.description_swahili = f'Katika utafiti wa wanafunzi {self.total}, taarifa zifuatazo zilikusanywa kuhusu mapendeleo yao kwa masomo matatu: Hisabati, Sayansi, na Kiingereza. Matokeo yanaonyeshwa kwenye mchoro wa Venn hapa chini. Je, ni wanafunzi wangapi wanapenda Hisabati?'

class Mat003_multi(Mat003):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Dengan membulatkan setiap dimensi menjadi 1 angka penting, perkirakan volume kotak tersebut.'
        self.description_chinese = f'通过将每个尺寸四舍五入到1位有效数字，估算盒子的体积。'
        self.description_arabic = f'بتقريب كل بُعد إلى رقم معنوي واحد، قدّر حجم الصندوق.'
        self.description_hindi = f'प्रत्येक विमा को 1 सार्थक अंक (significant figure) तक पूर्णांकित करके, बॉक्स के आयतन का अनुमान लगाएँ।'
        self.description_kazakh = f'Әрбір өлшемді 1 маңызды цифрға дейін дөңгелектей отырып, қораптың көлемін бағалаңыз.'
        self.description_swahili = f'Kwa kuraundisha kila kipimo hadi tarakimu 1 ya maana, kadiria ujazo wa sanduku.'

class Mat004_multi(Mat004):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diberikan gambar taman di bawah ini yang pengukurannya akurat hingga meter terdekat. Hitunglah batas atas luas taman tersebut.'
        self.description_chinese = f'已知下方花园的测量值精确到最近的米。计算该花园面积的上限。'
        self.description_arabic = f'بالنظر إلى الحديقة أدناه التي قياساتها صحيحة لأقرب متر. احسب الحد الأعلى لمساحة الحديقة.'
        self.description_hindi = f'नीचे एक बगीचा दिया गया है जिसकी माप निकटतम मीटर तक सही है। बगीचे के क्षेत्रफल की ऊपरी सीमा (upper bound) की गणना करें।'
        self.description_kazakh = f'Төменде өлшемдері ең жақын метрге дейін дәл берілген бақ көрсетілген. Бақ ауданының жоғарғы шегін есептеңіз.'
        self.description_swahili = f'Kutokana na bustani iliyo hapa chini ambayo vipimo vyake ni sahihi hadi mita iliyo karibu zaidi. Kokotoa kikomo cha juu cha eneo la bustani.'

class Mat005_multi(Mat005):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Botol manakah yang menawarkan nilai ekonomi lebih baik? Tunjukkan bagaimana Anda menentukannya.'
        self.description_chinese = f'哪瓶更划算？请展示你的判断过程。'
        self.description_arabic = f'أي زجاجة تقدم قيمة أفضل مقابل المال؟ وضح كيف اتخذت قرارك.'
        self.description_hindi = f'कौन सी बोतल पैसे के लिए बेहतर मूल्य (value for money) प्रदान करती है? दिखाएँ कि आपने यह निर्णय कैसे लिया।'
        self.description_kazakh = f'Қай бөтелке ақша үшін тиімдірек құндылықты ұсынады? Қалай шешім қабылдағаныңызды көрсетіңіз.'
        self.description_swahili = f'Ni chupa ipi inatoa thamani bora kwa pesa? Onyesha jinsi ulivyoamua.'

class Mat006_multi(Mat006):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Seorang turis ingin menukar {self.total_eur} Euro (EUR) ke Yen Jepang (JPY) menggunakan nilai tukar yang ditunjukkan di papan. Berapa banyak Yen yang akan mereka terima? Bulatkan hasilnya hingga dua tempat desimal.'
        self.description_chinese = f'一名游客想按照牌价将{self.total_eur}欧元 (EUR) 兑换成日元 (JPY)。他们将收到多少日元？结果保留两位小数。'
        self.description_arabic = f'يريد سائح تحويل {self.total_eur} يورو (EUR) إلى ين ياباني (JPY) باستخدام الأسعار المعروضة على اللوحة. كم ينًا سيحصل عليه؟ قرّب النتيجة إلى منزلتين عشريتين.'
        self.description_hindi = f'एक पर्यटक बोर्ड पर दी गई दरों का उपयोग करके {self.total_eur} Euros (EUR) को Japanese Yen (JPY) में बदलना चाहता है। उन्हें कितने Yen मिलेंगे? परिणाम को दो दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Турист тақтада көрсетілген бағамдарды пайдаланып {self.total_eur} Еуроны (EUR) Жапон Йеніне (JPY) айырбастағысы келеді. Ол қанша Йен алады? Нәтижені екі ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = f'Mtalii anataka kubadilisha Euro (EUR) {self.total_eur} kuwa Yen ya Japani (JPY) kwa kutumia viwango vinavyoonyeshwa kwenye ubao. Atapokea Yen ngapi? Raundisha jibu hadi sehemu mbili za desimali.'

class Mat007_multi(Mat007):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitung persentase kisi yang diarsir. Bulatkan hasilnya hingga dua tempat desimal.'
        self.description_chinese = f'计算网格中阴影部分所占的百分比。结果保留两位小数。'
        self.description_arabic = f'احسب النسبة المئوية للجزء المظلل من الشبكة. قرّب النتيجة إلى منزلتين عشريتين.'
        self.description_hindi = f'गणना करें कि ग्रिड का कितना प्रतिशत भाग छायांकित है। परिणाम को दो दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Тордың қанша пайыз бөлігі боялғанын есептеңіз. Нәтижені екі ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = f'Kokotoa ni asilimia ngapi ya gridi imewekwa kivuli. Raundisha jibu hadi sehemu mbili za desimali.'

class Mat008_multi(Mat008):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Jam menunjukkan waktu mulai dan selesai dari sebuah ujian matematika. Hitung total durasi ujian tersebut dalam jam dan menit.'
        self.description_chinese = f'时钟显示了一场数学考试的开始和结束时间。计算考试的总时长，以小时和分钟为单位。'
        self.description_arabic = f'تعرض الساعات وقتي البدء والانتهاء لامتحان الرياضيات. احسب المدة الإجمالية للامتحان بالساعات والدقائق.'
        self.description_hindi = f'घड़ियाँ एक गणित परीक्षा के शुरू होने और समाप्त होने का समय दिखाती हैं। परीक्षा की कुल अवधि की घंटों और मिनटों में गणना करें।'
        self.description_kazakh = f'Сағаттар математика емтиханының басталу және аяқталу уақытын көрсетеді. Емтиханның жалпы ұзақтығын сағат және минутпен есептеңіз.'
        self.description_swahili = f'Saa zinaonyesha muda wa kuanza na kumaliza kwa mtihani wa hisabati. Kokotoa muda wa jumla wa mtihani katika saa na dakika.'

class Mat009_multi(Mat009):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Jason meninggalkan Kota A pada pukul {self.departure_time}.00 dan bersepeda ke Kota D. Grafik perjalanan menunjukkan perjalanan Jason. Carilah selisih Kecepatan Rata-rata Jason dari A ke B dan dari C ke D."
        self.description_chinese = f"Jason在{self.departure_time}.00离开A镇骑行前往D镇。行程图展示了Jason的旅程。求Jason从A到B与从C到D的平均速度之差。"
        self.description_arabic = f"يغادر جيسون المدينة A في الساعة {self.departure_time}.00 ويركب دراجته إلى المدينة D، يوضح الرسم البياني للسفر رحلة جيسون. أوجد الفرق في متوسط سرعة جيسون من A إلى B ومن C إلى D."
        self.description_hindi = f"Jason टाउन A से {self.departure_time}.00 बजे निकलता है और साइकिल से टाउन D तक जाता है, यात्रा ग्राफ Jason की यात्रा को दर्शाता है। A से B और C से D तक Jason की औसत गति (Average Speed) का अंतर ज्ञात करें।"
        self.description_kazakh = f"Джейсон А қаласынан {self.departure_time}.00-де шығып, D қаласына велосипедпен барады. Жол жүру графигі Джейсонның саяхатын көрсетеді. Джейсонның А-дан В-ға дейінгі және С-дан D-ге дейінгі орташа жылдамдығының айырмашылығын табыңыз."
        self.description_swahili = f"Jason anaondoka Mji A saa {self.departure_time}.00 na kuendesha baiskeli hadi Mji D. Grafu ya usafiri inaonyesha safari ya Jason. Tafuta tofauti ya Mwendokasi wa Wastani wa Jason kutoka A hadi B na C hadi D."

class Mat010_multi(Mat010):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram ini menunjukkan grafik kecepatan-waktu dari bagian perjalanan sebuah mobil. Hitung total jarak yang ditempuh selama {self.t_end} detik tersebut.'
        self.description_chinese = f'该图显示了汽车部分旅程的速度-时间图。计算在{self.t_end}秒内行驶的总距离。'
        self.description_arabic = f'يوضح الرسم البياني علاقة السرعة بالزمن لجزء من رحلة سيارة. احسب المسافة الإجمالية المقطوعة خلال {self.t_end} ثانية.'
        self.description_hindi = f'आरेख एक कार यात्रा के एक हिस्से का गति-समय ग्राफ (speed-time graph) दिखाता है। {self.t_end} सेकंड के दौरान तय की गई कुल दूरी की गणना करें।'
        self.description_kazakh = f'Диаграмма автокөлік сапарының бір бөлігінің жылдамдық-уақыт графигін көрсетеді. {self.t_end} секунд ішінде жүріп өткен жалпы қашықтықты есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya mwendokasi-muda ya sehemu ya safari ya gari. Kokotoa umbali wa jumla uliosafiriwa katika sekunde {self.t_end}.'

class Mat011_multi(Mat011):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Ky bersepeda dari kantornya ke tempat pertemuan dan kembali lagi. Grafik perjalanan menunjukkan waktunya di pertemuan dan perjalanan pulangnya. Ky bersepeda dari kantornya ke pertemuan tersebut dengan kecepatan konstan {self.speed:.2f} km/jam. Jam berapa Ky meninggalkan kantornya?'
        self.description_chinese = f'Ky从办公室骑车去开会，然后再骑回来。行程图显示了他在会议上的时间以及他返回的旅程。Ky以{self.speed:.2f} km/h的恒定速度从办公室骑车去开会。Ky什么时候离开他的办公室？'
        self.description_arabic = f'يركب كي دراجته من مكتبه إلى اجتماع ثم يعود مرة أخرى. يوضح الرسم البياني للسفر وقته في الاجتماع ورحلة عودته. يركب كي دراجته من مكتبه إلى الاجتماع بسرعة ثابتة تبلغ {self.speed:.2f} كم/ساعة. في أي وقت يغادر كي مكتبه؟'
        self.description_hindi = f'Ky अपने कार्यालय से एक मीटिंग के लिए साइकिल से जाता है और वापस आता है। यात्रा ग्राफ मीटिंग में उसका समय और उसकी वापसी की यात्रा दिखाता है। Ky अपने कार्यालय से मीटिंग के लिए {self.speed:.2f} km/h की निरंतर गति से साइकिल चलाता है। Ky अपने कार्यालय से कितने बजे निकलता है?'
        self.description_kazakh = f'Кай кеңсесінен кездесуге дейін велосипедпен барып, қайта оралады. Жол жүру графигі оның кездесуде болған уақытын және қайтар жолын көрсетеді. Кай кеңсесінен кездесуге {self.speed:.2f} км/сағ тұрақты жылдамдықпен барады. Кай кеңседен қай уақытта шығады?'
        self.description_swahili = f'Ky anaendesha baiskeli kutoka ofisini kwake kwenda kwenye mkutano na kurudi tena. Grafu ya usafiri inaonyesha muda wake kwenye mkutano na safari yake ya kurudi. Ky anaendesha baiskeli kutoka ofisini kwake kwenda kwenye mkutano kwa mwendokasi thabiti wa {self.speed:.2f} km/h. Ky anaondoka ofisini kwake saa ngapi?'

class Mat012_multi(Mat012):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Grafik fungsi kuadrat ditunjukkan pada kisi. Dengan menentukan persamaan grafiknya terlebih dahulu, gunakan persamaan tersebut untuk menyelesaikan ${self.target_eq}$.'
        self.description_chinese = f'网格上显示了一个二次函数的图像。首先确定图像的方程，然后用它来求解 ${self.target_eq}$。'
        self.description_arabic = f'يُعرض الرسم البياني لدالة تربيعية على الشبكة. من خلال تحديد معادلة الرسم البياني أولاً، استخدمها لحل ${self.target_eq}$.'
        self.description_hindi = f'ग्रिड पर एक द्विघात फलन (quadratic function) का ग्राफ दिखाया गया है। सबसे पहले ग्राफ का समीकरण निर्धारित करके, इसका उपयोग ${self.target_eq}$ को हल करने के लिए करें।'
        self.description_kazakh = f'Квадраттық функцияның графигі торда көрсетілген. Алдымен графиктің теңдеуін анықтай отырып, оны ${self.target_eq}$ шешу үшін пайдаланыңыз.'
        self.description_swahili = f'Grafu ya utendakazi wa kipeo cha pili inaonyeshwa kwenye gridi. Kwa kuanza kutafuta mlinganyo wa grafu, utumie kutatua ${self.target_eq}$.'

class Mat013_multi(Mat013):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Dengan menggambar garis lurus yang sesuai pada kisi, selesaikan persamaan ${self.target_eq_str}$.'
        self.description_chinese = f'通过在网格上画一条合适的直线，求解方程 ${self.target_eq_str}$。'
        self.description_arabic = f'برسم خط مستقيم مناسب على الشبكة، حل المعادلة ${self.target_eq_str}$.'
        self.description_hindi = f'ग्रिड पर एक उपयुक्त सीधी रेखा खींचकर, समीकरण ${self.target_eq_str}$ को हल करें।'
        self.description_kazakh = f'Торда сәйкес келетін түзу сызықты сызу арқылы ${self.target_eq_str}$ теңдеуін шешіңіз.'
        self.description_swahili = f'Kwa kuchora mstari mnyoofu unaofaa kwenye gridi, tatua mlinganyo ${self.target_eq_str}$.'

class Mat014_multi(Mat014):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Populasi kultur bakteri, $P$, meningkat secara eksponensial seiring waktu $t$ jam.\nGrafik pertumbuhan ini ditunjukkan pada kisi.\nGunakan grafik tersebut untuk mencari berapa jam yang dibutuhkan agar jumlah bakteri mencapai {round(float(self.k), 10)}.'
        self.description_chinese = f'细菌培养物的种群数量 $P$ 随时间 $t$ 小时呈指数增长。\n网格上显示了这种增长的图像。\n利用图像找出细菌数量达到 {round(float(self.k), 10)} 需要多少小时。'
        self.description_arabic = f'يزداد عدد البكتيريا في مزرعة بكتيرية، $P$، أسيًا بمرور الوقت $t$ بالساعات.\nيتم عرض الرسم البياني لهذا النمو على الشبكة.\nاستخدم الرسم البياني لمعرفة عدد الساعات التي يستغرقها عدد البكتيريا للوصول إلى {round(float(self.k), 10)}.'
        self.description_hindi = f'एक जीवाणु संवर्धन की आबादी, $P$, समय $t$ घंटों के साथ चरघातांकी रूप से (exponentially) बढ़ती है।\nइस वृद्धि का ग्राफ ग्रिड पर दिखाया गया है।\nयह ज्ञात करने के लिए ग्राफ का उपयोग करें कि जीवाणुओं की संख्या {round(float(self.k), 10)} तक पहुंचने में कितने घंटे लगते हैं।'
        self.description_kazakh = f'Бактерия дақылының популяциясы, $P$, уақыт өте келе $t$ сағат ішінде экспоненциалды түрде өседі.\nБұл өсудің графигі торда көрсетілген.\nБактериялар саны {round(float(self.k), 10)}-ға жетуі үшін қанша сағат қажет екенін табу үшін графикті пайдаланыңыз.'
        self.description_swahili = f'Idadi ya tamaduni ya bakteria, $P$, inaongezeka kwa eksponeshia kwa muda wa saa $t$.\nGrafu ya ukuaji huu inaonyeshwa kwenye gridi.\nTumia grafu kutafuta inachukua saa ngapi kwa idadi ya bakteria kufikia {round(float(self.k), 10)}.'

class Mat015_multi(Mat015):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Massa, $M$ gram, dari suatu zat radioaktif meluruh secara eksponensial seiring waktu $t$ tahun.\nGrafik peluruhan ini ditunjukkan pada kisi.\nGunakan grafik tersebut untuk mencari berapa tahun yang dibutuhkan agar massa tersebut mencapai {round(float(self.k), 10)} gram.'
        self.description_chinese = f'放射性物质的质量 $M$ 克随时间 $t$ 年呈指数衰减。\n网格上显示了这种衰减的图像。\n利用图像找出质量达到 {round(float(self.k), 10)} 克需要多少年。'
        self.description_arabic = f'تتناقص الكتلة، $M$ بالجرام، لمادة مشعة أسيًا بمرور الوقت $t$ بالسنوات.\nيتم عرض الرسم البياني لهذا الاضمحلال على الشبكة.\nاستخدم الرسم البياني لمعرفة عدد السنوات التي تستغرقها الكتلة للوصول إلى {round(float(self.k), 10)} جرام.'
        self.description_hindi = f'एक रेडियोधर्मी पदार्थ का द्रव्यमान, $M$ ग्राम, समय $t$ वर्षों के साथ चरघातांकी रूप से घटता है।\nइस क्षय का ग्राफ ग्रिड पर दिखाया गया है।\nयह ज्ञात करने के लिए ग्राफ का उपयोग करें कि द्रव्यमान को {round(float(self.k), 10)} ग्राम तक पहुंचने में कितने वर्ष लगते हैं।'
        self.description_kazakh = f'Радиоактивті заттың массасы, $M$ грамм, $t$ жыл ішінде экспоненциалды түрде азаяды.\nБұл ыдыраудың графигі торда көрсетілген.\nМассасы {round(float(self.k), 10)} граммға жетуі үшін қанша жыл қажет екенін табу үшін графикті пайдаланыңыз.'
        self.description_swahili = f'Tungamo, gramu $M$, ya dutu nururifu inapungua kwa eksponeshia kwa muda wa miaka $t$.\nGrafu ya upungufu huu inaonyeshwa kwenye gridi.\nTumia grafu kutafuta inachukua miaka mingapi kwa tungamo kufikia gramu {round(float(self.k), 10)}.'

class Mat016_multi(Mat016):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan grafik fungsi kubik dengan titik potongnya yang diberi label. Sebuah garis vertikal digambar. Berdasarkan informasi pada grafik, tentukan nilai $y$ pada titik potong yang diberi label $(k, ?)$.'
        self.description_chinese = f'图中显示了一个三次函数的图像，并标出了其截距。画了一条垂直线。根据图中的信息，确定标记为 $(k, ?)$ 的交点处的 $y$ 值。'
        self.description_arabic = f'يوضح الشكل الرسم البياني لدالة تكعيبية مع تحديد نقاط التقاطع الخاصة بها. تم رسم خط رأسي. بناءً على المعلومات الواردة في الرسم البياني، حدد قيمة $y$ عند نقطة التقاطع المسماة $(k, ?)$.'
        self.description_hindi = f'चित्र एक त्रिघात फलन (cubic function) का ग्राफ दिखाता है जिसके अंतःखंड (intercepts) अंकित हैं। एक ऊर्ध्वाधर रेखा खींची गई है। ग्राफ में दी गई जानकारी के आधार पर, $(k, ?)$ लेबल वाले प्रतिच्छेदन बिंदु पर $y$ का मान निर्धारित करें।'
        self.description_kazakh = f'Суретте қиылысу нүктелері белгіленген кубтық функцияның графигі көрсетілген. Тік сызық сызылған. Графиктегі ақпаратқа сүйене отырып, $(k, ?)$ деп белгіленген қиылысу нүктесіндегі $y$ мәнін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi wa kikyubi na vizuio vyake vikiwa vimewekwa lebo. Mstari wa wima umechora. Kulingana na taarifa kwenye grafu, tafuta thamani ya $y$ kwenye nukta ya makutano iliyowekwa lebo $(k, ?)$.'

class Mat017_multi(Mat017):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan grafik fungsi resiprokal dalam bentuk $y = \\frac{k}{x - p} + q$. Asimtot vertikal dan horizontal ditunjukkan sebagai garis putus-putus, dan satu titik pada kurva diberikan. Berdasarkan informasi yang diberikan dalam diagram, temukan nilai $y$ yang hilang pada titik yang ditunjukkan.'
        self.description_chinese = '图中显示了形式为 $y = \frac{k}{x - p} + q$ 的反比例函数的图像。垂直和水平渐近线显示为虚线，并给出了曲线上的一点。根据图中提供的信息，求出指示点处缺失的 $y$ 值。'
        self.description_arabic = 'يوضح الشكل الرسم البياني لدالة كسرية على الصورة $y = \frac{k}{x - p} + q$. تظهر الخطوط التقاربية الرأسية والأفقية كخطوط متقطعة، وتم إعطاء نقطة واحدة على المنحنى. بناءً على المعلومات المقدمة في المخطط، أوجد قيمة $y$ المفقودة عند النقطة المشار إليها.'
        self.description_hindi = 'चित्र $y = \\frac{k}{x - p} + q$ के रूप में एक व्युत्क्रम फलन (reciprocal function) का ग्राफ दिखाता है। ऊर्ध्वाधर और क्षैतिज अनंतस्पर्शी (asymptotes) को धराशायी रेखाओं के रूप में दिखाया गया है, और वक्र पर एक बिंदु दिया गया है। आरेख में दी गई जानकारी के आधार पर, इंगित बिंदु पर अज्ञात $y$-मान ज्ञात करें।'
        self.description_kazakh = 'Суретте $y = \frac{k}{x - p} + q$ түріндегі бөлшек-рационал функцияның графигі көрсетілген. Тік және көлденең асимптоталар үзік сызықтармен көрсетілген және қисықта бір нүкте берілген. Диаграммада берілген ақпаратқа сүйене отырып, көрсетілген нүктедегі жетіспейтін $y$ мәнін табыңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha grafu ya utendakazi rejeshi katika mfumo wa $y = \frac{k}{x - p} + q$. Asimptoti za wima na ulalo zinaonyeshwa kama mistari iliyokatikakatika, na nukta moja kwenye mzingo imetolewa. Kulingana na taarifa iliyotolewa kwenye mchoro, tafuta thamani ya $y$ inayokosekana kwenye nukta iliyoonyeshwa.'

class Mat018_multi(Mat018):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan grafik fungsi kubik. Titik $M$ adalah {self.m_type} lokal dari kurva tersebut. Berdasarkan gambar tersebut, carilah koordinat-{self.ask_for} dari $M$.'
        self.description_chinese = f'该图显示了一个三次函数的图像。点 $M$ 是曲线的局部{self.m_type}。根据该图，求 $M$ 的{self.ask_for}坐标。'
        self.description_arabic = f'يوضح المخطط الرسم البياني لدالة تكعيبية. النقطة $M$ هي {self.m_type} محلي للمنحنى. بناءً على الشكل، أوجد الإحداثي {self.ask_for} للنقطة $M$.'
        self.description_hindi = f'आरेख एक त्रिघात फलन का ग्राफ दिखाता है। बिंदु $M$ वक्र का एक स्थानीय {self.m_type} है। चित्र के आधार पर, $M$ का {self.ask_for}-निर्देशांक (coordinate) ज्ञात करें।'
        self.description_kazakh = f'Диаграммада кубтық функцияның графигі көрсетілген. $M$ нүктесі – қисықтың локальді {self.m_type}. Суретке сүйене отырып, $M$ нүктесінің {self.ask_for}-координатасын табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya utendakazi wa kikyubi. Nukta $M$ ni {self.m_type} ya kieneo ya mzingo. Kulingana na kielelezo, tafuta koordinate ya {self.ask_for} ya $M$.'

class Mat019_multi(Mat019):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan grafik fungsi kubik dan garis singgung $l$ yang menyentuh kurva pada titik $M$ seperti yang ditunjukkan pada gambar. Berdasarkan gambar tersebut, temukan nilai gradien $m$.'
        self.description_chinese = f'该图显示了一个三次函数的图像以及在点 $M$ 处与曲线相切的切线 $l$，如图所示。根据该图，求斜率 $m$ 的值。'
        self.description_arabic = f'يوضح المخطط الرسم البياني لدالة تكعيبية وخط مماس $l$ يمس المنحنى عند النقطة $M$ كما هو موضح في الشكل. بناءً على الشكل، أوجد قيمة الميل $m$.'
        self.description_hindi = f'आरेख एक त्रिघात फलन का ग्राफ और चित्र में दिखाए अनुसार बिंदु $M$ पर वक्र को छूने वाली एक स्पर्श रेखा (tangent line) $l$ दिखाता है। चित्र के आधार पर, प्रवणता (gradient) $m$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада кубтық функцияның графигі және суретте көрсетілгендей қисықты $M$ нүктесінде жанайтын $l$ жанамасы көрсетілген. Суретке сүйене отырып, $m$ градиентінің мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya utendakazi wa kikyubi na mstari wa tanjiti $l$ unaogusa mzingo kwenye nukta $M$ kama inavyoonyeshwa kwenye kielelezo. Kulingana na kielelezo, tafuta thamani ya mwinuko $m$.'

class Mat020_multi(Mat020):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan grafik parabola $g(x)$ dan garis sekan yang memotong kurva pada titik $A$ dan $B$. Terdapat titik $T$ pada kurva di mana garis singgungnya sejajar dengan garis sekan $AB$. Berdasarkan informasi yang diberikan dalam gambar, carilah koordinat-{self.ask_for} dari titik $T$.'
        self.description_chinese = f'该图显示了抛物线 $g(x)$ 的图像以及一条与曲线交于 $A$ 和 $B$ 两点的割线。曲线上有一点 $T$，其切线平行于割线 $AB$。根据图中提供的信息，求点 $T$ 的{self.ask_for}坐标。'
        self.description_arabic = f'يوضح المخطط الرسم البياني للقطع المكافئ $g(x)$ وقاطعًا يتقاطع مع المنحنى عند النقطتين $A$ و $B$. توجد نقطة $T$ على المنحنى حيث يكون الخط المماس موازيًا للقاطع $AB$. بناءً على المعلومات المقدمة في الشكل، أوجد الإحداثي {self.ask_for} للنقطة $T$.'
        self.description_hindi = f'आरेख परवलय (parabola) $g(x)$ का ग्राफ और वक्र को $A$ और $B$ बिंदुओं पर प्रतिच्छेद करने वाली एक छेदक रेखा (secant line) दिखाता है। वक्र पर एक बिंदु $T$ है जहाँ स्पर्श रेखा छेदक रेखा $AB$ के समानांतर है। चित्र में दी गई जानकारी के आधार पर, बिंदु $T$ का {self.ask_for}-निर्देशांक ज्ञात करें।'
        self.description_kazakh = f'Диаграммада $g(x)$ параболасының графигі және қисықты $A$ және $B$ нүктелерінде қиып өтетін қиюшы сызық көрсетілген. Қисықта жанамасы $AB$ қиюшысына параллель болатын $T$ нүктесі бар. Суретте берілген ақпаратқа сүйене отырып, $T$ нүктесінің {self.ask_for}-координатасын табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya parabola $g(x)$ na mstari sekanti unaokata mzingo kwenye nukta $A$ na $B$. Kuna nukta $T$ kwenye mzingo ambapo mstari wa tanjiti ni sambamba na sekanti $AB$. Kulingana na taarifa iliyotolewa kwenye kielelezo, tafuta koordinate ya {self.ask_for} ya nukta $T$.'

class Mat021_multi(Mat021):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan grafik fungsi kuadrat $f(x)$ sebagai garis tegas dan fungsi inversnya $f^{{-1}}(x)$ sebagai garis putus-putus. Berdasarkan koordinat yang diberikan dalam diagram, temukan nilai dari $f^{{-1}}({self.k})$.'
        self.description_chinese = f'图中实线显示了二次函数 $f(x)$ 的图像，虚线显示了其反函数 $f^{{-1}}(x)$ 的图像。根据图中提供的坐标，求 $f^{{-1}}({self.k})$ 的值。'
        self.description_arabic = f'يوضح الشكل الرسم البياني لدالة تربيعية $f(x)$ كخط متصل ودالتها العكسية $f^{{-1}}(x)$ كخط متقطع. بناءً على الإحداثيات المقدمة في المخطط، أوجد قيمة $f^{{-1}}({self.k})$.'
        self.description_hindi = f'चित्र एक ठोस रेखा के रूप में एक द्विघात फलन $f(x)$ और एक धराशायी रेखा के रूप में इसके व्युत्क्रम फलन $f^{{-1}}(x)$ का ग्राफ दिखाता है। आरेख में दिए गए निर्देशांकों के आधार पर, $f^{{-1}}({self.k})$ का मान ज्ञात करें।'
        self.description_kazakh = f'Суретте тұтас сызықпен $f(x)$ квадраттық функциясының графигі және үзік сызықпен оның кері функциясы $f^{{-1}}(x)$ көрсетілген. Диаграммада берілген координаталарға сүйене отырып, $f^{{-1}}({self.k})$ мәнін табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi wa kipeo cha pili $f(x)$ kama mstari kamili na utendakazi wake kinyume $f^{{-1}}(x)$ kama mstari uliokatikakatika. Kulingana na koordinate zilizotolewa kwenye mchoro, tafuta thamani ya $f^{{-1}}({self.k})$.'

class Mat022_multi(Mat022):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Sebuah pabrik menggunakan sistem pemrosesan dua tahap seperti yang ditunjukkan pada diagram. Berdasarkan input bahan baku dan fungsi dari setiap mesin, tentukan nilai produk akhir dalam liter.'
        self.description_chinese = '一家工厂使用如图所示的两阶段处理系统。根据原材料的输入和每台机器的功能，确定最终产品的数量（以升为单位）。'
        self.description_arabic = 'يستخدم مصنع نظام معالجة ثنائي المراحل كما هو موضح في المخطط. بناءً على مدخلات المواد الخام ووظائف كل آلة، حدد قيمة المنتج النهائي باللترات.'
        self.description_hindi = 'एक कारखाना आरेख में दिखाए अनुसार दो-चरणीय प्रसंस्करण प्रणाली का उपयोग करता है। कच्चे माल के इनपुट और प्रत्येक मशीन के कार्यों के आधार पर, अंतिम उत्पाद का मान लीटर में निर्धारित करें।'
        self.description_kazakh = 'Зауыт диаграммада көрсетілгендей екі кезеңді өңдеу жүйесін пайдаланады. Шикізат көлеміне және әрбір машинаның функцияларына сүйене отырып, соңғы өнімнің көлемін литрмен анықтаңыз.'
        self.description_swahili = 'Kiwanda kinatumia mfumo wa uchakataji wa hatua mbili kama inavyoonyeshwa kwenye mchoro. Kulingana na ingizo la malighafi na utendakazi wa kila mashine, amua thamani ya bidhaa ya mwisho katika lita.'

class Mat023_multi(Mat023):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan grafik fungsi resiprokal $f(x)$ yang melewati titik $P$. Berdasarkan informasi yang diberikan dalam diagram, tentukan {self.target_text}.'
        self.description_chinese = f'图中显示了经过点 $P$ 的反比例函数 $f(x)$ 的图像。根据图中提供的信息，确定 {self.target_text}。'
        self.description_arabic = f'يوضح الشكل الرسم البياني لدالة كسرية $f(x)$ تمر عبر النقطة $P$. بناءً على المعلومات المقدمة في المخطط، حدد {self.target_text}.'
        self.description_hindi = f'चित्र एक व्युत्क्रम फलन $f(x)$ का ग्राफ दिखाता है जो बिंदु $P$ से होकर गुजरता है। आरेख में दी गई जानकारी के आधार पर, {self.target_text} निर्धारित करें।'
        self.description_kazakh = f'Суретте $P$ нүктесі арқылы өтетін $f(x)$ кері функциясының графигі көрсетілген. Диаграммада берілген ақпаратқа сүйене отырып, {self.target_text} анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi rejeshi $f(x)$ ambayo inapita kwenye nukta $P$. Kulingana na taarifa iliyotolewa kwenye mchoro, amua {self.target_text}.'

class Mat024_multi(Mat024):
    def __init__(self):
        super().__init__()
        self.description_indonesian = "Sebuah robot bergerak dari titik $D$ ke titik $E$ di sepanjang garis kisi seperti yang ditunjukkan pada gambar. Jalur robot terdiri dari langkah horizontal dan vertikal, dan ia bergerak secara monotonik (tidak pernah menjauh dari tujuannya). Berdasarkan koordinat yang diberikan pada diagram, carilah total jarak yang ditempuh oleh robot tersebut."
        self.description_chinese = "如图所示，一个机器人沿着网格线从点 $D$ 移动到点 $E$。机器人的路径由水平和垂直步骤组成，并且它是单调移动的（从不远离其目的地）。根据图中提供的坐标，求机器人行驶的总距离。"
        self.description_arabic = "ينتقل روبوت من النقطة $D$ إلى النقطة $E$ على طول خطوط الشبكة كما هو موضح في الشكل. يتكون مسار الروبوت من خطوات أفقية ورأسية، ويتحرك بشكل رتيب (لا يبتعد أبدًا عن وجهته). بناءً على الإحداثيات المقدمة في المخطط، أوجد المسافة الإجمالية التي قطعها الروبوت."
        self.description_hindi = "एक रोबोट चित्र में दिखाए अनुसार ग्रिड लाइनों के साथ बिंदु $D$ से बिंदु $E$ तक यात्रा करता है। रोबोट के पथ में क्षैतिज और ऊर्ध्वाधर कदम शामिल हैं, और यह एकदिष्ट रूप से (monotonically) चलता है (यह कभी भी अपने गंतव्य से दूर नहीं जाता है)। आरेख में दिए गए निर्देशांकों के आधार पर, रोबोट द्वारा तय की गई कुल दूरी ज्ञात करें।"
        self.description_kazakh = "Робот суретте көрсетілгендей тор сызықтарының бойымен $D$ нүктесінен $E$ нүктесіне барады. Роботтың жолы көлденең және тік қадамдардан тұрады және ол монотонды қозғалады (ол ешқашан мақсатынан ауытқымайды). Диаграммада берілген координаталарға сүйене отырып, робот жүріп өткен жалпы қашықтықты табыңыз."
        self.description_swahili = "Roboti inasafiri kutoka nukta $D$ hadi nukta $E$ kando ya mistari ya gridi kama inavyoonyeshwa kwenye kielelezo. Njia ya roboti inajumuisha hatua za ulalo na wima, na inasonga kwa mwelekeo mmoja (hairudi nyuma kutoka kwenye kituo chake). Kulingana na koordinate zilizotolewa kwenye mchoro, tafuta umbali wa jumla uliosafiriwa na roboti."

class Mat025_multi(Mat025):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan segitiga siku-siku $MNO$. Titik $O$ berada pada titik asal $(0,0)$ dan titik $N$ berada pada sumbu-$x$. Luas segitiga $MNO$ adalah {self.area} satuan luas. Berdasarkan koordinat yang ditunjukkan pada gambar, hitunglah gradien dari segmen garis $MO$.'
        self.description_chinese = f'该图显示了一个直角三角形 $MNO$。点 $O$ 位于原点 $(0,0)$，点 $N$ 位于 $x$ 轴上。三角形 $MNO$ 的面积为 {self.area} 平方单位。根据图中显示的坐标，计算线段 $MO$ 的斜率。'
        self.description_arabic = f'يوضح المخطط مثلثًا قائم الزاوية $MNO$. النقطة $O$ تقع عند نقطة الأصل $(0,0)$ والنقطة $N$ تقع على المحور $x$. مساحة المثلث $MNO$ هي {self.area} وحدة مربعة. بناءً على الإحداثيات الموضحة في الشكل، احسب ميل القطعة المستقيمة $MO$.'
        self.description_hindi = f'आरेख एक समकोण त्रिभुज $MNO$ दिखाता है। बिंदु $O$ मूल बिंदु $(0,0)$ पर है और बिंदु $N$, $x$-अक्ष पर है। त्रिभुज $MNO$ का क्षेत्रफल {self.area} वर्ग इकाई है। चित्र में दिखाए गए निर्देशांकों के आधार पर, रेखाखंड $MO$ की प्रवणता की गणना करें।'
        self.description_kazakh = f'Диаграммада $MNO$ тікбұрышты үшбұрышы көрсетілген. $O$ нүктесі бас нүктеде $(0,0)$ орналасқан және $N$ нүктесі $x$ осінде жатыр. $MNO$ үшбұрышының ауданы {self.area} квадрат бірлікке тең. Суретте көрсетілген координаталарға сүйене отырып, $MO$ кесіндісінің градиентін есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha pembetatu mraba $MNO$. Nukta $O$ ipo kwenye asili $(0,0)$ na nukta $N$ ipo kwenye mhimili wa $x$. Eneo la pembetatu $MNO$ ni vipimo vya mraba {self.area}. Kulingana na koordinate zilizoonyeshwa kwenye kielelezo, kokotoa mwinuko wa pingili ya mstari $MO$.'

class Mat026_multi(Mat026):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan tiga titik kolinear $P$, $Q$, dan $R$ pada suatu kisi koordinat. Titik $P$ memiliki koordinat-$x$ yang tidak diketahui, $k$. Berdasarkan koordinat yang ditunjukkan, hitunglah nilai $k$.'
        self.description_chinese = '该图显示了坐标网格上的三个共线点 $P$、$Q$ 和 $R$。点 $P$ 的 $x$ 坐标未知，为 $k$。根据显示的坐标，计算 $k$ 的值。'
        self.description_arabic = 'يوضح المخطط ثلاث نقاط تقع على خط مستقيم واحد $P$ و $Q$ و $R$ على شبكة إحداثيات. النقطة $P$ لها إحداثي $x$ غير معروف، $k$. بناءً على الإحداثيات الموضحة، احسب قيمة $k$.'
        self.description_hindi = 'आरेख एक समन्वय ग्रिड पर तीन संरेखीय (collinear) बिंदु $P$, $Q$ और $R$ दिखाता है। बिंदु $P$ का एक अज्ञात $x$-निर्देशांक $k$ है। दिखाए गए निर्देशांकों के आधार पर, $k$ के मान की गणना करें।'
        self.description_kazakh = 'Диаграммада координаталық тордағы үш коллинеар $P$, $Q$ және $R$ нүктелері көрсетілген. $P$ нүктесінің $x$-координатасы белгісіз $k$. Көрсетілген координаталарға сүйене отырып, $k$ мәнін есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha nukta tatu zilizonyooka kwenye mstari mmoja $P$, $Q$, na $R$ kwenye gridi ya koordinate. Nukta $P$ ina koordinate ya $x$ isiyojulikana, $k$. Kulingana na koordinate zilizoonyeshwa, kokotoa thamani ya $k$.'

class Mat027_multi(Mat027):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan garis $L_1$ yang melewati titik $A$ dan $B$. Garis $L_2$ tegak lurus terhadap $L_1$ dan memotong sumbu-$y$ pada titik yang sama dengan $L_1$. Berdasarkan gambar tersebut, hitunglah gradien garis $L_2$.'
        self.description_chinese = '该图显示了穿过点 $A$ 和 $B$ 的直线 $L_1$。直线 $L_2$ 垂直于 $L_1$，并在与 $L_1$ 相同的点处与 $y$ 轴相交。根据该图，计算直线 $L_2$ 的斜率。'
        self.description_arabic = 'يوضح المخطط الخط $L_1$ الذي يمر عبر النقطتين $A$ و $B$. الخط $L_2$ عمودي على $L_1$ ويقطع المحور $y$ في نفس النقطة مثل $L_1$. بناءً على الشكل، احسب ميل الخط $L_2$.'
        self.description_hindi = 'आरेख बिंदुओं $A$ और $B$ से गुजरने वाली रेखा $L_1$ दिखाता है। रेखा $L_2$, $L_1$ के लंबवत है और $y$-अक्ष को उसी बिंदु पर प्रतिच्छेद करती है जिस पर $L_1$ करती है। चित्र के आधार पर, रेखा $L_2$ की प्रवणता की गणना करें।'
        self.description_kazakh = 'Диаграммада $A$ және $B$ нүктелері арқылы өтетін $L_1$ түзуі көрсетілген. $L_2$ түзуі $L_1$-ге перпендикуляр және $y$-осін $L_1$ сияқты бірдей нүктеде қиып өтеді. Суретке сүйене отырып, $L_2$ түзуінің градиентін есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha mstari $L_1$ ukipita kwenye nukta $A$ na $B$. Mstari $L_2$ ni wima kwa $L_1$ na unakata mhimili wa $y$ kwenye nukta sawa na $L_1$. Kulingana na kielelezo, kokotoa mwinuko wa mstari $L_2$.'

class Mat028_multi(Mat028):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan segitiga $ABC$ yang diplot pada suatu kisi koordinat. Luas segitiga tersebut adalah ${self.area}$ satuan luas. Berdasarkan gambar tersebut, temukan nilai $k$.'
        self.description_chinese = f'该图显示了绘制在坐标网格上的三角形 $ABC$。该三角形的面积为 ${self.area}$ 平方单位。根据该图，求 $k$ 的值。'
        self.description_arabic = f'يوضح المخطط المثلث $ABC$ مرسومًا على شبكة إحداثيات. مساحة المثلث هي ${self.area}$ وحدة مربعة. بناءً على الشكل، أوجد قيمة $k$.'
        self.description_hindi = f'आरेख समन्वय ग्रिड पर आलेखित त्रिभुज $ABC$ को दिखाता है। त्रिभुज का क्षेत्रफल ${self.area}$ वर्ग इकाई है। चित्र के आधार पर, $k$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада координаталық торда салынған $ABC$ үшбұрышы көрсетілген. Үшбұрыштың ауданы ${self.area}$ квадрат бірлікке тең. Суретке сүйене отырып, $k$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha pembetatu $ABC$ iliyochorwa kwenye gridi ya koordinate. Eneo la pembetatu ni vipimo vya mraba ${self.area}$. Kulingana na kielelezo, tafuta thamani ya $k$.'

class Mat029_multi(Mat029):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan sebuah segmen garis $AB$. Titik $C$ adalah titik tengah dari $AB$, titik $D$ adalah titik tengah dari $AC$, dan titik $E$ adalah titik tengah dari $DB$. Berdasarkan koordinat yang diberikan pada gambar, hitunglah panjang segmen $AE$.'
        self.description_chinese = '该图显示了一条线段 $AB$。点 $C$ 是 $AB$ 的中点，点 $D$ 是 $AC$ 的中点，点 $E$ 是 $DB$ 的中点。根据图中提供的坐标，计算线段 $AE$ 的长度。'
        self.description_arabic = 'يوضح المخطط القطعة المستقيمة $AB$. النقطة $C$ هي منتصف $AB$، والنقطة $D$ هي منتصف $AC$، والنقطة $E$ هي منتصف $DB$. بناءً على الإحداثيات المقدمة في الشكل، احسب طول القطعة $AE$.'
        self.description_hindi = 'आरेख एक रेखाखंड $AB$ दिखाता है। बिंदु $C$, $AB$ का मध्यबिंदु है, बिंदु $D$, $AC$ का मध्यबिंदु है, और बिंदु $E$, $DB$ का मध्यबिंदु है। चित्र में दिए गए निर्देशांकों के आधार पर, खंड $AE$ की लंबाई की गणना करें।'
        self.description_kazakh = 'Диаграммада $AB$ кесіндісі көрсетілген. $C$ нүктесі – $AB$ ортасы, $D$ нүктесі – $AC$ ортасы және $E$ нүктесі – $DB$ ортасы. Суретте берілген координаталарға сүйене отырып, $AE$ кесіндісінің ұзындығын есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha pingili ya mstari $AB$. Nukta $C$ ni nukta ya kati ya $AB$, nukta $D$ ni nukta ya kati ya $AC$, na nukta $E$ ni nukta ya kati ya $DB$. Kulingana na koordinate zilizotolewa kwenye kielelezo, kokotoa urefu wa pingili $AE$.'

class Mat030_multi(Mat030):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sebuah segmen garis $PQ$ pada bidang koordinat. Berdasarkan gambar tersebut, carilah jarak tegak lurus dari titik tengah $PQ$ ke {self.target_axis}.'
        self.description_chinese = f'该图显示了坐标平面上的一条线段 $PQ$。根据该图，求从 $PQ$ 的中点到 {self.target_axis} 的垂直距离。'
        self.description_arabic = f'يوضح المخطط القطعة المستقيمة $PQ$ على مستوى إحداثي. بناءً على الشكل، أوجد المسافة العمودية من منتصف $PQ$ إلى المحور {self.target_axis}.'
        self.description_hindi = f'आरेख एक समन्वय तल पर एक रेखाखंड $PQ$ दिखाता है। चित्र के आधार पर, $PQ$ के मध्यबिंदु से {self.target_axis} तक की लंबवत दूरी (perpendicular distance) ज्ञात करें।'
        self.description_kazakh = f'Диаграммада координаталық жазықтықтағы $PQ$ кесіндісі көрсетілген. Суретке сүйене отырып, $PQ$ ортасынан {self.target_axis}-не дейінгі перпендикуляр қашықтықты табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha pingili ya mstari $PQ$ kwenye bapa la koordinate. Kulingana na kielelezo, tafuta umbali wa wima kutoka kwenye nukta ya kati ya $PQ$ hadi kwenye {self.target_axis}.'

class Mat031_multi(Mat031):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan grafik sebuah garis lurus. Berdasarkan informasi yang diberikan dalam diagram, temukan nilai titik potong sumbu-$y$, $c$.'
        self.description_chinese = '图中显示了一条直线的图像。根据图中提供的信息，求 $y$ 截距 $c$ 的值。'
        self.description_arabic = 'يوضح الشكل الرسم البياني لخط مستقيم. بناءً على المعلومات المقدمة في المخطط، أوجد قيمة نقطة التقاطع مع المحور $y$، $c$.'
        self.description_hindi = 'चित्र एक सीधी रेखा का ग्राफ दिखाता है। आरेख में दी गई जानकारी के आधार पर, $y$-अंतःखंड ($y$-intercept), $c$ का मान ज्ञात करें।'
        self.description_kazakh = 'Суретте түзу сызықтың графигі көрсетілген. Диаграммада берілген ақпаратқа сүйене отырып, $y$-осімен қиылысу нүктесінің $c$ мәнін табыңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha grafu ya mstari mnyoofu. Kulingana na taarifa iliyotolewa kwenye mchoro, tafuta thamani ya kizuio cha $y$, $c$.'

class Mat032_multi(Mat032):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Garis L ditunjukkan pada kisi. Carilah persamaan garis L dalam bentuk y = mx + c.'
        self.description_chinese = f'直线 L 显示在网格上。求直线 L 的方程，形式为 y = mx + c。'
        self.description_arabic = f'الخط L موضح على الشبكة. أوجد معادلة الخط L على الصورة y = mx + c.'
        self.description_hindi = f'रेखा L को ग्रिड पर दिखाया गया है। रेखा L का समीकरण y = mx + c के रूप में ज्ञात करें।'
        self.description_kazakh = f'Торда L түзуі көрсетілген. L түзуінің теңдеуін y = mx + c түрінде табыңыз.'
        self.description_swahili = f'Mstari L unaonyeshwa kwenye gridi. Tafuta mlinganyo wa mstari L katika mfumo wa y = mx + c.'

class Mat033_multi(Mat033):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menampilkan garis lurus $L$ dan garis putus-putus $M$ dengan persamaan ${self.line_m_eq}$. Seperti yang ditunjukkan pada gambar, carilah koordinat-${self.find_coord}$ dari titik potongnya.'
        self.description_chinese = f'图中显示了一条直线 $L$ 和一条方程为 ${self.line_m_eq}$ 的虚线 $M$。如图所示，求交点的 ${self.find_coord}$ 坐标。'
        self.description_arabic = f'يعرض الشكل خطًا مستقيمًا $L$ وخطًا متقطعًا $M$ بالمعادلة ${self.line_m_eq}$. كما هو موضح في الشكل، أوجد الإحداثي ${self.find_coord}$ لنقطة التقاطع.'
        self.description_hindi = f'चित्र एक सीधी रेखा $L$ और समीकरण ${self.line_m_eq}$ वाली एक धराशायी रेखा $M$ प्रदर्शित करता है। जैसा कि चित्र में दिखाया गया है, प्रतिच्छेदन बिंदु का ${self.find_coord}$-निर्देशांक ज्ञात करें।'
        self.description_kazakh = f'Суретте $L$ түзуі және ${self.line_m_eq}$ теңдеуімен берілген үзік сызықты $M$ түзуі көрсетілген. Суретте көрсетілгендей, қиылысу нүктесінің ${self.find_coord}$-координатасын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mstari mnyoofu $L$ na mstari uliokatikakatika $M$ wenye mlinganyo ${self.line_m_eq}$. Kama inavyoonyeshwa kwenye kielelezo, tafuta koordinate ya ${self.find_coord}$ ya nukta ya makutano.'

class Mat034_multi(Mat034):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan dua garis sejajar, $L_1$ dan $L_2$. Berdasarkan informasi yang diberikan dalam diagram, temukan koordinat-{self.target_var} dari titik pada $L_2$ di mana koordinat-{self.given_var} adalah {self.const_val}.'
        self.description_chinese = f'图中显示了两条平行线 $L_1$ 和 $L_2$。根据图中提供的信息，求 $L_2$ 上当 {self.given_var} 坐标为 {self.const_val} 时该点的 {self.target_var} 坐标。'
        self.description_arabic = f'يوضح الشكل خطين متوازيين، $L_1$ و $L_2$. بناءً على المعلومات المقدمة في المخطط، أوجد الإحداثي {self.target_var} للنقطة على $L_2$ حيث يكون الإحداثي {self.given_var} هو {self.const_val}.'
        self.description_hindi = f'चित्र दो समानांतर रेखाएँ, $L_1$ और $L_2$ दिखाता है। आरेख में दी गई जानकारी के आधार पर, $L_2$ पर उस बिंदु का {self.target_var}-निर्देशांक ज्ञात करें जहाँ {self.given_var}-निर्देशांक {self.const_val} है।'
        self.description_kazakh = f'Суретте екі параллель $L_1$ және $L_2$ түзулері көрсетілген. Диаграммада берілген ақпаратқа сүйене отырып, $L_2$ түзуіндегі {self.given_var}-координатасы {self.const_val} болатын нүктенің {self.target_var}-координатасын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mistari miwili sambamba, $L_1$ na $L_2$. Kulingana na taarifa iliyotolewa kwenye mchoro, tafuta koordinate ya {self.target_var} ya nukta kwenye $L_2$ ambapo koordinate ya {self.given_var} ni {self.const_val}.'

class Mat035_multi(Mat035):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan dua garis, garis $k$ dan garis $m$, di mana garis $m$ sejajar dengan garis $k$. Berdasarkan koordinat dan informasi yang diberikan dalam diagram, temukan koordinat-{self.target_var} pada garis $m$ ketika koordinat-{self.given_var} adalah {self.const_val}.'
        self.description_chinese = f'图中显示了两条直线，直线 $k$ 和直线 $m$，其中直线 $m$ 平行于直线 $k$。根据图中提供的坐标和信息，求当 {self.given_var} 坐标为 {self.const_val} 时直线 $m$ 上的 {self.target_var} 坐标。'
        self.description_arabic = f'يوضح الشكل خطين، الخط $k$ والخط $m$، حيث يكون الخط $m$ موازيًا للخط $k$. بناءً على الإحداثيات والمعلومات المقدمة في المخطط، أوجد الإحداثي {self.target_var} على الخط $m$ عندما يكون الإحداثي {self.given_var} هو {self.const_val}.'
        self.description_hindi = f'चित्र दो रेखाएँ, रेखा $k$ और रेखा $m$ दिखाता है, जहाँ रेखा $m$ रेखा $k$ के समानांतर है। आरेख में दिए गए निर्देशांक और जानकारी के आधार पर, जब {self.given_var}-निर्देशांक {self.const_val} हो तो रेखा $m$ पर {self.target_var}-निर्देशांक ज्ञात करें।'
        self.description_kazakh = f'Суретте екі түзу, $k$ және $m$ түзулері көрсетілген, мұндағы $m$ түзуі $k$ түзуіне параллель. Диаграммада берілген координаталар мен ақпаратқа сүйене отырып, {self.given_var}-координатасы {self.const_val} болған кездегі $m$ түзуіндегі {self.target_var}-координатасын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mistari miwili, mstari $k$ na mstari $m$, ambapo mstari $m$ ni sambamba na mstari $k$. Kulingana na koordinate na taarifa iliyotolewa kwenye mchoro, tafuta koordinate ya {self.target_var} kwenye mstari $m$ wakati koordinate ya {self.given_var} ni {self.const_val}.'

class Mat036_multi(Mat036):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Seperti yang ditunjukkan dalam diagram, garis $M$ tegak lurus terhadap garis $L$. Carilah koordinat-{self.find_var} dari titik di mana garis $M$ memotong garis ${self.given_line}$.'
        self.description_chinese = f'如图所示，直线 $M$ 垂直于直线 $L$。求直线 $M$ 与直线 ${self.given_line}$ 相交处的 {self.find_var} 坐标。'
        self.description_arabic = f'كما هو موضح في المخطط، الخط $M$ عمودي على الخط $L$. أوجد الإحداثي {self.find_var} للنقطة التي يتقاطع فيها الخط $M$ مع الخط ${self.given_line}$.'
        self.description_hindi = f'जैसा कि आरेख में दिखाया गया है, रेखा $M$ रेखा $L$ के लंबवत है। उस बिंदु का {self.find_var}-निर्देशांक ज्ञात करें जहाँ रेखा $M$ रेखा ${self.given_line}$ को प्रतिच्छेद करती है।'
        self.description_kazakh = f'Диаграммада көрсетілгендей, $M$ түзуі $L$ түзуіне перпендикуляр. $M$ түзуі ${self.given_line}$ түзуін қиып өтетін нүктенің {self.find_var}-координатасын табыңыз.'
        self.description_swahili = f'Kama inavyoonyeshwa kwenye mchoro, mstari $M$ ni wima kwa mstari $L$. Tafuta koordinate ya {self.find_var} ya nukta ambapo mstari $M$ unakata mstari ${self.given_line}$.'

class Mat037_multi(Mat037):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan garis $L$ dan garis $P$, di mana garis $P$ tegak lurus terhadap garis $L$. Berdasarkan koordinat yang diberikan dalam diagram, temukan koordinat-{self.target_var} dari titik pada garis $P$ di mana koordinat-{self.given_var} adalah {self.const_val}.'
        self.description_chinese = f'图中显示了直线 $L$ 和直线 $P$，其中直线 $P$ 垂直于直线 $L$。根据图中提供的坐标，求直线 $P$ 上当 {self.given_var} 坐标为 {self.const_val} 时该点的 {self.target_var} 坐标。'
        self.description_arabic = f'يوضح الشكل الخط $L$ والخط $P$، حيث يكون الخط $P$ عموديًا على الخط $L$. بناءً على الإحداثيات المقدمة في المخطط، أوجد الإحداثي {self.target_var} للنقطة على الخط $P$ حيث يكون الإحداثي {self.given_var} هو {self.const_val}.'
        self.description_hindi = f'चित्र रेखा $L$ और रेखा $P$ दिखाता है, जहाँ रेखा $P$ रेखा $L$ के लंबवत है। आरेख में दिए गए निर्देशांकों के आधार पर, रेखा $P$ पर उस बिंदु का {self.target_var}-निर्देशांक ज्ञात करें जहाँ {self.given_var}-निर्देशांक {self.const_val} है।'
        self.description_kazakh = f'Суретте $L$ түзуі және $P$ түзуі көрсетілген, мұндағы $P$ түзуі $L$ түзуіне перпендикуляр. Диаграммада берілген координаталарға сүйене отырып, $P$ түзуіндегі {self.given_var}-координатасы {self.const_val} болатын нүктенің {self.target_var}-координатасын табыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mstari $L$ na mstari $P$, ambapo mstari $P$ ni wima kwa mstari $L$. Kulingana na koordinate zilizotolewa kwenye mchoro, tafuta koordinate ya {self.target_var} ya nukta kwenye mstari $P$ ambapo koordinate ya {self.given_var} ni {self.const_val}.'

class Mat038_multi(Mat038):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan dua garis yang saling tegak lurus, garis $k$ dan garis $l$, yang berpotongan di titik $C$. Berdasarkan koordinat titik $A$ dan $B$ serta persamaan yang diberikan dalam diagram, carilah luas segitiga $ABC$.'
        self.description_chinese = '图中显示了两条相互垂直的直线 $k$ 和 $l$，它们在点 $C$ 处相交。根据点 $A$ 和 $B$ 的坐标以及图中提供的方程，求三角形 $ABC$ 的面积。'
        self.description_arabic = 'يوضح الشكل خطين متعامدين، الخط $k$ والخط $l$، يتقاطعان في النقطة $C$. بناءً على إحداثيات النقطتين $A$ و $B$ والمعادلات المقدمة في المخطط، أوجد مساحة المثلث $ABC$.'
        self.description_hindi = 'चित्र दो लंबवत रेखाएँ, रेखा $k$ और रेखा $l$ दिखाता है, जो बिंदु $C$ पर प्रतिच्छेद करती हैं। बिंदुओं $A$ और $B$ के निर्देशांक और आरेख में दिए गए समीकरणों के आधार पर, त्रिभुज $ABC$ का क्षेत्रफल ज्ञात करें।'
        self.description_kazakh = 'Суретте $C$ нүктесінде қиылысатын екі перпендикуляр $k$ және $l$ түзулері көрсетілген. $A$ және $B$ нүктелерінің координаталарына және диаграммада берілген теңдеулерге сүйене отырып, $ABC$ үшбұрышының ауданын табыңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha mistari miwili ya wima, mstari $k$ na mstari $l$, ambayo inakata kwenye nukta $C$. Kulingana na koordinate za nukta $A$ na $B$ na milinganyo iliyotolewa kwenye mchoro, tafuta eneo la pembetatu $ABC$.'

class Mat039_multi(Mat039):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Persegi panjang $A$ sebangun secara matematis dengan persegi panjang $B$. Hitunglah nilai $x$.'
        self.description_chinese = f'矩形 $A$ 在数学上与矩形 $B$ 相似。求 $x$ 的值。'
        self.description_arabic = f'المستطيل $A$ مشابه رياضيًا للمستطيل $B$. احسب قيمة $x$.'
        self.description_hindi = f'आयत $A$ गणितीय रूप से आयत $B$ के समरूप (similar) है। $x$ का मान ज्ञात करें।'
        self.description_kazakh = f'$A$ тіктөртбұрышы $B$ тіктөртбұрышына математикалық тұрғыда ұқсас. $x$ мәнін есептеңіз.'
        self.description_swahili = f'Mstatili $A$ unafanana kihisabati na mstatili $B$. Tafuta thamani ya $x$.'

class Mat040_multi(Mat040):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Bangun ruang $A$ sebangun secara matematis dengan bangun ruang $B$. Diagram tersebut menunjukkan tinggi dan luas permukaan ($S_A$ dan $S_B$) dari kedua bangun ruang. Hitunglah tinggi, $H$, dari bangun ruang $B$.'
        self.description_chinese = f'立体 $A$ 在数学上与立体 $B$ 相似。该图显示了这两个立体的高度和表面积（$S_A$ 和 $S_B$）。计算立体 $B$ 的高度 $H$。'
        self.description_arabic = f'المجسم $A$ مشابه رياضيًا للمجسم $B$. يوضح المخطط الارتفاعات ومساحات السطح ($S_A$ و $S_B$) لكلا المجسمين. احسب الارتفاع، $H$، للمجسم $B$.'
        self.description_hindi = f'ठोस $A$ गणितीय रूप से ठोस $B$ के समरूप है। आरेख दोनों ठोसों के लिए ऊँचाई और पृष्ठीय क्षेत्रफल ($S_A$ और $S_B$) दिखाता है। ठोस $B$ की ऊँचाई, $H$, की गणना करें।'
        self.description_kazakh = f'$A$ денесі $B$ денесіне математикалық тұрғыда ұқсас. Диаграммада екі дененің биіктіктері мен бетінің аудандары ($S_A$ және $S_B$) көрсетілген. $B$ денесінің биіктігін, $H$, есептеңіз.'
        self.description_swahili = f'Umbo dhabiti $A$ linafanana kihisabati na umbo dhabiti $B$. Mchoro unaonyesha kimo na maeneo ya uso ($S_A$ na $S_B$) kwa maumbo dhabiti yote mawili. Kokotoa kimo, $H$, cha umbo dhabiti $B$.'

class Mat041_multi(Mat041):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Bangun ruang $A$ dan bangun ruang $B$ sebangun secara matematis. Diagram tersebut menunjukkan tinggi dan volume ($V_A$ dan $V_B$) dari kedua bangun ruang. Hitunglah volume, $V_B$, dari bangun ruang $B$.'
        self.description_chinese = f'立体 $A$ 和立体 $B$ 在数学上相似。该图显示了这两个立体的高度和体积（$V_A$ 和 $V_B$）。计算立体 $B$ 的体积 $V_B$。'
        self.description_arabic = f'المجسم $A$ والمجسم $B$ متشابهان رياضيًا. يوضح المخطط الارتفاعات والأحجام ($V_A$ و $V_B$) لكلا المجسمين. احسب الحجم، $V_B$، للمجسم $B$.'
        self.description_hindi = f'ठोस $A$ और ठोस $B$ गणितीय रूप से समरूप हैं। आरेख दोनों ठोसों के लिए ऊँचाई और आयतन ($V_A$ और $V_B$) दिखाता है। ठोस $B$ के आयतन, $V_B$, की गणना करें।'
        self.description_kazakh = f'$A$ денесі мен $B$ денесі математикалық тұрғыда ұқсас. Диаграммада екі дененің биіктіктері мен көлемдері ($V_A$ және $V_B$) көрсетілген. $B$ денесінің көлемін, $V_B$, есептеңіз.'
        self.description_swahili = f'Umbo dhabiti $A$ na umbo dhabiti $B$ yanafanana kihisabati. Mchoro unaonyesha kimo na ujazo ($V_A$ na $V_B$) kwa maumbo dhabiti yote mawili. Kokotoa ujazo, $V_B$, wa umbo dhabiti $B$.'

class Mat042_multi(Mat042):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sebuah segi empat dengan sisi-sisi yang sama panjang. Hitunglah nilai $a$.'
        self.description_chinese = f'该图显示了一个各边长度相等的四边形。求 $a$ 的值。'
        self.description_arabic = f'يوضح المخطط شكلًا رباعيًا بأضلاع متساوية الطول. احسب قيمة $a$.'
        self.description_hindi = f'आरेख समान लंबाई की भुजाओं वाला एक चतुर्भुज दिखाता है। $a$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада қабырғаларының ұзындығы тең төртбұрыш көрсетілген. $a$ мәнін есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha pembenne yenye pande za urefu sawa. Tafuta thamani ya $a$.'

class Mat043_multi(Mat043):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'$BDC$ adalah garis lurus, $AB = AC$, sudut $ABD = {round(self.angle_B, 2)}^\\circ$ dan sudut $ADC = {round(self.angle_ADC, 2)}^\\circ$. \\\\ Hitunglah sudut $DAC$.'
        self.description_chinese = f'$BDC$ 是一条直线，$AB = AC$，角 $ABD = {round(self.angle_B, 2)}^\circ$ 且角 $ADC = {round(self.angle_ADC, 2)}^\circ$。 \\\\ 求角 $DAC$。'
        self.description_arabic = f'$BDC$ هو خط مستقيم، $AB = AC$، والزاوية $ABD = {round(self.angle_B, 2)}^\circ$ والزاوية $ADC = {round(self.angle_ADC, 2)}^\circ$. \\ احسب الزاوية $DAC$.'
        self.description_hindi = f'$BDC$ एक सीधी रेखा है, $AB = AC$, कोण $ABD = {round(self.angle_B, 2)}^\\circ$ और कोण $ADC = {round(self.angle_ADC, 2)}^\\circ$ है। \\\\ कोण $DAC$ ज्ञात करें।'
        self.description_kazakh = f'$BDC$ - түзу сызық, $AB = AC$, $ABD$ бұрышы = {round(self.angle_B, 2)}^\\circ$ және $ADC$ бұрышы = {round(self.angle_ADC, 2)}^\\circ$. \\\\ $DAC$ бұрышын есептеңіз.'
        self.description_swahili = f'$BDC$ ni mstari mnyoofu, $AB = AC$, pembe $ABD = {round(self.angle_B, 2)}^\\circ$ na pembe $ADC = {round(self.angle_ADC, 2)}^\\circ$. \\\\ Tafuta pembe $DAC$.'

class Mat044_multi(Mat044):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Garis $AB$ dan $CD$ sejajar. $EF$ dan $EG$ adalah garis lurus. Sudut yang terbentuk pada perpotongan $EF$ dan $CD$ adalah {self.angle_top:.2f}°. Carilah nilai $a$.'
        self.description_chinese = f'直线 $AB$ 和 $CD$ 相互平行。$EF$ 和 $EG$ 是直线。在 $EF$ 和 $CD$ 的交点处形成的角为 {self.angle_top:.2f}°。求 $a$ 的值。'
        self.description_arabic = f'الخطان $AB$ و $CD$ متوازيان. $EF$ و $EG$ خطان مستقيمان. الزاوية المتكونة عند تقاطع $EF$ و $CD$ هي {self.angle_top:.2f}°. أوجد قيمة $a$.'
        self.description_hindi = f'रेखाएँ $AB$ और $CD$ समानांतर हैं। $EF$ और $EG$ सीधी रेखाएँ हैं। $EF$ और $CD$ के प्रतिच्छेदन पर बनने वाला कोण {self.angle_top:.2f}° है। $a$ का मान ज्ञात करें।'
        self.description_kazakh = f'$AB$ және $CD$ түзулері параллель. $EF$ және $EG$ - түзу сызықтар. $EF$ және $CD$ қиылысуында пайда болған бұрыш {self.angle_top:.2f}°. $a$ мәнін табыңыз.'
        self.description_swahili = f'Mistari $AB$ na $CD$ ni sambamba. $EF$ na $EG$ ni mistari minyoofu. Pembe inayoundwa kwenye makutano ya $EF$ na $CD$ ni {self.angle_top:.2f}°. Tafuta thamani ya $a$.'

class Mat045_multi(Mat045):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sudut-sudut dalam sebuah {self.shape_name}, ditulis dalam bentuk $x$. Carilah nilai $x$.'
        self.description_chinese = f'该图显示了用 $x$ 表示的 {self.shape_name} 的内角。求 $x$ 的值。'
        self.description_arabic = f'يوضح المخطط الزوايا الداخلية لـ {self.shape_name}، مكتوبة بدلالة $x$. أوجد قيمة $x$.'
        self.description_hindi = f'आरेख एक {self.shape_name} के आंतरिक कोणों को दिखाता है, जिन्हें $x$ के पदों में लिखा गया है। $x$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада $x$ арқылы жазылған {self.shape_name} ішкі бұрыштары көрсетілген. $x$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha pembe za ndani za {self.shape_name}, zilizoandikwa kwa kutumia $x$. Tafuta thamani ya $x$.'

class Mat046_multi(Mat046):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan segi empat tali busur $ABCD$. Diagonal $BD$ dan $AC$ berpotongan. Sudut $BAD = {self.angle_bad}^\\circ$ dan sudut $BCA = {self.angle_bca}^\\circ$. Carilah nilai sudut $ABD$.'
        self.description_chinese = f'该图显示了一个圆内接四边形 $ABCD$。对角线 $BD$ 和 $AC$ 相交。角 $BAD = {self.angle_bad}^\circ$，角 $BCA = {self.angle_bca}^\circ$。求角 $ABD$ 的值。'
        self.description_arabic = f'يوضح المخطط رباعيًا دائريًا $ABCD$. يتقاطع القطران $BD$ و $AC$. الزاوية $BAD = {self.angle_bad}^\circ$ والزاوية $BCA = {self.angle_bca}^\circ$. أوجد قيمة الزاوية $ABD$.'
        self.description_hindi = f'आरेख एक चक्रीय चतुर्भुज (cyclic quadrilateral) $ABCD$ दिखाता है। विकर्ण $BD$ और $AC$ प्रतिच्छेद करते हैं। कोण $BAD = {self.angle_bad}^\\circ$ और कोण $BCA = {self.angle_bca}^\\circ$ है। कोण $ABD$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада шеңберге іштей сызылған $ABCD$ төртбұрышы көрсетілген. $BD$ және $AC$ диагональдары қиылысады. $BAD$ бұрышы = {self.angle_bad}^\\circ$ және $BCA$ бұрышы = {self.angle_bca}^\\circ$. $ABD$ бұрышының мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha pembenne mzingo $ABCD$. Ulalo $BD$ na $AC$ inakata. Pembe $BAD = {self.angle_bad}^\\circ$ na pembe $BCA = {self.angle_bca}^\\circ$. Tafuta thamani ya pembe $ABD$.'

class Mat047_multi(Mat047):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sebuah lingkaran dengan pusat $O$. $P$ dan $S$ adalah titik-titik pada lingkaran. $POR$ adalah garis lurus. $QRST$ adalah garis singgung lingkaran di titik $S$. Sudut $OPS = {self.angle_ops}^\\circ$. Carilah nilai $y$.'
        self.description_chinese = f'该图显示了一个圆心为 $O$ 的圆。$P$ 和 $S$ 是圆上的点。$POR$ 是一条直线。$QRST$ 是圆在 $S$ 处的切线。角 $OPS = {self.angle_ops}^\circ$。求 $y$ 的值。'
        self.description_arabic = f'يوضح المخطط دائرة مركزها $O$. $P$ و $S$ هما نقطتان على الدائرة. $POR$ خط مستقيم. $QRST$ مماس للدائرة عند $S$. الزاوية $OPS = {self.angle_ops}^\circ$. أوجد قيمة $y$.'
        self.description_hindi = f'आरेख केंद्र $O$ वाला एक वृत्त दिखाता है। $P$ और $S$ वृत्त पर बिंदु हैं। $POR$ एक सीधी रेखा है। $QRST$ बिंदु $S$ पर वृत्त की एक स्पर्श रेखा है। कोण $OPS = {self.angle_ops}^\\circ$ है। $y$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. $P$ және $S$ - шеңбер бойындағы нүктелер. $POR$ - түзу сызық. $QRST$ - шеңберді $S$ нүктесінде жанайтын жанама. $OPS$ бұрышы = {self.angle_ops}^\\circ$. $y$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha duara, kitovu $O$. $P$ na $S$ ni nukta kwenye duara. $POR$ ni mstari mnyoofu. $QRST$ ni tanjiti kwenye duara katika $S$. Pembe $OPS = {self.angle_ops}^\\circ$. Tafuta thamani ya $y$.'

class Mat048_multi(Mat048):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sebuah lingkaran dengan pusat $O$. $A$, $B$, dan $C$ adalah tiga titik pada lingkaran. Sudut $ACO = {self.angle_aco}^\\circ$ dan sudut $BCO = {self.angle_bco}^\\circ$. Carilah nilai sudut $ABC$.'
        self.description_chinese = f'该图显示了一个圆心为 $O$ 的圆。$A$、$B$ 和 $C$ 是圆上的三个点。角 $ACO = {self.angle_aco}^\circ$，角 $BCO = {self.angle_bco}^\circ$。求角 $ABC$ 的值。'
        self.description_arabic = f'يوضح المخطط دائرة مركزها $O$. $A$ و $B$ و $C$ هي ثلاث نقاط على الدائرة. الزاوية $ACO = {self.angle_aco}^\circ$ والزاوية $BCO = {self.angle_bco}^\circ$. أوجد قيمة الزاوية $ABC$.'
        self.description_hindi = f'आरेख केंद्र $O$ वाला एक वृत्त दिखाता है। $A$, $B$ और $C$ वृत्त पर तीन बिंदु हैं। कोण $ACO = {self.angle_aco}^\\circ$ और कोण $BCO = {self.angle_bco}^\\circ$ है। कोण $ABC$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. $A$, $B$ және $C$ - шеңбер бойындағы үш нүкте. $ACO$ бұрышы = {self.angle_aco}^\\circ$ және $BCO$ бұрышы = {self.angle_bco}^\\circ$. $ABC$ бұрышының мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha duara, kitovu $O$. $A$, $B$ na $C$ ni nukta tatu kwenye duara. Pembe $ACO = {self.angle_aco}^\\circ$ na pembe $BCO = {self.angle_bco}^\\circ$. Tafuta thamani ya pembe $ABC$.'

class Mat049_multi(Mat049):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Titik-titik $A, B, C, D$, dan $E$ terletak pada sebuah lingkaran. $FG$ adalah garis singgung lingkaran di titik $C$. Menggunakan informasi yang diberikan dalam diagram, carilah nilai sudut $DCG$.'
        self.description_chinese = '点 $A, B, C, D$ 和 $E$ 位于一个圆上。$FG$ 是圆在 $C$ 处的切线。使用图中提供的信息，求角 $DCG$ 的值。'
        self.description_arabic = 'النقاط $A$ و $B$ و $C$ و $D$ و $E$ تقع على دائرة. $FG$ هو مماس للدائرة عند $C$. باستخدام المعلومات المقدمة في المخطط، أوجد قيمة الزاوية $DCG$.'
        self.description_hindi = 'बिंदु $A, B, C, D$ और $E$ एक वृत्त पर स्थित हैं। $FG$ बिंदु $C$ पर वृत्त की एक स्पर्श रेखा है। आरेख में दी गई जानकारी का उपयोग करके, कोण $DCG$ का मान ज्ञात करें।'
        self.description_kazakh = '$A, B, C, D$ және $E$ нүктелері шеңбер бойында жатыр. $FG$ - шеңберді $C$ нүктесінде жанайтын жанама. Диаграммада берілген ақпаратты пайдалана отырып, $DCG$ бұрышының мәнін табыңыз.'
        self.description_swahili = 'Nukta $A, B, C, D$ na $E$ zipo kwenye duara. $FG$ ni tanjiti kwenye duara katika $C$. Kwa kutumia taarifa iliyotolewa kwenye mchoro, tafuta thamani ya pembe $DCG$.'

class Mat050_multi(Mat050):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sebuah lingkaran dengan pusat $O$. Jari-jari dan tali busur $AB$ memiliki panjang seperti yang ditunjukkan pada gambar. Hitunglah jarak terpendek dari pusat lingkaran ke tali busur tersebut.'
        self.description_chinese = f'该图显示了一个圆心为 $O$ 的圆。半径和弦 $AB$ 的长度如图所示。计算从圆心到弦的最短距离。'
        self.description_arabic = f'يوضح المخطط دائرة مركزها $O$. أطوال نصف القطر والوتر $AB$ كما هي موضحة في الصورة. احسب أقصر مسافة من مركز الدائرة إلى الوتر.'
        self.description_hindi = f'आरेख केंद्र $O$ वाला एक वृत्त दिखाता है। त्रिज्या और जीवा (chord) $AB$ की लंबाई चित्र में दिखाए अनुसार है। वृत्त के केंद्र से जीवा तक की सबसे छोटी दूरी की गणना करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. Радиус пен $AB$ хордасының ұзындықтары суретте көрсетілгендей. Шеңбердің центрінен хордаға дейінгі ең қысқа қашықтықты есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha duara lenye kitovu $O$. Nusu kipenyo na kigwe $AB$ vina urefu kama unavyoonyeshwa kwenye picha. Kokotoa umbali mfupi zaidi kutoka kwenye kitovu cha duara hadi kwenye kigwe.'

class Mat051_multi(Mat051):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sebuah lingkaran dengan pusat $O$. Dua tali busur, $AB$ dan $CD$, masing-masing memiliki panjang ${round(self.c_len, 2)}$ cm. Tali busur $AB$ berjarak ${round(self.d, 2)}$ cm dari pusat. Jarak dari pusat ke tali busur $CD$ adalah $({self.expr.strip()})$ cm. Carilah nilai $x$.'
        self.description_chinese = f'该图显示了一个圆心为 $O$ 的圆。两条弦 $AB$ 和 $CD$ 的长度均为 ${round(self.c_len, 2)}$ cm。弦 $AB$ 距离圆心 ${round(self.d, 2)}$ cm。从圆心到弦 $CD$ 的距离为 $({self.expr.strip()})$ cm。求 $x$ 的值。'
        self.description_arabic = f'يوضح المخطط دائرة مركزها $O$. الوتران، $AB$ و $CD$، يبلغ طول كل منهما ${round(self.c_len, 2)}$ سم. يبعد الوتر $AB$ مسافة ${round(self.d, 2)}$ سم عن المركز. المسافة من المركز إلى الوتر $CD$ هي $({self.expr.strip()})$ سم. أوجد قيمة $x$.'
        self.description_hindi = f'आरेख केंद्र $O$ वाला एक वृत्त दिखाता है। दो जीवाओं, $AB$ और $CD$, प्रत्येक की लंबाई ${round(self.c_len, 2)}$ cm है। जीवा $AB$ केंद्र से ${round(self.d, 2)}$ cm की दूरी पर है। केंद्र से जीवा $CD$ की दूरी $({self.expr.strip()})$ cm है। $x$ का मान ज्ञात करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. $AB$ және $CD$ екі хордасының әрқайсысының ұзындығы ${round(self.c_len, 2)}$ см. $AB$ хордасы центрден ${round(self.d, 2)}$ см қашықтықта орналасқан. Центрден $CD$ хордасына дейінгі қашықтық $({self.expr.strip()})$ см. $x$ мәнін табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha duara lenye kitovu $O$. Vigwe viwili, $AB$ na $CD$, kila kimoja kina urefu wa ${round(self.c_len, 2)}$ cm. Kigwe $AB$ kipo ${round(self.d, 2)}$ cm kutoka kwenye kitovu. Umbali kutoka kwenye kitovu hadi kwenye kigwe $CD$ ni $({self.expr.strip()})$ cm. Tafuta thamani ya $x$.'

class Mat052_multi(Mat052):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sebuah lingkaran dengan pusat $O$. $PA$ dan $PB$ adalah garis singgung lingkaran dari titik eksternal $P$, menyentuh lingkaran di $A$ dan $B$. Jari-jari lingkaran adalah ${self.radius}$ cm dan sudut $\\angle APB = {self.angle_apb}^\\circ$. Hitunglah panjang garis singgung $PA$.'
        self.description_chinese = f'该图显示了一个圆心为 $O$ 的圆。$PA$ 和 $PB$ 是从外部点 $P$ 到圆的切线，分别在 $A$ 和 $B$ 处与圆相切。圆的半径为 ${self.radius}$ cm，角 $\angle APB = {self.angle_apb}^\circ$。计算切线 $PA$ 的长度。'
        self.description_arabic = f'يوضح المخطط دائرة مركزها $O$. $PA$ و $PB$ هما مماسان للدائرة من نقطة خارجية $P$، ويمسان الدائرة عند $A$ و $B$. نصف قطر الدائرة هو ${self.radius}$ سم والزاوية $\angle APB = {self.angle_apb}^\circ$. احسب طول المماس $PA$.'
        self.description_hindi = f'आरेख केंद्र $O$ वाला एक वृत्त दिखाता है। $PA$ और $PB$ एक बाहरी बिंदु $P$ से वृत्त की स्पर्श रेखाएँ हैं, जो वृत्त को $A$ और $B$ पर छूती हैं। वृत्त की त्रिज्या ${self.radius}$ cm है और कोण $\\angle APB = {self.angle_apb}^\\circ$ है। स्पर्श रेखा $PA$ की लंबाई की गणना करें।'
        self.description_kazakh = f'Диаграммада центрі $O$ болатын шеңбер көрсетілген. $PA$ және $PB$ - сыртқы $P$ нүктесінен шеңберді $A$ және $B$ нүктелерінде жанайтын жанамалар. Шеңбердің радиусы ${self.radius}$ см және $\\angle APB = {self.angle_apb}^\\circ$ бұрышы. $PA$ жанамасының ұзындығын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha duara lenye kitovu $O$. $PA$ na $PB$ ni tanjiti kwenye duara kutoka kwenye nukta ya nje $P$, zinazogusa duara katika $A$ na $B$. Nusu kipenyo cha duara ni ${self.radius}$ cm na pembe $\\angle APB = {self.angle_apb}^\\circ$. Kokotoa urefu wa tanjiti $PA$.'

class Mat053_multi(Mat053):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan sebuah lingkaran yang disinggungkan di dalam segitiga $ABC$, menyentuh sisi-sisinya di $P$, $Q$, dan $R$. Keliling segitiga $ABC$ adalah ${self.perimeter:.1f}$ cm. Diketahui bahwa segmen garis singgung $AR = {self.x:.1f}$ cm dan $BP = {self.y:.1f}$ cm, hitunglah panjang sisi $AC$.'
        self.description_chinese = f'该图显示了内切于三角形 $ABC$ 的一个圆，分别在 $P$、$Q$ 和 $R$ 处与边相切。三角形 $ABC$ 的周长为 ${self.perimeter:.1f}$ cm。已知切线段 $AR = {self.x:.1f}$ cm 且 $BP = {self.y:.1f}$ cm，计算边 $AC$ 的长度。'
        self.description_arabic = f'يوضح المخطط دائرة محاطة بمثلث $ABC$، وتمس الأضلاع عند $P$ و $Q$ و $R$. محيط المثلث $ABC$ هو ${self.perimeter:.1f}$ سم. علمًا بأن قطع المماس $AR = {self.x:.1f}$ سم و $BP = {self.y:.1f}$ سم، احسب طول الضلع $AC$.'
        self.description_hindi = f'आरेख त्रिभुज $ABC$ में उत्कीर्ण (inscribed) एक वृत्त दिखाता है, जो भुजाओं को $P$, $Q$, और $R$ पर छूता है। त्रिभुज $ABC$ का परिमाप ${self.perimeter:.1f}$ cm है। यह देखते हुए कि स्पर्श रेखा खंड $AR = {self.x:.1f}$ cm और $BP = {self.y:.1f}$ cm है, भुजा $AC$ की लंबाई की गणना करें।'
        self.description_kazakh = f'Диаграммада $ABC$ үшбұрышына іштей сызылған, қабырғаларды $P$, $Q$ және $R$ нүктелерінде жанайтын шеңбер көрсетілген. $ABC$ үшбұрышының периметрі ${self.perimeter:.1f}$ см. $AR = {self.x:.1f}$ см және $BP = {self.y:.1f}$ см жанама кесінділері берілген болса, $AC$ қабырғасының ұзындығын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha duara lililochorwa ndani ya pembetatu $ABC$, likigusa pande katika $P$, $Q$, na $R$. Mzingo wa pembetatu $ABC$ ni ${self.perimeter:.1f}$ cm. Kwa kuwa pingili za tanjiti ni $AR = {self.x:.1f}$ cm na $BP = {self.y:.1f}$ cm, kokotoa urefu wa upande $AC$.'

class Mat054_multi(Mat054):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total luas bangun yang ditunjukkan.'
        self.description_chinese = f'计算所示图形的总面积。'
        self.description_arabic = f'احسب المساحة الإجمالية للشكل الموضح.'
        self.description_hindi = f'दिखाए गए आकार के कुल क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Көрсетілген фигураның жалпы ауданын есептеңіз.'
        self.description_swahili = f'Kokotoa eneo la jumla la umbo lililoonyeshwa.'

class Mat055_multi(Mat055):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah luas jajar genjang tersebut.'
        self.description_chinese = f'计算平行四边形的面积。'
        self.description_arabic = f'احسب مساحة متوازي الأضلاع.'
        self.description_hindi = f'समांतर चतुर्भुज (parallelogram) के क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Параллелограммның ауданын есептеңіз.'
        self.description_swahili = f'Kokotoa eneo la msambamba.'

class Mat056_multi(Mat056):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah luas trapesium tersebut.'
        self.description_chinese = f'计算梯形的面积。'
        self.description_arabic = f'احسب مساحة شبه المنحرف.'
        self.description_hindi = f'समलंब चतुर्भुज (trapezium) के क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Трапецияның ауданын есептеңіз.'
        self.description_swahili = f'Kokotoa eneo la trapeza.'

class Mat057_multi(Mat057):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah luas jalur tersebut.'
        self.description_chinese = f'计算小径的面积。'
        self.description_arabic = f'احسب مساحة المسار.'
        self.description_hindi = f'पथ (path) के क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Жолдың ауданын есептеңіз.'
        self.description_swahili = f'Kokotoa eneo la njia.'

class Mat058_multi(Mat058):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah keliling bangun tersebut.'
        self.description_chinese = f'计算图形的周长。'
        self.description_arabic = f'احسب محيط الشكل.'
        self.description_hindi = f'आकार के परिमाप (perimeter) की गणना करें।'
        self.description_kazakh = f'Фигураның периметрін есептеңіз.'
        self.description_swahili = f'Kokotoa mzingo wa umbo.'

class Mat059_multi(Mat059):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah luas juring mayor yang diarsir. Berikan jawaban Anda dalam bentuk $\\pi$. Bulatkan hasilnya hingga dua tempat desimal.'
        self.description_chinese = f'计算阴影优扇形的面积。答案保留 $\pi$ 的形式。结果保留两位小数。'
        self.description_arabic = f'احسب مساحة القطاع الدائري الأكبر المظلل. أعط إجابتك بدلالة $\pi$. قرّب النتيجة إلى منزلتين عشريتين.'
        self.description_hindi = f'छायांकित प्रमुख त्रिज्यखंड (major sector) के क्षेत्रफल की गणना करें। अपना उत्तर $\\pi$ के पदों में दें। परिणाम को दो दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Боялған үлкен сектордың ауданын есептеңіз. Жауабыңызды $\\pi$ арқылы беріңіз. Нәтижені екі ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = f'Kokotoa eneo la sekta kuu iliyowekwa kivuli. Toa jibu lako kwa kutumia $\\pi$. Raundisha jibu hadi sehemu mbili za desimali.'

class Mat060_multi(Mat060):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah panjang busur dari juring yang diarsir. {self.pi_instruction} Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算阴影扇形的弧长。{self.pi_instruction} 答案精确到两位小数。'
        self.description_arabic = f'احسب طول قوس القطاع المظلل. {self.pi_instruction} أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'छायांकित त्रिज्यखंड के चाप (arc) की लंबाई की गणना करें। {self.pi_instruction} अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Боялған сектор доғасының ұзындығын есептеңіз. {self.pi_instruction} Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa urefu wa tao la sekta iliyowekwa kivuli. {self.pi_instruction} Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat061_multi(Mat061):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total keliling bingkai jendela tersebut. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算窗框的总周长。答案精确到两位小数。'
        self.description_arabic = f'احسب المحيط الإجمالي لإطار النافذة. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'खिड़की के फ्रेम के कुल परिमाप की गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Терезе жақтауының жалпы периметрін есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa mzingo wa jumla wa fremu ya dirisha. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat062_multi(Mat062):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah luas daerah yang diarsir. Biarkan jawaban Anda dalam bentuk $\\pi$.'
        self.description_chinese = f'计算阴影区域的面积。答案保留 $\pi$ 的形式。'
        self.description_arabic = f'احسب مساحة المنطقة المظللة. اترك إجابتك بدلالة $\pi$.'
        self.description_hindi = f'छायांकित क्षेत्र के क्षेत्रफल की गणना करें। अपना उत्तर $\\pi$ के पदों में छोड़ें।'
        self.description_kazakh = f'Боялған аймақтың ауданын есептеңіз. Жауабыңызды $\\pi$ арқылы қалдырыңыз.'
        self.description_swahili = f'Kokotoa eneo la kanda iliyowekwa kivuli. Acha jibu lako kwa kutumia $\\pi$.'

class Mat063_multi(Mat063):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah luas kaca depan yang dibersihkan oleh wiper. Berikan jawaban Anda dalam bentuk $\\pi$. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算雨刷器清洁的挡风玻璃面积。答案保留 $\pi$ 的形式。答案精确到两位小数。'
        self.description_arabic = f'احسب مساحة الزجاج الأمامي التي تنظفها الشفرة. أعط إجابتك بدلالة $\pi$. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'ब्लेड द्वारा साफ किए गए विंडशील्ड के क्षेत्रफल की गणना करें। अपना उत्तर $\\pi$ के पदों में दें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Щеткамен тазартылған әйнек ауданын есептеңіз. Жауабыңызды $\\pi$ арқылы беріңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo la kioo cha mbele kilichosafishwa na wembe. Toa jibu lako kwa kutumia $\\pi$. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat064_multi(Mat064):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total volume silo tersebut. Berikan jawaban Anda dalam bentuk $\\pi$. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算筒仓的总体积。答案保留 $\pi$ 的形式。答案精确到两位小数。'
        self.description_arabic = f'احسب الحجم الإجمالي للصومعة. أعط إجابتك بدلالة $\pi$. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'साइलो (silo) के कुल आयतन की गणना करें। अपना उत्तर $\\pi$ के पदों में दें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Сүрлемнің жалпы көлемін есептеңіз. Жауабыңызды $\\pi$ арқылы беріңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa ujazo wa jumla wa silo. Toa jibu lako kwa kutumia $\\pi$. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat065_multi(Mat065):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah kapasitas kolam tersebut dalam meter kubik. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算水池的容量（以立方米为单位）。答案精确到两位小数。'
        self.description_arabic = f'احسب سعة المسبح بالأمتار المكعبة. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'पूल की क्षमता की घन मीटर में गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Бассейннің сыйымдылығын текше метрмен есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa ujazo wa bwawa katika mita za ujazo. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat066_multi(Mat066):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total luas permukaan kerucut. Gunakan $\\pi = 3.142$. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算圆锥的总表面积。取 $\pi = 3.142$。答案精确到两位小数。'
        self.description_arabic = f'احسب المساحة السطحية الكلية للمخروط. استخدم $\pi = 3.142$. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'शंकु के कुल पृष्ठीय क्षेत्रफल की गणना करें। $\\pi = 3.142$ का उपयोग करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Конустың толық бетінің ауданын есептеңіз. $\\pi = 3.142$ мәнін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo la jumla la uso wa pia. Tumia $\\pi = 3.142$. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat067_multi(Mat067):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total luas permukaan belahan bola padat tersebut. Gunakan $\\pi = 3.14$. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算实心半球的总表面积。取 $\pi = 3.14$。答案精确到两位小数。'
        self.description_arabic = f'احسب المساحة السطحية الكلية لنصف الكرة المصمت. استخدم $\pi = 3.14$. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'ठोस अर्धगोले (hemisphere) के कुल पृष्ठीय क्षेत्रफल की गणना करें। $\\pi = 3.14$ का उपयोग करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Жарты шар тәрізді тұтас дененің толық бетінің ауданын есептеңіз. $\\pi = 3.14$ мәнін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo la jumla la uso wa nusu tufe dhabiti. Tumia $\\pi = 3.14$. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat068_multi(Mat068):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah tinggi vertikal limas tersebut lalu gunakan untuk mencari volumenya. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算角锥的垂直高度，然后据此求其体积。答案精确到两位小数。'
        self.description_arabic = f'احسب الارتفاع الرأسي للهرم ثم استخدمه لإيجاد الحجم. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'पिरामिड की ऊर्ध्वाधर ऊँचाई की गणना करें और फिर इसका उपयोग आयतन ज्ञात करने के लिए करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Пирамиданың тік биіктігін есептеңіз, содан кейін оны көлемді табу үшін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa kimo cha wima cha piramidi na kisha ukitumie kutafuta ujazo. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat069_multi(Mat069):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total keliling bangun tersebut. Gunakan $\\pi = 3.1416$. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算图形的总周长。取 $\pi = 3.1416$。答案精确到两位小数。'
        self.description_arabic = f'احسب المحيط الإجمالي للشكل. استخدم $\pi = 3.1416$. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'आकार के कुल परिमाप की गणना करें। $\\pi = 3.1416$ का उपयोग करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Фигураның жалпы периметрін есептеңіз. $\\pi = 3.1416$ мәнін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa mzingo wa jumla wa umbo. Tumia $\\pi = 3.1416$. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat070_multi(Mat070):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total luas bangun tersebut. Gunakan $\\pi = 3.1416$. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算图形的总面积。取 $\pi = 3.1416$。答案精确到两位小数。'
        self.description_arabic = f'احسب المساحة الإجمالية للشكل. استخدم $\pi = 3.1416$. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'आकार के कुल क्षेत्रफल की गणना करें। $\\pi = 3.1416$ का उपयोग करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Фигураның жалпы ауданын есептеңіз. $\\pi = 3.1416$ мәнін пайдаланыңыз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo la jumla la umbo. Tumia $\\pi = 3.1416$. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat071_multi(Mat071):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah luas daerah yang diarsir. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算阴影区域的面积。答案精确到两位小数。'
        self.description_arabic = f'احسب مساحة المنطقة المظللة. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'छायांकित क्षेत्र के क्षेत्रफल की गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Боялған аймақтың ауданын есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo la kanda iliyowekwa kivuli. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat072_multi(Mat072):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total volume tangki tersebut. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算水箱的总体积。答案精确到两位小数。'
        self.description_arabic = f'احسب الحجم الإجمالي للخزان. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'टैंक के कुल आयतन की गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Резервуардың жалпы көлемін есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa ujazo wa jumla wa tanki. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat073_multi(Mat073):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah total luas permukaan eksterior tangki (dengan asumsi alasnya datar dan tertutup). Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算水箱的总外表面积（假设底部平坦且闭合）。答案精确到两位小数。'
        self.description_arabic = f'احسب المساحة السطحية الخارجية الكلية للخزان (بافتراض أن القاعدة مسطحة ومغلقة). أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'टैंक के कुल बाहरी पृष्ठीय क्षेत्रफल की गणना करें (यह मानते हुए कि आधार सपाट और बंद है)। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Резервуардың жалпы сыртқы бетінің ауданын есептеңіз (табаны тегіс және жабық деп есептеңіз). Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa eneo la jumla la uso wa nje wa tanki (kwa kudhani kitako ni bapa na kimefungwa). Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat074_multi(Mat074):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan segitiga siku-siku $ABC$. Hitunglah $BC$.'
        self.description_chinese = f'该图显示了一个直角三角形 $ABC$。计算 $BC$。'
        self.description_arabic = f'يوضح المخطط مثلثًا قائم الزاوية $ABC$. احسب $BC$.'
        self.description_hindi = f'आरेख एक समकोण त्रिभुज $ABC$ दिखाता है। $BC$ की गणना करें।'
        self.description_kazakh = f'Диаграммада $ABC$ тікбұрышты үшбұрышы көрсетілген. $BC$ қабырғасын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha pembetatu mraba $ABC$. Kokotoa $BC$.'

class Mat075_multi(Mat075):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sebuah tangga bersandar pada dinding vertikal. Bagian bawah tangga berjarak ${self.ground_dist}$ m dari bagian bawah dinding, di atas tanah yang mendatar. Tangga tersebut mencapai ketinggian ${self.wall_height}$ m pada dinding. Hitunglah panjang tangga tersebut.'
        self.description_chinese = f'一个梯子靠在垂直的墙上。梯子的底部在水平地面上，距离墙底 ${self.ground_dist}$ 米。梯子到达墙上 ${self.wall_height}$ 米的高处。计算梯子的长度。'
        self.description_arabic = f'يستند سلم على جدار رأسي. يبعد الجزء السفلي من السلم مسافة ${self.ground_dist}$ متر عن أسفل الجدار، على أرض أفقية. يصل السلم إلى ارتفاع ${self.wall_height}$ متر على الجدار. احسب طول السلم.'
        self.description_hindi = f'एक सीढ़ी एक ऊर्ध्वाधर दीवार के सहारे टिकी है। सीढ़ी का निचला सिरा क्षैतिज जमीन पर दीवार के निचले भाग से ${self.ground_dist}$ m की दूरी पर है। सीढ़ी दीवार पर ${self.wall_height}$ m ऊपर तक पहुँचती है। सीढ़ी की लंबाई की गणना करें।'
        self.description_kazakh = f'Баспалдақ тік қабырғаға сүйеліп тұр. Баспалдақтың төменгі жағы қабырғаның түбінен көлденең жерде ${self.ground_dist}$ м қашықтықта орналасқан. Баспалдақ қабырға бойымен ${self.wall_height}$ м биіктікке жетеді. Баспалдақтың ұзындығын есептеңіз.'
        self.description_swahili = f'Ngazi imeegemezwa kwenye ukuta wa wima. Chini ya ngazi ni mita ${self.ground_dist}$ kutoka chini ya ukuta, kwenye ardhi ya ulalo. Ngazi inafika mita ${self.wall_height}$ juu ya ukuta. Kokotoa urefu wa ngazi.'

class Mat076_multi(Mat076):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan balok dengan panjang, lebar, dan tinggi seperti yang ditunjukkan pada gambar dalam cm. Hitunglah panjang diagonal ruang dari sudut $A$ ke sudut $G$.'
        self.description_chinese = f'该图显示了一个长方体，其长、宽、高如图所示（单位：cm）。计算从角 $A$ 到角 $G$ 的内部对角线长度。'
        self.description_arabic = f'يوضح المخطط متوازي مستطيلات مع الطول والعرض والارتفاع بالسنتيمتر كما هو موضح في الشكل. احسب طول القطر الداخلي من الزاوية $A$ إلى الزاوية $G$.'
        self.description_hindi = f'आरेख एक घनाभ (cuboid) दिखाता है जिसकी लंबाई, चौड़ाई, ऊँचाई चित्र में cm में दिखाई गई है। कोने $A$ से कोने $G$ तक आंतरिक विकर्ण की लंबाई की गणना करें।'
        self.description_kazakh = f'Диаграммада ұзындығы, ені, биіктігі суретте көрсетілгендей см болатын тікбұрышты параллелепипед көрсетілген. $A$ бұрышынан $G$ бұрышына дейінгі ішкі диагональдің ұзындығын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha mchestatili ukiwa na urefu, upana, na kimo katika cm kama inavyoonyeshwa kwenye kielelezo. Kokotoa urefu wa ulalo wa ndani kutoka kona $A$ hadi kona $G$.'

class Mat077_multi(Mat077):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan sebuah segitiga siku-siku. Hitunglah nilai $x$.'
        self.description_chinese = '该图显示了一个直角三角形。计算 $x$ 的值。'
        self.description_arabic = 'يوضح المخطط مثلثًا قائم الزاوية. احسب قيمة $x$.'
        self.description_hindi = 'आरेख एक समकोण त्रिभुज दिखाता है। $x$ के मान की गणना करें।'
        self.description_kazakh = 'Диаграммада тікбұрышты үшбұрыш көрсетілген. $x$ мәнін есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha pembetatu mraba. Kokotoa thamani ya $x$.'

class Mat078_multi(Mat078):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Seseorang dengan tinggi {self.person_height} m berdiri di atas tanah datar, {self.distance} m dari dasar sebuah menara vertikal. Sudut elevasi dari mata orang tersebut ke puncak menara adalah {self.angle_elevation}^\\circ. Hitunglah total tinggi menara tersebut."
        self.description_chinese = f"一个身高为 {self.person_height} 米的人站在水平地面上，距离垂直塔的底部 {self.distance} 米。从这个人的眼睛到塔顶的仰角为 {self.angle_elevation}^\circ。计算塔的总高度。"
        self.description_arabic = f"يقف شخص ارتفاعه {self.person_height} متر على أرض أفقية، على بعد {self.distance} متر من قاعدة برج رأسي. زاوية الارتفاع من عيني الشخص إلى قمة البرج هي {self.angle_elevation}^\circ. احسب الارتفاع الإجمالي للبرج."
        self.description_hindi = f"{self.person_height} m ऊँचाई वाला एक व्यक्ति क्षैतिज जमीन पर, एक ऊर्ध्वाधर टॉवर के आधार से {self.distance} m की दूरी पर खड़ा है। व्यक्ति की आँखों से टॉवर के शीर्ष का उन्नयन कोण (angle of elevation) {self.angle_elevation}^\\circ है। टॉवर की कुल ऊँचाई की गणना करें।"
        self.description_kazakh = f"Бойының ұзындығы {self.person_height} м болатын адам көлденең жерде, тік мұнараның табанынан {self.distance} м қашықтықта тұр. Адамның көзінен мұнараның төбесіне дейінгі көтерілу бұрышы {self.angle_elevation}^\\circ. Мұнараның жалпы биіктігін есептеңіз."
        self.description_swahili = f"Mtu mwenye kimo cha mita {self.person_height} amesimama kwenye ardhi ya ulalo, mita {self.distance} kutoka kwenye kitako cha mnara wa wima. Pembe ya mwinuko kutoka kwenye macho ya mtu huyo hadi kwenye kilele cha mnara ni {self.angle_elevation}^\\circ. Kokotoa kimo cha jumla cha mnara."

class Mat079_multi(Mat079):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Pada segitiga $ABC$, $AC = {self.side_ac}$ cm dan $BC = {self.side_bc}$ cm. Sudut $BAC = {self.angle_a}^\\circ$. Sebuah garis tegak lurus ditarik dari $C$ untuk memotong $AB$ di $D$. Hitunglah panjang $AB$.'
        self.description_chinese = f'在三角形 $ABC$ 中，$AC = {self.side_ac}$ cm 且 $BC = {self.side_bc}$ cm。角 $BAC = {self.angle_a}^\circ$。从 $C$ 作一条垂线，交 $AB$ 于 $D$。计算 $AB$ 的长度。'
        self.description_arabic = f'في المثلث $ABC$، $AC = {self.side_ac}$ سم و $BC = {self.side_bc}$ سم. الزاوية $BAC = {self.angle_a}^\circ$. يتم إسقاط عمود من $C$ ليلتقي مع $AB$ عند $D$. احسب طول $AB$.'
        self.description_hindi = f'त्रिभुज $ABC$ में, $AC = {self.side_ac}$ cm और $BC = {self.side_bc}$ cm है। कोण $BAC = {self.angle_a}^\\circ$ है। $C$ से एक लंब डाला जाता है जो $AB$ को $D$ पर मिलता है। $AB$ की लंबाई की गणना करें।'
        self.description_kazakh = f'$ABC$ үшбұрышында $AC = {self.side_ac}$ см және $BC = {self.side_bc}$ см. $BAC$ бұрышы = {self.angle_a}^\\circ$. $C$ төбесінен $AB$ қабырғасын $D$ нүктесінде қиятындай перпендикуляр түсірілген. $AB$ ұзындығын есептеңіз.'
        self.description_swahili = f'Katika pembetatu $ABC$, $AC = {self.side_ac}$ cm na $BC = {self.side_bc}$ cm. Pembe $BAC = {self.angle_a}^\\circ$. Mstari wa wima unashushwa kutoka $C$ ili kukutana na $AB$ katika $D$. Kokotoa urefu wa $AB$.'

class Mat080_multi(Mat080):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan grafik fungsi trigonometri dalam bentuk $y = a {self.func_name}(bx + c) + d$. Carilah nilai dari $a$, $b$, $c$, dan $d$. (Berikan jawaban Anda dalam format: a, b, c, d. Contoh: 1, 2, 3, 4)'
        self.description_chinese = f'该图显示了形式为 $y = a {self.func_name}(bx + c) + d$ 的三角函数图像。求 $a$、$b$、$c$ 和 $d$ 的值。（请以 a, b, c, d 的格式提供答案。例如：1, 2, 3, 4）'
        self.description_arabic = f'يوضح المخطط الرسم البياني لدالة مثلثية على الصورة $y = a {self.func_name}(bx + c) + d$. أوجد قيم $a$ و $b$ و $c$ و $d$. (قدم إجابتك بالتنسيق: a, b, c, d. مثال: 1, 2, 3, 4)'
        self.description_hindi = f'आरेख $y = a {self.func_name}(bx + c) + d$ के रूप के एक त्रिकोणमितीय फलन (trigonometric function) का ग्राफ दिखाता है। $a$, $b$, $c$, और $d$ के मान ज्ञात करें। (अपना उत्तर इस प्रारूप में दें: a, b, c, d. उदाहरण: 1, 2, 3, 4)'
        self.description_kazakh = f'Диаграммада $y = a {self.func_name}(bx + c) + d$ түріндегі тригонометриялық функцияның графигі көрсетілген. $a$, $b$, $c$ және $d$ мәндерін табыңыз. (Жауабыңызды келесі форматта беріңіз: a, b, c, d. Мысалы: 1, 2, 3, 4)'
        self.description_swahili = f'Mchoro unaonyesha grafu ya utendakazi wa trigonometria wa mfumo $y = a {self.func_name}(bx + c) + d$. Tafuta thamani za $a$, $b$, $c$, na $d$. (Toa jibu lako katika mpangilio: a, b, c, d. Mfano: 1, 2, 3, 4)'

class Mat081_multi(Mat081):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut menunjukkan grafik $y = f(x)$ di mana $f(x) = {self.func_display}$. Dengan menggunakan informasi visual yang diberikan, temukan semua solusi untuk ${self.implicit_eq}$ dalam rentang $0^\\circ \\leqslant x \\leqslant 360^\\circ$.'
        self.description_chinese = f'该图显示了 $y = f(x)$ 的图像，其中 $f(x) = {self.func_display}$。使用提供的视觉信息，求出 ${self.implicit_eq}$ 在 $0^\circ \leqslant x \leqslant 360^\circ$ 范围内的所有解。'
        self.description_arabic = f'يوضح المخطط الرسم البياني لـ $y = f(x)$ حيث $f(x) = {self.func_display}$. باستخدام المعلومات المرئية المقدمة، أوجد جميع حلول ${self.implicit_eq}$ في النطاق $0^\circ \leqslant x \leqslant 360^\circ$.'
        self.description_hindi = f'आरेख $y = f(x)$ का ग्राफ दिखाता है जहाँ $f(x) = {self.func_display}$ है। दी गई दृश्य जानकारी का उपयोग करते हुए, $0^\\circ \\leqslant x \\leqslant 360^\\circ$ की सीमा में ${self.implicit_eq}$ के लिए सभी हल ज्ञात करें।'
        self.description_kazakh = f'Диаграммада $f(x) = {self.func_display}$ болатын $y = f(x)$ графигі көрсетілген. Берілген визуалды ақпаратты пайдалана отырып, $0^\\circ \\leqslant x \\leqslant 360^\\circ$ аралығындағы ${self.implicit_eq}$ үшін барлық шешімдерді табыңыз.'
        self.description_swahili = f'Mchoro unaonyesha grafu ya $y = f(x)$ ambapo $f(x) = {self.func_display}$. Kwa kutumia taarifa ya kuona iliyotolewa, tafuta suluhu zote kwa ${self.implicit_eq}$ katika masafa ya $0^\\circ \\leqslant x \\leqslant 360^\\circ$.'

class Mat082_multi(Mat082):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Berdasarkan gambar tersebut, hitunglah nilai dari $\\sin x$.'
        self.description_chinese = f'根据图像，计算 $\sin x$ 的值。'
        self.description_arabic = f'بناءً على الصورة، احسب قيمة $\sin x$.'
        self.description_hindi = f'छवि के आधार पर, $\\sin x$ के मान की गणना करें।'
        self.description_kazakh = f'Суретке сүйене отырып, $\\sin x$ мәнін есептеңіз.'
        self.description_swahili = f'Kulingana na picha, kokotoa thamani ya $\\sin x$.'

class Mat083_multi(Mat083):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan posisi tiga titik $A$, $B$, dan $C$. Berdasarkan informasi pada gambar, hitunglah jarak $AB$.'
        self.description_chinese = '该图显示了三个点 $A$、$B$ 和 $C$ 的位置。根据图中的信息，计算距离 $AB$。'
        self.description_arabic = 'يوضح المخطط مواقع ثلاث نقاط $A$ و $B$ و $C$. بناءً على المعلومات الواردة في الشكل، احسب المسافة $AB$.'
        self.description_hindi = 'आरेख तीन बिंदुओं $A$, $B$ और $C$ की स्थिति दिखाता है। चित्र में दी गई जानकारी के आधार पर, दूरी $AB$ की गणना करें।'
        self.description_kazakh = 'Диаграммада $A$, $B$ және $C$ үш нүктесінің орындары көрсетілген. Суреттегі ақпаратқа сүйене отырып, $AB$ қашықтығын есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha nafasi za nukta tatu $A$, $B$ na $C$. Kulingana na taarifa kwenye kielelezo, kokotoa umbali $AB$.'

class Mat084_multi(Mat084):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan segi empat $ABCD$. Hitunglah luas segi empat $ABCD$ berdasarkan informasi yang diberikan pada gambar.'
        self.description_chinese = '该图显示了一个四边形 $ABCD$。根据图中提供的信息计算四边形 $ABCD$ 的面积。'
        self.description_arabic = 'يوضح المخطط شكلًا رباعيًا $ABCD$. احسب مساحة الرباعي $ABCD$ بناءً على المعلومات المقدمة في الشكل.'
        self.description_hindi = 'आरेख एक चतुर्भुज $ABCD$ दिखाता है। चित्र में दी गई जानकारी के आधार पर चतुर्भुज $ABCD$ के क्षेत्रफल की गणना करें।'
        self.description_kazakh = 'Диаграммада $ABCD$ төртбұрышы көрсетілген. Суретте берілген ақпаратқа сүйене отырып, $ABCD$ төртбұрышының ауданын есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha pembenne $ABCD$. Kokotoa eneo la pembenne $ABCD$ kulingana na taarifa iliyotolewa kwenye kielelezo.'

class Mat085_multi(Mat085):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Berdasarkan gambar tersebut, hitunglah sudut tumpul $BDC$.'
        self.description_chinese = '根据该图，计算钝角 $BDC$。'
        self.description_arabic = 'بناءً على الشكل، احسب الزاوية المنفرجة $BDC$.'
        self.description_hindi = 'चित्र के आधार पर, अधिक कोण (obtuse angle) $BDC$ की गणना करें।'
        self.description_kazakh = 'Суретке сүйене отырып, $BDC$ доғал бұрышын есептеңіз.'
        self.description_swahili = 'Kulingana na kielelezo, kokotoa pembe butu $BDC$.'

class Mat086_multi(Mat086):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan sebuah balok. Hitunglah sudut antara $AB$ dan alas horizontal balok tersebut.'
        self.description_chinese = '该图显示了一个长方体。计算 $AB$ 与长方体水平底面之间的夹角。'
        self.description_arabic = 'يوضح المخطط متوازي مستطيلات. احسب الزاوية بين $AB$ والقاعدة الأفقية لمتوازي المستطيلات.'
        self.description_hindi = 'आरेख एक घनाभ दिखाता है। $AB$ और घनाभ के क्षैतिज आधार के बीच के कोण की गणना करें।'
        self.description_kazakh = 'Диаграммада тікбұрышты параллелепипед көрсетілген. $AB$ мен параллелепипедтің көлденең табаны арасындағы бұрышты есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha mchestatili. Kokotoa pembe kati ya $AB$ na kitako cha ulalo cha mchestatili.'

class Mat087_multi(Mat087):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan limas $OABCD$ dengan alas persegi $ABCD$. Titik puncak $O$ berada vertikal di atas pusat alas, $M$. Hitunglah sudut yang dibentuk $OA$ dengan alasnya.'
        self.description_chinese = '该图显示了一个底面为正方形 $ABCD$ 的角锥 $OABCD$。顶点 $O$ 垂直位于底面中心 $M$ 的正上方。计算 $OA$ 与底面所成的角。'
        self.description_arabic = 'يوضح المخطط هرمًا $OABCD$ بقاعدة مربعة $ABCD$. الرأس $O$ يقع رأسيًا فوق مركز القاعدة، $M$. احسب الزاوية التي يصنعها $OA$ مع القاعدة.'
        self.description_hindi = 'आरेख एक वर्गाकार आधार $ABCD$ वाला एक पिरामिड $OABCD$ दिखाता है। शीर्ष $O$ आधार के केंद्र, $M$ के ठीक ऊपर (vertically above) है। $OA$ आधार के साथ जो कोण बनाता है उसकी गणना करें।'
        self.description_kazakh = 'Диаграммада табаны $ABCD$ квадраты болатын $OABCD$ пирамидасы көрсетілген. $O$ төбесі табанның центрі $M$-нің дәл үстінде тік орналасқан. $OA$ қабырғасының табанмен жасайтын бұрышын есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha piramidi $OABCD$ yenye kitako cha mraba $ABCD$. Kilele $O$ kiko wima juu ya kitovu cha kitako, $M$. Kokotoa pembe ambayo $OA$ inatengeneza na kitako.'

class Mat088_multi(Mat088):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan bangun ruang yang terbuat dari belahan bola dan kerucut, keduanya memiliki jari-jari yang sama. Berdasarkan ukuran yang ditunjukkan pada gambar, hitunglah total volume bangun ruang tersebut.'
        self.description_chinese = '该图显示了一个由同半径的半球和圆锥组成的立体。根据图中显示的测量值，计算该立体的总体积。'
        self.description_arabic = 'يوضح المخطط مجسمًا مصنوعًا من نصف كرة ومخروط، كلاهما بنفس نصف القطر. بناءً على القياسات الموضحة في الشكل، احسب الحجم الإجمالي للمجسم.'
        self.description_hindi = 'आरेख एक अर्धगोले और एक शंकु से बना एक ठोस दिखाता है, दोनों की त्रिज्या समान है। चित्र में दिखाए गए मापों के आधार पर, ठोस के कुल आयतन की गणना करें।'
        self.description_kazakh = 'Диаграммада радиустары бірдей жарты шар мен конустан жасалған дене көрсетілген. Суретте көрсетілген өлшемдерге сүйене отырып, дененің жалпы көлемін есептеңіз.'
        self.description_swahili = 'Mchoro unaonyesha umbo dhabiti lililoundwa na nusu tufe na pia, zote zikiwa na nusu kipenyo sawa. Kulingana na vipimo vilivyoonyeshwa kwenye kielelezo, kokotoa ujazo wa jumla wa umbo hilo dhabiti.'

class Mat089_multi(Mat089):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Berapakah faktor skala dari perbesaran tersebut?'
        self.description_chinese = f'放大的比例因子是多少？'
        self.description_arabic = f'ما هو معامل التكبير؟'
        self.description_hindi = f'विस्तार (enlargement) का स्केल फैक्टर (scale factor) क्या है?'
        self.description_kazakh = f'Үлкейтудің масштабтық коэффициенті қандай?'
        self.description_swahili = f'Je, kizio cha mizani (scale factor) cha ukuzaji ni kipi?'

class Mat090_multi(Mat090):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Berapakah luas bangun Q dalam $cm^2$? Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'图形 Q 的面积是多少 $cm^2$？答案精确到两位小数。'
        self.description_arabic = f'ما هي مساحة الشكل Q بـ $cm^2$؟، أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'आकार Q का क्षेत्रफल $cm^2$ में क्या है? अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Q фигурасының ауданы неше $cm^2$? Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Je, eneo la umbo Q katika $cm^2$ ni nini?, Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat091_multi(Mat091):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Berapakah koordinat-$y$ yang baru dari titik $A'$?"
        self.description_chinese = f"点 $A'$ 的新 $y$ 坐标是多少？"
        self.description_arabic = f"ما هو إحداثي $y$ الجديد للنقطة $A'$؟"
        self.description_hindi = f"बिंदु $A'$ का नया $y$-निर्देशांक क्या है?"
        self.description_kazakh = f"$A'$ нүктесінің жаңа $y$-координатасы қандай?"
        self.description_swahili = f"Je, koordinate mpya ya $y$ ya nukta $A'$ ni nini?"

class Mat092_multi(Mat092):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Salah satu titik sudut segitiga aslinya disorot. Setelah ditranslasikan, berapakah jumlah koordinat $x$ dan $y$ dari titik sudut yang baru tersebut?'
        self.description_chinese = f'原三角形的其中一个顶点被高亮显示。平移后，新顶点的 $x$ 坐标和 $y$ 坐标之和是多少？'
        self.description_arabic = f'أحد رؤوس المثلث الأصلي مظلل. بعد إجراء انسحاب له، ما هو مجموع إحداثيات $x$ و $y$ للرأس الجديد؟'
        self.description_hindi = f'मूल त्रिभुज के शीर्षों (vertices) में से एक को हाइलाइट किया गया है। इसका स्थानांतरण (translate) होने के बाद, नए शीर्ष के $x$ और $y$ निर्देशांकों का योग क्या है?'
        self.description_kazakh = f'Бастапқы үшбұрыштың төбелерінің бірі ерекшеленген. Оны параллель көшіргеннен кейін жаңа төбенің $x$ және $y$ координаталарының қосындысы қандай болады?'
        self.description_swahili = f'Mojawapo ya vilele vya pembetatu asili vimeangaziwa. Baada ya kuhamishwa, ni nini jumla ya koordinate za $x$ na $y$ za kilele kipya?'

class Mat093_multi(Mat093):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Berapakah koordinat-{self.ask_for} dari bayangan titik A setelah direfleksikan terhadap {self.line['desc']}?"
        self.description_chinese = f"点 A 经过 {self.line['desc']} 的反射后，其图像的 {self.ask_for} 坐标是多少？"
        self.description_arabic = f"ما هو الإحداثي {self.ask_for} لصورة النقطة A بعد الانعكاس حول {self.line['desc']}؟"
        self.description_hindi = f"{self.line['desc']} में प्रतिबिंब (reflection) के बाद बिंदु A की छवि का {self.ask_for}-निर्देशांक क्या है?"
        self.description_kazakh = f"{self.line['desc']} түзуіне қатысты шағылысқаннан (симметриядан) кейінгі A нүктесі бейнесінің {self.ask_for}-координатасы қандай?"
        self.description_swahili = f"Je, ni nini koordinate ya {self.ask_for} ya taswira ya nukta A baada ya mtawanyo kwenye {self.line['desc']}?"

class Mat094_multi(Mat094):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Berapakah nilai komponen-x dari vektor resultan $\\mathbf{{r}}$?'
        self.description_chinese = f'合向量 $\mathbf{{r}}$ 的 x 分量的值是多少？'
        self.description_arabic = f'ما هي قيمة المركبة x للمتجه المحصل $\mathbf{{r}}$؟'
        self.description_hindi = f'परिणामी सदिश (resultant vector) $\\mathbf{{r}}$ के x-घटक (x-component) का मान क्या है?'
        self.description_kazakh = f'Қорытқы $\\mathbf{{r}}$ векторының x-құраушысының мәні қандай?'
        self.description_swahili = f'Je, ni nini thamani ya kipengele cha x cha vekta tokeo $\\mathbf{{r}}$?'

class Mat095_multi(Mat095):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Pada diagram, vektor $\\mathbf{p}$ dan $\\mathbf{q}$ ditunjukkan pada suatu kisi. Jika $\\mathbf{p}$ dan $\\mathbf{q}$ sejajar, carilah nilai $k$.'
        self.description_chinese = '在图中，向量 $\mathbf{p}$ 和 $\mathbf{q}$ 显示在网格上。如果 $\mathbf{p}$ 和 $\mathbf{q}$ 平行，求 $k$ 的值。'
        self.description_arabic = 'في المخطط، المتجهان $\mathbf{p}$ و $\mathbf{q}$ معروضان على شبكة. إذا كان $\mathbf{p}$ و $\mathbf{q}$ متوازيين، فأوجد قيمة $k$.'
        self.description_hindi = 'आरेख में, सदिश $\\mathbf{p}$ और $\\mathbf{q}$ एक ग्रिड पर दिखाए गए हैं। यदि $\\mathbf{p}$ और $\\mathbf{q}$ समानांतर हैं, तो $k$ का मान ज्ञात करें।'
        self.description_kazakh = 'Диаграммада торда $\\mathbf{p}$ және $\\mathbf{q}$ векторлары көрсетілген. Егер $\\mathbf{p}$ және $\\mathbf{q}$ параллель болса, $k$ мәнін табыңыз.'
        self.description_swahili = 'Katika mchoro, vekta $\\mathbf{p}$ na $\\mathbf{q}$ zinaonyeshwa kwenye gridi. Ikiwa $\\mathbf{p}$ na $\\mathbf{q}$ ni sambamba, tafuta thamani ya $k$.'

class Mat096_multi(Mat096):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah magnitudo (panjang) vektor tersebut. Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = f'计算向量的大小（长度）。答案精确到两位小数。'
        self.description_arabic = f'احسب مقدار (طول) المتجه. أعط إجابتك مقربة إلى منزلتين عشريتين.'
        self.description_hindi = f'सदिश के परिमाण (लंबाई) की गणना करें। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Вектордың модулін (ұзындығын) есептеңіз. Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa ukubwa (urefu) wa vekta. Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat097_multi(Mat097):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Dengan menggunakan vektor, carilah nilai skalar $k$ sedemikian rupa sehingga titik $A$, $B$, dan $C$ kolinear.'
        self.description_chinese = f'使用向量求标量 $k$ 的值，使得点 $A$、$B$ 和 $C$ 共线。'
        self.description_arabic = f'باستخدام المتجهات، أوجد قيمة الكمية القياسية $k$ بحيث تقع النقاط $A$ و $B$ و $C$ على استقامة واحدة.'
        self.description_hindi = f'सदिशों का उपयोग करते हुए, अदिश (scalar) $k$ का मान इस प्रकार ज्ञात करें कि बिंदु $A$, $B$ और $C$ संरेखीय (collinear) हों।'
        self.description_kazakh = f'Векторларды пайдалана отырып, $A$, $B$ және $C$ нүктелері коллинеар болатындай $k$ скалярының мәнін табыңыз.'
        self.description_swahili = f'Kwa kutumia vekta, tafuta thamani ya skana $k$ ili nukta $A$, $B$, na $C$ ziwe kwenye mstari mmoja.'

class Mat098_multi(Mat098):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Pada diagram, $OABC$ adalah sebuah trapesium di mana $OA$ sejajar dengan $CB$. Titik $P$ terletak pada segmen garis $AB$. Carilah nilai $k$ jika diketahui bahwa $\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = f'在图中，$OABC$ 是一个梯形，其中 $OA$ 平行于 $CB$。点 $P$ 位于线段 $AB$ 上。已知 $\vec{{OP}} = k({self.term_a}\mathbf{{a}} + {self.term_b}\mathbf{{b}})$，求 $k$ 的值。答案精确到三位小数。'
        self.description_arabic = f'في المخطط، $OABC$ هو شبه منحرف حيث $OA$ يوازي $CB$. تقع النقطة $P$ على القطعة المستقيمة $AB$. أوجد قيمة $k$ علمًا بأن $\vec{{OP}} = k({self.term_a}\mathbf{{a}} + {self.term_b}\mathbf{{b}})$. أعط إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'आरेख में, $OABC$ एक समलंब चतुर्भुज (trapezium) है जहाँ $OA$, $CB$ के समानांतर है। बिंदु $P$ रेखाखंड $AB$ पर स्थित है। यह देखते हुए कि $\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$ है, $k$ का मान ज्ञात करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Диаграммада $OA$ қабырғасы $CB$-ға параллель болатын $OABC$ трапециясы көрсетілген. $P$ нүктесі $AB$ кесіндісінде жатыр. $\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$ екені белгілі болса, $k$ мәнін табыңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Katika mchoro, $OABC$ ni trapeza ambapo $OA$ inasambamba na $CB$. Nukta $P$ ipo kwenye pingili ya mstari $AB$. Tafuta thamani ya $k$ ikiwa $\\vec{{OP}} = k({self.term_a}\\mathbf{{a}} + {self.term_b}\\mathbf{{b}})$. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat099_multi(Mat099):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gunakan informasi pada diagram vektor untuk mencari nilai skalar positif $k$.'
        self.description_chinese = '利用向量图中的信息求正标量 $k$ 的值。'
        self.description_arabic = 'استخدم المعلومات الموجودة في المخطط المتجهي لإيجاد قيمة الكمية القياسية الموجبة $k$.'
        self.description_hindi = 'धनात्मक अदिश $k$ का मान ज्ञात करने के लिए सदिश आरेख (vector diagram) में दी गई जानकारी का उपयोग करें।'
        self.description_kazakh = 'Оң $k$ скалярының мәнін табу үшін векторлық диаграммадағы ақпаратты пайдаланыңыз.'
        self.description_swahili = 'Tumia taarifa katika mchoro wa vekta kutafuta thamani ya skana chanya $k$.'

class Mat100_multi(Mat100):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Pada segitiga $OAB$, vektor $\\vec{{OA}} = \\mathbf{{a}}$ dan vektor $\\vec{{OB}} = \\mathbf{{b}}$. Diketahui bahwa $\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$, carilah nilai $k$. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = f'在三角形 $OAB$ 中，向量 $\vec{{OA}} = \mathbf{{a}}$ 且向量 $\vec{{OB}} = \mathbf{{b}}$。已知 $\vec{{OP}} = k({self.n}\mathbf{{a}} + {self.m}\mathbf{{b}})$，求 $k$ 的值。答案精确到三位小数。'
        self.description_arabic = f'في المثلث $OAB$، المتجه $\vec{{OA}} = \mathbf{{a}}$ والمتجه $\vec{{OB}} = \mathbf{{b}}$. علمًا بأن $\vec{{OP}} = k({self.n}\mathbf{{a}} + {self.m}\mathbf{{b}})$، أوجد قيمة $k$. أعط إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = f'त्रिभुज $OAB$ में, सदिश $\\vec{{OA}} = \\mathbf{{a}}$ और सदिश $\\vec{{OB}} = \\mathbf{{b}}$ है। यह देखते हुए कि $\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$ है, $k$ का मान ज्ञात करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'$OAB$ үшбұрышында $\\vec{{OA}} = \\mathbf{{a}}$ векторы және $\\vec{{OB}} = \\mathbf{{b}}$ векторы. $\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$ екені белгілі болса, $k$ мәнін табыңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Katika pembetatu $OAB$, vekta $\\vec{{OA}} = \\mathbf{{a}}$ na vekta $\\vec{{OB}} = \\mathbf{{b}}$. Kwa kuwa $\\vec{{OP}} = k({self.n}\\mathbf{{a}} + {self.m}\\mathbf{{b}})$, tafuta thamani ya $k$. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat101_multi(Mat101):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Berdasarkan hasil pada gambar, berapakah frekuensi relatif jarum pemutar berhenti pada warna {self.target_color}? Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = f'根据图中的结果，转盘停在颜色 {self.target_color} 上的相对频率是多少？答案保留3位小数。'
        self.description_arabic = f'بناءً على النتائج في الشكل، ما هو التكرار النسبي لوقوف القرص الدوار على اللون {self.target_color}؟ قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = f'चित्र में दिए गए परिणामों के आधार पर, यह सापेक्ष आवृत्ति (relative frequency) क्या है कि स्पिनर रंग {self.target_color} पर रुकता है? अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Суреттегі нәтижелерге сүйене отырып, айналдырғыштың {self.target_color} түсіне тоқтауының салыстырмалы жиілігі қандай? Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kulingana na matokeo katika kielelezo, ni nini marudio linganifu ya gurudumu kusimama kwenye rangi {self.target_color}? Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat102_multi(Mat102):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Menggunakan frekuensi relatif dari diagram, hitunglah frekuensi harapan dari pelemparan dadu {self.target_face} jika dadu dilempar sebanyak {self.total_rolls_scenario} kali.'
        self.description_chinese = f'使用图表中的相对频率，计算如果掷骰子 {self.total_rolls_scenario} 次，掷出 {self.target_face} 的期望频率。'
        self.description_arabic = f'باستخدام التكرار النسبي من المخطط، احسب التكرار المتوقع لدحرجة {self.target_face} إذا تم دحرجة حجر النرد {self.total_rolls_scenario} مرة.'
        self.description_hindi = f'चार्ट से सापेक्ष आवृत्ति का उपयोग करते हुए, यदि पासा {self.total_rolls_scenario} बार फेंका जाता है, तो {self.target_face} आने की अपेक्षित आवृत्ति (expected frequency) की गणना करें।'
        self.description_kazakh = f'Диаграммадағы салыстырмалы жиілікті пайдалана отырып, егер сүйек {self.total_rolls_scenario} рет лақтырылса, {self.target_face} түсуінің күтілетін жиілігін есептеңіз.'
        self.description_swahili = f'Kwa kutumia marudio linganifu kutoka kwenye chati, kokotoa marudio yanayotarajiwa ya kurusha {self.target_face} ikiwa kete itarushwa mara {self.total_rolls_scenario}.'

class Mat103_multi(Mat103):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Seorang penjaga hutan menangkap {self.M} ekor ikan dari danau, menandai mereka dengan tanda pengenal, lalu melepaskannya. Kemudian, penjaga hutan tersebut menangkap sampel baru (ditunjukkan pada gambar di atas). Menggunakan frekuensi relatif ikan yang ditandai pada tangkapan kedua, perkirakan total harapan jumlah ikan di danau tersebut.'
        self.description_chinese = f'一名护林员从湖中捕获了 {self.M} 条鱼，给它们打上标记后放生。之后，护林员捕获了一个新样本（如上图所示）。使用第二次捕获中标记鱼的相对频率，估算湖中预期的鱼的总数。'
        self.description_arabic = f'يصطاد حارس {self.M} سمكة من البحيرة، ويضع عليها علامة، ثم يطلقها. لاحقًا، يصطاد الحارس عينة جديدة (موضحة في الشكل أعلاه). باستخدام التكرار النسبي للأسماك ذات العلامات في الصيد الثاني، قدّر العدد الإجمالي المتوقع للأسماك في البحيرة.'
        self.description_hindi = f'एक रेंजर झील से {self.M} मछलियाँ पकड़ता है, उन पर एक टैग लगाता है, और उन्हें छोड़ देता है। बाद में, रेंजर एक नया नमूना (ऊपर चित्र में दिखाया गया है) पकड़ता है। दूसरी बार पकड़ी गई मछलियों में टैग लगी मछलियों की सापेक्ष आवृत्ति का उपयोग करके, झील में मछलियों की कुल अपेक्षित संख्या का अनुमान लगाएँ।'
        self.description_kazakh = f'Қорықшы көлден {self.M} балық аулап, оларды белгілейді де, қайтадан босатады. Кейінірек қорықшы жаңа таңдама аулайды (жоғарыдағы суретте көрсетілген). Екінші ауланған балықтардың ішіндегі белгіленген балықтардың салыстырмалы жиілігін пайдалана отырып, көлдегі балықтардың жалпы күтілетін санын бағалаңыз.'
        self.description_swahili = f'Mlinzi anavua samaki {self.M} kutoka ziwani, anawaweka alama kwa kutumia kitambulisho, na kuwaachia. Baadaye, mlinzi anavua sampuli mpya (iliyoonyeshwa kwenye kielelezo hapo juu). Kwa kutumia marudio linganifu ya samaki waliowekwa alama katika uvuvi wa pili, kadiria idadi ya jumla ya samaki wanaotarajiwa ziwani.'

class Mat104_multi(Mat104):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Menggunakan data pada gambar, tentukan jumlah siswa Kelas 10 yang bergabung dengan Klub Seni (diwakili oleh $x$).'
        self.description_chinese = '使用图中的数据，确定加入艺术俱乐部（用 $x$ 表示）的10年级学生人数。'
        self.description_arabic = 'باستخدام البيانات الواردة في الشكل، حدد عدد الطلاب في الصف العاشر الذين انضموا إلى نادي الفنون (ممثلاً بـ $x$).'
        self.description_hindi = 'चित्र में दिए गए डेटा का उपयोग करके, कक्षा 10 के उन छात्रों की संख्या निर्धारित करें जो आर्ट क्लब में शामिल हुए (जिन्हें $x$ द्वारा दर्शाया गया है)।'
        self.description_kazakh = 'Суреттегі деректерді пайдалана отырып, 10-сыныптағы Өнер үйірмесіне қатысатын оқушылар санын анықтаңыз ($x$ арқылы белгіленген).'
        self.description_swahili = 'Kwa kutumia data katika kielelezo, amua idadi ya wanafunzi katika Gredi ya 10 waliojiunga na Klabu ya Sanaa (inayowakilishwa na $x$).'

class Mat105_multi(Mat105):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Grafik garis di atas merepresentasikan suhu yang dicatat setiap dua jam di sebuah kota selama periode 8 jam. Hitunglah total penurunan suhu, dalam derajat Celcius, antara titik terpanas yang tercatat dan suhu pada pukul 16:00.'
        self.description_chinese = '上方的折线图表示某城市在8小时内每两小时记录一次的温度。计算记录的最高温度与16:00的温度之间的总降温（以摄氏度为单位）。'
        self.description_arabic = 'يمثل الرسم البياني الخطي أعلاه درجة الحرارة المسجلة كل ساعتين في مدينة على مدار فترة 8 ساعات. احسب إجمالي الانخفاض في درجة الحرارة، بالدرجات المئوية، بين أعلى نقطة مسجلة ودرجة الحرارة عند الساعة 16:00.'
        self.description_hindi = 'ऊपर दिया गया रेखा ग्राफ़ (line graph) 8 घंटे की अवधि में एक शहर में हर दो घंटे में दर्ज किए गए तापमान को दर्शाता है। दर्ज किए गए सबसे गर्म बिंदु और 16:00 बजे के तापमान के बीच, डिग्री सेल्सियस में, तापमान में कुल गिरावट की गणना करें।'
        self.description_kazakh = 'Жоғарыдағы сызықтық график қаладағы 8 сағаттық кезеңде әр екі сағат сайын тіркелген температураны көрсетеді. Тіркелген ең ыстық нүкте мен 16:00-дегі температура арасындағы жалпы температураның төмендеуін Цельсий градусымен есептеңіз.'
        self.description_swahili = 'Grafu ya mstari hapo juu inawakilisha halijoto iliyorekodiwa kila baada ya saa mbili katika jiji kwa kipindi cha saa 8. Kokotoa jumla ya kushuka kwa halijoto, katika nyuzi Selsiasi, kati ya sehemu yenye joto zaidi iliyorekodiwa na halijoto saa 16:00.'

class Mat106_multi(Mat106):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Menggunakan gambar tersebut, hitunglah selisih antara total jumlah laptop yang terjual oleh Toko A dan total jumlah laptop yang terjual oleh Toko B selama seluruh periode tiga minggu tersebut.'
        self.description_chinese = '使用该图，计算在整个三周期间，A店销售的笔记本电脑总数与B店销售的笔记本电脑总数之间的差值。'
        self.description_arabic = 'باستخدام الشكل، احسب الفرق بين العدد الإجمالي لأجهزة الكمبيوتر المحمولة التي باعها المتجر A والعدد الإجمالي لأجهزة الكمبيوتر المحمولة التي باعها المتجر B على مدار فترة الأسابيع الثلاثة بأكملها.'
        self.description_hindi = 'चित्र का उपयोग करते हुए, पूरी तीन सप्ताह की अवधि में स्टोर A द्वारा बेचे गए लैपटॉप की कुल संख्या और स्टोर B द्वारा बेचे गए लैपटॉप की कुल संख्या के बीच के अंतर की गणना करें।'
        self.description_kazakh = 'Суретті пайдалана отырып, бүкіл үш апталық кезеңде А дүкені сатқан ноутбуктердің жалпы саны мен В дүкені сатқан ноутбуктердің жалпы саны арасындағы айырмашылықты есептеңіз.'
        self.description_swahili = 'Kwa kutumia kielelezo, kokotoa tofauti kati ya idadi ya jumla ya kompyuta mpakato zilizouzwa na Duka A na idadi ya jumla ya kompyuta mpakato zilizouzwa na Duka B katika kipindi kizima cha wiki tatu.'

class Mat107_multi(Mat107):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Merujuk pada gambar, yang mencantumkan nilai ujian 11 siswa yang diurutkan secara 오름차순 (ascending). Hitunglah Jangkauan Antarkuartil (IQR) dari kumpulan data ini.'
        self.description_chinese = '参考该图，其中列出了按升序排列的11名学生的考试成绩。计算该数据集的四分位距（IQR）。'
        self.description_arabic = 'ارجع إلى الشكل الذي يسرد درجات الاختبار لـ 11 طالبًا مرتبة تصاعديًا. احسب المدى الربيعي (IQR) لمجموعة البيانات هذه.'
        self.description_hindi = 'चित्र देखें, जो आरोही क्रम (ascending order) में क्रमबद्ध 11 छात्रों के परीक्षा स्कोर सूचीबद्ध करता है। इस डेटा सेट के इंटरक्वेर्टाइल रेंज (IQR) की गणना करें।'
        self.description_kazakh = 'Өсу ретімен сұрыпталған 11 оқушының тест балдары берілген суретке сүйеніңіз. Осы деректер жиынының квартиль аралық құлашын (IQR) есептеңіз.'
        self.description_swahili = 'Rejelea kielelezo, ambacho kinaorodhesha alama za mtihani za wanafunzi 11 zilizopangwa kwa mpangilio wa kupanda. Kokotoa Masafa ya Kati ya Robo (IQR) ya seti hii ya data.'

class Mat108_multi(Mat108):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Merujuk pada gambar. Hitunglah rata-rata jumlah buku yang dibaca oleh siswa. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = '参考该图。计算学生阅读书籍的平均数量。答案保留3位小数。'
        self.description_arabic = 'ارجع إلى الشكل. احسب متوسط عدد الكتب التي قرأها الطلاب. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र देखें। छात्रों द्वारा पढ़ी गई पुस्तकों की माध्य संख्या (mean number) की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретке сүйеніңіз. Оқушылардың оқыған кітаптарының орташа санын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Rejelea kielelezo. Kokotoa wastani wa idadi ya vitabu vilivyosomwa na wanafunzi. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat109_multi(Mat109):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Merujuk pada gambar, yang menunjukkan tinggi anak pohon. Hitunglah estimasi rata-rata tinggi anak pohon. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = '参考该图，图中显示了树苗的高度。计算树苗的估计平均高度。答案保留3位小数。'
        self.description_arabic = 'ارجع إلى الشكل الذي يوضح ارتفاعات الشتلات. احسب متوسط الارتفاع المقدر للشتلات. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र देखें, जो पौधों की ऊँचाई दर्शाता है। पौधों की अनुमानित माध्य ऊँचाई की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Көшеттердің биіктігін көрсететін суретке сүйеніңіз. Көшеттердің бағаланған орташа биіктігін есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Rejelea kielelezo, ambacho kinaonyesha vimo vya miche. Kokotoa wastani wa kimo uliokadiriwa wa miche hiyo. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat110_multi(Mat110):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram dahan-dan-daun di bawah ini menampilkan usia anggota di sebuah klub buku. Menggunakan kunci yang diberikan, hitunglah jangkauan usia tersebut.'
        self.description_chinese = '下方的茎叶图显示了读书俱乐部成员的年龄。使用提供的图例，计算年龄的极差。'
        self.description_arabic = 'يعرض مخطط الساق والورقة أدناه أعمار أعضاء نادي الكتاب. باستخدام المفتاح المرفق، احسب مدى الأعمار.'
        self.description_hindi = 'नीचे दिया गया तना-और-पत्ती आरेख (stem-and-leaf diagram) एक बुक क्लब के सदस्यों की आयु प्रदर्शित करता है। दी गई कुंजी (key) का उपयोग करके, आयु के परास (range) की गणना करें।'
        self.description_kazakh = 'Төмендегі сабақ-жапырақ диаграммасы кітап клубы мүшелерінің жасын көрсетеді. Берілген кілтті пайдаланып, жас құлашын есептеңіз.'
        self.description_swahili = 'Mchoro wa shina na jani hapa chini unaonyesha umri wa wanachama katika klabu ya vitabu. Kwa kutumia ufunguo uliotolewa, kokotoa masafa ya umri.'

class Mat111_multi(Mat111):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Diagram batang komposit di bawah ini menunjukkan total pendapatan sebuah toko selama tiga hari. Pada hari Jumat, total tinggi batang merepresentasikan ${self.friday_total}. Berapakah nilai penjualan 'Minuman' pada hari itu?"
        self.description_chinese = f"下方的复合条形图显示了某商店三天的总收入。在星期五，条形图的总高度代表 ${self.friday_total}。那天的“饮料”（Drink）销售额是多少？"
        self.description_arabic = f"يوضح المخطط الشريطي المركب أدناه إجمالي إيرادات متجر على مدار ثلاثة أيام. في يوم الجمعة، يمثل الارتفاع الإجمالي للشريط ${self.friday_total}. ما هي قيمة مبيعات 'المشروبات' لذلك اليوم؟"
        self.description_hindi = f"नीचे दिया गया संयुक्त दंड आलेख (composite bar chart) तीन दिनों में एक स्टोर के कुल राजस्व को दर्शाता है। शुक्रवार को, बार की कुल ऊँचाई ${self.friday_total} को दर्शाती है। उस दिन 'Drink' की बिक्री का मूल्य क्या है?"
        self.description_kazakh = f"Төмендегі құрама бағандық диаграмма дүкеннің үш күн ішіндегі жалпы түсімін көрсетеді. Жұма күні бағанның жалпы биіктігі ${self.friday_total} құрайды. Сол күнгі 'Сусын' сатылымының мәні қандай?"
        self.description_swahili = f"Chati ya mwambaa mseto hapa chini inaonyesha mapato ya jumla ya duka kwa siku tatu. Siku ya Ijumaa, kimo cha jumla cha mwambaa kinawakilisha ${self.friday_total}. Ni nini thamani ya mauzo ya 'Kinywaji' kwa siku hiyo?"

class Mat112_multi(Mat112):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Piktogram menunjukkan pizza yang terjual pada empat malam. Kunci menunjukkan bahwa satu simbol penuh merepresentasikan {self.key_value} pizza. Berapa banyak pizza yang terjual pada hari Selasa?'
        self.description_chinese = f'象形图显示了四个晚上售出的比萨饼数量。图例表示一个完整的符号代表 {self.key_value} 个比萨饼。星期二售出了多少个比萨饼？'
        self.description_arabic = f'يوضح المخطط التصويري البيتزا المباعة في أربع أمسيات. يشير المفتاح إلى أن رمزًا كاملاً واحدًا يمثل {self.key_value} بيتزا. كم عدد البيتزا التي بيعت يوم الثلاثاء؟'
        self.description_hindi = f'पिक्टोग्राम चार शामों को बेचे गए पिज्जा को दर्शाता है। कुंजी (key) इंगित करती है कि एक पूर्ण प्रतीक {self.key_value} पिज्जा का प्रतिनिधित्व करता है। मंगलवार को कितने पिज्जा बेचे गए?'
        self.description_kazakh = f'Пиктограмма төрт кеште сатылған пиццаларды көрсетеді. Кілт бір толық символдың {self.key_value} пиццаны білдіретінін көрсетеді. Сейсенбіде қанша пицца сатылды?'
        self.description_swahili = f'Piktogramu inaonyesha piza zilizouzwa kwa jioni nne. Ufunguo unaonyesha kuwa alama moja kamili inawakilisha piza {self.key_value}. Ni piza ngapi ziliuzwa siku ya Jumanne?'

class Mat113_multi(Mat113):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Menurut diagram pencar, berapakah nilai jual kembali (dalam ribuan dolar) dari mobil berusia {self.target_age} tahun yang diwakili oleh titik P?'
        self.description_chinese = f'根据散点图，由点P代表的这辆 {self.target_age} 年车龄的汽车，其转售价值（以千美元计）是多少？'
        self.description_arabic = f'وفقًا لمخطط الانتشار، ما هي قيمة إعادة البيع (بآلاف الدولارات) للسيارة البالغة من العمر {self.target_age} عامًا الممثلة بالنقطة P؟'
        self.description_hindi = f'प्रकीर्ण आरेख (scatter diagram) के अनुसार, बिंदु P द्वारा दर्शाई गई {self.target_age}-वर्ष पुरानी कार का पुनर्विक्रय मूल्य (हजारों डॉलर में) क्या है?'
        self.description_kazakh = f'Шашырау диаграммасына сәйкес, P нүктесімен белгіленген {self.target_age} жылдық көліктің қайта сату құны (мың доллармен) қандай?'
        self.description_swahili = f'Kulingana na mchoro wa mtawanyiko, ni nini thamani ya kuuza tena (kwa maelfu ya dola) ya gari la miaka {self.target_age} linalowakilishwa na nukta P?'

class Mat114_multi(Mat114):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Menggunakan garis penyesuaian terbaik (line of best fit) yang ditunjukkan pada gambar, hitunglah prediksi tinggi (dalam cm) tanaman ketika {self.x_query} gram pupuk digunakan. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = f'使用图中所示的最佳拟合线，计算当使用 {self.x_query} 克肥料时植物的预测高度（以厘米为单位）。答案保留3位小数。'
        self.description_arabic = f'باستخدام خط أفضل مطابقة الموضح في الشكل، احسب الارتفاع المتوقع (بالسنتيمتر) لنبتة عند استخدام {self.x_query} جرام من الأسمدة. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = f'चित्र में दिखाई गई सर्वोत्तम फिट की रेखा (line of best fit) का उपयोग करके, जब {self.x_query} ग्राम उर्वरक का उपयोग किया जाता है, तो पौधे की अनुमानित ऊँचाई (cm में) की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Суретте көрсетілген ең жақсы сәйкестік сызығын пайдалана отырып, {self.x_query} грамм тыңайтқыш пайдаланылған кездегі өсімдіктің болжамды биіктігін (см-мен) есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kwa kutumia mstari wa mlingano bora unaoonyeshwa kwenye kielelezo, kokotoa kimo kilichotabiriwa (katika cm) cha mmea wakati gramu {self.x_query} za mbolea zinatumiwa. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat115_multi(Mat115):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Berapakah selisih vertikal (residu) antara nilai Fisika Siswa A yang sebenarnya dan nilai yang diprediksi oleh garis penyesuaian terbaik untuk nilai Matematika sebesar {self.student_a_x}? Berikan jawaban Anda yang benar hingga 3 tempat desimal."
        self.description_chinese = f"学生A的实际物理成绩与针对数学成绩为 {self.student_a_x} 时由最佳拟合线预测的成绩之间的垂直差（残差）是多少？答案保留3位小数。"
        self.description_arabic = f"ما هو الفرق الرأسي (الباقي) بين درجة الفيزياء الفعلية للطالب A والدرجة المتوقعة بواسطة خط أفضل مطابقة لدرجة رياضيات تبلغ {self.student_a_x}؟ قرّب إجابتك إلى 3 منازل عشرية."
        self.description_hindi = f"छात्र A के वास्तविक भौतिकी स्कोर और {self.student_a_x} के गणित स्कोर के लिए सर्वोत्तम फिट की रेखा द्वारा अनुमानित स्कोर के बीच ऊर्ध्वाधर अंतर (अवशिष्ट/residual) क्या है? अपना उत्तर 3 दशमलव स्थानों तक सही दें।"
        self.description_kazakh = f"А оқушысының физикадан алған нақты балы мен математикадан {self.student_a_x} балына арналған ең жақсы сәйкестік сызығы бойынша болжанған балдың арасындағы тік айырмашылық (қалдық) қандай? Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз."
        self.description_swahili = f"Ni nini tofauti ya wima (salio) kati ya alama halisi ya Fizikia ya Mwanafunzi A na alama iliyotabiriwa na mstari wa mlingano bora kwa alama ya Hisabati ya {self.student_a_x}?Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali."

class Mat116_multi(Mat116):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Menggunakan titik-titik koordinat yang diberikan pada gambar, tentukan nilai median ujian bagi siswa. Berikan jawaban Anda yang benar hingga 1 tempat desimal.'
        self.description_chinese = f'使用图中提供的坐标点，确定学生的分数中位数。答案保留1位小数。'
        self.description_arabic = f'باستخدام نقاط الإحداثيات المقدمة في الشكل، حدد الدرجة الوسيطة للطلاب. قرّب إجابتك إلى منزلة عشرية واحدة.'
        self.description_hindi = f'चित्र में दिए गए समन्वय बिंदुओं (coordinate points) का उपयोग करके, छात्रों के लिए माध्यिका अंक (median mark) निर्धारित करें। अपना उत्तर 1 दशमलव स्थान तक सही दें।'
        self.description_kazakh = f'Суретте берілген координаталық нүктелерді пайдалана отырып, оқушылар үшін медианалық балды анықтаңыз. Жауабыңызды 1 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kwa kutumia nukta za koordinate zilizotolewa kwenye kielelezo, amua alama ya mediani kwa wanafunzi. Toa jibu lako likiwa sahihi hadi sehemu 1 ya desimali.'

class Mat117_multi(Mat117):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah Jangkauan Antarkuartil (IQR) dari tinggi tanaman berdasarkan data yang diberikan pada gambar.'
        self.description_chinese = f'根据图中提供的数据，计算植物高度的四分位距（IQR）。'
        self.description_arabic = f'احسب المدى الربيعي (IQR) لارتفاعات النباتات بناءً على البيانات المقدمة في الشكل.'
        self.description_hindi = f'चित्र में दिए गए डेटा के आधार पर पौधों की ऊँचाई के इंटरक्वेर्टाइल रेंज (IQR) की गणना करें।'
        self.description_kazakh = f'Суретте берілген деректер негізінде өсімдік биіктіктерінің квартиль аралық құлашын (IQR) есептеңіз.'
        self.description_swahili = f'Kokotoa Masafa ya Kati ya Robo (IQR) ya vimo vya mimea kulingana na data iliyotolewa kwenye kielelezo.'

class Mat118_multi(Mat118):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Hitunglah frekuensi data yang direpresentasikan oleh batang ini. Berikan jawaban Anda yang benar hingga 1 tempat desimal.'
        self.description_chinese = f'计算该条形图所代表的数据频率。答案保留1位小数。'
        self.description_arabic = f'احسب تكرار البيانات الممثلة بهذا الشريط. قرّب إجابتك إلى منزلة عشرية واحدة.'
        self.description_hindi = f'इस बार (bar) द्वारा दर्शाए गए डेटा की आवृत्ति की गणना करें। अपना उत्तर 1 दशमलव स्थान तक सही दें।'
        self.description_kazakh = f'Осы бағанмен ұсынылған деректердің жиілігін есептеңіз. Жауабыңызды 1 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa marudio ya data inayowakilishwa na mwambaa huu. Toa jibu lako likiwa sahihi hadi sehemu 1 ya desimali.'

class Mat119_multi(Mat119):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Berapakah total frekuensi data yang direpresentasikan oleh ketiga batang ini?'
        self.description_chinese = f'这三个条形图所代表的数据的总频率是多少？'
        self.description_arabic = f'ما هو إجمالي تكرار البيانات الممثلة بهذه الأشرطة الثلاثة؟'
        self.description_hindi = f'इन तीन बारों द्वारा दर्शाए गए डेटा की कुल आवृत्ति क्या है?'
        self.description_kazakh = f'Осы үш бағанмен ұсынылған деректердің жалпы жиілігі қандай?'
        self.description_swahili = f'Ni nini marudio ya jumla ya data inayowakilishwa na miambaa hii mitatu?'

class Mat120_multi(Mat120):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Jika kelompok-kelompok ini diplot pada histogram yang sama, berapakah selisih positif antara tinggi batang untuk Kelompok B dan Kelompok A?'
        self.description_chinese = f'如果将这些组绘制在同一个直方图上，B组和A组条形图高度之间的正差值是多少？'
        self.description_arabic = f'إذا تم رسم هذه المجموعات على نفس المدرج التكراري، فما هو الفرق الموجب بين ارتفاع الشريط للمجموعة B والمجموعة A؟'
        self.description_hindi = f'यदि इन समूहों को एक ही हिस्टोग्राम पर आलेखित किया जाता है, तो समूह B और समूह A के बार की ऊँचाई के बीच धनात्मक अंतर क्या है?'
        self.description_kazakh = f'Егер осы топтар бір гистограммада салынса, B тобы мен A тобы үшін баған биіктігі арасындағы оң айырмашылық қандай болады?'
        self.description_swahili = f'Ikiwa vikundi hivi vimechorwa kwenye histrogramu sawa, ni nini tofauti chanya kati ya kimo cha mwambaa wa Kikundi B na Kikundi A?'

class Mat121_multi(Mat121):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Menggunakan grafik yang dideskripsikan pada gambar, evaluasi fungsi komposisi $f(g({self.start_x}))$.'
        self.description_chinese = f'使用图中所述的图像，求复合函数 $f(g({self.start_x}))$ 的值。'
        self.description_arabic = f'باستخدام الرسوم البيانية الموصوفة في الشكل، أوجد قيمة الدالة المركبة $f(g({self.start_x}))$.'
        self.description_hindi = f'चित्र में वर्णित ग्राफ़ का उपयोग करके, संयुक्त फलन (composite function) $f(g({self.start_x}))$ का मूल्यांकन करें।'
        self.description_kazakh = f'Суретте сипатталған графиктерді пайдалана отырып, $f(g({self.start_x}))$ күрделі функциясын есептеңіз.'
        self.description_swahili = f'Kwa kutumia grafu zilizofafanuliwa kwenye kielelezo, tathmini utendakazi mseto $f(g({self.start_x}))$.'

class Mat122_multi(Mat122):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Berdasarkan hubungan antara suatu fungsi dan inversnya yang ditunjukkan pada gambar, tentukan nilai $x$ sedemikian sehingga $f^{{-1}}(x) = {self.a}$.'
        self.description_chinese = f'根据图中所示的函数及其反函数之间的关系，确定当 $f^{{-1}}(x) = {self.a}$ 时 $x$ 的值。'
        self.description_arabic = f'بناءً على العلاقة بين دالة ودالتها العكسية الموضحة في الشكل، حدد قيمة $x$ بحيث يكون $f^{{-1}}(x) = {self.a}$.'
        self.description_hindi = f'चित्र में दिखाए गए एक फलन और उसके व्युत्क्रम (inverse) के बीच के संबंध के आधार पर, $x$ का वह मान निर्धारित करें जिसके लिए $f^{{-1}}(x) = {self.a}$ हो।'
        self.description_kazakh = f'Суретте көрсетілген функция мен оның кері функциясы арасындағы байланысқа сүйене отырып, $f^{{-1}}(x) = {self.a}$ болатындай $x$ мәнін анықтаңыз.'
        self.description_swahili = f'Kulingana na uhusiano kati ya utendakazi na kinyume chake unaoonyeshwa kwenye kielelezo, amua thamani ya $x$ ili $f^{{-1}}(x) = {self.a}$.'

class Mat123_multi(Mat123):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut mengilustrasikan grafik fungsi kuadrat $y = f(x)$ yang memiliki titik balik minimum pada koordinat $({self.h}, {self.k})$. Gambar tersebut juga menunjukkan kurva putus-putus kedua yang merepresentasikan suatu transformasi {self.label_g}. Hitunglah koordinat-$y$ dari titik minimum grafik hasil transformasi $g(x)$.'
        self.description_chinese = f'图中展示了二次函数 $y = f(x)$ 的图像，该函数在坐标 $({self.h}, {self.k})$ 处有一个最小拐点。图中还指示了第二条虚线曲线，代表变换 {self.label_g}。计算变换后的图像 $g(x)$ 的最低点的 $y$ 坐标。'
        self.description_arabic = f'يوضح الشكل الرسم البياني لدالة تربيعية $y = f(x)$ لها نقطة تحول صغرى عند الإحداثي $({self.h}, {self.k})$. يشير الشكل أيضًا إلى منحنى متقطع ثانٍ يمثل التحويل {self.label_g}. احسب الإحداثي $y$ للنقطة الصغرى للرسم البياني المحول $g(x)$.'
        self.description_hindi = f'चित्र एक द्विघात फलन $y = f(x)$ का ग्राफ़ दिखाता है जिसका न्यूनतम टर्निंग पॉइंट निर्देशांक $({self.h}, {self.k})$ पर है। चित्र एक दूसरा धराशायी वक्र (dashed curve) भी इंगित करता है जो एक रूपांतरण (transformation) {self.label_g} को दर्शाता है। रूपांतरित ग्राफ़ $g(x)$ के न्यूनतम बिंदु के $y$-निर्देशांक की गणना करें।'
        self.description_kazakh = f'Суретте $({self.h}, {self.k})$ координатасында минимум нүктесі бар $y = f(x)$ квадраттық функциясының графигі көрсетілген. Сондай-ақ, суретте {self.label_g} түрлендіруін білдіретін екінші үзік сызықты қисық көрсетілген. $g(x)$ түрлендірілген графигінің минимум нүктесінің $y$-координатасын есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi wa kipeo cha pili $y = f(x)$ ambayo ina nukta ya chini ya kugeukia kwenye koordinate $({self.h}, {self.k})$. Kielelezo pia kinaonyesha mzingo wa pili uliokatikakatika unaowakilisha mageuzi {self.label_g}. Kokotoa koordinate ya $y$ ya nukta ya chini ya grafu iliyogeuzwa $g(x)$.'

class Mat124_multi(Mat124):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan parabola penuh dari fungsi: ${self.equation_latex}$. Sumbu simetri $x = {self.h}$ ditandai dengan garis putus-putus. Tentukan nilai bilangan bulat terkecil untuk $k$ sedemikian sehingga fungsi $f(x)$ adalah fungsi satu-satu untuk domain $x \\ge k$.'
        self.description_chinese = f'图中显示了函数的完整抛物线：${self.equation_latex}$。对称轴 $x = {self.h}$ 用虚线标记。确定 $k$ 的最小整数值，使得函数 $f(x)$ 在定义域 $x \ge k$ 上是一个单射函数。'
        self.description_arabic = f'يوضح الشكل القطع المكافئ الكامل للدالة: ${self.equation_latex}$. محور التماثل $x = {self.h}$ محدد بخط منقط. حدد أصغر قيمة صحيحة لـ $k$ بحيث تكون الدالة $f(x)$ دالة واحد لواحد للمجال $x \ge k$.'
        self.description_hindi = f'चित्र फलन का पूर्ण परवलय (parabola) दिखाता है: ${self.equation_latex}$। सममिति का अक्ष (axis of symmetry) $x = {self.h}$ एक बिंदु वाली रेखा (dotted line) के साथ चिह्नित है। $k$ के लिए सबसे छोटा पूर्णांक मान निर्धारित करें ताकि फलन $f(x)$ डोमेन $x \\ge k$ के लिए एकैकी फलन (one-one function) हो।'
        self.description_kazakh = f'Суретте функцияның толық параболасы көрсетілген: ${self.equation_latex}$. Симметрия осі $x = {self.h}$ нүктелі сызықпен белгіленген. $f(x)$ функциясы $x \\ge k$ анықталу облысы үшін бірмәнді функция болатындай $k$ үшін ең кіші бүтін мәнді анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha parabola kamili ya utendakazi: ${self.equation_latex}$. Mhimili wa ulinganifu $x = {self.h}$ umewekwa alama ya mstari wa vitone. Amua thamani ndogo zaidi ya namba kamili ya $k$ ili utendakazi $f(x)$ uwe utendakazi wa moja-moja kwa kikoa $x \\ge k$.'

class Mat125_multi(Mat125):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Garis tegas berwarna biru pada gambar menampilkan grafik $y = h(x)$, yang memotong sumbu-$x$ positif di $x = {self.original_intercept}$. Garis putus-putus berwarna merah merepresentasikan transformasi $y = h({self.k}x)$. Carilah titik potong sumbu-$x$ dari grafik hasil transformasi $y = h({self.k}x)$.'
        self.description_chinese = f'图中蓝色实线显示了 $y = h(x)$ 的图像，该图像在 $x = {self.original_intercept}$ 处与正 $x$ 轴相交。红色虚线表示变换 $y = h({self.k}x)$。求变换后的图像 $y = h({self.k}x)$ 的 $x$ 截距。'
        self.description_arabic = f'يعرض الخط الأزرق المتصل في الشكل الرسم البياني لـ $y = h(x)$، والذي يتقاطع مع المحور x الموجب عند $x = {self.original_intercept}$. يمثل الخط الأحمر المتقطع التحويل $y = h({self.k}x)$. أوجد نقطة التقاطع مع المحور x للرسم البياني المحول $y = h({self.k}x)$.'
        self.description_hindi = f'चित्र में नीली ठोस रेखा $y = h(x)$ का ग्राफ़ प्रदर्शित करती है, जो धनात्मक x-अक्ष को $x = {self.original_intercept}$ पर प्रतिच्छेद करती है। लाल धराशायी रेखा रूपांतरण $y = h({self.k}x)$ को दर्शाती है। रूपांतरित ग्राफ़ $y = h({self.k}x)$ का x-अंतःखंड (x-intercept) ज्ञात करें।'
        self.description_kazakh = f'Суреттегі көк тұтас сызық $y = h(x)$ графигін көрсетеді, ол оң x-осін $x = {self.original_intercept}$ нүктесінде қияды. Қызыл үзік сызық $y = h({self.k}x)$ түрлендіруін білдіреді. Түрлендірілген $y = h({self.k}x)$ графигінің x-осімен қиылысу нүктесін табыңыз.'
        self.description_swahili = f'Mstari mnyoofu wa buluu kwenye kielelezo unaonyesha grafu ya $y = h(x)$, ambayo inakata mhimili wa x chanya kwenye $x = {self.original_intercept}$. Mstari mwekundu uliokatikakatika unawakilisha mageuzi $y = h({self.k}x)$. Tafuta kizuio cha x cha grafu iliyogeuzwa $y = h({self.k}x)$.'

class Mat126_multi(Mat126):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sebuah lingkaran didefinisikan oleh persamaan $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$. Sebuah garis singgung menyentuh lingkaran ini di titik $P({self.px}, {self.py})$. Tentukan titik potong sumbu-$y$ dari garis singgung ini. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = f'一个圆的方程为 $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$。一条切线在点 $P({self.px}, {self.py})$ 处与该圆相切。确定这条切线的 $y$ 截距。答案保留3位小数。'
        self.description_arabic = f'تُعرف دائرة بالمعادلة $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$. يمس خط مماس هذه الدائرة عند النقطة $P({self.px}, {self.py})$. حدد نقطة تقاطع هذا الخط المماس مع المحور $y$. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = f'एक वृत्त समीकरण $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$ द्वारा परिभाषित किया गया है। एक स्पर्श रेखा (tangent line) इस वृत्त को बिंदु $P({self.px}, {self.py})$ पर छूती है। इस स्पर्श रेखा का $y$-अंतःखंड निर्धारित करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Шеңбер $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$ теңдеуімен анықталады. Жанама сызық бұл шеңберді $P({self.px}, {self.py})$ нүктесінде жанайды. Осы жанама сызықтың $y$-осімен қиылысу нүктесін анықтаңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Duara inafafanuliwa kwa mlinganyo $(x - {self.h})^2 + (y - {self.k})^2 = {self.r ** 2}$. Mstari wa tanjiti unagusa duara hili kwenye nukta $P({self.px}, {self.py})$. Amua kizuio cha $y$ cha mstari huu wa tanjiti. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat127_multi(Mat127):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Garis lurus ${self.line_eq}$ memotong lingkaran ${self.circle_eq}$ pada dua titik yang berbeda, $A$ dan $B$. Hitunglah kuadrat panjang tali busur $AB$ (yaitu, carilah $AB^2$). Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = f'直线 ${self.line_eq}$ 与圆 ${self.circle_eq}$ 相交于两个不同的点 $A$ 和 $B$。计算弦 $AB$ 长度的平方（即求 $AB^2$）。答案保留3位小数。'
        self.description_arabic = f'يتقاطع الخط المستقيم ${self.line_eq}$ مع الدائرة ${self.circle_eq}$ في نقطتين متمايزتين، $A$ و $B$. احسب مربع طول الوتر $AB$ (أي أوجد $AB^2$). قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = f'सीधी रेखा ${self.line_eq}$ वृत्त ${self.circle_eq}$ को दो अलग-अलग बिंदुओं, $A$ और $B$ पर प्रतिच्छेद करती है। जीवा (chord) $AB$ की वर्ग लंबाई (squared length) की गणना करें (अर्थात, $AB^2$ ज्ञात करें)। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'${self.line_eq}$ түзуі ${self.circle_eq}$ шеңберін екі түрлі $A$ және $B$ нүктелерінде қияды. $AB$ хордасы ұзындығының квадратын есептеңіз (яғни, $AB^2$ табыңыз). Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Mstari mnyoofu ${self.line_eq}$ unakata duara ${self.circle_eq}$ kwenye nukta mbili tofauti, $A$ na $B$. Kokotoa urefu wa mraba wa kigwe $AB$ (yaani, tafuta $AB^2$). Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat128_multi(Mat128):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Pertimbangkan segmen garis yang menghubungkan titik $A({self.x1}, {self.y1})$ dan $B({self.x2}, {self.y2})$. Garis bagi tegak lurus dari segmen garis $AB$ memotong sumbu-$x$ di suatu titik $P$. Tentukan koordinat-$x$ dari $P$. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = f'考虑连接点 $A({self.x1}, {self.y1})$ 和 $B({self.x2}, {self.y2})$ 的线段。线段 $AB$ 的垂直平分线与 $x$ 轴相交于点 $P$。确定点 $P$ 的 $x$ 坐标。答案保留3位小数。'
        self.description_arabic = f'اعتبر القطعة المستقيمة التي تصل بين النقطتين $A({self.x1}, {self.y1})$ و $B({self.x2}, {self.y2})$. يتقاطع المنصف العمودي للقطعة المستقيمة $AB$ مع المحور x عند النقطة $P$. حدد الإحداثي x للنقطة $P$. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = f'बिंदुओं $A({self.x1}, {self.y1})$ और $B({self.x2}, {self.y2})$ को जोड़ने वाले रेखाखंड (line segment) पर विचार करें। रेखाखंड $AB$ का लंब समद्विभाजक (perpendicular bisector) x-अक्ष को एक बिंदु $P$ पर प्रतिच्छेद करता है। $P$ का x-निर्देशांक निर्धारित करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'$A({self.x1}, {self.y1})$ және $B({self.x2}, {self.y2})$ нүктелерін қосатын кесіндіні қарастырыңыз. $AB$ кесіндісінің орта перпендикуляры x-осін $P$ нүктесінде қияды. $P$ нүктесінің x-координатасын анықтаңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Fikiria pingili ya mstari inayounganisha nukta $A({self.x1}, {self.y1})$ na $B({self.x2}, {self.y2})$. Bisekta wima ya pingili ya mstari $AB$ inakata mhimili wa x kwenye nukta $P$. Amua koordinate ya x ya $P$. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat129_multi(Mat129):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sebuah lingkaran dengan persamaan $(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ terletak sepenuhnya di kuadran pertama dan menyinggung sumbu-$y$ tepat di satu titik. Carilah nilai $k$.'
        self.description_chinese = f'方程为 $(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ 的圆完全位于第一象限，并且与 $y$ 轴刚好相切于一点。求 $k$ 的值。'
        self.description_arabic = f'تقع دائرة معادلتها $(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ بالكامل في الربع الأول وتمس المحور y في نقطة واحدة بالضبط. أوجد قيمة $k$.'
        self.description_hindi = f'समीकरण $(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ वाला एक वृत्त पूरी तरह से प्रथम चतुर्थांश (first quadrant) में स्थित है और y-अक्ष को ठीक एक बिंदु पर छूता है। $k$ का मान ज्ञात करें।'
        self.description_kazakh = f'$(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ теңдеуімен берілген шеңбер толығымен бірінші ширекте жатыр және y-осін дәл бір нүктеде жанайды. $k$ мәнін табыңыз.'
        self.description_swahili = f'Duara lenye mlinganyo $(x-k)^2 + (y-{self.y_c})^2 = {self.r_squared}$ lipo kikamilifu katika roboduara ya kwanza na linagusa mhimili wa y kwenye nukta moja tu. Tafuta thamani ya $k$.'

class Mat130_multi(Mat130):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sebuah segitiga dibentuk oleh titik-titik sudut $A({self.ax}, {self.ay})$, $B({self.bx}, {self.by})$, dan $C({self.cx}, {self.cy})$. Hitunglah luas eksak dari segitiga $ABC$.'
        self.description_chinese = f'一个三角形由顶点 $A({self.ax}, {self.ay})$、$B({self.bx}, {self.by})$ 和 $C({self.cx}, {self.cy})$ 组成。计算三角形 $ABC$ 的准确面积。'
        self.description_arabic = f'يتكون مثلث من الرؤوس $A({self.ax}, {self.ay})$ و $B({self.bx}, {self.by})$ و $C({self.cx}, {self.cy})$. احسب المساحة الدقيقة للمثلث $ABC$.'
        self.description_hindi = f'शीर्षों (vertices) $A({self.ax}, {self.ay})$, $B({self.bx}, {self.by})$, और $C({self.cx}, {self.cy})$ द्वारा एक त्रिभुज बनता है। त्रिभुज $ABC$ के सटीक क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Үшбұрыш $A({self.ax}, {self.ay})$, $B({self.bx}, {self.by})$ және $C({self.cx}, {self.cy})$ төбелерінен құралған. $ABC$ үшбұрышының дәл ауданын есептеңіз.'
        self.description_swahili = f'Pembetatu inaundwa na vilele $A({self.ax}, {self.ay})$, $B({self.bx}, {self.by})$, na $C({self.cx}, {self.cy})$. Kokotoa eneo kamili la pembetatu $ABC$.'

class Mat131_multi(Mat131):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan juring sebuah lingkaran dan sebuah persegi. Persegi tersebut dikonstruksi sedemikian rupa sehingga total kelilingnya sama persis dengan total keliling juring tersebut. Tentukan luas persegi tersebut dalam cm$^2$. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = '图中显示了一个扇形和一个正方形。正方形的构造使其总周长刚好等于扇形的总周长。确定正方形的面积（单位：cm$^2$）。答案保留3位小数。'
        self.description_arabic = 'يوضح الشكل قطاعًا من دائرة ومربعًا. تم إنشاء المربع بحيث يكون محيطه الإجمالي مساويًا تمامًا للمحيط الإجمالي للقطاع. حدد مساحة المربع بـ cm$^2$. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र एक वृत्त का एक त्रिज्यखंड (sector) और एक वर्ग दिखाता है। वर्ग इस प्रकार बनाया गया है कि इसका कुल परिमाप त्रिज्यखंड के कुल परिमाप के बिल्कुल बराबर है। cm$^2$ में वर्ग का क्षेत्रफल निर्धारित करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте шеңбердің секторы және квадрат көрсетілген. Квадрат оның жалпы периметрі сектордың жалпы периметріне дәл тең болатындай етіп салынған. Квадраттың ауданын см$^2$ өлшемімен анықтаңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha sekta ya duara na mraba. Mraba umejengwa ili mzingo wake wa jumla uwe sawa kabisa na mzingo wa jumla wa sekta. Amua eneo la mraba katika cm$^2$. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat132_multi(Mat132):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Wiper kaca belakang mobil membersihkan area berbentuk bagian dari anulus (cincin), seperti yang ditunjukkan di daerah yang diarsir pada gambar. Area tersebut dibentuk oleh dua busur konsentris dengan sudut pusat yang sama $\\theta$. Jari-jari dalam daerah yang dibersihkan adalah $r$ cm. Menggunakan informasi yang diberikan pada gambar, hitunglah nilai jari-jari dalam $r$.'
        self.description_chinese = '汽车的后窗雨刮器清洁出一个类似于圆环一部分形状的区域，如图中阴影区域所示。该区域由两个具有相同圆心角 $\theta$ 的同心圆弧形成。清洁区域的内半径为 $r$ 厘米。使用图中提供的信息，计算内半径 $r$ 的值。'
        self.description_arabic = 'تنظف ممسحة الزجاج الخلفي للسيارة منطقة على شكل جزء من حلقة، كما هو موضح في المنطقة المظللة من الشكل. تتكون المنطقة من قوسين متحدي المركز بنفس الزاوية المركزية $\theta$. نصف القطر الداخلي للمنطقة المنظفة هو $r$ سم. باستخدام المعلومات المقدمة في الشكل، احسب قيمة نصف القطر الداخلي $r$.'
        self.description_hindi = 'कार के लिए एक रियर विंडो वाइपर एक वलय (annulus/ring) के हिस्से के आकार के क्षेत्र को साफ करता है, जैसा कि चित्र के छायांकित क्षेत्र में दिखाया गया है। क्षेत्र समान केंद्रीय कोण $\\theta$ वाले दो संकेंद्रित चापों (concentric arcs) से बनता है। साफ किए गए क्षेत्र की आंतरिक त्रिज्या $r$ cm है। चित्र में दी गई जानकारी का उपयोग करके, आंतरिक त्रिज्या $r$ के मान की गणना करें।'
        self.description_kazakh = 'Автокөліктің артқы терезе тазалағышы суреттегі боялған аймақта көрсетілгендей сақинаның бір бөлігі тәрізді аймақты тазартады. Аймақ бірдей орталық $\\theta$ бұрышы бар екі концентрлік доғадан құралған. Тазартылған аймақтың ішкі радиусы $r$ см. Суретте берілген ақпаратты пайдалана отырып, ішкі $r$ радиусының мәнін есептеңіз.'
        self.description_swahili = 'Wembe wa dirisha la nyuma wa gari unasafisha kanda yenye umbo la sehemu ya anula (duara lenye shimo katikati), kama inavyoonyeshwa kwenye eneo lililowekwa kivuli kwenye kielelezo. Kanda hiyo inaundwa na matao mawili ya kitovu kimoja yenye pembe sawa ya kitovu $\\theta$. Nusu kipenyo cha ndani cha kanda iliyosafishwa ni $r$ cm. Kwa kutumia taarifa iliyotolewa kwenye kielelezo, kokotoa thamani ya nusu kipenyo cha ndani $r$.'

class Mat133_multi(Mat133):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Sebuah juring kertas dipotong seperti yang ditunjukkan pada gambar. Tepi-tepi lurus (jari-jari) dari juring tersebut disambungkan tanpa ada bagian yang saling tumpang tindih untuk membentuk selimut kerucut lingkaran tegak. Hitunglah jari-jari alas ($r$) dari kerucut yang dihasilkan dalam cm. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = '如图所示剪下一个纸质扇形。扇形的直边（半径）无重叠地连接在一起，形成一个直角圆锥的曲面。计算所得圆锥的底面半径（$r$），单位为厘米。答案保留3位小数。'
        self.description_arabic = 'تم قطع قطاع ورقي كما هو موضح في الشكل. تم ضم الحواف المستقيمة (أنصاف الأقطار) للقطاع معًا دون تداخل لتشكيل السطح المنحني لمخروط دائري قائم. احسب نصف قطر القاعدة ($r$) للمخروط الناتج بالسم. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'कागज का एक त्रिज्यखंड काटा जाता है जैसा कि चित्र में दिखाया गया है। त्रिज्यखंड के सीधे किनारों (त्रिज्याओं) को बिना ओवरलैप किए एक साथ जोड़ा जाता है ताकि एक लंब वृत्तीय शंकु (right circular cone) का वक्र पृष्ठ बन सके। परिणामी शंकु के आधार की त्रिज्या ($r$) cm में गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Қағаз секторы суретте көрсетілгендей қиылып алынған. Сектордың түзу жиектері (радиустары) тік дөңгелек конустың қисық бетін құру үшін бір-біріне қабаттастырылмай біріктіріледі. Пайда болған конустың табан радиусын ($r$) см-мен есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Sekta ya karatasi inakatwa kama inavyoonyeshwa kwenye kielelezo. Kingo zilizonyooka (nusu kipenyo) za sekta zinaunganishwa pamoja bila kupishana ili kuunda uso mzingo wa pia wa duara mraba. Kokotoa nusu kipenyo cha kitako ($r$) cha pia linalotokana katika cm. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat134_multi(Mat134):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menampilkan kurva $y = f(x)$ di kuadran pertama. Sebuah garis normal ditarik pada kurva di titik $P$. Garis normal ini memotong sumbu-$x$ di titik $A$ dan sumbu-$y$ di titik $B$, membentuk segitiga $AOB$ dengan sumbu-sumbu koordinat. Hitunglah luas segitiga $AOB$. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = '图中在第一象限显示了一条曲线 $y = f(x)$。在点 $P$ 处画了曲线的一条法线。该法线与 $x$ 轴交于点 $A$，与 $y$ 轴交于点 $B$，与坐标轴形成一个三角形 $AOB$。计算三角形 $AOB$ 的面积。答案保留3位小数。'
        self.description_arabic = 'يعرض الشكل منحنى $y = f(x)$ في الربع الأول. يُرسم خط عمودي على المنحنى عند النقطة $P$. يتقاطع هذا الخط العمودي مع المحور x عند النقطة $A$ والمحور y عند النقطة $B$، مكونًا مثلثًا $AOB$ مع المحاور الإحداثية. احسب مساحة المثلث $AOB$. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र प्रथम चतुर्थांश में एक वक्र $y = f(x)$ प्रदर्शित करता है। बिंदु $P$ पर वक्र के लिए एक अभिलंब रेखा (normal line) खींची जाती है। यह अभिलंब रेखा x-अक्ष को बिंदु $A$ पर और y-अक्ष को बिंदु $B$ पर प्रतिच्छेद करती है, जिससे निर्देशांक अक्षों के साथ एक त्रिभुज $AOB$ बनता है। त्रिभुज $AOB$ के क्षेत्रफल की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте бірінші ширектегі $y = f(x)$ қисығы көрсетілген. Қисыққа $P$ нүктесінде нормаль сызық жүргізілген. Бұл нормаль сызық координата осьтерімен бірге $AOB$ үшбұрышын құрай отырып, x-осін $A$ нүктесінде және y-осін $B$ нүктесінде қияды. $AOB$ үшбұрышының ауданын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mzingo $y = f(x)$ katika roboduara ya kwanza. Mstari wa kawaida unachorwa kwenye mzingo kwenye nukta $P$. Mstari huu wa kawaida unakata mhimili wa x kwenye nukta $A$ na mhimili wa y kwenye nukta $B$, na kuunda pembetatu $AOB$ yenye mhimili wa koordinate. Kokotoa eneo la pembetatu $AOB$. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat135_multi(Mat135):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut mengilustrasikan tumpahan minyak berbentuk lingkaran di permukaan laut. Tumpahan tersebut meluas sedemikian rupa sehingga jari-jarinya $r$ meningkat dengan laju konstan. Menggunakan ukuran yang diberikan pada gambar, temukan laju peningkatan luas ($dA/dt$) dalam m$^2$/s pada saat ini. (Bagilah jawaban akhir Anda dengan $\\pi$). Berikan jawaban Anda yang benar hingga 2 tempat desimal.'
        self.description_chinese = '图中说明了海面上的一个圆形漏油区域。漏油区域正在扩大，其半径 $r$ 以恒定速率增加。使用图中提供的测量值，求此时面积的增加速率（$dA/dt$），单位为 m$^2$/s。（将最终答案除以 $\pi$）。答案保留2位小数。'
        self.description_arabic = 'يوضح الشكل تسربًا نفطيًا دائريًا على سطح المحيط. يتسع التسرب بحيث يزداد نصف قطره $r$ بمعدل ثابت. باستخدام القياسات المقدمة في الشكل، أوجد معدل الزيادة في المساحة ($dA/dt$) بـ m$^2$/s في هذه اللحظة. (اقسم إجابتك النهائية على $\pi$). قرّب إجابتك إلى منزلتين عشريتين.'
        self.description_hindi = 'चित्र समुद्र की सतह पर एक गोलाकार तेल रिसाव को दर्शाता है। रिसाव इस तरह फैल रहा है कि इसकी त्रिज्या $r$ एक निश्चित दर से बढ़ रही है। चित्र में दिए गए मापों का उपयोग करके, इस क्षण m$^2$/s में क्षेत्रफल वृद्धि की दर ($dA/dt$) ज्ञात करें। (अपने अंतिम उत्तर को $\\pi$ से विभाजित करें)। अपना उत्तर 2 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте мұхит бетіндегі дөңгелек мұнай дағы көрсетілген. Дақ оның $r$ радиусы тұрақты жылдамдықпен өсетіндей ұлғайып келеді. Суретте берілген өлшемдерді пайдалана отырып, осы сәттегі ауданның өсу жылдамдығын ($dA/dt$) м$^2$/с өлшемімен табыңыз. (Соңғы жауабыңызды $\\pi$-ге бөліңіз). Жауабыңызды 2 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha kumwagika kwa mafuta kwenye mviringo juu ya uso wa bahari. Kumwagika kunapanuka ili nusu kipenyo chake $r$ kiongezeke kwa kasi thabiti. Kwa kutumia vipimo vilivyotolewa kwenye kielelezo, tafuta kasi ya kuongezeka kwa eneo ($dA/dt$) katika m$^2$/s wakati huu. (Gawanya jibu lako la mwisho kwa $\\pi$). Toa jibu lako likiwa sahihi hadi sehemu 2 za desimali.'

class Mat136_multi(Mat136):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan jaring-jaring untuk sebuah kotak tanpa tutup yang terbuat dari lembaran logam persegi dengan memotong persegi berukuran sisi $x$ yang sama dari sudut-sudutnya dan melipat tutup-tutupnya ke atas. Berdasarkan dimensi yang diberikan pada gambar, temukan nilai $x$ yang membuat volume $V$ menjadi maksimum. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = '图中显示了一个无盖盒子的展开图，该盒子由一块正方形金属板制成，其制作方法是从四个角剪去边长为 $x$ 的等大正方形并折起翻边。根据图中提供的尺寸，求使体积 $V$ 达到最大时 $x$ 的值。答案保留3位小数。'
        self.description_arabic = 'يوضح الشكل شبكة لصندوق مفتوح من الأعلى مصنوع من لوح معدني مربع عن طريق قطع مربعات متساوية الضلع $x$ من الزوايا وطي اللوحات لأعلى. بناءً على الأبعاد المقدمة في الشكل، أوجد قيمة $x$ التي يكون الحجم $V$ عندها أقصى ما يمكن. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र एक खुले-शीर्ष वाले बॉक्स के लिए एक नेट दिखाता है जिसे धातु की एक चौकोर शीट के कोनों से भुजा $x$ वाले समान वर्ग काटकर और फ्लैप्स को मोड़कर बनाया गया है। चित्र में दिए गए आयामों के आधार पर, $x$ का वह मान ज्ञात करें जिसके लिए आयतन $V$ अधिकतम हो। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте бұрыштарынан қабырғасы $x$ болатын бірдей квадраттарды кесіп алып, қақпақтарын қайыру арқылы шаршы металл парақтан жасалған үсті ашық қораптың жазбасы көрсетілген. Суретте берілген өлшемдер негізінде $V$ көлемі максималды болатын $x$ мәнін табыңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha wavu wa sanduku la juu wazi lililotengenezwa kwa karatasi ya mraba ya chuma kwa kukata mraba sawa wa upande $x$ kutoka kwenye kona na kukunja viwambo juu. Kulingana na vipimo vilivyotolewa kwenye kielelezo, tafuta thamani ya $x$ ambapo ujazo $V$ ni mkubwa zaidi. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat137_multi(Mat137):
    def __init__(self):
        super().__init__()
        self.description_indonesian = "Gambar tersebut menampilkan dua fungsi linear, $f(x)$ dan $g(x)$. Misalkan $h(x) = f(g(x))$. Menggunakan koordinat dan titik yang ditunjukkan pada gambar, hitunglah nilai $h'(x)$ pada nilai-$x$ yang ditandai. Berikan jawaban Anda yang benar hingga 3 tempat desimal."
        self.description_chinese = "图中显示了两个线性函数 $f(x)$ 和 $g(x)$。令 $h(x) = f(g(x))$。使用图中坐标和指示的点，计算在标记的 $x$ 值处 $h'(x)$ 的值。答案保留3位小数。"
        self.description_arabic = "يعرض الشكل دالتين خطيتين، $f(x)$ و $g(x)$. لتكن $h(x) = f(g(x))$. باستخدام الإحداثيات والنقطة المشار إليها في الشكل، احسب قيمة $h'(x)$ عند قيمة $x$ المحددة. قرّب إجابتك إلى 3 منازل عشرية."
        self.description_hindi = "चित्र दो रैखिक फलन, $f(x)$ और $g(x)$ प्रदर्शित करता है। मान लीजिए $h(x) = f(g(x))$ है। निर्देशांकों और चित्र में दर्शाए गए बिंदु का उपयोग करके, चिह्नित $x$-मान पर $h'(x)$ के मान की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।"
        self.description_kazakh = "Суретте $f(x)$ және $g(x)$ екі сызықтық функциясы көрсетілген. $h(x) = f(g(x))$ болсын. Суретте көрсетілген координаталар мен белгіленген нүктені пайдалана отырып, белгіленген $x$ мәніндегі $h'(x)$ мәнін есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз."
        self.description_swahili = "Kielelezo kinaonyesha utendakazi mbili za mstari, $f(x)$ na $g(x)$. Acha $h(x) = f(g(x))$. Kwa kutumia koordinate na nukta iliyoonyeshwa kwenye kielelezo, kokotoa thamani ya $h'(x)$ kwenye thamani ya $x$ iliyowekwa alama. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali."

class Mat138_multi(Mat138):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menampilkan daerah yang diarsir di kuadran pertama yang dibatasi di bagian atas oleh fungsi parabola $f(x)$ dan di bagian bawah oleh sumbu-$x$. Menggunakan informasi dan fungsi yang diberikan pada gambar, hitunglah total luas daerah yang diarsir tersebut. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = '图中在第一象限显示了一个阴影区域，其上方以抛物线函数 $f(x)$ 为界，下方以 $x$ 轴为界。使用图中的信息和给定的函数，计算阴影区域的总面积。答案保留3位小数。'
        self.description_arabic = 'يعرض الشكل منطقة مظللة في الربع الأول يحدها من الأعلى دالة قطع مكافئ $f(x)$ ومن الأسفل المحور x. باستخدام المعلومات والدالة المعطاة في الشكل، احسب المساحة الإجمالية للمنطقة المظللة. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र प्रथम चतुर्थांश में एक छायांकित क्षेत्र प्रदर्शित करता है जो ऊपर एक परवलयिक फलन (parabolic function) $f(x)$ और नीचे x-अक्ष से घिरा है। चित्र में दी गई जानकारी और फलन का उपयोग करके, छायांकित क्षेत्र के कुल क्षेत्रफल की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте бірінші ширекте жоғарыдан $f(x)$ параболалық функциясымен және төменнен x-осімен шектелген боялған аймақ көрсетілген. Суретте берілген ақпарат пен функцияны пайдалана отырып, боялған аймақтың жалпы ауданын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha kanda iliyowekwa kivuli katika roboduara ya kwanza inayopakana juu na utendakazi wa parabola $f(x)$ na chini na mhimili wa x. Kwa kutumia taarifa na utendakazi uliotolewa kwenye kielelezo, kokotoa eneo la jumla la kanda iliyowekwa kivuli. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat139_multi(Mat139):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan grafik fungsi kecepatan $v(t)$ (dalam m/s) selama suatu interval waktu. Menggunakan koordinat yang diberikan pada grafik kecepatan-waktu, hitunglah total perpindahan benda tersebut selama seluruh durasi yang ditunjukkan.'
        self.description_chinese = '图中显示了某时间段内速度函数 $v(t)$（单位：m/s）的图像。使用速度-时间图中的坐标，计算物体在所显示的整个期间内的总位移。'
        self.description_arabic = 'يوضح الشكل الرسم البياني لدالة السرعة $v(t)$ (بالمتر/ثانية) خلال فترة زمنية. باستخدام الإحداثيات المقدمة في الرسم البياني للسرعة والزمن، احسب الإزاحة الإجمالية للجسم خلال المدة بأكملها الموضحة.'
        self.description_hindi = 'चित्र समय के एक अंतराल में एक वेग फलन (velocity function) $v(t)$ (m/s में) का ग्राफ़ दिखाता है। वेग-समय ग्राफ़ में दिए गए निर्देशांकों का उपयोग करके, दिखाई गई पूरी अवधि में वस्तु के कुल विस्थापन (displacement) की गणना करें।'
        self.description_kazakh = 'Суретте уақыт аралығындағы $v(t)$ жылдамдық функциясының (м/с өлшемімен) графигі көрсетілген. Жылдамдық-уақыт графигінде берілген координаталарды пайдалана отырып, көрсетілген барлық уақыт ішіндегі объектінің жалпы орын ауыстыруын есептеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha grafu ya utendakazi wa velositi $v(t)$ (katika m/s) kwa muda fulani. Kwa kutumia koordinate zilizotolewa kwenye grafu ya velositi-muda, kokotoa mtawanyo wa jumla wa kitu kwa muda wote ulioonyeshwa.'

class Mat140_multi(Mat140):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut mengilustrasikan bangun ruang 3D padat yang dibentuk dengan memutar daerah 2D tertentu mengelilingi sumbu-$x$. Berdasarkan fungsi, garis vertikal, dan putaran yang ditunjukkan pada gambar, hitunglah volume bangun ruang padat yang dihasilkan. Berikan jawaban Anda sebagai desimal yang dibulatkan hingga tiga tempat desimal. (Gunakan $\\pi \\approx 3.14159$).'
        self.description_chinese = '图中说明了一个三维立体图形，它是通过将特定的二维区域绕 $x$ 轴旋转而形成的。根据图中所指的函数、垂直线和旋转，计算所得立体的体积。答案以小数形式保留三位。（使用 $\pi \approx 3.14159$）。'
        self.description_arabic = 'يوضح الشكل مجسمًا ثلاثي الأبعاد تم تشكيله بتدوير منطقة محددة ثنائية الأبعاد حول المحور x. بناءً على الدالة والخط الرأسي والدوران المشار إليه في الشكل، احسب حجم المجسم الناتج. أعط إجابتك كعدد عشري مقرب إلى ثلاثة منازل. (استخدم $\pi \approx 3.14159$).'
        self.description_hindi = 'चित्र x-अक्ष के चारों ओर एक विशिष्ट 2D क्षेत्र को घुमाकर बनाई गई एक ठोस 3D आकृति को दर्शाता है। चित्र में दर्शाए गए फलन, ऊर्ध्वाधर रेखा और घूर्णन के आधार पर, परिणामी ठोस के आयतन की गणना करें। अपना उत्तर तीन स्थानों तक पूर्णांकित दशमलव के रूप में दें। ($\\pi \\approx 3.14159$ का उपयोग करें)।'
        self.description_kazakh = 'Суретте белгілі бір 2D аймақты x-осімен айналдыру арқылы пайда болған тұтас 3D фигура көрсетілген. Суретте көрсетілген функцияға, тік сызыққа және айналдыруға сүйене отырып, пайда болған дененің көлемін есептеңіз. Жауабыңызды үш таңбаға дейін дөңгелектелген ондық бөлшек ретінде беріңіз. ($\\pi \\approx 3.14159$ пайдаланыңыз).'
        self.description_swahili = 'Kielelezo kinaonyesha umbo dhabiti la 3D lililoundwa kwa kuzungusha kanda mahususi ya 2D kuzunguka mhimili wa x. Kulingana na utendakazi, mstari wa wima, na mzunguko ulioonyeshwa kwenye kielelezo, kokotoa ujazo wa umbo dhabiti linalotokana. Toa jibu lako kama desimali iliyoraundishwa hadi sehemu tatu. (Tumia $\\pi \\approx 3.14159$).'

class Mat141_multi(Mat141):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Variabel $x$ dan $y$ memenuhi hubungan $y = k a^x$, di mana $k$ dan $a$ adalah konstanta. Seperti yang ditunjukkan pada gambar, grafik $\\ln y$ terhadap $x$ adalah garis lurus yang melewati titik-titik $({self.x1}, {self.lny1})$ dan $({self.x2}, {self.lny2})$. Carilah nilai $a$.'
        self.description_chinese = f'变量 $x$ 和 $y$ 满足关系 $y = k a^x$，其中 $k$ 和 $a$ 是常数。如图所示，$\ln y$ 对 $x$ 的图是一条经过点 $({self.x1}, {self.lny1})$ 和 $({self.x2}, {self.lny2})$ 的直线。求 $a$ 的值。'
        self.description_arabic = f'المتغيران $x$ و $y$ يحققان العلاقة $y = k a^x$، حيث $k$ و $a$ ثابتان. كما هو موضح في الشكل، فإن الرسم البياني لـ $\ln y$ مقابل $x$ هو خط مستقيم يمر عبر النقطتين $({self.x1}, {self.lny1})$ و $({self.x2}, {self.lny2})$. أوجد قيمة $a$.'
        self.description_hindi = f'चर $x$ और $y$ संबंध $y = k a^x$ को संतुष्ट करते हैं, जहाँ $k$ और $a$ स्थिरांक हैं। जैसा कि चित्र में दिखाया गया है, $x$ के विरुद्ध $\\ln y$ का ग्राफ़ एक सीधी रेखा है जो बिंदुओं $({self.x1}, {self.lny1})$ और $({self.x2}, {self.lny2})$ से होकर गुजरती है। $a$ का मान ज्ञात करें।'
        self.description_kazakh = f'$x$ және $y$ айнымалылары $y = k a^x$ қатынасын қанағаттандырады, мұндағы $k$ және $a$ — тұрақтылар. Суретте көрсетілгендей, $\\ln y$-тің $x$-ке тәуелділік графигі $({self.x1}, {self.lny1})$ және $({self.x2}, {self.lny2})$ нүктелері арқылы өтетін түзу сызық болып табылады. $a$ мәнін табыңыз.'
        self.description_swahili = f'Vigezo $x$ na $y$ vinakidhi uhusiano $y = k a^x$, ambapo $k$ na $a$ ni viwango vya kutosha. Kama inavyoonyeshwa kwenye kielelezo, grafu ya $\\ln y$ dhidi ya $x$ ni mstari mnyoofu unaopita kwenye nukta $({self.x1}, {self.lny1})$ na $({self.x2}, {self.lny2})$. Tafuta thamani ya $a$.'

class Mat142_multi(Mat142):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Seperti yang ditunjukkan pada gambar, pertumbuhan kultur bakteri dimodelkan oleh $N = {self.n0} \\times {self.b}^{{{self.k}t}}$, di mana $N$ adalah jumlah bakteri setelah $t$ jam. Berdasarkan gambar tersebut, temukan nilai bilangan bulat terkecil untuk $t$ sedemikian rupa sehingga populasinya melebihi {self.threshold}.'
        self.description_chinese = f'如图所示，细菌培养物的生长模型为 $N = {self.n0} \times {self.b}^{{{self.k}t}}$，其中 $N$ 是 $t$ 小时后的细菌数量。根据该图，求使种群数量超过 {self.threshold} 的最小 $t$ 整数值。'
        self.description_arabic = f'كما هو موضح في الشكل، يتم نمذجة نمو مزرعة بكتيرية بواسطة $N = {self.n0} \times {self.b}^{{{self.k}t}}$، حيث $N$ هو عدد البكتيريا بعد $t$ ساعة. بناءً على الشكل، أوجد أصغر قيمة صحيحة لـ $t$ يتجاوز عندها عدد السكان {self.threshold}.'
        self.description_hindi = f'जैसा कि चित्र में दिखाया गया है, एक जीवाणु संवर्धन (bacterial culture) की वृद्धि को $N = {self.n0} \\times {self.b}^{{{self.k}t}}$ द्वारा प्रतिरूपित (modeled) किया जाता है, जहाँ $N$, $t$ घंटों के बाद जीवाणुओं की संख्या है। चित्र के आधार पर, $t$ का सबसे छोटा पूर्णांक मान ज्ञात करें जिसके लिए जनसंख्या {self.threshold} से अधिक हो जाती है।'
        self.description_kazakh = f'Суретте көрсетілгендей, бактерия дақылының өсуі $N = {self.n0} \\times {self.b}^{{{self.k}t}}$ формуласымен модельденеді, мұндағы $N$ — $t$ сағаттан кейінгі бактериялар саны. Суретке сүйене отырып, популяция {self.threshold} мәнінен асатын $t$-ның ең кіші бүтін мәнін табыңыз.'
        self.description_swahili = f'Kama inavyoonyeshwa kwenye kielelezo, ukuaji wa tamaduni ya bakteria unaigwa kwa $N = {self.n0} \\times {self.b}^{{{self.k}t}}$, ambapo $N$ ni idadi ya bakteria baada ya saa $t$. Kulingana na kielelezo, tafuta thamani ndogo zaidi ya namba kamili ya $t$ ambayo idadi ya watu inazidi {self.threshold}.'

class Mat143_multi(Mat143):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Seperti yang ditunjukkan pada gambar, suatu zat radioaktif meluruh mengikuti model $N = 100e^{{-\\lambda t}}$, di mana $N$ adalah persentase zat yang tersisa setelah $t$ tahun. Berdasarkan koordinat dari titik yang ditunjukkan pada kurva, carilah nilai konstanta peluruhan $\\lambda$. Berikan jawaban Anda yang benar hingga empat tempat desimal.'
        self.description_chinese = f'如图所示，某放射性物质根据模型 $N = 100e^{{-\lambda t}}$ 衰减，其中 $N$ 是 $t$ 年后剩余该物质的百分比。根据曲线上指示点的坐标，求衰变常数 $\lambda$ 的值。答案保留四位小数。'
        self.description_arabic = f'كما هو موضح في الشكل، تتحلل مادة مشعة وفقًا للنموذج $N = 100e^{{-\lambda t}}$، حيث $N$ هو النسبة المئوية للمادة المتبقية بعد $t$ سنة. بناءً على إحداثي النقطة المشار إليها على المنحنى، أوجد قيمة ثابت التحلل $\lambda$. قرّب إجابتك إلى أربع منازل عشرية.'
        self.description_hindi = f'जैसा कि चित्र में दिखाया गया है, एक रेडियोधर्मी पदार्थ मॉडल $N = 100e^{{-\\lambda t}}$ के अनुसार क्षय होता है, जहाँ $N$, $t$ वर्षों के बाद शेष बचे पदार्थ का प्रतिशत है। वक्र पर दर्शाए गए बिंदु के निर्देशांक के आधार पर, क्षय नियतांक (decay constant) $\\lambda$ का मान ज्ञात करें। अपना उत्तर चार दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'Суретте көрсетілгендей, радиоактивті зат $N = 100e^{{-\\lambda t}}$ моделіне сәйкес ыдырайды, мұндағы $N$ — $t$ жылдан кейінгі қалған заттың пайызы. Қисықтағы көрсетілген нүктенің координатасына сүйене отырып, ыдырау тұрақтысы $\\lambda$ мәнін табыңыз. Жауабыңызды төрт ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kama inavyoonyeshwa kwenye kielelezo, dutu nururifu inaoza kulingana na muundo $N = 100e^{{-\\lambda t}}$, ambapo $N$ ni asilimia ya dutu iliyobaki baada ya miaka $t$. Kulingana na koordinate ya nukta iliyoonyeshwa kwenye mzingo, tafuta thamani ya namba isiyobadilika ya uozo $\\lambda$. Toa jibu lako likiwa sahihi hadi sehemu nne za desimali.'

class Mat144_multi(Mat144):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan daerah yang dibatasi oleh sebuah kurva, sumbu-$x$, dan dua garis vertikal. Carilah luas eksak dari daerah yang diarsir ini.'
        self.description_chinese = '图中显示了一个由曲线、$x$ 轴和两条垂直线围成的区域。求该阴影区域的准确面积。'
        self.description_arabic = 'يوضح الشكل منطقة يحدها منحنى والمحور $x$ وخطان رأسيان. أوجد المساحة الدقيقة لهذه المنطقة المظللة.'
        self.description_hindi = 'चित्र एक वक्र, $x$-अक्ष और दो ऊर्ध्वाधर रेखाओं से घिरे एक क्षेत्र को दिखाता है। इस छायांकित क्षेत्र का सटीक क्षेत्रफल ज्ञात करें।'
        self.description_kazakh = 'Суретте қисықпен, $x$-осімен және екі тік сызықпен шектелген аймақ көрсетілген. Осы боялған аймақтың дәл ауданын табыңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha kanda inayopakana na mzingo, mhimili wa $x$, na mistari miwili ya wima. Tafuta eneo kamili la kanda hii iliyowekwa kivuli.'

class Mat145_multi(Mat145):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan grafik fungsi polinomial $y = f(x)$ berderajat 3. Menggunakan koordinat titik-titik yang ditunjukkan pada grafik, gunakan aturan trapesium dengan {self.n} interval untuk mengestimasi nilai integral tentu $\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$.'
        self.description_chinese = f'图中显示了3次多项式函数 $y = f(x)$ 的图像。使用图上所示点的坐标，用具有 {self.n} 个区间的梯形法则来估算定积分 $\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \, dx$ 的值。'
        self.description_arabic = f'يوضح الشكل الرسم البياني لدالة كثيرة الحدود $y = f(x)$ من الدرجة 3. باستخدام إحداثيات النقاط الموضحة على الرسم البياني، استخدم قاعدة شبه المنحرف مع {self.n} من الفترات لتقدير قيمة التكامل المحدد $\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \, dx$.'
        self.description_hindi = f'चित्र घात 3 के एक बहुपद फलन (polynomial function) $y = f(x)$ का ग्राफ़ दिखाता है। ग्राफ़ पर दिखाए गए बिंदुओं के निर्देशांकों का उपयोग करके, निश्चित समाकलन (definite integral) $\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$ के मान का अनुमान लगाने के लिए {self.n} अंतरालों के साथ समलंब नियम (trapezium rule) का उपयोग करें।'
        self.description_kazakh = f'Суретте 3-дәрежелі $y = f(x)$ көпмүшелік функциясының графигі көрсетілген. Графикте көрсетілген нүктелердің координаталарын пайдаланып, $\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$ анықталған интегралының мәнін бағалау үшін {self.n} аралығы бар трапеция ережесін қолданыңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi wa polinomiali $y = f(x)$ wa digrii 3. Kwa kutumia koordinate za nukta zilizoonyeshwa kwenye grafu, tumia kanuni ya trapeza yenye vipindi vya {self.n} kukadiria thamani ya intigro dhahiri $\\int_{{{self.x_start}}}^{{{self.x_end}}} f(x) \\, dx$.'

class Mat146_multi(Mat146):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan kurva $y = f(x)$. Daerah $R$ dibatasi oleh kurva tersebut, sumbu-$x$, dan garis $x=0$ serta $x=k$. Jika luas daerah $R$ tepat $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$, tentukan nilai $k$.'
        self.description_chinese = f'图中显示了曲线 $y = f(x)$。区域 $R$ 由该曲线、$x$ 轴以及直线 $x=0$ 和 $x=k$ 围成。如果区域 $R$ 的面积刚好为 $\frac{{{self.k}}}{{{self.a}}} \ln({self.ratio})$，确定 $k$ 的值。'
        self.description_arabic = f'يوضح الشكل المنحنى $y = f(x)$. يحد المنطقة $R$ المنحنى والمحور $x$ والخطان $x=0$ و $x=k$. إذا كانت مساحة المنطقة $R$ هي بالضبط $\frac{{{self.k}}}{{{self.a}}} \ln({self.ratio})$، فحدد قيمة $k$.'
        self.description_hindi = f'चित्र वक्र $y = f(x)$ दिखाता है। क्षेत्र $R$ वक्र, $x$-अक्ष और रेखाओं $x=0$ और $x=k$ से घिरा है। यदि क्षेत्र $R$ का क्षेत्रफल ठीक $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$ है, तो $k$ का मान निर्धारित करें।'
        self.description_kazakh = f'Суретте $y = f(x)$ қисығы көрсетілген. $R$ аймағы қисықпен, $x$-осімен және $x=0$ мен $x=k$ сызықтарымен шектелген. Егер $R$ аймағының ауданы дәл $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$ болса, $k$ мәнін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha mzingo $y = f(x)$. Kanda $R$ inapakana na mzingo, mhimili wa $x$, na mistari $x=0$ na $x=k$. Ikiwa eneo la kanda $R$ ni $\\frac{{{self.k}}}{{{self.a}}} \\ln({self.ratio})$ kamili, amua thamani ya $k$.'

class Mat147_multi(Mat147):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan grafik fungsi periodik $y = f(x)$ untuk $x \\ge 0$. Hitunglah luas daerah yang diarsir yang dibatasi oleh kurva dan sumbu-$x$ dari $x = 0$ ke batas yang ditunjukkan.'
        self.description_chinese = f'图中显示了 $x \ge 0$ 时周期函数 $y = f(x)$ 的图像。计算由曲线和 $x$ 轴在 $x = 0$ 到指示的上限之间围成的阴影区域面积。'
        self.description_arabic = f'يوضح الشكل الرسم البياني لدالة دورية $y = f(x)$ لـ $x \ge 0$. احسب مساحة المنطقة المظللة التي يحدها المنحنى والمحور $x$ من $x = 0$ إلى الحد المشار إليه.'
        self.description_hindi = f'चित्र $x \\ge 0$ के लिए एक आवर्ती फलन (periodic function) $y = f(x)$ का ग्राफ़ दिखाता है। वक्र और $x$-अक्ष द्वारा $x = 0$ से इंगित सीमा तक घिरे छायांकित क्षेत्र के क्षेत्रफल की गणना करें।'
        self.description_kazakh = f'Суретте $x \\ge 0$ үшін $y = f(x)$ периодты функциясының графигі көрсетілген. Қисықпен және $x = 0$-ден көрсетілген шекке дейінгі $x$-осімен шектелген боялған аймақтың ауданын есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi wa kipindi $y = f(x)$ kwa $x \\ge 0$. Kokotoa eneo la kanda iliyowekwa kivuli inayopakana na mzingo na mhimili wa $x$ kutoka $x = 0$ hadi kikomo kilichoonyeshwa.'

class Mat148_multi(Mat148):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan grafik fungsi kontinu $y = f(x)$ di atas suatu domain lokal. Identifikasi bilangan bulat **{self.extremum_type}** $n$ yang terlihat pada gambar sedemikian rupa sehingga akar persamaan $f(x) = 0$ terdapat di dalam interval $[n, n+1]$.'
        self.description_chinese = f'图中显示了连续函数 $y = f(x)$ 在局部定义域上的图像。识别图中可见的**{self.extremum_type}**整数 $n$，使得方程 $f(x) = 0$ 的根存在于区间 $[n, n+1]$ 内。'
        self.description_arabic = f'يوضح الشكل الرسم البياني لدالة متصلة $y = f(x)$ على مجال محلي. حدد العدد الصحيح $n$ **{self.extremum_type}** الظاهر في الشكل بحيث يوجد جذر للمعادلة $f(x) = 0$ في الفترة $[n, n+1]$.'
        self.description_hindi = f'चित्र एक स्थानीय डोमेन पर एक सतत फलन (continuous function) $y = f(x)$ का ग्राफ़ दिखाता है। चित्र में देखे गए **{self.extremum_type}** पूर्णांक $n$ को पहचानें ताकि अंतराल $[n, n+1]$ में समीकरण $f(x) = 0$ का एक मूल (root) मौजूद हो।'
        self.description_kazakh = f'Суретте локальді анықталу облысындағы $y = f(x)$ үзіліссіз функциясының графигі көрсетілген. $f(x) = 0$ теңдеуінің түбірі $[n, n+1]$ аралығында болатындай суретте көрінетін **{self.extremum_type}** бүтін $n$ санын анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi endelevu $y = f(x)$ katika kikoa cha ndani. Tambua **{self.extremum_type}** namba kamili $n$ inayoonekana kwenye kielelezo ili mzizi wa mlinganyo $f(x) = 0$ uwepo katika muda $[n, n+1]$.'

class Mat149_multi(Mat149):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan diagram sarang laba-laba untuk iterasi titik tetap guna mengaproksimasi akar positif dari $x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$. Dimulai dari nilai $x_0$ yang ditunjukkan pada grafik, temukan nilai aproksimasi dari akar tersebut setelah {self.k_iterations} iterasi. Berikan jawaban Anda hingga 10 tempat desimal.'
        self.description_chinese = f'图中显示了用于逼近 $x = \frac{{{self.p}}}{{{self.q}x + {self.r}}}$ 正根的不动点迭代的蛛网图。从图中所示的 $x_0$ 值开始，求 {self.k_iterations} 次迭代后的根的近似值。答案保留10位小数。'
        self.description_arabic = f'يوضح الشكل مخطط نسيج العنكبوت لتكرار النقطة الثابتة لتقريب الجذر الموجب لـ $x = \frac{{{self.p}}}{{{self.q}x + {self.r}}}$. بدءًا من القيمة $x_0$ الموضحة في الرسم البياني، أوجد تقريب الجذر بعد {self.k_iterations} من التكرارات. قرّب إجابتك إلى 10 منازل عشرية.'
        self.description_hindi = f'चित्र $x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$ के धनात्मक मूल (positive root) का अनुमान लगाने के लिए एक निश्चित-बिंदु पुनरावृत्ति (fixed-point iteration) के लिए एक कॉबवेब आरेख (cobweb diagram) दिखाता है। ग्राफ़ में दिखाए गए मान $x_0$ से शुरू करके, {self.k_iterations} पुनरावृत्तियों के बाद मूल का अनुमान ज्ञात करें। अपना उत्तर 10 दशमलव स्थानों तक दें।'
        self.description_kazakh = f'Суретте $x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$ теңдеуінің оң түбірін жуықтап табуға арналған жылжымайтын нүктелік итерацияға арналған өрмекші торы диаграммасы көрсетілген. Графикте көрсетілген $x_0$ мәнінен бастап, {self.k_iterations} итерациядан кейінгі түбірдің жуықталған мәнін табыңыз. Жауабыңызды 10 ондық таңбаға дейін беріңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha mchoro wa utando wa buibui wa mwisho usiobadilika ili kukaribia mzizi chanya wa $x = \\frac{{{self.p}}}{{{self.q}x + {self.r}}}$. Kuanzia na thamani $x_0$ inayoonyeshwa kwenye grafu, tafuta makadirio ya mzizi baada ya marudio ya {self.k_iterations}. Toa jibu lako hadi sehemu 10 za desimali.'

class Mat150_multi(Mat150):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Seperti yang ditunjukkan pada diagram sarang laba-laba untuk iterasi $x_{{n+1}} = g(x_n)$ yang dimulai dari $x_0$, tentukan jumlah iterasi yang diperlukan agar barisan tersebut bergerak keluar dari rentang bilangan bulat $[{self.range_a}, {self.range_b}]$.'
        self.description_chinese = f'如从 $x_0$ 开始的迭代 $x_{{n+1}} = g(x_n)$ 的蛛网图所示，确定序列移出整数范围 $[{self.range_a}, {self.range_b}]$ 所需的迭代次数。'
        self.description_arabic = f'كما هو موضح في مخطط نسيج العنكبوت للتكرار $x_{{n+1}} = g(x_n)$ بدءًا من $x_0$، حدد عدد التكرارات المطلوبة حتى يخرج التسلسل خارج النطاق الصحيح $[{self.range_a}, {self.range_b}]$.'
        self.description_hindi = f'जैसा कि $x_0$ से शुरू होने वाली पुनरावृत्ति $x_{{n+1}} = g(x_n)$ के लिए कॉबवेब आरेख में दिखाया गया है, अनुक्रम (sequence) को पूर्णांक सीमा $[{self.range_a}, {self.range_b}]$ से बाहर जाने के लिए आवश्यक पुनरावृत्तियों की संख्या निर्धारित करें।'
        self.description_kazakh = f'$x_0$ нүктесінен басталатын $x_{{n+1}} = g(x_n)$ итерациясына арналған өрмекші торы диаграммасында көрсетілгендей, тізбектің $[{self.range_a}, {self.range_b}]$ бүтін сандар диапазонынан шығуы үшін қажетті итерациялар санын анықтаңыз.'
        self.description_swahili = f'Kama inavyoonyeshwa kwenye mchoro wa utando wa buibui wa kurudia $x_{{n+1}} = g(x_n)$ kuanzia $x_0$, amua idadi ya marudio inahitajika ili mfuatano usonge nje ya masafa ya namba kamili $[{self.range_a}, {self.range_b}]$.'

class Mat151_multi(Mat151):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Variabel $x$ dan $y$ dihubungkan oleh persamaan $y = k e^{{ax}}$, di mana $k$ dan $a$ adalah konstanta. Grafik garis lurus diplot pada sumbu berlabel $x$ (horizontal) dan $\\ln y$ (vertikal). Menggunakan titik-titik yang ditandai pada grafik linear pada gambar, tentukan nilai konstanta $a$.'
        self.description_chinese = f'变量 $x$ 和 $y$ 通过方程 $y = k e^{{ax}}$ 相关联，其中 $k$ 和 $a$ 是常数。在标记为 $x$（水平）和 $\ln y$（垂直）的坐标轴上绘制了一条直线图。使用图中线性图上标记的点，确定常数 $a$ 的值。'
        self.description_arabic = f'يرتبط المتغيران $x$ و $y$ بالمعادلة $y = k e^{{ax}}$، حيث $k$ و $a$ ثابتان. تم رسم رسم بياني لخط مستقيم على محاور مسماة $x$ (أفقي) و $\ln y$ (رأسي). باستخدام النقاط المحددة على الرسم البياني الخطي في الشكل، حدد قيمة الثابت $a$.'
        self.description_hindi = f'चर $x$ और $y$ समीकरण $y = k e^{{ax}}$ द्वारा संबंधित हैं, जहाँ $k$ और $a$ स्थिरांक हैं। $x$ (क्षैतिज) और $\\ln y$ (ऊर्ध्वाधर) लेबल वाले अक्षों पर एक सीधी रेखा का ग्राफ़ आलेखित किया गया है। चित्र में रैखिक ग्राफ़ पर चिह्नित बिंदुओं का उपयोग करके, स्थिरांक $a$ का मान निर्धारित करें।'
        self.description_kazakh = f'$x$ және $y$ айнымалылары $y = k e^{{ax}}$ теңдеуімен байланысты, мұндағы $k$ және $a$ — тұрақтылар. Түзу сызық графигі $x$ (көлденең) және $\\ln y$ (тік) деп белгіленген осьтерде салынған. Суреттегі сызықтық графикте белгіленген нүктелерді пайдаланып, $a$ тұрақтысының мәнін анықтаңыз.'
        self.description_swahili = f'Vigezo $x$ na $y$ vinahusiana kwa mlinganyo $y = k e^{{ax}}$, ambapo $k$ na $a$ ni viwango vya kutosha. Grafu ya mstari mnyoofu inachorwa kwenye mhimili ulio na lebo $x$ (ulalo) na $\\ln y$ (wima). Kwa kutumia nukta zilizowekwa alama kwenye grafu ya mstari kwenye kielelezo, amua thamani ya kiwango cha kutosha cha $a$.'

class Mat152_multi(Mat152):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Variabel $x$ dan $y$ memenuhi hubungan $y = Ax^n$. Gambar tersebut menunjukkan grafik garis lurus yang diplot pada sumbu berlabel $\\lg x$ (horizontal) dan $\\lg y$ (vertikal), di mana $\\lg$ melambangkan $\\log_{{10}}$. Menggunakan titik-titik yang ditunjukkan pada gambar, temukan nilai $n$. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = f'变量 $x$ 和 $y$ 满足关系 $y = Ax^n$。图中显示了一条绘制在标记为 $\lg x$（水平）和 $\lg y$（垂直）的坐标轴上的直线，其中 $\lg$ 表示 $\log_{{10}}$。使用图中指示的点，求 $n$ 的值。答案保留3位小数。'
        self.description_arabic = f'يحقق المتغيران $x$ و $y$ العلاقة $y = Ax^n$. يوضح الشكل خطًا مستقيمًا مرسومًا على محاور مسماة $\lg x$ (أفقي) و $\lg y$ (رأسي)، حيث تشير $\lg$ إلى $\log_{{10}}$. باستخدام النقاط المشار إليها في الشكل، أوجد قيمة $n$. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = f'चर $x$ और $y$ संबंध $y = Ax^n$ को संतुष्ट करते हैं। चित्र $\\lg x$ (क्षैतिज) और $\\lg y$ (ऊर्ध्वाधर) लेबल वाले अक्षों पर आलेखित एक सीधी रेखा को दिखाता है, जहाँ $\\lg$, $\\log_{{10}}$ को दर्शाता है। चित्र में दर्शाए गए बिंदुओं का उपयोग करके, $n$ का मान ज्ञात करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = f'$x$ және $y$ айнымалылары $y = Ax^n$ қатынасын қанағаттандырады. Суретте $\\lg x$ (көлденең) және $\\lg y$ (тік) деп белгіленген осьтерде салынған түзу сызық көрсетілген, мұндағы $\\lg$ $\\log_{{10}}$ белгілейді. Суретте көрсетілген нүктелерді пайдаланып, $n$ мәнін табыңыз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Vigezo $x$ na $y$ vinakidhi uhusiano $y = Ax^n$. Kielelezo kinaonyesha mstari mnyoofu uliochorwa kwenye mhimili ulio na lebo $\\lg x$ (ulalo) na $\\lg y$ (wima), ambapo $\\lg$ inawakilisha $\\log_{{10}}$. Kwa kutumia nukta zilizoonyeshwa kwenye kielelezo, tafuta thamani ya $n$. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat153_multi(Mat153):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Sebuah persegi panjang ditunjukkan pada gambar dengan panjang, lebar, dan luasnya dinyatakan dalam bentuk $x$. Berdasarkan label yang diberikan pada diagram, hitunglah nilai numerik dari $x$.'
        self.description_chinese = '图中显示了一个矩形，其长度、宽度和面积均用 $x$ 表示。根据图中提供的标签，计算 $x$ 的数值。'
        self.description_arabic = 'يظهر مستطيل في الشكل مع التعبير عن طوله وعرضه ومساحته بدلالة $x$. بناءً على التسميات المقدمة في المخطط، احسب القيمة العددية لـ $x$.'
        self.description_hindi = 'चित्र में एक आयत दिखाया गया है जिसकी लंबाई, चौड़ाई और क्षेत्रफल $x$ के पदों में व्यक्त किए गए हैं। आरेख में दिए गए लेबलों के आधार पर, $x$ के संख्यात्मक मान की गणना करें।'
        self.description_kazakh = 'Суретте ұзындығы, ені және ауданы $x$ арқылы өрнектелген тіктөртбұрыш көрсетілген. Диаграммада берілген белгілерге сүйене отырып, $x$-тің сандық мәнін есептеңіз.'
        self.description_swahili = 'Mstatili unaonyeshwa kwenye kielelezo huku urefu wake, upana wake, na eneo lake vikielezewa kwa kutumia $x$. Kulingana na lebo zilizotolewa kwenye mchoro, kokotoa thamani ya namba ya $x$.'

class Mat154_multi(Mat154):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan grafik sebuah fungsi logaritmik. Grafik tersebut memiliki sebuah asimtot vertikal yang ditunjukkan oleh garis putus-putus dan melewati sebuah titik yang ditandai. Menggunakan informasi yang diberikan pada gambar, tentukan nilai $k$.'
        self.description_chinese = f'图中显示了一个对数函数的图像。该图像有一条由虚线指示的垂直渐近线，并经过一个标记点。使用图中提供的信息，确定 $k$ 的值。'
        self.description_arabic = f'يوضح الشكل رسمًا بيانيًا لدالة لوغاريتمية. يحتوي الرسم البياني على خط تقاربي رأسي مشار إليه بخط متقطع ويمر عبر نقطة محددة. باستخدام المعلومات المقدمة في الشكل، حدد قيمة $k$.'
        self.description_hindi = f'चित्र एक लघुगणकीय फलन (logarithmic function) का ग्राफ़ दिखाता है। ग्राफ़ में एक धराशायी रेखा द्वारा दर्शाया गया एक ऊर्ध्वाधर अनंतस्पर्शी (vertical asymptote) है और यह एक चिह्नित बिंदु से होकर गुजरता है। चित्र में दी गई जानकारी का उपयोग करके, $k$ का मान निर्धारित करें।'
        self.description_kazakh = f'Суретте логарифмдік функцияның графигі көрсетілген. Графикте үзік сызықпен көрсетілген тік асимптота бар және белгіленген нүкте арқылы өтеді. Суретте берілген ақпаратты пайдаланып, $k$ мәнін анықтаңыз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi wa logariti. Grafu ina asimptoti ya wima inayoonyeshwa na mstari uliokatikakatika na inapita kwenye nukta iliyowekwa alama. Kwa kutumia taarifa iliyotolewa kwenye kielelezo, amua thamani ya $k$.'

class Mat155_multi(Mat155):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menampilkan kurva eksponensial $y = e^{kx}$ dan daerah $R$ yang diarsir. Daerah tersebut dibatasi oleh kurva tersebut, sumbu koordinat, dan garis vertikal yang ditandai pada gambar. Hitunglah luas eksak dari daerah $R$ yang diarsir. Berikan jawaban Anda yang benar hingga 3 tempat desimal.'
        self.description_chinese = '图中显示了一条指数曲线 $y = e^{kx}$ 和一个阴影区域 $R$。该区域由曲线、坐标轴和图中标记的一条垂直线围成。计算阴影区域 $R$ 的准确面积。答案保留3位小数。'
        self.description_arabic = 'يعرض الشكل منحنى أسيًا $y = e^{kx}$ ومنطقة مظللة $R$. يحد المنطقة المنحنى والمحاور وخط رأسي محدد في الشكل. احسب المساحة الدقيقة للمنطقة المظللة $R$. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र एक घातांकीय वक्र (exponential curve) $y = e^{kx}$ और एक छायांकित क्षेत्र $R$ प्रदर्शित करता है। क्षेत्र वक्र, अक्षों और चित्र में चिह्नित एक ऊर्ध्वाधर रेखा से घिरा है। छायांकित क्षेत्र $R$ के सटीक क्षेत्रफल की गणना करें। अपना उत्तर 3 दशमलव स्थानों तक सही दें।'
        self.description_kazakh = 'Суретте $y = e^{kx}$ экспоненциалдық қисығы және боялған $R$ аймағы көрсетілген. Аймақ қисықпен, осьтермен және суретте белгіленген тік сызықпен шектелген. Боялған $R$ аймағының дәл ауданын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дәлдікпен беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mzingo wa eksponeshia $y = e^{kx}$ na kanda iliyowekwa kivuli $R$. Kanda inapakana na mzingo, mhimili, na mstari wa wima uliowekwa alama kwenye kielelezo. Kokotoa eneo kamili la kanda iliyowekwa kivuli $R$. Toa jibu lako likiwa sahihi hadi sehemu 3 za desimali.'

class Mat156_multi(Mat156):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan sebuah kurva dan daerah yang diarsir di bawahnya. Area yang diarsir terletak di antara kurva dan sumbu-x, dari titik asal ke batas atas yang ditandai. Menggunakan informasi pada gambar, carilah luas daerah yang diarsir. Berikan jawaban Anda sebagai desimal yang dibulatkan hingga tiga tempat desimal.'
        self.description_chinese = '图中显示了一条曲线及其下方的阴影区域。阴影区域位于曲线和 $x$ 轴之间，从原点延伸到标记的上限。使用图中的信息，求阴影区域的面积。答案以小数形式保留三位小数。'
        self.description_arabic = 'يوضح الشكل منحنى ومنطقة مظللة تحته. تقع المنطقة المظللة بين المنحنى والمحور x، من نقطة الأصل إلى حد علوي محدد. باستخدام المعلومات الواردة في الشكل، أوجد مساحة المنطقة المظللة. أعط إجابتك كعدد عشري مقرب إلى ثلاثة منازل عشرية.'
        self.description_hindi = 'चित्र एक वक्र और उसके नीचे एक छायांकित क्षेत्र दिखाता है। छायांकित क्षेत्र वक्र और x-अक्ष के बीच, मूल बिंदु से एक चिह्नित ऊपरी सीमा तक स्थित है। चित्र में दी गई जानकारी का उपयोग करके, छायांकित क्षेत्र का क्षेत्रफल ज्ञात करें। अपना उत्तर तीन दशमलव स्थानों तक पूर्णांकित दशमलव के रूप में दें।'
        self.description_kazakh = 'Суретте қисық сызық және оның астындағы боялған аймақ көрсетілген. Боялған аудан қисық пен x-осі арасында, координаталар басынан белгіленген жоғарғы шекке дейін орналасқан. Суреттегі ақпаратты пайдаланып, боялған аймақтың ауданын табыңыз. Жауабыңызды үш ондық таңбаға дейін дөңгелектелген ондық бөлшек ретінде беріңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mzingo na kanda iliyowekwa kivuli chini yake. Eneo lililowekwa kivuli lipo kati ya mzingo na mhimili wa x, kutoka kwenye asili hadi kikomo cha juu kilichowekwa alama. Kwa kutumia taarifa kwenye kielelezo, tafuta eneo la kanda iliyowekwa kivuli. Toa jibu lako kama desimali iliyoraundishwa hadi sehemu tatu za desimali.'

class Mat157_multi(Mat157):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut melukiskan grafik fungsi rasional $f(x)$. Area yang diminati diarsir dan dibatasi oleh kurva tersebut, sumbu-x, dan dua garis vertikal. Berdasarkan informasi visual pada gambar, hitunglah integral tentu dari $f(x)$ pada interval yang diarsir. Bulatkan jawaban Anda hingga tiga tempat desimal.'
        self.description_chinese = '图中描绘了有理函数 $f(x)$ 的图像。感兴趣的区域被涂上阴影，并由曲线、$x$ 轴和两条垂直线围成。根据图中的视觉信息，计算 $f(x)$ 在阴影区间上的定积分。将你的答案保留三位小数。'
        self.description_arabic = 'يصور الشكل الرسم البياني لدالة كسرية $f(x)$. المنطقة محل الاهتمام مظللة ويحدها المنحنى والمحور x وخطان رأسيان. بناءً على المعلومات المرئية في الشكل، احسب التكامل المحدد لـ $f(x)$ على الفترة المظللة. قرّب إجابتك إلى ثلاثة منازل عشرية.'
        self.description_hindi = 'चित्र एक परिमेय फलन (rational function) $f(x)$ का ग्राफ़ दर्शाता है। रुचि का क्षेत्र छायांकित है और वक्र, x-अक्ष और दो ऊर्ध्वाधर रेखाओं से घिरा है। चित्र में दृश्य जानकारी के आधार पर, छायांकित अंतराल पर $f(x)$ के निश्चित समाकलन (definite integral) की गणना करें। अपने उत्तर को तीन दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = 'Суретте $f(x)$ бөлшек-рационал функциясының графигі бейнеленген. Қарастырылып отырған аймақ боялған және қисықпен, x-осімен және екі тік сызықпен шектелген. Суреттегі визуалды ақпаратқа сүйене отырып, боялған интервалдағы $f(x)$ анықталған интегралын есептеңіз. Жауабыңызды үш ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha grafu ya utendakazi wenye mantiki $f(x)$. Eneo linalolengwa limewekwa kivuli na kupakana na mzingo, mhimili wa x, na mistari miwili ya wima. Kulingana na taarifa ya kuona kwenye kielelezo, kokotoa intigro dhahiri ya $f(x)$ katika muda uliowekwa kivuli. Raundisha jibu lako hadi sehemu tatu za desimali.'

class Mat158_multi(Mat158):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan sebuah kurva di kuadran pertama dan daerah yang diarsir yang dibatasi oleh kurva tersebut, sumbu-x, dan batas vertikal. Menggunakan informasi yang diberikan pada gambar, tentukan luas daerah yang diarsir. Bulatkan jawaban Anda hingga 3 tempat desimal.'
        self.description_chinese = '图中在第一象限显示了一条曲线，以及一个由该曲线、$x$ 轴和垂直界限围成的阴影区域。使用图中提供的信息，确定阴影区域的面积。将你的答案保留3位小数。'
        self.description_arabic = 'يوضح الشكل منحنى في الربع الأول ومنطقة مظللة يحدها المنحنى والمحور x وحد رأسي. باستخدام المعلومات المقدمة في الشكل، حدد مساحة المنطقة المظللة. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र प्रथम चतुर्थांश में एक वक्र और वक्र, x-अक्ष और एक ऊर्ध्वाधर सीमा से घिरे एक छायांकित क्षेत्र को दिखाता है। चित्र में दी गई जानकारी का उपयोग करके, छायांकित क्षेत्र का क्षेत्रफल निर्धारित करें। अपने उत्तर को 3 दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = 'Суретте бірінші ширектегі қисық сызық және қисықпен, x-осімен және тік шекпен шектелген боялған аймақ көрсетілген. Суретте берілген ақпаратты пайдаланып, боялған аймақтың ауданын анықтаңыз. Жауабыңызды 3 ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mzingo katika roboduara ya kwanza na kanda iliyowekwa kivuli inayopakana na mzingo, mhimili wa x, na kikomo cha wima. Kwa kutumia taarifa iliyotolewa kwenye kielelezo, amua eneo la kanda iliyowekwa kivuli. Raundisha jibu lako hadi sehemu 3 za desimali.'

class Mat159_multi(Mat159):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut mengilustrasikan kurva berbentuk lonceng dan daerah yang diarsir di bawahnya yang memanjang dari sumbu-y ke sebuah garis vertikal yang ditandai. Berdasarkan fungsi dan batas yang ditunjukkan pada diagram, hitunglah luas daerah ini. Bulatkan jawaban Anda hingga 3 tempat desimal.'
        self.description_chinese = '图中说明了一条钟形曲线及其下方从 $y$ 轴延伸至标记垂直线的阴影区域。根据图中所示的函数和界限，计算该区域的面积。将你的答案保留3位小数。'
        self.description_arabic = 'يوضح الشكل منحنى على شكل جرس ومنطقة مظللة تحته تمتد من المحور y إلى خط رأسي محدد. بناءً على الدالة والحد الموضح في المخطط، احسب مساحة هذه المنطقة. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र एक घंटी के आकार का वक्र (bell-shaped curve) और y-अक्ष से एक चिह्नित ऊर्ध्वाधर रेखा तक फैले इसके नीचे एक छायांकित क्षेत्र को दर्शाता है। फलन और आरेख में दिखाई गई सीमा के आधार पर, इस क्षेत्र के क्षेत्रफल की गणना करें। अपने उत्तर को 3 दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = 'Суретте қоңырау тәрізді қисық және y-осінен белгіленген тік сызыққа дейін созылатын оның астындағы боялған аймақ бейнеленген. Диаграммада көрсетілген функция мен шекке сүйене отырып, осы аймақтың ауданын есептеңіз. Жауабыңызды 3 ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mzingo wenye umbo la kengele na kanda iliyowekwa kivuli chini yake inayotoka kwenye mhimili wa y hadi kwenye mstari wa wima uliowekwa alama. Kulingana na utendakazi na kikomo kinachoonyeshwa kwenye mchoro, kokotoa eneo la kanda hii. Raundisha jibu lako hadi sehemu 3 za desimali.'

class Mat160_multi(Mat160):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut menunjukkan grafik fungsi trigonometri $y = f(x)$ pada suatu interval yang diarsir. Carilah luas daerah yang diarsir di bawah kurva tersebut. Bulatkan jawaban Anda hingga 3 tempat desimal.'
        self.description_chinese = f'图中显示了在阴影区间内三角函数 $y = f(x)$ 的图像。求曲线下方阴影区域的面积。将你的答案保留3位小数。'
        self.description_arabic = f'يوضح الشكل الرسم البياني لدالة مثلثية $y = f(x)$ على فترة مظللة. أوجد مساحة المنطقة المظللة تحت المنحنى. قرّب إجابتك إلى 3 منازل عشرية.'
        self.description_hindi = f'चित्र एक छायांकित अंतराल पर एक त्रिकोणमितीय फलन (trigonometric function) $y = f(x)$ का ग्राफ़ दिखाता है। वक्र के नीचे छायांकित क्षेत्र का क्षेत्रफल ज्ञात करें। अपने उत्तर को 3 दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Суретте боялған интервалдағы $y = f(x)$ тригонометриялық функциясының графигі көрсетілген. Қисық астындағы боялған аймақтың ауданын табыңыз. Жауабыңызды 3 ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha grafu ya utendakazi wa trigonometria $y = f(x)$ katika muda uliowekwa kivuli. Tafuta eneo la kanda iliyowekwa kivuli chini ya mzingo. Raundisha jibu lako hadi sehemu 3 za desimali.'

class Mat161_multi(Mat161):
    def __init__(self):
        super().__init__()
        self.description_indonesian = "Diagram tersebut menunjukkan grafik $y = x$ dan $y = f(x)$ untuk $x > 0$. Barisan 'sarang laba-laba' mengilustrasikan konvergensi proses iteratif $x_{n+1} = f(x_n)$ yang dimulai dari nilai awal $x_1$ yang ditandai pada sumbu. Menggunakan rumus iteratif dan nilai awal yang ditunjukkan pada gambar, hitunglah nilai dari iterasi ketiga, $x_3$, yang dibulatkan ke 3 tempat desimal."
        self.description_chinese = "图表显示了 $x > 0$ 时 $y = x$ 和 $y = f(x)$ 的图像。一个“蛛网”序列说明了从轴上标记的初始值 $x_1$ 开始的迭代过程 $x_{n+1} = f(x_n)$ 的收敛性。使用图中所示的迭代公式和初始值，计算第三次迭代 $x_3$ 的值，保留3位小数。"
        self.description_arabic = "يوضح المخطط الرسوم البيانية لـ $y = x$ و $y = f(x)$ لـ $x > 0$. يوضح تسلسل 'نسيج العنكبوت' تقارب عملية تكرارية $x_{n+1} = f(x_n)$ بدءًا من قيمة أولية $x_1$ محددة على المحور. باستخدام الصيغة التكرارية والقيمة الأولية الموضحة في الشكل، احسب قيمة التكرار الثالث، $x_3$، مقربًا إلى 3 منازل عشرية."
        self.description_hindi = "आरेख $x > 0$ के लिए $y = x$ और $y = f(x)$ के ग्राफ़ दिखाता है। एक 'कॉबवेब' अनुक्रम (sequence) अक्ष पर चिह्नित प्रारंभिक मान $x_1$ से शुरू होने वाली पुनरावृत्त प्रक्रिया (iterative process) $x_{n+1} = f(x_n)$ के अभिसरण (convergence) को दर्शाता है। चित्र में दिखाए गए पुनरावृत्त सूत्र और प्रारंभिक मान का उपयोग करके, 3 दशमलव स्थानों तक पूर्णांकित करते हुए, तीसरी पुनरावृत्ति, $x_3$ के मान की गणना करें।"
        self.description_kazakh = "Диаграммада $x > 0$ үшін $y = x$ және $y = f(x)$ графиктері көрсетілген. 'Өрмекші торы' тізбегі осьте белгіленген бастапқы $x_1$ мәнінен басталатын $x_{n+1} = f(x_n)$ итерациялық процесінің жинақтылығын бейнелейді. Суретте көрсетілген итерациялық формула мен бастапқы мәнді пайдаланып, 3 ондық таңбаға дейін дөңгелектей отырып, үшінші итерацияның мәнін, $x_3$, есептеңіз."
        self.description_swahili = "Mchoro unaonyesha grafu za $y = x$ na $y = f(x)$ kwa $x > 0$. Mfuatano wa 'utando wa buibui' unaonyesha muunganiko wa mchakato wa kurudia $x_{n+1} = f(x_n)$ kuanzia na thamani ya mwanzo $x_1$ iliyowekwa alama kwenye mhimili. Kwa kutumia kanuni ya kurudia na thamani ya mwanzo iliyoonyeshwa kwenye kielelezo, kokotoa thamani ya mrudio wa tatu, $x_3$, ukiraundisha hadi sehemu 3 za desimali."

class Mat162_multi(Mat162):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan sketsa kurva $y = a\\ln(x) - x + b$. Kurva tersebut memotong sumbu-$x$ di dua titik. Akar yang lebih besar, $\\alpha$, ditunjukkan terletak di antara dua bilangan bulat berurutan pada kisi sumbu-$x$, yang ditandai dengan interval satuan. Berdasarkan lokasi visual akar yang lebih besar pada gambar, identifikasi bilangan bulat $n$ sedemikian rupa sehingga $n < \\alpha < n+1$.'
        self.description_chinese = '图示为曲线 $y = a\ln(x) - x + b$ 的草图。该曲线与 $x$ 轴相交于两点。较大的根 $\alpha$ 显示为位于标有单位区间的 $x$ 轴网格上两个连续整数之间。根据图中较大根的视觉位置，找出满足 $n < \alpha < n+1$ 的整数 $n$。'
        self.description_arabic = 'يوضح الشكل رسمًا تخطيطيًا للمنحنى $y = a\ln(x) - x + b$. يتقاطع المنحنى مع المحور $x$ في نقطتين. يظهر أن الجذر الأكبر، $\alpha$، يقع بين عددين صحيحين متتاليين على شبكة المحور $x$، والمحددة بفترات الوحدة. بناءً على الموقع المرئي للجذر الأكبر في الشكل، حدد العدد الصحيح $n$ بحيث يكون $n < \alpha < n+1$.'
        self.description_hindi = 'चित्र वक्र $y = a\\ln(x) - x + b$ का एक रेखाचित्र दिखाता है। वक्र $x$-अक्ष को दो बिंदुओं पर प्रतिच्छेद करता है। बड़ा मूल (root), $\\alpha$, $x$-अक्ष ग्रिड पर दो क्रमागत पूर्णांकों के बीच स्थित दिखाया गया है, जो इकाई अंतरालों (unit intervals) के साथ चिह्नित है। चित्र में बड़े मूल के दृश्य स्थान के आधार पर, पूर्णांक $n$ की पहचान करें ताकि $n < \\alpha < n+1$ हो।'
        self.description_kazakh = 'Суретте $y = a\\ln(x) - x + b$ қисығының нобайы көрсетілген. Қисық $x$-осін екі нүктеде қияды. Үлкенірек $\\alpha$ түбірі бірлік интервалдармен белгіленген $x$-осі торындағы қатар тұрған екі бүтін санның арасында жатқаны көрсетілген. Суреттегі үлкенірек түбірдің визуалды орналасуына сүйене отырып, $n < \\alpha < n+1$ болатындай $n$ бүтін санын анықтаңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha mchoro wa mzingo $y = a\\ln(x) - x + b$. Mzingo unakata mhimili wa $x$ kwenye nukta mbili. Mzizi mkubwa zaidi, $\\alpha$, unaonyeshwa kuwa kati ya namba kamili mbili zinazofuatana kwenye gridi ya mhimili wa $x$, ambayo imewekwa alama ya vipindi vya kizio. Kulingana na eneo la kuona la mzizi mkubwa zaidi kwenye kielelezo, tambua namba kamili $n$ ili $n < \\alpha < n+1$.'

class Mat163_multi(Mat163):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menampilkan dua vektor yang berawal dari sebuah titik yang sama $O$ di ruang 3D. Vektor $\\mathbf{a}$ dan vektor $\\mathbf{b}$ adalah seperti yang dilabeli pada diagram. Vektor-vektor tersebut ditunjukkan tegak lurus oleh sebuah simbol sudut siku-siku. Menggunakan informasi pada gambar, hitunglah nilai konstanta $p$.'
        self.description_chinese = '图中显示了在三维空间中从公共点 $O$ 引出的两个向量。向量 $\mathbf{a}$ 和向量 $\mathbf{b}$ 如图中标记所示。通过直角符号指示这些向量是垂直的。使用图中的信息，计算常数 $p$ 的值。'
        self.description_arabic = 'يعرض الشكل متجهين ينبعثان من نقطة مشتركة $O$ في الفضاء ثلاثي الأبعاد. المتجه $\mathbf{a}$ والمتجه $\mathbf{b}$ كما هما مسميان في المخطط. يُشار إلى أن المتجهين متعامدان بواسطة رمز الزاوية القائمة. باستخدام المعلومات الواردة في الشكل، احسب قيمة الثابت $p$.'
        self.description_hindi = 'चित्र 3D स्पेस में एक सामान्य बिंदु $O$ से उत्पन्न होने वाले दो सदिश (vectors) प्रदर्शित करता है। सदिश $\\mathbf{a}$ और सदिश $\\mathbf{b}$ आरेख में लेबल किए गए अनुसार हैं। सदिशों को समकोण प्रतीक द्वारा लंबवत (perpendicular) होने का संकेत दिया गया है। चित्र में दी गई जानकारी का उपयोग करके, स्थिरांक $p$ के मान की गणना करें।'
        self.description_kazakh = 'Суретте 3D кеңістігіндегі ортақ $O$ нүктесінен шығатын екі вектор көрсетілген. $\\mathbf{a}$ векторы және $\\mathbf{b}$ векторы диаграммада белгіленгендей. Векторлар тік бұрыш символымен перпендикуляр екендігі көрсетілген. Суреттегі ақпаратты пайдаланып, $p$ тұрақтысының мәнін есептеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha vekta mbili zinazotoka kwenye nukta moja $O$ katika nafasi ya 3D. Vekta $\\mathbf{a}$ na vekta $\\mathbf{b}$ zimewekwa lebo kama kwenye mchoro. Vekta zinaonyeshwa kuwa za wima kwa alama ya pembetatu mraba. Kwa kutumia taarifa kwenye kielelezo, kokotoa thamani ya kiwango cha kutosha cha $p$.'

class Mat164_multi(Mat164):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Sebuah diagram menunjukkan dua garis lurus $L_1$ dan $L_2$ yang berpotongan di titik $X$ di ruang 3D. Garis $L_1$ melewati titik $A$ dan sejajar dengan vektor $\\mathbf{d_1}$. Garis $L_2$ melewati titik $B$ dan sejajar dengan vektor $\\mathbf{d_2}$. Menggunakan koordinat dan komponen yang dilabeli pada diagram, selesaikan untuk titik potong dari garis-garis ini guna menentukan nilai numerik dari konstanta $m$.'
        self.description_chinese = '图表显示了在三维空间中相交于点 $X$ 的两条直线 $L_1$ 和 $L_2$。直线 $L_1$ 经过点 $A$ 且平行于向量 $\mathbf{d_1}$。直线 $L_2$ 经过点 $B$ 且平行于向量 $\mathbf{d_2}$。使用图中标记的坐标和分量，求解这些直线的交点，以确定常数 $m$ 的数值。'
        self.description_arabic = 'يوضح المخطط خطين مستقيمين $L_1$ و $L_2$ يتقاطعان عند النقطة $X$ في الفضاء ثلاثي الأبعاد. يمر الخط $L_1$ عبر النقطة $A$ ويوازي المتجه $\mathbf{d_1}$. يمر الخط $L_2$ عبر النقطة $B$ ويوازي المتجه $\mathbf{d_2}$. باستخدام الإحداثيات والمركبات المسماة في المخطط، حل لإيجاد نقطة تقاطع هذين الخطين لتحديد القيمة العددية للثابت $m$.'
        self.description_hindi = 'एक आरेख 3D स्पेस में बिंदु $X$ पर प्रतिच्छेद करने वाली दो सीधी रेखाएँ $L_1$ और $L_2$ दिखाता है। रेखा $L_1$ बिंदु $A$ से होकर गुजरती है और सदिश $\\mathbf{d_1}$ के समानांतर है। रेखा $L_2$ बिंदु $B$ से होकर गुजरती है और सदिश $\\mathbf{d_2}$ के समानांतर है। आरेख में लेबल किए गए निर्देशांकों और घटकों का उपयोग करके, स्थिरांक $m$ का संख्यात्मक मान निर्धारित करने के लिए इन रेखाओं के प्रतिच्छेदन (intersection) को हल करें।'
        self.description_kazakh = 'Диаграммада 3D кеңістігіндегі $X$ нүктесінде қиылысатын $L_1$ және $L_2$ екі түзу сызық көрсетілген. $L_1$ түзуі $A$ нүктесі арқылы өтеді және $\\mathbf{d_1}$ векторына параллель. $L_2$ түзуі $B$ нүктесі арқылы өтеді және $\\mathbf{d_2}$ векторына параллель. Диаграммада белгіленген координаталар мен құрамдастарды пайдаланып, $m$ тұрақтысының сандық мәнін анықтау үшін осы түзулердің қиылысуын табыңыз.'
        self.description_swahili = 'Mchoro unaonyesha mistari miwili minyoofu $L_1$ na $L_2$ inayokata kwenye nukta $X$ katika nafasi ya 3D. Mstari $L_1$ unapita kwenye nukta $A$ na ni sambamba na vekta $\\mathbf{d_1}$. Mstari $L_2$ unapita kwenye nukta $B$ na ni sambamba na vekta $\\mathbf{d_2}$. Kwa kutumia koordinate na vipengele vilivyowekwa lebo kwenye mchoro, tatua makutano ya mistari hii ili kuamua thamani ya namba ya kiwango cha kutosha cha $m$.'

class Mat165_multi(Mat165):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Sebuah limas segitiga $OABC$ ditunjukkan dengan titik asal di $O(0,0,0)$. Vektor posisi dari titik-titik sudut $A, B,$ dan $C$ adalah seperti yang ditunjukkan pada diagram. Titik $M$ adalah titik tengah eksak dari rusuk $AB$. Vektor $\\vec{MC}$ menghubungkan $M$ ke titik sudut $C$. Hitunglah kuadrat magnitudo dari vektor $\\vec{MC}$ (yaitu, hitunglah $|\\vec{MC}|^2$).'
        self.description_chinese = '图示为一个以原点 $O(0,0,0)$ 为顶点的三棱锥 $OABC$。顶点 $A$、$B$ 和 $C$ 的位置向量如图所示。点 $M$ 是边 $AB$ 的精确中点。向量 $\vec{MC}$ 将 $M$ 连接到顶点 $C$。计算向量 $\vec{MC}$ 大小的平方（即计算 $|\vec{MC}|^2$）。'
        self.description_arabic = 'يظهر هرم ثلاثي $OABC$ ونقطة الأصل عند $O(0,0,0)$. متجهات الموضع للرؤوس $A$ و $B$ و $C$ هي كما هو موضح في المخطط. النقطة $M$ هي نقطة المنتصف الدقيقة للحافة $AB$. يصل متجه $\vec{MC}$ النقطة $M$ بالرأس $C$. احسب مربع مقدار المتجه $\vec{MC}$ (أي احسب $|\vec{MC}|^2$).'
        self.description_hindi = 'मूल बिंदु $O(0,0,0)$ के साथ एक त्रिभुजाकार पिरामिड $OABC$ दिखाया गया है। शीर्षों $A, B,$ और $C$ के स्थिति सदिश (position vectors) आरेख में दिखाए गए अनुसार हैं। बिंदु $M$ किनारे $AB$ का सटीक मध्यबिंदु है। एक सदिश $\\vec{MC}$, $M$ को शीर्ष $C$ से जोड़ता है। सदिश $\\vec{MC}$ के वर्ग परिमाण (squared magnitude) की गणना करें (अर्थात, $|\\vec{MC}|^2$ की गणना करें)।'
        self.description_kazakh = '$O(0,0,0)$ бас нүктесінде орналасқан $OABC$ үшбұрышты пирамидасы көрсетілген. $A, B$ және $C$ төбелерінің радиус-векторлары диаграммада көрсетілгендей. $M$ нүктесі — $AB$ қырының дәл ортасы. $\\vec{MC}$ векторы $M$ нүктесін $C$ төбесімен қосады. $\\vec{MC}$ векторы ұзындығының квадратын есептеңіз (яғни, $|\\vec{MC}|^2$ есептеңіз).'
        self.description_swahili = 'Piramidi ya pembetatu $OABC$ inaonyeshwa kukiwa na asili kwenye $O(0,0,0)$. Vekta za nafasi za vilele $A, B,$ na $C$ zinaonyeshwa kama kwenye mchoro. Nukta $M$ ni nukta ya kati kamili ya ukingo $AB$. Vekta $\\vec{MC}$ inaunganisha $M$ kwenye kilele $C$. Kokotoa ukubwa wa mraba wa vekta $\\vec{MC}$ (yaani, kokotoa $|\\vec{MC}|^2$).'

class Mat166_multi(Mat166):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Sebuah jajar genjang $ABCD$ diplot dalam sistem koordinat 3D. Koordinat dari tiga titik sudut $A, B,$ dan $C$ dilabeli pada diagram. Titik sudut keempat $D$ dilabeli dengan koordinat yang tidak diketahui $(x, y, z)$. Menggunakan sifat penjumlahan/pengurangan vektor untuk jajar genjang, temukan jumlah koordinat dari titik sudut $D$ (yaitu, hitunglah $x + y + z$).'
        self.description_chinese = '在三维坐标系中绘制了一个平行四边形 $ABCD$。三个顶点 $A$、$B$ 和 $C$ 的坐标在图中已标出。第四个顶点 $D$ 被标记为未知坐标 $(x, y, z)$。使用平行四边形的向量加减性质，求顶点 $D$ 的坐标之和（即计算 $x + y + z$）。'
        self.description_arabic = 'تم رسم متوازي أضلاع $ABCD$ في نظام إحداثيات ثلاثي الأبعاد. تم تسمية إحداثيات ثلاثة من الرؤوس $A$ و $B$ و $C$ في المخطط. تم تسمية الرأس الرابع $D$ بإحداثيات غير معروفة $(x, y, z)$. باستخدام خصائص جمع/طرح المتجهات لمتوازي الأضلاع، أوجد مجموع إحداثيات الرأس $D$ (أي احسب $x + y + z$).'
        self.description_hindi = 'एक 3D समन्वय प्रणाली में एक समांतर चतुर्भुज (parallelogram) $ABCD$ आलेखित किया गया है। तीन शीर्षों $A, B,$ और $C$ के निर्देशांक आरेख में लेबल किए गए हैं। चौथा शीर्ष $D$ अज्ञात निर्देशांकों $(x, y, z)$ के साथ लेबल किया गया है। एक समांतर चतुर्भुज के लिए सदिश योग/घटाव गुणों का उपयोग करके, शीर्ष $D$ के निर्देशांकों का योग ज्ञात करें (अर्थात, $x + y + z$ की गणना करें)।'
        self.description_kazakh = '$ABCD$ параллелограмы 3D координаталар жүйесінде салынған. $A, B$ және $C$ үш төбесінің координаталары диаграммада белгіленген. Төртінші $D$ төбесі белгісіз $(x, y, z)$ координаталарымен белгіленген. Параллелограмм үшін векторларды қосу/азайту қасиеттерін пайдаланып, $D$ төбесі координаталарының қосындысын табыңыз (яғни, $x + y + z$ есептеңіз).'
        self.description_swahili = 'Msambamba $ABCD$ umechora katika mfumo wa koordinate wa 3D. Koordinate za vilele vitatu $A, B,$ na $C$ zimewekwa lebo kwenye mchoro. Kilele cha nne $D$ kimewekwa lebo ya koordinate zisizojulikana $(x, y, z)$. Kwa kutumia sifa za kujumlisha/kutoa vekta kwa msambamba, tafuta jumla ya koordinate za kilele $D$ (yaani, kokotoa $x + y + z$).'

class Mat167_multi(Mat167):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan sebuah persegi pada diagram Argand dengan titik sudut yang diberi label $O$, $P$, $Q$, dan $R$ dengan urutan berlawanan arah jarum jam. $O$ adalah titik asal. Titik sudut $P$ merepresentasikan bilangan kompleks $z_1$, seperti yang ditentukan pada label.\n\nJika titik-titik sudut tersebut membentuk sebuah persegi $OPQR$, tentukan bagian imajiner dari bilangan kompleks yang direpresentasikan oleh titik sudut $R$.'
        self.description_chinese = '图中显示了阿甘图（复平面图）中的一个正方形，其顶点按逆时针顺序标记为 $O$、$P$、$Q$ 和 $R$。$O$ 为原点。顶点 $P$ 代表复数 $z_1$，如标签中所述。\n\n如果这些顶点组成正方形 $OPQR$，确定由顶点 $R$ 代表的复数的虚部。'
        self.description_arabic = 'يوضح الشكل مربعًا في مخطط أرجاند برؤوس مسماة $O$ و $P$ و $Q$ و $R$ بترتيب عكس اتجاه عقارب الساعة. $O$ هي نقطة الأصل. يمثل الرأس $P$ العدد المركب $z_1$، كما هو محدد في التسمية.\n\nإذا كانت الرؤوس تشكل مربعًا $OPQR$، فحدد الجزء التخيلي للعدد المركب الذي يمثله الرأس $R$.'
        self.description_hindi = 'चित्र आर्गंड आरेख (Argand diagram) में वामावर्त (counter-clockwise) क्रम में $O$, $P$, $Q$, और $R$ लेबल वाले शीर्षों के साथ एक वर्ग दिखाता है। $O$ मूल बिंदु है। शीर्ष $P$ सम्मिश्र संख्या $z_1$ को दर्शाता है, जैसा कि लेबल में निर्दिष्ट है।\n\nयदि शीर्ष एक वर्ग $OPQR$ बनाते हैं, तो शीर्ष $R$ द्वारा दर्शाई गई सम्मिश्र संख्या का काल्पनिक भाग (imaginary part) निर्धारित करें।'
        self.description_kazakh = 'Суретте Арганд диаграммасында сағат тіліне қарсы бағытта $O$, $P$, $Q$ және $R$ деп белгіленген төбелері бар квадрат көрсетілген. $O$ — координаталар басы. $P$ төбесі белгіде көрсетілгендей $z_1$ комплекс санын білдіреді.\n\nЕгер төбелер $OPQR$ квадратын құраса, $R$ төбесімен берілген комплекс санның жорамал бөлігін анықтаңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha mraba katika mchoro wa Argand huku vilele vikiwa vimewekwa lebo $O$, $P$, $Q$, na $R$ kwa mpangilio wa kinyume na mwendo wa saa. $O$ ni asili. Kilele $P$ kinawakilisha namba changamano $z_1$, kama ilivyotajwa kwenye lebo.\n\nIkiwa vilele vinaunda mraba $OPQR$, amua sehemu ya kuwaziwa ya namba changamano inayowakilishwa na kilele $R$.'

class Mat168_multi(Mat168):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menampilkan diagram Argand dengan sebuah lingkaran dan sebuah garis vertikal. Lingkaran tersebut merepresentasikan tempat kedudukan (lokus) yang didefinisikan oleh $|z - c| = r$. Garis tersebut merepresentasikan tempat kedudukan titik-titik di mana $\\text{Re}(z) = k$. Garis tersebut menyinggung lingkaran di sisi kanannya. Berdasarkan label pada diagram, tentukan nilai $k$.'
        self.description_chinese = '图中显示了一个带有圆和垂直线的阿甘图。圆代表由 $|z - c| = r$ 定义的轨迹。直线代表 $\text{Re}(z) = k$ 的点的轨迹。该直线在圆的右侧与圆相切。根据图中的标签，确定 $k$ 的值。'
        self.description_arabic = 'يعرض الشكل مخطط أرجاند بدائرة وخط رأسي. تمثل الدائرة المحل الهندسي المعرف بـ $|z - c| = r$. يمثل الخط المحل الهندسي للنقاط حيث $\text{Re}(z) = k$. الخط مماس للدائرة على جانبها الأيمن. بناءً على التسميات في المخطط، حدد قيمة $k$.'
        self.description_hindi = 'चित्र एक वृत्त और एक ऊर्ध्वाधर रेखा के साथ एक आर्गंड आरेख प्रदर्शित करता है। वृत्त $|z - c| = r$ द्वारा परिभाषित बिंदुपथ (locus) का प्रतिनिधित्व करता है। रेखा उन बिंदुओं के बिंदुपथ का प्रतिनिधित्व करती है जहाँ $\\text{Re}(z) = k$ है। रेखा वृत्त के दाईं ओर उस पर स्पर्शरेखा (tangent) है। आरेख में लेबलों के आधार पर, $k$ का मान निर्धारित करें।'
        self.description_kazakh = 'Суретте шеңбері және тік сызығы бар Арганд диаграммасы көрсетілген. Шеңбер $|z - c| = r$ арқылы анықталатын геометриялық орынды білдіреді. Түзу $\\text{Re}(z) = k$ болатын нүктелердің геометриялық орнын білдіреді. Түзу шеңберді оның оң жағында жанайды. Диаграммадағы белгілерге сүйене отырып, $k$ мәнін анықтаңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha mchoro wa Argand wenye duara na mstari wa wima. Duara linawakilisha kiini kinachofafanuliwa na $|z - c| = r$. Mstari unawakilisha kiini cha nukta ambapo $\\text{Re}(z) = k$. Mstari ni tanjiti kwa duara kwenye upande wake wa kulia. Kulingana na lebo kwenye mchoro, amua thamani ya $k$.'

class Mat169_multi(Mat169):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan diagram Argand dengan tiga titik: titik asal $O$, titik $A$ yang merepresentasikan bilangan kompleks $z$, dan titik $B$ yang merepresentasikan konjugatnya $\\bar{z}$. Sebuah segitiga yang diarsir menghubungkan ketiga titik ini. Menggunakan nilai $z$ yang dilabeli pada gambar, hitunglah luas segitiga yang diarsir tersebut.'
        self.description_chinese = '图中显示了一个有三个点的阿甘图：原点 $O$、代表复数 $z$ 的点 $A$ 以及代表其共轭复数 $\bar{z}$ 的点 $B$。一个阴影三角形连接了这些点。使用图中标记的 $z$ 值，计算阴影三角形的面积。'
        self.description_arabic = 'يوضح الشكل مخطط أرجاند بثلاث نقاط: نقطة الأصل $O$، النقطة $A$ التي تمثل العدد المركب $z$، والنقطة $B$ التي تمثل مرافقه $\bar{z}$. يصل مثلث مظلل بين هذه النقاط. باستخدام قيمة $z$ المسماة في الشكل، احسب مساحة المثلث المظلل.'
        self.description_hindi = 'चित्र तीन बिंदुओं के साथ एक आर्गंड आरेख दिखाता है: मूल बिंदु $O$, सम्मिश्र संख्या $z$ को दर्शाने वाला बिंदु $A$, और इसके संयुग्मी (conjugate) $\\bar{z}$ को दर्शाने वाला बिंदु $B$। एक छायांकित त्रिभुज इन बिंदुओं को जोड़ता है। चित्र में लेबल किए गए $z$ के मान का उपयोग करके, छायांकित त्रिभुज के क्षेत्रफल की गणना करें।'
        self.description_kazakh = 'Суретте үш нүктесі бар Арганд диаграммасы көрсетілген: координаталар басы $O$, $z$ комплекс санын білдіретін $A$ нүктесі және оның түйіндесі $\\bar{z}$-ті білдіретін $B$ нүктесі. Боялған үшбұрыш осы нүктелерді қосады. Суретте белгіленген $z$ мәнін пайдаланып, боялған үшбұрыштың ауданын есептеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mchoro wa Argand wenye nukta tatu: asili $O$, nukta $A$ inayowakilisha namba changamano $z$, na nukta $B$ inayowakilisha unyambulisho wake $\\bar{z}$. Pembetatu iliyowekwa kivuli inaunganisha nukta hizi. Kwa kutumia thamani ya $z$ iliyowekwa lebo kwenye kielelezo, kokotoa eneo la pembetatu iliyowekwa kivuli.'

class Mat170_multi(Mat170):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan sebuah sinar (setengah garis) yang merepresentasikan sebuah tempat kedudukan (lokus) pada bidang kompleks. Sinar tersebut berawal dari titik $A$ pada sumbu imajiner dan memiliki sudut argumen yang spesifik, seperti yang ditunjukkan pada diagram. Carilah nilai titik potong sumbu-$x$ di mana tempat kedudukan ini melintasi sumbu real. Bulatkan ke 3 tempat desimal.'
        self.description_chinese = '图中显示了一条代表复平面中轨迹的射线（半直线）。该射线起源于虚轴上的点 $A$，并具有特定的辐角，如图所示。求该轨迹穿过实轴处的 $x$ 截距的值。保留3位小数。'
        self.description_arabic = 'يوضح الشكل شعاعًا (نصف خط) يمثل محلًا هندسيًا في المستوى المركب. ينبعث الشعاع من النقطة $A$ على المحور التخيلي وله زاوية سعة محددة، كما هو موضح في المخطط. أوجد قيمة نقطة التقاطع $x$ حيث يعبر هذا المحل الهندسي المحور الحقيقي. قرّب إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र सम्मिश्र तल (complex plane) में एक बिंदुपथ (locus) का प्रतिनिधित्व करने वाली एक किरण (ray/half-line) को दिखाता है। किरण काल्पनिक अक्ष (imaginary axis) पर बिंदु $A$ से उत्पन्न होती है और इसका एक विशिष्ट कोणांक (argument angle) होता है, जैसा कि आरेख में दिखाया गया है। उस $x$-अंतःखंड का मान ज्ञात करें जहाँ यह बिंदुपथ वास्तविक अक्ष (real axis) को पार करता है। 3 दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = 'Суретте комплекс жазықтықтағы геометриялық орынды білдіретін сәуле (жартылай түзу) көрсетілген. Сәуле жорамал осьтегі $A$ нүктесінен басталады және диаграммада көрсетілгендей нақты аргумент бұрышына ие. Осы геометриялық орынның нақты осьті қиып өтетін x-қиылысының мәнін табыңыз. 3 ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mshale (nusu-mstari) unaowakilisha kiini katika bapa changamano. Mshale unatoka kwenye nukta $A$ kwenye mhimili wa kuwaziwa na una pembe maalum ya hoja, kama inavyoonyeshwa kwenye mchoro. Tafuta thamani ya kizuio cha $x$ ambapo kiini hiki kinavuka mhimili halisi. Raundisha hadi sehemu 3 za desimali.'

class Mat171_multi(Mat171):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Tiga gaya sebidang bekerja di satu titik ke arah yang ditunjukkan pada diagram. Diketahui bahwa gaya-gaya tersebut dalam keadaan setimbang, carilah nilai $X$.'
        self.description_chinese = '三个共面力在图中所示方向上作用于一点。已知这些力处于平衡状态，求 $X$ 的值。'
        self.description_arabic = 'تؤثر ثلاث قوى متحدة المستوى عند نقطة في الاتجاهات الموضحة في المخطط. علمًا بأن القوى في حالة اتزان، أوجد قيمة $X$.'
        self.description_hindi = 'आरेख में दिखाई गई दिशाओं में एक बिंदु पर तीन समतलीय बल (coplanar forces) कार्य करते हैं। यह देखते हुए कि बल संतुलन (equilibrium) में हैं, $X$ का मान ज्ञात करें।'
        self.description_kazakh = 'Бір жазықтықта жатқан үш күш бір нүктеге диаграммада көрсетілген бағыттарда әсер етеді. Күштер тепе-теңдікте екенін ескере отырып, $X$ мәнін табыңыз.'
        self.description_swahili = 'Nguvu tatu kwenye bapa moja zinafanya kazi kwenye nukta katika mielekeo inayoonyeshwa kwenye mchoro. Kwa kuzingatia kwamba nguvu zipo katika usawa, tafuta thamani ya $X$.'

class Mat172_multi(Mat172):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan grafik kecepatan-waktu yang memodelkan gerak suatu partikel. Partikel tersebut meninggalkan $O$ dan pada akhirnya kembali ke $O$ pada waktu $T$. Berdasarkan gambar dan informasi yang diberikan, carilah nilai $T$.'
        self.description_chinese = '图表显示了对粒子运动建模的速度-时间图。粒子离开 $O$ 并最终在时间 $T$ 返回 $O$。根据图表和提供的信息，求 $T$ 的值。'
        self.description_arabic = 'يوضح المخطط رسمًا بيانيًا للسرعة والزمن يمثل حركة جسيم. يغادر الجسيم النقطة $O$ ويعود في النهاية إلى $O$ في الوقت $T$. بناءً على الشكل والمعلومات المقدمة، أوجد قيمة $T$.'
        self.description_hindi = 'आरेख एक वेग-समय ग्राफ़ (velocity-time graph) दिखाता है जो एक कण की गति को मॉडल करता है। कण $O$ से निकलता है और अंततः समय $T$ पर $O$ पर वापस आ जाता है। चित्र और दी गई जानकारी के आधार पर, $T$ का मान ज्ञात करें।'
        self.description_kazakh = 'Диаграммада бөлшектің қозғалысын модельдейтін жылдамдық-уақыт графигі көрсетілген. Бөлшек $O$-дан шығып, ақырында $T$ уақытында $O$-ға оралады. Суретке және берілген ақпаратқа сүйене отырып, $T$ мәнін табыңыз.'
        self.description_swahili = 'Mchoro unaonyesha grafu ya velositi-muda ambayo inaiga mwendo wa chembe. Chembe inaondoka $O$ na hatimaye inarudi $O$ katika muda $T$. Kulingana na kielelezo na taarifa iliyotolewa, tafuta thamani ya $T$.'

class Mat173_multi(Mat173):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Tiga buah partikel $P, Q$, dan $R$ berada dalam keadaan diam dalam satu garis lurus pada sebuah bidang horizontal yang licin seperti yang ditunjukkan pada gambar. Massa $P$ adalah $m_P$, $Q$ adalah $m_Q$, dan $R$ adalah $m_R$. $P$ diproyeksikan secara langsung menuju $Q$ dengan kecepatan awal. Setelah $P$ dan $Q$ bertumbukan, $P$ terus bergerak dalam arah yang sama dengan kecepatan yang berkurang. Pada tumbukan selanjutnya antara $Q$ dan $R$, partikel-partikel ini menyatu. Carilah kecepatan partikel gabungan tersebut setelah tumbukan kedua ini.'
        self.description_chinese = '如图所示，三个粒子 $P, Q$ 和 $R$ 静止在光滑水平面上的一条直线上。$P$ 的质量为 $m_P$，$Q$ 为 $m_Q$，$R$ 为 $m_R$。$P$ 以初速度直接朝 $Q$ 投影。在 $P$ 和 $Q$ 碰撞后，$P$ 继续以降低的速度沿相同方向移动。在 $Q$ 和 $R$ 的后续碰撞中，这些粒子结合在一起。求这第二次碰撞后结合体的速度。'
        self.description_arabic = 'تستقر ثلاثة جسيمات $P$ و $Q$ و $R$ في خط مستقيم على مستوى أفقي أملس كما هو موضح في الشكل. كتلة $P$ هي $m_P$، و $Q$ هي $m_Q$، و $R$ هي $m_R$. يُقذف $P$ مباشرة نحو $Q$ بسرعة ابتدائية. بعد اصطدام $P$ و $Q$، يستمر $P$ في التحرك في نفس الاتجاه بسرعة منخفضة. في الاصطدام اللاحق بين $Q$ و $R$، يندمج هذان الجسيمان. أوجد سرعة الجسيم المدمج بعد هذا الاصطدام الثاني.'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक चिकने क्षैतिज तल पर एक सीधी रेखा में तीन कण $P, Q$ और $R$ विराम अवस्था में हैं। $P$ का द्रव्यमान $m_P$ है, $Q$ का $m_Q$ है, और $R$ का $m_R$ है। $P$ को एक प्रारंभिक गति के साथ सीधे $Q$ की ओर प्रक्षेपित किया जाता है। $P$ और $Q$ के टकराने के बाद, $P$ घटी हुई गति के साथ उसी दिशा में आगे बढ़ता रहता है। $Q$ और $R$ के बीच बाद की टक्कर में, ये कण आपस में जुड़ (coalesce) जाते हैं। इस दूसरी टक्कर के बाद संयुक्त कण की गति ज्ञात करें।'
        self.description_kazakh = 'Үш бөлшек $P, Q$ және $R$ суретте көрсетілгендей тегіс көлденең жазықтықта түзу бойында тыныштықта тұр. $P$ массасы $m_P$, $Q$ массасы $m_Q$ және $R$ массасы $m_R$. $P$ тікелей $Q$-ға қарай бастапқы жылдамдықпен лақтырылады. $P$ және $Q$ соқтығысқаннан кейін, $P$ сол бағытта төмендеген жылдамдықпен қозғалуын жалғастырады. $Q$ және $R$ арасындағы келесі соқтығысуда бұл бөлшектер бірігеді. Осы екінші соқтығысудан кейінгі біріккен бөлшектің жылдамдығын табыңыз.'
        self.description_swahili = 'Chembe tatu $P, Q$ na $R$ zipo kwenye utulivu kwenye mstari mnyoofu kwenye bapa laini la ulalo kama inavyoonyeshwa kwenye kielelezo. Tungamo la $P$ ni $m_P$, $Q$ ni $m_Q$, na $R$ ni $m_R$. $P$ inakadiriwa moja kwa moja kuelekea $Q$ kwa mwendokasi wa mwanzo. Baada ya $P$ na $Q$ kugongana, $P$ inaendelea kusonga katika mwelekeo uleule kwa mwendokasi uliopunguzwa. Katika mgongano unaofuata kati ya $Q$ na $R$, chembe hizi zinaungana. Tafuta mwendokasi wa chembe iliyounganishwa baada ya mgongano huu wa pili.'

class Mat174_multi(Mat174):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Berdasarkan gambar tersebut, sebuah balok diletakkan pada bidang miring kasar pada sudut $\\alpha$ terhadap bidang horizontal. Gaya konstan dikerjakan pada balok langsung ke atas bidang miring. Carilah waktu yang dibutuhkan balok tersebut untuk bergerak dari keadaan diam menuju jarak yang ditentukan menuruni bidang miring.'
        self.description_chinese = '根据该图，一个物块被放置在与水平面成 $\alpha$ 角的粗糙斜面上。一个恒定的力沿着斜面向上直接作用于物块。求物块从静止开始沿斜面向下移动指定距离所需的时间。'
        self.description_arabic = 'بناءً على الشكل، يوضع مكعب على مستوى خشن مائل بزاوية $\alpha$ على الأفقي. تُطبق قوة ثابتة على المكعب مباشرة لأعلى المستوى. أوجد الوقت الذي يستغرقه المكعب للتحرك من السكون لمسافة محددة لأسفل المستوى.'
        self.description_hindi = 'चित्र के आधार पर, क्षैतिज से $\\alpha$ कोण पर झुके हुए एक खुरदरे तल (rough plane) पर एक ब्लॉक रखा गया है। ब्लॉक पर सीधे तल के ऊपर की ओर एक निरंतर बल लगाया जाता है। वह समय ज्ञात करें जो ब्लॉक को विराम अवस्था से तल के नीचे निर्दिष्ट दूरी तक जाने में लगता है।'
        self.description_kazakh = 'Суретке сүйенсек, блок көлденеңге $\\alpha$ бұрышымен көлбеу орналасқан кедір-бұдыр жазықтыққа қойылған. Блокқа жазықтық бойымен тікелей жоғары қарай тұрақты күш қолданылады. Блоктың жазықтық бойымен төмен қарай көрсетілген қашықтыққа тыныштық күйінен қозғалуына кететін уақытты табыңыз.'
        self.description_swahili = 'Kulingana na kielelezo, tofali linawekwa kwenye bapa korofi lililoinama kwa pembe $\\alpha$ kwa mhimili wa ulalo. Nguvu thabiti inatumika kwenye tofali moja kwa moja juu ya bapa. Tafuta muda unaochukua kwa tofali kusonga kutoka kwenye utulivu kwa umbali uliobainishwa chini ya bapa.'

class Mat175_multi(Mat175):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram tersebut menunjukkan penampang melintang vertikal $ABC$ dari sebuah perosotan air yang kasar. Seorang pria yang dimodelkan sebagai partikel meluncur turun dari keadaan diam di $A$. Berdasarkan informasi yang diberikan pada gambar, carilah usaha yang dilakukan untuk melawan gaya hambatan saat pria tersebut bergerak dari $B$ ke $C$.'
        self.description_chinese = '图表显示了粗糙水滑梯的垂直横截面 $ABC$。被建模为粒子的男子从 $A$ 处静止滑下。根据图中提供的信息，求当该男子从 $B$ 移动到 $C$ 时克服阻力所做的功。'
        self.description_arabic = 'يوضح المخطط المقطع العرضي الرأسي $ABC$ لمنزلق مائي خشن. ينزلق رجل، يُعتبر جسيمًا، لأسفل من السكون عند $A$. بناءً على المعلومات المقدمة في الشكل، أوجد الشغل المبذول ضد قوة المقاومة أثناء تحرك الرجل من $B$ إلى $C$.'
        self.description_hindi = 'आरेख एक खुरदरी वॉटरस्लाइड का ऊर्ध्वाधर क्रॉस-सेक्शन $ABC$ दिखाता है। एक कण के रूप में प्रतिरूपित एक व्यक्ति $A$ पर विराम अवस्था से नीचे खिसकता है। चित्र में दी गई जानकारी के आधार पर, जब व्यक्ति $B$ से $C$ तक जाता है तो प्रतिरोध बल (resistance force) के विरुद्ध किया गया कार्य (work done) ज्ञात करें।'
        self.description_kazakh = 'Диаграммада кедір-бұдыр су сырғанағының $ABC$ тік қимасы көрсетілген. Бөлшек ретінде модельденген адам $A$ нүктесінен тыныштық күйінен сырғанайды. Суретте берілген ақпаратқа сүйене отырып, адам $B$-дан $C$-ға дейін қозғалған кездегі кедергі күшіне қарсы жасалған жұмысты табыңыз.'
        self.description_swahili = 'Mchoro unaonyesha sehemu ya msalaba wa wima $ABC$ wa slaidi ya maji korofi. Mwanaume aliyeigwa kama chembe anateleza chini kutoka kwenye utulivu katika $A$. Kulingana na taarifa iliyotolewa kwenye kielelezo, tafuta kazi iliyofanywa dhidi ya nguvu ya ukinzani wakati mwanaume anasonga kutoka $B$ hadi $C$.'

class Mat176_multi(Mat176):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Diagram dahan-dan-daun berdampingan (back-to-back stem-and-leaf) menunjukkan nilai tes dari siswa di Kelas A dan Kelas B. Berdasarkan gambar tersebut, hitunglah selisih positif antara nilai median Kelas B dan nilai median Kelas A.'
        self.description_chinese = '背靠背的茎叶图显示了A班和B班学生的考试分数。根据该图，计算B班得分中位数与A班得分中位数之间的正差值。'
        self.description_arabic = 'يوضح مخطط الساق والورقة المزدوج درجات الاختبار للطلاب في الفصل A والفصل B. بناءً على الشكل، احسب الفرق الموجب بين الدرجة الوسيطة للفصل B والدرجة الوسيطة للفصل A.'
        self.description_hindi = 'बैक-टू-बैक स्टेम-एंड-लीफ आरेख (back-to-back stem-and-leaf diagram) कक्षा A और कक्षा B के छात्रों के परीक्षा स्कोर दिखाता है। चित्र के आधार पर, कक्षा B के माध्यिका स्कोर और कक्षा A के माध्यिका स्कोर के बीच धनात्मक अंतर की गणना करें।'
        self.description_kazakh = 'Артқа қарай орналасқан сабақ-жапырақ диаграммасы А сыныбы мен В сыныбы оқушыларының тест балдарын көрсетеді. Суретке сүйене отырып, В сыныбының медианалық балы мен А сыныбының медианалық балы арасындағы оң айырмашылықты есептеңіз.'
        self.description_swahili = 'Mchoro wa shina na jani wa mgongo kwa mgongo unaonyesha alama za mtihani za wanafunzi katika Darasa A na Darasa B. Kulingana na kielelezo, kokotoa tofauti chanya kati ya alama ya mediani ya Darasa B na alama ya mediani ya Darasa A.'

class Mat177_multi(Mat177):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Plot kotak dan kumis (box-and-whisker) merangkum tinggi spesies tanaman tertentu. Berdasarkan gambar tersebut, hitunglah nilai numerik minimum yang harus dicapai oleh tinggi tanaman agar dianggap sebagai pencilan menurut kriteria standar $Q_3 + 1.5 \\times (IQR)$.'
        self.description_chinese = '箱线图总结了特定植物物种的高度。根据该图，计算根据标准 $Q_3 + 1.5 \times (IQR)$ 准则，植物高度必须达到的被视为异常值的最小数值。'
        self.description_arabic = 'يلخص مخطط الصندوق ذو العارضتين ارتفاعات نوع معين من النباتات. بناءً على الشكل، احسب الحد الأدنى للقيمة العددية التي يجب أن يصل إليها ارتفاع النبات لاعتباره قيمة متطرفة وفقًا للمعيار القياسي $Q_3 + 1.5 \times (IQR)$.'
        self.description_hindi = 'बॉक्स-एंड-व्हिस्कर प्लॉट (box-and-whisker plot) एक विशिष्ट पौधे की प्रजाति की ऊँचाई को सारांशित करता है। चित्र के आधार पर, मानक $Q_3 + 1.5 \\times (IQR)$ मानदंड (criterion) के अनुसार एक आउटलेयर (outlier) माने जाने के लिए पौधे की ऊँचाई का न्यूनतम संख्यात्मक मान ज्ञात करें।'
        self.description_kazakh = 'Қорап-мұрт сызбасы өсімдіктердің белгілі бір түрінің биіктіктерін қорытындылайды. Суретке сүйене отырып, өсімдік биіктігі $Q_3 + 1.5 \\times (IQR)$ стандарты бойынша ауытқу (шығарылған мән) деп есептелуі үшін жетуі тиіс минималды сандық мәнді есептеңіз.'
        self.description_swahili = 'Njama ya sanduku-na-masharubu inafupisha vimo vya spishi maalum ya mmea. Kulingana na kielelezo, kokotoa thamani ya chini ya namba ambayo kimo cha mmea lazima kifikie ili kuchukuliwa kama kiashiria nje kulingana na kigezo cha kawaida cha $Q_3 + 1.5 \\times (IQR)$.'

class Mat178_multi(Mat178):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Grafik frekuensi kumulatif menampilkan waktu yang dihabiskan oleh {self.total_students} siswa untuk tugas pekerjaan rumah. Berdasarkan gambar tersebut, estimasikan waktu persentil ke-{self.percentile_rank} untuk distribusi ini.'
        self.description_chinese = f'累积频率图显示了 {self.total_students} 名学生在家庭作业上花费的时间。根据该图，估算该分布的第 {self.percentile_rank} 个百分位时间。'
        self.description_arabic = f'يعرض الرسم البياني التكراري التراكمي الوقت الذي قضاه {self.total_students} طالبًا في أداء واجب منزلي. بناءً على الشكل، قدّر وقت الرتبة المئينية {self.percentile_rank} لهذا التوزيع.'
        self.description_hindi = f'संचयी आवृत्ति ग्राफ़ (cumulative frequency graph) एक होमवर्क असाइनमेंट पर {self.total_students} छात्रों द्वारा बिताए गए समय को प्रदर्शित करता है। चित्र के आधार पर, इस वितरण (distribution) के लिए {self.percentile_rank}वें पर्सेंटाइल (percentile) समय का अनुमान लगाएँ।'
        self.description_kazakh = f'Кумулятивті жиілік графигі {self.total_students} оқушының үй тапсырмасына жұмсаған уақытын көрсетеді. Суретке сүйене отырып, осы үлестірім үшін {self.percentile_rank}-ші процентиль уақытын бағалаңыз.'
        self.description_swahili = f'Grafu ya marudio nyongeza inaonyesha muda uliotumiwa na wanafunzi {self.total_students} kwa kazi ya nyumbani. Kulingana na kielelezo, kadiria muda wa asilimia {self.percentile_rank} kwa mtawanyiko huu.'

class Mat179_multi(Mat179):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Histogram tersebut mengilustrasikan distribusi massa dari himpunan sejumlah {self.total_n} paket di gudang pengiriman. Berdasarkan gambar tersebut, hitunglah kepadatan frekuensi interval kelas terakhir.'
        self.description_chinese = f'直方图说明了配送仓库中一组 {self.total_n} 个包裹的质量分布。根据该图，计算最后一个组距的频率密度。'
        self.description_arabic = f'يوضح المدرج التكراري توزيع كتل مجموعة من {self.total_n} طردًا في مستودع توصيل. بناءً على الشكل، احسب الكثافة التكرارية لفئة الفئة الأخيرة.'
        self.description_hindi = f'हिस्टोग्राम एक डिलीवरी वेयरहाउस में {self.total_n} पार्सलों के सेट के लिए द्रव्यमान (masses) के वितरण को दर्शाता है। चित्र के आधार पर, अंतिम वर्ग अंतराल (class interval) के आवृत्ति घनत्व (frequency density) की गणना करें।'
        self.description_kazakh = f'Гистограмма жеткізу қоймасындағы {self.total_n} сәлемдемелер жиынтығының массаларының үлестірімін бейнелейді. Суретке сүйене отырып, соңғы таптық интервалдың жиілік тығыздығын есептеңіз.'
        self.description_swahili = f'Histogramu inaonyesha mtawanyiko wa tungamo kwa seti ya vifurushi {self.total_n} katika ghala la utoaji. Kulingana na kielelezo, kokotoa wiani wa marudio wa muda wa mwisho wa darasa.'

class Mat180_multi(Mat180):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sekelompok siswa akan didudukkan di deretan kursi yang ditunjukkan pada gambar. Di antara para siswa tersebut terdapat sepasang anak kembar yang tidak boleh duduk bersebelahan. Carilah total kemungkinan cara semua siswa tersebut dapat didudukkan sedemikian rupa sehingga anak kembar tersebut terpisah.'
        self.description_chinese = f'一组学生将坐在图中所示的一排椅子上。学生中有一对双胞胎，他们不能坐在一起。求将所有学生安排入座且这对双胞胎分开的总分配方式数。'
        self.description_arabic = f'يجب إجلاس مجموعة من الطلاب في صف الكراسي الموضح في الشكل. من بين الطلاب يوجد توأم يجب ألا يجلسا بجوار بعضهما البعض. أوجد العدد الإجمالي للطرق المختلفة التي يمكن بها إجلاس جميع الطلاب بحيث يكون التوأم منفصلين.'
        self.description_hindi = f'छात्रों के एक समूह को चित्र में कुर्सियों की पंक्ति में बैठाया जाना है। छात्रों में जुड़वा बच्चों का एक जोड़ा भी है जिन्हें एक-दूसरे के बगल में नहीं बैठना चाहिए। उन सभी छात्रों को अलग-अलग बैठाने के कुल तरीकों की संख्या ज्ञात करें ताकि जुड़वा बच्चे अलग-अलग रहें।'
        self.description_kazakh = f'Суретте көрсетілгендей, оқушылар тобы бір қатар орындықтарға отыруы керек. Оқушылардың арасында бірге отыруға болмайтын бір жұп егіз бар. Егіздер бөлек отыратындай етіп, барлық оқушыларды отырғызудың түрлі тәсілдерінің жалпы санын табыңыз.'
        self.description_swahili = f'Kikundi cha wanafunzi kinapaswa kuketi katika safu ya viti inayoonyeshwa kwenye kielelezo. Kati ya wanafunzi kuna jozi ya mapacha ambao hawapaswi kuketi kando ya kila mmoja. Tafuta jumla ya idadi ya njia tofauti ambazo wanafunzi wote wanaweza kuketi ili mapacha watenganishwe.'

class Mat181_multi(Mat181):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sebuah komite akan dipilih dari kelompok orang yang ditunjukkan pada gambar. Komite tersebut harus terdiri dari tepat {self.req_women} wanita dan {self.req_men} pria. Tentukan jumlah kemungkinan cara komite ini dapat dipilih.'
        self.description_chinese = f'将从图中所示的人群中选出一个委员会。该委员会必须由恰好 {self.req_women} 名女性和 {self.req_men} 名男性组成。确定选择该委员会的不同方式数。'
        self.description_arabic = f'يجب اختيار لجنة من مجموعة الأشخاص الموضحة في الشكل. يجب أن تتكون اللجنة من {self.req_women} نساء و {self.req_men} رجال بالضبط. حدد عدد الطرق المختلفة التي يمكن بها اختيار هذه اللجنة.'
        self.description_hindi = f'चित्र में दिखाए गए लोगों के समूह से एक समिति चुनी जानी है। समिति में ठीक {self.req_women} महिलाएँ और {self.req_men} पुरुष होने चाहिए। इस समिति को चुने जाने के अलग-अलग तरीकों की संख्या निर्धारित करें।'
        self.description_kazakh = f'Комитет суретте көрсетілген адамдар тобынан таңдалуы керек. Комитет құрамында дәл {self.req_women} әйел және {self.req_men} ер адам болуы керек. Бұл комитетті таңдаудың түрлі тәсілдерінің санын анықтаңыз.'
        self.description_swahili = f'Kamati inapaswa kuchaguliwa kutoka kwenye kikundi cha watu wanaoonyeshwa kwenye kielelezo. Kamati lazima iwe na wanawake {self.req_women} na wanaume {self.req_men} kamili. Amua idadi ya njia tofauti ambazo kamati hii inaweza kuchaguliwa.'

class Mat182_multi(Mat182):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Satu set berisi {self.n} ornamen unik sedang disusun dalam garis lurus pada rak pajangan. Dua ornamen tertentu, yang ditunjukkan oleh label berwarna pada gambar, harus selalu diletakkan berdampingan. Tentukan total kemungkinan cara ornamen-ornamen tersebut dapat disusun.'
        self.description_chinese = f'一组 {self.n} 个独特的装饰品被排列在展示架上的直线上。图中彩色标签指示的两个特定装饰品必须始终并排放置。确定排列这些装饰品的不同方式总数。'
        self.description_arabic = f'يتم ترتيب مجموعة من {self.n} من الحلي الفريدة في خط مستقيم على رف عرض. يجب دائمًا وضع حليتين محددتين، يُشار إليهما بالملصقات الملونة في الشكل، جنبًا إلى جنب. حدد العدد الإجمالي للطرق المختلفة التي يمكن بها ترتيب الحلي.'
        self.description_hindi = f'{self.n} अद्वितीय आभूषणों के एक सेट को डिस्प्ले शेल्फ पर एक सीधी रेखा में व्यवस्थित किया जा रहा है। चित्र में रंगीन लेबलों द्वारा इंगित दो विशिष्ट आभूषणों को हमेशा अगल-बगल (side-by-side) रखा जाना चाहिए। आभूषणों को व्यवस्थित करने के कुल अलग-अलग तरीकों की संख्या निर्धारित करें।'
        self.description_kazakh = f'{self.n} бірегей әшекейлер жиынтығы көрме сөресінде бір қатарға орналастырылады. Суреттегі түрлі-түсті белгілермен көрсетілген екі нақты әшекей әрқашан қатар қойылуы керек. Әшекейлерді орналастырудың түрлі тәсілдерінің жалпы санын анықтаңыз.'
        self.description_swahili = f'Seti ya mapambo ya kipekee {self.n} yanapangwa kwenye mstari mnyoofu kwenye rafu ya onyesho. Mapambo mawili maalum, yaliyoonyeshwa na lebo za rangi kwenye kielelezo, lazima kila wakati yawekwe kando ya kila mmoja. Amua jumla ya idadi ya njia tofauti ambazo mapambo yanaweza kupangwa.'

class Mat183_multi(Mat183):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Sekelompok anggota dewan, termasuk seorang Ketua dan seorang Sekretaris, sedang mengadakan pertemuan di meja panjang yang ditunjukkan pada gambar. Untuk pertemuan spesifik ini, Ketua dan Sekretaris harus duduk di kursi yang bersebelahan. Hitunglah total kemungkinan cara anggota-anggota dewan tersebut dapat duduk.'
        self.description_chinese = '包括主席和秘书在内的一组董事会成员正在图中所示的长桌旁开会。在本次特定会议上，主席和秘书必须坐在相邻的座位上。计算这些成员入座的不同方式总数。'
        self.description_arabic = 'تجمتمع مجموعة من أعضاء مجلس الإدارة، بما في ذلك رئيس وسكرتير، على الطاولة الطويلة الموضحة في الشكل. بالنسبة لهذا الاجتماع المحدد، يجب أن يجلس الرئيس والسكرتير في مقعدين متجاورين. احسب العدد الإجمالي للطرق المختلفة التي يمكن للأعضاء الجلوس بها.'
        self.description_hindi = 'अध्यक्ष (Chairperson) और सचिव (Secretary) सहित बोर्ड के सदस्यों का एक समूह चित्र में दिखाई गई लंबी मेज पर बैठक कर रहा है। इस विशिष्ट बैठक के लिए, अध्यक्ष और सचिव को आसन्न सीटों (adjacent seats) पर बैठना चाहिए। सदस्यों को बैठाने के कुल अलग-अलग तरीकों की संख्या की गणना करें।'
        self.description_kazakh = 'Суретте көрсетілгендей, Төраға мен Хатшыны қоса алғанда, басқарма мүшелерінің тобы ұзын үстел басында жиналыс өткізуде. Осы нақты жиналыс үшін Төраға мен Хатшы қатарлас орындарда отыруы керек. Мүшелерді отырғызудың түрлі тәсілдерінің жалпы санын есептеңіз.'
        self.description_swahili = 'Kikundi cha wajumbe wa bodi, ikiwa ni pamoja na Mwenyekiti na Katibu, wanakutana kwenye meza ndefu inayoonyeshwa kwenye kielelezo. Kwa mkutano huu maalum, Mwenyekiti na Katibu lazima waketi kwenye viti vilivyo karibu. Kokotoa jumla ya idadi ya njia tofauti ambazo wajumbe wanaweza kuketi.'

class Mat184_multi(Mat184):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menampilkan fungsi massa probabilitas (PMF) dari variabel acak diskret $X$. Berdasarkan tinggi segmen yang ditunjukkan, hitunglah variansi $Var(X)$.'
        self.description_chinese = '图中显示了离散随机变量 $X$ 的概率质量函数。根据显示的线段高度，计算方差 $Var(X)$。'
        self.description_arabic = 'يعرض الشكل دالة الكتلة الاحتمالية لمتغير عشوائي منفصل $X$. بناءً على ارتفاعات المقاطع الموضحة، احسب التباين $Var(X)$.'
        self.description_hindi = 'चित्र एक असतत यादृच्छिक चर (discrete random variable) $X$ का प्रायिकता द्रव्यमान फलन (probability mass function) प्रदर्शित करता है। दिखाए गए खंडों (segments) की ऊँचाई के आधार पर, प्रसरण (variance) $Var(X)$ की गणना करें।'
        self.description_kazakh = 'Суретте $X$ дискретті кездейсоқ шамасының ықтималдық массасының функциясы көрсетілген. Көрсетілген сегменттердің биіктіктеріне сүйене отырып, $Var(X)$ дисперсиясын есептеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha utendakazi wa tungamo la uwezekano wa kigeugeu kinachojitegemea na kinachobadilika cha $X$. Kulingana na vimo vya pingili zilizoonyeshwa, kokotoa variansi $Var(X)$.'

class Mat185_multi(Mat185):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Variabel acak diskret $X$ merepresentasikan skor pada jarum pemutar persegi berbobot yang ditunjukkan pada gambar. Jika jarum pemutar diputar satu kali, carilah nilai harapan $E(X)$.'
        self.description_chinese = '离散随机变量 $X$ 代表图中所示的加权四面转盘上的分数。如果转动一次转盘，求期望值 $E(X)$。'
        self.description_arabic = 'يمثل متغير عشوائي منفصل $X$ الدرجة على القرص الدوار المرجح ذي الجوانب الأربعة الموضح في الشكل. إذا تم تدوير القرص الدوار مرة واحدة، فأوجد القيمة المتوقعة $E(X)$.'
        self.description_hindi = 'एक असतत यादृच्छिक चर $X$ चित्र में दिखाए गए भारित चार-तरफा स्पिनर (weighted four-sided spinner) पर स्कोर को दर्शाता है। यदि स्पिनर को एक बार घुमाया जाता है, तो अपेक्षित मान (expected value) $E(X)$ ज्ञात करें।'
        self.description_kazakh = '$X$ дискретті кездейсоқ шамасы суретте көрсетілген салмақталған төрт қырлы айналдырғыштағы ұпайды білдіреді. Егер айналдырғыш бір рет айналдырылса, күтілетін $E(X)$ мәнін табыңыз.'
        self.description_swahili = 'Kigeugeu kinachojitegemea na kinachobadilika cha $X$ kinawakilisha alama kwenye gurudumu lenye pande nne lililopimwa linaloonyeshwa kwenye kielelezo. Ikiwa gurudumu litazungushwa mara moja, tafuta thamani inayotarajiwa $E(X)$.'

class Mat186_multi(Mat186):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Variabel acak diskret $X$ mengikuti distribusi geometri $X \\sim \\text{{Geo}}(p)$. Gambar tersebut menunjukkan fungsi massa probabilitas untuk beberapa nilai pertama dari $x$. Berdasarkan gambar tersebut, tentukan nilai $p$ sebagai desimal.'
        self.description_chinese = f'离散随机变量 $X$ 服从几何分布 $X \sim \text{{Geo}}(p)$。图中显示了前几个 $x$ 值的概率质量函数。根据该图，确定 $p$ 的值（以小数表示）。'
        self.description_arabic = f'يتبع متغير عشوائي منفصل $X$ توزيعًا هندسيًا $X \sim \text{{Geo}}(p)$. يوضح الشكل دالة الكتلة الاحتمالية للقيم القليلة الأولى لـ $x$. بناءً على الشكل، حدد قيمة $p$ كعدد عشري.'
        self.description_hindi = f'एक असतत यादृच्छिक चर $X$ एक ज्यामितीय वितरण (geometric distribution) $X \\sim \\text{{Geo}}(p)$ का अनुसरण करता है। चित्र $x$ के पहले कुछ मानों के लिए प्रायिकता द्रव्यमान फलन दिखाता है। चित्र के आधार पर, दशमलव के रूप में $p$ का मान निर्धारित करें।'
        self.description_kazakh = f'$X$ дискретті кездейсоқ шамасы геометриялық үлестірімге $X \\sim \\text{{Geo}}(p)$ бағынады. Суретте $x$-тің алғашқы бірнеше мәніне арналған ықтималдық массасының функциясы көрсетілген. Суретке сүйене отырып, $p$ мәнін ондық бөлшек түрінде анықтаңыз.'
        self.description_swahili = f'Kigeugeu kinachojitegemea na kinachobadilika cha $X$ kinafuata mtawanyiko wa kijiometri $X \\sim \\text{{Geo}}(p)$. Kielelezo kinaonyesha utendakazi wa tungamo la uwezekano kwa thamani chache za kwanza za $x$. Kulingana na kielelezo, amua thamani ya $p$ kama desimali.'

class Mat187_multi(Mat187):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Histogram tersebut menunjukkan distribusi probabilitas dari variabel acak diskret $W$ di mana $W \\sim B(n, p)$. Berdasarkan tinggi batang yang ditunjukkan pada gambar, carilah nilai numerik dari probabilitas keberhasilan $p$.'
        self.description_chinese = f'直方图显示了离散随机变量 $W$ 的概率分布，其中 $W \sim B(n, p)$。根据图中条形图的高度，求成功概率 $p$ 的数值。'
        self.description_arabic = f'يوضح المدرج التكراري التوزيع الاحتمالي لمتغير عشوائي منفصل $W$ حيث $W \sim B(n, p)$. بناءً على ارتفاعات الأشرطة الموضحة في الشكل، أوجد القيمة العددية لاحتمال النجاح $p$.'
        self.description_hindi = f'हिस्टोग्राम एक असतत यादृच्छिक चर $W$ का प्रायिकता वितरण दिखाता है जहाँ $W \\sim B(n, p)$ है। चित्र में दिखाए गए बार (bars) की ऊँचाई के आधार पर, सफलता की प्रायिकता (success probability) $p$ का संख्यात्मक मान ज्ञात करें।'
        self.description_kazakh = f'Гистограмма $W \\sim B(n, p)$ болатын $W$ дискретті кездейсоқ шамасының ықтималдық үлестірімін көрсетеді. Суретте көрсетілген бағандардың биіктіктеріне сүйене отырып, $p$ сәттілік ықтималдығының сандық мәнін табыңыз.'
        self.description_swahili = f'Histogramu inaonyesha mtawanyiko wa uwezekano wa kigeugeu kinachojitegemea na kinachobadilika cha $W$ ambapo $W \\sim B(n, p)$. Kulingana na vimo vya miambaa inayoonyeshwa kwenye kielelezo, tafuta thamani ya namba ya uwezekano wa kufaulu $p$.'

class Mat188_multi(Mat188):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut mengilustrasikan variabel acak kontinu $X$ yang mengikuti distribusi normal. Berdasarkan parameter dan daerah yang diarsir yang ditunjukkan pada diagram, hitunglah nilai dari probabilitas yang diindikasikan.'
        self.description_chinese = '图示为服从正态分布的连续随机变量 $X$。根据图中的参数和阴影区域，计算所示概率的值。'
        self.description_arabic = 'يوضح الشكل متغيرًا عشوائيًا متصلاً $X$ يتبع توزيعًا طبيعيًا. بناءً على المعلمات والمنطقة المظللة الموضحة في المخطط، احسب قيمة الاحتمال المشار إليه.'
        self.description_hindi = 'चित्र एक सतत यादृच्छिक चर (continuous random variable) $X$ को दर्शाता है जो एक सामान्य वितरण (normal distribution) का अनुसरण करता है। मापदंडों (parameters) और आरेख में दिखाए गए छायांकित क्षेत्र के आधार पर, इंगित प्रायिकता (probability) के मान की गणना करें।'
        self.description_kazakh = 'Суретте қалыпты үлестірімге бағынатын $X$ үзіліссіз кездейсоқ шамасы бейнеленген. Параметрлерге және диаграммада көрсетілген боялған аймаққа сүйене отырып, көрсетілген ықтималдықтың мәнін есептеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha kigeugeu endelevu kisichojitegemea cha $X$ kinachofuata mtawanyiko wa kawaida. Kulingana na vigezo na kanda iliyowekwa kivuli inayoonyeshwa kwenye mchoro, kokotoa thamani ya uwezekano ulioonyeshwa.'

class Mat189_multi(Mat189):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Variabel acak $X$ mengikuti distribusi normal dengan nilai rata-rata (mean) yang ditunjukkan pada gambar. Mengingat probabilitas direpresentasikan oleh area yang diarsir, hitunglah nilai deviasi standar $\\sigma$.'
        self.description_chinese = '随机变量 $X$ 服从正态分布，其均值如图所示。已知阴影区域代表的概率，计算标准差 $\sigma$ 的值。'
        self.description_arabic = 'يتبع متغير عشوائي $X$ توزيعًا طبيعيًا بالمتوسط الموضح في الشكل. نظرًا للاحتمال الذي تمثله المنطقة المظللة، احسب قيمة الانحراف المعياري $\sigma$.'
        self.description_hindi = 'एक यादृच्छिक चर $X$ चित्र में दिखाए गए माध्य (mean) के साथ एक सामान्य वितरण का अनुसरण करता है। छायांकित क्षेत्र द्वारा दर्शायी गई प्रायिकता को देखते हुए, मानक विचलन (standard deviation) $\\sigma$ के मान की गणना करें।'
        self.description_kazakh = '$X$ кездейсоқ шамасы суретте көрсетілген орташа мәнмен қалыпты үлестірімге бағынады. Боялған аймақпен берілген ықтималдықты ескере отырып, $\\sigma$ стандартты ауытқуының мәнін есептеңіз.'
        self.description_swahili = 'Kigeugeu kinachojitegemea cha $X$ kinafuata mtawanyiko wa kawaida na wastani unaoonyeshwa kwenye kielelezo. Kwa kuzingatia uwezekano unaowakilishwa na eneo lililowekwa kivuli, kokotoa thamani ya mkengeuko wa kawaida $\\sigma$.'

class Mat190_multi(Mat190):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan suatu distribusi normal di mana daerah yang diarsir merepresentasikan probabilitas spesifik. Berdasarkan nilai batas pada daerah yang diarsir dan varians dari distribusinya, carilah nilai rata-ratanya $\\mu$.'
        self.description_chinese = '图中显示了一个正态分布，其中阴影区域代表特定概率。根据阴影区域的边界值和分布的方差，求均值 $\mu$ 的值。'
        self.description_arabic = 'يوضح الشكل توزيعًا طبيعيًا حيث تمثل المنطقة المظللة احتمالًا محددًا. بناءً على القيم الحدودية للمنطقة المظللة وتباين التوزيع، أوجد قيمة المتوسط $\mu$.'
        self.description_hindi = 'चित्र एक सामान्य वितरण दिखाता है जहाँ छायांकित क्षेत्र एक विशिष्ट प्रायिकता का प्रतिनिधित्व करता है। छायांकित क्षेत्र के सीमा मानों (boundary values) और वितरण के प्रसरण (variance) के आधार पर, माध्य $\\mu$ का मान ज्ञात करें।'
        self.description_kazakh = 'Суретте боялған аймақ белгілі бір ықтималдықты білдіретін қалыпты үлестірім көрсетілген. Боялған аймақтың шекаралық мәндеріне және үлестірімнің дисперсиясына сүйене отырып, $\\mu$ орташа мәнін табыңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha mtawanyiko wa kawaida ambapo kanda iliyowekwa kivuli inawakilisha uwezekano mahususi. Kulingana na thamani za mpaka za eneo lililowekwa kivuli na variansi ya mtawanyiko, tafuta thamani ya wastani $\\mu$.'

class Mat191_multi(Mat191):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar tersebut mengilustrasikan fungsi kepadatan probabilitas (PDF) dari sampel rata-rata $\\overline{{X}}$ untuk ukuran sampel $n = {self.n}$ yang diambil dari populasi berdistribusi normal dengan rata-rata $\\mu$ dan varians $\\sigma^2$. Berdasarkan parameter yang ditunjukkan pada gambar, hitunglah standar deviasi populasinya, $\\sigma$.'
        self.description_chinese = f'图中说明了从均值为 $\mu$、方差为 $\sigma^2$ 的正态分布总体中抽取样本量为 $n = {self.n}$ 的样本均值 $\overline{{X}}$ 的概率密度函数。根据图中显示的参数，计算总体的标准差 $\sigma$。'
        self.description_arabic = f'يوضح الشكل دالة كثافة الاحتمال لمتوسط العينة $\overline{{X}}$ لعينات بحجم $n = {self.n}$ مأخوذة من مجتمع موزع توزيعًا طبيعيًا بمتوسط $\mu$ وتباين $\sigma^2$. بناءً على المعلمات الموضحة في الشكل، احسب الانحراف المعياري للمجتمع، $\sigma$.'
        self.description_hindi = f'चित्र माध्य $\\mu$ और प्रसरण $\\sigma^2$ वाले सामान्य रूप से वितरित जनसंख्या से लिए गए आकार $n = {self.n}$ के नमूनों के लिए नमूना माध्य (sample mean) $\\overline{{X}}$ के प्रायिकता घनत्व फलन (probability density function) को दर्शाता है। चित्र में दिखाए गए मापदंडों के आधार पर, जनसंख्या के मानक विचलन, $\\sigma$ की गणना करें।'
        self.description_kazakh = f'Суретте орташа мәні $\\mu$ және дисперсиясы $\\sigma^2$ қалыпты үлестірілген популяциядан алынған көлемі $n = {self.n}$ таңдамалар үшін $\\overline{{X}}$ таңдамалық орташа мәннің ықтималдық тығыздығы функциясы бейнеленген. Суретте көрсетілген параметрлерге сүйене отырып, популяцияның стандартты ауытқуын, $\\sigma$, есептеңіз.'
        self.description_swahili = f'Kielelezo kinaonyesha utendakazi wa wiani wa uwezekano wa wastani wa sampuli $\\overline{{X}}$ kwa sampuli za ukubwa $n = {self.n}$ zilizochukuliwa kutoka kwenye idadi iliyosambazwa kawaida yenye wastani $\\mu$ na variansi $\\sigma^2$. Kulingana na vigezo vilivyoonyeshwa kwenye kielelezo, kokotoa mkengeuko wa kawaida wa idadi, $\\sigma$.'

class Mat192_multi(Mat192):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Plot titik tersebut menunjukkan ukuran rentang sayap (dalam cm) dari sampel acak sekelompok burung. Berdasarkan data visual yang diberikan pada gambar, hitunglah taksiran tak bias untuk varians populasi ($s^2$).'
        self.description_chinese = '点图显示了鸟类随机样本的翼展测量值（以厘米为单位）。根据图中提供的视觉数据，计算总体方差的无偏估计（$s^2$）。'
        self.description_arabic = 'يوضح المخطط النقطي قياسات طول جناحي طيور (بالسنتيمتر) لعينة عشوائية من الطيور. بناءً على البيانات المرئية المقدمة في الشكل، احسب التقدير غير المتحيز لتباين المجتمع ($s^2$).'
        self.description_hindi = 'डॉट प्लॉट (dot plot) पक्षियों के एक यादृच्छिक नमूने के पंखों के फैलाव (wingspan) का माप (cm में) दिखाता है। चित्र में दिए गए दृश्य डेटा (visual data) के आधार पर, जनसंख्या प्रसरण के निष्पक्ष अनुमान (unbiased estimate) ($s^2$) की गणना करें।'
        self.description_kazakh = 'Нүктелік график құстардың кездейсоқ таңдамасының қанат құлашын (см-мен) өлшеуді көрсетеді. Суретте берілген визуалды деректерге сүйене отырып, популяция дисперсиясының ығыспаған бағалауын ($s^2$) есептеңіз.'
        self.description_swahili = 'Njama ya nukta inaonyesha vipimo vya upana wa mabawa (katika cm) ya sampuli isiyojitegemea ya ndege. Kulingana na data ya kuona iliyotolewa kwenye kielelezo, kokotoa makadirio yasiyo na upendeleo ya variansi ya idadi ($s^2$).'

class Mat193_multi(Mat193):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan distribusi suatu populasi dan distribusi sampling rata-rata sampel $\\overline{X}$ yang bersesuaian untuk ukuran sampel $n$. Berdasarkan parameter statistik yang diberikan pada gambar, tentukan nilai ukuran sampel $n$.'
        self.description_chinese = '图中显示了总体的分布以及对应的样本量为 $n$ 的样本均值 $\overline{X}$ 的抽样分布。根据图中提供的统计参数，确定样本量 $n$ 的值。'
        self.description_arabic = 'يوضح الشكل توزيع مجتمع إحصائي وتوزيع المعاينة المقابل لمتوسط العينة $\overline{X}$ لعينات بحجم $n$. بناءً على المعلمات الإحصائية المقدمة في الشكل، حدد قيمة حجم العينة $n$.'
        self.description_hindi = 'चित्र एक जनसंख्या के वितरण और नमूना आकार $n$ के लिए नमूना माध्य $\\overline{X}$ के संबंधित नमूना वितरण (sampling distribution) को दिखाता है। चित्र में दिए गए सांख्यिकीय मापदंडों के आधार पर, नमूना आकार $n$ का मान निर्धारित करें।'
        self.description_kazakh = 'Суретте $X$ популяциясының үлестірімі және көлемі $n$ болатын таңдамалар үшін $\\overline{X}$ таңдамалық орташа мәнінің сәйкес таңдамалық үлестірімі көрсетілген. Суретте берілген статистикалық параметрлерге сүйене отырып, $n$ таңдама көлемінің мәнін анықтаңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha mtawanyiko wa idadi na mtawanyiko unaofanana wa sampuli wa wastani wa sampuli $\\overline{X}$ kwa sampuli za ukubwa $n$. Kulingana na vigezo vya takwimu vilivyotolewa kwenye kielelezo, amua thamani ya ukubwa wa sampuli $n$.'

class Mat194_multi(Mat194):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan distribusi normal standar yang digunakan untuk menentukan nilai kritis $z$ dari suatu interval kepercayaan (confidence interval). Berdasarkan daerah yang ditandai pada ekor yang diarsir, hitunglah tingkat kepercayaan dari interval tersebut dalam persentase.'
        self.description_chinese = '图中显示了用于确定置信区间临界值 $z$ 的标准正态分布。根据阴影尾部的指示面积，计算置信区间的置信水平（以百分比表示）。'
        self.description_arabic = 'يوضح الشكل توزيعًا طبيعيًا قياسيًا يُستخدم لتحديد القيمة الحرجة $z$ لفترة ثقة. بناءً على المساحة المشار إليها في الأطراف المظللة، احسب مستوى الثقة للفترة كنسبة مئوية.'
        self.description_hindi = 'चित्र एक विश्वास अंतराल (confidence interval) के लिए महत्वपूर्ण मान (critical value) $z$ निर्धारित करने के लिए उपयोग किया जाने वाला एक मानक सामान्य वितरण (standard normal distribution) दिखाता है। छायांकित पूंछ (shaded tails) में इंगित क्षेत्र के आधार पर, प्रतिशत के रूप में अंतराल के विश्वास स्तर (confidence level) की गणना करें।'
        self.description_kazakh = 'Суретте сенімділік интервалы үшін $z$ критикалық мәнін анықтау үшін қолданылатын стандартты қалыпты үлестірім көрсетілген. Боялған құйрықтардағы көрсетілген ауданға сүйене отырып, интервалдың сенімділік деңгейін пайызбен есептеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mtawanyiko wa kawaida wa kawaida unaotumiwa kuamua thamani muhimu $z$ kwa kipindi cha uhakika. Kulingana na eneo lililoonyeshwa kwenye mikia iliyowekwa kivuli, kokotoa kiwango cha uhakika cha muda kama asilimia.'

class Mat195_multi(Mat195):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Sebuah interval kepercayaan untuk rata-rata tinggi spesies tanaman dihitung dari ukuran sampel yang besar. Berdasarkan kurva distribusi normal dan interval yang ditunjukkan pada gambar, carilah nilai rata-rata sampel $\\overline{x}$ yang digunakan untuk menyusun interval ini.'
        self.description_chinese = '某植物物种平均高度的置信区间是通过大样本计算得出的。根据正态分布曲线和图中所示的区间，求用于构造此区间的样本均值 $\overline{x}$。'
        self.description_arabic = 'تم حساب فترة ثقة لمتوسط ارتفاع نوع من النباتات من عينة كبيرة. بناءً على منحنى التوزيع الطبيعي والفترة الموضحة في الشكل، أوجد متوسط العينة $\overline{x}$ المستخدم لإنشاء هذه الفترة.'
        self.description_hindi = 'एक बड़े नमूने से पौधे की प्रजातियों की माध्य ऊँचाई के लिए एक विश्वास अंतराल की गणना की गई थी। चित्र में दिखाए गए सामान्य वितरण वक्र और अंतराल के आधार पर, इस अंतराल के निर्माण के लिए उपयोग किए गए नमूना माध्य $\\overline{x}$ को ज्ञात करें।'
        self.description_kazakh = 'Өсімдік түрлерінің орташа биіктігіне арналған сенімділік интервалы үлкен таңдамадан есептелді. Суретте көрсетілген қалыпты үлестірім қисығына және интервалға сүйене отырып, осы интервалды құру үшін пайдаланылған $\\overline{x}$ таңдамалық орташа мәнін табыңыз.'
        self.description_swahili = 'Muda wa uhakika wa wastani wa kimo cha spishi ya mmea ulikokotolewa kutoka kwenye sampuli kubwa. Kulingana na mzingo wa mtawanyiko wa kawaida na muda unaoonyeshwa kwenye kielelezo, tafuta wastani wa sampuli $\\overline{x}$ uliotumiwa kujenga muda huu.'

class Mat196_multi(Mat196):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan area di bawah kurva normal standar yang digunakan untuk interval kepercayaan (confidence interval) tertentu. Berdasarkan area yang diarsir dan standard error (SE) yang diberikan, hitunglah lebar dari interval kepercayaan untuk rata-rata populasi $\\mu$.'
        self.description_chinese = '图中显示了用于特定置信区间的标准正态曲线下的面积。根据阴影区域和给定的标准误（SE），计算总体均值 $\mu$ 的置信区间的宽度。'
        self.description_arabic = 'يوضح الشكل المساحات تحت المنحنى الطبيعي القياسي المستخدمة لفترة ثقة محددة. بناءً على المساحة المظللة والخطأ المعياري (SE) المعطى، احسب عرض فترة الثقة لمتوسط المجتمع $\mu$.'
        self.description_hindi = 'चित्र एक विशिष्ट विश्वास अंतराल के लिए मानक सामान्य वक्र के अंतर्गत क्षेत्रों को दिखाता है। छायांकित क्षेत्र और दी गई मानक त्रुटि (standard error / SE) के आधार पर, जनसंख्या माध्य $\\mu$ के लिए विश्वास अंतराल की चौड़ाई की गणना करें।'
        self.description_kazakh = 'Суретте белгілі бір сенімділік интервалы үшін қолданылатын стандартты қалыпты қисық астындағы аудандар көрсетілген. Боялған аймақ пен берілген стандартты қателікке (SE) сүйене отырып, $\\mu$ популяциялық орташа мәні үшін сенімділік интервалының енін есептеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha maeneo chini ya mzingo wa kawaida wa kawaida uliotumiwa kwa muda mahususi wa uhakika. Kulingana na eneo lililowekwa kivuli na hitilafu ya kawaida iliyotolewa (SE), kokotoa upana wa muda wa uhakika wa wastani wa idadi $\\mu$.'

class Mat197_multi(Mat197):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut menunjukkan dua distribusi sampling, $A$ dan $B$, untuk nilai rata-rata populasi yang sama tetapi dengan ukuran sampel yang berbeda, $n_A$ dan $n_B$. Berdasarkan hubungan yang ditunjukkan dan parameter di legendanya, hitunglah nilai $n_B$.'
        self.description_chinese = '图中显示了针对同一总体均值但样本量不同的两个抽样分布 $A$ 和 $B$（样本量分别为 $n_A$ 和 $n_B$）。根据图中显示的关系和图例中的参数，计算 $n_B$ 的值。'
        self.description_arabic = 'يوضح الشكل توزيعي معاينة، $A$ و $B$، لنفس متوسط المجتمع ولكن بأحجام عينات مختلفة، $n_A$ و $n_B$. بناءً على العلاقة الموضحة والمعلمات الموجودة في وسيلة الإيضاح، احسب قيمة $n_B$.'
        self.description_hindi = 'चित्र एक ही जनसंख्या माध्य के लिए दो नमूना वितरण, $A$ और $B$, लेकिन अलग-अलग नमूना आकार, $n_A$ और $n_B$ दिखाता है। दिखाए गए संबंध और लेजेंड में मापदंडों के आधार पर, $n_B$ के मान की गणना करें।'
        self.description_kazakh = 'Суретте бірдей популяциялық орташа мән үшін, бірақ әртүрлі $n_A$ және $n_B$ таңдама көлемдері бар $A$ және $B$ екі таңдамалық үлестірімі көрсетілген. Көрсетілген қатынасқа және аңыздағы (легендадағы) параметрлерге сүйене отырып, $n_B$ мәнін есептеңіз.'
        self.description_swahili = 'Kielelezo kinaonyesha mitawanyiko miwili ya sampuli, $A$ na $B$, kwa wastani sawa wa idadi lakini yenye ukubwa tofauti wa sampuli, $n_A$ na $n_B$. Kulingana na uhusiano unaoonyeshwa na vigezo kwenye hadithi, kokotoa thamani ya $n_B$.'

class Mat198_multi(Mat198):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut mengilustrasikan hubungan antara batas kesalahan matematis ($E$) dan ukuran sampel ($n$) dari hasil sebuah survei. Berdasarkan parameter yang diberikan pada legenda gambar dan titik yang ditandai pada kurva, tentukan ukuran sampel yang diperlukan, $n$.'
        self.description_chinese = '图示说明了调查结果的误差幅度（$E$）与样本量（$n$）之间的关系。根据图例中提供的参数和曲线上的标记点，确定所需的样本量 $n$。'
        self.description_arabic = 'يوضح الشكل العلاقة بين هامش الخطأ ($E$) وحجم العينة ($n$) لنتيجة استطلاع. بناءً على المعلمات المقدمة في وسيلة إيضاح الشكل والنقطة المحددة على المنحنى، حدد حجم العينة المطلوب $n$.'
        self.description_hindi = 'चित्र सर्वेक्षण परिणाम के लिए त्रुटि के मार्जिन (margin of error / $E$) और नमूना आकार ($n$) के बीच संबंध को दर्शाता है। चित्र लेजेंड में दिए गए मापदंडों और वक्र पर चिह्नित बिंदु के आधार पर, आवश्यक नमूना आकार $n$ निर्धारित करें।'
        self.description_kazakh = 'Суретте сауалнама нәтижесі үшін қателік шегі ($E$) мен таңдама көлемі ($n$) арасындағы байланыс бейнеленген. Сурет аңызында (легендасында) берілген параметрлерге және қисықтағы белгіленген нүктеге сүйене отырып, қажетті $n$ таңдама көлемін анықтаңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha uhusiano kati ya ukingo wa hitilafu ($E$) na ukubwa wa sampuli ($n$) kwa matokeo ya utafiti. Kulingana na vigezo vilivyotolewa kwenye hadithi ya kielelezo na nukta iliyowekwa alama kwenye mzingo, amua ukubwa unaohitajika wa sampuli $n$.'

class Mat199_multi(Mat199):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Dua sampel independen diambil dari populasi yang sama. Berdasarkan plot kotak (boxplots) dan ukuran sampel yang diberikan pada legenda gambar, hitunglah taksiran tak bias dari rata-rata populasi dengan menggabungkan semua pengamatannya.'
        self.description_chinese = '从同一总体中抽取两个独立样本。根据图例中提供的箱线图和样本量，通过组合所有观察值计算总体均值的无偏估计。'
        self.description_arabic = 'يتم أخذ عينتين مستقلتين من نفس المجتمع. بناءً على مخططات الصندوق وأحجام العينات المقدمة في وسيلة إيضاح الشكل، احسب التقدير غير المتحيز لمتوسط المجتمع من خلال دمج جميع الملاحظات.'
        self.description_hindi = 'एक ही जनसंख्या से दो स्वतंत्र नमूने (independent samples) लिए गए हैं। चित्र लेजेंड में दिए गए बॉक्सप्लॉट और नमूना आकार के आधार पर, सभी अवलोकनों (observations) को मिलाकर जनसंख्या माध्य के निष्पक्ष अनुमान की गणना करें।'
        self.description_kazakh = 'Бір популяциядан екі тәуелсіз таңдама алынды. Қорап-мұрт сызбаларына және сурет аңызында (легендасында) берілген таңдама көлемдеріне сүйене отырып, барлық бақылауларды біріктіре отырып, популяциялық орташа мәннің ығыспаған бағалауын есептеңіз.'
        self.description_swahili = 'Sampuli mbili zinazojitegemea zinachukuliwa kutoka kwenye idadi sawa. Kulingana na njama za sanduku na ukubwa wa sampuli zilizotolewa kwenye hadithi ya kielelezo, kokotoa makadirio yasiyo na upendeleo ya wastani wa idadi kwa kuchanganya uchunguzi wote.'

class Mat200_multi(Mat200):
    def __init__(self):
        super().__init__()
        self.description_indonesian = "Sebuah survei dilakukan dengan ukuran sampel yang besar. Diagram batang frekuensi mengilustrasikan hitungan dari hasil 'sukses' dan 'gagal'. Berdasarkan gambar tersebut, hitunglah taksiran titik tak bias untuk proporsi populasi $p$."
        self.description_chinese = "进行了一项大样本调查。频率条形图说明了“成功”和“失败”结果的计数。根据该图，计算总体比例 $p$ 的无偏点估计。"
        self.description_arabic = "تم إجراء استطلاع بحجم عينة كبير. يوضح المخطط الشريطي التكراري عدد نتائج 'النجاح' و 'الفشل'. بناءً على الشكل، احسب تقدير النقطة غير المتحيز لنسبة المجتمع $p$."
        self.description_hindi = "एक बड़े नमूना आकार के साथ एक सर्वेक्षण किया गया था। आवृत्ति बार चार्ट (frequency bar chart) 'सफलता' और 'विफलता' परिणामों की गिनती को दर्शाता है। चित्र के आधार पर, जनसंख्या अनुपात (population proportion) $p$ के लिए निष्पक्ष बिंदु अनुमान (unbiased point estimate) की गणना करें।"
        self.description_kazakh = "Сауалнама үлкен таңдама көлемімен жүргізілді. Жиіліктердің бағандық диаграммасы 'сәттілік' және 'сәтсіздік' нәтижелерінің санын бейнелейді. Суретке сүйене отырып, $p$ популяциялық пропорциясы үшін ығыспаған нүктелік бағалауды есептеңіз."
        self.description_swahili = "Utafiti ulifanywa ukiwa na ukubwa mkubwa wa sampuli. Chati ya mwambaa wa marudio inaonyesha hesabu ya matokeo ya 'kufaulu' na 'kushindwa'. Kulingana na kielelezo, kokotoa makadirio yasiyo na upendeleo ya nukta kwa uwiano wa idadi $p$."

class Mat201_multi(Mat201):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Gambar tersebut mengilustrasikan distribusi sebuah populasi $X$ dan distribusi dari rata-rata sampel $\\bar{X}$ untuk ukuran sampel $n = ' + str(self.n) + '$. Berdasarkan sifat-sifat statistik yang ditunjukkan, tentukan nilai dari $E(\\bar{X})$.'
        self.description_chinese = '图中说明了总体 $X$ 的分布以及样本量为 $n = ' + str(self.n) + '$ 的样本均值 $\bar{X}$ 的分布。根据显示的统计属性，确定 $E(\bar{X})$ 的值。'
        self.description_arabic = 'يوضح الشكل توزيع مجتمع $X$ وتوزيع متوسط العينة $\bar{X}$ لحجم عينة $n = ' + str(self.n) + '$. بناءً على الخصائص الإحصائية الموضحة، حدد قيمة $E(\bar{X})$.'
        self.description_hindi = 'चित्र एक जनसंख्या $X$ के वितरण और नमूना आकार $n = ' + str(self.n) + '$ के लिए नमूना माध्य $\\bar{X}$ के वितरण को दर्शाता है। दिखाए गए सांख्यिकीय गुणों के आधार पर, $E(\\bar{X})$ का मान निर्धारित करें।'
        self.description_kazakh = 'Суретте $X$ популяциясының үлестірімі және $n = ' + str(self.n) + '$ таңдама көлемі үшін $\\bar{X}$ таңдамалық орташа мәннің үлестірімі бейнеленген. Көрсетілген статистикалық қасиеттерге сүйене отырып, $E(\\bar{X})$ мәнін анықтаңыз.'
        self.description_swahili = 'Kielelezo kinaonyesha mtawanyiko wa idadi $X$ na mtawanyiko wa wastani wa sampuli $\\bar{X}$ kwa ukubwa wa sampuli $n = ' + str(self.n) + '$. Kulingana na sifa za takwimu zinazoonyeshwa, amua thamani ya $E(\\bar{X})$.'

