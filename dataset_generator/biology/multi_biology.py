from templates_001_050 import *

class Bio001_multi(Bio001):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Fotomikrograf menunjukkan sebuah sel tumbuhan. Garis XY menunjukkan panjang bayangan sel tersebut. Hitung panjang sel yang sebenarnya dalam satuan µm.'
        self.description_chinese = f'显微照片显示了一个植物细胞。线段 XY 显示了该细胞的图像长度。计算该细胞的实际长度，单位为 µm。'
        self.description_arabic = f'تُظهر الصورة المجهرية خلية نباتية.\nيمثل الخط XY طول صورة الخلية.\nاحسب الطول الحقيقي للخلية بوحدة µm.'
        self.description_hindi = f'फोटोमाइक्रोग्राफ में एक पादप कोशिका दिखाई गई है। रेखा XY कोशिका की प्रतिबिंब लंबाई दर्शाती है। कोशिका की वास्तविक लंबाई µm में ज्ञात कीजिए।'
        self.description_kazakh = f'Микрофотография өсімдік жасушасын көрсетеді. XY сызығы жасуша кескінінің ұзындығын көрсетеді. Жасушаның нақты ұзындығын µm-мен есептеңіз.'
        self.description_swahili = f'Picha ya hadubini (photomicrograph) inaonyesha seli ya mmea. Mstari XY unaonyesha urefu wa picha ya seli hiyo. Kokotoa urefu halisi wa seli katika µm.'

class Bio002_multi(Bio002):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Karen menggambar sketsa sebuah cangkang. Menggunakan ukuran yang diberikan, hitung perbesaran sketsa tersebut dibandingkan dengan cangkang yang sebenarnya.'
        self.description_chinese = f'凯伦画了一幅贝壳的素描。使用提供的测量值，计算该素描与实际贝壳相比的放大倍数。'
        self.description_arabic = f'رسمت كارين مخططًا لصدفة.\nباستخدام القياسات المعطاة، احسب مقدار التكبير مقارنة بالصدفة الحقيقية.'
        self.description_hindi = f'कैरेन (Karen) ने एक शैल का रेखाचित्र बनाया। दिए गए मापों का उपयोग करके, रेखाचित्र के आवर्धन की तुलना वास्तविक शैल से कीजिए।'
        self.description_kazakh = f'Карен бақалшақтың нобайын салды. Берілген өлшемдерді пайдаланып, нобайдың нақты бақалшақпен салыстырғандағы үлкейтілуін есептеңіз.'
        self.description_swahili = f'Karen alichora mchoro wa ganda la kiumbe. Kwa kutumia vipimo vilivyotolewa, kokotoa ukuzaji (magnification) wa mchoro huo ikilinganishwa na ganda halisi.'

class Bio003_multi(Bio003):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Seorang ahli genetika menyilangkan dua Mawar Merah ({self.dominant_pheno} x {self.recessive_pheno}). Diagram Punnett yang dihasilkan dapat dilihat di bawah ini. Jika biji yang dihasilkan menghasilkan total {self.sample_size} tanaman, hitung jumlah mawar {self.recessive_pheno} yang diharapkan.'
        self.description_chinese = f'一位遗传学家将两株红玫瑰进行杂交 ({self.dominant_pheno} x {self.recessive_pheno})。生成的庞氏表如下所示。如果生成的种子总共长出 {self.sample_size} 株植物，请计算 {self.recessive_pheno} 玫瑰的预期数量。'
        self.description_arabic = f'قام عالم وراثة بتهجين وردتين ({self.dominant_pheno} × {self.recessive_pheno}).\nيوضح مربع بانيت النتائج.\nإذا نتج {self.sample_size} نباتًا، احسب العدد المتوقع من {self.recessive_pheno}.'
        self.description_hindi = f'एक आनुवंशिकीविद् दो लाल गुलाबों ({self.dominant_pheno} x {self.recessive_pheno}) का संकरण करते हैं। परिणामी पुनेट (Punnett) वर्ग नीचे दिखाया गया है। यदि परिणामी बीजों से कुल {self.sample_size} पौधे उत्पन्न होते हैं, तो {self.recessive_pheno} गुलाबों की अपेक्षित संख्या की गणना कीजिए।'
        self.description_kazakh = f'Генетик екі қызыл раушанды шағылыстырады ({self.dominant_pheno} x {self.recessive_pheno}). Нәтижесінде алынған Пеннет торкөзін төменде көруге болады. Егер алынған тұқымдар барлығы {self.sample_size} өсімдік берсе, {self.recessive_pheno} раушан гүлдерінің күтілетін санын есептеңіз.'
        self.description_swahili = f'Mwanajenetiki anavukisha mawaridi mekundu mawili ({self.dominant_pheno} x {self.recessive_pheno}). Mraba wa Punnett (Punnett square) unaotokana unaonekana hapa chini. Ikiwa mbegu zitatoa jumla ya mimea {self.sample_size}, kokotoa idadi inayotarajiwa ya mawaridi ya {self.recessive_pheno}.'

class Bio004_multi(Bio004):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Grafik ini menunjukkan bagaimana populasi suatu spesies burung meningkat setelah adanya program konservasi. Berdasarkan grafik tersebut, hitung persentase peningkatan jumlah pasangan burung yang berbiak dari tahun {self.year_a} hingga {self.year_b}. Bulatkan jawaban ke bilangan bulat terdekat.'
        self.description_chinese = f'图中显示了在实施保护计划后，某种鸟类的种群数量是如何增加的。根据该图，计算从 {self.year_a} 到 {self.year_b} 繁殖鸟类对数的百分比增长。将答案四舍五入至最接近的整数。'
        self.description_arabic = f'يوضح الشكل تغير عدد أفراد نوع من الطيور بعد برنامج حماية.\nاحسب نسبة الزيادة في عدد الأزواج المتكاثرة من {self.year_a} إلى {self.year_b}.\nقرّب إلى أقرب عدد صحيح.'
        self.description_hindi = f'ग्राफ में एक संरक्षण कार्यक्रम के बाद पक्षियों की एक प्रजाति की जनसंख्या में हुई वृद्धि को दर्शाया गया है। ग्राफ के आधार पर, वर्ष {self.year_a} से वर्ष {self.year_b} तक पक्षियों के प्रजनन करने वाले जोड़ों की संख्या में प्रतिशत वृद्धि की गणना कीजिए। उत्तर को निकटतम पूर्णांक तक राउंड ऑफ करें।'
        self.description_kazakh = f'График құстардың бір түрінің популяциясы табиғатты қорғау бағдарламасынан кейін қалай өскенін көрсетеді. Графикке сүйене отырып, {self.year_a} жылдан {self.year_b} жылға дейінгі құстардың көбейетін жұптары санының пайыздық өсімін есептеңіз. Жауапты ең жақын бүтін санға дейін дөңгелектеңіз.'
        self.description_swahili = f'Grafu inaonyesha jinsi idadi ya spishi fulani ya ndege ilivyoongezeka kufuatia mpango wa uhifadhi. Kulingana na grafu, kokotoa asilimia ya ongezeko la idadi ya jozi za uzazi (breeding pairs) kuanzia mwaka wa {self.year_a} hadi {self.year_b}. Zungusha jibu lako kwa nambari nzima iliyo karibu zaidi.'

class Bio005_multi(Bio005):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Grafik ini menunjukkan kurva pertumbuhan kultur bakteri. Hitung persentase peningkatan populasi selama fase log.'
        self.description_chinese = f'图中显示了细菌培养物的生长曲线。计算对数期内种群数量的百分比增长。'
        self.description_arabic = f'يوضح الشكل منحنى نمو مزرعة بكتيرية.\nاحسب نسبة الزيادة خلال الطور اللوغاريتمي.'
        self.description_hindi = f'ग्राफ में जीवाणु संवर्धन का वृद्धि वक्र दर्शाया गया है। लॉग चरण के दौरान जनसंख्या में प्रतिशत वृद्धि की गणना कीजिए।'
        self.description_kazakh = f'График бактерия дақылының өсу қисығын көрсетеді. log фазасындағы популяцияның пайыздық өсімін есептеңіз.'
        self.description_swahili = f'Grafu inaonyesha mchirizi wa ukuaji (growth curve) wa malezi ya bakteria. Kokotoa asilimia ya ongezeko la idadi wakati wa awamu ya logi (log phase).'

class Bio006_multi(Bio006):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram ini menunjukkan rantai makanan. Berapa efisiensi transfer energi antara {self.trophics_names[self.indexA]} dan {self.trophics_names[self.indexB]}?'
        self.description_chinese = f'图中显示了一条食物链。在 {self.trophics_names[self.indexA]} 和 {self.trophics_names[self.indexB]} 之间的能量传递效率是多少？'
        self.description_arabic = f'يوضح الشكل سلسلة غذائية.\nما كفاءة انتقال الطاقة بين {self.trophics_names[self.indexA]} و {self.trophics_names[self.indexB]}؟'
        self.description_hindi = f'यह आरेख एक खाद्य श्रृंखला को दर्शाता है। {self.trophics_names[self.indexA]} और {self.trophics_names[self.indexB]} के बीच ऊर्जा स्थानांतरण की दक्षता क्या है?'
        self.description_kazakh = f'Бұл диаграмма қоректік тізбекті көрсетеді. {self.trophics_names[self.indexA]} және {self.trophics_names[self.indexB]} арасындағы энергия тасымалдау тиімділігі қандай?'
        self.description_swahili = f'Mchoro huu unaonyesha mnyororo wa chakula (food chain). Je, ufanisi wa uhamishaji wa nishati kati ya {self.trophics_names[self.indexA]} na {self.trophics_names[self.indexB]} ni upi?'

class Bio007_multi(Bio007):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Ini adalah bagian dari lapisan sel kontinu yang membentuk permukaan atas daun. Asumsikan bahwa semua sel ini identik ukurannya. Jika luas total permukaan atas daun adalah {self.surface_area_cm} cm², hitung jumlah sel di permukaan atas daun tersebut. Bulatkan jawaban ke bilangan bulat.'
        self.description_chinese = f'这些是形成树叶上表面的连续细胞层的一部分。假设所有这些细胞的大小相同。如果树叶上表面的总面积为 {self.surface_area_cm} cm²，请计算树叶上表面的细胞数量。将答案四舍五入为整数。'
        self.description_arabic = f'تمثل الصورة جزءًا من طبقة خلايا تغطي السطح العلوي للورقة.\nبافتراض تماثل الخلايا، وإذا كانت المساحة الكلية {self.surface_area_cm} cm²، احسب عدد الخلايا.\nقرّب إلى أقرب عدد صحيح.'
        self.description_hindi = f'ये कोशिकाएँ पत्ती की ऊपरी सतह बनाने वाली कोशिकाओं की एक सतत परत का हिस्सा हैं। मान लीजिए कि ये सभी कोशिकाएँ आकार में समान हैं। यदि पत्ती की ऊपरी सतह का कुल क्षेत्रफल {self.surface_area_cm} cm² है, तो पत्ती की ऊपरी सतह में कोशिकाओं की संख्या ज्ञात कीजिए। उत्तर को पूर्णांक में बदलें।'
        self.description_kazakh = f'Бұлар жапырақтың үстіңгі бетін құрайтын жасушалардың тұтас қабатының бір бөлігі. Бұл жасушалардың барлығының өлшемі бірдей деп есептеңіз. Егер жапырақтың үстіңгі бетінің жалпы ауданы {self.surface_area_cm} cm² болса, жапырақтың үстіңгі бетіндегі жасушалар санын есептеңіз. Жауапты бүтін санға дейін дөңгелектеңіз.'
        self.description_swahili = f'Hizi ni sehemu ya tabaka endelevu la seli zinazounda uso wa juu wa jani. Chukulia kuwa seli hizi zote zina ukubwa unaofanana. Ikiwa jumla ya eneo la uso wa juu wa jani ni {self.surface_area_cm} cm², kokotoa idadi ya seli katika uso huo wa juu. Zungusha jibu lako kwa nambari nzima.'

class Bio008_multi(Bio008):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Tabel tersebut menunjukkan spesies tumbuhan yang tercatat di satu lokasi, di suatu pulau, pada tahun 1975. Hitung indeks keanekaragaman untuk lokasi ini!'
        self.description_chinese = f'该表显示了 1975 年在一个岛屿上的一个地点记录的植物物种。请计算该地点的多样性指数！'
        self.description_arabic = f'يوضح الجدول أنواع نباتية مسجلة في موقع واحد عام 1975.\nاحسب مؤشر التنوع لهذا الموقع.'
        self.description_hindi = f'तालिका में एक द्वीप पर स्थित एक स्थान पर 1975 में दर्ज की गई पौधों की प्रजातियों को दर्शाया गया है। इस स्थान के लिए विविधता सूचकांक की गणना कीजिए!'
        self.description_kazakh = f'Кестеде 1975 жылы бір аралдың бір учаскесінде тіркелген өсімдік түрлері көрсетілген. Осы учаскенің әртүрлілік индексін есептеңіз!'
        self.description_swahili = f'Jedwali linaonyesha spishi za mimea zilizorekodiwa katika eneo moja, kwenye kisiwa kimoja, mwaka wa 1975. Kokotoa faharasa ya uanuwai (index of diversity) kwa eneo hili!'

class Bio009_multi(Bio009):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perbandingan kuantitatif dapat dilakukan terhadap jumlah RNA pada sampel A dan B. Hal ini melibatkan penentuan jumlah siklus yang diperlukan untuk mencapai 50% konsentrasi maksimum DNA (C). Jika jumlah RNA dalam suatu sampel dapat diukur sebagai: 1/C, hitung berapa kali lipat lebih banyak RNA yang terdapat pada sampel A dibandingkan dengan sampel B.'
        self.description_chinese = f'可以对样本 A 和 B 中的 RNA 数量进行定量比较。这涉及确定达到 DNA 最大浓度的 50% 所需的循环数 (C)。如果样本中的 RNA 数量可以测量为：1/C，请计算样本 A 中的 RNA 含量是样本 B 中的多少倍。'
        self.description_arabic = f'يمكن إجراء مقارنة كمية لكمية RNA في العينتين A و B.\nيتضمن ذلك تحديد عدد الدورات اللازمة للوصول إلى 50% من أقصى تركيز للـ DNA (C).\nإذا كانت كمية RNA تُقاس على صورة 1/C، فاحسب كم مرة تزيد كمية RNA في العينة A عنها في العينة B.'
        self.description_hindi = f'नमूने A और B में RNA की मात्रा की मात्रात्मक तुलना की जा सकती है। इसमें DNA की अधिकतम सांद्रता (C) के 50% तक पहुँचने के लिए आवश्यक चक्रों की संख्या निर्धारित करना शामिल है। यदि किसी नमूने में RNA की मात्रा को 1/C के रूप में मापा जा सकता है, तो गणना कीजिए कि नमूना A में नमूना B की तुलना में कितने गुना अधिक RNA मौजूद है।'
        self.description_kazakh = f'А және В үлгілеріндегі RNA мөлшерін сандық түрде салыстыруға болады. Бұл DNA максималды концентрациясының 50%-на жету үшін қажетті циклдер санын (C) анықтауды қамтиды. Егер үлгідегі RNA мөлшері 1/C ретінде өлшенсе, А үлгісінде В үлгісіне қарағанда RNA неше есе көп екенін есептеңіз.'
        self.description_swahili = f'Ulinganisho wa kiasi unaweza kufanywa kuhusu kiasi cha RNA katika sampuli A na B. Hii inahusisha kubaini idadi ya mizunguko inayohitajika kufikia 50% ya konsentresheni ya juu zaidi ya DNA (C). Ikiwa kiasi cha RNA katika sampuli kinaweza kupimwa kama 1/C, kokotoa ni mara ngapi zaidi RNA inapatikana katika sampuli A kuliko katika sampuli B.'

class Bio010_multi(Bio010):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Ini adalah ilustrasi sebuah potometer. Dalam satu eksperimen, gelembung udara bergerak sejauh {self.distance} mm dalam {self.minute} menit. Hitung laju penyerapan air oleh pucuk dalam eksperimen ini dalam mm³.'
        self.description_chinese = f'这是一个蒸腾计的示意图。在一次实验中，气泡在 {self.minute} 分钟内移动了 {self.distance} mm。计算在本次实验中枝条吸收水分的速率，单位为 mm³。'
        self.description_arabic = f'يوضح الشكل مقياس تدفق (potometer).\nفي إحدى التجارب، تحركت فقاعة الهواء مسافة {self.distance} mm خلال {self.minute} دقيقة.\nاحسب معدل امتصاص الماء بواسطة الساق بوحدة mm³.'
        self.description_hindi = f'यह एक पोटोमीटर का चित्र है। एक प्रयोग में, वायु का बुलबुला {self.distance} mm की दूरी {self.minute} मिनट में तय करता है। इस प्रयोग में पौधे द्वारा जल अवशोषण की दर को mm³ में ज्ञात कीजिए।'
        self.description_kazakh = f'Бұл потометрдің иллюстрациясы. Бір тәжірибеде ауа көпіршігі {self.minute} минут ішінде {self.distance} mm-ге жылжыды. Осы тәжірибедегі өркеннің суды сіңіру жылдамдығын mm³-пен есептеңіз.'
        self.description_swahili = f'Huu ni mchoro wa potometa (potometer). Katika jaribio moja, kiputo cha hewa kilisonga kwa umbali wa mm {self.distance} ndani ya dakika {self.minute}. Kokotoa kiwango cha unyonyaji wa maji kinachofanywa na mche katika jaribio hili katika mm³.'

class Bio011_multi(Bio011):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Para ilmuwan mempelajari efek hidup pada suhu yang berbeda terhadap respirasi ikan muda pada berbagai tahap pertumbuhan. Hasilnya ditunjukkan di bawah ini. Hitung nilai Q₁₀ untuk respirasi pada ikan terbesar.'
        self.description_chinese = f'科学家们研究了生活在不同温度下对不同生长阶段幼鱼呼吸作用的影响。他们的结果如下所示。请计算最大鱼类呼吸作用的 Q₁₀。'
        self.description_arabic = f'درس العلماء تأثير درجات الحرارة المختلفة على التنفس في أسماك صغيرة بمراحل نمو مختلفة.\nالنتائج موضحة في الشكل.\nاحسب قيمة Q₁₀ للتنفس في أكبر سمكة.'
        self.description_hindi = f'वैज्ञानिकों ने विकास के विभिन्न चरणों में युवा मछलियों में श्वसन पर विभिन्न तापमानों के प्रभाव का अध्ययन किया। उनके परिणाम नीचे दिए गए हैं। सबसे बड़ी मछली में श्वसन के लिए Q₁₀ की गणना कीजिए।'
        self.description_kazakh = f'Ғалымдар әртүрлі температурада өмір сүрудің әртүрлі өсу сатыларындағы жас балықтардың тыныс алуына әсерін зерттеді. Олардың нәтижелері төменде көрсетілген. Ең үлкен балықтың тыныс алуы үшін Q₁₀ есептеңіз.'
        self.description_swahili = f'Wanasayansi walichunguza athari za viwango tofauti vya joto kwenye upumuaji wa samaki wachanga katika hatua mbalimbali za ukuaji. Matokeo yao yanaonyeshwa hapa chini. Kokotoa Q₁₀ ya upumuaji kwa samaki mkubwa zaidi.'

class Bio012_multi(Bio012):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Untuk menentukan reliabilitas teknik tangkap-lepas dan Indeks Lincoln, dua peneliti mengumpulkan data populasi tikus dari lokasi yang sama pada waktu yang sama. Jika reliabilitas teknik tersebut tinggi, berapa banyak tikus bertanda yang diharapkan pada penangkapan kedua untuk peneliti II?'
        self.description_chinese = f'为了确定标志重捕法和林肯指数的可靠性，两名研究人员同时从同一地点收集了小鼠种群的数据。如果该技术的可靠性很高，研究人员 II 在第二次捕获中预期会有多少只被标记的小鼠？'
        self.description_arabic = f'لتقييم موثوقية تقنية الصيد وإعادة الصيد ومؤشر لينكولن، جمع باحثان بيانات من نفس الموقع وفي نفس الوقت.\nإذا كانت الموثوقية عالية، فكم عدد الفئران المعلّمة المتوقع اصطيادها في العينة الثانية للباحث الثاني؟'
        self.description_hindi = f'कैप्चर-रीकैप्चर तकनीक और लिंकन (Lincoln) इंडेक्स की विश्वसनीयता निर्धारित करने के लिए, दो शोधकर्ताओं ने एक ही स्थान से एक ही समय में चूहों की आबादी पर डेटा एकत्र किया। यदि तकनीक की विश्वसनीयता उच्च है, तो शोधकर्ता II द्वारा दूसरी बार पकड़े जाने पर कितने चिह्नित चूहे मिलने की उम्मीद होगी?'
        self.description_kazakh = f'Ұстау-қайта ұстау әдісінің және Линкольн индексінің сенімділігін анықтау үшін екі зерттеуші бір уақытта бір учаскеден тышқан популяциясы бойынша деректер жинады. Егер әдістің сенімділігі жоғары болса, II зерттеушінің екінші рет ұстауында қанша таңбаланған тышқан болуы күтіледі?'
        self.description_swahili = f'Ili kubaini uaminifu (reliability) wa mbinu ya kukamata-na-kukamata tena (capture-recapture) na Faharasa ya Lincoln, watafiti wawili walikusanya data kuhusu idadi ya panya kutoka eneo moja kwa wakati mmoja. Ikiwa uaminifu wa mbinu hiyo ni wa kiwango cha juu, ni panya wangapi waliotiwa alama wangetegemewa kupatikana katika mkamato wa pili wa mtafiti wa II?'

class Bio013_multi(Bio013):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram ini memberikan informasi tentang populasi kerbau Afrika di sebuah taman nasional. Jika populasi akhir pada akhir tahun {self.year} adalah {self.final_population}, hitung laju pertumbuhan populasi untuk populasi ini dibandingkan dengan tahun sebelumnya.'
        self.description_chinese = f'图表提供了有关某国家公园中非洲水牛种群的信息。如果 {self.year} 年底的最终种群数量为 {self.final_population}，请计算该种群与上一年相比的种群增长率。'
        self.description_arabic = f'يوضح الشكل بيانات عن جماعة من الجاموس الإفريقي في حديقة وطنية.\nإذا كان عدد الأفراد في نهاية عام {self.year} هو {self.final_population}، احسب معدل النمو السكاني مقارنة بالعام السابق.'
        self.description_hindi = f'यह चार्ट एक राष्ट्रीय उद्यान में अफ्रीकी भैंसों की आबादी के बारे में जानकारी प्रदान करता है। यदि {self.year} के अंत में अंतिम आबादी {self.final_population} थी, तो पिछले वर्ष की तुलना में इस आबादी की जनसंख्या वृद्धि दर की गणना करें।'
        self.description_kazakh = f'Бұл диаграмма ұлттық саябақтағы африкалық буйвол популяциясы туралы ақпарат береді. Егер {self.year} жылдың соңындағы соңғы популяция {self.final_population} болса, осы популяцияның алдыңғы жылмен салыстырғандағы өсу қарқынын есептеңіз.'
        self.description_swahili = f'Chati hii inatoa maelezo kuhusu idadi ya nyati wa Afrika katika hifadhi ya taifa. Ikiwa idadi ya mwisho mwishoni mwa mwaka wa {self.year} ilikuwa {self.final_population}, kokotoa kiwango cha ukuaji wa idadi ya nyati hawa ikilinganishwa na mwaka uliopita.'

class Bio014_multi(Bio014):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Beberapa siswa sedang melakukan eksperimen sampling kuadrat untuk memperkirakan jumlah bunga A yang tumbuh di lapangan tertentu. Mereka menempatkan 3 kuadrat secara acak di lapangan, dan mencatat pengamatan ini. Berapa perkiraan ukuran populasi bunga A di lapangan tersebut?'
        self.description_chinese = f'一些学生正在进行样方抽样实验，以估计某块田地中生长的花卉 A 的数量。他们在田地中随机放置了 3 个样方，并记录了这些观察结果。该田地中花卉 A 的估计种群规模是多少？'
        self.description_arabic = f'يجري طلاب تجربة أخذ عينات باستخدام المربعات (quadrats) لتقدير عدد النبات A في حقل.\nوُضعت 3 مربعات عشوائيًا وسُجلت النتائج.\nاحسب الحجم التقديري للجماعة النباتية A في الحقل.'
        self.description_hindi = f'कुछ छात्र एक खेत में उगने वाले फूल A की संख्या का अनुमान लगाने के लिए क्वाड्रेट सैंपलिंग प्रयोग कर रहे हैं। उन्होंने खेत में तीन क्वाड्रेट यादृच्छिक रूप से रखे और अवलोकन दर्ज किए। उस खेत में फूल A की अनुमानित जनसंख्या क्या है?'
        self.description_kazakh = f'Кейбір студенттер белгілі бір алқапта өсетін А гүлінің санын бағалау үшін квадраттық сынама алу тәжірибесін жүргізуде. Олар алқапқа 3 квадратты кездейсоқ орналастырып, осы бақылауларды жазып алды. Сол алқаптағы А гүлінің бағаланған популяция мөлшері қандай?'
        self.description_swahili = f'Baadhi ya wanafunzi wanafanya jaribio la sampuli ya kwadrati (quadrat sampling) ili kukadiria idadi ya ua A linalokua kwenye uwanja fulani. Waliweka kwadrati 3 kwa nasibu uwanjani, na kurekodi matokeo haya. Je, makadirio ya ukubwa wa idadi ya ua A kwenye uwanja huo ni upi?'

class Bio015_multi(Bio015):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Mikrometer objektif digunakan untuk mengkalibrasi mikrometer okuler. Mikrometer objektif memiliki 0.1 mm per skala. Hitung panjang sebenarnya yang diwakili oleh 1 unit skala okuler dalam µm.'
        self.description_chinese = f'载物台测微尺用于校准目镜测微尺。载物台测微尺每格代表 0.1 mm。计算 1 个目镜测微尺单位代表的实际长度，单位为 µm。'
        self.description_arabic = f'يُستخدم ميكرومتر المسرح لمعايرة تدريج العدسة العينية.\nإذا كان كل تدريج في ميكرومتر المسرح يساوي 0.1 mm، احسب الطول الحقيقي الذي تمثله وحدة واحدة من تدريج العدسة العينية بوحدة µm.'
        self.description_hindi = f'आईपिस ग्रैटिक्यूल को कैलिब्रेट करने के लिए स्टेज माइक्रोमीटर का उपयोग किया जाता है। इस स्टेज माइक्रोमीटर में प्रति डिवीजन 0.1 mm होता है। 1 ग्रैटिक्यूल इकाई द्वारा दर्शाई गई वास्तविक लंबाई को µm में ज्ञात कीजिए।'
        self.description_kazakh = f'Окулярлық торды калибрлеу үшін объектив-микрометр қолданылады. Объектив-микрометрдің әрбір бөлігінде 0.1 mm бар. 1 тор бірлігімен ұсынылған нақты ұзындықты µm-мен есептеңіз.'
        self.description_swahili = f'Maikromita ya jukwaa (stage micrometer) inatumika kurekebisha wavu wa mboni (eyepiece graticule). Maikromita ya jukwaa ina mm 0.1 kwa kila kigawanyo. Kokotoa urefu halisi unaowakilishwa na kipimo kimoja (1 unit) cha wavu katika µm.'

class Bio016_multi(Bio016):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sifat untuk kacang polong halus ({self.dominant_shape_gamet}) dominan terhadap kacang polong keriput ({self.recessive_shape_gamet}) dan warna kacang polong kuning ({self.dominant_color_gamet}) dominan terhadap hijau ({self.recessive_color_gamet}). Persilangan dihibrid antara dua tanaman kacang polong heterozigot dilakukan, menghasilkan Diagram Punnett ini. Kemudian, frekuensi fenotipe berikut diamati. Hitung nilai chi-kuadrat (χ²) untuk generasi ini.'
        self.description_chinese = f'圆滑豌豆特征 ({self.dominant_shape_gamet}) 对皱缩豌豆 ({self.recessive_shape_gamet}) 为显性，黄色豌豆特征 ({self.dominant_color_gamet}) 对绿色 ({self.recessive_color_gamet}) 为显性。在两株杂合豌豆植物之间进行双基因杂交，得到此庞氏表。随后，观察到以下表型频率。计算这一代的卡方 (χ²) 值。'
        self.description_arabic = f'صفة البازلاء الملساء ({self.dominant_shape_gamet}) سائدة على المجعدة ({self.recessive_shape_gamet})، واللون الأصفر ({self.dominant_color_gamet}) سائد على الأخضر ({self.recessive_color_gamet}).\nتم إجراء تهجين ثنائي الهجين بين نباتين متغايري الزيجوت.\nباستخدام النتائج، احسب قيمة مربع كاي (χ²).'
        self.description_hindi = f'चिकने मटर का लक्षण ({self.dominant_shape_gamet}) झुर्रीदार मटर के लक्षण ({self.recessive_shape_gamet}) पर प्रभावी है, और पीले मटर का रंग ({self.dominant_color_gamet}) हरे मटर के लक्षण ({self.recessive_color_gamet}) पर प्रभावी है। दो विषमयुग्मजी मटर के पौधों के बीच एक द्विसंकरी संकरण कराया जाता है, जिसके परिणामस्वरूप यह पुनेट वर्ग (Punnett Square) प्राप्त होता है। फिर, निम्नलिखित फलन-रूप आवृत्तियाँ देखी जाती हैं। इस पीढ़ी के लिए chi-square (χ²) का मान ज्ञात कीजिए।'
        self.description_kazakh = f'Тегіс бұршақ белгісі ({self.dominant_shape_gamet}) әжімді бұршақтарға ({self.recessive_shape_gamet}) қарағанда доминантты, ал сары бұршақ түсі ({self.dominant_color_gamet}) жасыл түске ({self.recessive_color_gamet}) қарағанда доминантты. Екі гетерозиготалы бұршақ өсімдігінің арасында дигибридті шағылыстыру жүргізіліп, нәтижесінде осы Пеннет торкөзі алынды. Содан кейін келесі фенотиптік жиіліктер байқалады. Бұл ұрпақ үшін хи-квадрат (χ²) мәнін есептеңіз.'
        self.description_swahili = f'Sifa ya njegere laini ({self.dominant_shape_gamet}) inatawala njegere zilizokunjamana ({self.recessive_shape_gamet}), na rangi ya njano ({self.dominant_color_gamet}) inatawala rangi ya kijani ({self.recessive_color_gamet}). Mvukisho wa dihaibridi (dihybrid cross) kati ya mimea miwili ya heterozigoti unafanywa na kutoa Mraba wa Punnett ufuatao. Ikiwa marudio ya fenotipu (phenotypic frequencies) yaliyozingatiwa ni haya, kokotoa thamani ya chi-mraba (χ²) kwa kizazi hiki.'

class Bio017_multi(Bio017):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar di bawah ini menunjukkan {self.total_ladybug} kepik yang dikumpulkan dari suatu populasi. Kepik-kepik tersebut tampak berwarna merah (sifat dominan, R) atau oranye (sifat resesif, r). Berdasarkan gambar tersebut, hitung persentase kepik yang heterozigot (Rr). Asumsikan populasi tersebut berada dalam kesetimbangan Hardy-Weinberg.'
        self.description_chinese = f'下图显示了从一种群中收集的 {self.total_ladybug} 只瓢虫。这些瓢虫表现为红色（显性特征，R）或橙色（隐性特征，r）。根据该图，计算杂合体 (Rr) 瓢虫的百分比。假设该种群处于哈迪-温伯格平衡。'
        self.description_arabic = f'تُظهر الصورة {self.total_ladybug} دعسوقة من جماعة سكانية.\nتكون إما حمراء (R) أو برتقالية (r).\nبافتراض اتزان هاردي-واينبرغ، احسب نسبة الدعسوقات متغايرة الزيجوت (Rr).'
        self.description_hindi = f'नीचे दी गई चित्र में एक आबादी से एकत्रित की गई {self.total_ladybug} लेडीबग दिखाई गई हैं। ये लेडीबग या तो लाल (प्रभावी लक्षण, R) या नारंगी (अप्रभावी लक्षण, r) रंग की हैं। छवि के आधार पर, विषमयुग्मजी (Rr) लेडीबगों का प्रतिशत ज्ञात कीजिए। मान लीजिए कि आबादी हार्डी-वीनबर्ग संतुलन (Hardy-Weinberg equilibrium) में है।'
        self.description_kazakh = f'Төмендегі суретте популяциядан жиналған {self.total_ladybug} қанқыз көрсетілген. Қанқыздар қызыл (доминантты белгі, R) немесе қызғылт сары (рецессивті белгі, r) болып көрінеді. Суретке сүйене отырып, гетерозиготалы (Rr) қанқыздардың пайызын есептеңіз. Популяция Харди-Вайнберг тепе-теңдігінде деп есептеңіз.'
        self.description_swahili = f'Picha iliyo hapa chini inaonyesha wadudu kobe (ladybugs) {self.total_ladybug} waliokusanywa kutoka kwa kundi fulani. Wadudu kobe hao wanaonekana ama wekundu (sifa tawala, R) au wa machungwa (sifa fumbwa, r). Kulingana na picha, kokotoa asilimia ya wadudu kobe walio heterozigoti (Rr). Chukulia kuwa kundi hili lipo katika usawa wa Hardy-Weinberg.'

class Bio018_multi(Bio018):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Tanaman yang dikenal sebagai Sesawi India (Brassica juncea) mengakumulasi emas dari garam emas di tanah tempat ia tumbuh. Tanaman ini dapat digunakan untuk mengekstraksi emas dari limbah tambang yang masih mengandung sisa emas yang tidak ekonomis untuk diekstraksi dengan metode tradisional. Penambahan amonium tiosianat ke substrat pertumbuhan limbah tambang diperkirakan dapat meningkatkan akumulasi emas oleh tanaman. Sebuah investigasi dilakukan untuk menguji apakah hal tersebut benar. Hasil investigasi (emas terakumulasi / mg emas kg⁻¹ massa kering) ditunjukkan pada tabel di bawah ini. Hitung nilai t.'
        self.description_chinese = f'被称为印度芥菜 (Brassica juncea) 的植物会从其生长的土壤中的金盐里富集黄金。它可用于从贫瘠的矿山废料中提取黄金，这些废料中仍含有残留的黄金，用传统方法提取是不经济的。在矿山废料生长基质中添加硫氰酸铵被认为可以促进植物对金的富集。为此进行了一项调查以测试是否如此。调查结果（积累的金 / mg 金 kg⁻¹ 干重）如下表所示。计算 t 的值。'
        self.description_arabic = f'يُراكم نبات الخردل الهندي (Brassica juncea) الذهب من التربة.\nتم اختبار تأثير إضافة ثيوسيانات الأمونيوم على التراكم.\nالنتائج موضحة في الجدول.\nاحسب قيمة t.'
        self.description_hindi = f'भारतीय सरसों (ब्रासिका जुनसिया) नामक पौधा जिस मिट्टी में उगता है, उसमें मौजूद स्वर्ण लवणों से सोना एकत्रित करता है। इसका उपयोग उन खदानों के अपशिष्टों से सोना निकालने के लिए किया जा सकता है जिनमें अभी भी अवशिष्ट सोना मौजूद है, जिसे पारंपरिक विधियों से निकालना आर्थिक रूप से लाभदायक नहीं है। खदान के अपशिष्ट के विकास सब्सट्रेट में अमोनियम थायोसाइनेट (ammonium thiocyanate) मिलाने से पौधों द्वारा सोने के संचय में वृद्धि होने की संभावना है। यह जानने के लिए एक अध्ययन किया गया कि क्या यह वास्तव में ऐसा है। अध्ययन के परिणाम (gold accumulated / mg gold kg⁻¹ dry mass) नीचे दी गई तालिका में दर्शाए गए हैं। t का मान ज्ञात कीजिए।'
        self.description_kazakh = f'Үнді қышасы (Brassica juncea) ретінде белгілі өсімдік өзі өсетін топырақтағы алтын тұздарынан алтын жинайды. Оны дәстүрлі әдістермен алу тиімсіз болатын, құрамында қалдық алтыны бар жұтаң кеніш қалдықтарынан алтынды алу үшін пайдалануға болады. Кеніш қалдықтарының өсу субстратына аммоний тиоцианатын қосу өсімдіктердің алтынды жинауын арттырады деп саналады. Мұның рас екенін тексеру үшін зерттеу жүргізілді. Зерттеу нәтижелері (жиналған алтын / mg алтын kg⁻¹ құрғақ масса) төмендегі кестеде көрсетілген. t мәнін есептеңіз.'
        self.description_swahili = f'Mmea wa Haradali ya India (Brassica juncea) hulimbikiza dhahabu kutoka kwa chumvi za dhahabu zilizomo kwenye udongo. Unaweza kutumika kutoa dhahabu kutoka kwa masalia duni ya migodi (mine wastes) ambayo yana dhahabu isiyo na faida kiuchumi ikitolewa kwa mbinu za kienyeji. Inaaminika kuwa uongezaji wa thiocyanate ya amonia kwenye tabaka la ukuaji huimarisha ulimbikizaji wa dhahabu kwenye mimea hiyo. Uchunguzi ulifanywa ili kuthibitisha dhana hiyo. Matokeo ya uchunguzi (dhahabu iliyolimbikizwa / mg ya dhahabu kwa kila kilo ya masi kavu) yameonyeshwa kwenye jedwali hapa chini. Kokotoa thamani ya t.'

class Bio019_multi(Bio019):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sebuah kromatogram pigmen tumbuhan dihasilkan menggunakan kromatografi kertas. Tentukan nilai Rf dari pigmen {self.pigment}.'
        self.description_chinese = f'使用纸色谱法制作了植物色素的色谱图。测定色素 {self.pigment} 的 Rf 值。'
        self.description_arabic = f'تم إجراء كروماتوغرافيا ورقية لأصباغ نباتية.\nاحسب قيمة Rf للصبغة {self.pigment}.'
        self.description_hindi = f'पेपर क्रोमैटोग्राफी का उपयोग करके पादप वर्णकों का एक क्रोमैटोग्राम तैयार किया गया था। वर्णक {self.pigment} का Rf मान ज्ञात करें।'
        self.description_kazakh = f'Өсімдік пигменттерінің хроматограммасы қағаз хроматографиясын пайдаланып жасалды. {self.pigment} пигментінің Rf мәнін анықтаңыз.'
        self.description_swahili = f'Kromatogramu ya pigmenti za mmea ilitengenezwa kwa kutumia kromatografia ya karatasi (paper chromatography). Tambua thamani ya Rf ya pigmenti ya {self.pigment}.'

class Bio020_multi(Bio020):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Ilmuwan lain menyelidiki sebuah enzim yang mengkatalisis reaksi berikut: ATP → ADP + Pi. Para ilmuwan menyiapkan dua eksperimen, C dan L. Eksperimen C menggunakan enzimnya dan konsentrasi ATP yang berbeda-beda. Eksperimen L menggunakan enzimnya, konsentrasi ATP yang berbeda-beda, dan gula yang disebut liksosa. Para ilmuwan mengukur laju reaksi di setiap eksperimen. Hasilnya ditunjukkan pada grafik. Hitung laju reaksi aktivitas enzim tanpa liksosa pada 2.5mmol dm⁻3 ATP sebagai persentase dari laju maksimum yang ditunjukkan dengan adanya liksosa.'
        self.description_chinese = f'另一位科学家研究了一种催化以下反应的酶：ATP → ADP + Pi。科学家们设置了两个实验，C 和 L。实验 C 使用了该酶和不同浓度的 ATP。实验 L 使用了该酶、不同浓度的 ATP 以及一种称为来苏糖（lyxose）的糖。科学家们测量了每个实验中的反应速率。他们的结果如图所示。计算在无来苏糖且 ATP 浓度为 2.5mmol dm⁻3 时酶活性的反应速率，并以含有来苏糖时所示最大速率的百分比表示。'
        self.description_arabic = f'درس العلماء إنزيماً يحفز التفاعل: ATP → ADP + Pi.\nأُجريت تجربتان مع وبدون ليكسوز.\nباستخدام الرسم، احسب معدل التفاعل بدون ليكسوز عند 2.5 mmol dm⁻3 كنسبة من المعدل الأقصى.'
        self.description_hindi = f'एक अन्य वैज्ञानिक ने एक एंजाइम की जांच की जो निम्नलिखित प्रतिक्रिया को उत्प्रेरित करता है: ATP → ADP + Pi। वैज्ञानिकों ने दो प्रयोग, C और L स्थापित किए। प्रयोग C में एंजाइम और ATP की विभिन्न सांद्रता का उपयोग किया गया। प्रयोग L में एंजाइम, ATP की विभिन्न सांद्रता, और लाइक्सोज़ (lyxose) नामक शर्करा का उपयोग किया गया। वैज्ञानिकों ने प्रत्येक प्रयोग में प्रतिक्रिया की दर को मापा। उनके परिणाम ग्राफ़ में दिखाए गए हैं। लाइक्सोज़ के साथ दिखाई गई अधिकतम दर के प्रतिशत के रूप में, 2.5mmol dm⁻3 ATP पर बिना लाइक्सोज़ के एंजाइम गतिविधि की प्रतिक्रिया दर की गणना करें।'
        self.description_kazakh = f'Басқа бір ғалым келесі реакцияны катализдейтін ферментті зерттеді: ATP → ADP + Pi. Ғалымдар екі тәжірибе, C және L орнатты. C тәжірибесі ферментті және ATP-дің әртүрлі концентрацияларын пайдаланды. L тәжірибесі ферментті, ATP-дің әртүрлі концентрацияларын және ликсоза деп аталатын қантты пайдаланды. Ғалымдар әр тәжірибеде реакция жылдамдығын өлшеді. Олардың нәтижелері графикте көрсетілген. ATP-дің 2.5mmol dm⁻3 концентрациясында ликсозасыз фермент белсенділігінің реакция жылдамдығын ликсозамен көрсетілген максималды жылдамдықтың пайызы ретінде есептеңіз.'
        self.description_swahili = f'Mwanasayansi mwingine alichunguza kimeng\'enya kinachochochea mmenyuko ufuatao: ATP → ADP + Pi. Wanasayansi waliandaa majaribio mawili, C na L. Jaribio la C lilitumia kimeng\'enya na konsentresheni tofauti za ATP. Jaribio la L lilitumia kimeng\'enya, konsentresheni tofauti za ATP, na sukari inayoitwa lyxose. Wanasayansi walipima kasi ya mmenyuko katika kila jaribio. Matokeo yao yanaonyeshwa kwenye grafu. Kokotoa kasi ya mmenyuko wa kimeng\'enya bila lyxose kwenye ATP ya 2.5 mmol dm⁻³ kama asilimia ya kasi ya juu zaidi (maximum rate) inayoonyeshwa kukiwa na lyxose.'

class Bio021_multi(Bio021):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Diagram tersebut merepresentasikan seluruh panjang molekul DNA rantai ganda, yang menunjukkan posisi nukleotida adenin (A). Hitung persentase nukleotida sitosin yang ada.'
        self.description_chinese = f'该图代表双链 DNA 分子的全长，显示了腺嘌呤 (A) 核苷酸的位置。计算存在的胞嘧啶核苷酸的百分比。'
        self.description_arabic = f'يوضح الشكل جزيء DNA مزدوج الشريط مع مواقع الأدينين (A).\nاحسب النسبة المئوية للسيتوزين.'
        self.description_hindi = f'यह आरेख एक दोहरे-केन्द्रित DNA अणु की संपूर्ण लंबाई को दर्शाता है, जिसमें एडेनिन (A) न्यूक्लियोटाइड (nucleotides) की स्थिति दिखाई गई है। उपस्थित साइटोसिन न्यूक्लियोटाइड (cytosine nucleotides) का प्रतिशत ज्ञात कीजिए।'
        self.description_kazakh = f'Диаграмма аденин (A) нуклеотидтерінің орналасуын көрсететін қос тізбекті DNA молекуласының толық ұзындығын білдіреді. Құрамындағы цитозин нуклеотидтерінің пайызын есептеңіз.'
        self.description_swahili = f'Mchoro huu unawakilisha urefu mzima wa molekuli ya DNA yenye nyuzi mbili (double-stranded DNA), ukionyesha nafasi za nyukliotaidi za adenine (A). Kokotoa asilimia ya nyukliotaidi za cytosine zilizopo.'

class Bio022_multi(Bio022):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Mata cokelat (B) dominan terhadap mata biru (b). Rambut keriting (C) dominan terhadap rambut lurus (c). Berdasarkan persilangan antara ayah dan ibu yang keduanya memiliki genotipe tertentu (disediakan dalam Diagram Punnett ini), tentukan jumlah individu yang diharapkan memiliki rambut keriting dalam total sampel sebanyak {self.sample_size}.'
        self.description_chinese = f'棕色眼睛 (B) 对蓝色眼睛 (b) 为显性。卷发 (C) 对直发 (c) 为显性。根据父母双方均具有特定基因型（提供于此庞氏表中）的杂交，确定在总样本量为 {self.sample_size} 中预期具有卷发的个体数量。'
        self.description_arabic = f'العيون البنية (B) سائدة على الزرقاء (b)، والشعر المجعد (C) سائد على الأملس (c).\nباستخدام مربع بانيت، احسب عدد الأفراد ذوي الشعر المجعد من أصل {self.sample_size}.'
        self.description_hindi = f'भूरी आँखें (B) नीली आँखों (b) पर प्रभावी होती हैं। घुंघराले बाल (C) सीधे बालों (c) पर प्रभावी होते हैं। एक पिता और एक माता के बीच क्रॉस के आधार पर, जिनके दोनों का जीनोटाइप एक निश्चित है (इस पुनेट स्क्वायर (Punnett Square) में दिया गया है), {self.sample_size} के कुल नमूने में घुंघराले बालों वाले व्यक्तियों की अपेक्षित संख्या ज्ञात कीजिए।'
        self.description_kazakh = f'Қоңыр көздер (B) көк көздерге (b) қарағанда доминантты. Бұйра шаш (C) тік шашқа (c) қарағанда доминантты. Әкесі мен анасының белгілі бір генотипі (осы Пеннет торкөзінде берілген) бар шағылыстыруға сүйене отырып, жалпы {self.sample_size} іріктемеде бұйра шашы болуы күтілетін даралар санын анықтаңыз.'
        self.description_swahili = f'Macho ya kahawia (B) yanatawala macho ya bluu (b). Nywele za kujikunja (C) zinatawala nywele zilizonyooka (c). Kulingana na mvukisho kati ya baba na mama wenye jiniotipu (genotype) fulani (kama inavyoonekana kwenye Mraba huu wa Punnett), tambua idadi ya viumbe wanaotarajiwa kuwa na nywele za kujikunja katika jumla ya sampuli ya {self.sample_size}.'

class Bio023_multi(Bio023):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Sebuah hemositometer digunakan untuk memperkirakan populasi ragi hidup dalam sampel sari buah apel yang tidak diencerkan. Pewarna metilen biru ditambahkan ke dalam sampel tersebut. Hanya sel ragi yang hidup yang akan menyerap pewarna ini. Gambar ini menunjukkan bilik hemositometer yang berisi sampel sari buah apel saat dilihat di bawah mikroskop cahaya. Kisi berukuran {self.grid_length_mm} mm x {self.grid_width_mm} mm dan memiliki kedalaman {self.depth_mm} mm. Hitung jumlah sel ragi hidup dalam 1 cm³ sampel sari buah apel tersebut. Asumsikan bahwa tidak ada aturan garis batas, dan bulatkan jawabannya ke bilangan bulat terdekat.'
        self.description_chinese = f'血细胞计数板用于估计未稀释苹果酒样本中活酵母的种群数量。将亚甲基蓝染料添加到样本中。只有活酵母细胞才会吸收这种染料。此图像显示了在光学显微镜下观察到的包含苹果酒样本的血细胞计数室。网格尺寸为 {self.grid_length_mm} mm x {self.grid_width_mm} mm，深度为 {self.depth_mm} mm。计算 1 cm³ 苹果酒样本中活酵母细胞的数量。假设没有边界规则，并将答案四舍五入为整数。'
        self.description_arabic = f'يُستخدم مقياس الكريات الدموية (haemocytometer) لتقدير عدد خلايا الخميرة الحية.\nأبعاد الشبكة {self.grid_length_mm} mm × {self.grid_width_mm} mm وعمقها {self.depth_mm} mm.\nاحسب عدد الخلايا في 1 cm³، مع التقريب لأقرب عدد صحيح.'
        self.description_hindi = f'बिना पतले किए गए (undiluted) साइडर के एक नमूने में जीवित यीस्ट (yeast) की आबादी का अनुमान लगाने के लिए हीमोसाइटोमीटर (haemocytometer) का उपयोग किया जाता है। नमूने में मेथिलीन ब्लू स्टेन मिलाया जाता है। केवल जीवित यीस्ट कोशिकाएं ही इस स्टेन को ग्रहण करेंगी। यह चित्र प्रकाश सूक्ष्मदर्शी के तहत देखे जाने पर साइडर के नमूने वाले हीमोसाइटोमीटर कक्ष को दिखाती है। ग्रिड का माप {self.grid_length_mm} mm x {self.grid_width_mm} mm है और इसकी गहराई {self.depth_mm} mm है। साइडर नमूने के 1 cm³ में जीवित यीस्ट कोशिकाओं की संख्या की गणना करें। मान लें कि कोई सीमा नियम नहीं हैं, और उत्तर को एक पूर्ण संख्या तक पूर्णांकित करें।'
        self.description_kazakh = f'Гемоцитометр сұйылтылмаған сидр үлгісіндегі тірі ашытқы популяциясын бағалау үшін қолданылады. Үлгіге метилен көгі бояуы қосылады. Тек тірі ашытқы жасушалары ғана бұл бояуды сіңіреді. Бұл суретте жарық микроскопымен қараған кезде сидр үлгісі бар гемоцитометр камерасы көрсетілген. Тордың өлшемі {self.grid_length_mm} mm x {self.grid_width_mm} mm және тереңдігі {self.depth_mm} mm. Сидр үлгісінің 1 cm³-індегі тірі ашытқы жасушаларының санын есептеңіз. Шекаралық ережелер жоқ деп есептеңіз және жауапты бүтін санға дейін дөңгелектеңіз.'
        self.description_swahili = f'Haimositomita (haemocytometer) inatumika kukadiria idadi ya hamira hai katika sampuli ya saida (cider) ambayo haijapunguzwa makali. Rangi ya buluu ya methilini (methylene blue) huongezwa kwenye sampuli. Seli hai za hamira pekee ndizo zitakazochukua rangi hii. Picha hii inaonyesha chemba ya haimositomita iliyo na sampuli ya saida inapotazamwa kupitia hadubini ya mwanga. Gridi ina vipimo vya mm {self.grid_length_mm} x mm {self.grid_width_mm} na ina kina cha mm {self.depth_mm}. Kokotoa idadi ya seli hai za hamira katika cm³ 1 ya sampuli ya saida. Chukulia kuwa hakuna sheria za mipaka, na zungusha jibu lako kwa nambari nzima.'

class Bio024_multi(Bio024):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Gambar ini menunjukkan {self.total_cells} sel dalam berbagai tahapan siklus sel. Dari gambar ini, hitung indeks mitosis (sebagai persentase).'
        self.description_chinese = f'图中显示了处于细胞周期不同阶段的 {self.total_cells} 个细胞。根据此图像，计算有丝分裂指数（以百分比表示）。'
        self.description_arabic = f'تُظهر الصورة {self.total_cells} خلية في مراحل مختلفة من دورة الخلية.\nاحسب المؤشر الانقسامي كنسبة مئوية.'
        self.description_hindi = f'यह चित्र {self.total_cells} कोशिकाओं को कोशिका चक्र के विभिन्न चरणों में दर्शाती है। इस चित्र से समसूत्री माइटोटिक सूचकांक (प्रतिशत में) की गणना कीजिए।'
        self.description_kazakh = f'Бұл суретте жасуша циклінің әртүрлі сатыларындағы {self.total_cells} жасуша көрсетілген. Осы суреттен митоздық индексті (пайызбен) есептеңіз.'
        self.description_swahili = f'Picha hii inaonyesha seli {self.total_cells} katika hatua tofauti za mzunguko wa seli. Kutokana na picha hii, kokotoa faharasa ya maitosisi (mitotic index) kama asilimia.'

