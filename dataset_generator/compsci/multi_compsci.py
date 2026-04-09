from templates_001_050 import *
from templates_051_100 import *

class Com001_multi(Com001):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'将图像中显示的十进制数转换为其二进制形式。'
        self.description_arabic = f'حوّل العدد العشري الموضح إلى النظام الثنائي.'
        self.description_hindi = f'चित्र में दर्शाई गई दशमलव संख्या को उसके बाइनरी रूप में परिवर्तित करें।'
        self.description_kazakh = f'Суретте көрсетілген ондық санды оның екілік түріне түрлендіріңіз.'
        self.description_swahili = f'Badilisha nambari ya desimali (decimal) inayoonyeshwa kwenye picha kwenda kwenye mfumo wake wa binari (binary).'

class Com002_multi(Com002):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'将图像中显示的二进制数转换为其十六进制形式。'
        self.description_arabic = f'حوّل العدد الثنائي الموضح إلى النظام السداسي عشر.'
        self.description_hindi = f'चित्र में दर्शाई गई बाइनरी संख्या को उसके हेक्साडेसिमल रूप में परिवर्तित करें।'
        self.description_kazakh = f'Суретте көрсетілген екілік санды оның он алтылық түріне түрлендіріңіз.'
        self.description_swahili = f'Badilisha nambari ya binari inayoonyeshwa kwenye picha kwenda kwenye mfumo wake wa heksadesimali (hexadecimal).'

class Com003_multi(Com003):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'将图像中显示的十六进制数转换为其十进制形式。'
        self.description_arabic = f'حوّل العدد السداسي عشر الموضح إلى النظام العشري.'
        self.description_hindi = f'चित्र में दर्शाई गई हेक्साडेसिमल संख्या को उसके दशम संख्या रूप में परिवर्तित करें।'
        self.description_kazakh = f'Суретте көрсетілген он алтылық санды оның ондық түріне түрлендіріңіз.'
        self.description_swahili = f'Badilisha nambari ya heksadesimali inayoonyeshwa kwenye picha kwenda kwenye mfumo wake wa denari (decimal).'

class Com004_multi(Com004):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如果我们将显示的两个8位无符号二进制数求和，并将结果存储在标准的8位寄存器中，在丢弃进位/溢出位后，最终的十进制值是多少？'
        self.description_arabic = f'احسب مجموع عددين ثنائيين من 8 بت وخزّنه في سجل 8 بت.\nبعد حذف بت الحمل (overflow)، ما القيمة العشرية النهائية؟'
        self.description_hindi = f'यदि हम दिखाए गए दो 8-bit अहस्ताक्षरित बाइनरी संख्याओं का योगफल निकालते हैं और परिणाम को एक मानक 8-bit रजिस्टर में संग्रहीत करते हैं, तो कैरी आउट/ओवरफ्लो bit को हटाने के बाद अंतिम दशमलव मान क्या होगा?'
        self.description_kazakh = f'Егер көрсетілген екі 8 биттік таңбасыз екілік санның қосындысын есептеп, нәтижені стандартты 8 биттік регистрде сақтасақ, тасымалдау/толып кету (Carry Out/overflow) биті алынып тасталғаннан кейінгі соңғы ондық мән қандай болады?'
        self.description_swahili = f'Ikiwa tutakokotoa jumla ya namba mbili za binari za biti 8 (8-bit unsigned binary) na kuhifadhi jibu katika rejista ya kawaida ya biti 8, ni ipi thamani ya mwisho ya desimali baada ya biti ya ziada (Carry Out/overflow) kutupwa?'

class Com005_multi(Com005):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"使用补码将图像中显示的二进制数表示为负数形式。"
        self.description_arabic = f"حوّل الأعداد الثنائية إلى صورتها السالبة باستخدام متمم الاثنين (Two's complement)."
        self.description_hindi = f"चित्र में दर्शाई गई बाइनरी संख्याओं को दो के पूरक का उपयोग करके उनके ऋणात्मक रूप में निरूपित करें।"
        self.description_kazakh = f"Суретте көрсетілген екілік сандарды қосымша код (two's complement) көмегімен теріс түрде көрсетіңіз."
        self.description_swahili = f"Wakilisha namba za binari zinazoonyeshwa kwenye picha katika umbo lake hasi kwa kutumia kikamilisho cha mbili (two's complement)."

class Com006_multi(Com006):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'传感器使用 {self.type} 校验以 {self.num_bytes}x{self.num_bytes} 数据块传输数据。在识别出下方数据块中的损坏位并将其翻转为正确值后，现在纠正后的行和纠正后的列中的位总和是多少？'
        self.description_arabic = f'يرسل مستشعر البيانات في كتلة بحجم {self.num_bytes}×{self.num_bytes} باستخدام تماثل {self.type}.\nبعد تحديد البت التالف في الكتلة أدناه وتصحيحه، ما هو المجموع الكلي للبتات في الصف والعمود المصححين معًا؟'
        self.description_hindi = f'एक सेंसर {self.type} Parity का उपयोग करके {self.num_bytes}x{self.num_bytes} ब्लॉक में डेटा ट्रांसमिट करता है। नीचे दिए गए डेटा ब्लॉक में दूषित (corrupted) बिट की पहचान करने और उसे उसके सही मान में बदलने (flip) के बाद, अब सही की गई पंक्ति (row) और सही किए गए कॉलम (column) के बिट्स को मिलाकर उनका कुल योग क्या है?'
        self.description_kazakh = f'Датчик деректерді {self.type} жұптығын (Parity) пайдаланып {self.num_bytes}x{self.num_bytes} блогында тасымалдайды. Төмендегі деректер блогындағы зақымдалған битті анықтап, оны дұрыс мәніне ауыстырғаннан кейін, түзетілген қатар мен түзетілген бағандағы биттердің жалпы қосындысы енді қанша болады?'
        self.description_swahili = f'Kitambuzi kinatuma data katika kitalu cha {self.num_bytes}x{self.num_bytes} kwa kutumia Pariti (Parity) ya {self.type}. Baada ya kutambua biti iliyoharibika katika kitalu cha data kilicho hapa chini, na kuigeuza (flip) kuwa thamani yake sahihi, ni nini jumla ya biti zote katika safumlalo na safuwima zilizosahihishwa kwa pamoja?'

class Com007_multi(Com007):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了一种搜索算法的伪代码。如果目标值 (x) 设置为 {self.target}，最终显示的输出是什么？'
        self.description_arabic = f'تعرض الصورة كودًا زائفًا (pseudocode) لخوارزمية بحث.\nإذا كانت قيمة الهدف (x) هي {self.target}، فما هي النتيجة النهائية المعروضة؟'
        self.description_hindi = f'यह चित्र एक खोज एल्गोरिदम के लिए स्यूडोकोड (pseudocode) दिखा रही है। यदि लक्ष्य (x) को {self.target} पर सेट किया जाता है, तो अंतिम आउटपुट क्या प्रदर्शित होगा?'
        self.description_kazakh = f'Бұл суретте іздеу алгоритмінің псевдокоды көрсетілген. Егер мақсат (x) {self.target} етіп орнатылса, көрсетілген соңғы шығыс қандай болады?'
        self.description_swahili = f'Picha hii inaonyesha misimbo ghushi (pseudocode) ya algoriti ya kutafuta (searching algorithm). Ikiwa lengwa (x) limewekwa kuwa {self.target}, ni towe gani la mwisho linaloonyeshwa?'

class Com008_multi(Com008):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个人正在测量他们一周中每天的步行步数：{self.steps}。根据下面显示的伪代码，最终显示的输出是什么？'
        self.description_arabic = f'يقيس شخص عدد خطواته يوميًا خلال الأسبوع: {self.steps}.\nوفقًا للكود الزائف الموضح، ما هي النتيجة النهائية المعروضة؟'
        self.description_hindi = f'एक व्यक्ति सप्ताह के प्रत्येक दिन अपने चलने के कदमों की संख्या माप रहा है: {self.steps}। नीचे दिखाए गए स्यूडोकोड (pseudocode) के अनुसार, अंतिम आउटपुट क्या प्रदर्शित होगा?'
        self.description_kazakh = f'Бір адам аптаның әр күні үшін жаяу жүру қадамдарының санын өлшейді: {self.steps}. Төменде көрсетілген псевдокодқа сәйкес, көрсетілген соңғы шығыс қандай болады?'
        self.description_swahili = f'Mtu anapima idadi ya hatua zake za kutembea kwa kila siku ya wiki: {self.steps}. Kulingana na misimbo ghushi (pseudocode) inayoonyeshwa hapa chini, ni towe gani la mwisho linaloonyeshwa?'

class Com009_multi(Com009):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了一种排序算法的伪代码。给定未排序的数字数组，需要多少次交换才能对数据进行排序？'
        self.description_arabic = f'تعرض الصورة كودًا زائفًا لخوارزمية فرز.\nبناءً على المصفوفة غير المرتبة، كم عدد عمليات التبديل اللازمة لفرز البيانات؟'
        self.description_hindi = f'यह चित्र एक सॉर्टिंग एल्गोरिदम के लिए स्यूडोकोड (pseudocode) दिखा रही है। संख्याओं के एक अव्यवस्थित ऐरे को देखते हुए, डेटा को सॉर्ट करने के लिए कितने स्वैप की आवश्यकता होगी?'
        self.description_kazakh = f'Бұл суретте сұрыптау алгоритмінің псевдокоды көрсетілген. Сұрыпталмаған сандар массиві берілген болса, деректерді сұрыптау үшін қанша алмастыру (swap) қажет болады?'
        self.description_swahili = f'Picha hii inaonyesha misimbo ghushi (pseudocode) ya algoriti ya kupanga (sorting algorithm). Kwa kuzingatia safu (array) ya namba zisizopangwa, itachukua ubadilishanaji (swaps) mingapi kupanga data hiyo?'

class Com010_multi(Com010):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'下图是一个程序的流程图。如果输入 N 为 {self.N_copy}，合共的最终值是多少？'
        self.description_arabic = f'يوضح الشكل مخططًا انسيابيًا لبرنامج.\nما هي القيمة النهائية للمتغير total إذا كان N = {self.N_copy}؟'
        self.description_hindi = f'नीचे दी गई चित्र में एक प्रोग्राम का फ्लोचार्ट दिया गया है। यदि इनपुट N, {self.N_copy} है, तो total का अंतिम मान क्या होगा?'
        self.description_kazakh = f'Төмендегі суретте бағдарламаның блок-схемасы берілген. Егер енгізілген N мәні {self.N_copy} болса, total айнымалысының соңғы мәні қандай болады?'
        self.description_swahili = f'Chati mtiririko (flowchart) ya programu imetolewa katika picha hapa chini. Thamani ya mwisho ya kiambajengo cha "total" ni ipi, ikiwa ingizo N ni {self.N_copy}?'

class Com011_multi(Com011):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'使用搜索算法在数组 (x) 中查找目标值 (y)。该算法的伪代码如下方图像所示。如果我们从当前位置开始下一次比较，包括找到目标值的那次比较在内，一共进行了多少次比较？'
        self.description_arabic = f'تُستخدم خوارزمية بحث لإيجاد القيمة y داخل مصفوفة x.\nيظهر الكود الزائف في الصورة.\nإذا بدأنا كل مقارنة من الموضع الحالي، فكم عدد المقارنات حتى العثور على القيمة (بما في ذلك المقارنة الأخيرة)؟'
        self.description_hindi = f'एक सर्चिंग एल्गोरिदम (searching algorithm) का उपयोग करके एक ऐरे (x) में लक्ष्य मान (y) का पता लगाया जाता है। एल्गोरिदम का स्यूडोकोड (pseudocode) नीचे दिए गए चित्र में दिखाया गया है। यदि हम अगली तुलना वर्तमान स्थिति से शुरू करते हैं, तो लक्ष्य मान प्राप्त करने वाली तुलना सहित कितनी तुलनाएँ की जाती हैं?'
        self.description_kazakh = f'Іздеу алгоритмі массивтегі (x) мақсатты мәнді (y) табу үшін қолданылады. Алгоритмнің псевдокоды төмендегі суретте көрсетілген. Егер келесі салыстыруды ағымдағы орыннан бастасақ, мақсатты мән табылған салыстыруды қосқанда барлығы неше салыстыру жасалады?'
        self.description_swahili = f'Algoriti ya kutafuta inatumika kupata thamani lengwa (y) katika safu (x). Misimbo ghushi (pseudocode) ya algoriti hiyo inaonyeshwa katika picha hapa chini. Ikiwa tutaanza ulinganisho unaofuata kutoka kwenye nafasi ya sasa, ni milinganisho mingapi itafanywa ukijumuisha ule ulinganisho ambao thamani lengwa inapatikana?'

class Com012_multi(Com012):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'这是一张显示了一个简单 Python 程序的图像。如果我们给定的输入 = {self.n}，打印出的 total 值将是多少？'
        self.description_arabic = f'تعرض الصورة برنامج Python بسيطًا.\nإذا كان الإدخال هو {self.n}، فما القيمة النهائية للمتغير total التي سيتم طباعتها؟'
        self.description_hindi = f'यहां एक साधारण Python प्रोग्राम का चित्र दिया गया है। यदि हम इनपुट के रूप में {self.n} देते हैं, तो मुद्रित कुल मान क्या होगा?'
        self.description_kazakh = f'Бұл суретте қарапайым Python бағдарламасы көрсетілген. Егер енгізу = {self.n} берсек, басып шығарылатын total мәні қандай болады?'
        self.description_swahili = f'Hapa kuna picha inayoonyesha programu rahisi ya Python. Ikiwa tutatoa ingizo (input) la {self.n}, thamani ya jumla (total) itakayochapishwa itakuwa nini?'

class Com013_multi(Com013):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'此图像显示了一段简单的字符串处理代码。如果输入 s 为 "{self.text}" 且输入 c 为 "{self.ch}"，此代码的输出将打印什么？'
        self.description_arabic = f'تعرض الصورة كودًا بسيطًا لمعالجة النصوص.\nإذا كان s = "{self.text}" و c = "{self.ch}"، فما الناتج المطبوع؟'
        self.description_hindi = f'यह चित्र एक सरल स्ट्रिंग हैंडलिंग कोड दिखा रही है। यदि इनपुट s "{self.text}" है और इनपुट c "{self.ch}" है, तो इस कोड का आउटपुट क्या होगा?'
        self.description_kazakh = f'Бұл суретте жолдарды өңдейтін қарапайым код көрсетілген. Егер енгізілген s мәні "{self.text}" және енгізілген c мәні "{self.ch}" болса, бұл кодтың шығысы ретінде не басып шығарылады?'
        self.description_swahili = f'Picha hii inaonyesha msimbo rahisi wa kushughulikia maandishi (string handling). Ikiwa ingizo s ni "{self.text}" na ingizo c ni "{self.ch}", nini kitachapishwa kama towe (output) la msimbo huu?'

class Com014_multi(Com014):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定的图像包含一段涉及二维数组的 Python 代码。如果输入为 {self.input}，最终结果将是什么？'
        self.description_arabic = f'تحتوي الصورة على كود Python يتعامل مع مصفوفة ثنائية الأبعاد.\nإذا كان الإدخال {self.input}، فما النتيجة النهائية؟'
        self.description_hindi = f'दी गई चित्र में दो-आयामी ऐरे से संबंधित पायथन कोड है। यदि इनपुट {self.input} हो, तो अंतिम परिणाम क्या होगा?'
        self.description_kazakh = f'Берілген суретте екі өлшемді массивке қатысты Python коды бар. Егер енгізу {self.input} болса, соңғы нәтиже қандай болады?'
        self.description_swahili = f'Picha iliyotolewa ina msimbo wa Python unaohusisha safu ya pande mbili (2D array). Je, matokeo ya mwisho yatakuwa nini, ikiwa ingizo (input) ni {self.input}?'

class Com015_multi(Com015):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'在线商店的销售数据存储在名为 Orders 的表中，如图所示。店主运行查询：SELECT COUNT(OrderID) FROM Orders WHERE Items < {self.items_threshold} AND Total >= {self.total_threshold};。输出应该是什么？'
        self.description_arabic = f'تُخزن بيانات المبيعات في جدول Orders كما هو موضح.\nينفذ الاستعلام التالي:\nSELECT COUNT(OrderID) FROM Orders WHERE Items < {self.items_threshold} AND Total >= {self.total_threshold};\nما الناتج؟'
        self.description_hindi = f'ऑनलाइन दुकान से प्राप्त बिक्री डेटा को Orders नामक तालिका में संग्रहित किया जाता है, जैसा कि चित्र में दिखाया गया है। दुकान का मालिक निम्न क्वेरी चलाता है: SELECT COUNT(OrderID) FROM Orders WHERE Items < {self.items_threshold} AND Total >= {self.total_threshold};। इसका आउटपुट क्या होना चाहिए?'
        self.description_kazakh = f'Интернет-дүкеннің сату деректері суретте көрсетілгендей Orders деп аталатын кестеде сақталған. Иесі келесі сұранысты орындайды: SELECT COUNT(OrderID) FROM Orders WHERE Items < {self.items_threshold} AND Total >= {self.total_threshold};. Шығыс қандай болуы керек?'
        self.description_swahili = f'Data ya mauzo kutoka duka la mtandaoni imehifadhiwa katika jedwali linaloitwa "Orders", kama inavyoonyeshwa kwenye picha. Mmiliki anaendesha hoja (query) ifuatayo: SELECT COUNT(OrderID) FROM Orders WHERE Items < {self.items_threshold} AND Total >= {self.total_threshold};. Je, towe (output) linapaswa kuwa nini?'

class Com016_multi(Com016):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图像中的下表显示了 2025 年 1 月的笔记本电脑销售情况。如果 x 为 {self.query_type}，其下方的 SQL 语句输出的值是多少？'
        self.description_arabic = f'يوضح الجدول مبيعات أجهزة كمبيوتر محمولة في يناير 2025.\nما القيمة الناتجة من تعليمة SQL إذا كان x = {self.query_type}؟'
        self.description_hindi = f'चित्र में निम्नलिखित तालिका जनवरी 2025 में की गई लैपटॉप की बिक्री को दर्शाती है। यदि x, {self.query_type} है, तो इसके नीचे दिए गए SQL स्टेटमेंट द्वारा कौन सा मान आउटपुट किया जाएगा?'
        self.description_kazakh = f'Суреттегі келесі кестеде 2025 жылдың қаңтар айында жасалған ноутбук сатылымдары көрсетілген. Егер x {self.query_type} болса, оның төменіндегі SQL операторы қандай мәнді шығарады?'
        self.description_swahili = f'Jedwali lifuatalo katika picha linaonyesha mauzo ya kompyuta mpakato (laptop) yaliyofanywa Januari 2025. Ni thamani gani inatolewa kama towe (output) na kauli ya SQL iliyo chini yake, ikiwa x ni {self.query_type}?'

class Com017_multi(Com017):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定此逻辑电路图像，如果 A 为 {self.input_1}，B 为 {self.input_2}，C 为 {self.input_3}，D 为 {self.input_4}，请测定O 的输出。'
        self.description_arabic = f'بناءً على دائرة منطقية في الصورة، حدّد قيمة O إذا كانت A = {self.input_1}، و B = {self.input_2}، و C = {self.input_3}، و D = {self.input_4}.'
        self.description_hindi = f'लॉजिक सर्किट की इस चित्र को देखते हुए, O का आउटपुट निर्धारित करें यदि A, {self.input_1} है, B, {self.input_2} है, C, {self.input_3} है, और D, {self.input_4} है।'
        self.description_kazakh = f'Логикалық схеманың осы суретін ескере отырып, егер A {self.input_1}, B {self.input_2}, C {self.input_3} және D {self.input_4} болса, O шығысын анықтаңыз.'
        self.description_swahili = f'Kwa kuzingatia picha hii ya saketi ya mantiki (logic circuit), tafuta towe (output) la O ikiwa A ni {self.input_1}, B ni {self.input_2}, C ni {self.input_3}, na D ni {self.input_4}.'

class Com018_multi(Com018):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定此逻辑电路图像，如果输入 A 为 {self.input_1}，B 为 {self.input_2}，C 为 {self.input_3}，D 为 {self.input_4}，请测定 O 的输出。'
        self.description_arabic = f'بناءً على دائرة منطقية في الصورة، حدّد قيمة O إذا كان الإدخال A = {self.input_1}، و B = {self.input_2}، و C = {self.input_3}، و D = {self.input_4}.'
        self.description_hindi = f'लॉजिक सर्किट की इस चित्र को देखते हुए, O का आउटपुट निर्धारित करें यदि Input A, {self.input_1} है, B, {self.input_2} है, C, {self.input_3} है, और D, {self.input_4} है।'
        self.description_kazakh = f'Логикалық схеманың осы суретін ескере отырып, егер A кірісі {self.input_1}, B {self.input_2}, C {self.input_3} және D {self.input_4} болса, O шығысын анықтаңыз.'
        self.description_swahili = f'Kwa kuzingatia picha hii ya saketi ya mantiki (logic circuit), tafuta towe la O ikiwa Ingizo A ni {self.input_1}, B ni {self.input_2}, C ni {self.input_3}, na D ni {self.input_4}.'

class Com019_multi(Com019):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定此逻辑电路图像，如果输入 A 为 {self.input_1}，B 为 {self.input_2}，C 为 {self.input_3}，D 为 {self.input_4}，F 的输出是什么？'
        self.description_arabic = f'بناءً على دائرة منطقية في الصورة، ما قيمة F إذا كان الإدخال A = {self.input_1}، و B = {self.input_2}، و C = {self.input_3}، و D = {self.input_4}؟'
        self.description_hindi = f'लॉजिक सर्किट की इस चित्र को देखते हुए, F का आउटपुट क्या है यदि Input A, {self.input_1} है, B, {self.input_2} है, C, {self.input_3} है, और D, {self.input_4} है?'
        self.description_kazakh = f'Логикалық схеманың осы суретін ескере отырып, егер A кірісі {self.input_1}, B {self.input_2}, C {self.input_3} және D {self.input_4} болса, F шығысы қандай болады?'
        self.description_swahili = f'Kwa kuzingatia picha hii ya saketi ya mantiki (logic circuit), ni nini towe la F ikiwa Ingizo A ni {self.input_1}, B ni {self.input_2}, C ni {self.input_3}, na D ni {self.input_4}?'

class Com020_multi(Com020):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定此逻辑电路图像，如果输入 A 为 {self.input_1}，B 为 {self.input_2}，C 为 {self.input_3}，D 为 {self.input_4}， F 的输出是什么？'
        self.description_arabic = f'بناءً على دائرة منطقية في الصورة، ما قيمة F إذا كان الإدخال A = {self.input_1}، و B = {self.input_2}، و C = {self.input_3}، و D = {self.input_4}؟'
        self.description_hindi = f'दिए गए लॉजिक सर्किट के चित्र को देखते हुए, F का आउटपुट क्या होगा यदि इनपुट A {self.input_1}, B {self.input_2}, C {self.input_3} और D {self.input_4} है?'
        self.description_kazakh = f'Логикалық схеманың осы суретін ескере отырып, егер A кірісі {self.input_1}, B {self.input_2}, C {self.input_3} және D {self.input_4} болса, F шығысы қандай болады?'
        self.description_swahili = f'Kwa kuzingatia picha hii ya saketi ya mantiki (logic circuit), ni nini towe la F ikiwa Ingizo A ni {self.input_1}, B ni {self.input_2}, C ni {self.input_3}, na D ni {self.input_4}?'

class Com021_multi(Com021):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定此逻辑电路图像，如果输入 A 为 {self.input_1}，B 为 {self.input_2}，C 为 {self.input_3}，D 为 {self.input_4}，F 的输出是什么？'
        self.description_arabic = f'بناءً على دائرة منطقية في الصورة، ما قيمة F إذا كان الإدخال A = {self.input_1}، و B = {self.input_2}، و C = {self.input_3}، و D = {self.input_4}؟'
        self.description_hindi = f'लॉजिक सर्किट की इस चित्र को देखते हुए, F का आउटपुट क्या है यदि Input A, {self.input_1} है, B, {self.input_2} है, C, {self.input_3} है, और D, {self.input_4} है?'
        self.description_kazakh = f'Логикалық схеманың осы суретін ескере отырып, егер A кірісі {self.input_1}, B {self.input_2}, C {self.input_3} және D {self.input_4} болса, F шығысы қандай болады?'
        self.description_swahili = f'Kwa kuzingatia picha hii ya saketi ya mantiki (logic circuit), ni nini towe la F ikiwa Ingizo A ni {self.input_1}, B ni {self.input_2}, C ni {self.input_3}, na D ni {self.input_4}?'

class Com022_multi(Com022):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'此图像显示了一个 BCD（二进制编码的十进制数）。将该 BCD 转换为其十进制表示。'
        self.description_arabic = f'تعرض الصورة تمثيل BCD (عشري مشفر ثنائيًا).\nحوّله إلى النظام العشري.'
        self.description_hindi = f'यह चित्र एक BCD (बाइनरी कोडेड डेसिमल) प्रदर्शित कर रही है। BCD को उसके दशमलव रूप में परिवर्तित करें।'
        self.description_kazakh = f'Бұл суретте BCD (Binary Coded Decimal) көрсетілген. BCD кодын оның ондық көрінісіне түрлендіріңіз.'
        self.description_swahili = f'Picha hii inaonyesha BCD (Desimali Iliyosimbwa kwa Binari). Badili BCD hiyo kwenda kwenye uwakilishi wake wa desimali (decimal representation).'

class Com023_multi(Com023):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'求这两个 8 位数（如图所示）的差值，结果以十进制值表示。'
        self.description_arabic = f'أوجد ناتج طرح العددين المكونين من 8 بت (كما في الصورة) وعبّر عنهما بالنظام العشري.'
        self.description_hindi = f'चित्र में दर्शाई गई इन दो 8-bit संख्याओं का घटाव दशमलव मान के रूप में ज्ञात कीजिए।'
        self.description_kazakh = f'Суретте көрсетілген екі 8-биттік санның айырмасын (азайту нәтижесін) ондық мән түрінде табыңыз.'
        self.description_swahili = f'Tafuta matokeo ya kutoa namba hizi mbili za biti-8 (zinazoonyeshwa kwenye picha) katika mfumo wa thamani ya desimali.'

class Com024_multi(Com024):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一位计算机科学家创建了此图像中显示的以下逻辑电路。如果输入 A 给定为 {self.input_1}，B 给定为 {self.input_2}，C 给定为 {self.input_3}，D 给定为 {self.input_4}，F 的输出是什么？'
        self.description_arabic = f'أنشأ عالم حاسوب دائرة منطقية كما في الصورة.\nما قيمة F إذا كانت A = {self.input_1}، و B = {self.input_2}، و C = {self.input_3}، و D = {self.input_4}؟'
        self.description_hindi = f'एक कंप्यूटर वैज्ञानिक ने इस चित्र में दर्शाए गए लॉजिक सर्किट का निर्माण किया है। यदि इनपुट A को {self.input_1}, B को {self.input_2}, C को {self.input_3} और D को {self.input_4} दिया जाए, तो F का आउटपुट क्या होगा?'
        self.description_kazakh = f'Информатик осы суретте көрсетілген келесі логикалық схеманы жасады. Егер A кірісіне {self.input_1}, B кірісіне {self.input_2}, C кірісіне {self.input_3} және D кірісіне {self.input_4} берілсе, F шығысы қандай болады?'
        self.description_swahili = f'Mwanasayansi wa kompyuta ametengeneza saketi ya mantiki (logic circuit) ifuatayo inayoonyeshwa kwenye picha hii. Je, towe la F litakuwa nini ikiwa Ingizo A limepewa {self.input_1}, B limepewa {self.input_2}, C limepewa {self.input_3}, na D limepewa {self.input_4}?'

class Com025_multi(Com025):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'请看此图像中显示的以下逻辑电路。如果输入 A 给定为 {self.input_1}，B 给定为 {self.input_2}，C 给定为 {self.input_3}，D 给定为 {self.input_4}，E 给定为 {self.input_5}，Z 的输出将是什么？'
        self.description_arabic = f'انظر إلى الدائرة المنطقية في الصورة.\nما قيمة Z إذا كانت A = {self.input_1}، و B = {self.input_2}، و C = {self.input_3}، و D = {self.input_4}، و E = {self.input_5}؟'
        self.description_hindi = f'इस चित्र में दिखाए गए लॉजिक सर्किट को देखें। यदि इनपुट A को {self.input_1}, B को {self.input_2}, C को {self.input_3}, D को {self.input_4} और E को {self.input_5} दिया जाए, तो Z का आउटपुट क्या होगा?'
        self.description_kazakh = f'Осы суретте көрсетілген келесі логикалық схемаға қараңыз. Егер A кірісіне {self.input_1}, B кірісіне {self.input_2}, C кірісіне {self.input_3}, D кірісіне {self.input_4} және E кірісіне {self.input_5} берілсе, Z шығысы қандай болады?'
        self.description_swahili = f'Angalia saketi ya mantiki (logic circuit) ifuatayo inayoonyeshwa kwenye picha hii. Je, towe la Z litakuwa nini ikiwa Ingizo A limepewa {self.input_1}, B limepewa {self.input_2}, C limepewa {self.input_3}, D limepewa {self.input_4}, na E limepewa {self.input_5}?'

class Com026_multi(Com026):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了一个逻辑电路，其中 Y2 给定输入 {self.input_1}，Y1 给定输入 {self.input_2}，Y0 给定输入 {self.input_3}，X 给定输入 {self.input_4}。该电路产生输出 D2、D1、D0 和 Y，这些输出拼接成一个以 D2 为最高有效位的两位二进制数。将此两位二进制数转换为其十进制值，并将其作为最终答案。'
        self.description_arabic = f'يوضح الشكل دائرة منطقية حيث Y2 = {self.input_1}، و Y1 = {self.input_2}، و Y0 = {self.input_3}، و X = {self.input_4}.\nتنتج الدائرة القيم D2 و D1 و D0 و Y، والتي تُدمج لتكوين عدد ثنائي.\nحوّل هذا العدد إلى قيمته العشرية.'
        self.description_hindi = f'चित्र में एक लॉजिक सर्किट दिखाया गया है, जिसमें Y2 को इनपुट {self.input_1}, Y1 को इनपुट {self.input_2}, Y0 को इनपुट {self.input_3} और X को इनपुट {self.input_4} दिया गया है। सर्किट से आउटपुट D2, D1, D0 और Y प्राप्त होते हैं, जिन्हें जोड़कर एक दो-बिट बाइनरी संख्या बनाई जाती है, जिसमें D2 सबसे महत्वपूर्ण बिट है। इस दो-बिट बाइनरी संख्या को इसके दशमलव मान में परिवर्तित करें और इसे अंतिम उत्तर के रूप में बताएं।'
        self.description_kazakh = f'Диаграммада Y2-ге {self.input_1} кірісі, Y1-ге {self.input_2} кірісі, Y0-ге {self.input_3} кірісі және X-ке {self.input_4} кірісі берілген логикалық схема көрсетілген. Схема D2, D1, D0 және Y шығыстарын береді, олар ең үлкен разрядты бит (most significant bit) ретінде D2 болатын екі биттік екілік санды құру үшін біріктіріледі. Осы екі биттік екілік санды ондық мәніне түрлендіріңіз және оны соңғы жауап ретінде көрсетіңіз.'
        self.description_swahili = f'Mchoro unaonyesha saketi ya mantiki ambapo Y2 inapewa ingizo {self.input_1}, Y1 inapewa ingizo {self.input_2}, Y0 inapewa ingizo {self.input_3}, na X inapewa ingizo {self.input_4}. Saketi hiyo inazalisha matowe D2, D1, D0, na Y, ambayo yanaunganishwa kuunda namba ya binari ya biti mbili (huku D2 ikiwa ndiyo biti yenye uzito mkubwa zaidi/MSB). Badili namba hii ya binari kuwa thamani ya desimali na utoe jibu hilo kama matokeo ya mwisho.'

class Com027_multi(Com027):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'下图显示了一个逻辑电路，它根据发动机状况向飞机飞行员发出警告灯。当输出 W 出现高电平 (1) 时，警告灯变为开启 (ON)。当温度 > {self.temp_threshold}°C 时，温度传感器输出高电平。当压力 > {self.pressure_threshold} kPa 时，压力传感器输出高电平。当 RPM > {self.RPM_threshold} rpm 时，转速 (RPM) 传感器输出高电平。如果测量值为：温度 = {self.temp}°C，压力 = {self.pressure} kPa，RPM = {self.RPM} rpm，请确定警告灯 W 的状态（0 或 1）。'
        self.description_arabic = f'يوضح الشكل دائرة منطقية تعطي ضوء تحذير لطيار الطائرة بناءً على ظروف المحرك.\nيضيء الضوء (ON) عندما يكون المخرج W = 1.\nيُخرج مستشعر الحرارة قيمة HIGH عندما تكون درجة الحرارة > {self.temp_threshold}°C.\nويُخرج مستشعر الضغط قيمة HIGH عندما يكون الضغط > {self.pressure_threshold} kPa.\nويُخرج مستشعر عدد الدورات (RPM) قيمة HIGH عندما يكون RPM > {self.RPM_threshold} rpm.\nإذا كانت القيم المقاسة: درجة الحرارة = {self.temp}°C، والضغط = {self.pressure} kPa، و RPM = {self.RPM} rpm، فما حالة W (0 أو 1)؟'
        self.description_hindi = f'नीचे दिए गए चित्र में एक लॉजिक सर्किट दिखाया गया है जो इंजन की स्थिति के आधार पर विमान के पायलट को चेतावनी देता है। आउटपुट W पर उच्च (1) स्तर होने पर चेतावनी लाइट चालू हो जाती है। तापमान सेंसर उच्च आउटपुट देता है जब तापमान {self.temp_threshold}°C से अधिक होता है। दबाव सेंसर उच्च आउटपुट देता है जब दबाव {self.pressure_threshold} किलोपैसे से अधिक होता है। RPM सेंसर उच्च आउटपुट देता है जब RPM > {self.RPM_threshold} RPM से अधिक होता है। यदि मापे गए मान हैं: तापमान = {self.temp}°C, दबाव = {self.pressure} kPa, RPM = {self.RPM} RPM, तो चेतावनी लाइट W की स्थिति (0 या 1) ज्ञात कीजिए।'
        self.description_kazakh = f'Төменде берілген суретте қозғалтқыш жағдайларына байланысты ұшақ ұшқышына ескерту шамын беретін логикалық схема көрсетілген. W шығысында HIGH (1) деңгейі болған кезде ескерту шамы ON (қосылған) болады. Температура > {self.temp_threshold}°C болғанда температура датчигі HIGH мәнін шығарады. Қысым > {self.pressure_threshold} kPa болғанда қысым датчигі HIGH мәнін шығарады. RPM > {self.RPM_threshold} rpm болғанда RPM датчигі HIGH мәнін шығарады. Егер өлшенген мәндер: Температура = {self.temp}°C, Қысым = {self.pressure} kPa, RPM = {self.RPM} rpm болса, W ескерту шамының күйін (0 немесе 1) анықтаңыз.'
        self.description_swahili = f'Kielelezo kilichotolewa hapa chini kinaonyesha saketi ya mantiki inayotoa mwanga wa onyo kwa rubani wa ndege kulingana na hali ya injini. Mwanga wa onyo huwaka (ON) kunapokuwa na kiwango cha JUU (1) kwenye towe W. Kitambuzi cha halijoto hutoa JUU (1) ikiwa halijoto > {self.temp_threshold}°C. Kitambuzi cha shinikizo hutoa JUU (1) ikiwa shinikizo > {self.pressure_threshold} kPa. Kitambuzi cha RPM hutoa JUU (1) ikiwa RPM > {self.RPM_threshold} rpm. Ikiwa vipimo vilivyopatikana ni: Halijoto = {self.temp}°C, Shinikizo = {self.pressure} kPa, na RPM = {self.RPM} rpm, tambua hali ya mwanga wa onyo W (0 au 1).'

class Com028_multi(Com028):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'这是一张逻辑电路的图像，其中输入 A = {self.input_1}，输入 B = {self.input_2}，输入 C = {self.input_3}，输入 D = {self.input_4}，输入 E = {self.input_5}。基于显示的电路，最终输出 X 是什么？'
        self.description_arabic = f'تعرض الصورة دائرة منطقية حيث A = {self.input_1}، و B = {self.input_2}، و C = {self.input_3}، و D = {self.input_4}، و E = {self.input_5}.\nبناءً على الدائرة، ما قيمة المخرج X؟'
        self.description_hindi = f'यहां एक लॉजिक सर्किट का चित्र दिया गया है, जिसमें इनपुट A = {self.input_1}, इनपुट B = {self.input_2}, इनपुट C = {self.input_3}, इनपुट D = {self.input_4}, और इनपुट E = {self.input_5} है। दिखाए गए सर्किट के आधार पर, अंतिम आउटपुट X क्या होगा?'
        self.description_kazakh = f'Мұнда A кірісі = {self.input_1}, B кірісі = {self.input_2}, C кірісі = {self.input_3}, D кірісі = {self.input_4} және E кірісі = {self.input_5} болатын логикалық схеманың суреті берілген. Көрсетілген схема негізінде X соңғы шығысы қандай болады?'
        self.description_swahili = f'Hapa kuna picha ya saketi ya mantiki (logic circuit) ambapo ingizo A = {self.input_1}, ingizo B = {self.input_2}, ingizo C = {self.input_3}, ingizo D = {self.input_4}, na ingizo E = {self.input_5}. Kulingana na saketi inayoonyeshwa, je, towe la mwisho X ni nini?'

class Com029_multi(Com029):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'下图显示了一系列汇编语言指令。给定输入 {self.input_1}（用于第一个 IN）和 {self.input_2}（用于第二个 IN），追踪程序的执行，然后说出最终输出的值。'
        self.description_arabic = f'توضح الصورة سلسلة من تعليمات لغة التجميع (Assembly).\nبناءً على المدخلين {self.input_1} (للأمر IN الأول) و {self.input_2} (للأمر IN الثاني)، تتبع تنفيذ البرنامج وحدد قيمة المخرج النهائي.'
        self.description_hindi = f'नीचे दी गई चित्र असेंबली भाषा निर्देशों का एक क्रम दर्शाती है। दिए गए इनपुट {self.input_1} (पहले इनपुट के लिए) और {self.input_2} (दूसरे इनपुट के लिए) के आधार पर, प्रोग्राम के निष्पादन का पता लगाएं और फिर अंतिम आउटपुट का मान बताएं।'
        self.description_kazakh = f'Келесі суретте ассемблер тілі нұсқауларының тізбегі көрсетілген. {self.input_1} (бірінші IN үшін) және {self.input_2} (екінші IN үшін) кірістері берілген болса, бағдарламаның орындалуын қадағалаңыз, содан кейін соңғы шығыстың мәнін көрсетіңіз.'
        self.description_swahili = f'Picha ifuatayo inaonyesha mfuatano wa maagizo ya lugha ya asambili (assembly language). Kwa kuzingatia maingizo {self.input_1} (kwa IN ya kwanza) na {self.input_2} (kwa IN ya pili), fuatilia utekelezaji wa programu kisha ueleze thamani ya towe la mwisho (final output).'

class Com030_multi(Com030):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'下图显示了一系列汇编语言指令。给定输入 {self.input}，追踪程序的执行，然后说出最终输出的值。'
        self.description_arabic = f'توضح الصورة سلسلة من تعليمات لغة التجميع.\nبناءً على المدخل {self.input}، تتبع تنفيذ البرنامج وحدد قيمة المخرج النهائي.'
        self.description_hindi = f'नीचे दी गई चित्र असेंबली भाषा के निर्देशों का एक क्रम दर्शाती है। इनपुट {self.input} दिए जाने पर, प्रोग्राम के निष्पादन का पता लगाएं और फिर अंतिम आउटपुट का मान बताएं।'
        self.description_kazakh = f'Келесі суретте ассемблер тілі нұсқауларының тізбегі көрсетілген. {self.input} кірісі берілген болса, бағдарламаның орындалуын қадағалаңыз, содан кейін соңғы шығыстың мәнін көрсетіңіз.'
        self.description_swahili = f'Picha ifuatayo inaonyesha mfuatano wa maagizo ya lugha ya asambili (assembly language). Kwa kuzingatia ingizo {self.input}, fuatilia utekelezaji wa programu kisha ueleze thamani ya towe la mwisho.'

class Com031_multi(Com031):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"表 'plant_shipment' 存储有关植物运输的详细信息。数据库管理员运行以下 SQL 语句：UPDATE plant_shipment SET health_score = health_score + {self.increase} WHERE health_score < {self.threshold};执行该查询后，计算 `health_score` 列的总和 (sum)。"
        self.description_arabic = f"يخزن الجدول 'plant_shipment' بيانات شحن النباتات.\nينفذ مسؤول قاعدة البيانات التعليمة التالية:\nUPDATE plant_shipment SET health_score = health_score + {self.increase} WHERE health_score < {self.threshold};\nبعد التنفيذ، احسب مجموع العمود `health_score`."
        self.description_hindi = f"'plant_shipment' नामक तालिका में पौधों की शिपमेंट से संबंधित विवरण संग्रहित हैं। एक डेटाबेस प्रशासक निम्नलिखित SQL स्टेटमेंट चलाता है: UPDATE plant_shipment SET health_score = health_score + {self.increase} WHERE health_score < {self.threshold}; क्वेरी निष्पादित होने के बाद, 'health_score' कॉलम का कुल योग (योग) ज्ञात कीजिए।"
        self.description_kazakh = f"\'plant_shipment\' кестесінде өсімдіктерді тасымалдау туралы мәліметтер сақталады. Дерекқор әкімшісі келесі SQL операторын орындайды: UPDATE plant_shipment SET health_score = health_score + {self.increase} WHERE health_score < {self.threshold};Сұраныс орындалғаннан кейін `health_score` бағанының жалпы қосындысын (sum) есептеңіз."
        self.description_swahili = f"Jedwali la 'plant_shipment' linahifadhi maelezo kuhusu usafirishaji wa mimea. Msimamizi wa hifadhidata (Database Administrator) anaendesha kauli ifuatayo ya SQL: UPDATE plant_shipment SET health_score = health_score + {self.increase} WHERE health_score < {self.threshold}; Baada ya hoja hiyo kutekelezwa, kokotoa jumla (sum) ya safuwima ya 'health_score'."

class Com032_multi(Com032):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'表 bike_rental 存储有关自行车租赁的数据，包括使用的站点、用户类型以及每次租赁的持续时间（分钟）。执行了以下 SQL 查询：\nSELECT SUM(avg_duration) AS sum_of_group_averages\nFROM (\nSELECT user_type, AVG(duration_min) AS avg_duration \nFROM bike_rental \nGROUP BY station_name \n) group_averages;\n使用表中显示的数据，确定此查询的输出。将答案四舍五入到两位小数。'
        self.description_arabic = f'يخزن الجدول bike_rental بيانات تأجير الدراجات، بما في ذلك المحطة ونوع المستخدم ومدة الإيجار.\nيتم تنفيذ الاستعلام التالي:\nSELECT SUM(avg_duration) AS sum_of_group_averages\nFROM (\nSELECT user_type, AVG(duration_min) AS avg_duration\nFROM bike_rental\nGROUP BY station_name\n) group_averages;\nباستخدام البيانات، حدد الناتج وقرّبه إلى منزلتين عشريتين.'
        self.description_hindi = f'bike_rental तालिका में बाइक किराए पर लेने से संबंधित डेटा संग्रहित है, जिसमें उपयोग किया गया स्टेशन, उपयोगकर्ता का प्रकार और प्रत्येक किराए की अवधि (मिनटों में) शामिल है। निम्नलिखित SQL क्वेरी निष्पादित की जाती है: \nSELECT SUM(avg_duration) AS sum_of_group_averages\nFROM (\nSELECT user_type, AVG(duration_min) AS avg_duration \nFROM bike_rental \nGROUP BY station_name \n) group_averages;\nतालिका में दिखाए गए डेटा का उपयोग करके, इस क्वेरी का आउटपुट ज्ञात कीजिए। उत्तर को दो दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'bike_rental кестесінде велосипедтерді жалға алу туралы деректер сақталады, оның ішінде пайдаланылған станция, пайдаланушы түрі және әрбір жалға алудың минутпен берілген ұзақтығы бар. Келесі SQL сұранысы орындалады: \nSELECT SUM(avg_duration) AS sum_of_group_averages\nFROM (\nSELECT user_type, AVG(duration_min) AS avg_duration \nFROM bike_rental \nGROUP BY station_name \n) group_averages;\nКестеде көрсетілген деректерді пайдалана отырып, осы сұраныстың шығысын анықтаңыз. Жауапты екі ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = f'Jedwali la bike_rental linahifadhi data kuhusu ukodishaji wa baiskeli, ikijumuisha kituo (station) kilichotumika, aina ya mtumiaji, na muda wa kila ukodishaji katika dakika. Hoja (query) ifuatayo ya SQL inatekelezwa: \nSELECT SUM(avg_duration) AS sum_of_group_averages\nFROM (\nSELECT user_type, AVG(duration_min) AS avg_duration \nFROM bike_rental \nGROUP BY station_name \n) group_averages;\nKwa kutumia data inayoonyeshwa kwenye jedwali, tambua towe la hoja hii. Zungusha (round) jibu kwa nafasi mbili za desimali.'

class Com033_multi(Com033):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'doCheck() 函数接受一个整数值作为参数，执行一系列计算并返回一个整数值。该函数如图所示。请说出调用 doCheck({self.number}) 时该函数返回的值。'
        self.description_arabic = f'تأخذ الدالة doCheck() عددًا صحيحًا كمدخل وتُرجع عددًا صحيحًا بعد سلسلة من العمليات.\nما القيمة التي تُرجعها الدالة عند استدعاء doCheck({self.number})؟'
        self.description_hindi = f'doCheck() फ़ंक्शन एक पूर्णांक मान को पैरामीटर के रूप में लेता है, कई गणनाएँ करता है और एक पूर्णांक मान लौटाता है। फ़ंक्शन इस चित्र में दिखाया गया है। doCheck({self.number}) फ़ंक्शन को कॉल करने पर इससे प्राप्त मान बताइए।'
        self.description_kazakh = f'doCheck() функциясы бүтін мәнді параметр ретінде қабылдайды, бірқатар есептеулер жүргізеді және бүтін мәнді қайтарады. Функция осы суретте көрсетілген. doCheck({self.number}) шақырылған кезде функциядан қайтарылатын мәнді көрсетіңіз.'
        self.description_swahili = f'Function ya doCheck() huchukua thamani ya namba nzima (integer) kama kigezo (parameter), hufanya mfululizo wa hesabu na kurudisha thamani ya namba nzima. Function hii inaonyeshwa kwenye picha hii. Eleza thamani inayorudishwa na function hiyo wakati doCheck({self.number}) inapoitwa.'

class Com034_multi(Com034):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'正在开发一个程序。下方给定图像中显示了该程序一部分的算法。该算法将输入三个数值，并将它们分配给标识符 Num1、Num2 和 Num3。如果输入是 {self.input_1}、{self.input_2} 和 {self.input_3}，最终输出将显示什么？将答案四舍五入到两位小数。'
        self.description_arabic = f'توضح الصورة خوارزمية لجزء من برنامج.\nتستقبل الخوارزمية ثلاث قيم Num1 و Num2 و Num3.\nإذا كانت القيم {self.input_1} و {self.input_2} و {self.input_3}، فما الناتج النهائي؟\nقرّب الإجابة إلى منزلتين عشريتين.'
        self.description_hindi = f'एक प्रोग्राम विकसित किया जा रहा है। प्रोग्राम के एक भाग के लिए एल्गोरिदम नीचे दी गई चित्र में दिखाया गया है। यह एल्गोरिदम तीन संख्यात्मक मान इनपुट के रूप में लेगा और उन्हें Num1, Num2 और Num3 पहचानकर्ताओं को असाइन करेगा। यदि इनपुट {self.input_1}, {self.input_2} और {self.input_3} हैं, तो अंतिम आउटपुट क्या प्रदर्शित होगा? उत्तर को दो दशमलव स्थानों तक पूर्णांकित करें।'
        self.description_kazakh = f'Бағдарлама әзірленуде. Бағдарламаның бір бөлігіне арналған алгоритм төменде берілген суретте көрсетілген. Алгоритм үш сандық мәнді енгізіп, оларды Num1, Num2 және Num3 идентификаторларына тағайындайды. Егер енгізілген мәндер {self.input_1}, {self.input_2} және {self.input_3} болса, соңғы шығыс ретінде не көрсетіледі? Жауапты екі ондық таңбаға дейін дөңгелектеңіз.'
        self.description_swahili = f'Programu inatengenezwa. Algoriti ya sehemu ya programu hiyo inaonyeshwa kwenye picha hapa chini. Algoriti hii itaingiza thamani tatu za namba na kuzikabidhi kwenye vitambulisho (identifiers) Num1, Num2, na Num3. Ikiwa maingizo ni {self.input_1}, {self.input_2}, na {self.input_3}, ni nini kitaonyeshwa kama towe la mwisho? Zungusha jibu lako kwa nafasi mbili za desimali.'

class Com035_multi(Com035):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了一个包含以下值的栈。对该栈执行了 pop() 操作。在此操作之后，栈顶的值是多少？'
        self.description_arabic = f'يوضح الشكل مكدسًا (stack) يحتوي على القيم المعطاة.\nبعد تنفيذ عملية pop()، ما القيمة الموجودة أعلى المكدس؟'
        self.description_hindi = f'चित्र में एक स्टैक दिखाया गया है जिसमें निम्नलिखित मान हैं। स्टैक पर pop() ऑपरेशन किया जाता है। इस ऑपरेशन के बाद स्टैक के शीर्ष पर क्या मान होगा?'
        self.description_kazakh = f'Диаграммада келесі мәндерді қамтитын стек көрсетілген. Стекте pop() операциясы орындалады. Осы операциядан кейін стектің жоғарғы жағындағы (top) мән қандай болады?'
        self.description_swahili = f'Mchoro unaonyesha staki (stack) iliyo na thamani zifuatazo. Oparesheni ya pop() inafanywa kwenye staki hiyo. Je, ni thamani gani itakuwa juu ya staki baada ya oparesheni hii kukamilika?'

class Com036_multi(Com036):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了一个使用数组实现的栈，其中 top 存储当前栈顶元素的索引。执行了一次 pop() 操作，然后执行了 push({self.push_1})，接着执行了 push({self.push_2})。在这些操作之后，top 的值是多少？'
        self.description_arabic = f'يوضح الشكل مكدسًا ممثلًا بمصفوفة، حيث يشير top إلى فهرس العنصر العلوي.\nبعد تنفيذ pop() ثم push({self.push_1}) ثم push({self.push_2})، ما قيمة top؟'
        self.description_hindi = f'चित्र में एक स्टैक दिखाया गया है जिसे ऐरे का उपयोग करके कार्यान्वित किया गया है, जहाँ top में वर्तमान शीर्ष तत्व का सूचकांक संग्रहीत है। पहले pop() ऑपरेशन किया जाता है, फिर push({self.push_1}) और उसके बाद push({self.push_2}) किया जाता है। इन ऑपरेशनों के बाद top का मान क्या होगा?'
        self.description_kazakh = f'Диаграммада массивті пайдаланып жүзеге асырылған стек көрсетілген, мұнда top ағымдағы жоғарғы элементтің индексін сақтайды. pop() операциясы орындалады, одан кейін push({self.push_1}) және сосын push({self.push_2}) орындалады. Осы операциялардан кейін top мәні қандай болады?'
        self.description_swahili = f'Mchoro unaonyesha staki (stack) inayotekelezwa kwa kutumia safu (array), ambapo "top" huhifadhi faharasa (index) ya kipengee kilichopo juu kwa sasa. Oparesheni ya pop() inafanywa, ikifuatiwa na push({self.push_1}) na kisha push({self.push_2}). Je, thamani ya "top" itakuwa nini baada ya oparesheni hizi kukamilika?'

class Com037_multi(Com037):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了一个使用数组实现的队列。执行了一次 dequeue() 操作。现在队列前面的值是多少？'
        self.description_arabic = f'يوضح الشكل طابورًا (queue) ممثلًا بمصفوفة.\nبعد تنفيذ عملية dequeue()، ما القيمة الموجودة في مقدمة الطابور؟'
        self.description_hindi = f'चित्र में एक ऐरे का उपयोग करके बनाई गई क्यू दिखाई गई है। एक dequeue() ऑपरेशन किया जाता है। अब क्यू के सबसे आगे कौन सा मान है?'
        self.description_kazakh = f'Диаграммада массивті пайдаланып жүзеге асырылған кезек (queue) көрсетілген. Бір dequeue() операциясы орындалады. Енді кезектің алдыңғы жағында (front) қандай мән тұр?'
        self.description_swahili = f'Mchoro unaonyesha foleni (queue) inayotekelezwa kwa kutumia safu (array). Oparesheni moja ya dequeue() inafanywa. Je, ni thamani gani itakuwa mbele ya foleni (front of the queue) baada ya oparesheni hiyo?'

class Com038_multi(Com038):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了队列 ADT 的一种实现。依次执行了 enqueue({self.enq_1})、dequeue 和 enqueue({self.enq_2}) 操作。在这些操作之后，队列中当前存储的所有值的总和是多少？'
        self.description_arabic = f'يوضح الشكل تنفيذًا لنوع البيانات المجرد للطابور (Queue ADT).\nبعد تنفيذ enqueue({self.enq_1}) ثم dequeue ثم enqueue({self.enq_2})، ما مجموع القيم الموجودة في الطابور؟'
        self.description_hindi = f'आरेख में क्यू ADT का कार्यान्वयन दर्शाया गया है। enqueue({self.enq_1}), dequeue और फिर enqueue({self.enq_2}) ऑपरेशनों इसी क्रम में निष्पादित की जाती हैं। इन ऑपरेशनों के बाद क्यू में संग्रहीत सभी मानों का योग क्या होगा?'
        self.description_kazakh = f'Диаграммада кезек (queue) ADT-сінің (деректердің абстрактілі түрі) жүзеге асырылуы көрсетілген. enqueue({self.enq_1}), dequeue және содан кейін enqueue({self.enq_2}) операциялары осы ретпен орындалады. Осы операциялардан кейін қазіргі уақытта кезекте сақталған барлық мәндердің қосындысы қандай?'
        self.description_swahili = f'Mchoro unaonyesha utekelezaji wa foleni ya ADT (Abstract Data Type). Oparesheni za enqueue({self.enq_1}), dequeue, na kisha enqueue({self.enq_2}) zinafanywa kwa mpangilio huo. Je, jumla ya thamani zote zilizohifadhiwa kwenye foleni baada ya oparesheni hizi ni nini?'

class Com039_multi(Com039):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'将使用链表抽象数据类型 (ADT) 来存储和组织数据。这将使用一维数组和起始指针来实现。请说出紧接在 LinkedList[StartPtr] 之后的节点中存储的值。'
        self.description_arabic = f'يُستخدم نوع البيانات المجرد للقائمة المرتبطة (Linked List ADT) لتنظيم البيانات باستخدام مصفوفة ومؤشر بداية.\nما القيمة الموجودة في العقدة التي تلي LinkedList[StartPtr] مباشرة؟'
        self.description_hindi = f'डेटा को संग्रहित और व्यवस्थित करने के लिए लिंक्ड लिस्ट एब्स्ट्रैक्ट डेटा टाइप (ADT) का उपयोग किया जाना है। इसे एक 1D ऐरे और एक स्टार्ट पॉइंटर के साथ कार्यान्वित किया जाएगा। LinkedList[StartPtr] के ठीक बाद वाले नोड में संग्रहित मान बताइए।'
        self.description_kazakh = f'Деректерді сақтау және ұйымдастыру үшін байланысқан тізім (linked list) деректердің абстрактілі түрі (ADT) қолданылады. Бұл 1D массивімен және бастапқы нұсқағышпен (start pointer) жүзеге асырылады. LinkedList[StartPtr] түйінінен кейін бірден сақталған мәнді көрсетіңіз.'
        self.description_swahili = f'Aina ya data dhahania (ADT) ya orodha iliyounganishwa (linked list) itatumika kuhifadhi na kupanga data. Hii itatekelezwa kwa kutumia safu ya mwelekeo mmoja (1D array) na kielekezi cha kuanza (start pointer). Eleza thamani iliyohifadhiwa kwenye nodi inayofuata mara baada ya ile inayoelekezwa na LinkedList[StartPtr].'

class Com040_multi(Com040):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了一个链表示例。如果包含 {self.delete_value} 的节点从链表中删除，删除后紧挨着它的前一个节点的指针字段中应该存储什么值？'
        self.description_arabic = f'توضح الصورة قائمة مرتبطة.\nإذا تم حذف العقدة التي تحتوي على {self.delete_value}، فما القيمة التي ستُخزن في مؤشر العقدة السابقة لها؟'
        self.description_hindi = f'निम्नलिखित चित्र लिंक्ड लिस्ट का एक उदाहरण दिखा रही है। यदि {self.delete_value} युक्त नोड को लिंक्ड लिस्ट से हटा दिया जाता है, तो हटाने के बाद उससे ठीक पहले वाले नोड के पॉइंटर फ़ील्ड में क्या मान संग्रहीत किया जाना चाहिए?'
        self.description_kazakh = f'Келесі суретте байланысқан тізімнің (linked list) мысалы көрсетілген. Егер құрамында {self.delete_value} бар түйін байланысқан тізімнен жойылса, жоюдан кейін оның алдындағы түйіннің нұсқағыш (pointer) өрісінде қандай мән сақталуы керек?'
        self.description_swahili = f'Picha ifuatayo inaonyesha mfano wa orodha iliyounganishwa (linked list). Ikiwa nodi yenye thamani ya {self.delete_value} itafutwa, ni thamani gani inapaswa kuhifadhiwa kwenye uga wa kielekezi wa nodi iliyokuwa kabla yake mara baada ya mchakato wa kufuta kukamilika?'

class Com041_multi(Com041):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'此图像中显示了一段 Python 代码片段。longest_run("{self.input}") 将输出什么？'
        self.description_arabic = f'توضح الصورة كود Python.\nما القيمة التي تُرجعها الدالة longest_run("{self.input}")؟'
        self.description_hindi = f'इस चित्र में एक Python कोड स्निपेट दिखाया गया है। longest_run("{self.input}") क्या रिटर्न करेगा?'
        self.description_kazakh = f'Бұл суретте Python кодының үзіндісі көрсетілген. longest_run("{self.input}") нені қайтарады?'
        self.description_swahili = f'Kipande cha msimbo wa Python kinaonyeshwa kwenye picha hii. Je, function ya longest_run("{self.input}") itarudisha nini?'

class Com042_multi(Com042):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'请观察下图。设 inp 为一个整数。如果进行了函数调用 func1(func2(inp))，其中 inp 为 {self.input}，将打印出什么值？'
        self.description_arabic = f'لاحظ الكود في الصورة.\nإذا كان inp = {self.input}، فما القيمة المطبوعة عند استدعاء func1(func2(inp))؟'
        self.description_hindi = f'नीचे दी गई चित्र को देखें। मान लीजिए inp एक पूर्णांक है। यदि फ़ंक्शन call func1(func2(inp)) बनाया जाता है, जहाँ inp का मान {self.input} है, तो क्या मान प्रिंट होगा?'
        self.description_kazakh = f'Төмендегі суретті бақылаңыз. inp бүтін сан болсын. Егер inp {self.input} болатын func1(func2(inp)) функциясын шақыру орындалса, қандай мән басып шығарылады?'
        self.description_swahili = f'Chunguza picha hii hapa chini. Hebu tuchukulie "inp" ni namba nzima (integer). Ikiwa function ya func1(func2(inp)) itaitwa ambapo inp ni {self.input}, ni thamani gani itachapishwa kama matokeo?'

class Com043_multi(Com043):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'下图提供了一段伪代码。最后输出的值是什么？'
        self.description_arabic = f'تعرض الصورة كودًا زائفًا.\nما القيمة الناتجة في النهاية؟'
        self.description_hindi = f'नीचे दी गई चित्र में एक स्यूडोकोड (pseudocode) दिया गया है। अंत में क्या मान आउटपुट होगा?'
        self.description_kazakh = f'Төмендегі суретте псевдокод берілген. Соңында қандай мән шығарылады?'
        self.description_swahili = f'Pseudocode (msimbo bandia) imetolewa kwenye picha hapa chini. Je, ni thamani gani itatolewa kama towe (output) mwishoni?'

class Com044_multi(Com044):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定图像中指示的卡诺图单元格可以获得什么布尔表达式？使用以下编码规则构成答案：A = 1, B = 2, C = 3, D = 4, Ā = 5, B̄ = 6, C̄ = 7, D̄ = 8。按照 A、B、C、D 的顺序将数字拼接起来，形成最终的数字答案。'
        self.description_arabic = f'ما التعبير المنطقي المقابل لخلية خريطة كارنوف (Karnaugh) المحددة؟\nاستخدم الترميز: A=1، B=2، C=3، D=4، Ā=5، B̄=6، C̄=7، D̄=8.\nاكتب الإجابة بترتيب A ثم B ثم C ثم D.'
        self.description_hindi = f'दी गई चित्र में दर्शाए गए कार्नघ मानचित्र सेल (Karnaugh map cell) के लिए बूलियन व्यंजक (Boolean expression) क्या है? निम्नलिखित एन्कोडिंग नियम का उपयोग करके उत्तर लिखें: A = 1, B = 2, C = 3, D = 4, Ā = 5, B̄ = 6, C̄ = 7, D̄ = 8। अंतिम संख्यात्मक उत्तर बनाने के लिए अंकों को A, B, C, D के क्रम में संयोजित करें।'
        self.description_kazakh = f'Берілген суретте көрсетілген Карно картасының (Karnaugh map) ұяшығы үшін қандай логикалық өрнек алуға болады? Жауапты келесі кодтау ережесін пайдаланып құрастырыңыз: A = 1, B = 2, C = 3, D = 4, Ā = 5, B̄ = 6, C̄ = 7, D̄ = 8. Соңғы сандық жауапты құру үшін сандарды A, B, C, D ретімен біріктіріңіз.'
        self.description_swahili = f'Ni usemi (expression) gani wa Boolean unaoweza kupatikana kwa seli ya ramani ya Karnaugh (Karnaugh Map) inayoonyeshwa kwenye picha? Unda jibu lako kwa kutumia kanuni ifuatayo ya usimbaji (encoding): A=1, B=2, C=3, D=4, Ā=5, B̄=6, C̄=7, D̄=8. Unganisha tarakimu hizo kwa mpangilio wa A, B, C, D ili kupata jibu la mwisho la nambari.'

class Com045_multi(Com045):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定一个具有每个节点的启发式估计值的有向加权图，使用 A* 搜索算法找到从节点 {self.start_node} 到节点 {self.goal_node} 的最短/最小成本。图下方的表格提供了节点到目标节点的估计距离。'
        self.description_arabic = f'بناءً على رسم بياني موجه وموزون مع قيم إرشادية، استخدم خوارزمية A* لإيجاد أقل تكلفة من العقدة {self.start_node} إلى العقدة {self.goal_node}.'
        self.description_hindi = f'प्रत्येक नोड के लिए अनुमानित मार्ग के साथ दिए गए निर्देशित भारित ग्राफ में, नोड {self.start_node} से नोड {self.goal_node} तक की सबसे छोटी/न्यूनतम लागत ज्ञात करने के लिए A* खोज एल्गोरिदम का उपयोग करें। ग्राफ के नीचे दी गई तालिका नोड्स से लक्ष्य नोड तक की अनुमानित दूरी दर्शाती है।'
        self.description_kazakh = f'Әрбір түйін үшін эвристикалық бағалаулары бар бағытталған өлшенген граф (directed weighted graph) берілген болса, {self.start_node} түйінінен {self.goal_node} түйініне дейінгі ең қысқа/минималды құнды табу үшін A* іздеу алгоритмін пайдаланыңыз. Графтың астындағы кестеде түйіндерден мақсатты түйінге дейінгі болжамды қашықтық берілген.'
        self.description_swahili = f'Kwa kuzingatia grafu yenye mwelekeo na uzito (directed weighted graph) pamoja na makadirio ya kiheuristiki ya kila nodi, tumia algoriti ya utafutaji ya A* kupata gharama ndogo zaidi kutoka nodi {self.start_node} hadi nodi {self.goal_node}. Jedwali lililopo chini ya grafu linatoa makadirio ya umbali (heuristic) kutoka kwenye nodi husika hadi nodi lengwa.'

class Com046_multi(Com046):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'给定一个无向加权图，使用 Dijkstra 算法找到从节点 {self.start} 到节点 {self.goal} 的最短长度。'
        self.description_arabic = f'بناءً على رسم بياني غير موجه وموزون، استخدم خوارزمية ديكسترا لإيجاد أقصر مسار من {self.start} إلى {self.goal}.'
        self.description_hindi = f'एक अनडायरेक्टेड वेटेड ग्राफ (undirected weighted graph) दिया गया है, डाइक्स्ट्रा एल्गोरिदम (Dijkstra algorithm) का उपयोग करके नोड {self.start} से नोड {self.goal} तक की सबसे छोटी लंबाई ज्ञात कीजिए।'
        self.description_kazakh = f'Бағытталмаған өлшенген граф (undirected weighted graph) берілген болса, {self.start} түйінінен {self.goal} түйініне дейінгі ең қысқа ұзындықты табу үшін Дейкстра алгоритмін (Dijkstra algorithm) пайдаланыңыз.'
        self.description_swahili = f'Kwa kuzingatia grafu yenye uzito na isiyo na mwelekeo (undirected weighted graph), tumia algoriti ya Dijkstra kupata umbali mfupi zaidi kutoka nodi {self.start} hadi nodi {self.goal}.'

class Com047_multi(Com047):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'桑迪普编写了一个执行加法和减法的算法。该算法将使用一个初始已填充的栈，并接受用户的输入。算法采取的操作取决于用户输入的值。这些操作在给定图形中列出。如果用户的输入是 "{self.input}"，输出将是什么？'
        self.description_arabic = f'يكتب سونديب خوارزمية لتنفيذ عمليتي الجمع والطرح باستخدام مكدس مبدئي.\nيعتمد التنفيذ على إدخال المستخدم.\nإذا كان الإدخال "{self.input}"، فما الناتج؟'
        self.description_hindi = f'संदीप (Sundip) जोड़ और घटाव करने के लिए एक एल्गोरिदम लिखता है। यह एल्गोरिदम प्रारंभ में भरी हुई स्टैक का उपयोग करेगा और उपयोगकर्ता से इनपुट लेगा। एल्गोरिदम की क्रिया उपयोगकर्ता द्वारा इनपुट किए गए मान पर निर्भर करती है। ये क्रियाएँ दिए गए चित्र में सूचीबद्ध हैं। यदि उपयोगकर्ता द्वारा इनपुट "{self.input}" है, तो आउटपुट क्या होगा?'
        self.description_kazakh = f'Сундип қосу мен азайтуды орындау үшін алгоритм жазады. Алгоритм бастапқыда толтырылған стекті пайдаланады және пайдаланушыдан кірісті қабылдайды. Алгоритмнің орындайтын әрекеті пайдаланушы енгізген мәнге байланысты. Бұл әрекеттер берілген суретте тізімделген. Егер пайдаланушыдан енгізілген мән "{self.input}" болса, шығыс қандай болады?'
        self.description_swahili = f'Sundip anaandika algoriti ya kufanya operesheni za kujumlisha na kutoa. Algoriti hii inatumia staki (stack) iliyojazwa data awali na itapokea ingizo kutoka kwa mtumiaji. Hatua inayochukuliwa na algoriti inategemea thamani iliyoingizwa na mtumiaji kama inavyoonyeshwa kwenye kielelezo. Ikiwa ingizo la mtumiaji ni "{self.input}", je, towe (output) litakuwa nini?'

class Com048_multi(Com048):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个机器人从网格上的坐标 ({self.x}, {self.y}) 开始，必须到达 (0, 0)。它只能向左（x 减 1）或向下（y 减 1）移动。使用这段递归伪代码，一共有多少条不同的路径？'
        self.description_arabic = f'يبدأ روبوت عند الإحداثي ({self.x}, {self.y}) على شبكة، ويجب أن يصل إلى (0, 0). يمكنه التحرك فقط إلى اليسار (إنقاص x بمقدار 1) أو إلى الأسفل (إنقاص y بمقدار 1). باستخدام هذا الكود الزائف العودي (recursive)، كم عدد المسارات المختلفة الممكنة؟'
        self.description_hindi = f'एक रोबोट ग्रिड पर निर्देशांक ({self.x}, {self.y}) से चलना शुरू करता है और उसे (0, 0) तक पहुंचना है। यह केवल बाईं ओर (x को 1 से घटाकर) या नीचे की ओर (y को 1 से घटाकर) चल सकता है। इस पुनरावर्ती स्यूडोकोड (recursive pseudocode) का उपयोग करके, कितने अलग-अलग पथ संभव हैं?'
        self.description_kazakh = f'Робот тордағы ({self.x}, {self.y}) координатасынан бастап (0, 0) нүктесіне жетуі керек. Ол тек солға (x мәнін 1-ге азайту) немесе төменге (y мәнін 1-ге азайту) қозғала алады. Осы рекурсивті псевдокодты пайдалана отырып, қанша түрлі жол бар екенін табыңыз?'
        self.description_swahili = f'Roboti inaanza kwenye kiratibu ({self.x}, {self.y}) katika gridi na lazima ifike (0, 0). Inaweza kusonga upande wa kushoto pekee (kupunguza x kwa 1) au chini (kupunguza y kwa 1). Kwa kutumia pseudocode hii inayojirudia (recursive), kuna njia ngapi tofauti za kufika lengoni?'

class Com049_multi(Com049):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'二叉搜索树 (BST) 的构造如下图所示。在后序遍历期间访问的第 4 个元素是什么？'
        self.description_arabic = f'تم بناء شجرة بحث ثنائية (BST) كما هو موضح في الشكل أدناه. ما هو العنصر الرابع الذي تتم زيارته أثناء الاجتياز اللاحق (postorder traversal)؟'
        self.description_hindi = f'नीचे दिए गए चित्र के अनुसार एक बाइनरी सर्च ट्री (BST) बनाया गया है। पोस्टऑर्डर ट्रैवर्सल (postorder traversal) के दौरान चौथा तत्व कौन सा होगा?'
        self.description_kazakh = f'Екілік іздеу ағашы (Binary Search Tree - BST) төмендегі суреттегідей құрастырылған. Postorder (кері реттік) өту кезінде барған 4-ші элемент қандай?'
        self.description_swahili = f'Mti wa Kutafuta wa Binari (Binary Search Tree - BST) umeundwa kama inavyoonyeshwa kwenye picha. Je, ni kipengee (element) gani cha nne kitakachotembelewa wakati wa upitaji wa baada ya mpangilio (postorder traversal)?'

class Com050_multi(Com050):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'下图显示了一个排序好的数组。我们要搜索的值是 {self.target}。使用二分查找，需要多少次拆分（迭代）才能找到目标？这里的拆分次数定义为找到目标所需的检查次数。'
        self.description_arabic = f'تُظهر الصورة مصفوفة مرتبة. القيمة المطلوب البحث عنها هي {self.target}. باستخدام البحث الثنائي (binary search)، كم عدد التكرارات اللازمة للعثور على الهدف؟ (يُقصد بعدد التكرارات عدد عمليات التحقق).'
        self.description_hindi = f'नीचे दिए गए चित्र में एक क्रमबद्ध ऐरे दिखाया गया है। जिस मान को हम खोजना चाहते हैं वह {self.target} है। बाइनरी सर्च का उपयोग करके, लक्ष्य को खोजने के लिए कितने स्प्लिट (इटरेशन) की आवश्यकता होगी? यहां स्प्लिट की संख्या को लक्ष्य को खोजने के लिए किए जाने वाले चेक की संख्या के रूप में परिभाषित किया गया है।'
        self.description_kazakh = f'Төмендегі суретте сұрыпталған массив көрсетілген. Біз іздегіміз келетін мән - {self.target}. Екілік іздеудің көмегімен мақсатты мәнді табу үшін қанша бөлу (итерация) қажет? Мұндағы бөлулер саны мақсатты мәнді табу үшін жасалған тексерулер ретінде анықталады.'
        self.description_swahili = f'Safu iliyopangwa (sorted array) inaonyeshwa kwenye kielelezo hapa chini. Thamani tunayotaka kuitafuta ni {self.target}. Kwa kutumia utafutaji wa binari (binary search), ni mizunguko (iterations) mingapi itahitajika ili kupata thamani hiyo? Idadi ya mizunguko hapa inafafanuliwa kama idadi ya ukaguzi (checks) uliofanywa hadi kufikia lengo.'

class Com051_multi(Com051):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'下图显示了两个数组。第一个数组是初始数组。第二个数组是对第一个数组进行 X 趟插入排序后的结果。求 X。'
        self.description_arabic = f'تُظهر الصورة مصفوفتين: الأولى هي المصفوفة الأصلية، والثانية هي ناتج تطبيق خوارزمية فرز الإدراج (insertion sort) على الأولى بعد X تمريرات. أوجد قيمة X.'
        self.description_hindi = f'नीचे दिए गए चित्र में दो ऐरे दिखाए गए हैं। पहला ऐरे प्रारंभिक एरे है। दूसरा ऐरे पहले ऐरे पर X पास के लिए इंसर्शन सॉर्ट चलाने का परिणाम है। X ज्ञात कीजिए।'
        self.description_kazakh = f'Төмендегі суретте екі массив көрсетілген. Бірінші массив - бастапқы массив. Екінші массив - бірінші массивте X өту (pass) үшін кірістіру арқылы сұрыптауды (insertion sort) орындау нәтижесі. X мәнін табыңыз.'
        self.description_swahili = f'Safu (array) mbili zinaonyeshwa kwenye kielelezo hapa chini. Safu ya kwanza ni ile ya awali, na safu ya pili ni matokeo ya kufanya upangaji wa kuingiza (insertion sort) kwenye safu hiyo kwa "mapito" (passes) X. Tafuta thamani ya X.'

class Com052_multi(Com052):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如果 x 是 {self.x}，给定程序的输出是什么？'
        self.description_arabic = f'ما ناتج البرنامج المعطى إذا كانت قيمة x = {self.x}؟'
        self.description_hindi = f'यदि x का मान {self.x} है, तो दिए गए प्रोग्राम का आउटपुट क्या होगा?'
        self.description_kazakh = f'Егер x {self.x} болса, берілген бағдарламаның шығысы қандай болады?'
        self.description_swahili = f'Je, towe (output) la programu iliyotolewa ni nini, ikiwa x ni {self.x}?'

