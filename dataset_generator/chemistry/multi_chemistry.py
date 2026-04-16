from templates_001_050 import *
from templates_051_100 import *
from templates_101_150 import *

class Chem001_multi(Chem001):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan spektrum massa sampel {self.name} berikut! Hitunglah massa atom relatif (Ar) {self.name} hingga 2 angka di belakang koma.'
        self.description_chinese = f'下面显示了 {self.name} 样本的质谱图。计算 {self.name} 的相对原子质量，保留2位小数。'
        self.description_arabic = f'يوضح أدناه طيف الكتلة لعينة من {self.name}. احسب الكتلة الذرية النسبية لـ {self.name} لأقرب منزلتين عشريتين.'
        self.description_hindi = f'नीचे {self.name} के एक नमूने का द्रव्यमान स्पेक्ट्रम दिखाया गया है। {self.name} का सापेक्ष परमाणु द्रव्यमान 2 दशमलव स्थानों तक ज्ञात कीजिए।'
        self.description_kazakh = f'Төменде {self.name} үлгісінің масс-спектрі көрсетілген. {self.name} салыстырмалы атомдық массасын үтірден кейін 2 белгіге дейін дәлдікпен есептеңіз.'
        self.description_swahili = f'Spekta ya masi (mass spectrum) ya sampuli ya {self.name} imeonyeshwa hapa chini. Kokotoa masi atomia ya kilinganisho (relative atomic mass) ya {self.name} kwa usahihi wa nafasi 2 za desimali.'

class Chem002_multi(Chem002):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik energi ionisasi berurutan unsur X berikut! Berdasarkan grafik tersebut, tentukan nomor golongan unsur X dalam Tabel Periodik Unsur.'
        self.description_chinese = f'该图显示了元素 X 的逐级电离能。确定元素 X 在元素周期表中的族数。'
        self.description_arabic = f'يوضح الشكل طاقات التأين المتتالية للعنصر X. حدد رقم مجموعة العنصر X في الجدول الدوري.'
        self.description_hindi = f'ग्राफ में तत्व X की क्रमिक आयनीकरण ऊर्जाएँ दर्शाई गई हैं। आवर्त सारणी में तत्व X का समूह क्रमांक ज्ञात कीजिए।'
        self.description_kazakh = f'Графикте X элементінің тізбекті иондану энергиялары көрсетілген. Периодтық кестедегі X элементінің топ нөмірін анықтаңыз.'
        self.description_swahili = f'Grafu hii inaonyesha nishati za ionization mfululizo (successive ionisation energies) za elementi X. Tambua namba ya kundi (group number) la elementi X katika Jedwali la Kipindi (Periodic Table).'

class Chem003_multi(Chem003):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram kotak orbital berikut yang merepresentasikan konfigurasi elektron suatu atom netral! Berdasarkan representasi tersebut, tentukan nomor atom (Z) atom tersebut.'
        self.description_chinese = '下面的轨道排布图表示一个未知中性原子的电子组态。根据提供的直观表示，确定该原子的原子序数（Z）。'
        self.description_arabic = 'يمثل مخطط المدارات أدناه التوزيع الإلكتروني لذرة متعادلة غير معروفة. بناءً على التمثيل المرئي، حدد العدد الذري (Z) لهذه الذرة.'
        self.description_hindi = 'नीचे दिया गया ऑर्बिटल बॉक्स आरेख एक उदासीन अज्ञात परमाणु के इलेक्ट्रॉन विन्यास को दर्शाता है। दिए गए दृश्य निरूपण के आधार पर, इस परमाणु की परमाणु संख्या (Z) ज्ञात कीजिए।'
        self.description_kazakh = 'Төмендегі орбитальдық ұяшықтар диаграммасы бейтарап белгісіз атомның электрондық конфигурациясын көрсетеді. Берілген визуалды көрініс негізінде осы атомның атомдық нөмірін (Z) анықтаңыз.'
        self.description_swahili = f'Mchoro wa visanduku vya obitali (orbital box diagram) hapa chini unawakilisha mpangilio wa elektroni wa atomi isiyojulikana isiyo na chaji (neutral atom). Kulingana na kielelezo kilichotolewa, tambua namba atomia (Z) ya atomi hii.'

class Chem004_multi(Chem004):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram partikel bermuatan dalam medan listrik homogen berikut! Muatan dan kuat medan tercantum pada diagram. Hitunglah gaya elektrostatik pada partikel tersebut (dalam N, hingga 3 angka desimal).'
        self.description_chinese = f'该图显示了匀强电场中的一个带电粒子。电荷量和电场强度已在图中标出。计算粒子所受的静电力（单位：N，保留3位小数）。'
        self.description_arabic = f'يوضح الشكل جسيمًا مشحونًا في مجال كهربائي منتظم. الشحنة وشدة المجال موضحتان على الشكل. احسب القوة الكهروستاتيكية المؤثرة على الجسيم (بوحدة N، مقربة إلى 3 منازل عشرية).'
        self.description_hindi = f'चित्र में एक समान विद्युत क्षेत्र में एक आवेशित कण दर्शाया गया है। चित्र में आवेश और क्षेत्र की तीव्रता अंकित हैं। कण पर लगने वाले स्थिरवैद्युत बल की गणना कीजिए (N में, 3 d.p. तक)।'
        self.description_kazakh = f'Диаграммада біртекті электр өрісіндегі зарядталған бөлшек көрсетілген. Заряд пен өріс кернеулігі диаграммада белгіленген. Бөлшекке әсер ететін электростатикалық күшті есептеңіз (Н-мен, үтірден кейін 3 белгіге дейін дәлдікпен).'
        self.description_swahili = f'Mchoro unaonyesha chembe yenye chaji katika uga wa umeme sare (uniform electric field). Chaji na ukubwa wa uga zimewekewa lebo kwenye mchoro. Kokotoa kani ya umemetuamo (electrostatic force) inayokaimu chembe hiyo (toa jibu katika Newton [N], kwa usahihi wa nafasi 3 za desimali).'

class Chem005_multi(Chem005):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik energi ionisasi pertama unsur-unsur dalam Periode {self.period} berikut! Berdasarkan grafik tersebut, nyatakan energi ionisasi pertama {self.anomaly_element} (dalam kJ mol⁻¹, dibulatkan ke bilangan bulat terdekat).'
        self.description_chinese = f'该图显示了周期 {self.period} 中各元素的第一电离能。请利用该图表求出元素 {self.anomaly_element} 的第一电离能（单位为 kJ mol⁻¹，四舍五入到整数）。'
        self.description_arabic = f'يوضح الشكل طاقات التأين الأولى لعناصر الدورة {self.period}. استخدم الرسم البياني لتحديد طاقة التأين الأولى للعنصر {self.anomaly_element} (بوحدة kJ mol⁻¹، لأقرب عدد صحيح).'
        self.description_hindi = f'ग्राफ में आवर्त {self.period} के तत्वों की प्रथम आयनीकरण ऊर्जा दर्शाई गई है। ग्राफ का उपयोग करके {self.anomaly_element} की प्रथम आयनीकरण ऊर्जा (kJ mol⁻¹ में, निकटतम पूर्णांक तक) बताइए।'
        self.description_kazakh = f'Графикте {self.period}-кезең элементтерінің бірінші иондану энергиялары көрсетілген. Графикті пайдалана отырып, {self.anomaly_element} элементінің бірінші иондану энергиясын анықтаңыз (кДж моль⁻¹ бірлігінде, ең жақын бүтін санға дейін дөңгелектеп).'
        self.description_swahili = f'Grafu inaonyesha nishati za kwanza za ionization (first ionisation energies) za elementi katika Kipindi cha {self.period}. Tumia grafu hiyo kutaja nishati ya kwanza ya ionization ya {self.anomaly_element} (toa jibu katika kJ mol⁻¹, kwa namba kamili iliyo karibu).'

class Chem006_multi(Chem006):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram susunan elektron dalam suatu atom berikut! Tentukan nomor atom unsur tersebut.'
        self.description_chinese = f'该图显示了一个原子中的电子排布。确定该元素的原子序数。'
        self.description_arabic = f'يوضح الشكل ترتيب الإلكترونات في ذرة. حدد العدد الذري لهذا العنصر.'
        self.description_hindi = f'चित्र में एक परमाणु में इलेक्ट्रॉनों की व्यवस्था दर्शाई गई है। इस तत्व का परमाणु क्रमांक ज्ञात कीजिए।'
        self.description_kazakh = f'Диаграммада атомдағы электрондардың орналасуы көрсетілген. Бұл элементтің атомдық нөмірін анықтаңыз.'
        self.description_swahili = f'Mchoro huu unaonyesha mpangilio wa elektroni (electron arrangement) katika atomi. Tambua namba atomia (atomic number) ya elementi hii.'

class Chem007_multi(Chem007):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan spektrum massa {self.element['name']} berikut! Bacalah intensitas relatif dari diagram, kemudian hitunglah massa atom relatif (Ar) {self.element['name']}."
        self.description_chinese = f"图中显示了 {self.element['name']} 的质谱图。从图中读取相对丰度并计算 {self.element['name']} 的相对原子质量（Ar）。"
        self.description_arabic = f'يوضح الشكل طيف الكتلة للعنصر {self.element["name"]}. اقرأ الشدات النسبية من الشكل واحسب الكتلة الذرية النسبية (Ar) للعنصر {self.element["name"]}.'
        self.description_hindi = f"{self.element['name']} का द्रव्यमान स्पेक्ट्रम दर्शाया गया है। आरेख से सापेक्ष तीव्रताएँ पढ़ें और {self.element['name']} का सापेक्ष परमाणु द्रव्यमान (Ar) ज्ञात कीजिए।"
        self.description_kazakh = f"Мұнда {self.element['name']} масс-спектрі көрсетілген. Диаграммадан салыстырмалы қарқындылықтарды оқып, {self.element['name']} салыстырмалы атомдық массасын (Ar) есептеңіз."
        self.description_swahili = f"Spekta ya masi (mass spectrum) ya {self.element['name']} imeonyeshwa. Soma wingi wa kilinganisho (relative intensities) kutoka kwenye mchoro na ukokotoe masi atomia ya kilinganisho (Ar) ya {self.element['name']}."

class Chem008_multi(Chem008):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram lingkaran komposisi persentase massa suatu senyawa berikut! Hitunglah jumlah mol atom karbon dalam 100 g senyawa tersebut. (Berikan jawaban hingga 2 angka di belakang koma.)'
        self.description_chinese = '该图显示了一种化合物的质量百分比组成。100 g 该化合物中含有多少摩尔的碳原子？（答案保留2位小数。）'
        self.description_arabic = 'يوضح المخطط الدائري النسبة المئوية للتركيب الكتلي لمركب. كم عدد مولات ذرات الكربون في 100 g من هذا المركب؟ (أعطِ إجابتك مقربة إلى منزلتين عشريتين).'
        self.description_hindi = 'पाई चार्ट किसी यौगिक की द्रव्यमान प्रतिशत संरचना दर्शाता है। इस यौगिक के 100 g में कार्बन परमाणुओं के कितने मोल मौजूद हैं? (अपना उत्तर 2 दशमलव स्थानों तक दें।)'
        self.description_kazakh = 'Дөңгелек диаграммада қосылыстың массалық үлесі пайызбен көрсетілген. Осы қосылыстың 100 г-да көміртек атомдарының қанша молі бар? (Жауабыңызды үтірден кейін 2 белгіге дейін дәлдікпен беріңіз.)'
        self.description_swahili = f'Chati duara (pie chart) inaonyesha asilimia ya muundo wa masi ya kampaundi fulani. Je, kuna moli ngapi za atomi za kaboni katika gramu 100 za kampaundi hii? (Toa jibu lako kwa usahihi wa nafasi 2 za desimali.)'

class Chem009_multi(Chem009):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram reaksi kimia beserta jumlah mol awal masing-masing reaktan berikut! Hitunglah jumlah mol maksimum produk yang dapat terbentuk.'
        self.description_chinese = '该图显示了一个化学反应以及每种反应物的初始摩尔数。计算可能生成的产物的最大摩尔数。'
        self.description_arabic = 'يوضح الشكل تفاعلًا كيميائيًا مع عدد المولات الابتدائية لكل متفاعل. احسب أقصى عدد من مولات الناتج التي يمكن تكوينها.'
        self.description_hindi = 'चित्र में प्रत्येक अभिकारक के प्रारंभिक मोलों के साथ एक रासायनिक अभिक्रिया दर्शाई गई है। उत्पाद के अधिकतम मोलों की गणना कीजिए जो बन सकते हैं।'
        self.description_kazakh = 'Диаграммада химиялық реакция және әрбір реагенттің бастапқы мольдері көрсетілген. Түзілуі мүмкін өнімнің максималды моль санын есептеңіз.'
        self.description_swahili = f'Mchoro unaonyesha mmenyuko wa kikemikali pamoja na idadi ya moli za awali za kila kitendanishi (reactant). Kokotoa idadi ya juu zaidi ya moli za zao (product) zinazoweza kuzalishwa.'

class Chem010_multi(Chem010):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan diagram molekul {self.molecule['name']} berikut dengan nilai keelektronegatifan (KE) yang tercantum pada masing-masing atom! Hitunglah selisih keelektronegatifan ΔKE = |KE₂ − KE₁| antara kedua atom tersebut."
        self.description_chinese = f"该图显示了 {self.molecule['name']} 分子，每个原子上标有电负性（EN）值。计算两个原子之间的电负性差值 ΔEN = |EN₂ − EN₁|。"
        self.description_arabic = f'يوضح الشكل جزيء {self.molecule["name"]} مع قيم الكهرسلبية (EN) لكل ذرة. احسب فرق الكهرسلبية ΔEN = |EN₂ − EN₁| بين الذرتين.'
        self.description_hindi = f"चित्र में {self.molecule['name']} अणु को दर्शाया गया है, जिसमें प्रत्येक परमाणु पर विद्युतऋणात्मकता (EN) मान अंकित हैं। दोनों परमाणुओं के बीच विद्युतऋणात्मकता अंतर ΔEN = |EN₂ − EN₁| की गणना कीजिए।"
        self.description_kazakh = f"Диаграммада әрбір атомда электртерістілік (EN) мәндері белгіленген {self.molecule['name']} молекуласы көрсетілген. Екі атом арасындағы электртерістілік айырмасын ΔEN = |EN₂ − EN₁| есептеңіз."
        self.description_swahili = f"Mchoro unaonyesha molekuli ya {self.molecule['name']} ikiwa na thamani za elektronegativiti (EN) kwenye kila atomi. Kokotoa tofauti ya elektronegativiti ΔEN = |EN₂ − EN₁| kati ya atomi hizo mbili."

class Chem011_multi(Chem011):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan struktur bola-dan-tongkat 3D suatu molekul berikut! Massa atom relatif setiap jenis atom tercantum pada diagram. Hitunglah jumlah ikatan dari struktur tersebut dan tentukan massa molekul relatif (Mr) molekul ini.'
        self.description_chinese = '图中显示了一个分子的 3D 球棍模型。图中已标出每种原子类型的相对原子质量。从 3D 结构中计算化学键的数量，并计算该分子的相对分子质量（Mr）。'
        self.description_arabic = 'يوضح الشكل تركيبًا ثلاثي الأبعاد لجزيء بنموذج الكرة والعصا. الكتلة الذرية النسبية لكل نوع من الذرات موضحة. احسب الكتلة الجزيئية النسبية (Mr) للجزيء.'
        self.description_hindi = 'एक अणु की 3D बॉल-एंड-स्टिक संरचना दर्शायी गई है। प्रत्येक परमाणु प्रकार का सापेक्षिक परमाणु द्रव्यमान आरेख पर अंकित है। 3D संरचना से बांड की संख्या गिनें और अणु का सापेक्षिक आणविक द्रव्यमान (Mr) ज्ञात करें।'
        self.description_kazakh = 'Молекуланың 3D шар-өзек құрылымы көрсетілген. Әрбір атом түрінің салыстырмалы атомдық массасы диаграммада белгіленген. 3D құрылымнан байланыстар санын санап, молекуланың салыстырмалы молекулалық массасын (Mr) есептеңіз.'
        self.description_swahili = f'Muundo wa pande tatu (3D ball-and-stick) wa molekuli umeonyeshwa. Masi atomia ya kilinganisho ya kila aina ya atomi imewekewa lebo kwenye mchoro. Hesabu idadi ya vifungo (bonds) kutoka kwenye muundo huo na ukokotoe masi molekuli ya kilinganisho (Mr) ya molekuli hiyo.'

class Chem012_multi(Chem012):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan struktur bola-dan-tongkat 3D suatu molekul berikut dengan satu pasangan elektron bebas (PEB) yang ditandai! Massa atom relatif setiap jenis atom tercantum pada diagram. Hitunglah jumlah ikatan dari struktur tersebut dan tentukan massa molekul relatif (Mr) molekul ini.'
        self.description_chinese = '图中显示了一个分子的3D球棍模型，并标出了一对孤对电子。图中标记了每种原子类型的相对原子质量。请根据该三维结构计算分子中的化学键数量，并计算该分子的相对分子质量（Mr）。'
        self.description_arabic = 'يوضح الشكل تركيبًا ثلاثي الأبعاد لجزيء بنموذج الكرة والعصا مع الإشارة إلى زوج حر واحد. الكتلة الذرية النسبية لكل نوع من الذرات موضحة. احسب الكتلة الجزيئية النسبية (Mr) للجزيء.'
        self.description_hindi = 'एक अणु की 3D बॉल-एंड-स्टिक संरचना दिखाई गई है, जिसमें एक एकाकी इलेक्ट्रॉन युग्म दर्शाया गया है। प्रत्येक परमाणु प्रकार का सापेक्षिक परमाणु द्रव्यमान आरेख पर अंकित है। 3D संरचना से बांड की संख्या गिनें और अणु का सापेक्षिक आणविक द्रव्यमान (Mr) ज्ञात करें।'
        self.description_kazakh = 'Молекуланың 3D шарикті-өзекшелі құрылымы көрсетілген және онда бір бөлінбеген электрон жұбы белгіленген. Әрбір атом түрінің салыстырмалы атомдық массасы сызбада көрсетілген. 3D құрылымдағы байланыстар санын санаңыз және молекуланың салыстырмалы молекулалық массасын (Mr) есептеңіз.'
        self.description_swahili = f'Muundo wa pande tatu (3D ball-and-stick) wa molekuli umeonyeshwa ukiwa na jozi moja ya elektroni pweke (lone pair). Masi atomia ya kilinganisho ya kila aina ya atomi imewekewa lebo. Hesabu idadi ya vifungo kutoka kwenye muundo huo na ukokotoe masi molekuli ya kilinganisho (Mr) ya molekuli hiyo.'

class Chem013_multi(Chem013):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan struktur bola-dan-tongkat 3D suatu molekul berikut dengan dua pasangan elektron bebas (PEB) yang ditandai! Massa atom relatif setiap jenis atom tercantum pada diagram. Hitunglah jumlah ikatan dari struktur tersebut dan tentukan massa molekul relatif (Mr) molekul ini.'
        self.description_chinese = '图中显示了一个分子的 3D 球棍模型，并标出了两个孤电子对。图中已标出每种原子类型的相对原子质量。从 3D 结构中计算化学键的数量，并计算该分子的相对分子质量（Mr）。'
        self.description_arabic = 'يوضح الشكل تركيبًا ثلاثي الأبعاد لجزيء بنموذج الكرة والعصا مع الإشارة إلى زوجين حرين. الكتلة الذرية النسبية لكل نوع من الذرات موضحة. احسب الكتلة الجزيئية النسبية (Mr) للجزيء.'
        self.description_hindi = 'एक अणु की 3D बॉल-एंड-स्टिक संरचना दिखाई गई है, जिसमें दो एकाकी इलेक्ट्रॉन युग्म दर्शाए गए हैं। प्रत्येक परमाणु प्रकार का सापेक्षिक परमाणु द्रव्यमान आरेख पर अंकित है। 3D संरचना से बांड की संख्या गिनें और अणु का सापेक्षिक आणविक द्रव्यमान (Mr) ज्ञात करें।'
        self.description_kazakh = 'Екі бөлінбеген электрон жұбы көрсетілген молекуланың 3D шар-өзек құрылымы берілген. Әрбір атом түрінің салыстырмалы атомдық массасы диаграммада белгіленген. 3D құрылымнан байланыстар санын санап, молекуланың салыстырмалы молекулалық массасын (Mr) есептеңіз.'
        self.description_swahili = f'Muundo wa pande tatu (3D ball-and-stick) wa molekuli umeonyeshwa ukiwa na jozi mbili za elektroni pweke (lone pairs). Masi atomia ya kilinganisho ya kila aina ya atomi imewekewa lebo kwenye mchoro. Hesabu idadi ya vifungo kutoka kwenye muundo huo na ukokotoe masi molekuli ya kilinganisho (Mr) ya molekuli hiyo.'

class Chem014_multi(Chem014):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik titik didih hidrida Golongan 16 berikut! Berdasarkan grafik tersebut, nyatakan titik didih {self.asked_mol} (dalam °C, dibulatkan ke bilangan bulat terdekat).'
        self.description_chinese = f'该图显示了第 16 族氢化物的沸点。利用该图说明 {self.asked_mol} 的沸点（°C，四舍五入到最接近的整数）。'
        self.description_arabic = f'يوضح الشكل درجات غليان هيدريدات المجموعة 16. استخدم الرسم البياني لتحديد درجة غليان {self.asked_mol} (°C، لأقرب عدد صحيح).'
        self.description_hindi = f'ग्राफ में समूह 16 के हाइड्राइडों के क्वथनांक दर्शाए गए हैं। ग्राफ का उपयोग करके {self.asked_mol} का क्वथनांक (°C, निकटतम पूर्णांक तक) बताइए।'
        self.description_kazakh = f'Графикте 16-топ гидридтерінің қайнау температуралары көрсетілген. Графикті пайдаланып, {self.asked_mol} қайнау температурасын көрсетіңіз (°C, ең жақын бүтін санға дейін).'
        self.description_swahili = f'Grafu hii inaonyesha viwango vya kuchemka (boiling points) vya haidraidi za Kundi la 16. Tumia grafu hiyo kutaja kiwango cha kuchemka cha {self.asked_mol} (toa jibu katika °C, kwa namba kamili iliyo karibu).'

class Chem015_multi(Chem015):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram kisi logam berikut dengan muatan ion yang tercantum! Berapa elektron bebas (terdelokalisasi) yang disumbangkan setiap atom logam ke dalam kisi tersebut?'
        self.description_chinese = '该图显示了一个金属晶格，并标出了离子电荷。每个金属原子向晶格贡献多少个离域电子？'
        self.description_arabic = 'يوضح الشكل شبكة فلزية مع شحنة الأيون موضحة. كم عدد الإلكترونات غير المتمركزة التي تساهم بها كل ذرة فلز في الشبكة؟'
        self.description_hindi = 'चित्र में आयन आवेश दर्शाए गए धात्विक जालक को दर्शाया गया है। प्रत्येक धातु परमाणु जालक में कितने विस्थानीकृत इलेक्ट्रॉनों का योगदान देता है?'
        self.description_kazakh = 'Диаграммада ион заряды белгіленген металдық тор көрсетілген. Әрбір металл атомы торға қанша делокализацияланған электрон береді?'
        self.description_swahili = f'Mchoro huu unaonyesha muundo wa latisi ya kimetali (metallic lattice) ukiwa na lebo ya chaji ya kila ioni. Je, kila atomi ya metali huchangia elektroni ngapi zilizohamahama (delocalized electrons) kwenye latisi hiyo?'

class Chem016_multi(Chem016):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram molekul berikut dengan momen dipol ikatan dan sudut ikatan yang tercantum! Hitunglah momen dipol resultan (μ_net) dalam Debye (D), hingga 2 angka di belakang koma.'
        self.description_chinese = '图中显示了一个分子，并标出了键偶极矩和键角。利用该图计算净（合成）偶极矩 μ_net，单位为德拜（D），保留2位小数。'
        self.description_arabic = 'يوضح الشكل جزيئًا مع عزوم ثنائي القطب للروابط وزاوية الرابطة. احسب عزم ثنائي القطب المحصل μ_net بوحدة ديباي (D)، مقربًا إلى منزلتين عشريتين.'
        self.description_hindi = 'एक अणु को दर्शाया गया है जिसमें बंध द्विध्रुव आघूर्ण और बंध कोण अंकित हैं। आरेख का उपयोग करके कुल (परिणामी) द्विध्रुव आघूर्ण, μ_net, को Debye (D) में 2 d.p. तक परिकलित करें।'
        self.description_kazakh = 'Байланыстардың дипольдік моменттері және байланыс бұрышы белгіленген молекула көрсетілген. Диаграмманы пайдаланып, қорытқы (нәтижелеуші) дипольдік моментті, μ_net, Дебай (D) өлшем бірлігімен үтірден кейін 2 белгіге дейін дәлдікпен есептеңіз.'
        self.description_swahili = f'Molekuli imeonyeshwa ikiwa na lebo za momenta za daipoli za vifungo (bond dipole moments) na pembe ya kifungo (bond angle). Tumia mchoro huo kukokotoa momenta ya daipoli jumla (μ_net) katika uniti za Debye (D), kwa usahihi wa nafasi 2 za desimali.'

class Chem017_multi(Chem017):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik titik didih gas mulia terhadap massa molekul relatif berikut! Berdasarkan grafik tersebut, nyatakan titik didih {self.asked_symbol} (dalam °C, dibulatkan ke bilangan bulat terdekat).'
        self.description_chinese = f'该图显示了稀有气体的沸点与相对分子质量的关系。利用该图说明 {self.asked_symbol} 的沸点（°C，四舍五入到最接近的整数）。'
        self.description_arabic = f'يوضح الشكل درجات غليان الغازات النبيلة مقابل الكتلة الجزيئية النسبية. استخدم الرسم البياني لتحديد درجة غليان {self.asked_symbol} (°C، لأقرب عدد صحيح).'
        self.description_hindi = f'ग्राफ में उत्कृष्ट गैसों के क्वथनांक को सापेक्ष आणविक द्रव्यमान के सापेक्ष दर्शाया गया है। ग्राफ का उपयोग करके {self.asked_symbol} का क्वथनांक (°C, निकटतम पूर्णांक) बताइए।'
        self.description_kazakh = f'Графикте бекзат газдардың қайнау температураларының салыстырмалы молекулалық массаға тәуелділігі көрсетілген. Графикті пайдаланып, {self.asked_symbol} қайнау температурасын көрсетіңіз (°C, ең жақын бүтін санға дейін).'
        self.description_swahili = f'Grafu hii inaonyesha viwango vya kuchemka (boiling points) vya gesi adimu (noble gases) vikilinganishwa na masi molekuli ya kilinganisho. Tumia grafu hiyo kutaja kiwango cha kuchemka cha {self.asked_symbol} (toa jibu katika °C, kwa namba kamili iliyo karibu).'

class Chem018_multi(Chem018):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan kurva pemanasan suhu terhadap waktu untuk suatu zat murni yang dipanaskan pada laju konstan berikut! Berdasarkan grafik tersebut, nyatakan titik didih zat ini (dalam °C).'
        self.description_chinese = '该加热曲线显示了以恒定速率加热纯物质时的温度与时间的关系。利用该图说明该物质的沸点（°C）。'
        self.description_arabic = 'يوضح منحنى التسخين درجة الحرارة مقابل الزمن لمادة نقية تُسخَّن بمعدل ثابت. استخدم الرسم البياني لتحديد درجة الغليان (°C).'
        self.description_hindi = 'तापन वक्र एक स्थिर दर से गर्म किए जा रहे शुद्ध पदार्थ के लिए तापमान बनाम समय को दर्शाता है। इस ग्राफ का उपयोग करके इस पदार्थ का क्वथनांक (°C) बताइए।'
        self.description_kazakh = 'Қыздыру қисығы тұрақты жылдамдықпен қыздырылып жатқан таза зат үшін температураның уақытқа тәуелділігін көрсетеді. Графикті пайдаланып, осы заттың қайнау температурасын көрсетіңіз (°C).'
        self.description_swahili = f'Grafu ya mabadiliko ya joto (heating curve) inaonyesha halijoto dhidi ya muda kwa dutu safi inayopashwa joto kwa kiwango kisichobadilika. Tumia grafu hiyo kutaja kiwango cha kuchemka (boiling point) cha dutu hii (toa jibu katika °C).'

class Chem019_multi(Chem019):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan kurva pemanasan suhu terhadap waktu untuk suatu zat murni berikut! Berdasarkan grafik tersebut, tentukan titik leleh (dalam °C) zat tersebut.'
        self.description_chinese = f'该加热曲线显示了纯物质的温度与时间的关系。利用该图确定该物质的熔点（单位：°C）。'
        self.description_arabic = 'يوضح منحنى التسخين درجة الحرارة مقابل الزمن لمادة نقية. استخدم الرسم البياني لتحديد درجة الانصهار (°C).'
        self.description_hindi = f'तापन वक्र एक शुद्ध पदार्थ के लिए तापमान बनाम समय को दर्शाता है। इस ग्राफ का उपयोग करके पदार्थ का गलनांक (°C में) ज्ञात कीजिए।'
        self.description_kazakh = f'Қыздыру қисығы таза зат үшін температураның уақытқа тәуелділігін көрсетеді. Графикті пайдаланып, заттың балқу температурасын (°C-мен) анықтаңыз.'
        self.description_swahili = f'Grafu ya mabadiliko ya joto (heating curve) inaonyesha halijoto dhidi ya muda kwa dutu safi. Tumia grafu hiyo kutambua kiwango cha kuyeyuka (melting point) cha dutu hii (toa jibu katika °C).'

class Chem020_multi(Chem020):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram profil entalpi berikut dengan tingkat energi yang ditandai pada sumbu-y! Hitunglah perubahan entalpi ΔH (dalam kJ mol⁻¹) untuk reaksi tersebut.'
        self.description_chinese = '图中显示了焓变分布图，y 轴上标有能级。计算该反应的焓变 ΔH（单位：kJ mol⁻¹）。'
        self.description_arabic = 'يوضح الشكل مخطط منحنى المحتوى الحراري مع مستويات الطاقة على المحور الرأسي. احسب التغير في المحتوى الحراري ΔH (بوحدة kJ mol⁻¹) لهذا التفاعل.'
        self.description_hindi = 'एन्थैल्पी प्रोफाइल आरेख को y-अक्ष पर ऊर्जा स्तरों के साथ दर्शाया गया है। इस अभिक्रिया के लिए एन्थैल्पी परिवर्तन ΔH (kJ mol⁻¹ में) की गणना कीजिए।'
        self.description_kazakh = 'y-осінде энергия деңгейлері белгіленген энтальпия профилінің диаграммасы көрсетілген. Осы реакция үшін ΔH энтальпия өзгерісін (кДж моль⁻¹-мен) есептеңіз.'
        self.description_swahili = f'Mchoro wa wasifu wa entalpi (enthalpy profile diagram) umeonyeshwa ukiwa na viwango vya nishati kwenye mhimili wa y. Kokotoa badiliko la entalpi ΔH (katika kJ mol⁻¹) kwa mmenyuko huu.'

class Chem021_multi(Chem021):
    def __init__(self):
        super().__init__()
        self.description_indonesian = "Perhatikan siklus Hukum Hess berikut! Gunakan nilai entalpi yang tercantum pada diagram untuk menghitung ΔH rute langsung A → B (dalam kJ mol⁻¹)."
        self.description_chinese = "图中显示了盖斯定律循环。利用图中标注的焓值计算直接途径 A → B 的 ΔH（单位：kJ mol⁻¹）。"
        self.description_arabic = "يوضح الشكل دورة قانون هس. استخدم قيم المحتوى الحراري المبينة على الشكل لحساب ΔH للمسار المباشر A → B (بوحدة kJ mol⁻¹)."
        self.description_hindi = "हेस के नियम का एक चक्र (Hess's Law cycle) दर्शाया गया है। आरेख पर अंकित एन्थैल्पी मानों का उपयोग करके प्रत्यक्ष मार्ग A → B के लिए ΔH की गणना करें (kJ mol⁻¹ में)।"
        self.description_kazakh = "Гесс заңының циклі көрсетілген. Тікелей A → B бағыты үшін ΔH (кДж моль⁻¹-мен) есептеуге диаграммада белгіленген энтальпия мәндерін пайдаланыңыз."
        self.description_swahili = f"Mzunguko wa Sheria ya Hess (Hess's Law cycle) umeonyeshwa. Tumia thamani za entalpi zilizowekewa lebo kwenye mchoro kukokotoa ΔH kwa njia ya moja kwa moja A → B (toa jibu katika kJ mol⁻¹)."

class Chem022_multi(Chem022):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram sel elektrokimia berikut! Gunakan potensial elektrode standar yang tercantum pada diagram untuk menghitung potensial sel standar E°sel (dalam V, hingga 2 angka di belakang koma).'
        self.description_chinese = '图中显示了电化学电池图。利用图中标注的标准电极电势计算标准电池电势 E°cell（单位：V，保留2位小数）。'
        self.description_arabic = 'يوضح الشكل خلية كهروكيميائية. استخدم جهود الأقطاب القياسية المبينة لحساب جهد الخلية القياسي E°cell (بوحدة V، مقربًا إلى منزلتين عشريتين).'
        self.description_hindi = 'विद्युत रासायनिक सेल का आरेख दिखाया गया है। आरेख में अंकित मानक इलेक्ट्रोड विभवों का उपयोग करके मानक सेल विभव E°cell (V में, 2 d.p. तक) की गणना करें।'
        self.description_kazakh = 'Электрохимиялық ұяшық диаграммасы көрсетілген. Диаграммада белгіленген стандартты электродтық потенциалдарды пайдаланып, стандартты ұяшық потенциалын E°cell (В-мен, үтірден кейін 2 белгіге дейін дәлдікпен) есептеңіз.'
        self.description_swahili = f'Mchoro wa seli ya kielektrokemikali (electrochemical cell) umeonyeshwa. Tumia thamani za uwezo wa kielektrodi sanifu (standard electrode potentials) zilizowekwa kwenye mchoro kukokotoa uwezo wa seli sanifu E°cell (toa jibu katika V, kwa usahihi wa nafasi 2 za desimali).'

class Chem023_multi(Chem023):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan grafik konsentrasi terhadap waktu untuk reaksi A ⇌ B berikut! Berdasarkan grafik tersebut, nyatakan konsentrasi kesetimbangan A (dalam mol dm⁻³).'
        self.description_chinese = '该图显示了反应 A ⇌ B 的浓度与时间的关系。说明 A 的平衡浓度（单位：mol dm⁻³）。'
        self.description_arabic = 'يوضح الرسم البياني التركيز مقابل الزمن للتفاعل A ⇌ B. اذكر تركيز A عند الاتزان (بوحدة mol dm⁻³).'
        self.description_hindi = 'ग्राफ अभिक्रिया A ⇌ B के लिए सांद्रता बनाम समय को दर्शाता है। A की साम्य सांद्रता (mol dm⁻³ में) बताइए।'
        self.description_kazakh = 'Графикте A ⇌ B реакциясы үшін концентрацияның уақытқа тәуелділігі көрсетілген. A-ның тепе-теңдік концентрациясын (моль дм⁻³-мен) көрсетіңіз.'
        self.description_swahili = f'Grafu hii inaonyesha mkusanyiko (concentration) dhidi ya muda kwa mmenyuko A ⇌ B. Taja mkusanyiko wa msawazo (equilibrium concentration) wa A (toa jibu katika mol dm⁻³).'

class Chem024_multi(Chem024):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan data konsentrasi kesetimbangan reaksi H₂ + I₂ ⇌ 2HI berikut! Hitunglah tetapan kesetimbangan Kc.'
        self.description_chinese = '图中显示了反应 H₂ + I₂ ⇌ 2HI 的平衡浓度。计算 Kc。'
        self.description_arabic = 'بالنسبة للتفاعل H₂ + I₂ ⇌ 2HI، التراكيز عند الاتزان موضحة. احسب ثابت الاتزان Kc.'
        self.description_hindi = 'अभिक्रिया H₂ + I₂ ⇌ 2HI के लिए, साम्य सांद्रताएँ दर्शायी गई हैं। Kc की गणना कीजिए।'
        self.description_kazakh = 'H₂ + I₂ ⇌ 2HI реакциясы үшін тепе-теңдік концентрациялары көрсетілген. Kc есептеңіз.'
        self.description_swahili = f'Kwa mmenyuko H₂ + I₂ ⇌ 2HI, mikusanyiko ya msawazo (equilibrium concentrations) imeonyeshwa. Kokotoa kigawio cha msawazo, Kc.'

class Chem025_multi(Chem025):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan kurva distribusi Maxwell-Boltzmann pada {self.T1} K dan {self.T2} K berikut! Berdasarkan grafik tersebut, nyatakan energi aktivasi Ea (dalam kJ mol⁻¹).'
        self.description_chinese = f'图中显示了在 {self.T1} K 和 {self.T2} K 下的麦克斯韦-玻尔兹曼分布曲线。利用该图说明活化能 Ea（单位：kJ mol⁻¹）。'
        self.description_arabic = f'يوضح الشكل منحنيات توزيع ماكسويل-بولتزمان عند درجتي الحرارة {self.T1} K و {self.T2} K. استخدم الرسم البياني لتحديد طاقة التنشيط Ea (بوحدة kJ mol⁻¹).'
        self.description_hindi = f'{self.T1} K और {self.T2} K पर मैक्सवेल-बोल्ट्ज़मैन वितरण वक्र (Maxwell-Boltzmann distribution curves) दर्शाए गए हैं। ग्राफ का उपयोग करके सक्रियण ऊर्जा Ea (kJ mol⁻¹ में) बताइए।'
        self.description_kazakh = f'{self.T1} K және {self.T2} K температураларындағы Максвелл-Больцман таралу қисықтары көрсетілген. Графикті пайдаланып, Ea активтену энергиясын (кДж моль⁻¹-мен) көрсетіңіз.'
        self.description_swahili = f'Mizingo ya mtawanyo ya Maxwell-Boltzmann (Maxwell-Boltzmann distribution curves) katika {self.T1} K na {self.T2} K imeonyeshwa. Tumia grafu hiyo kutaja nishati ya uamilisho, Ea (toa jibu katika kJ mol⁻¹).'

class Chem026_multi(Chem026):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan grafik konsentrasi terhadap waktu untuk reaksi orde pertama berikut! Tentukan waktu paruh (t½) reaksi tersebut dalam detik.'
        self.description_chinese = '该图显示了一级反应的浓度与时间分布曲线。确定该反应的半衰期 (t½)，单位为秒。'
        self.description_arabic = 'يوضح الرسم البياني التركيز مقابل الزمن لتفاعل من الرتبة الأولى. حدد عمر النصف (t½) للتفاعل بالثواني.'
        self.description_hindi = 'ग्राफ प्रथम कोटि की अभिक्रिया के लिए सांद्रता बनाम समय का प्रोफाइल दर्शाता है। अभिक्रिया की अर्ध-आयु (t½) सेकंड में ज्ञात कीजिए।'
        self.description_kazakh = 'Графикте бірінші ретті реакция үшін концентрацияның уақытқа тәуелділік профилі көрсетілген. Реакцияның жартылай ыдырау периодын (t½) секундпен анықтаңыз.'
        self.description_swahili = f'Grafu hii inaonyesha wasifu wa mkusanyiko (concentration) dhidi ya muda kwa mmenyuko wa oda ya kwanza (first-order reaction). Tambua nusumaisha (t½) ya mmenyuko huu katika sekunde.'

class Chem027_multi(Chem027):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram batang energi ionisasi pertama unsur-unsur Periode 3 berikut! Berdasarkan diagram tersebut, nyatakan energi ionisasi pertama {self.asked_element} (dalam kJ mol⁻¹, dibulatkan ke bilangan bulat terdekat).'
        self.description_chinese = f'柱状图显示了第三周期元素的电离能。利用该图表，求出{self.asked_element}的第一电离能（kJ mol⁻¹，四舍五入到最接近的整数）。'
        self.description_arabic = f'يوضح المخطط الشريطي طاقات التأين الأولى لعناصر الدورة الثالثة. استخدم المخطط لتحديد طاقة التأين الأولى للعنصر {self.asked_element} (بوحدة kJ mol⁻¹، لأقرب عدد صحيح).'
        self.description_hindi = f'बार चार्ट में आवर्त 3 के तत्वों की प्रथम आयनीकरण ऊर्जा दर्शाई गई है। इस चार्ट का उपयोग करके {self.asked_element} की प्रथम आयनीकरण ऊर्जा (kJ mol⁻¹, निकटतम पूर्णांक तक) बताइए।'
        self.description_kazakh = f'Бағанды диаграммада 3-ші кезең элементтерінің бірінші иондану энергиялары көрсетілген. Диаграмманы пайдалана отырып, {self.asked_element} элементінің бірінші иондану энергиясын анықтаңыз (кДж моль⁻¹ бірлігінде, ең жақын бүтін санға дейін дөңгелектеп).'
        self.description_swahili = f'Chati ya mihimili (bar chart) inaonyesha nishati za kwanza za ayonishaji (first ionisation energies) za elementi za Kipindi cha 3. Tumia chati hiyo kutaja nishati ya kwanza ya ayonishaji ya {self.asked_element} (toa jibu katika kJ mol⁻¹, kwa namba kamili iliyo karibu).'

class Chem028_multi(Chem028):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik jari-jari atom unsur-unsur Periode 3 berikut! Berdasarkan grafik tersebut, nyatakan jari-jari atom {self.asked_element} (dalam pm, dibulatkan ke bilangan bulat terdekat).'
        self.description_chinese = f'该图显示了第 3 周期元素的原子半径。利用该图说明 {self.asked_element} 的原子半径（单位：pm，四舍五入到最接近的整数）。'
        self.description_arabic = f'يوضح الرسم البياني أنصاف الأقطار الذرية لعناصر الدورة الثالثة. استخدم الرسم البياني لتحديد نصف القطر الذري للعنصر {self.asked_element} (بوحدة pm، لأقرب عدد صحيح).'
        self.description_hindi = f'ग्राफ में आवर्त 3 के तत्वों की परमाणु त्रिज्याएँ दर्शाई गई हैं। ग्राफ का उपयोग करके {self.asked_element} की परमाणु त्रिज्या (pm, निकटतम पूर्ण संख्या) बताइए।'
        self.description_kazakh = f'Графикте 3-период элементтерінің атомдық радиустары көрсетілген. Графикті пайдаланып, {self.asked_element} атомдық радиусын көрсетіңіз (пм, ең жақын бүтін санға дейін).'
        self.description_swahili = f'Grafu hii inaonyesha rediasi za atomi (atomic radii) za elementi za Kipindi cha 3. Tumia grafu hiyo kutaja rediasi ya atomi ya {self.asked_element} (toa jibu katika pm, kwa namba kamili iliyo karibu).'

class Chem029_multi(Chem029):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan ilustrasi percobaan berikut! Hitunglah jumlah mol Br₂ yang dihasilkan. Berikan jawaban hingga 3 angka di belakang koma.'
        self.description_chinese = '计算图中实验产生的 Br₂ 的摩尔数。答案保留3位小数。'
        self.description_arabic = 'احسب عدد مولات Br₂ الناتجة في التجربة الموضحة في الشكل. أعطِ إجابتك مقربة إلى 3 منازل عشرية.'
        self.description_hindi = 'चित्र में दर्शाए गए प्रयोग में उत्पन्न Br₂ के मोलों की संख्या ज्ञात कीजिए। अपना उत्तर 3 दशमलव स्थानों तक दीजिए।'
        self.description_kazakh = 'Диаграммада көрсетілген экспериментте түзілген Br₂ моль санын есептеңіз. Жауабыңызды үтірден кейін 3 белгіге дейін дәлдікпен беріңіз.'
        self.description_swahili = f'Kokotoa idadi ya moli za Br₂ zinazozalishwa katika jaribio lililoonyeshwa kwenye mchoro. Toa jibu lako likiwa na usahihi wa nafasi 3 za desimali.'

class Chem030_multi(Chem030):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan rumus struktur berikut! Berapa ikatan C–C tunggal yang dimiliki molekul tersebut?'
        self.description_chinese = '图中显示了一个结构式。该分子包含多少个 C–C 单键？'
        self.description_arabic = 'تُظهر الصيغة البنائية جزيئًا. كم عدد الروابط الأحادية C–C في هذا الجزيء؟'
        self.description_hindi = 'एक संरचनात्मक सूत्र दर्शाया गया है। इस अणु में कितने C–C एकल बांड हैं?'
        self.description_kazakh = 'Құрылымдық формула көрсетілген. Бұл молекулада қанша C–C дара байланысы бар?'
        self.description_swahili = f'Fomula ya kimuundo (structural formula) imeonyeshwa. Je, molekuli hii ina vifungo (bonds) vingapi vya pekee vya C–C?'

class Chem031_multi(Chem031):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan rumus struktur suatu alkena berikut! Hitunglah massa molekul relatif (Mr) senyawa tersebut.'
        self.description_chinese = f'图中显示了一种烯烃的结构式。计算该化合物的相对分子质量（Mr）。'
        self.description_arabic = f'تُظهر الصيغة البنائية لألكين. احسب الكتلة الجزيئية النسبية (Mr) لهذا المركب.'
        self.description_hindi = f'एक एल्कीन (alkene) का संरचनात्मक सूत्र दर्शाया गया है। इस यौगिक का सापेक्ष आणविक द्रव्यमान (Mr) ज्ञात कीजिए।'
        self.description_kazakh = f'Алкеннің құрылымдық формуласы көрсетілген. Осы қосылыстың салыстырмалы молекулалық массасын (Mr) есептеңіз.'
        self.description_swahili = f'Fomula ya kimuundo (structural formula) ya alkeni imeonyeshwa. Kokotoa masi molekuli ya kilinganisho (Mr) ya kampaundi hii.'

class Chem032_multi(Chem032):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan tabel empat anggota pertama suatu deret homolog berikut! Berdasarkan pola dalam tabel tersebut, tentukan jumlah atom hidrogen pada anggota dengan {self.n} atom karbon.'
        self.description_chinese = f'该表显示了某同系物的前四个成员（未给出同系物名称）。利用表中的规律，确定含有 {self.n} 个碳原子的成员有多少个氢原子。'
        self.description_arabic = f'يوضح الجدول الأعضاء الأربعة الأولى في سلسلة متجانسة (اسم السلسلة غير معطى). باستخدام النمط في الجدول، حدد عدد ذرات الهيدروجين في العضو الذي يحتوي على {self.n} ذرة كربون.'
        self.description_hindi = f'तालिका में समजात श्रृंखला के पहले चार सदस्य दर्शाए गए हैं (श्रृंखला का नाम नहीं दिया गया है)। तालिका में दिए गए पैटर्न का उपयोग करके ज्ञात कीजिए कि {self.n} कार्बन परमाणुओं वाले सदस्य में कितने हाइड्रोजन परमाणु हैं।'
        self.description_kazakh = f'Кестеде гомологтық қатардың алғашқы төрт мүшесі көрсетілген (қатар атауы берілмеген). Кестедегі заңдылықты пайдаланып, {self.n} көміртек атомы бар мүшеде қанша сутек атомы бар екенін анықтаңыз.'
        self.description_swahili = f'Jedwali hili linaonyesha washiriki (members) wanne wa kwanza wa mfululizo homolojia (jina la mfululizo halijatolewa). Kwa kutumia mtindo au mpangilio ulio kwenye jedwali, tambua idadi ya atomi za hidrojeni alizonazo mshiriki mwenye atomi {self.n} za kaboni.'

class Chem033_multi(Chem033):
    def __init__(self):
        super().__init__()
        self.description_indonesian = "Perhatikan diagram mekanisme adisi elektrofilik berikut! Rumus alkena dan pereaksi tercantum pada diagram. Hitunglah massa molekul relatif (Mr) produk reaksi tersebut. (Ar: H=1, C=12, Cl=35,5, Br=79,9, I=127)"
        self.description_chinese = "该图显示了亲电加成机理。图中标记了烯烃和试剂的化学式。产物框仅显示为 '?'。计算产物的相对分子质量（Mr）。(Ar: H=1, C=12, Cl=35.5, Br=79.9, I=127)"
        self.description_arabic = "يوضح الشكل آلية الإضافة الإلكتروفيلية. صيغ الألكين والكاشف مبينة. يظهر مربع الناتج بعلامة '?'. احسب الكتلة الجزيئية النسبية (Mr) للناتج. (Ar: H=1, C=12, Cl=35.5, Br=79.9, I=127)"
        self.description_hindi = "आरेख में इलेक्ट्रोफिलिक योग क्रियाविधि दर्शाई गई है। आरेख में एल्कीन (alkene) और अभिकर्मक के सूत्र अंकित हैं। उत्पाद बॉक्स में केवल '?' दर्शाया गया है। उत्पाद का सापेक्षिक आणविक द्रव्यमान (Mr) ज्ञात कीजिए। (Ar: H=1, C=12, Cl=35.5, Br=79.9, I=127)"
        self.description_kazakh = "Диаграммада электрофильді қосылу механизмі көрсетілген. Алкен мен реагент формулалары диаграммада белгіленген. Өнім ұяшығында тек '?' көрсетілген. Өнімнің салыстырмалы молекулалық массасын (Mr) есептеңіз. (Ar: H=1, C=12, Cl=35.5, Br=79.9, I=127)"
        self.description_swahili = f"Mchoro unaonyesha utaratibu (mechanism) wa muongezo wa kielektrofili (electrophilic addition). Fomula za alkeni na kitendanishi (reagent) zimewekewa lebo kwenye mchoro. Kisanduku cha zao (product) kinaonyesha '?' pekee. Kokotoa masi molekuli ya kilinganisho (Mr) ya zao hilo. (Ar: H=1, C=12, Cl=35.5, Br=79.9, I=127)"

class Chem034_multi(Chem034):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan rumus struktur suatu molekul berikut! Berapa ikatan C–H yang dimiliki molekul tersebut?'
        self.description_chinese = f'图中显示了一个分子的结构式。该分子包含多少个 C–H 键？'
        self.description_arabic = f'تُظهر الصيغة البنائية جزيئًا. كم عدد روابط C–H في هذا الجزيء؟'
        self.description_hindi = f'एक अणु का संरचनात्मक सूत्र दर्शाया गया है। इस अणु में कितने C–H बांड हैं?'
        self.description_kazakh = f'Молекуланың құрылымдық формуласы көрсетілген. Бұл молекулада қанша C–H байланысы бар?'
        self.description_swahili = f'Fomula ya kimuundo (structural formula) ya molekuli imeonyeshwa. Je, molekuli hii ina vifungo (bonds) vingapi vya C–H?'

class Chem035_multi(Chem035):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram pembentukan amida dari asam karboksilat dan amina berikut! Rumus reaktan tercantum pada diagram. Hitunglah massa molekul relatif (Mr) produk amida yang terbentuk. (Ar: H=1, C=12, N=14, O=16)'
        self.description_chinese = f'该图显示了由羧酸和胺形成酰胺的过程。图中标出了反应物的化学式。计算酰胺产物的相对分子质量（Mr）。(Ar: H=1, C=12, N=14, O=16)'
        self.description_arabic = f'يوضح الشكل تكوين أميد من حمض كربوكسيلي وأمين. صيغ المتفاعلات مبينة. احسب الكتلة الجزيئية النسبية (Mr) لناتج الأميد. (Ar: H=1, C=12, N=14, O=16)'
        self.description_hindi = f'चित्र में कार्बोक्सिलिक अम्ल (carboxylic acid) और अमीन (amine) से अमाइड (amide) के निर्माण को दर्शाया गया है। अभिकारकों के सूत्र चित्र में दिखाए गए हैं। अमाइड (amide) उत्पाद का सापेक्ष आणविक द्रव्यमान (Mr) ज्ञात कीजिए। (Ar: H=1, C=12, N=14, O=16)'
        self.description_kazakh = f'Диаграммада карбон қышқылы мен аминнен амидтің түзілуі көрсетілген. Реагенттердің формулалары диаграммада көрсетілген. Амид өнімінің салыстырмалы молекулалық массасын (Mr) есептеңіз. (Ar: H=1, C=12, N=14, O=16)'
        self.description_swahili = f'Mchoro huu unaonyesha uundaji wa amaidi (amide) kutokana na asidi kaboksiliki na amini. Fomula za vitendanishi (reactants) zimeonyeshwa kwenye mchoro. Kokotoa masi molekuli ya kilinganisho (Mr) ya zao la amaidi. (Ar: H=1, C=12, N=14, O=16)'

class Chem036_multi(Chem036):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram polimer adisi berikut! Gunakan satuan pengulang dan massa molekul relatif (Mr) total yang tercantum pada gambar untuk menghitung derajat polimerisasi n.'
        self.description_chinese = '该图显示了一种加成聚合物。利用图像中提供的重复单元和总相对分子质量（Mr），计算聚合度 n。'
        self.description_arabic = 'يوضح الشكل بوليمر إضافة. باستخدام الوحدة المتكررة والكتلة الجزيئية النسبية الكلية (Mr) المعطاة، احسب درجة البلمرة n.'
        self.description_hindi = 'चित्र में एक योगात्मक बहुलक दर्शाया गया है। चित्र में दी गई आवर्ती इकाई और कुल सापेक्ष आणविक द्रव्यमान (Mr) का उपयोग करके बहुलकीकरण की डिग्री n की गणना कीजिए।'
        self.description_kazakh = 'Диаграммада қосылу полимері көрсетілген. Суретте берілген қайталанатын буынды және жалпы салыстырмалы молекулалық массаны (Mr) пайдаланып, n полимерлену дәрежесін есептеңіз.'
        self.description_swahili = f'Mchoro huu unaonyesha polima ya muongezo (addition polymer). Kwa kutumia kizio kinachojirudia (repeating unit) na jumla ya masi molekuli ya kilinganisho (Mr) iliyotolewa kwenye picha, kokotoa kiwango cha upolimishaji (degree of polymerization), n.'

class Chem037_multi(Chem037):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan diagram sintesis multitahap: {self.pathway['title']} berikut! Rendemen setiap tahap tercantum pada diagram. Hitunglah rendemen total (persentase hasil keseluruhan) hingga 1 angka di belakang koma."
        self.description_chinese = f"该图显示了多步合成：{self.pathway['title']}。图中标出了每一步的产率。计算总百分产率（保留1位小数）。"
        self.description_arabic = f"يوضح الشكل مسار اصطناع متعدد الخطوات: {self.pathway['title']}. ناتج كل خطوة مبين. احسب النسبة المئوية الكلية للناتج (مقربة إلى منزلة عشرية واحدة)."
        self.description_hindi = f"आरेख में एक बहु-चरणीय संश्लेषण दर्शाया गया है: {self.pathway['title']}। प्रत्येक चरण की उपज आरेख पर अंकित है। कुल प्रतिशत उपज की गणना करें (1 d.p. तक)।"
        self.description_kazakh = f"Диаграммада көп сатылы синтез көрсетілген: {self.pathway['title']}. Әрбір сатының шығымы диаграммада белгіленген. Жалпы пайыздық шығымды есептеңіз (үтірден кейін 1 белгіге дейін дәлдікпен)."
        self.description_swahili = f"Mchoro huu unaonyesha mchakato wa usanisi wa hatua nyingi (multi-step synthesis): {self.pathway['title']}. Mavuno ya kila hatua yamewekewa lebo kwenye mchoro. Kokotoa asilimia ya mavuno ya jumla (overall percentage yield) kwa usahihi wa nafasi 1 ya desimali."

class Chem038_multi(Chem038):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan spektrum massa suatu senyawa organik berikut! Tentukan nilai m/z puncak ion molekul (M⁺).'
        self.description_chinese = '图中显示了一种有机化合物的质谱图。分子离子峰（M⁺）的 m/z 值是多少？'
        self.description_arabic = 'يوضح الشكل طيف الكتلة لمركب عضوي. ما قيمة m/z لقمة الأيون الجزيئي (M⁺)؟'
        self.description_hindi = 'एक कार्बनिक यौगिक का द्रव्यमान स्पेक्ट्रम दर्शाया गया है। आणविक आयन पीक (M⁺) का m/z मान क्या है?'
        self.description_kazakh = 'Органикалық қосылыстың масс-спектрі көрсетілген. Молекулалық ион шыңының (M⁺) m/z мәні қандай?'
        self.description_swahili = f"Spekta ya masi (mass spectrum) ya kampaundi ya kikaboni (organic compound) imeonyeshwa. Je, thamani ya m/z ya kilele cha ioni ya molekuli (M⁺ peak) ni ipi?"

class Chem039_multi(Chem039):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan spektrum inframerah (IR) {self.mol['name']} ({self.mol['formula']}) berikut! Pada bilangan gelombang berapa (cm⁻¹) serapan {self.ask_group} muncul?"
        self.description_chinese = f"图中显示了 {self.mol['name']} ({self.mol['formula']}) 的红外光谱（IR）。{self.ask_group} 吸收峰出现在什么波数（cm⁻¹）处？"
        self.description_arabic = f"يوضح طيف الأشعة تحت الحمراء (IR) للمركب {self.mol['name']} ({self.mol['formula']}). عند أي عدد موجي (cm⁻¹) يظهر امتصاص المجموعة {self.ask_group}؟"
        self.description_hindi = f"{self.mol['name']} ({self.mol['formula']}) का IR स्पेक्ट्रम दिखाया गया है। किस तरंग संख्या (cm⁻¹) पर {self.ask_group} का अवशोषण दिखाई देता है?"
        self.description_kazakh = f"{self.mol['name']} ({self.mol['formula']}) IR-спектрі көрсетілген. {self.ask_group} жұтылу жолағы қандай толқын санында (см⁻¹) пайда болады?"
        self.description_swahili = f"Spekta ya IR (Infrared spectrum) ya {self.mol['name']} ({self.mol['formula']}) imeonyeshwa. Je, ufyonzaji (absorption) wa kundi la {self.ask_group} unatokea katika nambariwimbi (wavenumber) gani (cm⁻¹)?"

class Chem040_multi(Chem040):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan spektrum ¹H NMR suatu senyawa organik berikut! Puncak yang disorot berwarna merah muncul pada δ = {self.ask_shift} ppm. Berapa atom hidrogen yang bertanggung jawab atas puncak tersebut?'
        self.description_chinese = f'图中显示了一种有机化合物的 ¹H NMR（核磁共振氢谱）。突出显示（红色）的峰出现在 δ = {self.ask_shift} ppm 处。该峰对应多少个氢原子？'
        self.description_arabic = f'يوضح الشكل طيف ¹H NMR لمركب عضوي. تظهر القمة المظللة (باللون الأحمر) عند δ = {self.ask_shift} ppm. كم عدد ذرات الهيدروجين المسؤولة عن هذه القمة؟'
        self.description_hindi = f'एक कार्बनिक यौगिक का ¹H NMR स्पेक्ट्रम दिखाया गया है। लाल रंग में हाइलाइट किया गया पीक δ = {self.ask_shift} ppm पर दिखाई देता है। इस पीक के लिए कितने हाइड्रोजन परमाणु जिम्मेदार हैं?'
        self.description_kazakh = f'Органикалық қосылыстың ¹H NMR-спектрі көрсетілген. Бөлініп көрсетілген шың (қызыл түспен) δ = {self.ask_shift} ppm тұсында пайда болады. Бұл шыңға қанша сутек атомы жауап береді?'
        self.description_swahili = f"Spekta ya ¹H NMR ya kampaundi ya kikaboni (organic compound) imeonyeshwa. Kilele kilichoangaziwa (kwa rangi nyekundu) kinaonekana katika δ = {self.ask_shift} ppm. Je, ni atomi ngapi za hidrojeni zinazosababisha kilele hiki?"

class Chem041_multi(Chem041):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram profil entalpi reaksi eksoterm berikut! Hitunglah perubahan entalpi ΔH untuk reaksi tersebut dalam kJ mol⁻¹.'
        self.description_chinese = f'该焓变分布图显示了一个放热反应。计算该反应的焓变 ΔH（单位：kJ mol⁻¹）。'
        self.description_arabic = f'يوضح الشكل مخطط المحتوى الحراري لتفاعل طارد للحرارة. احسب التغير في المحتوى الحراري ΔH (بوحدة kJ mol⁻¹).'
        self.description_hindi = f'एन्थैल्पी प्रोफाइल आरेख एक ऊष्माक्षेपी अभिक्रिया को दर्शाता है। इस अभिक्रिया के लिए एन्थैल्पी परिवर्तन, ΔH, की गणना kJ mol⁻¹ में कीजिए।'
        self.description_kazakh = f'Энтальпия профилінің диаграммасы экзотермиялық реакцияны көрсетеді. Осы реакция үшін ΔH энтальпия өзгерісін кДж моль⁻¹-мен есептеңіз.'
        self.description_swahili = f'Mchoro wa wasifu wa enthapi (enthalpy profile diagram) unaonyesha mmenyuko wa eksothemiki (exothermic reaction). Kokotoa badiliko la enthapi, ΔH, kwa mmenyuko huu katika kJ mol⁻¹.'

class Chem042_multi(Chem042):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan siklus Hukum Hess untuk pembentukan senyawa XYZ berikut! Berdasarkan perubahan entalpi pembakaran yang diberikan, hitunglah ΔH°f untuk XYZ."
        self.description_chinese = f"该图显示了化合物 XYZ 形成的盖斯定律循环。已知燃烧焓变，计算 XYZ 的标准生成焓 ΔH°f。"
        self.description_arabic = f"يوضح الشكل دورة قانون هس لتكوين المركب XYZ. باستخدام قيم التغير في المحتوى الحراري للاحتراق، احسب ΔH°f للمركب XYZ."
        self.description_hindi = f"चित्र में यौगिक XYZ के निर्माण के लिए हेस के नियम का चक्र (Hess's Law cycle) दर्शाया गया है। दहन के एन्थैल्पी परिवर्तनों को देखते हुए, XYZ के लिए ΔH°f की गणना कीजिए।"
        self.description_kazakh = f"Диаграммада XYZ қосылысының түзілуіне арналған Гесс заңының циклі көрсетілген. Жану энтальпиясының өзгерістерін ескере отырып, XYZ үшін ΔH°f есептеңіз."
        self.description_swahili = f"Mchoro huu unaonyesha mzunguko wa Sheria ya Hess (Hess's Law cycle) kwa ajili ya uundaji wa kampaundi XYZ. Kwa kutumia mabadiliko ya enthapi ya mwako (enthalpy of combustion) yaliyotolewa, kokotoa ΔH°f kwa kampaundi hiyo ya XYZ."

class Chem043_multi(Chem043):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan data energi ikatan dan persamaan reaksi yang tercantum pada gambar berikut! Hitunglah perubahan entalpi (ΔH) reaksi: CH₄ + H₂ → C₂H₆.'
        self.description_chinese = f'利用图中所示的键能计算反应 CH₄ + H₂ → C₂H₆ 的焓变。'
        self.description_arabic = f'احسب التغير في المحتوى الحراري للتفاعل: CH₄ + H₂ → C₂H₆ باستخدام طاقات الروابط الموضحة في الشكل.'
        self.description_hindi = f'आरेख में दर्शाई गई बांड ऊर्जाओं का उपयोग करके अभिक्रिया CH₄ + H₂ → C₂H₆ के लिए एन्थैल्पी परिवर्तन की गणना कीजिए।'
        self.description_kazakh = f'Диаграммада көрсетілген байланыс энергияларын пайдаланып, мына реакцияның энтальпия өзгерісін есептеңіз: CH₄ + H₂ → C₂H₆.'
        self.description_swahili = f'Kokotoa badiliko la enthapi (enthalpy change) kwa mmenyuko wa: CH₄ + H₂ → C₂H₆ kwa kutumia nishati za vifungo (bond energies) zilizoonyeshwa kwenye mchoro.'

class Chem044_multi(Chem044):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan grafik hubungan energi bebas Gibbs (ΔG) terhadap suhu berikut! Berdasarkan grafik tersebut, tentukan suhu (dalam K, dibulatkan ke bilangan bulat terdekat) di mana reaksi mulai berlangsung spontan.'
        self.description_chinese = '该图显示了一个反应的吉布斯自由能（ΔG）随温度的变化。利用该图确定反应变为自发时的温度（单位：K，四舍五入到最接近的整数）。'
        self.description_arabic = 'يوضح الرسم البياني تغير طاقة جيبس الحرة (ΔG) مع درجة الحرارة لتفاعل ما. استخدم الرسم لتحديد درجة الحرارة (بوحدة K، لأقرب عدد صحيح) التي يصبح عندها التفاعل تلقائيًا.'
        self.description_hindi = 'यह ग्राफ़ दर्शाता है कि किसी अभिक्रिया के लिए गिब्स मुक्त ऊर्जा (Gibbs free energy) (ΔG) तापमान के साथ कैसे बदलती है। इस ग्राफ़ का उपयोग करके वह तापमान (K में, निकटतम पूर्णांक तक) ज्ञात कीजिए जिस पर अभिक्रिया स्वतःस्फूर्त हो जाती है।'
        self.description_kazakh = 'Графикте реакция үшін Гиббстің еркін энергиясының (ΔG) температураға тәуелділігі көрсетілген. Реакция өздігінен жүретін температураны (К-мен, ең жақын бүтін санға дейін) анықтау үшін графикті пайдаланыңыз.'
        self.description_swahili = f"Grafu hii inaonyesha jinsi nishati huru ya Gibbs (ΔG) inavyobadilika kulingana na halijoto kwa mmenyuko fulani. Tumia grafu hiyo kutambua halijoto (katika K, kwa namba kamili iliyo karibu) ambapo mmenyuko huo unaanza kuwa wa hiari (spontaneous)."

class Chem045_multi(Chem045):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram setengah sel standar berikut dengan potensial elektrode standar yang tercantum pada masing-masing wadah! Hitunglah potensial sel standar E°sel (dalam V, hingga 2 angka di belakang koma).'
        self.description_chinese = '图中显示了标准半电池图，每个烧杯中都标有标准电极电势。计算标准电池电势 E°cell（单位：V，保留2位小数）。'
        self.description_arabic = 'يوضح الشكل مخطط نصف خلية قياسية مع جهود الأقطاب القياسية. احسب جهد الخلية القياسي E°cell (بوحدة V، مقربًا إلى منزلتين عشريتين).'
        self.description_hindi = 'मानक अर्ध-कोशिका आरेख दर्शाया गया है, जिसमें प्रत्येक बीकर में मानक इलेक्ट्रोड विभव अंकित हैं। मानक कोशिका विभव E°cell की गणना कीजिए (V में, 2 d.p. तक)।'
        self.description_kazakh = 'Әрбір стақанда стандартты электродтық потенциалдары белгіленген стандартты жартылай ұяшық диаграммасы көрсетілген. Стандартты ұяшық потенциалын E°cell (В-мен, үтірден кейін 2 белгіге дейін дәлдікпен) есептеңіз.'
        self.description_swahili = f"Mchoro wa nusu-seli sanifu (standard half-cell) umeonyeshwa huku potenishali za kielektrodi sanifu (standard electrode potentials) zikiwa zimewekewa lebo katika kila bika. Kokotoa potenishali ya seli sanifu, E°cell (toa jibu katika V, kwa usahihi wa nafasi 2 za desimali)."

class Chem046_multi(Chem046):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan diagram sel elektrolisis untuk larutan ion logam berikut! Gunakan data yang tercantum pada diagram untuk menghitung massa logam yang mengendap di katoda. (Massa atom relatif = {self.element[1]}, Tetapan Faraday F = 96500 C mol⁻¹)"
        self.description_chinese = f"该图显示了特定金属离子溶液的电解池。利用图中提供的数据，计算在阴极沉积的金属质量。(相对原子质量 = {self.element[1]}，法拉第常数 F = 96500 C mol⁻¹)"
        self.description_arabic = f"يوضح الشكل خلية تحليل كهربائي لمحلول يحتوي على أيونات فلزية. باستخدام المعطيات، احسب كتلة الفلز المترسب عند الكاثود. (الكتلة الذرية النسبية = {self.element[1]}، ثابت فاراداي F = 96500 C mol⁻¹)"
        self.description_hindi = f"आरेख एक विशिष्ट धातु आयन विलयन के लिए एक विद्युत अपघटन सेल को दर्शाता है। आरेख में दिए गए डेटा का उपयोग करके, कैथोड पर निक्षेपित धातु के द्रव्यमान की गणना करें। (सापेक्ष परमाणु द्रव्यमान = {self.element[1]}, फैराडे नियतांक F = 96500 C mol⁻¹)"
        self.description_kazakh = f"Диаграммада белгілі бір металл ионының ерітіндісіне арналған электролиз ұяшығы көрсетілген. Диаграммада берілген мәліметтерді пайдаланып, катодта бөлінген металдың массасын есептеңіз. (Салыстырмалы атомдық масса = {self.element[1]}, Фарадей тұрақтысы F = 96500 C моль⁻¹)"
        self.description_swahili = f"Mchoro huu unaonyesha seli ya elektrolisisi (electrolysis cell) kwa ajili ya mnyeyusho wa ioni za metali fulani. Kwa kutumia data iliyotolewa kwenye mchoro, kokotoa masi ya metali inayotua (deposited) kwenye kathodi. (Masi atomia ya kilinganisho = {self.element[1]}, Konstanti ya Faraday F = 96500 C mol⁻¹)"

class Chem047_multi(Chem047):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik perubahan konsentrasi untuk reaksi A + B ⇌ C berikut! Berdasarkan grafik tersebut, nyatakan konsentrasi kesetimbangan C.'
        self.description_chinese = f'该图显示了反应 A + B ⇌ C 的浓度变化。C 的平衡浓度是多少？'
        self.description_arabic = f'يوضح الرسم البياني تغيرات التركيز للتفاعل A + B ⇌ C. ما تركيز C عند الاتزان؟'
        self.description_hindi = f'ग्राफ अभिक्रिया A + B ⇌ C के लिए सांद्रता में परिवर्तन दर्शाता है। C की साम्य सांद्रता क्या है?'
        self.description_kazakh = f'Графикте A + B ⇌ C реакциясы үшін концентрация өзгерістері көрсетілген. C-ның тепе-теңдік концентрациясы қандай?'
        self.description_swahili = f"Grafu hii inaonyesha mabadiliko ya konsentresheni (concentration) kwa mmenyuko wa A + B ⇌ C. Je, konsentresheni ya C katika hali ya msawazo (equilibrium) ni ipi?"

class Chem048_multi(Chem048):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan data konsentrasi kesetimbangan untuk kesetimbangan A + B ⇌ C + D berikut! Hitunglah tetapan kesetimbangan Kc.'
        self.description_chinese = f'图中显示了平衡反应 A + B ⇌ C + D 的平衡浓度。计算平衡常数 Kc。'
        self.description_arabic = f'بالنسبة للاتزان A + B ⇌ C + D، التراكيز عند الاتزان موضحة. احسب ثابت الاتزان Kc.'
        self.description_hindi = f'संतुलन A + B ⇌ C + D के लिए, संतुलन सांद्रताएँ दर्शायी गई हैं। संतुलन स्थिरांक Kc की गणना कीजिए।'
        self.description_kazakh = f'A + B ⇌ C + D тепе-теңдігі үшін тепе-теңдік концентрациялары көрсетілген. Kc тепе-теңдік константасын есептеңіз.'
        self.description_swahili = f"Kwa msawazo (equilibrium) wa A + B ⇌ C + D, konsentresheni za msawazo zimeonyeshwa. Kokotoa konstanti ya msawazo, Kc."

class Chem049_multi(Chem049):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik perubahan konsentrasi terhadap waktu berikut! Hitunglah laju reaksi pada t = {self.t_point} detik.'
        self.description_chinese = f'该图显示了浓度随时间的变化。计算 t = {self.t_point} 秒时的反应速率。'
        self.description_arabic = f'يوضح الرسم البياني تغير التركيز مع الزمن. احسب سرعة التفاعل عند t = {self.t_point} ثانية.'
        self.description_hindi = f'ग्राफ समय के साथ सांद्रता में होने वाले परिवर्तन को दर्शाता है। समय t = {self.t_point} सेकंड पर अभिक्रिया की दर की गणना कीजिए।'
        self.description_kazakh = f'Графикте концентрацияның уақытқа байланысты қалай өзгеретіні көрсетілген. t = {self.t_point} секундтағы реакция жылдамдығын есептеңіз.'
        self.description_swahili = f"Grafu hii inaonyesha jinsi konsentresheni (concentration) inavyobadilika kulingana na muda. Kokotoa kasi ya mmenyuko (rate of reaction) katika muda wa t = {self.t_point} sekunde."

class Chem050_multi(Chem050):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik hubungan laju awal terhadap konsentrasi reaktan A berikut! Berdasarkan grafik tersebut, tentukan orde reaksi terhadap A.'
        self.description_chinese = f'该图显示了初始速率随反应物 A 浓度的变化。确定关于反应物 A 的反应级数。'
        self.description_arabic = f'يوضح الرسم البياني العلاقة بين السرعة الابتدائية وتركيز المتفاعل A. حدد رتبة التفاعل بالنسبة لـ A.'
        self.description_hindi = f'ग्राफ दर्शाता है कि अभिकारक A की सांद्रता के साथ प्रारंभिक अभिक्रिया दर में किस प्रकार परिवर्तन होता है। A के सापेक्ष अभिक्रिया की कोटि ज्ञात कीजिए।'
        self.description_kazakh = f'Графикте бастапқы жылдамдықтың A реагентінің концентрациясына тәуелділігі көрсетілген. A бойынша реакцияның ретін анықтаңыз.'
        self.description_swahili = f"Grafu hii inaonyesha jinsi kasi ya awali (initial rate) inavyobadilika kulingana na konsentresheni ya kitendanishi A. Tambua oda ya mmenyuko (order of reaction) kuhusiana na A."

class Chem051_multi(Chem051):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram batang reaktivitas relatif empat unsur Golongan 2 dengan air berikut! Unsur-unsur disusun berdasarkan urutan nomor atom (posisi 1 hingga 4). Berapa nilai reaktivitas yang ditunjukkan untuk unsur pada posisi {self.position}?\n\n{self.options_text}'
        self.description_chinese = f'柱状图显示了四种第 2 族元素与水反应的相对反应性。元素按原子序数排列（位置 1 到 4）。位置 {self.position} 的元素显示的反应性值是多少？\n\n{self.options_text}'
        self.description_arabic = f'يوضح المخطط الشريطي التفاعلية النسبية لأربعة عناصر من المجموعة الثانية مع الماء. العناصر مرتبة حسب العدد الذري (من 1 إلى 4). ما قيمة التفاعلية للعنصر في الموضع {self.position}؟\n\n{self.options_text}'
        self.description_hindi = f'बार चार्ट में समूह 2 के चार तत्वों की जल के साथ सापेक्षिक प्रतिक्रियाशीलता दर्शाई गई है। तत्वों को परमाणु क्रमांक के क्रम में व्यवस्थित किया गया है (स्थिति 1 से 4 तक)। स्थिति {self.position} पर स्थित तत्व के लिए प्रतिक्रियाशीलता का मान क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Бағаналы диаграммада төрт 2-топ элементінің сумен салыстырмалы реакцияға түсу қабілеті көрсетілген. Элементтер атомдық нөмірлерінің өсу ретімен орналасқан (1-ден 4-ке дейінгі орын). {self.position}-орындағы элемент үшін көрсетілген реакцияға түсу қабілетінің мәні қандай?\n\n{self.options_text}'
        self.description_swahili = f"Chati ya mihimili (bar chart) inaonyesha utendaji kilinganisho (relative reactivity) wa elementi nne za Kundi la 2 zinapofanya mmenyuko na maji. Elementi hizi zimepangwa kulingana na namba zao za atomia (kuanzia nafasi ya 1 hadi 4). Ni thamani gani ya utendaji iliyoonyeshwa kwa elementi iliyopo katika nafasi ya {self.position}?\n\n{self.options_text}"

class Chem052_multi(Chem052):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan definisi dan konfigurasi elektron yang diberikan pada diagram berikut! Berdasarkan data tersebut, manakah yang merupakan unsur transisi?\n\n{self.options_text}'
        self.description_chinese = f'根据图中提供的定义和电子排布，以下哪项是过渡元素？\n\n{self.options_text}'
        self.description_arabic = f'بناءً على التعريف والتوزيعات الإلكترونية الموضحة، أي من التالي يُعد عنصرًا انتقاليًا؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख में दी गई परिभाषा और इलेक्ट्रॉन विन्यास के आधार पर, निम्नलिखित में से कौन सा/से संक्रमण तत्व है/हैं?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада берілген анықтама мен электрондық конфигурацияларға сүйене отырып, төмендегілердің қайсысы ауыспалы элемент(тер) болып табылады?\n\n{self.options_text}'
        self.description_swahili = f"Kulingana na fasili (definition) na mipangilio ya elektroni (electron configurations) iliyotolewa kwenye mchoro, ni ipi kati ya zifuatazo ni elementi ya mpito (transition element)?\n\n{self.options_text}"

class Chem053_multi(Chem053):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram tabung reaksi berisi senyawa suatu logam transisi pada berbagai bilangan oksidasi berikut! Tentukan bilangan oksidasi logam pada tabung reaksi yang disorot.\n\n{self.options_text}'
        self.description_chinese = f'图中的试管含有处于不同氧化态的某过渡金属的化合物。突出显示的试管中金属的氧化态是多少？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل أنابيب اختبار تحتوي على مركبات لفلز انتقالي في حالات أكسدة مختلفة. ما حالة أكسدة الفلز في الأنبوب المظلل؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख विभिन्न ऑक्सीकरण अवस्थाओं में एक संक्रमण धातु के यौगिकों वाली परखनलियों को दर्शाता है। हाइलाइट की गई परखनली में धातु की ऑक्सीकरण अवस्था क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада әртүрлі тотығу дәрежесіндегі ауыспалы металл қосылыстары бар сынауықтар көрсетілген. Бөлініп көрсетілген сынауықтағы металдың тотығу дәрежесі қандай?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mirija ya majaribio (test tubes) yenye kampaundi za metali ya mpito katika hali tofauti za oksidesheni (oxidation states). Je, hali ya oksidesheni ya metali iliyo kwenye mrija wa majaribio ulioangaziwa ni ipi?\n\n{self.options_text}"

class Chem054_multi(Chem054):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram susunan spasial ligan di sekitar ion logam transisi pusat berikut! Tentukan bilangan koordinasi ion logam pusat tersebut.'
        self.description_chinese = '该图显示了中心过渡金属离子周围配体的整体空间排列。中心金属离子的配位数是多少？'
        self.description_arabic = 'يوضح الشكل الترتيب الفراغي لليجندات حول أيون فلز انتقالي مركزي. ما العدد التناسقي لأيون الفلز المركزي؟'
        self.description_hindi = 'आरेख एक केंद्रीय संक्रमण धातु आयन के चारों ओर लिगेंड (ligands) की सामान्य स्थानिक व्यवस्था को दर्शाता है। केंद्रीय धातु आयन की उपसहसंयोजन संख्या (coordination number) क्या है?'
        self.description_kazakh = 'Диаграммада орталық ауыспалы металл ионының айналасындағы лигандтардың жалпы кеңістіктік орналасуы көрсетілген. Орталық металл ионының координациялық саны қандай?'
        self.description_swahili = f"Mchoro huu unaonyesha mpangilio wa anga (spatial arrangement) wa ligandi kuzunguka ioni ya kati ya metali ya mpito. Je, namba ya uratibu (coordination number) ya ioni ya kati ya metali hiyo ni ipi?"

class Chem055_multi(Chem055):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi pertukaran ligan yang dimulai dari larutan ion logam akua berikut! Tuliskan rumus ion kompleks akhir yang terbentuk.\n\n{self.options_text}'
        self.description_chinese = f'该图显示了从金属离子水溶液开始的配体交换反应。最终配离子的化学式是什么？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل تفاعل استبدال ليجندات بدءًا من محلول مائي لأيون فلز. ما صيغة الأيون المعقد النهائي؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख एक जलीय धातु आयन विलयन से शुरू होने वाली लिगेंड विनिमय अभिक्रिया को दर्शाता है। अंतिम संकुल आयन (complex ion) का सूत्र क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада сулы металл ионы ерітіндісінен басталатын лиганд алмасу реакциясы көрсетілген. Соңғы кешенді ионның (комплексті ионның) формуласы қандай?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mmenyuko wa mabadilishano ya ligandi (ligand exchange) kuanzia kwenye mnyeyusho wa akia (aqueous solution) wa ioni ya metali. Je, fomula ya ioni tata (complex ion) ya mwisho ni ipi?\n\n{self.options_text}"

class Chem056_multi(Chem056):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi substitusi ligan berikut! Kompleks awal dan ligan yang ditambahkan tercantum pada diagram. Warna apakah yang akan ditunjukkan larutan hasil reaksi?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了配体取代反应。图中显示了起始配合物和加入的配体。所得溶液将是什么颜色？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل تفاعل استبدال ليجند. المعقد الابتدائي والليجند المضاف موضحان. ما لون المحلول الناتج؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख एक लिगेंड प्रतिस्थापन अभिक्रिया को दर्शाता है। प्रारंभिक संकुल और मिलाया गया लिगेंड आरेख में दिखाए गए हैं। परिणामी विलयन का रंग क्या होगा?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада лигандты орынбасу реакциясы көрсетілген. Бастапқы кешен (комплекс) және қосылған лиганд диаграммада көрсетілген. Алынған ерітінді қандай түсті болады?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mmenyuko wa ubadilishaji wa ligandi (ligand substitution). Ioni tata ya kuanzia na ligandi iliyoongezwa vimeonyeshwa kwenye mchoro. Je, mnyeyusho (solution) utakaopatikana utakuwa na rangi gani?\n\n{self.options_text}"

class Chem057_multi(Chem057):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram pembelahan orbital-d berikut! Hitunglah panjang gelombang (dalam nm) cahaya yang diserap oleh kompleks tersebut.\n\n(Diketahui: h = 6,626×10⁻³⁴ J·s, c = 3,00×10⁸ m/s, Nₐ = 6,022×10²³ mol⁻¹)'
        self.description_chinese = f'根据提供的 d 轨道分裂图，计算该配合物吸收光波长（单位：nm）。\n\n(已知: h = 6.626×10⁻³⁴ J·s, c = 3.00×10⁸ m/s, Nₐ = 6.022×10²³ mol⁻¹)'
        self.description_arabic = f'بناءً على مخطط انقسام مدارات d، احسب الطول الموجي (بوحدة nm) للضوء الممتص بواسطة هذا المعقد.\n\n(بمعلومية: h = 6.626×10⁻³⁴ J·s، c = 3.00×10⁸ m/s، Nₐ = 6.022×10²³ mol⁻¹)'
        self.description_hindi = f'दिए गए d-कक्षीय विभाजन आरेख के आधार पर, इस जटिल यौगिक द्वारा अवशोषित प्रकाश की तरंगदैर्ध्य (nm में) की गणना कीजिए।\n\n(दिया गया है: h = 6.626×10⁻³⁴ J•s, c = 3.00×10⁸ m/s, Nₐ = 6.022×10²³ mol⁻¹)'
        self.description_kazakh = f'Берілген d-орбитальдардың жіктелу диаграммасына сүйене отырып, осы кешен сіңіретін жарықтың толқын ұзындығын (нм-мен) есептеңіз.\n\n(Берілгені: h = 6.626×10⁻³⁴ Дж·с, c = 3.00×10⁸ м/с, Nₐ = 6.022×10²³ моль⁻¹)'
        self.description_swahili = f"Kulingana na mchoro wa mgawanyiko wa d-obitali (d-orbital splitting) uliotolewa, kokotoa urefu wa wimbi (wavelength katika nm) wa mwanga unaofyonzwa (absorbed) na ioni tata hii.\n\n(Imepewa: h = 6.626×10⁻³⁴ J·s, c = 3.00×10⁸ m/s, Nₐ = 6.022×10²³ mol⁻¹)"

class Chem058_multi(Chem058):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram siklus katalitik yang melibatkan logam transisi berikut! Di antara dua bilangan oksidasi manakah katalis tersebut bersiklus?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了涉及过渡金属的催化循环。催化剂在哪两个氧化态之间循环？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل دورة تحفيزية تتضمن فلزًا انتقاليًا. بين أي حالتي أكسدة يدور المحفز؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में एक संक्रमण धातु से जुड़े उत्प्रेरक चक्र को दर्शाया गया है। यह उत्प्रेरक किन दो ऑक्सीकरण अवस्थाओं के बीच चक्रित होता है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада ауыспалы металл қатысатын катализдік цикл көрсетілген. Катализатор қандай екі тотығу дәрежесі арасында цикл түзеді?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mzunguko wa kichocheo (catalytic cycle) unaohusisha metali ya mpito. Je, kichocheo hicho kinabadilika kati ya hali zipi mbili za oksidesheni (oxidation states) katika mzunguko wake?\n\n{self.options_text}"

class Chem059_multi(Chem059):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram dua ion kompleks beserta tetapan kestabilannya (Kstab) berikut! Apakah pertukaran ligan yang ditampilkan pada diagram layak terjadi?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了两种配离子及其稳定常数（Kstab）。图中所示的配体交换是否可行？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل أيونين معقدين وثوابت الاستقرار (Kstab) لهما. هل تفاعل استبدال الليجند الموضح ممكن؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख में दो जटिल आयन और उनके स्थिरता स्थिरांक (Kstab) दर्शाए गए हैं। क्या आरेख में दर्शाया गया लिगैंड विनिमय संभव है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада екі кешенді ион және олардың тұрақтылық константалары (Kstab) көрсетілген. Диаграммада көрсетілген лиганд алмасуы мүмкін бе?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha ioni tata (complex ions) mbili pamoja na konstanti zao za uthabiti (Kstab). Je, mabadilishano ya ligandi (ligand exchange) yaliyoonyeshwa kwenye mchoro yanawezekana kutokea (feasible)?\n\n{self.options_text}"

class Chem060_multi(Chem060):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan rumus struktur berikut! Sebutkan nama alkana tersebut menggunakan tata nama IUPAC.\n\n{self.options_text}'
        self.description_chinese = f'使用 IUPAC 命名法对结构式中所示的烷烃进行命名。\n\n{self.options_text}'
        self.description_arabic = f'سَمِّ الألكان الموضح في الصيغة البنائية وفق تسمية الأيوباك (IUPAC).\n\n{self.options_text}'
        self.description_hindi = f'संरचनात्मक सूत्र में दर्शाए गए एल्केन (alkane) का नाम IUPAC नामकरण पद्धति का उपयोग करके लिखिए।\n\n{self.options_text}'
        self.description_kazakh = f'IUPAC номенклатурасын пайдаланып құрылымдық формулада көрсетілген алканды атаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Taja jina la akani (alkane) iliyoonyeshwa kwenye fomula ya muundo (structural formula) kwa kutumia kanuni za majina za IUPAC.\n\n{self.options_text}"

class Chem061_multi(Chem061):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan rumus kerangka beberapa senyawa berikut dengan rumus molekul yang sama tercantum di bagian atas! Berapa isomer struktur yang ditampilkan?'
        self.description_chinese = '该图显示了顶部标注的具有相同分子式的化合物键线式。图中显示了多少个结构异构体？'
        self.description_arabic = 'يوضح الشكل صيغًا هيكلية لمركبات لها نفس الصيغة الجزيئية. كم عدد المتشكلات البنائية المعروضة؟'
        self.description_hindi = 'चित्र में शीर्ष पर प्रदर्शित समान आणविक सूत्र वाले यौगिकों के कंकाल सूत्र दर्शाए गए हैं। इस आरेख में कितने संरचनात्मक समावयव (structural isomers) दर्शाए गए हैं?'
        self.description_kazakh = 'Диаграммада жоғарғы жағында көрсетілген ортақ молекулалық формуласы бар қосылыстардың қаңқалы формулалары берілген. Қанша құрылымдық изомер көрсетілген?'
        self.description_swahili = f"Mchoro huu unaonyesha fomula za kiunzi (skeletal formulas) za kampaundi zinazoshiriki fomula ya molekuli (molecular formula) inayofanana iliyoonyeshwa hapo juu. Je, kuna isoma za muundo (structural isomers) ngapi zilizoonyeshwa?"

class Chem062_multi(Chem062):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram isomer geometri berikut! Identifikasi apakah isomer yang ditampilkan merupakan isomer E atau Z.'
        self.description_chinese = f'确定图中所示的异构体是 E 异构体还是 Z 异构体。'
        self.description_arabic = f'حدد ما إذا كان المتشكل الموضح هو المتشكل E أو Z.'
        self.description_hindi = f'आरेख में दर्शाए गए समावयव को पहचानें कि वह E समावयव है या Z समावयव है।'
        self.description_kazakh = f'Диаграммада көрсетілген изомердің E немесе Z изомер екенін анықтаңыз.'
        self.description_swahili = f"Tambua ikiwa isoma iliyoonyeshwa kwenye mchoro ni isoma ya E (E-isomer) au Z (Z-isomer)."

class Chem063_multi(Chem063):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram dua enantiomer suatu senyawa organik berikut! Salah satu enantiomer memutar cahaya terpolarisasi bidang sebesar {self.rotation}{self.rotation_value}°. Berdasarkan gugus-gugus yang ditampilkan pada diagram, pada nomor karbon berapakah dalam rantai utama pusat kiral tersebut berada?'
        self.description_chinese = f'该图显示了一种有机化合物的两种对映异构体。其中一种对映异构体使平面偏振光旋转 {self.rotation}{self.rotation_value}°。根据图中所示的基团，主链上位于哪个碳原子编号处的是手性中心？'
        self.description_arabic = f'يوضح الشكل المتشاكلين الضوئيين (enantiomers) لمركب عضوي. يقوم أحدهما بتدوير الضوء المستقطب بمقدار {self.rotation}{self.rotation_value}°. عند أي ذرة كربون في السلسلة الرئيسية يقع المركز الكيرالي؟'
        self.description_hindi = f'चित्र में एक कार्बनिक यौगिक के दो एनैन्टिओमर दिखाए गए हैं। एक एनैन्टिओमर (enantiomer) समतल-ध्रुवीकृत प्रकाश को {self.rotation}{self.rotation_value}° से घुमाता है। चित्र में दिखाए गए समूहों के आधार पर, मुख्य श्रृंखला में किस कार्बन संख्या पर काइरल केंद्र (chiral centre) स्थित है?'
        self.description_kazakh = f'Диаграммада органикалық қосылыстың екі энантиомері көрсетілген. Бір энантиомер жазық поляризацияланған жарықты {self.rotation}{self.rotation_value}° бұрады. Диаграммада көрсетілген топтарға сүйене отырып, негізгі тізбектегі хиральды орталық қай көміртек нөмірінде орналасқан?'
        self.description_swahili = f"Mchoro huu unaonyesha inantioma (enantiomers) mbili za kampaundi ya ogani. Inantioma moja inazungusha mwanga uliopolairishwa (plane-polarized light) kwa kiwango cha {self.rotation}{self.rotation_value}°. Kulingana na makundi yaliyoonyeshwa kwenye mchoro, kituo cha kairali (chiral centre) kipo kwenye kaboni namba ngapi katika mnyororo mkuu?"

class Chem064_multi(Chem064):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram mekanisme substitusi aromatik elektrofilik (SEAr) pada benzena berikut! Pereaksi dan kondisi reaksi tercantum pada diagram. Apakah elektrofil dalam reaksi ini?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了苯的亲电芳香取代机理。图中显示了试剂和条件。该反应中的亲电试剂是什么？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل آلية الاستبدال الأروماتي الإلكتروفيلي للبنزين. الكواشف والظروف موضحة. ما الإلكتروفيل في هذا التفاعل؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख बेंजीन इलेक्ट्रॉनरागी एरोमैटिक प्रतिस्थापन क्रियाविधि को दर्शाता है। अभिकर्मक और परिस्थितियां आरेख पर दिखाई गई हैं। इस अभिक्रिया में इलेक्ट्रॉनरागी (electrophile) क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада бензолдың электрофильді ароматты орынбасу механизмі көрсетілген. Реагенттер мен жағдайлар диаграммада көрсетілген. Бұл реакциядағы электрофиль қандай?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mfumo (mechanism) wa ubadilishaji wa aromatiki kielektrofili (electrophilic aromatic substitution) wa benzeni. Vitendanishi na masharti ya mmenyuko vimeonyeshwa kwenye mchoro. Je, elektrofili (electrophile) katika mmenyuko huu ni ipi?\n\n{self.options_text}"

class Chem065_multi(Chem065):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram tahap propagasi substitusi radikal bebas berikut! Reaktan ditampilkan pada diagram. Apakah produk organik yang terbentuk pada tahap ini?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了自由基取代反应的链增长阶段。图中显示了反应物。此步骤生成的有机产物是什么？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل خطوة انتشار في تفاعل استبدال الجذور الحرة. ما الناتج العضوي المتكون في هذه الخطوة؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख मुक्त मूलक प्रतिस्थापन के संचरण चरण (propagation step) को दर्शाता है। अभिकारक आरेख में दिखाए गए हैं। इस चरण में कौन सा कार्बनिक उत्पाद बनता है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада еркін радикалды орынбасудың тізбектің өсу сатысы көрсетілген. Реагенттер диаграммада көрсетілген. Бұл сатыда қандай органикалық өнім түзіледі?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha hatua ya uenezaji (propagation step) ya ubadilishaji wa radikali huru (free radical substitution). Vitendanishi vimeonyeshwa kwenye mchoro. Je, ni zao gani la ogani (organic product) linaloundwa katika hatua hii?\n\n{self.options_text}"

class Chem066_multi(Chem066):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram cincin benzena bernomor dengan gugus substituen berikut! Ketika senyawa ini mengalami substitusi elektrofilik lebih lanjut, posisi manakah yang akan lebih disukai oleh substituen baru?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了带有一个取代基并编了号的苯环。当该化合物发生进一步的亲电取代时，新的取代基将优先占据哪个（些）位置？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل حلقة بنزين مرقمة مع مجموعة بديلة. عند إجراء استبدال إلكتروفيلي إضافي، أي المواضع يُفضَّل أن يشغلها البديل الجديد؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख एक प्रतिस्थापी समूह के साथ एक क्रमांकित बेंजीन वलय को दर्शाता है। जब यह यौगिक आगे इलेक्ट्रॉनरागी प्रतिस्थापन से गुजरता है, तो नया प्रतिस्थापी अधिमानतः किस स्थान/किन स्थानों पर कब्जा करेगा?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада орынбасушы тобы бар нөмірленген бензол сақинасы көрсетілген. Бұл қосылыс одан әрі электрофильді орынбасуға ұшырағанда, жаңа орынбасушы қай орын(дар)ды артықшылықпен алады?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha pete ya benzeni (benzene ring) yenye namba na kundi-ambatisho (substituent group). Wakati kampaundi hii inapopitia ubadilishaji zaidi wa kielektrofili, je, kundi jipya litapendelea kuchukua nafasi (position) gani?\n\n{self.options_text}"

class Chem067_multi(Chem067):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan tabel tiga senyawa berikut! Urutkan senyawa-senyawa tersebut berdasarkan kenaikan keasaman (asam terlemah terlebih dahulu).\n\n{self.options_text}'
        self.description_chinese = f'表中显示了三种化合物。将它们按酸性增加的顺序排列（最弱的酸排在最前面）。\n\n{self.options_text}'
        self.description_arabic = f'يوضح الجدول ثلاثة مركبات. رتّبها تصاعديًا حسب الحمضية (الأضعف أولًا).\n\n{self.options_text}'
        self.description_hindi = f'तालिका में तीन यौगिक दर्शाए गए हैं। इन्हें अम्लता के बढ़ते क्रम में व्यवस्थित करें (सबसे दुर्बल अम्ल पहले)।\n\n{self.options_text}'
        self.description_kazakh = f'Кестеде үш қосылыс көрсетілген. Оларды қышқылдықтың өсу ретімен орналастырыңыз (ең әлсіз қышқыл бірінші).\n\n{self.options_text}'
        self.description_swahili = f"Jedwali hili linaonyesha kampaundi tatu. Zipange kulingana na kuongezeka kwa asidi (ukali wa asidi), ukianzia na asidi dhaifu zaidi.\n\n{self.options_text}"

class Chem068_multi(Chem068):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi fenol dengan pereaksi tertentu beserta kondisi reaksinya berikut! Apakah produk organik yang terbentuk?\n\n{self.options_text}'
        self.description_chinese = f'苯酚在图中所示条件下与试剂发生反应。生成的有机产物是什么？\n\n{self.options_text}'
        self.description_arabic = f'يتفاعل الفينول مع الكاشف تحت الظروف الموضحة. ما الناتج العضوي المتكون؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में दर्शाई गई परिस्थितियों में फिनोल (Phenol) अभिकर्मक के साथ अभिक्रिया करता है। बनने वाला कार्बनिक उत्पाद क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Фенол диаграммада көрсетілген жағдайларда реагентпен әрекеттеседі. Қандай органикалық өнім түзіледі?\n\n{self.options_text}'
        self.description_swahili = f"Fenoli humenyuka na kitendanishi (reagent) chini ya masharti yaliyoonyeshwa kwenye mchoro. Je, ni zao gani la ogani (organic product) linaloundwa?\n\n{self.options_text}"

class Chem069_multi(Chem069):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi oksidasi suatu alkohol berikut! Berdasarkan alkohol awal dan pereaksi yang tercantum pada gambar, apakah produk organik yang terbentuk?\n\n{self.options_text}'
        self.description_chinese = f'该图显示醇的氧化反应。根据图中所示的起始醇和试剂，生成的有机产物是什么？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل كحولًا يخضع لتفاعل أكسدة. بناءً على الكحول الابتدائي والكواشف الموضحة، ما الناتج العضوي المتكون؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में एक अल्कोहल की ऑक्सीकरण अभिक्रिया दर्शाई गई है। चित्र में दिखाए गए प्रारंभिक अल्कोहल और अभिकर्मकों के आधार पर, बनने वाला कार्बनिक उत्पाद क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Сызбада тотығу реакциясына түсетін спирт көрсетілген. Бастапқы спирт пен суретте көрсетілген реагенттерге сүйене отырып, түзілетін органикалық өнімді анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha alkoholi ikipitia mmenyuko wa oksidesheni (oxidation). Kulingana na alkoholi ya kuanzia na vitendanishi vilivyoonyeshwa kwenye picha, ni zao gani la ogani (organic product) linaloundwa?\n\n{self.options_text}"

class Chem070_multi(Chem070):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi berikut! Berdasarkan reaksi yang ditampilkan, apakah produk alkena utama yang terbentuk?\n\n{self.options_text}'
        self.description_chinese = f'根据图中所示的反应，生成的主要烯烃产物是什么？\n\n{self.options_text}'
        self.description_arabic = f'بناءً على التفاعل الموضح في الشكل، ما ناتج الألكين الرئيسي المتكون؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख में दर्शाई गई अभिक्रिया के आधार पर, बनने वाला मुख्य एल्कीन (alkene) उत्पाद क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада көрсетілген реакция негізінде қандай негізгі алкен өнімі түзіледі?\n\n{self.options_text}'
        self.description_swahili = f"Kulingana na mmenyuko ulioonyeshwa kwenye mchoro, ni zao kuu la alkeni (major alkene product) linaloundwa ni lipi?\n\n{self.options_text}"

class Chem071_multi(Chem071):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi klorida asil dengan nukleofil pada suhu kamar berikut! Apakah produk-produk reaksi tersebut?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了酰氯在室温下与亲核试剂发生反应。该反应的产物是什么？\n\n{self.options_text}'
        self.description_arabic = f'يتفاعل كلوريد أسيل مع نيوكليوفيل في درجة حرارة الغرفة كما هو موضح في الشكل. ما نواتج هذا التفاعل؟\n\n{self.options_text}'
        self.description_hindi = f'एक एसाइल क्लोराइड कमरे के तापमान पर एक नाभिकरागी (nucleophile) के साथ अभिक्रिया करता है, जैसा कि आरेख में दिखाया गया है। इस अभिक्रिया के उत्पाद क्या हैं?\n\n{self.options_text}'
        self.description_kazakh = f'Ацилхлорид диаграммада көрсетілгендей бөлме температурасында нуклеофильмен әрекеттеседі. Бұл реакцияның өнімдері қандай?\n\n{self.options_text}'
        self.description_swahili = f"Kloraidi ya asili (acyl chloride) humenyuka na nukleofili (nucleophile) kwenye halijoto ya chumba, kama inavyoonyeshwa kwenye mchoro. Je, mazao (products) ya mmenyuko huu ni yapi?\n\n{self.options_text}"

class Chem072_multi(Chem072):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram batang laju hidrolisis relatif tiga senyawa berklorin dengan air pada suhu kamar berikut (skala logaritmik)! Satu batang disorot berwarna emas. Berapa nilai laju hidrolisis relatif yang ditunjukkan untuk batang yang disorot tersebut?'
        self.description_chinese = '柱状图以对数刻度显示了室温下三种含氯化合物与水水解的相对速率。其中一个柱体以金色突出显示。突出显示的柱体代表的相对水解速率是多少？'
        self.description_arabic = 'يوضح المخطط الشريطي معدلات التحلل المائي النسبية لثلاثة مركبات تحتوي على الكلور مع الماء عند درجة حرارة الغرفة، مرسومة على مقياس لوغاريتمي. تم تمييز أحد الأعمدة باللون الذهبي. ما معدل التحلل المائي النسبي لهذا العمود؟'
        self.description_hindi = 'बार चार्ट कमरे के तापमान पर पानी के साथ तीन क्लोरीन युक्त यौगिकों के जल-अपघटन की सापेक्ष दरों को दर्शाता है, जिन्हें लघुगणकीय पैमाने पर आलेखित किया गया है। एक बार को सुनहरे रंग में हाइलाइट किया गया है। हाइलाइट किए गए बार के लिए दिखाई गई जल-अपघटन की सापेक्ष दर क्या है?'
        self.description_kazakh = 'Бағаналы диаграммада логарифмдік шкала бойынша салынған бөлме температурасында құрамында хлор бар үш қосылыстың сумен гидролизденуінің салыстырмалы жылдамдықтары көрсетілген. Бір бағана алтын түспен бөлініп көрсетілген. Бөлініп көрсетілген бағана үшін қандай салыстырмалы гидролиз жылдамдығы көрсетілген?'
        self.description_swahili = f"Chati hii ya mihimili (bar chart) inaonyesha kasi kilinganisho za hidrolisisi (relative rates of hydrolysis) ya kampaundi tatu zenye klorini zikimenyana na maji kwenye halijoto ya chumba, kwa kutumia skeli ya logariti. Mhimili mmoja umeangaziwa kwa rangi ya dhahabu. Je, ni kasi gani kilinganisho ya hidrolisisi iliyoonyeshwa kwenye mhimili huo ulioangaziwa?"

class Chem073_multi(Chem073):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi asil klorida (RCOCl) dengan pereaksi yang rumusnya tercantum pada diagram berikut! Apakah produk organik yang terbentuk?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了酰氯 (RCOCl) 与一种试剂发生反应，图中给出了试剂的化学式。生成的有机产物是什么？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل تفاعل كلوريد أسيل (RCOCl) مع كاشف تظهر صيغته في الشكل. ما الناتج العضوي المتكون؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख एक एसाइल क्लोराइड (RCOCl) को एक अभिकर्मक के साथ अभिक्रिया करते हुए दर्शाता है जिसका सूत्र आरेख में दिखाया गया है। बनने वाला कार्बनिक उत्पाद क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада формуласы диаграммада көрсетілген реагентпен әрекеттесетін ацилхлорид (RCOCl) көрсетілген. Қандай органикалық өнім түзіледі?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha kloraidi ya asili (acyl chloride - RCOCl) ikimenyuka na kitendanishi ambacho fomula yake imeonyeshwa kwenye mchoro. Je, ni zao gani la ogani (organic product) linaloundwa?\n\n{self.options_text}"

class Chem074_multi(Chem074):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram struktur suatu asam amino pada tiga nilai pH berbeda berikut! Struktur manakah (A, B, atau C) yang merepresentasikan zwiterion?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了在三种不同 pH 值下某氨基酸的结构。哪种结构（A、B 或 C）代表两性离子？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل تركيب حمض أميني عند ثلاث قيم مختلفة للرقم الهيدروجيني (pH). أي تركيب (A أو B أو C) يمثل الأيون المزدوج (zwitterion)؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख तीन अलग-अलग pH मानों पर एक अमीनो अम्ल की संरचना को दर्शाता है। कौन सी संरचना (A, B, या C) ज़्विटरआयन (zwitterion) का प्रतिनिधित्व करती है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада үш түрлі pH мәніндегі аминқышқылының құрылымы көрсетілген. Қай құрылым (A, B немесе C) цвиттерионды білдіреді?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha muundo wa asidi amino (amino acid) katika thamani tatu tofauti za pH. Je, ni muundo gani (A, B, au C) unaowakilisha zwitaioni (zwitterion)?\n\n{self.options_text}"

class Chem075_multi(Chem075):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram strip elektroforesis untuk suatu asam amino berikut dengan pH dan titik isoelektrik (pI) yang tercantum! Ke arah manakah asam amino tersebut akan bermigrasi ketika tegangan diterapkan?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了氨基酸的电泳条。根据图中标注的 pH 和等电点（pI），施加电压时该氨基酸将向哪个方向迁移？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل شريط رحلان كهربائي (electrophoresis) لحمض أميني. بناءً على قيمة pH ونقطة التعادل الكهربي (pI) الموضحتين، في أي اتجاه سيتحرك الحمض الأميني عند تطبيق جهد كهربائي؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में एक अमीनो अम्ल (amino acid) के लिए इलेक्ट्रोफोरेसिस स्ट्रिप (electrophoresis strip) दिखाई गई है। चित्र में दर्शाए गए pH और समविद्युत बिंदु (pI) के आधार पर, वोल्टेज लगाने पर अमीनो अम्ल (amino acid) किस दिशा में गति करेगा?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада аминқышқылына арналған электрофорез жолағы көрсетілген. Диаграммада көрсетілген pH пен изоэлектрлік нүктеге (pI) сүйене отырып, кернеу берілгенде аминқышқылы қай бағытта жылжиды?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mchakato wa kielektroforesisi (electrophoresis) wa asidi amino. Kulingana na pH na kiwango cha isoelektriki (pI) vilivyoonyeshwa, je, asidi amino hiyo itahamia upande gani wakati mkondo wa umeme (voltage) utakapowekwa?\n\n{self.options_text}"

class Chem076_multi(Chem076):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram skema reaksi pembentukan amida berikut! Berdasarkan kondisi yang tercantum pada tanda panah reaksi, pereaksi apakah yang digunakan dalam metode ini?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了酰胺形成的反应机理。根据反应箭头上显示的条件，此方法中使用了哪些试剂？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل تفاعل تكوين أميد. بناءً على الظروف الموضحة على سهم التفاعل، ما الكواشف المستخدمة في هذه الطريقة؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख में एमाइड (amide) निर्माण की अभिक्रिया योजना दर्शाई गई है। अभिक्रिया तीर पर दर्शाई गई स्थितियों के आधार पर, इस विधि में किन अभिकर्मकों का उपयोग किया जाता है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада амид түзілуінің реакция сұлбасы көрсетілген. Реакция көрсеткісінде көрсетілген жағдайларға сүйене отырып, бұл әдісте қандай реагенттер қолданылатынын анықтаңыз?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mpango wa mmenyuko (reaction scheme) wa uundaji wa amidi (amide formation). Kulingana na masharti yaliyoonyeshwa kwenye mshale wa mmenyuko, ni vitendanishi (reagents) gani vinavyotumika katika njia hii?\n\n{self.options_text}"

class Chem077_multi(Chem077):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram dua monomer yang bereaksi membentuk poliamida berikut! Berdasarkan struktur monomer yang ditampilkan, manakah satuan ulang polimer ini?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了两种单体反应生成聚酰胺的过程。根据图中显示的单体结构，以下哪项是该聚合物的重复单元？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل مونومرين يتفاعلان لتكوين بولي أميد. بناءً على التراكيب الموضحة، أي مما يلي يمثل وحدة التكرار لهذا البوليمر؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में दो मोनोमर आपस में क्रिया करके एक पॉलीएमाइड (polyamide) बनाते हैं। चित्र में दर्शाई गई मोनोमर संरचनाओं के आधार पर, निम्नलिखित में से कौन सा इस पॉलीमर की पुनरावर्ती इकाई है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада полиамид түзу үшін әрекеттесетін екі мономер көрсетілген. Диаграммада көрсетілген мономер құрылымдарына сүйене отырып, төмендегілердің қайсысы осы полимердің қайталанатын құрылымдық буыны болып табылады?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha monoma (monomers) mbili zikimenyuka kuunda poliamidi (polyamide). Kulingana na miundo ya monoma iliyoonyeshwa, ni ipi kati ya zifuatazo ni uniti ya kujirudia (repeat unit) ya polima hii?\n\n{self.options_text}"

class Chem078_multi(Chem078):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram dua monomer yang bereaksi membentuk poliester berikut! Berdasarkan struktur monomer yang ditampilkan, manakah satuan ulang polimer ini?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了两种单体反应生成聚酯的过程。根据图中显示的单体结构，以下哪项是该聚合物的重复单元？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل مونومرين يتفاعلان لتكوين بولي إستر. بناءً على التراكيب الموضحة، أي مما يلي يمثل وحدة التكرار لهذا البوليمر؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में दो मोनोमर आपस में क्रिया करके पॉलीएस्टर (polyester) बनाते हैं। चित्र में दर्शाई गई मोनोमर संरचनाओं के आधार पर, निम्नलिखित में से कौन सा इस पॉलीमर की पुनरावर्ती इकाई है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада полиэфир түзу үшін әрекеттесетін екі мономер көрсетілген. Диаграммада көрсетілген мономер құрылымдарына сүйене отырып, төмендегілердің қайсысы осы полимердің қайталанатын құрылымдық буыны болып табылады?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha monoma (monomers) mbili zikimenyuka kuunda poliesta (polyester). Kulingana na miundo ya monoma iliyoonyeshwa kwenye mchoro, ni ipi kati ya zifuatazo ni uniti ya kujirudia (repeat unit) ya polima hii?\n\n{self.options_text}"

class Chem079_multi(Chem079):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan satuan ulang suatu polimer adisi yang ditampilkan pada diagram berikut! Apakah monomer yang digunakan untuk membuat polimer ini?\n\n{self.options_text}'
        self.description_chinese = f'图中显示了加成聚合物的重复单元。用于制造这种聚合物的单体是什么？\n\n{self.options_text}'
        self.description_arabic = f'تُظهر الصورة وحدة التكرار لبوليمر إضافة. ما المونومر المستخدم لتكوين هذا البوليمر؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में एक योगात्मक पॉलीमर की आवर्ती इकाई दिखाई गई है। इस पॉलीमर को बनाने में प्रयुक्त मोनोमर कौन सा है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада қосылу полимерінің қайталанатын құрылымдық буыны көрсетілген. Осы полимерді жасау үшін қандай мономер қолданылды?\n\n{self.options_text}'
        self.description_swahili = f"Uniti ya kujirudia (repeating unit) ya polima ya nyongeza (addition polymer) inaonyeshwa kwenye mchoro. Je, ni monoma gani inayotumika kutengeneza polima hii?\n\n{self.options_text}"

class Chem080_multi(Chem080):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan tabel informasi tentang jenis ikatan kimia dan mekanisme degradasi tiga polimer berikut! {self.scenario['question']}\n\n{self.options_text}"
        self.description_chinese = f"该表提供了有关三种聚合物的化学键和降解机理的信息。{self.scenario['question']}\n\n{self.options_text}"
        self.description_arabic = f'يوضح الجدول معلومات حول الروابط الكيميائية وآليات التحلل لثلاثة بوليمرات. {self.scenario["question"]}\n\n{self.options_text}'
        self.description_hindi = f"यह तालिका तीन पॉलिमरों के रासायनिक बंधनों और अपघटन तंत्रों के बारे में जानकारी प्रदान करती है। {self.scenario['question']}\n\n{self.options_text}"
        self.description_kazakh = f"Кестеде үш полимердің химиялық байланыстары мен ыдырау механизмдері туралы ақпарат берілген. {self.scenario['question']}\n\n{self.options_text}"
        self.description_swahili = f"Jedwali hili linatoa maelezo kuhusu viungo vya kikemikali (chemical linkages) na mifumo ya uozeshaji (degradation mechanisms) ya polima tatu. {self.scenario['question']}\n\n{self.options_text}"

class Chem081_multi(Chem081):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram monomer-monomer yang digunakan dalam polimerisasi kondensasi berikut! Berdasarkan gugus fungsi yang ditampilkan, jenis polimer apakah yang terbentuk?\n\n{self.options_text}'
        self.description_chinese = f'图中显示了缩聚反应中使用的单体。根据图中所示的官能团，会形成哪种类型的聚合物？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل المونومرات المستخدمة في بلمرة تكاثفية. بناءً على المجموعات الوظيفية الموضحة، ما نوع البوليمر المتكون؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में संघनन बहुलकीकरण में प्रयुक्त मोनोमर पदार्थ दर्शाए गए हैं। चित्र में दर्शाए गए कार्यात्मक समूहों के आधार पर, किस प्रकार का पॉलीमर बनता है?\n\n{self.options_text}'
        self.description_kazakh = f'Сызбада поликонденсациялану (конденсациялық полимерлену) реакциясында қолданылатын мономерлер көрсетілген. Сызбада көрсетілген функционалдық топтарға сүйене отырып, полимердің қай түрі түзілетінін анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha monoma (monomers) zinazotumika katika polimerishaji ya ufidishaji (condensation polymerization). Kulingana na makundi-kazi (functional groups) yaliyoonyeshwa kwenye mchoro, ni aina gani ya polima inayoundwa?\n\n{self.options_text}"

class Chem082_multi(Chem082):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram sintesis organik dua tahap berikut dengan bahan awal dan produk akhir yang dilabeli! Berdasarkan jalur reaksi dan kondisi yang ditampilkan, apakah senyawa antara (intermediat) yang tersembunyi?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了一个两步有机合成过程，并标明了起始原料和最终产物。根据显示的反应途径和条件，隐藏的中间体化合物是什么？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل تخليقًا عضويًا من خطوتين مع توضيح المادة البادئة والناتج النهائي. بناءً على مسار التفاعل والظروف، ما المركب الوسيط المخفي؟\n\n{self.options_text}'
        self.description_hindi = f'आरेख प्रारंभिक सामग्री और अंतिम उत्पाद के लेबल के साथ दो-चरणीय कार्बनिक संश्लेषण को दिखाता है। दिखाए गए अभिक्रिया पथ और स्थितियों के आधार पर, छिपा हुआ मध्यवर्ती यौगिक क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада бастапқы заты мен соңғы өнімі белгіленген екі сатылы органикалық синтез көрсетілген. Көрсетілген реакция жолы мен жағдайларына сүйене отырып, жасырын аралық қосылысты анықтаңыз?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha usanisi wa kikaboni (organic synthesis) wa hatua mbili ukiwa na malighafi ya kuanzia na zao la mwisho yakiwa yamewekewa lebo. Kulingana na njia ya mmenyuko na masharti yaliyoonyeshwa, ni kiambata gani cha kati (intermediate compound) kilichofichwa?\n\n{self.options_text}"

class Chem083_multi(Chem083):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram rute sintesis multitahap berikut dengan senyawa antara yang disembunyikan! Berdasarkan bahan awal dan produk akhir yang ditampilkan, identifikasi senyawa antara tersebut.\n\n{self.options_text}'
        self.description_chinese = f'该图显示了具有隐藏中间体的多步合成路线。根据图中显示的起始原料和最终产物，鉴定该中间体化合物。\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل مسار تخليق متعدد الخطوات مع وسيط مخفي. بناءً على المادة البادئة والناتج النهائي، حدد المركب الوسيط.\n\n{self.options_text}'
        self.description_hindi = f'चित्र में एक छिपे हुए मध्यवर्ती यौगिक के साथ बहु-चरणीय संश्लेषण मार्ग दर्शाया गया है। चित्र में दर्शाए गए प्रारंभिक पदार्थ और अंतिम उत्पाद के आधार पर, मध्यवर्ती यौगिक की पहचान कीजिए।\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада жасырын аралық заты бар көп сатылы синтез жолы көрсетілген. Диаграммада көрсетілген бастапқы зат пен соңғы өнімге сүйене отырып, аралық қосылысты анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha njia ya usanisi (synthesis route) ya hatua nyingi ikiwa na kiambata cha kati kilichofichwa. Kulingana na malighafi ya kuanzia na zao la mwisho vilivyoonyeshwa kwenye mchoro, tambua kiambata hicho cha kati (intermediate compound).\n\n{self.options_text}"

class Chem084_multi(Chem084):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan spektrum massa berikut yang menampilkan beberapa puncak! Berdasarkan nilai m/z yang ditunjukkan oleh tanda panah pada diagram, identifikasi ion fragmen yang bertanggung jawab atas puncak tersebut.\n\n{self.options_text}'
        self.description_chinese = f'质谱图显示了几个峰。根据图中箭头指示的m/z值，找出产生此峰的碎片离子。\n\n{self.options_text}'
        self.description_arabic = f'يُظهر طيف الكتلة عدة قمم. بناءً على قيمة m/z المشار إليها بالسهم، حدد الأيون المجزأ المسؤول عن هذه القمة.\n\n{self.options_text}'
        self.description_hindi = f'द्रव्यमान स्पेक्ट्रम में कई शिखर दिखाई देते हैं। आरेख में तीर द्वारा दर्शाए गए m/z मान के आधार पर, इस शिखर के लिए जिम्मेदार खंड आयन की पहचान करें।\n\n{self.options_text}'
        self.description_kazakh = f'Масс-спектрде бірнеше шың көрсетілген. Диаграммадағы жебемен көрсетілген m/z мәніне сүйене отырып, осы шыңға жауапты фрагменттік ионды анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Spektra ya masi (mass spectrum) inaonyesha vilele (peaks) kadhaa. Kulingana na thamani ya m/z inayoonyeshwa na mshale kwenye mchoro, tambua ioni ya kipande (fragment ion) inayohusika na kilele hiki.\n\n{self.options_text}"

class Chem085_multi(Chem085):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan diagram plat KLT (Kromatografi Lapis Tipis) dari suatu percobaan kromatografi berikut! Jarak-jarak pergerakan tercantum pada diagram. Hitunglah nilai Rf untuk {self.questioned_spot['name']}."
        self.description_chinese = f"该图显示了色谱实验中的薄层色谱板。图中标注了距离。计算 {self.questioned_spot['name']} 的 Rf 值。"
        self.description_arabic = f'يوضح الشكل لوحة كروماتوغرافيا الطبقة الرقيقة (TLC) مع المسافات المشار إليها. احسب قيمة Rf لـ {self.questioned_spot["name"]}.'
        self.description_hindi = f"चित्र में क्रोमैटोग्राफी (chromatography) प्रयोग से प्राप्त TLC प्लेट दर्शाई गई है। दूरियाँ चित्र पर अंकित हैं। {self.questioned_spot['name']} के लिए Rf मान की गणना कीजिए।"
        self.description_kazakh = f"Сызбада хроматографиялық эксперименттегі ЖҚХ (жұқа қабатты хроматография) пластинкасы көрсетілген. Сызбада қашықтықтар белгіленген. {self.questioned_spot['name']} үшін Rf мәнін есептеңіз."
        self.description_swahili = f"Mchoro huu unaonyesha sahani ya TLC kutokana na jaribio la kromatografia (chromatography). Umbali mbalimbali umewekewa maelezo kwenye mchoro. Kokotoa thamani ya Rf (Rf value) ya {self.questioned_spot['name']}."

class Chem086_multi(Chem086):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan kromatogram gas berikut yang menampilkan {self.num_peaks} puncak! Hitunglah komposisi persentase {self.questioned_peak['name']} berdasarkan luas puncak yang ditampilkan pada diagram."
        self.description_chinese = f"气相色谱图显示了{self.num_peaks}个峰。根据图中显示的峰面积，计算{self.questioned_peak['name']}的百分比组成。"
        self.description_arabic = f'يُظهر كروماتوغرام الغاز {self.num_peaks} قممًا. احسب النسبة المئوية لـ {self.questioned_peak["name"]} باستخدام مساحات القمم الموضحة.'
        self.description_hindi = f"एक गैस क्रोमैटोग्राम (chromatogram) में {self.num_peaks} पीक दिखाई दे रहे हैं। आरेख में दर्शाए गए पीक क्षेत्रफल के आधार पर {self.questioned_peak['name']} की प्रतिशत संघटन की गणना कीजिए।"
        self.description_kazakh = f"Газ хроматограммасында {self.num_peaks} шың көрсетілген. Диаграммада көрсетілген шың аудандарын ескере отырып, {self.questioned_peak['name']} пайыздық құрамын есептеңіз."
        self.description_swahili = f"Kromatogramu ya gesi (gas chromatogram) inaonyesha vilele (peaks) {self.num_peaks}. Kokotoa asilimia ya muundo (percentage composition) ya {self.questioned_peak['name']} kulingana na eneo la vilele (peak areas) lililoonyeshwa kwenye mchoro."

class Chem087_multi(Chem087):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan spektrum IR berikut dengan serapan karakteristik dan bilangan gelombangnya yang tercantum pada diagram! Gugus fungsi apakah yang bertanggung jawab atas serapan yang dilabeli tersebut?\n\n{self.options_text}'
        self.description_chinese = f'IR光谱显示了特征吸收峰，波数已在图中标注。哪个官能团产生了该标记的吸收峰？\n\n{self.options_text}'
        self.description_arabic = f'يُظهر طيف الأشعة تحت الحمراء (IR) امتصاصًا مميزًا مع عدد موجي محدد. ما المجموعة الوظيفية المسؤولة عن هذا الامتصاص؟\n\n{self.options_text}'
        self.description_hindi = f'IR स्पेक्ट्रम में एक विशिष्ट अवशोषण दिखाई देता है, जिसका तरंग संख्या आरेख पर अंकित है। इस अवशोषण के लिए कौन सा कार्यात्मक समूह जिम्मेदार है?\n\n{self.options_text}'
        self.description_kazakh = f'IR спектрінде диаграммада толқын саны белгіленген сипаттамалық жұтылу көрсетілген. Белгіленген жұтылуға қай функционалдық топ жауапты?\n\n{self.options_text}'
        self.description_swahili = f"Spektra ya IR (IR spectrum) inaonyesha ufyonzaji bainifu (characteristic absorption) huku nambari ya wimbi (wavenumber) ikiwa imewekewa maelezo kwenye mchoro. Je, ni kikundi-kazi (functional group) kipi kinachosababisha ufyonzaji huo uliowekewa lebo?\n\n{self.options_text}"

class Chem088_multi(Chem088):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan spektrum ¹H NMR suatu senyawa organik berikut! Satu puncak disorot dengan pergeseran kimia (δ) dan integrasinya yang tercantum pada diagram. Lingkungan hidrogen manakah yang diwakili oleh puncak yang dilabeli tersebut?\n\n{self.options_text}'
        self.description_chinese = f'图中显示了某有机化合物的¹H NMR谱图。其中一个峰被突出显示，图中标注了其化学位移(δ)和积分值。标记的峰代表哪种氢环境？\n\n{self.options_text}'
        self.description_arabic = f'يُظهر طيف ¹H NMR قمة مميزة مع انزياح كيميائي (δ) وتكامل موضحين. ما بيئة الهيدروجين التي تمثلها هذه القمة؟\n\n{self.options_text}'
        self.description_hindi = f'एक कार्बनिक यौगिक का ¹H NMR स्पेक्ट्रम दर्शाया गया है। एक पीक को हाइलाइट किया गया है और आरेख पर उसका रासायनिक विस्थापन (δ) और समाकलन अंकित है। चिह्नित पीक किस हाइड्रोजन वातावरण को दर्शाता है?\n\n{self.options_text}'
        self.description_kazakh = f'Органикалық қосылыстың ¹H NMR спектрі көрсетілген. Химиялық ығысуы (δ) және интеграциясы диаграммада белгіленген бір шың ерекшеленген. Белгіленген шың қандай сутек ортасын білдіреді?\n\n{self.options_text}'
        self.description_swahili = f"Spektra ya ¹H NMR (¹H NMR spectrum) ya kiambata cha kikaboni inaonyeshwa. Kilele kimoja kimeangaziwa huku msogeo wake wa kikemikali (δ) na integresheni (integration) vikiwa vimeonyeshwa kwenye mchoro. Je, kilele hicho kilichowekewa lebo kinawakilisha mazingira gani ya hidrojeni (hydrogen environment)?\n\n{self.options_text}"

class Chem089_multi(Chem089):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan spektrum ¹³C NMR suatu senyawa organik berikut! Berapa puncak yang muncul dalam spektrum tersebut? (Berikan jawaban berupa bilangan bulat.)'
        self.description_chinese = '下图显示了某有机化合物的¹³C NMR谱图。谱图中出现了多少个峰？（请给出一个数字答案。）'
        self.description_arabic = 'يوضح طيف ¹³C NMR لمركب عضوي. كم عدد القمم في الطيف؟ (أعطِ إجابة عددية).'
        self.description_hindi = 'नीचे एक कार्बनिक यौगिक का ¹³C NMR स्पेक्ट्रम दिखाया गया है। स्पेक्ट्रम में कितने पीक दिखाई देते हैं? (संख्यात्मक उत्तर दें।)'
        self.description_kazakh = 'Төменде органикалық қосылыстың ¹³C NMR спектрі көрсетілген. Спектрде қанша шың пайда болады? (Сандық жауап беріңіз.)'
        self.description_swahili = f"Spektra ya ¹³C NMR (¹³C NMR spectrum) ya kiambata cha kikaboni inaonyeshwa hapa chini. Je, ni vilele vingapi vinavyoonekana kwenye spektra hiyo? (Toa jibu kwa namba.)"

class Chem090_multi(Chem090):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan gambar puncak spektrum ¹H NMR berikut beserta pergeseran kimia (δ) dan integrasinya yang tercantum! Berdasarkan pola yang ditampilkan pada diagram, apakah pola pembelahan (splitting pattern) puncak ini?\n\n{self.options_text}'
        self.description_chinese = f'图像显示了¹H NMR谱图中的一个峰，以及它的化学位移(δ)和积分值。根据图中显示的模式，该峰的裂分峰型是什么？\n\n{self.options_text}'
        self.description_arabic = f'تُظهر الصورة قمة من طيف ¹H NMR مع الانزياح الكيميائي (δ) والتكامل. بناءً على النمط، ما نوع الانقسام لهذه القمة؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में ¹H NMR स्पेक्ट्रम का एक पीक, उसके रासायनिक विस्थापन (δ) और समाकलन को दर्शाया गया है। चित्र में दिखाए गए पैटर्न के आधार पर, इस पीक का विभाजन पैटर्न क्या है?\n\n{self.options_text}'
        self.description_kazakh = f'Суретте ¹H NMR спектрінің шыңы, оның химиялық ығысуы (δ) және интеграциясы көрсетілген. Диаграммада көрсетілген үлгіге сүйене отырып, бұл шыңның ыдырау сипаты қандай?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha kilele (peak) kutoka kwenye spektra ya ¹H NMR, pamoja na msogeo wake wa kikemikali (δ) na integresheni (integration). Kulingana na msururu wa mgawanyiko (splitting pattern) unaoonyeshwa kwenye mchoro, je, kilele hiki kimegawanyika vipi?\n\n{self.options_text}"

class Chem091_multi(Chem091):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan tabel data hasil analisis suatu senyawa organik tak dikenal menggunakan Spektrometri Massa, Spektroskopi IR, dan ¹H NMR berikut! Berdasarkan data gabungan tersebut, identifikasi senyawa tersebut.\n\n{self.options_text}'
        self.description_chinese = f'使用质谱法、IR光谱法和¹H NMR分析了一种未知的有机化合物。根据表中提供的综合数据，鉴定该化合物。\n\n{self.options_text}'
        self.description_arabic = f'تم تحليل مركب عضوي غير معروف باستخدام مطيافية الكتلة، والأشعة تحت الحمراء (IR)، و ¹H NMR. بناءً على البيانات، حدد المركب.\n\n{self.options_text}'
        self.description_hindi = f'एक अज्ञात कार्बनिक यौगिक का विश्लेषण मास स्पेक्ट्रोमेट्री, IR स्पेक्ट्रोस्कोपी और ¹H NMR का उपयोग करके किया गया। तालिका में दिए गए संयुक्त आंकड़ों के आधार पर, यौगिक की पहचान करें।\n\n{self.options_text}'
        self.description_kazakh = f'Белгісіз органикалық қосылыс масс-спектрометрия, IR спектроскопия және ¹H NMR көмегімен талданды. Кестеде берілген біріктірілген деректерге сүйене отырып, қосылысты анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Kiambata cha kikaboni (organic compound) kisichojulikana kilichanganuliwa kwa kutumia spektrometri ya masi (Mass Spectrometry), spektroskopi ya IR, na ¹H NMR. Kulingana na data iliyojumuishwa kwenye jedwali, tambua kiambata hicho.\n\n{self.options_text}"

class Chem092_multi(Chem092):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram siklus energi Born-Haber untuk suatu senyawa ionik berikut! Berdasarkan spesies kimia dan arah panah yang ditampilkan pada gambar, perubahan entalpi apakah yang diwakili oleh tahap {self.asked_step}?\n\n{self.options_text}'
        self.description_chinese = f'图中显示了离子化合物的Born-Haber能量循环。根据图像中的化学物种和箭头方向，步骤{self.asked_step}代表什么焓变？\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل دورة بورن-هابر لمركب أيوني. بناءً على الأنواع الكيميائية واتجاه السهم، ما التغير في المحتوى الحراري الذي تمثله الخطوة {self.asked_step}؟\n\n{self.options_text}'
        self.description_hindi = f'चित्र में एक आयनिक यौगिक के लिए बोर्न-हैबर ऊर्जा चक्र (Born-Haber energy cycle) दर्शाया गया है। चित्र में रासायनिक प्रजाति और तीर की दिशा के आधार पर, चरण {self.asked_step} किस एन्थैल्पी परिवर्तन को दर्शाता है?\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада иондық қосылыс үшін Борн-Габер энергетикалық циклі көрсетілген. Химиялық бөлшектер мен суреттегі жебе бағытына сүйене отырып, {self.asked_step} сатысы энтальпияның қандай өзгерісін білдіреді?\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mzunguko wa nishati wa Born-Haber (Born-Haber cycle) wa kiambata cha iyoniki (ionic compound). Kulingana na spishi za kikemikali na mwelekeo wa mshale kwenye mchoro, ni mabadiliko gani ya entalpi (enthalpy change) yanayowakilishwa na hatua ya {self.asked_step}?\n\n{self.options_text}"

class Chem093_multi(Chem093):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan sel elektrokimia yang dibangun menggunakan dua setengah sel berikut! Gunakan potensial elektrode standar (E°) yang tercantum pada gambar untuk menghitung GGL sel standar (E°sel) dalam V.'
        self.description_chinese = '使用图中显示的两个半电池构建了一个电化学电池。使用图中提供的标准电极电势(E°)，计算标准电池电动势(E°cell)，单位为V。'
        self.description_arabic = 'تُبنى خلية كهروكيميائية باستخدام نصفي الخلية الموضحين. باستخدام جهود الأقطاب القياسية (E°)، احسب القوة الدافعة الكهربائية القياسية للخلية (E°cell) بوحدة V.'
        self.description_hindi = 'चित्र में दर्शाए गए दो अर्ध-सेल का उपयोग करके एक विद्युतरासायनिक सेल का निर्माण किया जाता है। चित्र में दिए गए मानक इलेक्ट्रोड विभव (E°) का उपयोग करके, मानक सेल विद्युत वाहक बल (E°cell) की गणना V में कीजिए।'
        self.description_kazakh = 'Электрохимиялық ұяшық диаграммада көрсетілген екі жартылай ұяшықты пайдаланып құрастырылған. Суретте берілген стандартты электродтық потенциалдарды (E°) пайдаланып, стандартты ұяшықтың ЭҚК-ін (E°cell) В өлшемімен есептеңіз.'
        self.description_swahili = f"Seli ya kielektrokemikali (electrochemical cell) inajengwa kwa kutumia nusu-seli mbili zinazoonyeshwa kwenye mchoro. Kwa kutumia uwezo wa kawaida wa elektrodi (E°) unaotolewa kwenye mchoro, kokotoa EMF ya kawaida ya seli (E°cell) katika V."

class Chem094_multi(Chem094):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan kurva titrasi berikut! Berdasarkan grafik yang ditampilkan, {'berapa volume titran yang diperlukan untuk mencapai titik ekuivalen?' if self.q_type == 'equivalence_vol' else 'berapa pH pada titik ekuivalen?'}"
        self.description_chinese = f"图像显示了滴定曲线。根据提供的图表，{('达到滴定终点需要多少体积的滴定剂？' if self.q_type == 'equivalence_vol' else '当量点的pH值是多少？')}"
        self.description_arabic = f'يوضح الشكل منحنى معايرة. بناءً على الرسم البياني، {("ما حجم المعاير اللازم للوصول إلى نقطة التكافؤ؟" if self.q_type == "equivalence_vol" else "ما قيمة pH عند نقطة التكافؤ؟")}'
        self.description_hindi = f"चित्र में अनुमापन वक्र दर्शाया गया है। दिए गए ग्राफ़ के आधार पर, {('तुल्यता बिंदु तक पहुँचने के लिए अनुमापक की कितनी मात्रा आवश्यक है?' if self.q_type == 'equivalence_vol' else 'तुल्यता बिंदु पर pH क्या है?')}"
        self.description_kazakh = f"Суретте титрлеу қисығы көрсетілген. Берілген графикке сүйене отырып, {('эквиваленттік нүктеге жету үшін титранттың қандай көлемі қажет?' if self.q_type == 'equivalence_vol' else 'эквиваленттік нүктедегі pH мәні қандай?')}"
        self.description_swahili = f"Mchoro huu unaonyesha mzingo wa taitresheni (titration curve). Kulingana na grafu iliyotolewa, {('ni kiasi gani cha taitrati (titrant) kinahitajika ili kufikia hatua ya usawa (equivalence point)?' if self.q_type == 'equivalence_vol' else 'ni nini thamani ya pH katika hatua ya usawa (equivalence point)?')}"

class Chem095_multi(Chem095):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan grafik plot Arrhenius (ln k vs 1/T) untuk suatu reaksi kimia berikut! Gradien garis tercantum pada diagram. Hitunglah energi aktivasi Ea dalam kJ mol⁻¹.'
        self.description_chinese = '该图显示了化学反应的Arrhenius图(ln k 对 1/T)。直线的斜率已在图中标注。计算活化能Ea，单位为kJ mol⁻¹。'
        self.description_arabic = 'يُظهر الرسم البياني مخطط أرهينيوس (ln k مقابل 1/T). احسب طاقة التنشيط Ea (بوحدة kJ mol⁻¹) باستخدام ميل الخط.'
        self.description_hindi = 'ग्राफ में एक रासायनिक अभिक्रिया के लिए आर्हेनियस प्लॉट (Arrhenius plot) (ln k बनाम 1/T) दर्शाया गया है। रेखा की ढलान आरेख पर अंकित है। सक्रियण ऊर्जा, Ea, की गणना kJ mol⁻¹ में करें।'
        self.description_kazakh = 'Графикте химиялық реакция үшін Аррениус графигі (ln k мен 1/T) көрсетілген. Түзудің градиенті диаграммада белгіленген. Ea активтену энергиясын кДж·моль⁻¹ өлшемінде есептеңіз.'
        self.description_swahili = f"Grafu hii inaonyesha ploti ya Arrhenius (ln k dhidi ya 1/T) kwa ajili ya mmenyuko wa kikemikali. Mwinuko wa mstari (gradient) umeonyeshwa kwenye mchoro. Kokotoa nishati ya uamilisho (activation energy), Ea, katika kJ mol⁻¹."

class Chem096_multi(Chem096):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram uji kimia suatu alkohol berikut! Berdasarkan pengamatan dan rumus molekul yang tercantum pada gambar, identifikasi alkohol tersebut.\n\n{self.options_text}'
        self.description_chinese = f'某醇经历了图中显示的化学测试。根据图像中提供的观察结果和分子式，鉴定该醇。\n\n{self.options_text}'
        self.description_arabic = f'يخضع كحول للاختبار الكيميائي الموضح. بناءً على الملاحظات والصيغة الجزيئية، حدد نوع الكحول.\n\n{self.options_text}'
        self.description_hindi = f'चित्र में दर्शाए गए रासायनिक परीक्षण से एक अल्कोहल गुजरता है। चित्र में दिए गए प्रेक्षणों और आणविक सूत्र के आधार पर अल्कोहल की पहचान कीजिए।\n\n{self.options_text}'
        self.description_kazakh = f'Спирт диаграммада көрсетілген химиялық сынақтан өтеді. Бақылаулар мен суретте берілген молекулалық формулаға сүйене отырып, спиртті анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Alkoholi fulani inapitia jaribio la kikemikali linaloonyeshwa kwenye mchoro. Kulingana na uchunguzi (observations) na fomula ya molekuli iliyotolewa kwenye mchoro huo, tambua alkoholi husika.\n\n{self.options_text}"

class Chem097_multi(Chem097):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram tiga uji kimia untuk suatu senyawa organik tak dikenal berikut! Berdasarkan pengamatan visual tabung reaksi, identifikasi jenis senyawa tersebut.\n\n{self.options_text}'
        self.description_chinese = f'将未知的有机化合物进行图中显示的三种化学测试。根据试管的目视观察结果，鉴定该化合物的类型。\n\n{self.options_text}'
        self.description_arabic = f'يخضع مركب عضوي غير معروف لثلاثة اختبارات كيميائية. بناءً على ملاحظات أنابيب الاختبار، حدد نوع المركب.\n\n{self.options_text}'
        self.description_hindi = f'एक अज्ञात कार्बनिक यौगिक पर चित्र में दर्शाए गए तीन रासायनिक परीक्षण किए जाते हैं। परीक्षण नलिकाओं के दृश्य अवलोकन के आधार पर यौगिक के प्रकार की पहचान कीजिए।\n\n{self.options_text}'
        self.description_kazakh = f'Белгісіз органикалық қосылыс диаграммада көрсетілген үш химиялық сынақтан өтеді. Сынауықтардың визуалды бақылауларына сүйене отырып, қосылыс түрін анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Kiambata cha kikaboni kisichojulikana kinawekwa kwenye majaribio matatu ya kikemikali yanayoonyeshwa kwenye mchoro. Kulingana na uchunguzi wa macho (visual observations) wa mirija ya majaribio, tambua aina ya kiambata hicho.\n\n{self.options_text}"

class Chem098_multi(Chem098):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram mekanisme panah kurva untuk reaksi adisi elektrofilik berikut! Berdasarkan spesies kimia dan pergerakan elektron yang ditampilkan, identifikasi elektrofil yang memulai reaksi tersebut.\n\n{self.options_text}'
        self.description_chinese = f'图中说明了亲电加成反应的弯箭头机理(curly arrow mechanism)。根据图像中显示的化学物种和电子的转移，鉴定引发反应的亲电试剂。\n\n{self.options_text}'
        self.description_arabic = f'يوضح الشكل آلية السهم المنحني لتفاعل إضافة إلكتروفيلية. بناءً على حركة الإلكترونات، حدد الإلكتروفيل الذي يبدأ التفاعل.\n\n{self.options_text}'
        self.description_hindi = f'यह आरेख इलेक्ट्रोफिलिक योग अभिक्रिया के लिए घुमावदार तीर तंत्र को दर्शाता है। चित्र में दर्शाए गए रासायनिक यौगिकों और इलेक्ट्रॉनों की गति के आधार पर, उस विद्युत-प्रेमी की पहचान कीजिए जो अभिक्रिया को आरंभ करता है।\n\n{self.options_text}'
        self.description_kazakh = f'Диаграммада электрофильді қосылу реакциясының қисық жебе механизмі көрсетілген. Суретте көрсетілген химиялық бөлшектер мен электрондардың қозғалысына сүйене отырып, реакцияны бастайтын электрофильді анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Mchoro huu unaonyesha mbinu ya mishale iliyopinda (curly arrow mechanism) kwa mmenyuko wa nyongeza ya kielektrofili (electrophilic addition). Kulingana na spishi za kikemikali na mwendo wa elektroni ulioonyeshwa kwenye mchoro, tambua elektrofili (electrophile) inayoanzisha mmenyuko huo.\n\n{self.options_text}"

class Chem099_multi(Chem099):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram uji perak nitrat dan amonia untuk suatu halida tak dikenal berikut! Identifikasi ion halida yang ada dengan membandingkan pengamatan tabung reaksi terhadap data referensi yang diberikan.\n\n{self.options_text}'
        self.description_chinese = f'将未知的卤化物进行图中显示的硝酸银和氨水测试。通过比较试管的观察结果和提供的参考数据，鉴定存在的卤素离子。\n\n{self.options_text}'
        self.description_arabic = f'يخضع هاليد غير معروف لاختباري نترات الفضة والأمونيا. باستخدام الملاحظات، حدد أيون الهاليد.\n\n{self.options_text}'
        self.description_hindi = f'चित्र में दर्शाए गए सिल्वर नाइट्रेट (silver nitrate) और अमोनिया (ammonia) परीक्षणों के तहत एक अज्ञात हैलाइड (halide) का परीक्षण किया जाता है। परीक्षण ट्यूब में प्राप्त प्रेक्षणों की तुलना दिए गए संदर्भ डेटा से करके उपस्थित हैलाइड आयन की पहचान कीजिए।\n\n{self.options_text}'
        self.description_kazakh = f'Белгісіз галогенидке диаграммада көрсетілген күміс нитраты мен аммиак сынақтары жүргізіледі. Сынауықтағы бақылауларды берілген анықтамалық деректермен салыстыру арқылы бар галогенид ионын анықтаңыз.\n\n{self.options_text}'
        self.description_swahili = f"Halidi (halide) isiyojulikana inawekwa kwenye majaribio ya nitrati ya fedha (silver nitrate) na amonia yanayoonyeshwa kwenye mchoro. Tambua ioni ya halidi iliyopo kwa kulinganisha uchunguzi wa mirija ya majaribio na data ya marejeleo iliyotolewa.\n\n{self.options_text}"

class Chem100_multi(Chem100):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik hubungan pV terhadap p untuk gas nyata dibandingkan gas ideal berikut! Berdasarkan perilaku yang ditampilkan pada daerah yang disorot dalam diagram, pernyataan manakah yang paling tepat menjelaskan penyimpangan dari perilaku ideal tersebut?\n\n{self.options_text}'
        self.description_chinese = f'该图显示了真实气体与理想气体的 $pV$ 和 $p$ 之间的关系。根据图中突出显示区域内表现出的行为，哪种陈述最好地解释了观察到的对理想行为的偏离？\n\n{self.options_text}'
        self.description_arabic = f'يعرض الرسم البياني العلاقة بين $pV$ و $p$ لغاز حقيقي مقارنة بغاز مثالي. بناءً على السلوك في المنطقة المظللة، أي عبارة تفسر بشكل أفضل الانحراف عن السلوك المثالي؟\n\n{self.options_text}'
        self.description_hindi = f'यह ग्राफ एक वास्तविक गैस और एक आदर्श गैस के लिए $pV$ और $p$ के बीच संबंध दर्शाता है। आरेख के हाइलाइट किए गए क्षेत्र में दर्शाए गए व्यवहार के आधार पर, कौन सा कथन आदर्श व्यवहार से देखे गए विचलन की सबसे अच्छी व्याख्या करता है?\n\n{self.options_text}'
        self.description_kazakh = f'Графикте нақты газдың идеал газбен салыстырғандағы $pV$ және $p$ арасындағы байланысы көрсетілген. Диаграмманың ерекшеленген аймағында көрсетілген мінез-құлыққа сүйене отырып, қай тұжырым идеал мінез-құлықтан байқалған ауытқуды жақсы түсіндіреді?\n\n{self.options_text}'
        self.description_swahili = f"Grafu hii inaonyesha uhusiano kati ya $pV$ na $p$ kwa ajili ya gesi halisi (real gas) ikilinganishwa na gesi bora (ideal gas). Kulingana na tabia inayoonyeshwa kwenye eneo lililoangaziwa la mchoro, ni kauli ipi inayofafanua vizuri zaidi mkengeuko (deviation) uliozingatiwa kutoka kwenye tabia ya gesi bora?\n\n{self.options_text}"

class Chem101_multi(Chem101):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan grafik perubahan suhu suatu gas yang mendingin dan membentuk cairan berikut!\n\nDari A ke B zat berwujud gas.\nDari C ke D zat berwujud cair.\n\nHitunglah durasi (lamanya) perubahan fasa yang terjadi!'
        self.description_chinese = '气体冷却后形成液体。该图显示了物质的温度随时间的变化。\n\n从A到B，物质处于气态。\n从C到D，物质处于液态。\n\n计算相变的持续时间！'
        self.description_arabic = 'يُترك غاز ليبرد ويتحول إلى سائل. يوضح الرسم البياني كيف تتغير درجة الحرارة مع الزمن.\n\nمن A إلى B تكون المادة غازًا.\nمن C إلى D تكون المادة سائلًا.\n\nاحسب مدة تغير الحالة!'
        self.description_hindi = 'एक गैस को ठंडा होने के लिए छोड़ दिया जाता है और वह द्रव अवस्था में परिवर्तित हो जाती है। ग्राफ समय के साथ पदार्थ के तापमान में परिवर्तन को दर्शाता है।\n\nA से B तक पदार्थ गैस अवस्था में है।\nC से D तक पदार्थ द्रव अवस्था में है।\n\nअवस्था परिवर्तन की अवधि की गणना कीजिए!'
        self.description_kazakh = 'Газ суытуға қалдырылып, сұйықтық түзеді. График заттың температурасының уақытқа байланысты қалай өзгеретінін көрсетеді.\n\nA-дан B-ға дейін зат газ күйінде болады.\nC-дан D-ға дейін зат сұйықтық күйінде болады.\n\nФазалық ауысудың ұзақтығын есептеңіз!'
        self.description_swahili = f"Gesi inaachwa ipoe hadi kuwa kimiminika. Grafu hii inaonyesha jinsi halijoto ya dutu hiyo inavyobadilika kulingana na wakati.\n\nKutoka A hadi B, dutu hii ni gesi.\nKutoka C hadi D, dutu hii ni kimiminika.\n\nKokotoa muda uliochukuliwa kwa mabadiliko ya hali (phase change) kutokea!"

class Chem102_multi(Chem102):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram difusi gas melintasi suatu ruang berikut! Gas tersebut menempuh jarak terukur dalam periode waktu {self.time}.\n\nHitunglah laju difusi gas tersebut (dalam cm/s)!'
        self.description_chinese = f'如图所示，气体在腔室内扩散。气体在{self.time}的时间内移动了测量的距离。\n\n计算气体的扩散速率（单位为 cm/s）！'
        self.description_arabic = f'ينتشر غاز عبر حجرة كما هو موضح في الشكل. يقطع الغاز مسافة معينة خلال زمن قدره {self.time}.\n\nاحسب معدل انتشار الغاز (بوحدة cm/s).'
        self.description_hindi = f'चित्र में दर्शाए अनुसार एक गैस एक कक्ष में विसरित होती है। गैस {self.time} समय में एक निश्चित दूरी तय करती है।\n\nगैस के विसरण की दर (cm/s में) ज्ञात कीजिए।'
        self.description_kazakh = f'Диаграммада көрсетілгендей газ камера арқылы диффузияланады. Газ {self.time} уақыт ішінде өлшенген қашықтықты жүріп өтеді.\n\nГаздың диффузиялану жылдамдығын (см/с) есептеңіз!'
        self.description_swahili = f"Gesi inasambaa (diffuses) ndani ya chemba kama inavyoonyeshwa kwenye mchoro. Gesi hiyo husafiri umbali uliopimwa kwa muda wa {self.time}. Kokotoa kasi ya usambaaji (rate of diffusion) wa gesi hiyo (katika cm/s)!"

class Chem103_multi(Chem103):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram titik-silang berikut yang menunjukkan elektron kulit terluar atom logam dan atom nonlogam sebelum ikatan ionik terbentuk! Elektron dari atom logam ditandai dengan titik (•) dan elektron dari atom nonlogam ditandai dengan silang (×). Tanda panah menunjukkan arah transfer elektron.\n\nBerapa elektron yang dipindahkan dari atom logam ke atom nonlogam?'
        self.description_chinese = '电子点叉图显示了离子键形成之前金属原子和非金属原子的外层电子。来自金属原子的电子显示为点(•)，来自非金属原子的电子显示为叉(×)。箭头指示了电子转移的方向。\n\n有多少个电子从金属原子转移到非金属原子？'
        self.description_arabic = 'يوضح مخطط النقطة والتقاطع إلكترونات الغلاف الخارجي لذرة فلز وذرة لافلز قبل تكوّن الرابطة الأيونية. تمثل النقاط (•) إلكترونات الفلز، وتمثل العلامات (×) إلكترونات اللافلز. يشير السهم إلى اتجاه انتقال الإلكترونات.\n\nكم عدد الإلكترونات المنتقلة من الفلز إلى اللافلز؟'
        self.description_hindi = 'डॉट-एंड-क्रॉस आरेख आयनिक बांड होने से पहले एक धातु परमाणु और एक अधातु परमाणु के बाहरी कोश के इलेक्ट्रॉनों को दिखाता है। धातु परमाणु के इलेक्ट्रॉनों को डॉट्स (•) के रूप में और अधातु परमाणु के इलेक्ट्रॉनों को क्रॉस (×) के रूप में दिखाया गया है। तीर इलेक्ट्रॉन स्थानांतरण की दिशा को इंगित करता है।\n\nधातु परमाणु से अधातु परमाणु में कितने इलेक्ट्रॉन स्थानांतरित होते हैं?'
        self.description_kazakh = 'Нүктелер мен айқыштар диаграммасы иондық байланыс түзілгенге дейінгі металл атомы мен бейметалл атомының сыртқы қабат электрондарын көрсетеді. Металл атомының электрондары нүктелер (•), ал бейметалл атомының электрондары айқыштар (×) түрінде көрсетілген. Жебе электрон тасымалдану бағытын көрсетеді.\n\nМеталл атомынан бейметалл атомына қанша электрон тасымалданады?'
        self.description_swahili = f"Mchoro wa nukta-na-msalaba (dot-and-cross diagram) unaonyesha elektroni za ganda la nje (outer shell) za atomi ya metali na atomi isiyo ya metali kabla ya muungano wa iyoniki (ionic bonding) kutokea. Elektroni za atomi ya metali zinaonyeshwa kama nukta (•) na elektroni za atomi isiyo ya metali zinaonyeshwa kama misalaba (×). Mshale unaonyesha mwelekeo wa uhamishaji wa elektroni. Je, ni elektroni ngapi zinahamishwa kutoka kwenye atomi ya metali kwenda kwenye atomi isiyo ya metali?"

class Chem104_multi(Chem104):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram titik-silang ikatan kovalen dalam suatu molekul berikut!\n\nHitunglah total ikatan kovalen yang dimiliki molekul tersebut.'
        self.description_chinese = '电子点叉图显示了分子中的共价键。\n\n该分子总共包含多少个共价键？'
        self.description_arabic = 'يوضح مخطط النقطة والتقاطع الروابط التساهمية في جزيء.\n\nكم عدد الروابط التساهمية في هذا الجزيء؟'
        self.description_hindi = 'डॉट-एंड-क्रॉस आरेख एक अणु में सहसंयोजक बोंडिंग को दर्शाता है।\n\nइस अणु में कुल कितने सहसंयोजक बांड हैं?'
        self.description_kazakh = 'Нүктелер мен айқыштар диаграммасы молекуладағы коваленттік байланысты көрсетеді.\n\nБұл молекулада жалпы қанша коваленттік байланыс бар?'
        self.description_swahili = f"Mchoro wa nukta-na-msalaba (dot-and-cross diagram) unaonyesha muundo wa vifungo kovalenti (covalent bonding) katika molekuli. Je, molekuli hii ina jumla ya vifungo kovalenti mingapi?"

class Chem105_multi(Chem105):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram titik-silang berikut yang menunjukkan elektron ikatan dalam suatu molekul!\n\nHitung setiap pasangan titik-silang yang terlihat pada diagram untuk menemukan jumlah total elektron ikatan (elektron yang dipakai bersama) dalam molekul tersebut.'
        self.description_chinese = '电子点叉图显示了分子中的成键电子。\n\n计算图中可见的每一个点-叉对，以找出该分子中成键（共享）电子的总数。'
        self.description_arabic = 'يوضح مخطط النقطة والتقاطع إلكترونات الترابط في جزيء.\n\nعد كل زوج (نقطة–تقاطع) لإيجاد العدد الكلي لإلكترونات الترابط (المشتركة).'
        self.description_hindi = 'डॉट-एंड-क्रॉस आरेख एक अणु में आबंधी इलेक्ट्रॉनों को दिखाता है।\n\nइस अणु में आबंधी (साझा) इलेक्ट्रॉनों की कुल संख्या ज्ञात करने के लिए आरेख में दिखाई देने वाले प्रत्येक डॉट-क्रॉस युग्म की गणना करें।'
        self.description_kazakh = 'Нүктелер мен айқыштар диаграммасы молекуладағы байланыстырғыш электрондарды көрсетеді.\n\nБұл молекуладағы байланыстырушы (ортақ) электрондардың жалпы санын табу үшін диаграммада көрінетін әрбір нүкте-айқыш жұбын санаңыз.'
        self.description_swahili = f"Mchoro wa nukta-na-msalaba (dot-and-cross diagram) unaonyesha elektroni zinazounda vifungo (bonding electrons) katika molekuli. Hesabu kila jozi ya nukta na msalaba inayoonekana kwenye mchoro ili kupata jumla ya idadi ya elektroni zinazoshirikishwa (shared electrons) katika molekuli hii."

class Chem106_multi(Chem106):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan grafik yang melacak massa reaktan selama reaksi antara {self.reaction['reactant_A']} dan {self.reaction['reactant_B']} berikut!\n\nGunakan stoikiometri dan data awal yang diberikan pada grafik untuk menghitung massa tepat pereaksi berlebih yang tersisa!"
        self.description_chinese = f"该图记录了{self.reaction['reactant_A']}和{self.reaction['reactant_B']}反应期间反应物的质量。\n\n使用化学计量学和图中提供的初始数据，计算剩余过量反应物的准确质量！"
        self.description_arabic = f'يوضح الرسم البياني تغير كتلة المواد المتفاعلة أثناء التفاعل بين {self.reaction["reactant_A"]} و {self.reaction["reactant_B"]}.\n\nباستخدام الحسابات الستوكيومترية والبيانات المعطاة، احسب الكتلة الدقيقة للمتفاعل الفائض المتبقي.'
        self.description_hindi = f"यह ग्राफ {self.reaction['reactant_A']} और {self.reaction['reactant_B']} के बीच अभिक्रिया के दौरान अभिकारकों के द्रव्यमान को दर्शाता है।\n\nस्टोइकियोमेट्री (stoichiometry) और ग्राफ में दिए गए प्रारंभिक डेटा का उपयोग करके, शेष बचे अतिरिक्त अभिकारक के सटीक द्रव्यमान की गणना करें!"
        self.description_kazakh = f"График {self.reaction['reactant_A']} және {self.reaction['reactant_B']} арасындағы реакция кезіндегі реагенттердің массасын қадағалайды.\n\nСтехиометрия мен графикте берілген бастапқы деректерді пайдалана отырып, қалған артық реагенттің нақты массасын есептеңіз!"
        self.description_swahili = f"Grafu hii inafuatilia masi ya vitendanishi (reactants) wakati wa mmenyuko kati ya {self.reaction['reactant_A']} na {self.reaction['reactant_B']}. Kwa kutumia stoikiometri (stoichiometry) na data ya awali iliyotolewa kwenye grafu, kokotoa masi kamili ya kitendanishi cha ziada (excess reactant) kilichosalia!"

class Chem107_multi(Chem107):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan grafik massa zat-zat selama rantai reaksi bertahap berikut!\n\nTahap 1: {self.chain['stage1']}\nTahap 2: {self.chain['stage2']}\n\nMassa awal: {self.start_mass} g\n\nGunakan stoikiometri dan massa awal yang diberikan pada grafik untuk menghitung massa tepat produk akhir yang terbentuk!"
        self.description_chinese = f"该图记录了多步反应链中物质的质量。\n\n阶段 1：{self.chain['stage1']}\n阶段 2：{self.chain['stage2']}\n\n起始质量：{self.start_mass} g\n\n使用化学计量学和图中提供的初始质量，计算生成的最终产物的准确质量！"
        self.description_arabic = f'يوضح الرسم البياني تغير الكتلة خلال سلسلة تفاعلات متعددة المراحل.\n\nالمرحلة 1: {self.chain["stage1"]}\nالمرحلة 2: {self.chain["stage2"]}\n\nالكتلة الابتدائية: {self.start_mass} g\n\nباستخدام الحسابات الستوكيومترية، احسب الكتلة الدقيقة للناتج النهائي.'
        self.description_hindi = f"यह ग्राफ़ एक बहु-चरणीय अभिक्रिया श्रृंखला के दौरान पदार्थों के द्रव्यमान को दर्शाता है।\n\nStage 1: {self.chain['stage1']}\nStage 2: {self.chain['stage2']}\n\nStarting mass: {self.start_mass} g \n\nस्टोइकियोमेट्री और ग्राफ़ में दिए गए प्रारंभिक द्रव्यमान का उपयोग करके, बनने वाले अंतिम उत्पाद का सटीक द्रव्यमान ज्ञात कीजिए!"
        self.description_kazakh = f"График көп сатылы реакциялар тізбегі кезіндегі заттардың массасын қадағалайды.\n\n1-саты: {self.chain['stage1']}\n2-саты: {self.chain['stage2']}\n\nБастапқы массасы: {self.start_mass} г\n\nСтехиометрия мен графикте берілген бастапқы массаны пайдалана отырып, түзілген соңғы өнімнің нақты массасын есептеңіз!"
        self.description_swahili = f"Grafu inafuatilia masi ya dutu wakati wa mnyororo wa mimenyuko wa hatua nyingi.\n\nHatua ya 1: {self.chain['stage1']}\nHatua ya 2: {self.chain['stage2']}\n\nMasi ya kuanzia: {self.start_mass} g\n\nKwa kutumia stoikiometri na masi ya kuanzia iliyotolewa kwenye grafu, kokotoa masi kamili ya zao la mwisho lililoundwa!"

class Chem108_multi(Chem108):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan grafik yang melacak massa reaktan dan produk selama reaksi:\n{self.r['eq']}\n\nGunakan stoikiometri dan data pada grafik untuk menghitung persentase hasil (rendemen) reaksi tersebut."
        self.description_chinese = f"该图记录了反应期间反应物和产物的质量：\n{self.r['eq']}\n\n使用化学计量学和图中提供的数据，计算反应的产率。"
        self.description_arabic = f'يوضح الرسم البياني كتل المواد المتفاعلة والناتج في التفاعل:\n{self.r["eq"]}\n\nباستخدام الحسابات الستوكيومترية، احسب النسبة المئوية للمردود.'
        self.description_hindi = f"ग्राफ अभिक्रिया के दौरान अभिकारकों और उत्पाद के द्रव्यमान को ट्रैक करता है:\n{self.r['eq']}\n\nस्टोइकियोमेट्री और ग्राफ में दिए गए डेटा का उपयोग करके, अभिक्रिया की प्रतिशत लब्धि की गणना करें।"
        self.description_kazakh = f"График келесі реакция кезіндегі реагенттер мен өнімнің массаларын қадағалайды:\n{self.r['eq']}\n\nСтехиометрия мен графикте берілген деректерді пайдалана отырып, реакцияның пайыздық шығымын есептеңіз."
        self.description_swahili = f"Grafu inafuatilia masi za vitendanishi (reactants) na zao (product) wakati wa mmenyuko:\n{self.r['eq']}\n\nKwa kutumia stoikiometri na data iliyotolewa kwenye grafu, kokotoa asilimia ya mavuno (percentage yield) ya mmenyuko huo."

class Chem109_multi(Chem109):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan diagram batang volume gas untuk reaksi:\n{self.r['eq']}\n\nGunakan aturan 24 dm³ mol⁻¹, stoikiometri persamaan reaksi, dan data dari grafik untuk menghitung volume tepat gas produk yang terbentuk!"
        self.description_chinese = f"条形图显示了反应的气体体积：\n{self.r['eq']}\n\n使用 24 dm³ mol⁻¹ 规则、方程式的化学计量以及图表中的数据，计算生成的产物气体的确切体积！"
        self.description_arabic = f'يوضح المخطط الشريطي أحجام الغازات في التفاعل:\n{self.r["eq"]}\n\nباستخدام العلاقة 24 dm³ mol⁻¹ والمعادلة الكيميائية، احسب الحجم الدقيق لغاز الناتج.'
        self.description_hindi = f"बार चार्ट अभिक्रिया के लिए गैस आयतन दर्शाता है:\n{self.r['eq']}\n\n24 dm³ mol⁻¹ नियम, समीकरण की स्टोइकियोमेट्री (stoichiometry) और ग्राफ से प्राप्त आंकड़ों का उपयोग करके, निर्मित उत्पाद गैस का सटीक आयतन ज्ञात कीजिए!"
        self.description_kazakh = f"Бағанды диаграммада мына реакцияға арналған газ көлемдері көрсетілген:{self.r['eq']}\n\n24 дм³ моль⁻¹ ережесін, реакция теңдеуінің стехиометриясын және график мәліметтерін қолдана отырып, түзілген өнім газының нақты көлемін есептеңіз!"
        self.description_swahili = f"Chati ya mwambaa (bar chart) inaonyesha ujazo wa gesi kwa mmenyuko wa:\n{self.r['eq']}\n\nKwa kutumia kanuni ya 24 dm³ mol⁻¹, stoikiometri ya mlinganyo, na data kutoka kwenye grafu, kokotoa ujazo kamili wa gesi ya zao (product gas) iliyoundwa!"

class Chem110_multi(Chem110):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan diagram susunan reaksi berikut! Suatu senyawa mengandung {self.sys['percent_A']}% {self.sys['A']} dan {self.sys['percent_B']}% {self.sys['B']}.\n\nHitunglah massa tepat produk akhir yang terbentuk!"
        self.description_chinese = f"某化合物含有 {self.sys['percent_A']}% 的 {self.sys['A']} 和 {self.sys['percent_B']}% 的 {self.sys['B']}。\n\n根据图中显示的反应装置，计算生成的最终产物的准确质量！"
        self.description_arabic = f'يحتوي مركب على {self.sys["percent_A"]}% من {self.sys["A"]} و {self.sys["percent_B"]}% من {self.sys["B"]}.\n\nباستخدام المعطيات، احسب الكتلة الدقيقة للناتج النهائي.'
        self.description_hindi = f"एक यौगिक में {self.sys['percent_A']}% {self.sys['A']} और {self.sys['percent_B']}% {self.sys['B']} हैं।\n\nआरेख में दर्शाए गए अभिक्रिया सेटअप के आधार पर, बनने वाले अंतिम उत्पाद का सटीक द्रव्यमान ज्ञात कीजिए!"
        self.description_kazakh = f"Қосылыстың құрамында {self.sys['percent_A']}% {self.sys['A']} және {self.sys['percent_B']}% {self.sys['B']} бар.\n\nДиаграммада көрсетілген реакция қондырғысына сүйене отырып, түзілген соңғы өнімнің нақты массасын есептеңіз!"
        self.description_swahili = f"Kampaundi fulani ina {self.sys['percent_A']}% ya {self.sys['A']} na {self.sys['percent_B']}% ya {self.sys['B']}.\n\nKulingana na mpangilio wa mmenyuko (reaction setup) unaoonyeshwa kwenye mchoro, kokotoa masi kamili ya zao la mwisho lililoundwa!"

class Chem111_multi(Chem111):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram sel elektrolisis standar dan stopwatch berikut!\n\nArus tetap sebesar {self.current} A dialirkan melalui larutan.\n\nGunakan data dan persamaan yang diberikan untuk menghitung massa tembaga yang mengendap di katoda! (bulatkan ke 2 angka di belakang koma)'
        self.description_chinese = f'该图显示了标准电解池和秒表。\n\n使 {self.current} A 的恒定电流通过溶液。\n\n使用提供的数据和方程式，计算沉积在阴极的铜的质量！（保留两位小数）'
        self.description_arabic = f'يوضح الشكل خلية تحليل كهربائي قياسية وساعة إيقاف.\n\nيمر تيار ثابت شدته {self.current} A عبر المحلول.\n\nاحسب كتلة النحاس المترسبة عند الكاثود (قرب إلى منزلتين عشريتين).'
        self.description_hindi = f'आरेख एक मानक विद्युत अपघटन सेल और एक स्टॉपवॉच को दिखाता है।\n\nविलयन से {self.current} A की एक निरंतर धारा प्रवाहित की जाती है।\n\nप्रदान किए गए डेटा और समीकरणों का उपयोग करके, कैथोड पर जमा हुए तांबे के द्रव्यमान की गणना करें! (2 दशमलव स्थानों तक पूर्णांकित करें)'
        self.description_kazakh = f'Диаграммада стандартты электролиз ұяшығы мен секундомер көрсетілген.\n\nЕрітінді арқылы {self.current} А тұрақты ток өткізіледі.\n\nБерілген деректер мен теңдеулерді пайдалана отырып, катодта жиналған мыстың массасын есептеңіз! (2 ондық таңбаға дейін дөңгелектеңіз)'
        self.description_swahili = f"Mchoro unaonyesha seli sanifu ya elektrolisisi (standard electrolysis cell) na saa ya mkononi (stopwatch).\n\nMkondo wa umeme usiobadilika (constant current) wa {self.current} A unapitishwa kwenye mnyeyusho.\n\nKwa kutumia data na milinganyo iliyotolewa, kokotoa masi ya shaba (copper) inayotua kwenye kathodi! (kadiria jibu lako kwa nafasi 2 za desimali)"

class Chem112_multi(Chem112):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram susunan elektrolisis sebelum dan sesudah reaksi berikut!\n\nGunakan parameter yang diberikan pada gambar (arus, waktu, volume, dan konsentrasi awal) untuk menghitung massa logam yang mengendap di katoda!'
        self.description_chinese = '图示为反应前后的电解装置。\n\n使用图像中提供的参数（电流、时间、体积和初始浓度），计算沉积在阴极的金属的质量！'
        self.description_arabic = 'يوضح الشكل إعداد التحليل الكهربائي قبل وبعد التفاعل.\n\nباستخدام القيم المعطاة (التيار، الزمن، الحجم، والتركيز الابتدائي)، احسب كتلة الفلز المترسبة عند الكاثود.'
        self.description_hindi = 'चित्र अभिक्रिया से पहले और बाद में विद्युत अपघटन सेटअप को दर्शाते हैं।\n\nचित्र में दिए गए मापदंडों (धारा, समय, आयतन और प्रारंभिक सांद्रता) का उपयोग करके कैथोड पर जमा धातु के द्रव्यमान की गणना करें!'
        self.description_kazakh = 'Диаграммалар реакцияға дейінгі және одан кейінгі электролиз қондырғысын көрсетеді.\n\nСуретте берілген параметрлерді (ток күші, уақыт, көлем және бастапқы концентрация) пайдалана отырып, катодта жиналған металдың массасын есептеңіз!'
        self.description_swahili = f"Michoro hii inaonyesha mpangilio wa elektrolisisi (electrolysis setup) kabla na baada ya mmenyuko. Kwa kutumia vigezo vilivyotolewa kwenye picha (mkondo wa umeme, muda, ujazo, na konsentresheni ya awali), kokotoa masi ya metali inayotua (deposited) kwenye kathodi!"

class Chem113_multi(Chem113):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram voltameter Hoffman yang menunjukkan elektrolisis air berikut!\n\n2H₂O → 2H₂ + O₂\n\nGunakan volume gas yang diketahui yang terkumpul pada diagram untuk menghitung volume tepat gas lain yang dihasilkan!'
        self.description_chinese = '霍夫曼电解器(Hoffman voltameter)图显示了水的电解过程。\n\n2H2O → 2H2 + O2\n\n使用图中收集的已知气体的体积，计算产生的另一种气体的准确体积！'
        self.description_arabic = 'يوضح مخطط جهاز هوفمان التحليل الكهربائي للماء:\n\n2H₂O → 2H₂ + O₂\n\nباستخدام حجم أحد الغازين، احسب الحجم الدقيق للغاز الآخر.'
        self.description_hindi = 'हॉफमैन वोल्टमीटर (Hoffman voltameter) आरेख जल के विद्युत अपघटन को दर्शाता है।\n\n2H2O → 2H2 + O2\n\nआरेख में एकत्रित ज्ञात गैस के आयतन का उपयोग करके, उत्पन्न होने वाली दूसरी गैस का सटीक आयतन ज्ञात कीजिए!'
        self.description_kazakh = 'Гофман вольтаметрінің диаграммасы судың электролизін көрсетеді.\n\n2H2O → 2H2 + O2\n\nДиаграммада жиналған белгілі газдың көлемін пайдалана отырып, түзілген екінші газдың нақты көлемін есептеңіз!'
        self.description_swahili = f"Mchoro wa voltameta ya Hoffman (Hoffman voltameter) unaonyesha elektrolisisi ya maji.\n\n2H2O → 2H2 + O2\n\nKwa kutumia ujazo wa gesi inayojulikana iliyokusanywa kwenye mchoro, kokotoa ujazo kamili wa gesi nyingine iliyozalishwa!"

class Chem114_multi(Chem114):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram susunan elektroplating yang terhubung ke sumber daya {self.current} A berikut!\n\nGunakan parameter yang diberikan pada gambar (arus, waktu, luas permukaan, dan jenis logam) untuk menghitung ketebalan lapisan dalam mikrometer (µm)! (bulatkan ke 2 angka di belakang koma)'
        self.description_chinese = f'该图显示了连接到 {self.current}A 电源的电镀装置。\n\n使用图像中提供的参数（电流、时间、表面积和金属类型），计算涂层厚度，单位为微米(µm)（保留两位小数）！'
        self.description_arabic = f'يوضح الشكل إعداد طلاء كهربائي متصل بمصدر تيار شدته {self.current} A.\n\nباستخدام المعطيات، احسب سمك الطبقة المترسبة بوحدة µm (قرب إلى منزلتين عشريتين).'
        self.description_hindi = f'चित्र में {self.current}A के विद्युत स्रोत से जुड़े एक इलेक्ट्रोप्लेटिंग सेटअप को दर्शाया गया है।\n\nचित्र में दिए गए मापदंडों (धारा, समय, सतह क्षेत्र और धातु का प्रकार) का उपयोग करके, कोटिंग की मोटाई को माइक्रोमीटर (µm) में गणना करें (2 दशमलव स्थानों तक पूर्णांकित करें)!'
        self.description_kazakh = f'Диаграммада {self.current} А қуат көзіне қосылған гальваникалық қаптау қондырғысы көрсетілген.\n\nСуретте берілген параметрлерді (ток күші, уақыт, беттік аудан және металл түрі) пайдалана отырып, жабынның қалыңдығын микрометр (мкм) өлшемімен есептеңіз! (2 ондық таңбаға дейін дөңгелектеңіз)'
        self.description_swahili = f"Mchoro huu unaonyesha mpangilio wa upakaji metali kwa umeme (electroplating) uliounganishwa kwenye chanzo cha umeme cha {self.current} A. Kwa kutumia vigezo vilivyotolewa kwenye picha (mkondo wa umeme, muda, eneo la uso, na aina ya metali), kokotoa unene wa mipako katika maikromita (µm) (kadiria jibu lako kwa nafasi 2 za desimali)!"

class Chem115_multi(Chem115):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram pemurnian logam tidak murni menggunakan elektrolisis berikut!\n\nSistem terhubung ke sumber daya {self.current} A.\nGunakan parameter yang diberikan pada gambar (arus, waktu, massa bijih, jenis logam, dan kemurnian bijih) untuk menghitung massa logam murni yang mengendap di katoda!'
        self.description_chinese = f'该图显示了使用电解法提纯不纯金属的过程。\n\n系统连接到 {self.current}A 的电源。\n使用图像中提供的参数（电流、时间、矿石质量、金属类型和矿石纯度），计算沉积在阴极的纯金属质量！\n'
        self.description_arabic = f'يوضح الشكل تنقية فلز غير نقي بالتحليل الكهربائي.\n\nالنظام متصل بمصدر تيار شدته {self.current} A.\n\nباستخدام المعطيات، احسب كتلة الفلز النقي المترسبة عند الكاثود.'
        self.description_hindi = f'चित्र में विद्युत अपघटन द्वारा अशुद्ध धातु के शुद्धिकरण को दर्शाया गया है।\n\nयह प्रणाली {self.current}A विद्युत स्रोत से जुड़ी है।\nचित्र में दिए गए मापदंडों (धारा, समय, अयस्क का द्रव्यमान, धातु का प्रकार और अयस्क की शुद्धता) का उपयोग करके कैथोड पर जमा शुद्ध धातु के द्रव्यमान की गणना कीजिए!\n'
        self.description_kazakh = f'Диаграммада электролиз арқылы қоспасы бар металды тазарту көрсетілген.\n\nЖүйе {self.current} А қуат көзіне қосылған.\nСуретте берілген параметрлерді (ток күші, уақыт, кен массасы, металл түрі және кен тазалығы) пайдалана отырып, катодта жиналған таза металдың массасын есептеңіз!\n'
        self.description_swahili = f"Mchoro huu unaonyesha usafishaji wa metali (purification of metal) kwa kutumia elektrolisisi. Mfumo huu umeunganishwa kwenye chanzo cha umeme cha {self.current} A. Kwa kutumia vigezo vilivyotolewa kwenye picha (mkondo wa umeme, muda, masi ya madini, aina ya metali, na kiwango cha usafi wa madini), kokotoa masi ya metali safi inayotua kwenye kathodi!"

class Chem116_multi(Chem116):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram elektrolisis larutan tembaga(II) sulfat berikut! Proses dilakukan selama {self.time_minutes} menit.\nGunakan informasi pada diagram untuk menghitung massa tembaga yang dihasilkan.'
        self.description_chinese = f'该图显示了硫酸铜(II)溶液的电解。该过程在 {self.time_minutes} 分钟内完成。 \n使用图中的信息计算生成的铜的质量。'
        self.description_arabic = f'يوضح الشكل التحليل الكهربائي لمحلول كبريتات النحاس(II). تتم العملية خلال {self.time_minutes} دقيقة.\n\nاحسب كتلة النحاس الناتجة.'
        self.description_hindi = f'चित्र में कॉपर(II) सल्फेट विलयन के विद्युत अपघटन को दर्शाया गया है। यह प्रक्रिया {self.time_minutes} मिनट में पूरी होती है। \nचित्र में दी गई जानकारी का उपयोग करके उत्पादित कॉपर के द्रव्यमान की गणना कीजिए।'
        self.description_kazakh = f'Диаграммада мыс(II) сульфаты ерітіндісінің электролизі көрсетілген. Процесс {self.time_minutes} минут ішінде орындалады. \nТүзілген мыстың массасын есептеу үшін диаграммадағы ақпаратты пайдаланыңыз.'
        self.description_swahili = f"Mchoro huu unaonyesha elektrolisisi ya mnyeyusho wa shaba(II) sufeti (copper(II) sulfate). Mchakato huu unafanywa kwa muda wa dakika {self.time_minutes}. Tumia taarifa zilizopo kwenye mchoro kukokotoa masi ya shaba (copper) iliyozalishwa."

class Chem117_multi(Chem117):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram susunan elektrolisis larutan perak nitrat ({self.volume_dm3} dm³) berikut! Gunakan parameter yang diberikan pada gambar untuk menghitung massa perak yang mengendap di katoda!'
        self.description_chinese = f'该图显示了 {self.volume_dm3} dm³ 硝酸银溶液的电解装置。使用图像中提供的参数，计算沉积在阴极的银的质量！'
        self.description_arabic = f'يوضح الشكل تحليلًا كهربائيًا لمحلول نترات الفضة بحجم {self.volume_dm3} dm³.\n\nاحسب كتلة الفضة المترسبة عند الكاثود.'
        self.description_hindi = f'चित्र में {self.volume_dm3} dm³ आयतन वाले सिल्वर नाइट्रेट (silver nitrate) विलयन के लिए विद्युत अपघटन सेटअप दर्शाया गया है। चित्र में दिए गए मापदंडों का उपयोग करके कैथोड पर जमा हुई चांदी की मात्रा की गणना कीजिए!'
        self.description_kazakh = f'Диаграммада көлемі {self.volume_dm3} дм³ болатын күміс нитраты ерітіндісіне арналған электролиз қондырғысы көрсетілген. Суретте берілген параметрлерді пайдалана отырып, катодта жиналған күмістің массасын есептеңіз!'
        self.description_swahili = f"Mchoro huu unaonyesha mpangilio wa elektrolisisi (electrolysis setup) kwa ajili ya mnyeyusho wa fedha nitrati (silver nitrate) wa dm³ {self.volume_dm3}. Kwa kutumia vigezo vilivyotolewa kwenye picha, kokotoa masi ya fedha inayotua (deposited) kwenye kathodi!"

class Chem118_multi(Chem118):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram elektroplating nikel berikut dengan luas permukaan elektroda {self.area_cm2} cm² dan kerapatan nikel {self.density} g/cm³! Gunakan parameter yang diberikan untuk menghitung ketebalan nikel yang terdeposit dalam milimeter (mm).\n(Bulatkan ke 4 angka di belakang koma)'
        self.description_chinese = f'该图显示了镍电镀装置，其中电极表面积为 {self.area_cm2} cm²，镍的密度为 {self.density} g/cm³。使用图像中提供的参数，计算沉积的镍的厚度，单位为毫米(mm)。\n（保留四位小数）'
        self.description_arabic = f'يوضح الشكل طلاءً كهربائيًا بالنيكل، حيث مساحة السطح {self.area_cm2} cm² وكثافة النيكل {self.density} g/cm³.\n\nاحسب سمك الطبقة بالمليمتر (قرب إلى 4 منازل عشرية).'
        self.description_hindi = f'आरेख एक निकेल इलेक्ट्रोप्लेटिंग सेटअप दिखाता है जहाँ इलेक्ट्रोड का सतह क्षेत्रफल {self.area_cm2} cm² है और निकेल का घनत्व {self.density} g/cm³ है। चित्र में प्रदान किए गए मापदंडों का उपयोग करके, जमा हुए निकेल की मोटाई मिलीमीटर (mm) में परिकलित करें।\n(4 दशमलव स्थानों तक पूर्णांकित करें)'
        self.description_kazakh = f'Диаграммада электродтың беттік ауданы {self.area_cm2} см² және никельдің тығыздығы {self.density} г/см³ болатын никельмен гальваникалық қаптау қондырғысы көрсетілген. Суретте берілген параметрлерді пайдалана отырып, жиналған никельдің қалыңдығын миллиметрмен (мм) есептеңіз.\n(4 ондық таңбаға дейін дөңгелектеңіз)'
        self.description_swahili = f"Mchoro huu unaonyesha mpangilio wa upakaji nikeli kwa umeme (nickel electroplating) ambapo eneo la uso la kielektrodi (electrode surface area) ni cm² {self.area_cm2} na nikeli ina densiti ya g/cm³ {self.density}. Kwa kutumia vigezo vilivyotolewa kwenye picha, kokotoa unene wa nikeli inayotua (deposited) katika milimita (mm). (Kadiria jibu lako kwa nafasi 4 za desimali)."

class Chem119_multi(Chem119):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram profil entalpi berikut dengan reaktan pada {self.reactant_E} kJ/mol! Gunakan nilai yang ditandai pada sumbu-y untuk menentukan perubahan entalpi ΔH (dalam kJ mol⁻¹) untuk reaksi tersebut.'
        self.description_chinese = f'焓分布图显示反应物能量为 {self.reactant_E} kJ/mol。使用y轴上标记的数值，确定此反应的焓变 ΔH (kJ mol⁻¹)。'
        self.description_arabic = f'يوضح مخطط المحتوى الحراري أن طاقة المتفاعلات = {self.reactant_E} kJ/mol.\n\nاحسب ΔH بوحدة kJ mol⁻¹.'
        self.description_hindi = f'एन्थैल्पी प्रोफ़ाइल आरेख {self.reactant_E} kJ/mol पर अभिकारकों को दर्शाता है। y-अक्ष पर अंकित मानों का उपयोग करके, इस अभिक्रिया के लिए एन्थैल्पी परिवर्तन ΔH (kJ mol⁻¹) ज्ञात कीजिए।'
        self.description_kazakh = f'Энтальпия профилінің диаграммасы реагенттерді {self.reactant_E} кДж/моль деңгейінде көрсетеді. y осінде белгіленген мәндерді пайдалана отырып, осы реакция үшін ΔH энтальпия өзгерісін (кДж·моль⁻¹) анықтаңыз.'
        self.description_swahili = f"Mchoro wa wasifu wa entalpi (enthalpy profile diagram) unaonyesha vitendanishi katika kiwango cha {self.reactant_E} kJ/mol. Kwa kutumia thamani zilizowekwa kwenye mhimili wa y (y-axis), tambua mabadiliko ya entalpi ΔH (kJ mol⁻¹) ya mmenyuko huu."

class Chem120_multi(Chem120):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram sel ekstraksi tembaga melalui elektrolisis berikut! Sampel bijih memiliki massa {self.ore_mass} g. Gunakan informasi yang ditampilkan untuk menghitung massa maksimum tembaga murni yang diperoleh.'
        self.description_chinese = f'该图显示了通过电解提取铜的装置。矿石样品的质量为 {self.ore_mass} g。使用显示的信息计算可获得的最大纯铜质量。'
        self.description_arabic = f'يوضح الشكل استخلاص النحاس بالتحليل الكهربائي. كتلة الخام {self.ore_mass} g.\n\nاحسب أقصى كتلة من النحاس النقي الممكن الحصول عليها.'
        self.description_hindi = f'चित्र में विद्युत अपघटन द्वारा तांबा निकालने की विधि दर्शाई गई है। अयस्क के नमूने का द्रव्यमान {self.ore_mass} g है। दिए गए विवरण का उपयोग करके प्राप्त शुद्ध तांबे की अधिकतम मात्रा की गणना कीजिए।'
        self.description_kazakh = f'Диаграммада электролиз арқылы мысты алу қондырғысы көрсетілген. Кен үлгісінің массасы {self.ore_mass} г құрайды. Алынған таза мыстың максималды массасын есептеу үшін көрсетілген ақпаратты пайдаланыңыз.'
        self.description_swahili = f"Mchoro huu unaonyesha mpangilio wa uchimbaji wa shaba (copper extraction) kwa kutumia elektrolisisi. Sampuli ya madini (ore sample) ina masi ya {self.ore_mass} g. Tumia taarifa iliyoonyeshwa kukokotoa masi ya juu zaidi ya shaba safi inayoweza kupatikana."

class Chem121_multi(Chem121):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan grafik perubahan konsentrasi Cu²⁺ selama elektrolisis berikut! Gunakan grafik dan informasi yang ditampilkan untuk menghitung total muatan listrik yang dialirkan.'
        self.description_chinese =f'该图显示了电解过程中 Cu²⁺ 浓度的变化。利用该图和图中所示信息计算通过的总电荷量。'
        self.description_arabic = 'يوضح الرسم البياني تغير تركيز Cu²⁺ أثناء التحليل الكهربائي.\n\nباستخدام الرسم البياني، احسب الشحنة الكلية المارة.'
        self.description_hindi = 'ग्राफ में विद्युत अपघटन के दौरान Cu²⁺ की सांद्रता में होने वाले परिवर्तन को दर्शाया गया है। ग्राफ और दी गई जानकारी का उपयोग करके कुल स्थानांतरित आवेश की गणना कीजिए।'
        self.description_kazakh = 'Графикте электролиз кезінде Cu²⁺ концентрациясының қалай өзгеретіні көрсетілген. Графикті және берілген мәліметтерді пайдалана отырып, өткен жалпы зарядты есептеңіз.'
        self.description_swahili = f"Grafu hii inaonyesha jinsi konsentresheni ya Cu²⁺ inavyobadilika wakati wa elektrolisisi. Tumia grafu na taarifa iliyoonyeshwa kukokotoa jumla ya chaji (total charge) iliyopitishwa."

class Chem122_multi(Chem122):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram jalur reaksi yang menunjukkan tingkat energi reaktan dan produk berikut!\nHitunglah perubahan entalpi ΔH dalam kJ.'
        self.description_chinese = '反应途径图显示了反应物和产物的能级。\n计算焓变 ΔH，单位为 kJ。'
        self.description_arabic = 'يوضح مخطط مسار التفاعل مستويات الطاقة للمتفاعلات والنواتج.\n\nاحسب ΔH بوحدة kJ.'
        self.description_hindi = 'अभिक्रिया पथ आरेख अभिकारकों और उत्पादों के ऊर्जा स्तरों को दर्शाता है।\nएंथैल्पी परिवर्तन, ΔH, की गणना kJ में करें।'
        self.description_kazakh = 'Реакция жолының диаграммасы реагенттер мен өнімдердің энергетикалық деңгейлерін көрсетеді.\nΔH энтальпия өзгерісін кДж өлшемімен есептеңіз.'
        self.description_swahili = "Mchoro wa njia ya mmenyuko (reaction pathway) unaonyesha viwango vya nishati vya vitendanishi na mazao. Kokotoa mabadiliko ya entalpi, ΔH, katika kJ."

class Chem123_multi(Chem123):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram jalur reaksi yang menunjukkan tingkat energi reaktan dan produk berikut!\nHitunglah energi aktivasi Ea untuk reaksi maju.'
        self.description_chinese = '反应途径图显示了反应物和产物的能级。\n计算正反应的活化能 Ea。'
        self.description_arabic = 'يوضح مخطط مسار التفاعل مستويات الطاقة.\n\nاحسب طاقة التنشيط Ea للتفاعل الأمامي.'
        self.description_hindi = 'अभिक्रिया पथ आरेख अभिकारकों और उत्पादों के ऊर्जा स्तरों को दर्शाता है।\nअग्रगामी अभिक्रिया के लिए सक्रियण ऊर्जा, Ea की गणना कीजिए।'
        self.description_kazakh = 'Реакция жолының диаграммасы реагенттер мен өнімдердің энергетикалық деңгейлерін көрсетеді.\nТура реакция үшін Ea активтену энергиясын есептеңіз.'
        self.description_swahili = "Mchoro wa njia ya mmenyuko (reaction pathway) unaonyesha viwango vya nishati vya vitendanishi na mazao. Kokotoa nishati ya uamilisho (activation energy), Ea, kwa mmenyuko wa kwenda mbele."

class Chem124_multi(Chem124):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan data energi ikatan dan persamaan reaksi yang diberikan pada gambar berikut! Hitunglah perubahan entalpi (ΔH) reaksi tersebut dalam kJ/mol.'
        self.description_chinese = '使用图像中提供的键能和化学方程式，计算反应的焓变(ΔH)，单位为 kJ/mol。'
        self.description_arabic = 'باستخدام طاقات الروابط والمعادلة الكيميائية، احسب ΔH للتفاعل (بوحدة kJ/mol).'
        self.description_hindi = 'चित्र में दी गई बांड ऊर्जाओं और रासायनिक समीकरण का उपयोग करके, अभिक्रिया के एन्थैल्पी परिवर्तन (ΔH) की गणना kJ/mol में करें।'
        self.description_kazakh = 'Суретте берілген байланыс энергиялары мен химиялық теңдеуді пайдалана отырып, реакцияның энтальпия өзгерісін (ΔH) кДж/моль өлшемімен есептеңіз.'
        self.description_swahili = "Kwa kutumia nishati za vifungo (bond energies) na mlinganyo wa kikemikali uliotolewa kwenye picha, kokotoa mabadiliko ya entalpi (ΔH) ya mmenyuko katika kJ/mol."

class Chem125_multi(Chem125):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik volume gas yang dihasilkan terhadap waktu selama reaksi antara {self.reaction} berikut! Gunakan dua titik data yang ditandai secara eksplisit pada grafik untuk menghitung laju reaksi rata-rata pada selang waktu tersebut dalam cm³/s.'
        self.description_chinese = f'该图记录了在 {self.reaction} 反应期间产生的气体体积随时间的变化。使用图上明确突出显示的两个数据点，计算此时间间隔内的平均反应速率，单位为 cm³/s。'
        self.description_arabic = f'يوضح الرسم البياني حجم الغاز الناتج مع الزمن أثناء التفاعل بين {self.reaction}.\n\nباستخدام نقطتين محددتين، احسب متوسط معدل التفاعل (cm³/s).'
        self.description_hindi = f'यह ग्राफ़ {self.reaction} के बीच अभिक्रिया के दौरान समय के साथ उत्पन्न गैस की मात्रा को दर्शाता है। ग्राफ़ पर स्पष्ट रूप से दर्शाए गए दो बिंदुओं का उपयोग करके, इस समयावधि के लिए अभिक्रिया की औसत दर को cm³/s में ज्ञात कीजिए।'
        self.description_kazakh = f'График {self.reaction} арасындағы реакция кезінде уақыт өте келе түзілген газ көлемін қадағалайды. Графикте нақты ерекшеленген екі деректер нүктесін пайдалана отырып, осы уақыт аралығы үшін реакцияның орташа жылдамдығын см³/с өлшемімен есептеңіз.'
        self.description_swahili = f"Grafu hii inafuatilia ujazo wa gesi inayozalishwa kwa muda wakati wa mmenyuko kati ya {self.reaction}. Kwa kutumia nukta mbili za data zilizoangaziwa wazi kwenye grafu, kokotoa wastani wa kasi ya mmenyuko (average rate of reaction) kwa kipindi hicho katika cm³/s."

class Chem126_multi(Chem126):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik yang menunjukkan reaksi antara {self.reaction} berikut!\nDari grafik tersebut, tentukan waktu yang diperlukan hingga reaksi selesai.'
        self.description_chinese = f'该图显示了 {self.reaction} 之间的反应。\n从图中确定反应\n完成所需的时间。'
        self.description_arabic = f'يوضح الرسم البياني التفاعل بين {self.reaction}.\n\nحدد الزمن اللازم لاكتمال التفاعل.'
        self.description_hindi = f'ग्राफ {self.reaction} के बीच की प्रतिक्रिया को दर्शाता है।\nग्राफ से, प्रतिक्रिया पूरी होने में लगने वाला समय\nज्ञात कीजिए।'
        self.description_kazakh = f'График {self.reaction} арасындағы реакцияны көрсетеді.\nГрафиктен реакцияның аяқталуына\nкеткен уақытты анықтаңыз.'
        self.description_swahili = f"Grafu hii inaonyesha mmenyuko kati ya {self.reaction}. Kutokana na grafu hiyo, tambua muda uliochukuliwa ili mmenyuko ukamilike."

class Chem127_multi(Chem127):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram batang komposisi kesetimbangan untuk {self.process} berikut!\nHitunglah persentase hasil (rendemen) {self.product_name} pada kesetimbangan.'
        self.description_chinese = f'条形图显示了 {self.process} 的平衡组成。\n计算在平衡状态下 {self.product_name} 的产率。'
        self.description_arabic = f'يوضح المخطط الشريطي تركيب التوازن للتفاعل {self.process}.\n\nاحسب النسبة المئوية للمردود لـ {self.product_name}.'
        self.description_hindi = f'बार चार्ट {self.process} के लिए संतुलन संरचना दर्शाता है।\nसंतुलन पर {self.product_name} की प्रतिशत उपज की गणना करें।'
        self.description_kazakh = f'Бағаналы диаграмма {self.process} үшін тепе-теңдік құрамын көрсетеді.\nТепе-теңдік кезіндегі {self.product_name} пайыздық шығымын есептеңіз.'
        self.description_swahili = f"Chati ya mwambaa (bar chart) inaonyesha muundo wa msawazo (equilibrium composition) wa {self.process}. Kokotoa asilimia ya mavuno (percentage yield) ya {self.product_name} kwenye msawazo."

class Chem128_multi(Chem128):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi kesetimbangan untuk {self.process} berikut!\nGunakan informasi grafik untuk menghitung penurunan jumlah mol total.'
        self.description_chinese = f'该图显示了 {self.process} 的平衡反应。\n使用图表信息，计算\n总摩尔数的减少量。'
        self.description_arabic = f'يوضح الشكل تفاعل الاتزان لـ {self.process}.\n\nاحسب النقص في العدد الكلي للمولات.'
        self.description_hindi = f'आरेख {self.process} के लिए संतुलन प्रतिक्रिया दर्शाता है।\nग्राफ की जानकारी का उपयोग करके, मोलों की कुल संख्या में कमी\nकी गणना करें।'
        self.description_kazakh = f'Диаграмма {self.process} үшін тепе-теңдік реакциясын көрсетеді.\nГрафик ақпаратын пайдалана отырып, мольдердің жалпы санының\nтөмендеуін есептеңіз.'
        self.description_swahili = f"Mchoro huu unaonyesha mmenyuko wa msawazo (equilibrium reaction) wa {self.process}. Kwa kutumia taarifa iliyo kwenye grafu, kokotoa upungufu wa jumla ya idadi ya moli (total number of moles)."

class Chem129_multi(Chem129):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik volume {self.gas_name} yang dihasilkan dalam reaksi:\n{self.reaction}\nHitunglah konsentrasi asam yang digunakan.'
        self.description_chinese = f'该图显示了在以下反应中产生的 {self.gas_name} 的体积：\n{self.reaction}\n计算所用酸的浓度。'
        self.description_arabic = f'يوضح الرسم البياني حجم {self.gas_name} الناتج في التفاعل:\n{self.reaction}\n\nاحسب تركيز الحمض المستخدم.'
        self.description_hindi = f'ग्राफ अभिक्रिया में उत्पन्न {self.gas_name} की मात्रा दर्शाता है:\n{self.reaction}\nउपयोग किए गए अम्ल की सांद्रता की गणना करें।'
        self.description_kazakh = f'График келесі реакцияда түзілген {self.gas_name} көлемін көрсетеді:\n{self.reaction}\nҚолданылған қышқылдың концентрациясын есептеңіз.'
        self.description_swahili = f"Grafu hii inaonyesha ujazo wa {self.gas_name} iliyozalishwa katika mmenyuko wa:\n{self.reaction}\nKokotoa konsentresheni ya asidi iliyotumika."

class Chem130_multi(Chem130):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram komposisi kesetimbangan untuk {self.process} ({self.equation}) berikut, dengan {self.limiting_species} dimulai pada {self.initial_limiting} mol! Hitunglah persentase konversi {self.limiting_species}.'
        self.description_chinese = f'该图显示了 {self.process} ({self.equation}) 的平衡组成，其中 {self.limiting_species} 从 {self.initial_limiting} mol 开始。计算 {self.limiting_species} 的转化率。'
        self.description_arabic = f'يوضح الشكل تركيب التوازن للتفاعل {self.process} ({self.equation})، حيث يبدأ {self.limiting_species} بكمية {self.initial_limiting} مول. احسب النسبة المئوية لتحول {self.limiting_species}.'
        self.description_hindi = f'आरेख {self.process} ({self.equation}) के लिए संतुलन संघटन दर्शाता है, जिसमें {self.limiting_species} की प्रारंभिक मात्रा {self.initial_limiting} mol है। {self.limiting_species} के प्रतिशत रूपांतरण की गणना कीजिए।'
        self.description_kazakh = f'Диаграмма {self.process} ({self.equation}) үшін тепе-теңдік құрамын көрсетеді, {self.limiting_species} {self.initial_limiting} мольден басталады. {self.limiting_species} пайыздық айналуын есептеңіз.'
        self.description_swahili = f"Mchoro huu unaonyesha muundo wa msawazo (equilibrium composition) wa {self.process} ({self.equation}), huku {self.limiting_species} ikianza na moli {self.initial_limiting}. Kokotoa asilimia ya ubadilishaji (percentage conversion) ya {self.limiting_species}."

class Chem131_multi(Chem131):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan grafik perubahan konsentrasi untuk {self.reaction} berikut!\nHitunglah laju reaksi rata-rata antara 0 s hingga waktu akhir.'
        self.description_chinese = f'该图显示了 {self.reaction} 的浓度变化。\n计算从 0 s 到最终时间的平均反应速率。'
        self.description_arabic = f'يوضح الرسم البياني تغير التركيز للتفاعل {self.reaction}.\nاحسب متوسط معدل التفاعل بين الزمن 0 ثانية والزمن النهائي.'
        self.description_hindi = f'ग्राफ {self.reaction} के लिए सांद्रता परिवर्तन दर्शाता है।\n0 s और अंतिम समय के बीच प्रतिक्रिया की औसत दर की गणना करें।'
        self.description_kazakh = f'График {self.reaction} үшін концентрацияның өзгеруін көрсетеді.\n0 с пен соңғы уақыт аралығындағы реакцияның орташа жылдамдығын есептеңіз.'
        self.description_swahili = f"Grafu hii inaonyesha mabadiliko ya konsentresheni kwa ajili ya {self.reaction}. Kokotoa wastani wa kasi ya mmenyuko (average rate of reaction) kati ya sekunde 0 na muda wa mwisho."

class Chem132_multi(Chem132):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi redoks berikut:\n{self.equation}\nHitunglah jumlah mol elektron yang dipindahkan.'
        self.description_chinese = f'该图显示了氧化还原反应：\n{self.equation}\n计算转移电子的摩尔数。'
        self.description_arabic = f'يوضح الشكل تفاعل الأكسدة والاختزال:\n{self.equation}\nاحسب عدد مولات الإلكترونات المنتقلة.'
        self.description_hindi = f'आरेख रेडॉक्स अभिक्रिया (redox reaction) को दर्शाता है:\n{self.equation}\nस्थानांतरित इलेक्ट्रॉनों के मोलों की संख्या की गणना करें।'
        self.description_kazakh = f'Диаграмма тотығу-тотықсыздану реакциясын көрсетеді:\n{self.equation}\nТасымалданған электрондардың моль санын есептеңіз.'
        self.description_swahili = f"Mchoro huu unaonyesha mmenyuko wa redoksi (redox reaction):\n{self.equation}\nKokotoa idadi ya moli za elektroni zilizohamishwa (moles of electrons transferred)."

class Chem133_multi(Chem133):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram titrasi redoks berikut:\n{self.equation}\nHitunglah konsentrasi larutan Fe²⁺.'
        self.description_chinese = f'该图显示了氧化还原滴定：\n{self.equation}\n计算 Fe²⁺ 溶液的浓度。'
        self.description_arabic = f'يوضح الشكل معايرة أكسدة واختزال:\n{self.equation}\nاحسب تركيز محلول Fe²⁺.'
        self.description_hindi = f'आरेख रेडॉक्स अनुमापन (redox titration) दर्शाता है:\n{self.equation}\nFe²⁺ विलयन की सांद्रता की गणना कीजिए।'
        self.description_kazakh = f'Диаграмма тотығу-тотықсыздану титрлеуін көрсетеді:\n{self.equation}\nFe²⁺ ерітіндісінің концентрациясын есептеңіз.'
        self.description_swahili = f"Mchoro huu unaonyesha taitresheni ya redoksi (redox titration):\n{self.equation}\nKokotoa konsentresheni ya mnyeyusho wa Fe²⁺."

class Chem134_multi(Chem134):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan diagram reaksi berikut:\n{self.equation}\nHitunglah massa logam yang dihasilkan.'
        self.description_chinese =f'该图显示了反应式：\n{self.equation}\n计算生成的金属质量。'
        self.description_arabic = f'يوضح الشكل التفاعل:\n{self.equation}\nاحسب كتلة الفلز الناتج.'
        self.description_hindi = f'आरेख अभिक्रिया को दर्शाता है:\n{self.equation}\nउत्पादित धातु का द्रव्यमान ज्ञात कीजिए।'
        self.description_kazakh = f'Сызбада мына реакция көрсетілген:\n{self.equation}\nТүзілген металдың массасын есептеңіз.'
        self.description_swahili = f"Mchoro huu unaonyesha mmenyuko wa:\n{self.equation}\nKokotoa masi ya metali iliyozalishwa (mass of metal produced)."

class Chem135_multi(Chem135):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram titrasi asam–basa berikut!\nHitunglah konsentrasi asam klorida.'
        self.description_chinese = '该图显示了酸碱滴定过程。\n计算盐酸的浓度。'
        self.description_arabic = 'يوضح الشكل معايرة حمض–قاعدة.\nاحسب تركيز حمض الهيدروكلوريك.'
        self.description_hindi = 'चित्र में अम्ल-क्षार अनुमापन (acid–alkali titration) दर्शाया गया है।\nहाइड्रोक्लोरिक अम्ल (hydrochloric acid) की सांद्रता की गणना कीजिए।'
        self.description_kazakh = 'Диаграмма қышқыл-сілтілік титрлеуді көрсетеді.\nТұз қышқылының концентрациясын есептеңіз.'
        self.description_swahili = "Mchoro huu unaonyesha taitresheni ya asidi-alkali (acid–alkali titration). Kokotoa konsentresheni ya asidi ya hidrokloriki (hydrochloric acid)."

class Chem136_multi(Chem136):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram reaksi asam klorida dengan kalsium karbonat berlebih berikut!\nHitunglah volume karbon dioksida yang dihasilkan pada RTP.'
        self.description_chinese = '该图显示了盐酸与过量碳酸钙反应的过程。\n计算在室温常压(r.t.p.)下产生的二氧化碳体积。'
        self.description_arabic = 'يوضح الشكل تفاعل حمض الهيدروكلوريك مع كربونات الكالسيوم الزائدة.\nاحسب حجم غاز ثاني أكسيد الكربون الناتج عند الظروف القياسية للغرفة (r.t.p).'
        self.description_hindi = 'चित्र में हाइड्रोक्लोरिक अम्ल (hydrochloric acid) की अतिरिक्त कैल्शियम कार्बोनेट (calcium carbonate) के साथ अभिक्रिया दर्शाई गई है।\n r.t.p. पर उत्पन्न कार्बन डाइऑक्साइड (carbon dioxide) की मात्रा की गणना कीजिए।'
        self.description_kazakh = 'Диаграмма тұз қышқылының артық мөлшердегі кальций карбонатымен әрекеттесуін көрсетеді.\nБөлме температурасы мен қысымында (r.t.p.) түзілген көмірқышқыл газының көлемін есептеңіз.'
        self.description_swahili = "Mchoro huu unaonyesha asidi ya hidrokloriki (hydrochloric acid) ikimenyuka na kabonati ya kalsiamu (calcium carbonate) ya ziada. Kokotoa ujazo wa kaboni daioksaidi (carbon dioxide) inayozalishwa katika r.t.p."

class Chem137_multi(Chem137):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan gambar larutan {self.acid_name} dengan konsentrasi yang tercantum pada gambar berikut!\nHitunglah pH larutan tersebut.'
        self.description_chinese = f'{self.acid_name} 溶液的浓度如图所示。\n计算该溶液的 pH 值。'
        self.description_arabic = f'محلول من {self.acid_name} له تركيز كما هو موضح في الشكل.\nاحسب قيمة الرقم الهيدروجيني (pH) للمحلول.'
        self.description_hindi = f'{self.acid_name} के विलयन की सांद्रता चित्र में दर्शाई गई है।\nविलयन का pH ज्ञात कीजिए।'
        self.description_kazakh = f'{self.acid_name} ерітіндісінің концентрациясы суретте көрсетілгендей.\nЕрітіндінің pH мәнін есептеңіз.'
        self.description_swahili = f"Mnyeyusho wa {self.acid_name} una konsentresheni kama inavyoonyeshwa kwenye picha. Kokotoa pH ya mnyeyusho huo."

class Chem138_multi(Chem138):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram reaksi asam nitrat dengan natrium hidroksida berikut!\nHitunglah massa natrium nitrat yang terbentuk.'
        self.description_chinese = '该图显示了硝酸与氢氧化钠反应的过程。\n计算生成的硝酸钠的质量。'
        self.description_arabic = 'يوضح الشكل تفاعل حمض النيتريك مع هيدروكسيد الصوديوم.\nاحسب كتلة نترات الصوديوم المتكونة.'
        self.description_hindi = 'चित्र में नाइट्रिक अम्ल (nitric acid) और सोडियम हाइड्रॉक्साइड (sodium hydroxide) की अभिक्रिया दर्शाई गई है।\nनिर्मित सोडियम नाइट्रेट (sodium nitrate) का द्रव्यमान ज्ञात कीजिए।'
        self.description_kazakh = 'Диаграмма азот қышқылының натрий гидроксидімен әрекеттесуін көрсетеді.\nТүзілген натрий нитратының массасын есептеңіз.'
        self.description_swahili = "Mchoro huu unaonyesha asidi ya nitriki (nitric acid) ikimenyuka na hidroksidi ya sodiamu (sodium hydroxide). Kokotoa masi ya nitrati ya sodiamu (sodium nitrate) inayoundwa."

class Chem139_multi(Chem139):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram reaksi kalsium karbonat tidak murni dengan asam berlebih berikut!\nGunakan informasi yang ditampilkan untuk menghitung kemurnian persentase sampel tersebut.'
        self.description_chinese = '不纯的碳酸钙与过量酸反应。\n使用显示的信息来计算\n样品的纯度百分比。'
        self.description_arabic = 'تتفاعل كربونات الكالسيوم غير النقية مع حمض فائض.\nاستخدم المعطيات لحساب النسبة المئوية لنقاء العينة.'
        self.description_hindi = 'अशुद्ध कैल्शियम कार्बोनेट (calcium carbonate) अतिरिक्त अम्ल के साथ अभिक्रिया करता है।\nदी गई जानकारी का उपयोग करके\nनमूने की प्रतिशत शुद्धता की गणना करें।'
        self.description_kazakh = 'Қоспасы бар кальций карбонаты артық мөлшердегі қышқылмен әрекеттеседі.\nҮлгінің пайыздық тазалығын есептеу үшін\nкөрсетілген ақпаратты пайдаланыңыз.'
        self.description_swahili = "Kabonati ya kalsiamu (calcium carbonate) isiyo safi inamenyuka na asidi ya ziada. Tumia taarifa iliyoonyeshwa kukokotoa asilimia ya usafi (percentage purity) ya sampuli hiyo."

class Chem140_multi(Chem140):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram reaksi aluminium oksida dengan asam klorida berikut!\nGunakan informasi yang ditampilkan untuk menghitung massa aluminium klorida yang dihasilkan.'
        self.description_chinese = '氧化铝与盐酸反应。\n使用显示的信息来计算\n生成的氯化铝的质量。'
        self.description_arabic = 'يتفاعل أكسيد الألومنيوم مع حمض الهيدروكلوريك.\nاستخدم المعطيات لحساب كتلة كلوريد الألومنيوم الناتجة.'
        self.description_hindi = 'एल्युमिनियम ऑक्साइड (Aluminium oxide) हाइड्रोक्लोरिक अम्ल (hydrochloric acid) के साथ अभिक्रिया करता है।\nदी गई जानकारी का उपयोग करके\nउत्पादित एल्युमिनियम क्लोराइड (aluminium chloride) के द्रव्यमान की गणना करें।'
        self.description_kazakh = 'Алюминий оксиді тұз қышқылымен әрекеттеседі.\nТүзілген алюминий хлоридінің массасын есептеу үшін\nкөрсетілген ақпаратты пайдаланыңыз.'
        self.description_swahili = "Oksidi ya alumini (aluminium oxide) inamenyuka na asidi ya hidrokloriki (hydrochloric acid). Tumia taarifa iliyoonyeshwa kukokotoa masi ya kloridi ya alumini (aluminium chloride) inayozalishwa."

class Chem141_multi(Chem141):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram reaksi magnesium dengan asam sulfat berlebih berikut!\nGunakan informasi yang ditampilkan untuk menghitung massa magnesium sulfat yang terbentuk.'
        self.description_chinese = '镁与过量的硫酸反应。\n使用显示的信息来计算\n生成的硫酸镁的质量。'
        self.description_arabic = 'يتفاعل المغنيسيوم مع حمض الكبريتيك الزائد.\nاستخدم المعطيات لحساب كتلة كبريتات المغنيسيوم المتكونة.'
        self.description_hindi = 'मैग्नीशियम (Magnesium) अतिरिक्त सल्फ्यूरिक अम्ल (sulfuric acid) के साथ अभिक्रिया करता है।\nदी गई जानकारी का उपयोग करके\nनिर्मित मैग्नीशियम सल्फेट (magnesium sulfate) के द्रव्यमान की गणना करें।'
        self.description_kazakh = 'Магний артық мөлшердегі күкірт қышқылымен әрекеттеседі.\nТүзілген магний сульфатының массасын есептеу үшін\nкөрсетілген ақпаратты пайдаланыңыз.'
        self.description_swahili = "Magnesiamu (magnesium) inamenyuka na asidi ya sulfuri (sulfuric acid) ya ziada. Tumia taarifa iliyoonyeshwa kukokotoa masi ya sulfati ya magnesiamu (magnesium sulfate) inayoundwa."

class Chem142_multi(Chem142):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram reaksi barium nitrat dengan natrium sulfat berikut!\nGunakan informasi yang ditampilkan untuk menghitung massa endapan barium sulfat yang terbentuk.'
        self.description_chinese = '硝酸钡与硫酸钠反应。\n使用显示的信息来计算\n生成的硫酸钡沉淀的质量。'
        self.description_arabic = 'تتفاعل نترات الباريوم مع كبريتات الصوديوم.\nاستخدم المعطيات لحساب كتلة راسب كبريتات الباريوم المتكون.'
        self.description_hindi = 'बेरियम नाइट्रेट (Barium nitrate) सोडियम सल्फेट (sodium sulfate) के साथ अभिक्रिया करता है।\nदी गई जानकारी का उपयोग करके\nनिर्मित बेरियम सल्फेट अवक्षेप (barium sulfate precipitate) के द्रव्यमान की गणना करें।'
        self.description_kazakh = 'Барий нитраты натрий сульфатымен әрекеттеседі.\nТүзілген барий сульфаты тұнбасының массасын есептеу үшін\nкөрсетілген ақпаратты пайдаланыңыз.'
        self.description_swahili = "Nitrati ya bariamu (barium nitrate) inamenyuka na sulfati ya sodiamu (sodium sulfate). Tumia taarifa iliyoonyeshwa kukokotoa masi ya mashapo ya sulfati ya bariamu (barium sulfate precipitate) yanayoundwa."

class Chem143_multi(Chem143):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram pemanasan sampel tembaga(II) sulfat terhidrat berikut!\nGunakan informasi yang ditampilkan untuk menghitung nilai x dalam CuSO₄·xH₂O.'
        self.description_chinese = '水合硫酸铜(II)样品被加热。\n使用显示的信息来计算\nCuSO₄·xH₂O 中 x 的值。'
        self.description_arabic = 'يتم تسخين عينة من كبريتات النحاس(II) المائية.\nاستخدم المعطيات لحساب قيمة x في الصيغة CuSO₄·xH₂O.'
        self.description_hindi = 'एक हाइड्रेटेड कॉपर(II) सल्फेट (copper(II) sulfate) के नमूने को गर्म किया जाता है।\nदिखाई गई जानकारी का उपयोग करके\nCuSO₄•xH₂O में x का मान ज्ञात कीजिए।'
        self.description_kazakh = 'Гидратталған мыс(II) сульфатының үлгісі қыздырылады.\nCuSO₄·xH₂O құрамындағы x мәнін есептеу үшін\nкөрсетілген ақпаратты пайдаланыңыз.'
        self.description_swahili = "Sampuli ya salfeti ya shaba(II) yenye maji (hydrated copper(II) sulfate) inapashwa moto. Tumia taarifa iliyoonyeshwa kukokotoa thamani ya x katika CuSO₄·xH₂O."

class Chem144_multi(Chem144):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan diagram reaksi seng oksida dengan asam nitrat berlebih berikut!\nGunakan informasi yang ditampilkan untuk menghitung persentase hasil (rendemen) seng nitrat.'
        self.description_chinese = '氧化锌与过量的硝酸反应。\n使用显示的信息来计算\n硝酸锌的产率。'
        self.description_arabic = 'يتفاعل أكسيد الزنك مع حمض النيتريك الزائد.\nاستخدم المعطيات لحساب النسبة المئوية لمردود نترات الزنك.'
        self.description_hindi = 'जिंक ऑक्साइड (Zinc oxide) अतिरिक्त नाइट्रिक अम्ल (nitric acid) के साथ अभिक्रिया करता है।\nदी गई जानकारी का उपयोग करके\nजिंक नाइट्रेट (zinc nitrate) की प्रतिशत उपज की गणना करें।'
        self.description_kazakh = 'Мырыш оксиді артық мөлшердегі азот қышқылымен әрекеттеседі.\nМырыш нитратының пайыздық шығымын есептеу үшін\nкөрсетілген ақпаратты пайдаланыңыз.'
        self.description_swahili = "Oksidi ya zinki (zinc oxide) inamenyuka na asidi ya nitriki (nitric acid) ya ziada. Tumia taarifa iliyoonyeshwa kukokotoa asilimia ya mavuno (percentage yield) ya nitrati ya zinki."

class Chem145_multi(Chem145):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan persamaan reaksi redoks yang ditampilkan pada gambar berikut!\nTentukan bilangan oksidasi unsur yang disorot.'
        self.description_chinese = '图像显示了一个氧化还原反应方程式。\n突出显示元素的氧化数是多少？'
        self.description_arabic = 'تُظهر الصورة معادلة تفاعل أكسدة واختزال.\nما عدد الأكسدة للعنصر المظلل؟'
        self.description_hindi = 'चित्र में एक रेडॉक्स अभिक्रिया का समीकरण दर्शाया गया है।\nहाइलाइट किए गए तत्व की ऑक्सीकरण संख्या क्या है?'
        self.description_kazakh = 'Суретте тотығу-тотықсыздану реакциясының теңдеуі көрсетілген.\nЕрекшеленген элементтің тотығу дәрежесі қандай?'
        self.description_swahili = "Picha hii inaonyesha mlinganyo wa mmenyuko wa redoksi (redox reaction). Je, namba ya oksidesheni ya elementi iliyoangaziwa ni ipi?"

class Chem146_multi(Chem146):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan persamaan reaksi yang ditampilkan pada gambar berikut!\nBerapa mol {self.product} yang terbentuk dari 1 mol {self.reactant}?'
        self.description_chinese = f'在图像中的反应里\n由 1 摩尔 {self.reactant} 会生成多少摩尔 {self.product}？'
        self.description_arabic = f'في التفاعل الموضح في الشكل، كم عدد مولات {self.product} المتكونة من 1 مول من {self.reactant}؟'
        self.description_hindi = f'चित्र में दी गई अभिक्रिया में,\n1 मोल {self.reactant} से कितने मोल उत्पाद {self.product} बनते हैं?'
        self.description_kazakh = f'Суреттегі реакцияда\n1 моль {self.reactant} затынан қанша моль {self.product} түзіледі?'
        self.description_swahili = f"Katika mmenyuko ulio kwenye picha, je, ni moli ngapi za {self.product} zinazoundwa kutoka moli 1 ya {self.reactant}?"

class Chem147_multi(Chem147):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f"Perhatikan persamaan fermentasi glukosa menghasilkan etanol yang ditampilkan pada diagram berikut!\nHitunglah berapa molekul {self.product_name} yang terbentuk dari {self.given_amount} molekul {self.reactant_name}."
        self.description_chinese = f"葡萄糖发酵产生乙醇。\n使用图中显示的方程式，计算：\n由 {self.given_amount} 个 {self.reactant_name} 分子会生成多少个 {self.product_name} 分子？"
        self.description_arabic = f'ينتج تخمير الجلوكوز الإيثانول.\nباستخدام المعادلة الموضحة، احسب:\nكم عدد جزيئات {self.product_name} المتكونة من {self.given_amount} جزيء من {self.reactant_name}؟'
        self.description_hindi = f"ग्लूकोज के किण्वन से इथेनॉल उत्पन्न होता है।\nआरेख में दिखाए गए समीकरण का उपयोग करके, गणना करें:\n{self.reactant_name} के {self.given_amount} {'अणु' if self.given_amount == 1 else 'अणुओं'} से {self.product_name} के कितने अणु बनते हैं?"
        self.description_kazakh = f"Глюкозаның ашуы нәтижесінде этанол түзіледі.\nДиаграммада көрсетілген теңдеуді пайдаланып, есептеңіз:\n{self.given_amount} {self.reactant_name} молекуласынан қанша {self.product_name} молекуласы түзіледі?"
        self.description_swahili = f"Uchachushaji wa glukosi unazalisha ethanoli.\nKwa kutumia mlinganyo unaoonyeshwa kwenye mchoro, kokotoa:\nJe, ni molekuli ngapi za {self.product_name} zinazoundwa kutoka molekuli {self.given_amount} za {self.reactant_name}?"

class Chem148_multi(Chem148):
    def __init__(self):
        super().__init__()
        self.description_indonesian = f'Perhatikan reaksi pembakaran sempurna yang ditampilkan pada diagram berikut!\nGunakan persamaan setara tersebut untuk menghitung berapa mol {self.product_name} yang dihasilkan dari 1 mol {self.reactant_name}.'
        self.description_chinese = f'图中显示了完全燃烧反应。\n使用图中的配平化学方程式，计算：\n由 1 摩尔 {self.reactant_name} 会生成多少摩尔 {self.product_name}？'
        self.description_arabic = f'يوضح الشكل تفاعل احتراق كامل.\nباستخدام المعادلة الموزونة، احسب:\nكم عدد مولات {self.product_name} الناتجة من 1 مول من {self.reactant_name}؟'
        self.description_hindi = f'पूर्ण दहन अभिक्रिया दर्शायी गई है।\nआरेख में दिए गए संतुलित समीकरण का उपयोग करके गणना कीजिए:\n1 मोल {self.reactant_name} से कितने मोल {self.product_name} बनते हैं?'
        self.description_kazakh = f'Толық жану реакциясы көрсетілген.\nДиаграммадағы теңестірілген теңдеуді пайдаланып, есептеңіз:\n1 моль {self.reactant_name} затынан қанша моль {self.product_name} түзіледі?'
        self.description_swahili = f"Mmenyuko kamili wa mwako (complete combustion) unaonyeshwa. Kwa kutumia mlinganyo uliosawazishwa kwenye mchoro, kokotoa: Je, ni moli ngapi za {self.product_name} zinazozalishwa kutoka moli 1 ya {self.reactant_name}?"

class Chem149_multi(Chem149):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan konfigurasi elektron suatu unsur yang ditampilkan pada gambar berikut!\nTentukan nomor golongannya menurut IUPAC (1–18).'
        self.description_chinese = '某元素具有图像中显示的电子排布。\n确定其族数（IUPAC 1–18）。'
        self.description_arabic = 'يوضح الشكل التوزيع الإلكتروني لعنصر.\nحدد رقم مجموعته (IUPAC من 1 إلى 18).'
        self.description_hindi = 'चित्र में दर्शाए गए इलेक्ट्रॉन विन्यास वाला एक तत्व है।\nइसका समूह क्रमांक ज्ञात कीजिए (IUPAC 1–18)।'
        self.description_kazakh = 'Элементтің электрондық конфигурациясы суретте көрсетілген.\nОның топ нөмірін анықтаңыз (IUPAC 1–18).'
        self.description_swahili = "Elementi ina mpangilio wa elektroni (electron configuration) kama inavyoonyeshwa kwenye picha. Tambua namba ya kundi lake (Group number) kwa mfumo wa IUPAC 1–18."

class Chem150_multi(Chem150):
    def __init__(self):
        super().__init__()
        self.description_indonesian = 'Perhatikan konfigurasi elektron suatu atom yang ditampilkan pada gambar berikut!\nKetika membentuk ion stabil, berapa elektron yang dilepaskan?'
        self.description_chinese = '某原子具有图像中显示的电子排布。\n当形成稳定离子时，它失去了多少个电子？'
        self.description_arabic = 'يوضح الشكل التوزيع الإلكتروني لذرة.\nعند تكوين أيون مستقر، كم عدد الإلكترونات التي تفقدها؟'
        self.description_hindi = 'चित्र में दर्शाए गए इलेक्ट्रॉन विन्यास वाला एक परमाणु है।\nस्थिर आयन बनाते समय कितने इलेक्ट्रॉन खो जाते हैं?'
        self.description_kazakh = 'Атомның электрондық конфигурациясы суретте көрсетілген.\nТұрақты ион түзген кезде қанша электрон жоғалады?'
        self.description_swahili = f'Atomi ina mpangilio wa elektroni (electron configuration) kama unavyoonyeshwa kwenye picha. Wakati wa kuunda ioni thabiti (stable ion), ni elektroni ngapi hupotea?'

