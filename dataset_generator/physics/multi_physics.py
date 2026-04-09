from templates_001_050 import *
from templates_051_100 import *
from templates_101_150 import *
from templates_151_200 import *

class Phy001_multi(Phy001):
    def __init__(self):
        super().__init__()
        self.description_chinese = '移动直尺测量直线的长度，精确到最近的厘米。该直线的长度约为 (_) 厘米。'
        self.description_arabic = 'حرّك المسطرة لقياس طول الخط لأقرب سنتيمتر. يبلغ طول الخط تقريبًا (_) سنتيمتر.'
        self.description_hindi = 'रेखा की लंबाई को निकटतम सेंटीमीटर तक मापने के लिए रूलर को हिलाएँ। रेखा लगभग (_) सेंटीमीटर लंबी है।'
        self.description_kazakh = 'Сызғышты жылжытып, сызықтың ұзындығын ең жақын сантиметрге дейін өлшеңіз. Сызықтың ұзындығы шамамен (_) сантиметр.'
        self.description_swahili = 'Sogeza rula ili kupima urefu wa mstari hadi sentimita ya karibu zaidi. Mstari huo una urefu wa takriban sentimita (_).'

class Phy002_multi(Phy002):
    def __init__(self):
        super().__init__()
        self.description_chinese = '量筒最初装有左图所示的水量。当将一块石头放入量筒后，水位上升如右图所示。石头的体积为 ... ml'
        self.description_arabic = 'تحتوي أسطوانة قياس في البداية على كمية الماء الموضحة في الصورة اليسرى. عند وضع قطعة حجر في الأسطوانة، يرتفع مستوى الماء كما هو موضح في الصورة اليمنى. حجم الحجر هو ... ml'
        self.description_hindi = 'एक मापने वाले सिलेंडर में शुरुआत में उतना पानी है जितना बाईं ओर की चित्र में दिखाया गया है। जब सिलेंडर में एक पत्थर का टुकड़ा रखा जाता है, तो पानी का स्तर दाईं ओर की चित्र में दिखाए अनुसार बढ़ जाता है। पत्थर का आयतन ... ml है।'
        self.description_kazakh = 'Өлшеуіш цилиндрде бастапқыда сол жақтағы суретте көрсетілгендей су мөлшері бар. Цилиндрге тас кесегін салған кезде, оң жақтағы суретте көрсетілгендей су деңгейі көтеріледі. Тастың көлемі ... мл'
        self.description_swahili = 'Silinda ya kupimia awali ina kiasi cha maji kinachoonyeshwa kwenye picha ya kushoto. Kipande cha jiwe kinapowekwa ndani ya silinda, kiwango cha maji hupanda kama inavyoonyeshwa kwenye picha ya kulia. Ujazo wa jiwe ni ... ml'

class Phy003_multi(Phy003):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个盒子受到两个相互垂直的力。合力的大小为 (_) N'
        self.description_arabic = 'يتعرض صندوق لقوتين متعامدتين كما هو موضح في الشكل. مقدار القوة المحصلة هو (_) N.'
        self.description_hindi = 'चित्र में दर्शाए अनुसार एक बॉक्स पर दो लंबवत बल लगते हैं। परिणामी बल का परिमाण (_) N है।'
        self.description_kazakh = 'Диаграммада көрсетілгендей, қорапқа екі перпендикуляр күш әсер етеді. Қорытқы күштің модулі (_) N'
        self.description_swahili = 'Boksi linapata kani mbili zilizo wima (perpendicular) kama inavyoonyeshwa kwenye mchoro. Ukubwa wa kani tokeo (resultant force) ni (_) N'

class Phy004_multi(Phy004):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一只猫在 {self.time} 秒内从A点移动到B点以获取食物。假设它以匀速移动，猫的速度为 ... m/s'
        self.description_arabic = f'تتحرك قطة من النقطة A إلى النقطة B للوصول إلى طعامها خلال {self.time} ثانية. بافتراض أنها تتحرك بسرعة ثابتة، فإن سرعة القطة هي ... m/s.'
        self.description_hindi = f'एक बिल्ली {self.time} सेकंड में बिंदु A से बिंदु B तक चलकर अपना भोजन प्राप्त करती है। यह मानते हुए कि वह स्थिर वेग से चलती है, बिल्ली की गति ... m/s है।'
        self.description_kazakh = f'Мысық тамағына жету үшін А нүктесінен В нүктесіне {self.time} секунд ішінде барады. Ол тұрақты жылдамдықпен қозғалады деп есептесек, мысықтың жылдамдығы ... m/s'
        self.description_swahili = f'Paka anasogea kutoka nukta A hadi nukta B ili kufikia mlo wake ndani ya sekunde {self.time}. Akichukuliwa kuwa anasogea kwa velositi isiyobadilika (constant velocity), mwendo kasi wa paka huyo ni ... m/s'

class Phy005_multi(Phy005):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'安迪沿着图示路径行走。第一、第二和第三段的路径分别耗时 {self.first_time}、{self.second_time} 和 {self.third_time} 秒。他的平均速率为 ... m/s'
        self.description_arabic = f'يمشي آندي على المسار الموضح في الشكل. يُقطع المسار الأول والثاني والثالث في {self.first_time} و {self.second_time} و {self.third_time} ثانية على التوالي. متوسط سرعته هو ... m/s.'
        self.description_hindi = f' एंडी (Andy) चित्र में दर्शाए गए पथ पर चलता है। पहले, दूसरे और तीसरे पथ को तय करने में क्रमशः {self.first_time}, {self.second_time} और {self.third_time} सेकंड लगते हैं। उसकी औसत गति ... m/s है।'
        self.description_kazakh = f'Энди диаграммада көрсетілген жолмен жүреді. Бірінші, екінші және үшінші жолдар сәйкесінше {self.first_time}, {self.second_time} және {self.third_time} секундта жүріп өтілді. Оның орташа жылдамдығы ... m/s'
        self.description_swahili = f'Andy anatembea kando ya njia inayoonyeshwa kwenye mchoro. Njia ya kwanza, ya pili, na ya tatu zinasafiriwa ndani ya sekunde {self.first_time}, {self.second_time}, na {self.third_time}, mtawalia. Mwendo kasi wastani wake ni ... m/s'

class Phy006_multi(Phy006):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个物体以匀速运动。下方的距离-时间图像表示了它的运动。根据该图像，物体的速度为 (_) m/s'
        self.description_arabic = f'يتحرك جسم بسرعة ثابتة. يمثل الرسم البياني للمسافة والزمن أدناه حركته. بناءً على الرسم البياني، فإن سرعة الجسم هي (_) m/s.'
        self.description_hindi = f'एक वस्तु स्थिर वेग से गति कर रही है। नीचे दिया गया दूरी-समय ग्राफ इसकी गति को दर्शाता है। ग्राफ के अनुसार, वस्तु का वेग (_) m/s है।'
        self.description_kazakh = f'Дене тұрақты жылдамдықпен қозғалады. Төмендегі қашықтық-уақыт графигі оның қозғалысын көрсетеді. Графикке сәйкес, дененің жылдамдығы (_) m/s'
        self.description_swahili = f'Gimba linasogea kwa velositi isiyobadilika (constant velocity). Grafu ya umbali-muda hapa chini inawakilisha mwendo wake. Kulingana na grafu hiyo, velositi ya gimba hilo ni (_) m/s'

class Phy007_multi(Phy007):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个物体以匀速运动。下方的距离-时间图像表示了它的运动。根据该图像，物体在 t={self.t1} 到 t={self.t2} 之间的位移为 (_) m'
        self.description_arabic = f'يتحرك جسم بسرعة ثابتة. يمثل الرسم البياني للمسافة والزمن أدناه حركته. بناءً على الرسم البياني، فإن إزاحة الجسم بين t={self.t1} و t={self.t2} هي (_) m.'
        self.description_hindi = f'एक वस्तु स्थिर वेग से गति कर रही है। नीचे दिया गया दूरी-समय ग्राफ इसकी गति को दर्शाता है। ग्राफ के अनुसार, t={self.t1} और t={self.t2} के बीच वस्तु का विस्थापन (_) m है।'
        self.description_kazakh = f'Дене тұрақты жылдамдықпен қозғалады. Төмендегі қашықтық-уақыт графигі оның қозғалысын көрсетеді. Графикке сәйкес, дененің t={self.t1} және t={self.t2} аралығындағы орын ауыстыруы (_) m'
        self.description_swahili = f'Gimba linasogea kwa velositi isiyobadilika (constant velocity). Grafu ya umbali-muda hapa chini inawakilisha mwendo wake. Kulingana na grafu hiyo, mhamo (displacement) wa gimba kati ya t={self.t1} na t={self.t2} ni (_) m'

class Phy008_multi(Phy008):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个物体以匀加速运动。下方的速度-时间图像表示了它的运动。根据该图像，物体在 t={self.t} 时的速度为 (_) m/s'
        self.description_arabic = f'يتحرك جسم بتسارع ثابت. يمثل الرسم البياني للسرعة والزمن أدناه حركته. بناءً على الرسم البياني، فإن سرعة الجسم عند t={self.t} هي (_) m/s.'
        self.description_hindi = f'एक वस्तु स्थिर त्वरण से गति कर रही है। नीचे दिया गया वेग-समय ग्राफ इसकी गति को दर्शाता है। ग्राफ के अनुसार, समय t={self.t} पर वस्तु का वेग (_) m/s है।'
        self.description_kazakh = f'Дене тұрақты үдеумен қозғалады. Төмендегі жылдамдық-уақыт графигі оның қозғалысын көрсетеді. Графикке сәйкес, t={self.t} уақытындағы дененің жылдамдығы (_) m/s'
        self.description_swahili = f'Gimba linasogea kwa mchapuko isiyobadilika (constant acceleration). Grafu ya velositi-muda hapa chini inawakilisha mwendo wake. Kulingana na grafu hiyo, velositi ya gimba wakati t={self.t} ni (_) m/s'

class Phy009_multi(Phy009):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个物体以匀加速运动。下方的速度-时间图像表示了它的运动。根据该图像，物体在 t={self.t1} 到 t={self.t2} 之间的位移为 (_) m'
        self.description_arabic = f'يتحرك جسم بتسارع ثابت. يمثل الرسم البياني للسرعة والزمن أدناه حركته. بناءً على الرسم البياني، فإن إزاحة الجسم بين t={self.t1} و t={self.t2} هي (_) m.'
        self.description_hindi = f'एक वस्तु स्थिर त्वरण से गति कर रही है। नीचे दिया गया वेग-समय ग्राफ इसकी गति को दर्शाता है। ग्राफ के अनुसार, t={self.t1} और t={self.t2} के बीच वस्तु का विस्थापन (_) m है।'
        self.description_kazakh = f'Дене тұрақты үдеумен қозғалады. Төмендегі жылдамдық-уақыт графигі оның қозғалысын көрсетеді. Графикке сәйкес, дененің t={self.t1} және t={self.t2} аралығындағы орын ауыстыруы (_) m'
        self.description_swahili = f'Gimba linasogea kwa mchapuko isiyobadilika (constant acceleration). Grafu ya velositi-muda hapa chini inawakilisha mwendo wake. Kulingana na grafu hiyo, mhamo (displacement) wa gimba kati ya t={self.t1} na t={self.t2} ni (_) m'

class Phy010_multi(Phy010):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'质量m为 {self.m} kg 的实心圆柱体尺寸如图所示。该圆柱体的密度为 ... kg/m^3 (取 π=3.14)'
        self.description_arabic = f'أسطوانة صلبة كتلتها m={self.m} kg وأبعادها موضحة في الصورة. كثافة الأسطوانة هي ... kg/m^3 (استخدم π=3.14).'
        self.description_hindi = f'm = {self.m} kg द्रव्यमान वाले एक ठोस बेलन के आयाम चित्र में दिखाए गए हैं। बेलन का घनत्व ... kg/m^3 है (π = 3.14 का प्रयोग करें)।'
        self.description_kazakh = f'Массасы m={self.m} kg тұтас цилиндрдің өлшемдері суретте берілген. Цилиндрдің тығыздығы ... kg/m^3 (π=3.14 мәнін қолданыңыз)'
        self.description_swahili = f'Silinda yabisi yenye masi m={self.m} kg ina vipimo vilivyotolewa kwenye picha. Msongamano wa silinda hiyo ni ... kg/m^3 (tumia π=3.14)'

class Phy011_multi(Phy011):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，一个 {self.mass} kg 的盒子正被沿水平轴的三个力拉动。盒子的加速度为 ... m/s² (正值表示沿正水平轴方向加速，负值表示相反方向)。'
        self.description_arabic = f'يتم سحب صندوق كتلته {self.mass} kg بواسطة ثلاث قوى على طول المحور الأفقي كما هو موضح في الشكل. يتسارع الصندوق بمقدار ... m/s² (تشير القيمة الموجبة إلى التسارع نحو الاتجاه الموجب، والسالبة إلى الاتجاه المعاكس).'
        self.description_hindi = f'चित्र में दर्शाए अनुसार, {self.mass} kg के एक बॉक्स को क्षैतिज अक्ष के अनुदिश तीन बलों द्वारा खींचा जा रहा है। बॉक्स ... m/s² के त्वरण से बढ़ रहा है (धनात्मक मान धनात्मक क्षैतिज अक्ष की ओर त्वरण दर्शाता है, और ऋणात्मक मान विपरीत दिशा में त्वरण दर्शाता है)।'
        self.description_kazakh = f'Диаграммада көрсетілгендей, {self.mass} kg қорапты горизонтал ось бойымен үш күш тартып тұр. Қорап ... m/s² үдеумен қозғалады (оң мән оң горизонтал ось бағытындағы үдеуді, ал теріс мән қарама-қарсы бағытты білдіреді).'
        self.description_swahili = f'Boksi lenye masi ya {self.mass} kg linavutwa na kani tatu kando ya mhimili wa mlalo, kama inavyoonyeshwa kwenye mchoro. Boksi hilo lina mchapuko wa ... m/s^2 (thamani chanya inaonyesha mchapuko kuelekea mhimili mlalo chanya, na thamani hasi inaonyesha upande wa kinyume).'

class Phy012_multi(Phy012):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一根弹簧悬挂在天花板上，最初处于原长状态。然后将一个盒子挂在弹簧上，使其如图所示伸长。弹簧常数 (k) 为 ... N/m (假设 g = 10 m/s²)'
        self.description_arabic = f'يُعلّق نابض من السقف ويكون في البداية غير مشدود. ثم يُربط به صندوق، مما يؤدي إلى تمدده كما هو موضح في الصورة. ثابت النابض (k) هو ... N/m (افترض أن g = 10 m/s²).'
        self.description_hindi = f'एक स्प्रिंग छत से लटकी हुई है और प्रारंभ में शिथिल अवस्था में है। फिर स्प्रिंग से एक बॉक्स जोड़ा जाता है, जिससे स्प्रिंग चित्र में दिखाए अनुसार खिंच जाती है। स्प्रिंग स्थिरांक (k) ... N/m है (g = 10 m/s² मान लें)।'
        self.description_kazakh = f'Серіппе төбеге ілінген және бастапқыда босаңсыған күйде. Одан кейін серіппеге қорап бекітіліп, ол суретте көрсетілгендей созылады. Серіппенің қатаңдығы (k) ... N/m (g = 10 m/s² деп есептеңіз)'
        self.description_swahili = f'Springi imetundikwa kwenye dari na awali iko katika hali yake ya asili. Boksi kisha linafungwa kwenye springi hiyo, na kuisababisha kurefuka kama inavyoonyeshwa kwenye picha. Kigezo cha springi (k) ni ... N/m (chukulia g = 10 m/s^2)'

class Phy013_multi(Phy013):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"如图所示，在施加力的情况下，弹簧的载荷-伸长量关系。从图中我们可以得出结论，在 F = ... N 时，弹簧不再遵循胡克定律。"
        self.description_arabic = f"يوضح الرسم البياني العلاقة بين القوة والاستطالة لنابض. من الرسم البياني، يمكن استنتاج أنه عند F = ... N لا يعود النابض يحقق قانون هوك."
        self.description_hindi = f"ग्राफ में लगाए गए बल के तहत स्प्रिंग के भार-विस्तार संबंध को दर्शाया गया है। ग्राफ से हम यह निष्कर्ष निकाल सकते हैं कि F = ... N पर, स्प्रिंग हुक (Hooke) के नियम का पालन नहीं करती है।"
        self.description_kazakh = f"График түсірілген күш әсерінен серіппенің жүктеме мен ұзару байланысын көрсетеді. Графиктен F = ... N кезінде серіппе Гук заңына бағынбайтынын қорытындылауға болады."
        self.description_swahili = f"Grafu inaonyesha uhusiano kati ya mzigo na urefuko wa springi chini ya kani inayotumika. Kutoka kwenye grafu hiyo, tunaweza kuhitimisha kuwa kuanzia F = ... N, springi haitii tena sheria ya Hooke."

class Phy014_multi(Phy014):
    def __init__(self):
        super().__init__()
        self.description_chinese = f"一块质量为 {self.plank_mass} kg 的木板一端铰接并保持静止。木板的另一端连接着一个盒子。在盒子和支点之间，还有一根绳子系在木板上。支点、木板质心、绳子和盒子之间的距离如图所示。求绳子的张力（假设 g = 10 m/s²）！"
        self.description_arabic = f"لوح خشبي كتلته {self.plank_mass} kg مثبت من أحد طرفيه ويرتكز عليه. يُربط صندوق بالطرف الآخر، كما يُربط حبل باللوح بين الصندوق ونقطة الارتكاز. المسافات موضحة في الشكل. أوجد شد الحبل (افترض أن g = 10 m/s²)."
        self.description_hindi = f"{self.plank_mass} kg द्रव्यमान का एक लकड़ी का तख्ता एक सिरे पर धुरी से टिका हुआ है और स्थिर है। तख्ते के दूसरे सिरे पर एक बॉक्स जुड़ा हुआ है। बॉक्स और धुरी के बीच तख्ते से एक रस्सी भी बंधी हुई है। धुरी, तख्ते के द्रव्यमान केंद्र, रस्सी और बॉक्स के बीच की दूरियाँ चित्र में दर्शाई गई हैं। रस्सी में तनाव ज्ञात कीजिए (g = 10 m/s² मान लीजिए)!"
        self.description_kazakh = f"Массасы {self.plank_mass} kg ағаш тақтай бір шетінен топсаға бекітіліп, қозғалыссыз ұсталып тұр. Тақтайдың екінші шетіне қорап бекітілген. Қорап пен топсаның арасында тақтайға арқан да байланған. Топса, тақтайдың массалар центрі, арқан және қорап арасындағы қашықтықтар диаграммада көрсетілген. Арқанның керілу күшін анықтаңыз (g = 10 m/s² деп есептеңіз)!"
        self.description_swahili = f"Ubao wa mbao wenye masi ya {self.plank_mass} kg umeshikiliwa kwenye egemeo (pivot) katika ncha moja na kuwekwa tuli. Boksi limefungwa kwenye ncha nyingine ya ubao. Kati ya boksi na egemeo, kamba pia imefungwa kwenye ubao. Umbali kati ya egemeo, kitovu cha masi cha ubao, kamba, na boksi umeonyeshwa kwenye mchoro. Bainisha mvutano (tension) kwenye kamba (chukulia g = 10 m/s²)."

class Phy015_multi(Phy015):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'两辆小车位于无摩擦轨道上。如图所示，小车A向最初静止的小车B运动。碰撞后，两辆小车粘在一起共同运动。求碰撞后它们的共同速度！'
        self.description_arabic = f'توجد عربتان على مسار عديم الاحتكاك. تتحرك العربة A نحو العربة B الساكنة كما هو موضح في الصورة. بعد التصادم، تلتصق العربتان وتتحركان كجسم واحد. أوجد سرعتهما المشتركة بعد التصادم.'
        self.description_hindi = f'दो गाड़ियाँ घर्षण रहित पटरी पर चल रही हैं। गाड़ी A, गाड़ी B की ओर बढ़ती है, जो शुरू में स्थिर है, जैसा कि चित्र में दिखाया गया है।टक्कर के बाद, गाड़ियाँ आपस में चिपक जाती हैं और एक साथ चलने लगती हैं। टक्कर के बाद उनका उभयनिष्ठ वेग ज्ञात कीजिए!'
        self.description_kazakh = f'Үйкеліссіз жолда екі арба орналасқан. Суретте көрсетілгендей, А арбасы бастапқыда тыныштықта тұрған В арбасына қарай қозғалады. Соқтығысқаннан кейін арбалар бір-біріне жабысып, бірге қозғалады. Соқтығысқаннан кейінгі олардың ортақ жылдамдығын анықтаңыз!'
        self.description_swahili = f'Matoroli mawili yapo kwenye njia isiyo na msuguano (frictionless). Toroli A linasogea kuelekea toroli B, ambalo awali liko tuli, kama inavyoonyeshwa kwenye picha. Baada ya kugongana, matoroli hayo yanashikana na kusogea kama kitu kimoja. Bainisha velositi yao ya pamoja baada ya mgongano!'

class Phy016_multi(Phy016):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，一个球从光滑（无摩擦）斜面顶端由静止释放。它向下滑动到距地面高度 h = {self.final_height} m 的一点。假设 g = 10 m/s²，此时球的动能是多少？'
        self.description_arabic = f'تُترك كرة من السكون عند أعلى مستوى مائل أملس كما هو موضح في الشكل. تنزلق إلى نقطة على ارتفاع h = {self.final_height} m فوق سطح الأرض. بافتراض أن g = 10 m/s²، ما الطاقة الحركية للكرة عند هذه النقطة؟'
        self.description_hindi = f'चित्र में दिखाए अनुसार, एक चिकनी (घर्षण रहित) झुकी हुई सतह के शीर्ष से एक गेंद को विराम अवस्था से छोड़ा जाता है। यह जमीन से h = {self.final_height} m की ऊंचाई पर फिसलती है। यदि g = 10 m/s² है, तो इस बिंदु पर गेंद की गतिज ऊर्जा क्या होगी?'
        self.description_kazakh = f'Суретте көрсетілгендей, шар тегіс (үйкеліссіз) көлбеу жазықтықтың жоғарғы жағынан тыныштық күйінен босатылады. Ол жерден h = {self.final_height} m биіктіктегі нүктеге дейін сырғанап түседі. g = 10 m/s² деп есептесек, осы нүктедегі шардың кинетикалық энергиясы қандай?'
        self.description_swahili = f'Mpira unaachiwa kutoka hali ya utuli (rest) juu ya mteremko nyororo (usio na msuguano), kama inavyoonyeshwa kwenye kielelezo. Unateleza chini hadi kwenye nukta iliyo kimo h = {self.final_height} m juu ya ardhi. Kwa kudhani g = 10 m/s², nishati ya mwendo (kinetic energy) ya mpira kwenye nukta hiyo ni ipi?'

class Phy017_multi(Phy017):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个质量为 {self.box_mass} kg 的盒子在粗糙水平面上被一个恒定水平力拉动。图中展示作用在盒子上的摩擦力。盒子移动了图中所示的距离。求对盒子所做的净功！'
        self.description_arabic = f'يُسحب صندوق كتلته {self.box_mass} kg على سطح أفقي خشن بواسطة قوة أفقية ثابتة. قوة الاحتكاك موضحة في الشكل. يتحرك الصندوق المسافة الموضحة. أوجد الشغل الكلي المبذول على الصندوق.'
        self.description_hindi = f'{self.box_mass} kg द्रव्यमान वाले एक बॉक्स को एक खुरदरी क्षैतिज सतह पर एक स्थिर क्षैतिज बल द्वारा खींचा जाता है। बॉक्स पर लगने वाला घर्षण बल चित्र में दर्शाया गया है। बॉक्स चित्र में दर्शाई गई दूरी तय करता है। बॉक्स पर किए गए कुल कार्य का पता लगाएँ!'
        self.description_kazakh = f'Массасы {self.box_mass} kg қорап бұдырлы горизонтал бетпен тұрақты горизонтал күш арқылы тартылады. Қорапқа әсер ететін үйкеліс күші диаграммада көрсетілген. Қорап диаграммада көрсетілген қашықтыққа жылжиды. Қорапқа жасалған қорытқы жұмысты анықтаңыз!'
        self.description_swahili = f'Boksi lenye masi ya {self.box_mass} kg linavutwa kando ya uso wa mlalo wenye ukwaru kwa kani ya mlalo isiyobadilika. Kani ya msuguano inayokaimu juu ya boksi hilo imeonyeshwa kwenye mchoro. Boksi linasogea kwa umbali ulioonyeshwa. Bainisha kazi halisi (net work done) iliyofanywa kwenye boksi hilo!'

class Phy018_multi(Phy018):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一台起重机被用来将重物提升到如图所示的高度。起重机的电机消耗了 {self.energy_used} J 的能量。电机的效率为 ... % (假设 g = 10 m/s²)'
        self.description_arabic = f'تُستخدم رافعة لرفع حمولة إلى الارتفاع الموضح في الشكل. يستهلك المحرك {self.energy_used} J من الطاقة. ما كفاءة المحرك (%)؟ (افترض أن g = 10 m/s²).'
        self.description_hindi = f'चित्र में दर्शाई गई ऊँचाई तक भार उठाने के लिए क्रेन का उपयोग किया जाता है। क्रेन का मोटर {self.energy_used} J ऊर्जा का उपयोग करता है। मोटर की दक्षता ... % है (g = 10 m/s² मान लें)।'
        self.description_kazakh = f'Кран диаграммада көрсетілген биіктікке жүкті көтеру үшін қолданылады. Кранның қозғалтқышы {self.energy_used} J энергия жұмсайды. Қозғалтқыштың ПӘК-і ... % (g = 10 m/s² деп есептеңіз)'
        self.description_swahili = f'Kreni inatumiwa kuinua mzigo hadi kimo kilichoonyeshwa kwenye mchoro. Mota ya kreni hiyo inatumia nishati ya {self.energy_used} J. Ufanisi (efficiency) wa mota hiyo ni ... % (chukulia g = 10 m/s²)'

class Phy019_multi(Phy019):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，水族箱中的一条鱼向下游动。假设 g = 10 m/s² 且 ρ = 1000 kg/m³，鱼经历的压强变化为 ... Pa。'
        self.description_arabic = 'تتحرك سمكة في حوض إلى الأسفل كما هو موضح في الصورة. بافتراض أن g = 10 m/s² و ρ = 1000 kg/m³، فإن مقدار التغير في الضغط هو ... Pa.'
        self.description_hindi = 'चित्र में दर्शाए अनुसार, एक मछली एक्वेरियम में नीचे की ओर गति कर रही है। यदि g = 10 m/s² और ρ = 1000 kg/m³ है, तो मछली पर दाब में ... Pa का परिवर्तन होता है।'
        self.description_kazakh = 'Суретте көрсетілгендей, аквариумдағы балық төмен қарай қозғалады. g = 10 m/s² және ρ = 1000 kg/m³ деп есептесек, балыққа әсер ететін қысымның өзгеруі ... Pa құрайды.'
        self.description_swahili = f'Samaki kwenye akwariamu anasogea kwenda chini, kama inavyoonyeshwa kwenye picha. Kwa kudhani g = 10 m/s² na ρ = 1000 kg/m³, samaki huyo anapata mabadiliko ya kanieneo (change in pressure) ya ... Pa.'

class Phy020_multi(Phy020):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一定质量的气体在恒温下保持稳定。其压力-体积 (P-V) 关系如下图所示。当体积为 V={self.v_reference} 时，气体的压力是多少？'
        self.description_arabic = f'تُحفظ كتلة ثابتة من الغاز عند درجة حرارة ثابتة. يوضح الشكل العلاقة بين الضغط والحجم (P-V). ما ضغط الغاز عندما يكون الحجم V={self.v_reference}؟'
        self.description_hindi = f'एक निश्चित द्रव्यमान वाली गैस को स्थिर तापमान पर रखा जाता है। इसका दाब-आयतन (P-V) संबंध नीचे दिए गए ग्राफ में दर्शाया गया है। जब आयतन V={self.v_reference} हो, तो गैस का दाब क्या होगा?'
        self.description_kazakh = f'Газдың тұрақты массасы тұрақты температурада сақталады. Оның қысымы мен көлемі (P-V) арасындағы тәуелділік төмендегі графикте көрсетілген. Көлемі V={self.v_reference} болғандағы газдың қысымы неге тең?'
        self.description_swahili = f'Masi isiyobadilika ya gesi inadumishwa katika halijoto isiyobadilika (constant temperature). Uhusiano wa kanieneo na ujazo (P-V) umeonyeshwa kwenye grafu hapa chini. Kanieneo ya gesi hiyo ni ipi wakati ujazo ni V={self.v_reference}?'

class Phy021_multi(Phy021):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一定质量的气体保持在恒定温度下。其压强-体积 (P-V) 关系如下图所示。当压强为 P={self.p_reference} 时，气体的体积是多少？'
        self.description_arabic = f'تُحفظ كتلة ثابتة من الغاز عند درجة حرارة ثابتة. يوضح الشكل العلاقة بين الضغط والحجم (P-V). ما حجم الغاز عندما يكون الضغط P={self.p_reference}؟'
        self.description_hindi = f'एक निश्चित द्रव्यमान वाली गैस को स्थिर तापमान पर रखा जाता है। इसका दाब-आयतन (P-V) संबंध नीचे दिए गए ग्राफ में दर्शाया गया है। जब दाब P={self.p_reference} हो, तो गैस का आयतन क्या होगा?'
        self.description_kazakh = f'Газдың тұрақты массасы тұрақты температурада сақталады. Оның қысымы мен көлемі (P-V) арасындағы тәуелділік төмендегі графикте көрсетілген. Қысым P={self.p_reference} болған кезде газдың көлемі қандай болады?'
        self.description_swahili = f'Masi isiyobadilika ya gesi inadumishwa katika halijoto isiyobadilika (constant temperature). Uhusiano wa kanieneo na ujazo (P-V) umeonyeshwa kwenye grafu hapa chini. Ujazo wa gesi hiyo ni upi wakati kanieneo ni P={self.p_reference}?'

class Phy022_multi(Phy022):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示物体温度升高时传递给物体的热能。物体从 {self.initial_temperature} °C 加热到 {self.final_temperature} °C 时吸收的热能为 ... kJ。'
        self.description_arabic = f'يوضح الشكل الطاقة الحرارية المنتقلة إلى جسم مع ارتفاع درجة حرارته. الطاقة الحرارية التي يكتسبها الجسم عند تسخينه من {self.initial_temperature} °C إلى {self.final_temperature} °C هي ... kJ.'
        self.description_hindi = f'ग्राफ किसी वस्तु के तापमान में वृद्धि के साथ उसमें स्थानांतरित होने वाली ऊष्मीय ऊर्जा को दर्शाता है। वस्तु को प्रारंभिक तापमान {self.initial_temperature} °C से अंतिम तापमान {self.final_temperature} °C तक गर्म करने पर प्राप्त ऊष्मीय ऊर्जा ... kJ है।'
        self.description_kazakh = f'График дененің температурасы артқан кезде оған берілген жылу энергиясын көрсетеді. Денені {self.initial_temperature} °C-тан {self.final_temperature} °C-қа дейін қыздырғанда алған жылу энергиясы ... kJ.'
        self.description_swahili = f'Grafu inaonyesha nishati ya joto inayohamishiwa kwenye gimba wakati halijoto yake inapoongezeka. Nishati ya joto inayopokelewa na gimba linapopashwa joto kutoka {self.initial_temperature} °C hadi {self.final_temperature} °C ni ... kJ.'

class Phy023_multi(Phy023):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示物体温度从 {self.initial_temperature} °C 升高时传递给物体的热能。如果物体的质量为 {self.mass} kg，其比热容为 ... J/(kg °C)'
        self.description_arabic = f'يوضح الشكل الطاقة الحرارية المنتقلة إلى جسم مع ارتفاع درجة حرارته بدءًا من {self.initial_temperature} °C. إذا كانت كتلة الجسم {self.mass} kg، فأوجد السعة الحرارية النوعية له بوحدة J/(kg °C).'
        self.description_hindi = f'ग्राफ किसी वस्तु के तापमान में {self.initial_temperature} °C की वृद्धि होने पर उसमें स्थानांतरित होने वाली ऊष्मीय ऊर्जा को दर्शाता है। यदि वस्तु का द्रव्यमान {self.mass} kg है, तो उसकी विशिष्ट ऊष्मा धारिता ... J/(kg °C) है।'
        self.description_kazakh = f'График дененің температурасы {self.initial_temperature} °C-тан артқан кезде оған берілген жылу энергиясын көрсетеді. Егер дененің массасы {self.mass} kg болса, оның меншікті жылу сыйымдылығы ... J/(kg °C)'
        self.description_swahili = f'Grafu inaonyesha nishati ya joto inayohamishiwa kwenye gimba wakati halijoto yake inapoongezeka kutoka {self.initial_temperature} °C. Ikiwa masi ya gimba hilo ni {self.mass} kg, uwezo wake wa joto mahususi (specific heat capacity) ni ... J/(kg °C)'

class Phy024_multi(Phy024):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示物体温度从 {self.initial_temperature} °C 升高时传递给物体的热能。如果物体的比热容为 {self.specific_heat_capacity} J/(kg °C)，其质量为 ... kg'
        self.description_arabic = f'يوضح الشكل الطاقة الحرارية المنتقلة إلى جسم مع ارتفاع درجة حرارته بدءًا من {self.initial_temperature} °C. إذا كانت السعة الحرارية النوعية للجسم {self.specific_heat_capacity} J/(kg °C)، فأوجد كتلته.'
        self.description_hindi = f'ग्राफ किसी वस्तु के तापमान में {self.initial_temperature} °C की वृद्धि होने पर उसमें स्थानांतरित होने वाली ऊष्मीय ऊर्जा को दर्शाता है। यदि वस्तु की विशिष्ट ऊष्मा धारिता {self.specific_heat_capacity} J/(kg °C) है, तो उसका द्रव्यमान ... kg है।'
        self.description_kazakh = f'График дененің температурасы {self.initial_temperature} °C-тан артқан кезде оған берілген жылу энергиясын көрсетеді. Егер дененің меншікті жылу сыйымдылығы {self.specific_heat_capacity} J/(kg °C) болса, оның массасы ... kg'
        self.description_swahili = f'Grafu inaonyesha nishati ya joto inayohamishiwa kwenye gimba wakati halijoto yake inapoongezeka kutoka {self.initial_temperature} °C. Ikiwa uwezo wa joto mahususi (specific heat capacity) wa gimba ni {self.specific_heat_capacity} J/(kg °C), masi yake ni ... kg'

class Phy025_multi(Phy025):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示物体温度从 {self.initial_temperature} °C 升高时传递给物体的热能。当物体吸收的能量为 Q = {self.energy_in_kJ} kJ 时，其温度为 ... °C。'
        self.description_arabic = f'يوضح الشكل الطاقة الحرارية المنتقلة إلى جسم مع ارتفاع درجة حرارته بدءًا من {self.initial_temperature} °C. عندما تكون الطاقة المكتسبة Q = {self.energy_in_kJ} kJ، ما درجة حرارة الجسم؟'
        self.description_hindi = f'ग्राफ किसी वस्तु के तापमान में {self.initial_temperature} °C की वृद्धि के साथ उसमें स्थानांतरित होने वाली ऊष्मीय ऊर्जा को दर्शाता है। जब वस्तु द्वारा प्राप्त ऊर्जा Q = {self.energy_in_kJ} kJ होती है, तो उसका तापमान ... °C होता है।'
        self.description_kazakh = f'График дененің температурасы {self.initial_temperature} °C-тан артқан кезде оған берілген жылу энергиясын көрсетеді. Дене алған энергия Q = {self.energy_in_kJ} kJ болған кезде, оның температурасы ... °C.'
        self.description_swahili = f'Grafu inaonyesha nishati ya joto inayohamishiwa kwenye gimba wakati halijoto yake inapoongezeka kutoka {self.initial_temperature} °C. Wakati nishati inayopokelewa na gimba hilo ni Q = {self.energy_in_kJ} kJ, halijoto yake ni ... °C.'

class Phy026_multi(Phy026):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个导体放置在两个热库之间。如果导体保持在恒定温度，它会以 ... kJ/s 的速率散发热量 (假设除了热量外没有发生其他能量转移)。'
        self.description_arabic = 'يوضع موصل بين خزانين. إذا حُفظ الموصل عند درجة حرارة ثابتة، فإنه يبعث حرارة بمعدل ... kJ/s (افترض عدم انتقال طاقة إلا على شكل حرارة).'
        self.description_hindi = 'दो जलाशयों के बीच एक चालक रखा गया है। यदि चालक को स्थिर तापमान पर रखा जाए, तो यह ... kJ/s की दर से ऊष्मा उत्सर्जित करता है (मान लें कि ऊष्मा के अलावा कोई अन्य ऊर्जा स्थानांतरण नहीं होता है)।'
        self.description_kazakh = 'Өткізгіш екі резервуардың арасына орналастырылған. Егер өткізгіш тұрақты температурада ұсталса, ол ... kJ/s жылдамдықпен жылу бөледі (жылудан басқа энергия тасымалы орын алмайды деп есептеңіз).'
        self.description_swahili = 'Kipitishio kimewekwa kati ya hifadhi mbili za joto. Ikiwa kipitishio hicho kinadumishwa katika halijoto isiyobadilika (constant temperature), kinatoa joto katika kiwango cha ... kJ/s (chukulia kwamba hakuna uhamishaji wa nishati mwingine unaotokea isipokuwa joto).'

class Phy027_multi(Phy027):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图示为一列具有特定波长的波。如果频率为 {self.frequency} Hz，则波速为 ... cm/s'
        self.description_arabic = f'يوضح الشكل موجة ذات طول موجي معين. إذا كان التردد {self.frequency} Hz، فما سرعة الموجة بوحدة cm/s؟'
        self.description_hindi = f'चित्र में एक निश्चित तरंगदैर्ध्य की तरंग दर्शाई गई है। यदि आवृत्ति {self.frequency} Hz है, तो तरंग की गति ... cm/s है।'
        self.description_kazakh = f'Диаграммада белгілі бір толқын ұзындығы бар толқын көрсетілген. Егер жиілігі {self.frequency} Hz болса, толқынның таралу жылдамдығы ... cm/s'
        self.description_swahili = f'Mchoro unaonyesha wimbi lenye urefu fulani wa wimbi (wavelength). Ikiwa frikwensi ni {self.frequency} Hz, kasi ya wimbi hilo ni ... cm/s'

class Phy028_multi(Phy028):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图示为一列具有特定波长的波。如果波速为 {self.speed} cm/s，则其频率为 ... Hz'
        self.description_arabic = f'يوضح الشكل موجة ذات طول موجي معين. إذا كانت سرعة الموجة {self.speed} cm/s، فما ترددها بوحدة Hz؟'
        self.description_hindi = f'चित्र में एक निश्चित तरंगदैर्ध्य वाली तरंग दर्शाई गई है। यदि तरंग की गति {self.speed} cm/s है, तो इसकी आवृत्ति ... Hz है।'
        self.description_kazakh = f'Диаграммада белгілі бір толқын ұзындығы бар толқын көрсетілген. Егер толқынның таралу жылдамдығы {self.speed} cm/s болса, оның жиілігі ... Hz'
        self.description_swahili = f'Mchoro unaonyesha wimbi lenye urefu fulani wa wimbi (wavelength). Ikiwa kasi ya wimbi hilo ni {self.speed} cm/s, frikwensi yake ni ... Hz'

class Phy029_multi(Phy029):
    def __init__(self):
        super().__init__()
        self.description_chinese = '光在两种不同的介质A和B中传播。给出了光在每种介质中的速度。求介质B与介质A的折射率之比！'
        self.description_arabic = 'ينتقل الضوء عبر وسطين مختلفين A و B. سرعة الضوء في كل وسط معطاة. احسب نسبة معامل الانكسار للوسط B إلى الوسط A.'
        self.description_hindi = 'प्रकाश दो अलग-अलग माध्यमों, A और B से होकर गुजरता है। प्रत्येक माध्यम में प्रकाश की गति दी गई है। B और A के अपवर्तनांक का अनुपात ज्ञात कीजिए!'
        self.description_kazakh = 'Жарық екі түрлі А және В орталары арқылы таралады. Әр ортадағы жарық жылдамдығы берілген. В ортасының А ортасына қатысты сыну көрсеткішінің қатынасын есептеңіз!'
        self.description_swahili = 'Mwanga unasafiri kupitia midia mbili tofauti, A na B. Kasi ya mwanga katika kila midia imetolewa. Kokotoa uwiano wa faharisi ya mchepuko (refractive index) wa B kwa A!'

class Phy030_multi(Phy030):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'光在两种不同的介质A和B中传播。给出了光在介质A中的速度。如果介质B与介质A的折射率之比为 {self.b_to_a_ratio}，求光在介质B中的速度！'
        self.description_arabic = f'ينتقل الضوء عبر وسطين مختلفين A و B. سرعة الضوء في الوسط A معطاة. إذا كانت نسبة معامل الانكسار للوسط B إلى الوسط A تساوي {self.b_to_a_ratio}، فأوجد سرعة الضوء في الوسط B.'
        self.description_hindi = f'प्रकाश दो अलग-अलग माध्यमों, A और B से होकर गुजरता है। माध्यम A में प्रकाश की गति दी गई है। यदि माध्यम B और A के अपवर्तनांक का अनुपात {self.b_to_a_ratio} है, तो माध्यम B में प्रकाश की गति की गणना कीजिए!'
        self.description_kazakh = f'Жарық екі түрлі А және В орталары арқылы таралады. А ортасындағы жарық жылдамдығы берілген. Егер В ортасының А ортасына қатысты сыну көрсеткішінің қатынасы {self.b_to_a_ratio} болса, В ортасындағы жарық жылдамдығын есептеңіз!'
        self.description_swahili = f'Mwanga unasafiri kupitia midia mbili tofauti, A na B. Kasi ya mwanga katika midia A imetolewa. Ikiwa uwiano wa faharisi ya mchepuko (refractive index) wa midia B kwa A ni {self.b_to_a_ratio}, kokotoa kasi ya mwanga katika midia B!'

class Phy031_multi(Phy031):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'光入射到两种介质的边界上。第一种介质的折射率为 n1，第二种介质的折射率为 n2。求 sin(θ2) 的值。'
        self.description_arabic = 'يسقط الضوء على الحد الفاصل بين وسطين. معامل الانكسار للوسط الأول هو n1 وللوسط الثاني هو n2. احسب قيمة sin(θ2).'
        self.description_hindi = f'प्रकाश दो माध्यमों की सीमा पर आपतित होता है। पहले माध्यम का अपवर्तनांक n1 है और दूसरे माध्यम का अपवर्तनांक n2 है। sin(θ2) का मान ज्ञात कीजिए।'
        self.description_kazakh = f'Жарық екі ортаның шекарасына түседі. Бірінші ортаның сыну көрсеткіші n1, ал екінші ортанікі n2. sin(θ2) мәнін есептеңіз.'
        self.description_swahili = f'Mwanga unatua kwenye mpaka (boundary) kati ya midia mbili. Faharisi ya mchepuko (refractive index) ya midia ya kwanza ni n1 na ya midia ya pili ni n2. Kokotoa thamani ya sin(θ2)!'

class Phy032_multi(Phy032):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'光入射到两种介质的边界上。第一种介质的折射率为 n1，第二种介质的折射率为 n2。求 n2 的值。'
        self.description_arabic = 'يسقط الضوء على الحد الفاصل بين وسطين. معامل الانكسار للوسط الأول هو n1 وللوسط الثاني هو n2. احسب قيمة n2.'
        self.description_hindi = f'प्रकाश दो माध्यमों की सीमा पर आपतित होता है। पहले माध्यम का अपवर्तनांक n1 है और दूसरे माध्यम का अपवर्तनांक n2 है। n2 का मान ज्ञात कीजिए।'
        self.description_kazakh = f'Жарық екі ортаның шекарасына түседі. Бірінші ортаның сыну көрсеткіші n1, ал екінші ортанікі n2. n2 мәнін есептеңіз.'
        self.description_swahili = f'Mwanga unatua kwenye mpaka (boundary) kati ya midia mbili. Faharisi ya mchepuko (refractive index) ya midia ya kwanza ni n1 na ya midia ya pili ni n2. Kokotoa thamani ya n2!'

class Phy033_multi(Phy033):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一名学生站在A点开枪。站在B点的另一名学生在看到枪枝闪光时启动秒表，在听到枪声时停止秒表。秒表记录的时间为 {self.time} 秒。根据该实验计算空气中的声速 (以 m/s 为单位)！(忽略光速造成的延迟)'
        self.description_arabic = f'يقف طالب عند النقطة A ويطلق مسدسًا. يقف طالب آخر عند النقطة B ويشغّل ساعة إيقاف عند رؤية الوميض ويوقفها عند سماع الصوت. الزمن المسجل هو {self.time} ثانية. احسب سرعة الصوت في الهواء (بوحدة m/s)، مع إهمال زمن انتقال الضوء.'
        self.description_hindi = f'एक छात्र बिंदु A पर खड़ा होकर पिस्तौल से गोली चलाता है। एक अन्य छात्र बिंदु B पर खड़ा है और पिस्तौल की चमक देखते ही स्टॉपवॉच चालू कर देता है और गोली चलने की आवाज सुनते ही उसे रोक देता है। स्टॉपवॉच पर दर्ज समय {self.time} सेकंड है। इस प्रयोग के आधार पर हवा में ध्वनि की गति (m/s में) ज्ञात कीजिए! (प्रकाश की गति के कारण होने वाले विलंब को अनदेखा करें)'
        self.description_kazakh = f'Оқушы А нүктесінде тұрып, тапаншадан оқ атады. В нүктесінде тұрған басқа оқушы тапаншаның жарқылын көргенде секундомерді қосып, тарс еткен дыбысты естігенде оны тоқтатады. Секундомерде жазылған уақыт {self.time} секунд. Осы тәжірибе негізінде ауадағы дыбыс жылдамдығын (m/s) есептеңіз! (жарық жылдамдығына байланысты кідірісті ескермеңіз)'
        self.description_swahili = f'Mwanafunzi anasimama katika hatua A na kufyatua bastola. Mwanafunzi mwingine aliyesimama katika hatua B anawasha saa-muda (stopwatch) anapoona mwako wa bastola na kuizima anaposikia mlio. Muda uliorekodiwa ni sekunde {self.time}. Kokotoa kasi ya sauti (speed of sound) hewani (katika m/s) kulingana na jaribio hili! (puuza ucheleweshaji wa kasi ya mwanga)'

class Phy034_multi(Phy034):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一艘研究船正在绘制海底地形图。它向海底径直发送声音脉冲 (声纳)。随后，船只探测到该脉冲的反射波 (回声)。计算此位置的水深 (以米为单位)！'
        self.description_arabic = 'تقوم سفينة أبحاث برسم خرائط لقاع المحيط. ترسل نبضة صوتية (سونار) عموديًا نحو القاع، ثم تستقبل الصدى. احسب عمق الماء في هذا الموقع (بوحدة المتر).'
        self.description_hindi = f'एक शोध पोत समुद्र तल का मानचित्रण कर रहा है। यह समुद्र तल पर सीधे ध्वनि तरंग (सोनार) भेजता है। पोत फिर तरंग के परावर्तन (प्रतिध्वनि) का पता लगाता है। इस स्थान पर पानी की गहराई (मीटर में) ज्ञात कीजिए!'
        self.description_kazakh = f'Зерттеу кемесі мұхит түбінің картасын жасауда. Ол теңіз түбіне тікелей төмен қарай дыбыс импульсін (сонар) жібереді. Содан кейін кеме импульстің шағылысуын (жаңғырығын) анықтайды. Осы жердегі судың тереңдігін (метрмен) есептеңіз!'
        self.description_swahili = 'Meli ya utafiti inachora ramani ya sakafu ya bahari. Inatuma pigo la sauti (sonar) moja kwa moja chini hadi kwenye sakafu ya bahari. Kisha meli hiyo inanasa mwangwi (echo) wa pigo hilo. Kokotoa kina cha maji katika eneo hili (katika mita)!'

class Phy035_multi(Phy035):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示了一个电路。计算在 {self.time} 秒内通过电阻器的总电荷量 (以库仑为单位)！'
        self.description_arabic = f'يوضح الشكل دائرة كهربائية. احسب الشحنة الكلية (بوحدة الكولوم) التي تمر عبر المقاومة خلال {self.time} ثانية.'
        self.description_hindi = f'चित्र में एक विद्युत परिपथ दिखाया गया है। {self.time} सेकंड में प्रतिरोधक से होकर गुजरने वाले कुल आवेश (Coulombs में) की गणना कीजिए!'
        self.description_kazakh = f'Суретте электр тізбегі көрсетілген. Резистор арқылы {self.time} секундта өтетін жалпы зарядты (Кулонмен) есептеңіз!'
        self.description_swahili = f'Sakiti ya umeme imeonyeshwa kwenye picha. Kokotoa jumla ya chaji (total charge) katika kulumu (Coulombs) inayopita kwenye kinza (resistor) ndani ya sekunde {self.time}!'

class Phy036_multi(Phy036):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示了一个电路。计算总电荷量为 {self.total_charge} C 通过电阻器所需的时间！'
        self.description_arabic = f'يوضح الشكل دائرة كهربائية. احسب الزمن اللازم لمرور شحنة مقدارها {self.total_charge} C عبر المقاومة.'
        self.description_hindi = f'चित्र में एक विद्युत परिपथ दिखाया गया है। कुल आवेश {self.total_charge} C को प्रतिरोधक से गुजरने में लगने वाला समय ज्ञात कीजिए!'
        self.description_kazakh = f'Суретте электр тізбегі көрсетілген. Жалпы заряды {self.total_charge} C резистор арқылы өтуі үшін қажетті уақытты есептеңіз!'
        self.description_swahili = f'Sakiti ya umeme imeonyeshwa kwenye picha. Kokotoa muda uliochukuliwa ili jumla ya chaji (total charge) ya {self.total_charge} C ipite kwenye kinza (resistor)!'

class Phy037_multi(Phy037):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'在给定的电路中，观察到在 {self.time} 秒内，有 {self.total_charge} C的总电荷通过电阻B。计算流过电阻A的电流！'
        self.description_arabic = f'في الدائرة الموضحة، تمر شحنة مقدارها {self.total_charge} C عبر المقاومة B خلال {self.time} ثانية. احسب شدة التيار في المقاومة A.'
        self.description_hindi = f'दिए गए परिपथ में, यह देखा गया है कि प्रतिरोधक B से {self.time} सेकंड में {self.total_charge} C का कुल आवेश प्रवाहित होता है। प्रतिरोधक A से प्रवाहित होने वाली धारा की गणना कीजिए!'
        self.description_kazakh = f'Берілген тізбекте В резисторы арқылы {self.time} секундта жалпы заряды {self.total_charge} C өтетіні байқалды. А резисторы арқылы өтетін ток күшін есептеңіз!'
        self.description_swahili = f'Katika sakiti iliyotolewa, inazingatiwa kuwa jumla ya chaji (total charge) ya {self.total_charge} C inapita kwenye kinza B ndani ya sekunde {self.time}. Kokotoa mkondo (current) unaopita kwenye kinza A!'

class Phy038_multi(Phy038):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'在一次电学实验中，测得为了将电荷移过电路中的电阻器A，做了 {self.work} J 的功。计算该电阻器两端的电势差 (电压)！'
        self.description_arabic = f'في تجربة كهربائية، بُذل شغل مقداره {self.work} J لنقل شحنات عبر المقاومة A. احسب فرق الجهد بين طرفي المقاومة.'
        self.description_hindi = f'एक विद्युतीय प्रयोग के दौरान, परिपथ में प्रतिरोधक A के आर-पार आवेशों को स्थानांतरित करने में {self.work} J कार्य किया जाता है। प्रतिरोधक के दोनों सिरों के बीच विभवांतर (वोल्टेज) की गणना कीजिए!'
        self.description_kazakh = f'Электрлік тәжірибе кезінде тізбектегі А резисторы арқылы зарядтарды тасымалдау үшін {self.work} J жұмыс жасалатыны өлшенді. Резистордың екі ұшы арасындағы потенциалдар айырымын (кернеуді) есептеңіз!'
        self.description_swahili = f'Wakati wa jaribio la umeme, imepimwa kuwa kazi ya {self.work} J inafanywa ili kusogeza chaji (charges) kupitia kinza A katika sakiti. Kokotoa tofauti ya uwezo (potential difference) kati ya ncha mbili za kinza hicho!'

class Phy039_multi(Phy039):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'在一次电学实验中，{self.charge} C 的电荷被移过电路中的电阻器A。计算所做的总功 (以焦耳为单位)！'
        self.description_arabic = f'في تجربة كهربائية، نُقلت شحنة مقدارها {self.charge} C عبر المقاومة A. احسب الشغل الكلي المبذول (بوحدة الجول).'
        self.description_hindi = f'एक विद्युतीय प्रयोग के दौरान, परिपथ में प्रतिरोधक A के पार {self.charge} C आवेश स्थानांतरित किए जाते हैं। कुल कार्य (Joule में) की गणना कीजिए!'
        self.description_kazakh = f'Электрлік тәжірибе кезінде тізбектегі А резисторы арқылы {self.charge} C заряд тасымалданды. Жасалған жалпы жұмысты (Джоульмен) есептеңіз!'
        self.description_swahili = f'Wakati wa jaribio la umeme, chaji za {self.charge} C zinasogezwa kupitia kinza A katika sakiti. Kokotoa jumla ya kazi iliyofanywa (total work done) katika Joule!'

class Phy040_multi(Phy040):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示了一个电路。计算电阻器A的电阻！'
        self.description_arabic = 'يوضح الشكل دائرة كهربائية. احسب مقاومة المقاومة A.'
        self.description_hindi = f'चित्र में एक विद्युत परिपथ दिखाया गया है। प्रतिरोधक A का प्रतिरोध ज्ञात कीजिए!'
        self.description_kazakh = f'Суретте электр тізбегі көрсетілген. А резисторының кедергісін есептеңіз!'
        self.description_swahili = 'Picha inaonyesha sakiti ya umeme. Kokotoa ukinzani (resistance) wa kinza A!'

class Phy041_multi(Phy041):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示了一个电路。计算流过电阻器B的电流！'
        self.description_arabic = f'توضح الصورة دائرة كهربائية. احسب شدة التيار المار في المقاومة B.'
        self.description_hindi = f'चित्र में एक विद्युत परिपथ दिखाया गया है। प्रतिरोधक B में प्रवाहित होने वाली धारा की गणना कीजिए!'
        self.description_kazakh = f'Суретте электр тізбегі көрсетілген. В резисторы арқылы өтетін ток күшін есептеңіз!'
        self.description_swahili = 'Picha inaonyesha sakiti ya umeme. Kokotoa mkondo (current) unaopita kwenye kinza B!'

class Phy042_multi(Phy042):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中展示了一个电路。求电阻器C两端的电压！'
        self.description_arabic = 'توضح الصورة دائرة كهربائية. أوجد فرق الجهد عبر المقاومة C.'
        self.description_hindi = 'चित्र में एक विद्युत परिपथ दिखाया गया है। प्रतिरोधक C के सिरों पर वोल्टेज ज्ञात कीजिए!'
        self.description_kazakh = 'Суретте электр тізбегі көрсетілген. С резисторындағы кернеуді табыңыз!'
        self.description_swahili = 'Picha inaonyesha sakiti ya umeme. Kokotoa volteji (potential difference) inayopita kwenye kinza C!'

class Phy043_multi(Phy043):
    def __init__(self):
        super().__init__()
        self.description_chinese = '下图展示了阻值恒定的电阻器的电流-电压 (I-V) 特性。根据该图像，计算此电阻器的电阻 (以欧姆 (Ω) 为单位)！'
        self.description_arabic = 'يوضح الشكل منحنى التيار-الجهد (I-V) لمقاومة ذات قيمة ثابتة. بناءً على الشكل، احسب قيمة المقاومة بوحدة الأوم (Ω).'
        self.description_hindi = 'नीचे दिए गए ग्राफ में एक स्थिर प्रतिरोध वाले प्रतिरोधक के लिए धारा-वोल्टेज (I-V) विशेषताएँ दर्शाई गई हैं। ग्राफ के अनुसार, इस प्रतिरोधक का प्रतिरोध ohms (Ω) में ज्ञात कीजिए!'
        self.description_kazakh = 'Төмендегі графикте тұрақты кедергісі бар резистордың вольт-амперлік (I-V) сипаттамасы көрсетілген. Графикке сәйкес, осы резистордың кедергісін оммен (Ω) есептеңіз!'
        self.description_swahili = 'Grafu hapa chini inaonyesha sifa za mkondo-volteji (I-V characteristics) za kinza chenye ukinzani usiobadilika. Kulingana na grafu, kokotoa ukinzani wa kinza hiki katika omu (Ω)!'

class Phy044_multi(Phy044):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'下图展示了白炽灯的电流-电压 (I-V) 特性。根据该图像，计算当电势差为 {self.v_point} V 时白炽灯的电阻！'
        self.description_arabic = f'يوضح الشكل منحنى التيار-الجهد (I-V) لمصباح ذي فتيلة. بناءً على الشكل، احسب مقاومة المصباح عند فرق جهد مقداره {self.v_point} V.'
        self.description_hindi = f'नीचे दिए गए ग्राफ में फिलामेंट लैंप के लिए करंट-वोल्टेज (I-V) विशेषताएँ दर्शाई गई हैं। ग्राफ के अनुसार, जब विभवांतर {self.v_point} V हो, तो फिलामेंट लैंप का प्रतिरोध ज्ञात कीजिए!'
        self.description_kazakh = f'Төмендегі графикте қыздыру шамының вольт-амперлік (I-V) сипаттамасы көрсетілген. Графикке сәйкес, потенциалдар айырымы {self.v_point} V болған кездегі қыздыру шамының кедергісін есептеңіз!'
        self.description_swahili = f'Grafu hapa chini inaonyesha sifa za mkondo-volteji (I-V characteristics) za taa ya filamenti. Kulingana na grafu, kokotoa ukinzani wa taa hiyo wakati tofauti ya uwezo (potential difference) ni {self.v_point} V!'

class Phy045_multi(Phy045):
    def __init__(self):
        super().__init__()
        self.description_chinese = '电路图展示了由单个电池供电的三盏灯 (A、B和C)。根据图中提供的值，计算灯A耗散的功率 (以瓦特 (W) 为单位)！'
        self.description_arabic = 'يوضح مخطط الدائرة ثلاثة مصابيح (A و B و C) موصولة ببطارية واحدة. بناءً على القيم المعطاة، احسب القدرة المستهلكة في المصباح A بوحدة الواط (W).'
        self.description_hindi = 'सर्किट चित्र में तीन लैंप (A, B और C) एक ही बैटरी से संचालित होते हुए दिखाए गए हैं। चित्र में दिए गए मानों के आधार पर, लैंप A द्वारा खपत की गई शक्ति watts (W) में की गणना कीजिए!'
        self.description_kazakh = 'Тізбек диаграммасында бір батареядан қуат алатын үш шам (A, B және C) көрсетілген. Диаграммада берілген мәндерге сүйене отырып, А шамында тұтынылатын қуатты ваттпен (W) есептеңіз!'
        self.description_swahili = 'Mchoro wa sakiti unaonyesha taa tatu (A, B, na C) zinazowezeshwa na betri moja. Kulingana na thamani zilizotolewa kwenye mchoro, kokotoa nguvu ya umeme (power) iliyotawanywa na taa A katika wati (W)!'

class Phy046_multi(Phy046):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'电路图展示了由单个电池供电的三盏灯 (A、B和C)。已知灯B耗散 {self.power_B} W 的电功率，根据图中提供的值计算流过灯B的电流！'
        self.description_arabic = f'يوضح مخطط الدائرة ثلاثة مصابيح (A و B و C) موصولة ببطارية واحدة. إذا كانت القدرة المستهلكة في المصباح B تساوي {self.power_B} W، فأوجد شدة التيار المار فيه.'
        self.description_hindi = f'सर्किट आरेख में तीन लैंप (A, B और C) दिखाए गए हैं जो एक ही बैटरी से संचालित होते हैं। यह देखते हुए कि लैंप B {self.power_B} W विद्युत शक्ति का क्षय करता है, आरेख में दिए गए मानों के आधार पर लैंप B से प्रवाहित होने वाली धारा की गणना कीजिए!'
        self.description_kazakh = f'Тізбек диаграммасында бір батареядан қуат алатын үш шам (A, B және C) көрсетілген. В шамы {self.power_B} W электр қуатын тұтынатынын ескеріп, диаграммада берілген мәндер негізінде В шамы арқылы өтетін ток күшін есептеңіз!'
        self.description_swahili = f'Mchoro wa sakiti unaonyesha taa tatu (A, B, na C) zinazowezeshwa na betri moja. Kwa kuwa taa B inatawanya nguvu ya umeme (electrical power) ya {self.power_B} W, kokotoa mkondo (current) unaopita kwenye taa B kulingana na thamani zilizotolewa kwenye mchoro!'

class Phy047_multi(Phy047):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示了一个包含三盏灯和一个电阻器的电路。根据该图，计算灯C通电 {self.time} 秒后消耗的能量！'
        self.description_arabic = f'توضح الصورة دائرة كهربائية تحتوي على ثلاثة مصابيح ومقاومة واحدة. بناءً على الشكل، احسب الطاقة المستهلكة في المصباح C خلال {self.time} ثانية.'
        self.description_hindi = f'चित्र में तीन लैंप और एक प्रतिरोधक वाला एक विद्युत परिपथ दिखाया गया है। चित्र के आधार पर, {self.time} सेकंड तक चालू रहने के बाद लैंप C द्वारा खपत की गई ऊर्जा की गणना कीजिए!'
        self.description_kazakh = f'Суретте үш шам және бір резистордан тұратын электр тізбегі көрсетілген. Диаграммаға сүйене отырып, С шамы {self.time} секунд бойы қосылып тұрғаннан кейін тұтынатын энергияны есептеңіз!'
        self.description_swahili = f'Picha inaonyesha sakiti ya umeme yenye taa tatu na kinza kimoja. Kulingana na mchoro, kokotoa nishati (energy) iliyotumika na taa C baada ya kuwashwa kwa sekunde {self.time}!'

class Phy048_multi(Phy048):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'电路图展示了三个电阻器 (A、B和C)。根据图中提供的值，计算电阻器B耗散 {self.energy_dissipated} J 电能所需的时间 (以秒为单位)！'
        self.description_arabic = f'يوضح مخطط الدائرة ثلاث مقاومات (A و B و C). بناءً على القيم المعطاة، احسب الزمن اللازم لكي تبدد المقاومة B طاقة مقدارها {self.energy_dissipated} J.'
        self.description_hindi = f'परिपथ आरेख में तीन प्रतिरोधक (A, B और C) दर्शाए गए हैं। आरेख में दिए गए मानों के आधार पर, प्रतिरोधक B द्वारा {self.energy_dissipated} J विद्युत ऊर्जा के क्षय के लिए आवश्यक समय (सेकंड में) की गणना कीजिए!'
        self.description_kazakh = f'Тізбек диаграммасында үш резистор (A, B және C) көрсетілген. Диаграммада берілген мәндерге сүйене отырып, В резисторы {self.energy_dissipated} J электр энергиясын тұтынуы үшін қажетті уақытты (секундпен) есептеңіз!'
        self.description_swahili = f'Mchoro wa sakiti unaonyesha vikinza vitatu (A, B, na C). Kulingana na thamani zilizotolewa kwenye mchoro, kokotoa muda unaohitajika (katika sekunde) kwa kinza B kutawanya nishati ya umeme (electrical energy) ya {self.energy_dissipated} J!'

class Phy049_multi(Phy049):
    def __init__(self):
        super().__init__()
        self.description_chinese = '下方的电路图展示了标记为A到G的七个电阻器的排列。根据提供的图，计算包含电阻器E、F和G的部分的等效电阻 (以欧姆 (Ω) 为单位)！'
        self.description_arabic = 'يوضح مخطط الدائرة ترتيبًا لسبع مقاومات مسماة من A إلى G. احسب المقاومة المكافئة للجزء الذي يحتوي على المقاومات E و F و G بوحدة الأوم (Ω).'
        self.description_hindi = 'नीचे दिए गए परिपथ आरेख में A से G तक अंकित सात प्रतिरोधों की व्यवस्था दर्शाई गई है। दिए गए आरेख के आधार पर, प्रतिरोध E, F और G वाले भाग का समतुल्य प्रतिरोध ohms (Ω) में ज्ञात कीजिए!'
        self.description_kazakh = 'Төмендегі тізбек диаграммасында A-дан G-ге дейін белгіленген жеті резистордың орналасуы көрсетілген. Берілген диаграммаға сүйене отырып, құрамында E, F және G резисторлары бар бөліктің эквивалентті кедергісін оммен (Ω) есептеңіз!'
        self.description_swahili = 'Mchoro wa sakiti hapa chini unaonyesha mpangilio wa vikinza saba vilivyopewa majina A hadi G. Kulingana na mchoro uliotolewa, kokotoa ukinzani sawa (equivalent resistance) wa sehemu iliyo na vikinza E, F, na G katika omu (Ω)!'

class Phy050_multi(Phy050):
    def __init__(self):
        super().__init__()
        self.description_chinese = '下方的电路图展示了标记为A到G的七个电阻器的排列。根据提供的图，计算包含电阻器A、B、C和D的部分的等效电阻 (以欧姆 (Ω) 为单位)！'
        self.description_arabic = 'يوضح مخطط الدائرة ترتيبًا لسبع مقاومات مسماة من A إلى G. احسب المقاومة المكافئة للجزء الذي يحتوي على المقاومات A و B و C و D بوحدة الأوم (Ω).'
        self.description_hindi = 'नीचे दिए गए परिपथ आरेख में A से G तक अंकित सात प्रतिरोधों की व्यवस्था दर्शाई गई है। दिए गए आरेख के आधार पर, प्रतिरोध A, B, C और D वाले भाग का समतुल्य प्रतिरोध ohms (Ω) में ज्ञात कीजिए!'
        self.description_kazakh = 'Төмендегі тізбек диаграммасында A-дан G-ге дейін белгіленген жеті резистордың орналасуы көрсетілген. Берілген диаграммаға сүйене отырып, құрамында A, B, C және D резисторлары бар бөліктің эквивалентті кедергісін оммен (Ω) есептеңіз!'
        self.description_swahili = 'Mchoro wa sakiti hapa chini unaonyesha mpangilio wa vikinza saba vilivyopewa majina A hadi G. Kulingana na mchoro uliotolewa, kokotoa ukinzani sawa (equivalent resistance) wa sehemu iliyo na vikinza A, B, C, na D katika omu (Ω)!'

class Phy051_multi(Phy051):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个电路有两个串联的电阻器。电压表连接在R2两端 (假设为理想电表)。电流表上显示的电流是多少？(_) A'
        self.description_arabic = 'تحتوي دائرة على مقاومتين على التوالي. يُوصل فولتميتر عبر R2 (بافتراض أجهزة قياس مثالية). ما شدة التيار التي يشير إليها الأميتر؟ (_) A'
        self.description_hindi = 'एक परिपथ में दो प्रतिरोधक श्रृंखला में जुड़े हैं। R2 के सिरों पर एक वोल्टमीटर लगाया गया है (आदर्श मीटर मान लें)। एमीटर पर प्रदर्शित धारा क्या है? (_) A'
        self.description_kazakh = 'Тізбекте тізбектей жалғанған екі резистор бар. Вольтметр R2-ге қосылған (идеал құралдар деп есептеңіз). Амперметр қандай ток күшін көрсетеді? (_) A'
        self.description_swahili = 'Sakiti ina vikinza viwili katika mfululizo (series). Voltamita imeunganishwa kwenye ncha za R2 (chukulia mita kamilifu). Je, ni kiasi gani cha mkondo kinachoonyeshwa kwenye amita? (_) A'

class Phy052_multi(Phy052):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，两个电阻器并联。电流表测量总电流。电流表的读数是多少？(_) A'
        self.description_arabic = 'مقاومتان موصولتان على التوازي كما هو موضح. يقيس الأميتر التيار الكلي. ما قراءة الأميتر؟ (_) A'
        self.description_hindi = 'चित्र में दिखाए अनुसार दो प्रतिरोधक समानांतर क्रम में जुड़े हैं। एमीटर कुल धारा मापता है। एमीटर का मान क्या है? (_) A'
        self.description_kazakh = 'Көрсетілгендей, екі резистор параллель жалғанған. Амперметр жалпы ток күшін өлшейді. Амперметр көрсеткіші қандай? (_) A'
        self.description_swahili = 'Vikinza viwili vimeunganishwa sambamba (parallel) kama inavyoonyeshwa. Amita inapima jumla ya mkondo (total current). Je, ni kiasi gani cha mkondo kinachoonyeshwa kwenye amita? (_) A'

class Phy053_multi(Phy053):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个分压器使用了一个固定电阻器和一个NTC热敏电阻。电压表测量热敏电阻两端的 V_out。计算 V_out。(_) V'
        self.description_arabic = 'يُستخدم مجزئ جهد يتكون من مقاومة ثابتة ومقاومة حرارية من نوع NTC. يقيس الفولتميتر الجهد $V_{out}$ عبر المقاومة الحرارية. احسب $V_{out}$. (_) V'
        self.description_hindi = 'एक पोटेंशियल डिवाइडर में एक स्थिर प्रतिरोधक और एक NTC थर्मिस्टर का उपयोग किया जाता है। वोल्टमीटर थर्मिस्टर के सिरों पर V_out मापता है। V_out की गणना करें। (_) V'
        self.description_kazakh = 'Потенциал бөлгіш тұрақты резистор мен NTC термисторын пайдаланады. Вольтметр термистордағы V_out кернеуін өлшейді. V_out мәнін есептеңіз. (_) V'
        self.description_swahili = 'Kigawa uwezo (potential divider) kinatumia kinza kisichobadilika na themista ya NTC. Voltamita inapima V_out kwenye ncha za themista hiyo. Kokotoa V_out. (_) V'

class Phy054_multi(Phy054):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中显示了一块条形磁铁，其上有一个P点 。哪个箭头 (A、B、C或D) 表示P点的磁场方向？(_)'
        self.description_arabic = 'يوضح الشكل مغناطيسًا شريطيًا ونقطة P. أي سهم (A أو B أو C أو D) يبين اتجاه المجال المغناطيسي عند النقطة P؟ (_)'
        self.description_hindi = 'एक चुंबक को बिंदु P के साथ दर्शाया गया है। कौन सा तीर (A, B, C, या D) बिंदु P पर चुंबकीय क्षेत्र की दिशा दर्शाता है? (_)'
        self.description_kazakh = 'Жолақ магнит P нүктесімен көрсетілген. Қай көрсеткі (A, B, C немесе D) P нүктесіндегі магнит өрісінің бағытын көрсетеді? (_)'
        self.description_swahili = 'Sumaku mche (bar magnet) imeonyeshwa pamoja na nukta P. Ni mshale upi (A, B, C, au D) unaoonyesha uelekeo wa ugasumaku (magnetic field) kwenye nukta P? (_)'

class Phy055_multi(Phy055):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一根导线放置在磁场中。图中给出了电流方向。哪个箭头 (A、B、C或D) 表示导线受力方向？(_)'
        self.description_arabic = 'يوضح الشكل سلكًا موضوعًا في مجال مغناطيسي، واتجاه التيار معطى. أي سهم (A أو B أو C أو D) يبين اتجاه القوة المؤثرة على السلك؟ (_)'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक तार को चुंबकीय क्षेत्र में रखा गया है। चित्र में धारा की दिशा दी गई है। कौन सा तीर (A, B, C, या D) तार पर लगने वाले बल की दिशा दर्शाता है? (_)'
        self.description_kazakh = 'Сым көрсетілгендей магнит өрісіне орналастырылған. Ток бағыты диаграммада берілген. Қай көрсеткі (A, B, C немесе D) сымға әсер ететін күштің бағытын көрсетеді? (_)'
        self.description_swahili = 'Waya umewekwa kwenye ugasumaku (magnetic field) kama inavyoonyeshwa. Uelekeo wa mkondo (current) umetolewa kwenye mchoro. Je, ni mshale upi (A, B, C, au D) unaoonyesha uelekeo wa kani (force) kwenye waya? (_)'

class Phy056_multi(Phy056):
    def __init__(self):
        super().__init__()
        self.description_chinese = '变压器的初级和次级匝数如图所示。给出了初级电压。假设为理想变压器。计算次级电压。(_) V'
        self.description_arabic = 'يوضح الشكل محولًا بعدد لفات ابتدائية وثانوية معطى. الفولتية الابتدائية معلومة. بافتراض محول مثالي، احسب الفولتية الثانوية. (_) V'
        self.description_hindi = 'चित्र में दिखाए गए अनुसार एक ट्रांसफार्मर के प्राथमिक और द्वितीयक टर्न दिए गए हैं। प्राथमिक वोल्टेज दिया गया है। एक आदर्श ट्रांसफार्मर मान लें। द्वितीयक वोल्टेज की गणना करें। (_) V'
        self.description_kazakh = 'Трансформатордың біріншілік және екіншілік орамдары көрсетілген. Біріншілік кернеу берілген. Идеал трансформатор деп есептеңіз. Екіншілік кернеуді есептеңіз. (_) V'
        self.description_swahili = 'Transfoma ina mizunguko ya msingi na ya upili iliyoonyeshwa. Volteji ya msingi imetolewa. Chukulia kuwa ni transfoma kamilifu. Kokotoa volteji ya upili. (_) V'

class Phy057_multi(Phy057):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图像显示了放射源的校正计数率随时间的变化。求该同位素的半衰期。(_) s'
        self.description_arabic = 'يوضح الشكل معدل العد المصحح لمصدر مشع مع الزمن. أوجد عمر النصف للنظير. (_) s'
        self.description_hindi = 'ग्राफ समय के साथ रेडियोधर्मी स्रोत की संशोधित गणना दर को दर्शाता है। समस्थानिक की अर्ध-आयु ज्ञात कीजिए। (_) s'
        self.description_kazakh = 'График уақыт бойынша радиоактивті көздің түзетілген санау жылдамдығын көрсетеді. Изотоптың жартылай ыдырау периодын анықтаңыз. (_) s'
        self.description_swahili = 'Grafu inaonyesha kiwango cha mionzi kilichosahihishwa (corrected count rate) cha chanzo cha mionzi baada ya muda fulani. Bainisha nusumaisha (half-life) ya isotopu hiyo. (_) s'

class Phy058_multi(Phy058):
    def __init__(self):
        super().__init__()
        self.description_chinese = '在一个放射源和探测器之间使用不同的吸收体进行测试。探测器的读数如图所示。发射的是哪种类型的辐射？\nA: alpha  B: beta  C: gamma  (_)'
        self.description_arabic = 'يتم اختبار مصدر مشع باستخدام مواد ماصة مختلفة بين المصدر والكاشف. القراءات موضحة. ما نوع الإشعاع المنبعث؟\nA: ألفا   B: بيتا   C: جاما   (_)'
        self.description_hindi = 'एक रेडियोधर्मी स्रोत का परीक्षण स्रोत और डिटेक्टर के बीच विभिन्न अवशोषकों का उपयोग करके किया जाता है। डिटेक्टर के मान दर्शाए गए हैं। किस प्रकार का विकिरण उत्सर्जित होता है?\nA: अल्फा B: बीटा C: गामा (_)'
        self.description_kazakh = 'Радиоактивті көз бен детектор арасына әртүрлі жұтқыштар қойылып сыналады. Детектор көрсеткіштері берілген. Қандай сәулелену түрі шығарылады?\nA: альфа   B: бета   C: гамма   (_)'
        self.description_swahili = 'Chanzo cha mionzi kinapimwa kwa kutumia vifyonzaji (absorbers) tofauti kati ya chanzo na kitambuzi. Onyesho la kitambuzi limeonyeshwa. Ni aina gani ya mionzi inayozalishwa?\nA: alfa   B: beta   C: gama   (_)'

class Phy059_multi(Phy059):
    def __init__(self):
        super().__init__()
        self.description_chinese = '电流表显示电流 (A) 流动了一段时间 (t) (数值如图所示)。计算转移的电荷量。请以库仑 (C) 为单位给出答案。\n转移的电荷量 = (_) C'
        self.description_arabic = 'يوضح الأميتر شدة تيار (A) لمدة زمنية (t) كما في الشكل. احسب الشحنة المنقولة. أعطِ إجابتك بوحدة الكولوم (C).\nالشحنة المنقولة = (_) C'
        self.description_hindi = 'एक एमीटर किसी निश्चित समय (t) के लिए प्रवाहित धारा (A) दर्शाता है (मान चित्र में दिखाए गए हैं)। स्थानांतरित चार्ज की गणना कीजिए। अपना उत्तर coulombs (C) में दीजिए।\nस्थानांतरित चार्ज = (_) C'
        self.description_kazakh = 'Амперметр белгілі бір уақыт (t) бойы өткен ток күшін (A) көрсетеді (мәндер суретте берілген). Тасымалданған зарядты есептеңіз. Жауапты кулонмен (Кл) беріңіз. Тасымалданған заряд = (_) Кл'
        self.description_swahili = 'Amita inaonyesha mkondo ($A$) unaopita kwa muda fulani ($t$) (thamani zimeonyeshwa kwenye picha). Kokotoa chaji iliyohamishwa. Toa jibu lako katika kulombu (C).\nChaji iliyohamishwa = (_) C'

class Phy060_multi(Phy060):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一辆小车行驶了一段测量的距离并记录了所用时间 (数值如图所示)。\n计算速度 v 以及 v 的绝对不确定度。\n答案格式：v = (_) ± (_) m s⁻¹'
        self.description_arabic = 'تتحرك عربة لمسافة معلومة ويُقاس الزمن كما في الشكل.\nاحسب السرعة $v$ وعدم اليقين المطلق فيها.\nتنسيق الإجابة: v = (_) ± (_) m s⁻¹'
        self.description_hindi = 'एक ट्रॉली एक निश्चित दूरी तय करती है और तय किया गया समय रिकॉर्ड किया जाता है (मान चित्र में दिखाए गए हैं)।\nगति v और v में निरपेक्ष अनिश्चितता की गणना कीजिए।\nउत्तर का प्रारूप: v = (_) ± (_) m s⁻¹'
        self.description_kazakh = 'Арба өлшенген қашықтықты жүріп өтеді және кеткен уақыт тіркеледі (мәндер суретте көрсетілген).\nЖылдамдықты v және v-дің абсолютті қателігін есептеңіз.\nЖауап форматы: v = (_) ± (_) m s⁻¹'
        self.description_swahili = 'Toroli linasafiri umbali uliopimwa na muda uliochukuliwa unarekodiwa (thamani zimeonyeshwa kwenye picha).\nKokotoa kasi $v$ na utovu wa uhakika kamili (absolute uncertainty) katika $v$.\nMuundo wa jibu: v = (_) ± (_) m s⁻¹'

class Phy061_multi(Phy061):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，两个力 (F₁ 和 F₂) 作用于一点。\n计算合力的大小。\n合力大小 = (_) N'
        self.description_arabic = 'تؤثر قوتان (F₁ و F₂) عند نقطة كما هو موضح في الشكل.\nاحسب مقدار القوة المحصلة.\nالمحصلة = (_) N'
        self.description_hindi = 'चित्र में दर्शाए अनुसार दो बल (F₁ और F₂) एक बिंदु पर कार्य करते हैं।\nपरिणामी बल का परिमाण ज्ञात कीजिए।\nपरिणामी परिमाण = (_) N'
        self.description_kazakh = 'Екі күш (F₁ және F₂) суретте көрсетілгендей бір нүктеге әсер етеді.\nҚорытқы күштің модулін есептеңіз.\nҚорытқы модуль = (_) N'
        self.description_swahili = 'Kani mbili ($F_1$ na $F_2$) zinatenda kwenye nukta moja kama inavyoonyeshwa kwenye picha.\nKokotoa ukubwa wa kani tokeo (resultant force).\nUkubwa wa kani tokeo = (_) N'

class Phy062_multi(Phy062):
    def __init__(self):
        super().__init__()
        self.description_chinese = '位移-时间图像展示了质点的运动。求A点和B点之间的速度。(_) m s⁻¹'
        self.description_arabic = 'يوضح الشكل منحنى الإزاحة-الزمن لحركة جسيم. أوجد السرعة المتجهة بين النقطتين A و B. (_) m s⁻¹'
        self.description_hindi = 'विस्थापन-समय ग्राफ एक कण की गति को दर्शाता है। बिंदु A और B के बीच वेग ज्ञात कीजिए। (_) m s⁻¹'
        self.description_kazakh = 'Орын ауыстыру–уақыт графигі бөлшектің қозғалысын көрсетеді. А және В нүктелері арасындағы жылдамдықты анықтаңыз. (_) m s⁻¹'
        self.description_swahili = 'Grafu ya usogeo na muda (displacement–time graph) inaonyesha mwendo wa chembe. Bainisha velositi (velocity) kati ya nukta A na B. (_) m s⁻¹'

class Phy063_multi(Phy063):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'速度-时间图像展示了质点在前 {self.t} s 内的运动。求这段时间内的位移。(_) m'
        self.description_arabic = f'يوضح الشكل منحنى السرعة-الزمن لحركة جسيم خلال أول {self.t} s. أوجد الإزاحة خلال هذه الفترة. (_) m'
        self.description_hindi = f'वेग-समय ग्राफ पहले {self.t} s के लिए एक कण की गति को दर्शाता है। इस समय में विस्थापन ज्ञात कीजिए। (_) m'
        self.description_kazakh = f'Жылдамдық–уақыт графигі алғашқы {self.t} s ішіндегі бөлшектің қозғалысын көрсетеді. Осы уақыт ішіндегі орын ауыстыруды анықтаңыз. (_) m'
        self.description_swahili = f'Grafu ya velositi na muda (velocity–time graph) inaonyesha mwendo wa chembe kwa sekunde {self.t} za mwanzo. Bainisha usogeo (displacement) ndani ya muda huu. (_) m'

class Phy064_multi(Phy064):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个球从高度 h 处由静止落下。忽略空气阻力。取 g = 9.81 m s⁻²。计算它刚要触地前的速度。(_) m s⁻¹'
        self.description_arabic = 'تُسقط كرة من السكون من ارتفاع h كما هو موضح في الشكل. أهمل مقاومة الهواء، واعتبر g = 9.81 m s⁻². احسب السرعة قبل اصطدامها بالأرض مباشرة. (_) m s⁻¹'
        self.description_hindi = 'चित्र में दिखाए अनुसार, एक गेंद को h ऊँचाई से विराम अवस्था से गिराया जाता है। वायु प्रतिरोध को अनदेखा करें। g = 9.81 m s⁻² लें। ज़मीन से टकराने से ठीक पहले गेंद की गति की गणना करें। (_) m s⁻¹'
        self.description_kazakh = 'Шар суретте көрсетілгендей h биіктіктен тыныштық күйінен тасталады. Ауа кедергісін ескермеңіз. g = 9.81 m s⁻² деп алыңыз. Оның жерге соғылар алдындағы жылдамдығын есептеңіз. (_) m s⁻¹'
        self.description_swahili = 'Mpira unadondoshwa kutoka hali tuli (from rest) kutoka kimo $h$ kama inavyoonyeshwa kwenye picha. Puuza ukinzani wa hewa. Chukua $g = 9.81$ m s⁻². Kokotoa kasi muda mfupi kabla ya kugusa ardhi. (_) m s⁻¹'

class Phy065_multi(Phy065):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'质量为 {self.m:.2f} kg 的小车以初速度 {self.u} m s⁻¹ 作直线运动。一个合力作用在运动方向上。力随时间的变化如图所示。\n求力脉冲结束时小车的速度。(_) m s⁻¹'
        self.description_arabic = f'عربة كتلتها {self.m:.2f} kg تتحرك في خط مستقيم بسرعة ابتدائية {self.u} m s⁻¹. تؤثر قوة محصلة في اتجاه الحركة وتتغير مع الزمن كما هو موضح في الشكل.\nأوجد سرعة العربة عند نهاية نبضة القوة. (_) m s⁻¹'
        self.description_hindi = f'{self.m:.2f} kg द्रव्यमान वाली एक ट्रॉली {self.u} m s⁻¹ के प्रारंभिक वेग से सीधी रेखा में गति कर रही है। गति की दिशा में एक परिणामी बल कार्य कर रहा है। बल समय के साथ ग्राफ में दर्शाए अनुसार परिवर्तित होता है।\nबल पल्स के अंत में ट्रॉली का वेग ज्ञात कीजिए। (_) m s⁻¹'
        self.description_kazakh = f'Массасы {self.m:.2f} kg арба бастапқы {self.u} m s⁻¹ жылдамдықпен түзу сызық бойымен қозғалады. Қозғалыс бағытында қорытқы күш әсер етеді. Күш графикте көрсетілгендей уақытқа байланысты өзгереді.\nКүш импульсінің соңындағы арбаның жылдамдығын анықтаңыз. (_) m s⁻¹'
        self.description_swahili = f'Toroli lenye masi ya {self.m:.2f} kg linasonga katika mstari ulionyooka likiwa na kasi ya awali ya {self.u} m s⁻¹. Kani tokeo (resultant force) inatenda katika uelekeo wa mwendo. Kani hiyo inabadilika kulingana na muda kama inavyoonyeshwa kwenye grafu.\nBainisha kasi ya toroli mwishoni mwa pigo la kani (force pulse). (_) m s⁻¹'

class Phy066_multi(Phy066):
    def __init__(self):
        super().__init__()
        self.description_chinese = '在光滑水平面上，两个木块通过一根轻质不可伸长的细绳相连。如图所示，一个水平力作用在右侧木块上。\n施加的力及两木块的质量如图所示。\n求细绳中的张力。(_) N'
        self.description_arabic = 'كتلتان متصلتان بخيط خفيف غير قابل للتمدد على سطح أفقي أملس. تؤثر قوة أفقية على الكتلة اليمنى كما هو موضح في الشكل.\nالقوة المطبقة وكتلتا الكتلتين موضحتان.\nأوجد الشد في الخيط. (_) N'
        self.description_hindi = 'एक चिकनी क्षैतिज सतह पर दो ब्लॉक एक हल्की, अविस्तारणीय डोरी से जुड़े हुए हैं।चित्र में दिखाए अनुसार दाहिने ब्लॉक पर एक क्षैतिज बल लगाया गया है।\nचित्र में लगाए गए बल और दोनों ब्लॉकों के द्रव्यमान दिखाए गए हैं।\nडोरी में तनाव ज्ञात कीजिए। (_) N'
        self.description_kazakh = 'Екі блок тегіс горизонтал бетте жеңіл созылмайтын жіппен жалғанған.Көрсетілгендей оң жақтағы блокқа горизонтал күш түсіріледі.\nТүсірілген күш пен екі блоктың массалары суретте көрсетілген.\nЖіптің керілуін анықтаңыз. (_) N'
        self.description_swahili = 'Matofali mawili yameunganishwa na kamba nyepesi isiyonyumbulika (light inextensible string) kwenye uso mlalo nyororo. Kani mlalo inatenda kwenye tofali la upande wa kulia kama inavyoonyeshwa.\nKani inayotumika na masi za matofali yote mawili zimeonyeshwa kwenye picha. Bainisha mvutano (tension) katika kamba hiyo. (_) N'

class Phy067_multi(Phy067):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个人站在电梯里的体重秤上。电梯向 {self.dir_text} 加速 (m 和 a 均在图中显示)。取 g = 9.81 m s⁻²。\n求体重秤的读数 (法向反作用力)。(_) N'
        self.description_arabic = f'شخص يقف على ميزان داخل مصعد. يتسارع المصعد {self.dir_text} (قيمتا m و a موضحتان في الشكل). اعتبر g = 9.81 m s⁻².\nأوجد قراءة الميزان (رد الفعل العمودي). (_) N'
        self.description_hindi = f'एक व्यक्ति लिफ्ट में तराजू पर खड़ा है। लिफ्ट {self.dir_text} त्वरण से चल रही है (चित्र में m और a दोनों दर्शाए गए हैं)। g = 9.81 m s⁻² लें।\nतराजू का मान (सामान्य प्रतिक्रिया) ज्ञात कीजिए। (_) N'
        self.description_kazakh = f'Адам лифт ішіндегі таразыда тұр. Лифт {self.dir_text} үдейді (m және a мәндері суретте көрсетілген). g = 9.81 m s⁻² деп алыңыз.\nТаразының көрсеткішін (қалыпты реакция күшін) анықтаңыз. (_) N'
        self.description_swahili = f'Mtu anasimama kwenye mzani ndani ya lifti. Lifti inachapuka kuelekea {self.dir_text} (masi $m$ na mchapuko $a$ zimeonyeshwa kwenye picha). Chukua $g = 9.81$ m s⁻².\nBainisha onyesho la mzani (kani mshiko ya kawaida). (_) N'

class Phy068_multi(Phy068):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'两辆小车在光滑水平轨道上运动。{self.motion_text} 并与最初静止的另一辆小车发生碰撞。碰撞后两辆小车粘在一起 (如图)。\n求碰撞后瞬间的共同速度。(_) m s⁻¹'
        self.description_arabic = f'تتحرك عربتان على مسار أفقي أملس. {self.motion_text} وتصطدم بالعربة الأخرى الساكنة. تلتصق العربتان معًا بعد التصادم كما هو موضح.\nأوجد السرعة المشتركة مباشرة بعد التصادم. (_) m s⁻¹'
        self.description_hindi = f'दो ट्रॉलियाँ एक समतल क्षैतिज पटरी पर चल रही हैं। {self.motion_text} एक ट्रॉली दूसरी ट्रॉली से टकराती है, जो आरंभ में स्थिर है। टक्कर के बाद दोनों ट्रॉलियाँ आपस में चिपक जाती हैं (चित्र देखें)।\nटक्कर के तुरंत बाद उनकी सामान्य गति ज्ञात कीजिए। (_) m s⁻¹'
        self.description_kazakh = f'Екі арба тегіс горизонтал жолда қозғалады. Ол {self.motion_text} және бастапқыда тыныштықта тұрған екінші арбамен соқтығысады. Соқтығысқаннан кейін арбалар бірге жабысып қозғалады (диаграмманы қараңыз).\nСоқтығысудан кейінгі бірден ортақ жылдамдықты анықтаңыз. (_) m s⁻¹'
        self.description_swahili = f'Toroli mawili yanasonga kwenye njia mlalo nyororo (smooth horizontal track). {self.motion_text} na kugongana na toroli lingine ambalo awali lilikuwa tuli. Toroli hizo hushikana baada ya mgongano (tazama mchoro).\nBainisha kasi ya pamoja (common speed) mara tu baada ya mgongano. (_) m s⁻¹'

class Phy069_multi(Phy069):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'总质量为 {self.m_total} kg 的物体最初静止在光滑水平面上。它爆炸成A和B两个碎片，向相反方向运动 (见图)。\n碎片的质量和已知速度如图所示。\n求另一碎片的速度和方向。\n答案格式：向 (左/右)(_) m s⁻¹ '
        self.description_arabic = f'جسم كتلته الكلية {self.m_total} kg في البداية ساكن على سطح أفقي أملس. ينفجر إلى شظيتين A و B تتحركان في اتجاهين متعاكسين كما هو موضح.\nكتلتا الشظيتين والسرعة المعطاة موضحتان.\nأوجد سرعة واتجاه الشظية الأخرى.\nتنسيق الإجابة: (_) m s⁻¹ إلى (اليسار/اليمين)'
        self.description_hindi = f'एक वस्तु जिसका कुल द्रव्यमान {self.m_total} kg है, प्रारंभ में एक चिकनी क्षैतिज सतह पर स्थिर है। यह दो टुकड़ों A और B में विलीन हो जाती है जो विपरीत दिशाओं में गति करते हैं (चित्र देखें)।\nचित्र में टुकड़ों के द्रव्यमान और ज्ञात गति दर्शाई गई है।\nदूसरे टुकड़े की गति और दिशा ज्ञात कीजिए।\nउत्तर प्रारूप: (_) m s⁻¹ से (बाएँ/दाएँ)'
        self.description_kazakh = f'Жалпы массасы {self.m_total} kg дене бастапқыда тегіс горизонтал бетте тыныштықта тұрады. Ол қарама-қарсы бағытта қозғалатын екі А және В жарықшақтарына жарылады (диаграмманы қараңыз).\nЖарықшақтардың массалары мен белгілі жылдамдық диаграммада көрсетілген.\nЕкінші жарықшақтың жылдамдығы мен бағытын анықтаңыз.\nЖауап форматы: (_) m s⁻¹ (солға/оңға)'
        self.description_swahili = f'Gimba (object) lenye jumla ya masi ya {self.m_total} kg awali lilikuwa tuli kwenye uso mlalo nyororo. Linalipuka na kuwa vipande viwili A na B ambavyo vinasonga katika mielekeo mkabala (tazama mchoro).\nMasi za vipande na kasi inayojulikana zimeonyeshwa kwenye mchoro.\nBainisha kasi na uelekeo wa kipande kingine.\nMuundo wa jibu: (_) m s⁻¹ kuelekea (kushoto/kulia)'

class Phy070_multi(Phy070):
    def __init__(self):
        super().__init__()
        self.description_chinese = "两辆小车在光滑水平面上运动并在一点碰撞，然后粘在一起。\n小车A和B的质量、方向和速度均在图中显示。求结合后小车的速度及其方向 (+x 轴上方的角度)。\n速度 = (_) m s⁻¹, 角度 = (_)°。答案格式: (_) m s⁻¹ 在 (_)°"
        self.description_arabic = "تتحرك عربتان على سطح أفقي أملس وتصطدمان ثم تلتصقان.\nكتلتا العربتين A و B واتجاهاتهما وسرعتاهما موضحة في الشكل.\nأوجد سرعة العربة الناتجة واتجاهها (زاوية أعلى المحور x الموجب).\nالسرعة = (_) m s⁻¹، الزاوية = (_)°.\nتنسيق الإجابة: (_) m s⁻¹ عند (_)°"
        self.description_hindi = "दो ट्रॉलियाँ एक समतल क्षैतिज सतह पर चलती हैं और एक बिंदु पर टकराती हैं, फिर आपस में चिपक जाती हैं।\nचित्र में ट्रॉली A और B दोनों के द्रव्यमान, दिशाएँ और गति दर्शाई गई हैं।संयुक्त ट्रॉली की गति और उसकी दिशा (+x अक्ष के ऊपर का कोण) ज्ञात कीजिए।\nSpeed = (_) m s⁻¹, angle = (_)°। उत्तर प्रारूप: (_) m s⁻¹ पर (_)°"
        self.description_kazakh = "Екі арба тегіс горизонтал бетте қозғалып, бір нүктеде соқтығысады да, бір-біріне жабысады.\nА және В арбаларының массалары, бағыттары және жылдамдықтары диаграммада көрсетілген.Біріккен арбаның жылдамдығын және оның бағытын (+x осінен жоғары бұрыш) анықтаңыз.\nЖылдамдық = (_) m s⁻¹, бұрыш = (_)°. Жауап форматы: (_) m s⁻¹ бұрышы (_)°"
        self.description_swahili = "Matoroli mawili yanasonga kwenye uso mlalo nyororo na kugongana kwenye nukta moja, kisha kushikana. Masi, uelekeo, na kasi za Toroli A na B zimeonyeshwa kwenye mchoro. Bainisha kasi ya matoroli yaliyoungana na uelekeo wake (pembe juu ya mhimili wa +x).\nKasi = (_) m s⁻¹, pembe = (_)°. Muundo wa jibu: (_) m s⁻¹ katika (_)°"

class Phy071_multi(Phy071):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根轻质水平梁在 P 点处铰接。力和距离如图所示。\n求使梁保持平衡所需力 F 的大小。\nF = (_) N'
        self.description_arabic = 'عارضة أفقية خفيفة ترتكز عند النقطة P. القوى والمسافات موضحة في الشكل.\nأوجد مقدار القوة F اللازمة لإبقاء العارضة في حالة اتزان.\nF = (_) N'
        self.description_hindi = 'एक हल्की क्षैतिज बीम बिंदु P पर टिकी हुई है। बलों और दूरियों को चित्र में दर्शाया गया है।\nबीम को संतुलन में रखने के लिए आवश्यक बल F का परिमाण ज्ञात कीजिए।\nF = (_) N'
        self.description_kazakh = 'Жеңіл горизонтал арқалық P нүктесінде тірелген. Күштер мен қашықтықтар диаграммада көрсетілген.\nАрқалықты тепе-теңдікте ұстап тұру үшін қажетті Ғ күшінің модулін анықтаңыз.\nF = (_) N'
        self.description_swahili = 'Boriti nyepesi ya mlalo imeshikiliwa kwenye egemeo (pivot) P. Kani na umbali vimeonyeshwa kwenye mchoro.\nBainisha ukubwa wa kani F inayohitajika ili kuweka boriti hiyo katika msawazo (equilibrium).\nF = (_) N'

class Phy072_multi(Phy072):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，两个大小相等且方向相反的力形成一个力偶。所有所需数值均在图中显示。\n求以 ? 表示的缺失物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'قوتان متساويتان ومتضادتان تُكوِّنان ازدواجًا كما هو موضح. جميع القيم المطلوبة معطاة.\nأوجد الكمية المجهولة المشار إليها بـ ?.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'दो बराबर और विपरीत बल मिलकर एक युग्म बनाते हैं जैसा कि चित्र में दिखाया गया है। सभी आवश्यक मान आरेख में दर्शाए गए हैं।\n? द्वारा इंगित लुप्त राशि ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Екі бірдей және қарама-қарсы күш көрсетілгендей қос күшті құрайды. Барлық қажетті мәндер диаграммада көрсетілген.\n? белгісімен көрсетілген жетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Kani mbili sawa zinazoelekea pande mkabala zinaunda kapo (couple) kama inavyoonyeshwa. Thamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana kilichoonyeshwa na alama ya ?. Toa jibu lako katika muundo unaofaa.'

class Phy073_multi(Phy073):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个小圆环在三个共面力的作用下处于平衡状态。质量和角度如图所示。\n取 g = 9.81 m s⁻²。求缺失的张力。\n请以适当的形式给出答案。'
        self.description_arabic = 'حلقة صغيرة في حالة اتزان تحت تأثير ثلاث قوى مستوية كما هو موضح. الكتلة والزوايا معطاة.\nاعتبر g = 9.81 m s⁻². أوجد الشد المجهول.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'चित्र में दर्शाए अनुसार एक छोटी रिंग तीन समतलीय बलों के अधीन संतुलन में है। द्रव्यमान और कोण चित्र में दर्शाए गए हैं।\ng = 9.81 m s⁻² लें। लुप्त तनाव ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दें।'
        self.description_kazakh = 'Кішкентай сақина көрсетілгендей үш компланарлық күштің әсерінен тепе-теңдікте. Масса мен бұрыштар диаграммада көрсетілген.\ng = 9.81 m s⁻² деп алыңыз. Жетіспейтін керілуді анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Pete ndogo ipo katika msawazo (equilibrium) chini ya kani tatu bapa-moja (coplanar forces) kama inavyoonyeshwa. Masi na pembe zimeonyeshwa kwenye mchoro.\nChukua $g = 9.81$ m s⁻². Bainisha mvutano (tension) unaokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy074_multi(Phy074):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根均匀的梁在 A 和 B 的支撑下处于平衡状态。载荷和距离如图所示。\n求缺失的竖直反作用力。\n请以适当的形式给出答案。'
        self.description_arabic = 'عارضة منتظمة في حالة اتزان مسندة عند A و B. الأحمال والمسافات موضحة.\nأوجد رد الفعل العمودي المجهول.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एकसमान बीम संतुलन में है और A तथा B पर समर्थित है। भार और दूरियाँ चित्र में दर्शाई गई हैं।\nलुप्त ऊर्ध्वाधर प्रतिक्रिया ज्ञात कीजिए।\nअपना उत्तर उचित प्रारूप में दीजिए।'
        self.description_kazakh = 'Біртекті арқалық А және В нүктелеріне тіреліп, тепе-теңдікте орналасқан. Жүктемелер мен қашықтықтар диаграммада көрсетілген.\nЖетіспейтін вертикаль реакция күшін анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Boriti sawia (uniform beam) ipo katika msawazo ikiwa imeshikiliwa kwenye nukta A na B. Mizigo na umbali vimeonyeshwa kwenye mchoro.\nBainisha kani mshiko ya wima (vertical reaction) inayokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy075_multi(Phy075):
    def __init__(self):
        super().__init__()
        self.description_chinese = '两点 A 和 B 位于液体中。所有所需数值均在图中显示。\n取 g = 9.81 m s⁻²。求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'نقطتان A و B داخل سائل، وجميع القيم المطلوبة موضحة.\nاعتبر g = 9.81 m s⁻². أوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'दो बिंदु A और B एक द्रव में स्थित हैं। सभी आवश्यक मान आरेख में दर्शाए गए हैं।\ng = 9.81 m s⁻² लें। लुप्त मान ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'А және В екі нүктесі сұйықтық ішінде орналасқан. Барлық қажетті мәндер диаграммада көрсетілген.\ng = 9.81 m s⁻² деп алыңыз. Жетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Nukta mbili A na B zipo ndani ya kimiminika. Thamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nChukua $g = 9.81$ m s⁻². Bainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy076_multi(Phy076):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个立方体完全浸没在液体中，并由一根轻绳拉住保持静止。相关数值在图中显示。\n取 g = 9.81 m s⁻²。求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'مكعب مغمور بالكامل في سائل ومثبت بخيط خفيف كما هو موضح. القيم المعطاة موضحة.\nاعتبر g = 9.81 m s⁻². أوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक घन पूरी तरह से द्रव में डूबा हुआ है और एक हल्की डोरी से स्थिर रखा गया है, जैसा कि चित्र में दिखाया गया है। संबंधित मान आरेख में दर्शाए गए हैं।\ng = 9.81 m s⁻² लें। लुप्त राशि ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Куб көрсетілгендей сұйықтыққа толығымен батырылған және жеңіл жіппен тыныштықта ұсталып тұр. Тиісті мәндер диаграммада көрсетілген.\ng = 9.81 m s⁻² деп алыңыз. Жетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Mchemraba umezamishwa kabisa ndani ya kimiminika na kushikiliwa katika hali tuli kwa kamba nyepesi kama inavyoonyeshwa. Thamani husika zimeonyeshwa kwenye mchoro.\nChukua $g = 9.81$ m s⁻². Bainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy077_multi(Phy077):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个木块在粗糙水平面上运动。质量 (m)、施加的力 (F)、摩擦力 (f) 以及移动距离 (s) 均在图中显示。木块由静止开始运动。\n求木块移动图示距离后的速度。\nv = (_) m s⁻¹'
        self.description_arabic = 'كتلة تتحرك على سطح أفقي خشن. الكتلة (m) والقوة المطبقة (F) وقوة الاحتكاك (f) والمسافة (s) موضحة. تبدأ من السكون.\nأوجد سرعتها بعد قطع المسافة.\nv = (_) m s⁻¹'
        self.description_hindi = 'एक ब्लॉक एक खुरदरी क्षैतिज सतह पर गति करता है। द्रव्यमान (m), लगाया गया बल (F), घर्षण बल (f) और तय की गई दूरी (s) चित्र में दर्शाई गई हैं। ब्लॉक विराम अवस्था से चलना शुरू करता है।\nदर्शाई गई दूरी तय करने के बाद ब्लॉक की गति ज्ञात कीजिए।\nv = (_) m s⁻¹'
        self.description_kazakh = 'Блок бұдырлы горизонтал бетте қозғалады. Масса (m), түсірілген күш (F), үйкеліс күші (f) және жүрілген қашықтық (s) диаграммада көрсетілген. Блок тыныштық күйінен бастап қозғалады.\nКөрсетілген қашықтықты жүріп өткеннен кейінгі блоктың жылдамдығын анықтаңыз.\nv = (_) m s⁻¹'
        self.description_swahili = 'Tofali linasonga kwenye uso mlalo mkwaru (rough horizontal surface). Masi ($m$), kani inayotumika ($F$), kani ya msuguano ($f$) na umbali uliosogezwa ($s$) zimeonyeshwa kwenye mchoro. Tofali linaanza kutoka hali tuli.\nBainisha kasi ya tofali baada ya kusonga umbali ulioonyeshwa.\nv = (_) m s⁻¹'

class Phy078_multi(Phy078):
    def __init__(self):
        super().__init__()
        self.description_chinese ='一台电机以恒定速度垂直提升一个重物。相关数值如图所示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'محرك يرفع حمولة رأسيًا بسرعة ثابتة. القيم المعطاة موضحة.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक मोटर भार को स्थिर गति से ऊर्ध्वाधर रूप से उठाती है। संबंधित मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Қозғалтқыш жүкті вертикаль бағытта тұрақты жылдамдықпен көтереді. Тиісті мәндер сызбада көрсетілген. Белгісіз шаманы анықтаңыз. Жауапты тиісті түрде (өлшем бірлікте) көрсетіңіз.'
        self.description_swahili = 'Mota inainua mzigo kiwima (vertically) kwa kasi mfululizo (constant speed). Thamani husika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy079_multi(Phy079):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一辆汽车在平坦道路上行驶，受恒定阻力作用停下。相关数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'سيارة تتحرك على طريق أفقي وتتوقف تحت تأثير قوة كبح ثابتة. القيم المعطاة موضحة.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक कार समतल सड़क पर चल रही है और एक स्थिर ब्रेकिंग बल द्वारा रुक जाती है। संबंधित मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Автомобиль тегіс жолмен қозғалып келеді және тұрақты тежегіш күштің әсерінен тоқтайды. Тиісті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Gari linasonga kwenye barabara tambarare (level road) na kusimamishwa (brought to rest) kwa kani mfululizo ya breki (constant braking force). Thamani husika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy080_multi(Phy080):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个小球被竖直向上抛出。相关数值在图中显示。\n忽略空气阻力。求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'كرة صغيرة تُقذف رأسيًا إلى أعلى. القيم المعطاة موضحة.\nأهمل مقاومة الهواء.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक छोटी गेंद को लंबवत ऊपर की ओर प्रक्षेपित किया जाता है। संबंधित मान आरेख में दर्शाए गए हैं।\nवायु प्रतिरोध को अनदेखा करें। लुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Кішкентай шар вертикаль жоғары лақтырылды. Тиісті мәндер диаграммада көрсетілген.\nАуа кедергісін ескермеңіз. Жетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Mpira mdogo unarushwa kiwima kwenda juu (projected vertically upwards). Thamani husika zimeonyeshwa kwenye mchoro.\nPuuza ukinzani wa hewa. Bainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy081_multi(Phy081):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一辆小车在光滑轨道上从 A 运动到 B。质量、g 以及所有所需数值均在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'عربة تتحرك من A إلى B على مسار أملس كما هو موضح. الكتلة و g وجميع القيم المعطاة موضحة.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक गाड़ी A से B तक एक चिकने ट्रैक पर चलती है। द्रव्यमान g और सभी आवश्यक मान चित्र में दर्शाए गए हैं।\nलुप्त मान ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Арба көрсетілгендей тегіс жолмен А-дан В-ға дейін қозғалады. Масса, g және барлық қажетті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Toroli linasonga kutoka A hadi B kwenye njia nyororo (smooth track) kama inavyoonyeshwa. Masi, $g$, na thamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy082_multi(Phy082):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中展示了合力随位移 x 从 0 到 s 的变化情况。一辆质量为 m 的小车在光滑水平面上由静止开始运动，所有所需数值均在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يوضح الشكل كيف تتغير القوة المحصلة مع الإزاحة x من 0 إلى s. عربة كتلتها m تبدأ من السكون على سطح أفقي أملس.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'ग्राफ दर्शाता है कि परिणामी बल विस्थापन x के साथ 0 से s तक कैसे बदलता है। m द्रव्यमान वाली एक ट्रॉली एक चिकनी क्षैतिज सतह पर विराम अवस्था से चलना शुरू करती है, और सभी आवश्यक मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'График қорытқы күштің 0-ден s-ке дейінгі x орын ауыстыруына байланысты қалай өзгеретінін көрсетеді. Массасы m арба тегіс горизонтал бетте тыныштық күйінен бастап қозғалады, және барлық қажетті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Grafu inaonyesha jinsi kani tokeo (resultant force) inavyobadilika kulingana na usogeo $x$ kutoka $0$ hadi $s$. Toroli lenye masi $m$ linaanza kutoka hali tuli (rest) kwenye uso mlalo nyororo, na thamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy083_multi(Phy083):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根导线受拉力作用。所有所需数值均在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'سلك في حالة شد. جميع القيم المطلوبة موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक तार तनाव में है। सभी आवश्यक मान चित्र में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Сым керілуде. Барлық қажетті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Waya upo katika mvutano (tension). Thamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy084_multi(Phy084):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根金属丝被拉伸。原始长度和伸长量均在图中显示。\n求金属丝的拉伸应变。\n应变 = (_)'
        self.description_arabic = 'يتم شد سلك. الطول الأصلي والاستطالة موضحان في الشكل.\nأوجد الانفعال الشدي في السلك.\nالانفعال = (_)'
        self.description_hindi = 'एक तार को खींचा जाता है। चित्र में मूल लंबाई और खिंचाव दिखाया गया है।\nतार में उत्पन्न तन्य विकृति ज्ञात कीजिए।\nstrain = (_)'
        self.description_kazakh = 'Сым созылған. Бастапқы ұзындығы мен ұзаруы диаграммада көрсетілген.\nСымдағы салыстырмалы ұзаруды анықтаңыз.\nсалыстырмалы ұзару = (_)'
        self.description_swahili = 'Waya umevutwa. Urefu wa asili (original length) na ongezeko la urefu (extension) vimeonyeshwa kwenye mchoro.\nBainisha mnyumbuko wa mvutano (tensile strain) kwenye waya.\nmnyumbuko = (_)'

class Phy085_multi(Phy085):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中展示弹簧的力-伸长量。该弹簧在所示范围内遵循胡克定律。\n求弹簧常数 k。\nk = (_) N m⁻¹'
        self.description_arabic = 'يوضح الشكل منحنى القوة–الاستطالة لنابض. يخضع النابض لقانون هوك ضمن النطاق الموضح.\nأوجد ثابت النابض k.\nk = (_) N m⁻¹'
        self.description_hindi = 'एक स्प्रिंग का बल-विस्तार ग्राफ दिखाया गया है। स्प्रिंग दिखाए गए क्षेत्र में हुक (Hooke) के नियम का पालन करती है।\nस्प्रिंग स्थिरांक k ज्ञात कीजिए।\nk = (_) N m⁻¹'
        self.description_kazakh = 'Серіппе үшін күш–ұзару графигі көрсетілген. Серіппе көрсетілген аралықта Гук заңына бағынады.\nk қатаңдық коэффициентін анықтаңыз.\nk = (_) N m⁻¹'
        self.description_swahili = 'Grafu ya kani dhidi ya ongezeko la urefu (force–extension graph) kwa ajili ya springi imeonyeshwa. Springi inatii sheria ya Hooke katika kiwango kilichoonyeshwa.\nBainisha kigezo cha springi (spring constant) $k$.\n$k$ = (_) N m⁻¹'

class Phy086_multi(Phy086):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根弹簧遵循胡克定律。施加的力和伸长量均在图中显示。\n求弹簧中储存的弹性势能。\nE = (_) J'
        self.description_arabic = 'نابض يخضع لقانون هوك. القوة المطبقة والاستطالة موضحتان في الشكل.\nأوجد طاقة الوضع المرونية المخزنة في النابض.\nE = (_) J'
        self.description_hindi = 'एक स्प्रिंग हुक (Hooke) के नियम का पालन करती है। लगाए गए बल और विस्तार को चित्र में दर्शाया गया है।\nस्प्रिंग में संचित प्रत्यास्थ स्थितिज ऊर्जा ज्ञात कीजिए।\nE = (_) J'
        self.description_kazakh = 'Серіппе Гук заңына бағынады. Түсірілген күш пен ұзару диаграммада көрсетілген.\nСеріппеде жинақталған серпімділік потенциалдық энергиясын анықтаңыз.\nE = (_) J'
        self.description_swahili = 'Springi inatii sheria ya Hooke (Hooke’s law). Kani inayotumika na ongezeko la urefu (extension) vimeonyeshwa kwenye mchoro.\nBainisha nishati uwezo ya unyumbufu (elastic potential energy) iliyohifadhiwa kwenye springi.\nE = (_) J'

class Phy087_multi(Phy087):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示为金属丝的力-伸长量图像。金属丝被加载，然后沿着图中所示的线卸载。\n求卸载后金属丝的永久伸长量。\n永久伸长量 = (_) mm'
        self.description_arabic = 'يوضح الشكل منحنى القوة–الاستطالة لسلك. يتم تحميل السلك ثم تفريغه على المسار الموضح.\nأوجد الاستطالة الدائمة بعد التفريغ.\nالاستطالة الدائمة = (_) mm'
        self.description_hindi = 'एक तार का बल-विस्तार ग्राफ दिखाया गया है। तार पर भार डाला जाता है और फिर दिखाए गए रेखा के अनुदिश भार हटा दिया जाता है।\nभार हटाने के बाद तार का स्थायी विस्तार ज्ञात कीजिए।\npermanent extension = (_) mm'
        self.description_kazakh = 'Сым үшін күш–ұзару графигі көрсетілген. Сым жүктеліп, содан кейін көрсетілген сызық бойымен жүктемеден босатылады.\nЖүктемеден босатқаннан кейінгі сымның қалдық ұзаруын анықтаңыз.\nқалдық ұзару = (_) mm'
        self.description_swahili = 'Grafu ya kani dhidi ya ongezeko la urefu (force–extension graph) kwa ajili ya waya imeonyeshwa. Waya unaongezewa kani (loaded) na kisha kuondolewa kani (unloaded) kando ya mstari ulioonyeshwa.\nBainisha ongezeko la kudumu la urefu (permanent extension) la waya baada ya kuondolewa kani.\nongezeko la kudumu = (_) mm'

class Phy088_multi(Phy088):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图示为一列行波。图中给出了 f、λ 和 v 三个物理量中的两个。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يوضح الشكل موجة تقدمية. معطى اثنان من الكميات f و λ و v.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक प्रगामी तरंग दर्शायी गई है। आरेख में दो मात्राएं f, λ और v दी गई हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Жүгірме толқын көрсетілген. Диаграммада f, λ және v шамаларының екеуі берілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Wimbi endelevu (progressive wave) limeonyeshwa. Viwango viwili kati ya $f, \lambda$ na $v$ vimetolewa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy089_multi(Phy089):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图示为一行波的瞬时波形。A 和 B 两点的相关数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يوضح الشكل لقطة لموجة تقدمية. القيم المتعلقة بالنقطتين A و B معطاة.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक प्रगामी तरंग का स्नैपशॉट दिखाया गया है। आरेख में बिंदु A और B के लिए प्रासंगिक मान दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Жүгірме толқынның лездік суреті көрсетілген. А және В нүктелеріне қатысты мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Picha mnato (snapshot) ya wimbi endelevu imeonyeshwa. Thamani husika kwa nukta A na B zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy090_multi(Phy090):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个声源发出频率为 f₀ 的声音。声源如图所示地运动，而观察者静止。\n所有所需数值均在图中显示。\n求观察者听到的频率。\nf = (_) Hz'
        self.description_arabic = 'مصدر صوت يصدر موجات بتردد f₀ ويتحرك كما هو موضح، بينما المراقب ثابت.\nجميع القيم المعطاة موضحة.\nأوجد التردد الذي يسمعه المراقب.\nf = (_) Hz'
        self.description_hindi = 'एक ध्वनि स्रोत f₀ आवृत्ति की ध्वनि उत्सर्जित करता है। स्रोत चित्रानुसार गतिमान है और प्रेक्षक स्थिर है।\nसभी आवश्यक मान आरेख में दर्शाए गए हैं।\nप्रेक्षक द्वारा सुनी गई आवृत्ति ज्ञात कीजिए।\nf = (_) Hz'
        self.description_kazakh = 'Дыбыс көзі f₀ жиілігімен дыбыс шығарады. Көз көрсетілгендей қозғалады, ал бақылаушы тыныштықта.\nБарлық қажетті мәндер диаграммада көрсетілген.\nБақылаушы еститін жиілікті анықтаңыз.\nf = (_) Hz'
        self.description_swahili = 'Chanzo cha sauti kinatoa sauti yenye masafa (frequency) ya $f_0$. Chanzo kinasonga kama inavyoonyeshwa na mtazamaji yupo tuli (stationary).\nThamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha masafa yanayosikiwa na mtazamaji.\n$f$ = (_) Hz'

class Phy091_multi(Phy091):
    def __init__(self):
        super().__init__()
        self.description_chinese = '声源静止，观察者如图所示运动。\n所有所需数值均在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'مصدر صوت ثابت ومراقب يتحرك كما هو موضح.\nجميع القيم المعطاة موضحة.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'ध्वनि स्रोत स्थिर है और प्रेक्षक चित्रानुसार गति कर रहा है।\nसभी आवश्यक मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Дыбыс көзі тыныштықта, ал бақылаушы көрсетілгендей қозғалады.\nБарлық қажетті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Chanzo cha sauti kipo tuli (stationary) na mtazamaji anasonga kama inavyoonyeshwa.\nThamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy092_multi(Phy092):
    def __init__(self):
        super().__init__()
        self.description_chinese = '声源和观察者如图所示相向运动。\n所有所需数值均在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'مصدر صوت ومراقب يتحركان نحو بعضهما كما هو موضح.\nجميع القيم المعطاة موضحة.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक ध्वनि स्रोत और एक प्रेक्षक एक दूसरे की ओर गति कर रहे हैं।\nसभी आवश्यक मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Дыбыс көзі мен бақылаушы көрсетілгендей бір-біріне қарай қозғалады.\nБарлық қажетті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Chanzo cha sauti na mtazamaji (observer) vinasonga kuelekeana kama inavyoonyeshwa. Thamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy093_multi(Phy093):
    def __init__(self):
        super().__init__()
        self.description_chinese = '非偏振光穿过两个偏振片。所有所需数值均在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يمر ضوء غير مستقطب عبر مستقطبين.\nجميع القيم المعطاة موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'अध्रुवीकृत प्रकाश दो पोलरॉइड से होकर गुजरता है। सभी आवश्यक मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Поляризацияланбаған жарық екі поляроид арқылы өтеді. Барлық қажетті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Mwanga usio kutubishwa (unpolarised light) unapita kwenye polaroidi mbili. Thamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy094_multi(Phy094):
    def __init__(self):
        super().__init__()
        self.description_chinese = '在两端固定的拉伸弦上形成驻波。图案和数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'تتكون موجة موقوفة على وتر مشدود مثبت من الطرفين. النمط والقيم موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'दोनों सिरों से स्थिर एक खिंची हुई डोरी पर एक स्थिर तरंग उत्पन्न होती है। पैटर्न और मान चित्र में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Екі шеті бекітілген созылған ішекте тұрғын толқын пайда болды. Көрініс пен мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Wimbi msimamo (stationary wave) limeundwa kwenye kamba iliyovutwa na kufungwa kwenye ncha zote mbili. Muundo na thamani zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy095_multi(Phy095):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根管子一端封闭，另一端开口。驻波图案和数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'أنبوب مغلق من أحد طرفيه ومفتوح من الطرف الآخر. نمط الموجة الموقوفة والقيم موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक नली एक सिरे से बंद और दूसरे सिरे से खुली है। स्थिर तरंग पैटर्न और मान चित्र में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Құбырдың бір шеті жабық, ал екінші шеті ашық. Тұрғын толқын көрінісі мен мәндері диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Mrija umefungwa kwenye ncha moja na kufunguliwa kwenye ncha nyingine (closed at one end). Muundo wa wimbi msimamo (stationary-wave pattern) na thamani zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy096_multi(Phy096):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根两端固定的弦上产生驻波。波形和数值如图所示。\n求缺失的量。\n请以适当的形式给出答案。'
        self.description_arabic = 'تتكون موجة موقوفة على وتر مثبت من الطرفين. النمط والقيم موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'दोनों सिरों से बंधी डोरी पर एक स्थिर तरंग उत्पन्न होती है। पैटर्न और मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Екі ұшы бекітілген жіпте тұрғын толқын пайда болады. Толқын кескіні мен мәндері сызбада көрсетілген.\nБелгісіз шаманы анықтаңыз.\nЖауапты тиісті түрде көрсетіңіз.'
        self.description_swahili = 'Wimbi msimamo (stationary wave) limezalishwa kwenye kamba iliyofungwa kwenye ncha zote mbili. Muundo na thamani zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy097_multi(Phy097):
    def __init__(self):
        super().__init__()
        self.description_chinese = '光穿过双缝并在屏幕上形成干涉图样。\n相关数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يمر الضوء عبر شق مزدوج مكوِّنًا نمط تداخل على شاشة.\nالقيم المعطاة موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'प्रकाश एक दोहरी स्लिट से होकर गुजरता है और स्क्रीन पर एक व्यतिकरण पैटर्न बनाता है।\nसंबंधित मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Жарық қос саңылаудан өтіп, экранда интерференциялық көрініс түзеді.\nТиісті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Mwanga unapita kwenye mianya miwili (double slit) na kuunda muundo wa mwingiliano (interference pattern) kwenye skrini.\nThamani husika zimeonyeshwa kwenye mchoro. Bainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy098_multi(Phy098):
    def __init__(self):
        super().__init__()
        self.description_chinese = '两个相干光源 S1 和 S2 发出同相位的波。P 点是最大 (相长) 干涉点。\n相关数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'مصدران مترابطان S1 و S2 يصدران موجات في نفس الطور. النقطة P تمثل تداخلًا أعظميًا (بنّاءً).\nالقيم المعطاة موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'दो सुसंगत स्रोत S1 और S2 समान कला में तरंगें उत्सर्जित करते हैं। बिंदु P अधिकतम (रचनात्मक) व्यतिकरण का बिंदु है।\nप्रासंगिक मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Екі когерентті S1 және S2 көзі фазалас толқындар шығарады. P нүктесі – максимум (конструктивті) интерференция нүктесі.\nТиісті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Vyanzo viwili shirikishi S1 na S2 vinatoa mawimbi katika awamu sawa. Nukta P ni nukta ya mwingiliano jenga wa juu zaidi.\nThamani husika zimeonyeshwa kwenye mchoro. Bainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy099_multi(Phy099):
    def __init__(self):
        super().__init__()
        self.description_chinese = '单色光入射到衍射光栅上。数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'ضوء أحادي اللون يسقط على محزوز حيود.\nالقيم موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एकवर्णी प्रकाश एक विवर्तन ग्रेटिंग पर आपतित होता है। मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Монохроматты жарық дифракциялық торға түседі. Мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Mwanga wa rangi moja (monochromatic light) unatua kwenye kiwavu cha mchepusho (diffraction grating). Thamani zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy100_multi(Phy100):
    def __init__(self):
        super().__init__()
        self.description_chinese = '单色光入射到衍射光栅上。数值在图中显示。\n求可观察到的最高阶主极大及其对应角度。\nn_max = (_),  θ_max = (_)°。答案格式 (两个值用逗号分隔): (_), (_)'
        self.description_arabic = 'ضوء أحادي اللون يسقط على محزوز حيود.\nالقيم موضحة في الشكل.\nأوجد أعلى رتبة عظمى يمكن رصدها والزاوية المقابلة.\nn_max = (_)، θ_max = (_)°.\nتنسيق الإجابة: (_)، (_)'
        self.description_hindi = 'एकवर्णी प्रकाश एक विवर्तन ग्रेटिंग पर आपतित होता है। मान आरेख में दर्शाए गए हैं।\nप्रेक्षित किए जा सकने वाले उच्चतम कोटि के अधिकतम मान और संगत कोण ज्ञात कीजिए।\nn_max = (_),  θ_max = (_)°। उत्तर प्रारूप (अल्पविराम से अलग किए गए 2 मान): (_), (_)'
        self.description_kazakh = 'Монохроматты жарық дифракциялық торға түседі. Мәндер диаграммада көрсетілген.\nБақылауға болатын ең жоғарғы реттік максимумды және оған сәйкес бұрышты анықтаңыз.\nn_max = (_),  θ_max = (_)°. Жауап форматы (үтірмен бөлінген 2 мән): (_), (_)'
        self.description_swahili = 'Mwanga wa rangi moja unatua kwenye kiwavu cha mchepusho (diffraction grating). Thamani zimeonyeshwa kwenye mchoro.\nBainisha mpangilio wa juu kabisa wa mng’ao (highest order maximum) unaoweza kuonekana na pembe inayolingana nao.\nn_max = (_),  θ_max = (_)°. Muundo wa jibu (thamani 2 zilizotenganishwa kwa mkato): (_), (_)'

class Phy101_multi(Phy101):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'恒定电流在直导线中流动。P点是导线上的一个标记点。\n图中所示的数值与通过P点的电荷量有关。\n求所需物理量。\n{self.blank}'
        self.description_arabic = f'يتدفق تيار ثابت في سلك مستقيم. النقطة P موضحة على السلك.\nالقيم المعطاة تتعلق بالشحنة المارة عبر النقطة P.\nأوجد الكمية المطلوبة.\n{self.blank}'
        self.description_hindi = f'एक सीधी तार में स्थिर धारा प्रवाहित हो रही है। बिंदु P तार पर अंकित एक बिंदु है।\nआरेख में दर्शाए गए मान बिंदु P से गुजरने वाले आवेश से संबंधित हैं।\nआवश्यक मात्रा ज्ञात कीजिए।\n{self.blank}'
        self.description_kazakh = f'Түзу сым бойымен тұрақты ток жүреді. P нүктесі – сымдағы белгіленген нүкте.\nДиаграммада көрсетілген мәндер P нүктесі арқылы өтетін зарядқа қатысты.\nҚажетті шаманы анықтаңыз.\n{self.blank}'
        self.description_swahili = f'Mkondo thabiti (steady current) unapita kwenye waya ulionyooka. Nukta P ni nukta iliyotiwa alama kwenye waya.\nThamani zilizoonyeshwa kwenye mchoro zinahusiana na chaji inayopita nukta P.\nBainisha kiwango kinachohitajika.\n{self.blank}'

class Phy102_multi(Phy102):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了导体的电流随时间变化的规律。\n所有相关数值均在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يوضح الشكل منحنى التيار مقابل الزمن لموصل.\nجميع القيم المعطاة موضحة.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'ग्राफ में चालक के लिए समय के सापेक्ष धारा दर्शाई गई है।\nआरेख में सभी प्रासंगिक मान दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Графикте өткізгіш үшін токтың уақытқа тәуелділігі көрсетілген.\nБарлық қажетті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Grafu inaonyesha mkondo (current) dhidi ya muda (time) kwa kipitishio. Thamani zote husika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy103_multi(Phy103):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个器件连接在电路中。通过该器件的电流及其两端的电势差如图所示。\n求所需物理量。\n{self.blank}'
        self.description_arabic = f'جهاز موصل في دائرة كهربائية. التيار المار فيه وفرق الجهد عبره موضحان في الشكل.\nأوجد الكمية المطلوبة.\n{self.blank}'
        self.description_hindi = f'एक उपकरण को परिपथ में जोड़ा गया है। उपकरण से प्रवाहित धारा और उसके सिरों पर विभवांतर चित्र में दर्शाए गए हैं।\nआवश्यक मात्रा ज्ञात कीजिए।\n{self.blank}'
        self.description_kazakh = f'Құрылғы тізбекке қосылған. Құрылғы арқылы өтетін ток пен ондағы потенциалдар айырымы диаграммада көрсетілген.\nҚажетті шаманы анықтаңыз.\n{self.blank}'
        self.description_swahili = f'Kifaa kimeunganishwa kwenye sakiti (circuit). Mkondo unaopita kwenye kifaa na tofauti ya potenshalo (potential difference) inayokivuka zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachohitajika.\n{self.blank}'

class Phy104_multi(Phy104):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'电荷通过一段电势差移动。数值在图中显示。\n求所需的量。\n{self.blank}'
        self.description_arabic = f'تتحرك شحنة عبر فرق جهد. القيم موضحة في الشكل.\nأوجد الكمية المطلوبة.\n{self.blank}'
        self.description_hindi = f'एक चार्ज विभवांतर से होकर गति करता है। मान आरेख में दर्शाए गए हैं।\nआवश्यक मात्रा ज्ञात कीजिए।\n{self.blank}'
        self.description_kazakh = f'Заряд потенциалдар айырымы арқылы қозғалады. Мәндер диаграммада көрсетілген.\nҚажетті шаманы анықтаңыз.\n{self.blank}'
        self.description_swahili = f'Chaji inasonga kupitia tofauti ya potenshalo (potential difference). Thamani zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachohitajika.\n{self.blank}'

class Phy105_multi(Phy105):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根均匀导线的尺寸如图所示，并给出了其电阻。\n求导线材料的电阻率。\nρ = (_) Ω m'
        self.description_arabic = 'سلك منتظم أبعاده موضحة في الشكل ومقاومته معطاة.\nأوجد المقاومية النوعية لمادة السلك.\nρ = (_) Ω m'
        self.description_hindi = 'चित्र में दर्शाए गए आयामों वाले एक समान तार का प्रतिरोध दिया गया है।\nतार की प्रतिरोधकता ज्ञात कीजिए।\nρ = (_) Ω m'
        self.description_kazakh = 'Біртекті сымның өлшемдері диаграммада көрсетілген және оның кедергісі берілген.\nСым материалының меншікті кедергісін анықтаңыз.\nρ = (_) Ω m'
        self.description_swahili = 'Waya wenye umbo sare (uniform wire) una vipimo vilivyoonyeshwa kwenye mchoro na upinzani wake umetolewa.\nBainisha upinzani husika (resistivity) wa nyenzo ya waya.\nρ = (_) Ω m'

class Phy106_multi(Phy106):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根均匀导线的尺寸如图所示，其材料的电阻率为 ρ。\n求导线的电阻。\nR = (_) Ω'
        self.description_arabic = 'سلك منتظم أبعاده موضحة في الشكل، ومقاومية مادته ρ.\nأوجد مقاومة السلك.\nR = (_) Ω'
        self.description_hindi = 'चित्र में दर्शाए गए आयामों वाले एक समान तार का प्रतिरोध ρ ज्ञात कीजिए।\nतार का प्रतिरोध ज्ञात कीजिए।\nR = (_) Ω'
        self.description_kazakh = 'Біртекті сымның өлшемдері диаграммада көрсетілген, ал оның материалының меншікті кедергісі ρ.\nСымның кедергісін анықтаңыз.\nR = (_) Ω'
        self.description_swahili = 'Waya wenye umbo sare (uniform wire) una vipimo vilivyoonyeshwa kwenye mchoro, na nyenzo yake ina upinzani husika (resistivity) ρ.\nBainisha upinzani (resistance) wa waya.\nR = (_) Ω'

class Phy107_multi(Phy107):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了导体的电势差 V 随电流 I 变化的规律。\n所有所需数值均在图中显示。\n求导体的电阻。\nR = (_) Ω'
        self.description_arabic = 'يوضح الشكل فرق الجهد V مقابل التيار I لموصل.\nجميع القيم المعطاة موضحة.\nأوجد مقاومة الموصل.\nR = (_) Ω'
        self.description_hindi = 'ग्राफ में चालक के लिए विभवांतर V और धारा I के बीच का अंतर दर्शाया गया है।\nसभी आवश्यक मान आरेख में दर्शाए गए हैं।\nचालक का प्रतिरोध ज्ञात कीजिए।\nR = (_) Ω'
        self.description_kazakh = 'Графикте өткізгіштің V потенциалдар айырымының I токқа тәуелділігі көрсетілген.\nБарлық қажетті мәндер диаграммада көрсетілген.\nӨткізгіштің кедергісін анықтаңыз.\nR = (_) Ω'
        self.description_swahili = 'Grafu inaonyesha tofauti ya potenshalo (potential difference) V dhidi ya mkondo (current) I kwa kipitishio. Thamani zote zinazohitajika zimeonyeshwa kwenye mchoro.\nBainisha upinzani (resistance) wa kipitishio.\nR = (_) Ω'

class Phy108_multi(Phy108):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个电动势为 E、内阻为 r 的电池为一个电阻供电。电流表和电压表的读数如图所示。\n求电池的内阻。\nr = (_) Ω'
        self.description_arabic = 'خلية ذات قوة دافعة كهربائية E ومقاومة داخلية r تغذي مقاومة.\nقراءات الأميتر والفولتميتر موضحة في الشكل.\nأوجد المقاومة الداخلية للخلية.\nr = (_) Ω'
        self.description_hindi = 'एक सेल जिसका emf E और आंतरिक प्रतिरोध r है, एक प्रतिरोधक को आपूर्ति करता है। एमीटर और वोल्टमीटर के मान दर्शाए गए हैं।\nसेल का आंतरिक प्रतिरोध ज्ञात कीजिए।\nr = (_) Ω'
        self.description_kazakh = 'ЭҚК-і Е және ішкі кедергісі r элемент резисторды қоректендіреді. Амперметр мен вольтметр көрсеткіштері көрсетілген.\nЭлементтің ішкі кедергісін анықтаңыз.\nr = (_) Ω'
        self.description_swahili = 'Seli yenye nguvu ya elektromoti (emf) E na upinzani wa ndani r imeunganishwa na kipingamizi (resistor). Usomaji wa amita na voltamita umeonyeshwa kwenye mchoro.\nBainisha upinzani wa ndani wa seli.\nr = (_) Ω'

class Phy109_multi(Phy109):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个电阻连接在电路中，串联一个电流表，并联一个电压表在电阻两端（假设为理想电表）。\n电表读数如图所示。\n求电阻的阻值。\nR = (_) Ω'
        self.description_arabic = 'مقاومة موصولة في دائرة كهربائية مع أميتر على التوالي وفولتميتر على طرفيها (بافتراض أجهزة قياس مثالية).\nقراءات الأجهزة موضحة في الشكل.\nأوجد قيمة المقاومة.\nR = (_) Ω'
        self.description_hindi = 'एक प्रतिरोधक को एक परिपथ में एमीटर के साथ श्रृंखला में और वोल्टमीटर के साथ प्रतिरोधक के सिरों पर जोड़ा गया है (आदर्श मीटर मान लें)।\nआरेख में मीटर रीडिंग दर्शाई गई हैं।\nप्रतिरोधक का प्रतिरोध ज्ञात कीजिए।\nR = (_) Ω'
        self.description_kazakh = 'Резистор тізбекке амперметрмен тізбектей және вольтметрмен резисторға параллель жалғанған (идеал құралдар деп есептеңіз).\nҚұралдардың көрсеткіштері диаграммада көрсетілген.\nРезистордың кедергісін анықтаңыз.\nR = (_) Ω'
        self.description_swahili = 'Kipingamizi (resistor) kimeunganishwa kwenye sakiti na amita katika mfululizo (in series) na voltamita sambamba na kipingamizi (chukulia mita kamilifu). Usomaji wa mita umeonyeshwa kwenye mchoro.\nBainisha upinzani (resistance) wa kipingamizi.\nR = (_) Ω'

class Phy110_multi(Phy110):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个器件连接在电路中。通过该器件的电流及其两端的电势差如图所示。\n求传递给该器件的功率。\nP = (_) W'
        self.description_arabic = 'جهاز موصول في دائرة كهربائية. التيار المار فيه وفرق الجهد عبره موضحان.\nأوجد القدرة المنتقلة إلى الجهاز.\nP = (_) W'
        self.description_hindi = 'एक उपकरण एक परिपथ में जुड़ा है। उपकरण से प्रवाहित धारा और उसके सिरों पर विभवांतर दर्शाए गए हैं।\nउपकरण को स्थानांतरित पॉवर ज्ञात कीजिए।\nP = (_) W'
        self.description_kazakh = 'Құрылғы тізбекке қосылған. Құрылғы арқылы өтетін ток пен ондағы потенциалдар айырымы көрсетілген.\nҚұрылғыға берілген қуатты анықтаңыз.\nP = (_) W'
        self.description_swahili = 'Kifaa kimeunganishwa kwenye sakiti. Mkondo unaopita kwenye kifaa na tofauti ya potenshalo (potential difference) inayokivuka zimeonyeshwa.\nBainisha nguvu (power) inayopelekwa kwenye kifaa.\nP = (_) W'

class Phy111_multi(Phy111):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个器件在恒定电流和电势差下工作了时间 t。\n求转移的电能。\nW = (_) J'
        self.description_arabic = 'يعمل جهاز بتيار ثابت وفرق جهد ثابت لمدة زمنية t كما هو موضح.\nأوجد الطاقة الكهربائية المنتقلة.\nW = (_) J'
        self.description_hindi = 'एक उपकरण स्थिर धारा और विभवांतर पर समय t तक क्रियाशील रहता है, जैसा कि चित्र में दर्शाया गया है।\nस्थानांतरित विद्युत ऊर्जा ज्ञात कीजिए।\nW = (_) J'
        self.description_kazakh = 'Құрылғы диаграммада көрсетілгендей тұрақты ток пен потенциалдар айырымында t уақыт жұмыс істейді.\nБерілген электр энергиясын анықтаңыз.\nW = (_) J'
        self.description_swahili = 'Kifaa kinafanya kazi kwa mkondo thabiti (steady current) na tofauti ya potenshalo (potential difference) kwa muda t, kama inavyoonyeshwa kwenye mchoro.\nBainisha nishati ya umeme (electrical energy) iliyopelekwa kwenye kifaa.\nW = (_) J'

class Phy112_multi(Phy112):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个内阻为 r 的电池为一个电阻供电。电流表读数和路端电压如图所示。\n求电池的电动势。\nE = (_) V'
        self.description_arabic = 'خلية ذات مقاومة داخلية r تغذي مقاومة.\nقراءة الأميتر وفرق الجهد الطرفي موضحان.\nأوجد القوة الدافعة الكهربائية للخلية.\nE = (_) V'
        self.description_hindi = 'आंतरिक प्रतिरोध r वाली एक सेल एक प्रतिरोधक को आपूर्ति करती है। एमीटर रीडिंग और टर्मिनल p.d. दर्शाए गए हैं।\nसेल का emf ज्ञात कीजिए।\nE = (_) V'
        self.description_kazakh = 'Ішкі кедергісі r элемент резисторды қоректендіреді. Амперметр көрсеткіші мен қысқыштардағы потенциалдар айырымы көрсетілген.\nЭлементтің ЭҚК-ін анықтаңыз.\nE = (_) V'
        self.description_swahili = 'Seli yenye upinzani wa ndani (internal resistance) r imeunganishwa na kipingamizi (resistor). Usomaji wa amita na tofauti ya potenshalo ya vituo (terminal p.d.) vimeonyeshwa.\nBainisha nguvu ya elektromoti (emf) ya seli.\nE = (_) V'

class Phy113_multi(Phy113):
    def __init__(self):
        super().__init__()
        self.description_chinese = '调节可变电阻 (VR) 以改变包含电池的电路中的电流。\n图中显示了 VR 在两个设置下的电流 I 和路端电压 V。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يتم ضبط مقاومة متغيرة (VR) لتغيير التيار في دائرة تحتوي على خلية.\nلقيمتين مختلفتين لـ VR، فإن التيار I وفرق الجهد الطرفي V موضحان.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक परिवर्ती प्रतिरोधक (VR) को समायोजित करके एक सेल युक्त परिपथ में धारा को परिवर्तित किया जाता है।\nVR के दो मानों के लिए, धारा I और टर्मिनल विभवांतर V चित्र में दर्शाए गए है।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Айнымалы резистор (VR) элементі бар тізбектегі токты өзгерту үшін реттеледі.\nVR-дің екі реттелуі үшін I ток пен V қысқыштардағы потенциалдар айырымы диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Kipingamizi kigeugeu (VR) kinabadilishwa ili kubadilisha mkondo kwenye sakiti yenye seli. Kwa mipangilio miwili ya VR, mkondo I na tofauti ya potenshalo ya vituo (terminal p.d.) V zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy114_multi(Phy114):
    def __init__(self):
        super().__init__()
        self.description_chinese = '两个相同的电池串联连接到一个电阻上。每个电池的内阻为 r。\n电阻值和电流如图所示。\n求单个电池的电动势 E。\nE = (_) V'
        self.description_arabic = 'خليتان متماثلتان موصولتان على التوالي بمقاومة، ولكل منهما مقاومة داخلية r.\nقيمة المقاومة والتيار موضحان.\nأوجد القوة الدافعة الكهربائية E لإحدى الخليتين.\nE = (_) V'
        self.description_hindi = 'दो समान सेल एक प्रतिरोधक से श्रृंखला में जुड़े हैं। प्रत्येक सेल का आंतरिक प्रतिरोध r है।\nप्रतिरोधक का मान और धारा चित्र में दर्शाए गए हैं।\nएक सेल का emf E ज्ञात कीजिए।\nE = (_) V'
        self.description_kazakh = 'Екі бірдей элемент резисторға тізбектей жалғанған. Әр элементтің ішкі кедергісі r.\nРезистор мәні мен ток диаграммада көрсетілген.\nБір элементтің E ЭҚК-ін анықтаңыз.\nE = (_) V'
        self.description_swahili = 'Seli mbili zinazofanana zimeunganishwa katika mfululizo (in series) kwenye kipingamizi (resistor). Kila seli ina upinzani wa ndani r.\nThamani ya kipingamizi na mkondo zimeonyeshwa kwenye mchoro.\nBainisha nguvu ya elektromoti (emf) E ya seli moja.\nE = (_) V'

class Phy115_multi(Phy115):
    def __init__(self):
        super().__init__()
        self.description_chinese = '两个相同的电池并联连接到一个电阻上。每个电池的内阻为 r。\n数值如图所示。\n求电阻中的电流。\nI = (_) A'
        self.description_arabic = 'خليتان متماثلتان موصولتان على التوازي بمقاومة، ولكل منهما مقاومة داخلية r.\nالقيم موضحة في الشكل.\nأوجد شدة التيار في المقاومة.\nI = (_) A'
        self.description_hindi = 'दो समान सेल एक प्रतिरोधक के समानांतर जुड़े हुए हैं। प्रत्येक सेल का आंतरिक प्रतिरोध r है।\nमान चित्र में दर्शाए गए हैं।\nप्रतिरोधक में प्रवाहित धारा ज्ञात कीजिए।\nI = (_) A'
        self.description_kazakh = 'Екі бірдей элемент резисторға параллель жалғанған. Әр элементтің ішкі кедергісі r.\nМәндер диаграммада көрсетілген.\nРезистордағы токты анықтаңыз.\nI = (_) A'
        self.description_swahili = 'Seli mbili zinazofanana zimeunganishwa sambamba (in parallel) kwenye kipingamizi (resistor). Kila seli ina upinzani wa ndani r.\nThamani zimeonyeshwa kwenye mchoro.\nBainisha mkondo (current) kwenye kipingamizi.\nI = (_) A'

class Phy116_multi(Phy116):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个热敏电阻 (NTC) 与一个固定电阻串联。电源电压和电压表读数如图所示。\n求热敏电阻的阻值。\nR_T = (_) Ω'
        self.description_arabic = 'مقاومة حرارية (NTC) موصولة على التوالي مع مقاومة ثابتة.\nجهد المصدر وقراءة الفولتميتر موضحان.\nأوجد مقاومة المقاومة الحرارية.\nR_T = (_) Ω'
        self.description_hindi = 'एक थर्मिस्टर (NTC) एक स्थिर प्रतिरोधक के साथ श्रृंखला में जुड़ा हुआ है। आपूर्ति वोल्टेज और वोल्टमीटर रीडिंग दर्शाई गई हैं।\nथर्मिस्टर का प्रतिरोध ज्ञात कीजिए।\nR_T = (_) Ω'
        self.description_kazakh = 'Термистор (NTC) тұрақты резистормен тізбектей жалғанған. Қорек көзінің кернеуі мен вольтметр көрсеткіші көрсетілген.\nТермистордың кедергісін анықтаңыз.\nR_T = (_) Ω'
        self.description_swahili = 'Themista (NTC) imeunganishwa katika mfululizo (in series) na kipingamizi thabiti (fixed resistor). Volteji ya chanzo (supply voltage) na usomaji wa voltamita zimeonyeshwa.\nBainisha upinzani (resistance) wa themista.\nR_T = (_) Ω'

class Phy117_multi(Phy117):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该电路包含两个带有共用电阻的回路。数值如图所示。\n使用基尔霍夫定律，求共用电阻 R3 中的电流。\n电流 = (_) A，方向 = (向上/向下)。答案格式：(_) A 向上/向下'
        self.description_arabic = 'تحتوي الدائرة على حلقتين مع مقاومة مشتركة.\nالقيم موضحة في الشكل.\nباستخدام قوانين كيرشوف، أوجد التيار في المقاومة المشتركة R3.\nالتيار = (_) A، الاتجاه = (لأعلى/لأسفل).\nتنسيق الإجابة: (_) A لأعلى/لأسفل'
        self.description_hindi = 'इस परिपथ में एक साझा प्रतिरोधक के साथ दो लूप हैं। मान चित्र में दर्शाए गए हैं।\nकिरचॉफ (Kirchhoff) के नियमों का उपयोग करके, साझा प्रतिरोधक R3 में प्रवाहित धारा ज्ञात कीजिए।\nCurrent = (_) A, दिशा = (ऊपर की ओर/नीचे की ओर)। उत्तर प्रारूप: (_) A ऊपर की ओर/नीचे की ओर'
        self.description_kazakh = 'Тізбек ортақ резисторы бар екі контурдан тұрады. Мәндер диаграммада көрсетілген.\nКирхгоф заңдарын пайдаланып, ортақ R3 резисторындағы токты анықтаңыз.\nТок = (_) A, бағыты = (жоғары/төмен). Жауап форматы: (_) A жоғары/төмен'
        self.description_swahili = 'Sakiti (circuit) ina mizunguko (loops) miwili yenye kipingamizi cha pamoja R3. Thamani zimeonyeshwa kwenye mchoro.\nKwa kutumia sheria za Kirchhoff, bainisha mkondo (current) kwenye kipingamizi cha pamoja R3.\nMkondo = (_) A, uelekeo = (juu/chini). Muundo wa jibu: (_) A juu/chini'

class Phy118_multi(Phy118):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个电阻与一个并联网络串联。数值如图所示。\n使用基尔霍夫定律，求所要求的电流。\n电流 = (_) A'
        self.description_arabic = 'مقاومة موصولة على التوالي مع شبكة توازي.\nالقيم موضحة في الشكل.\nباستخدام قوانين كيرشوف، أوجد التيار المطلوب.\nالتيار = (_) A'
        self.description_hindi = 'एक प्रतिरोधक समानांतर नेटवर्क के साथ श्रृंखला में जुड़ा हुआ है। मान चित्र में दर्शाए गए हैं।\nकिरचॉफ (Kirchhoff) के नियमों का उपयोग करके, अपेक्षित धारा ज्ञात कीजिए।\nCurrent = (_) A'
        self.description_kazakh = 'Резистор параллель желіге тізбектей жалғанған. Мәндер диаграммада көрсетілген.\nКирхгоф заңдарын пайдаланып, сұралған токты анықтаңыз.\nТок = (_) A'
        self.description_swahili = 'Kipingamizi (resistor) kimeunganishwa katika mfululizo (series) na mzunguko sambamba (parallel network). Thamani zimeonyeshwa kwenye mchoro.\nKwa kutumia sheria za Kirchhoff, bainisha mkondo (current) unaotafutwa.\nMkondo = (_) A'

class Phy119_multi(Phy119):
    def __init__(self):
        super().__init__()
        self.description_chinese = '两个电阻并联。支路电流如图所示。\n使用基尔霍夫定律，求所需物理量。\n答案 = (_)'
        self.description_arabic = 'مقاومتان موصولتان على التوازي.\nتيارات الفروع موضحة في الشكل.\nباستخدام قوانين كيرشوف، أوجد الكمية المطلوبة.\nالإجابة = (_)'
        self.description_hindi = 'दो प्रतिरोधक समानांतर क्रम में जुड़े हैं। शाखा धाराओं को चित्र में दर्शाया गया है।\nकिरचॉफ (Kirchhoff) के नियमों का उपयोग करके आवश्यक मात्रा ज्ञात कीजिए।\nAnswer = (_)'
        self.description_kazakh = 'Екі резистор параллель жалғанған. Таррмақтардағы токтар диаграммада көрсетілген.\nКирхгоф заңдарын пайдаланып, қажетті шаманы анықтаңыз.\nЖауап = (_)'
        self.description_swahili = 'Vipingamizi (resistors) viwili vimeunganishwa sambamba (in parallel). Mikondo ya matawi (branch currents) imeonyeshwa kwenye mchoro.\nKwa kutumia sheria za Kirchhoff, bainisha kiwango kinachohitajika.\nJibu = (_)'

class Phy120_multi(Phy120):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个分压器连接在电源两端。所有数值均在图中显示。\n求所需物理量。\n答案 = (_)'
        self.description_arabic = 'مجزئ جهد موصول عبر مصدر.\nجميع القيم موضحة في الشكل.\nأوجد الكمية المطلوبة.\nالإجابة = (_)'
        self.description_hindi = 'एक आपूर्ति के समानांतर एक विभव विभाजक जुड़ा हुआ है। सभी मान आरेख में दर्शाए गए हैं।\nआवश्यक मात्रा ज्ञात कीजिए।\nAnswer = (_)'
        self.description_kazakh = 'Потенциал бөлгіш қорек көзіне қосылған. Барлық мәндер диаграммада көрсетілген.\nҚажетті шаманы анықтаңыз.\nЖауап = (_)'
        self.description_swahili = 'Kigawanya potenshalo (potential divider) kimeunganishwa kwenye ncha za chanzo. Thamani zote zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachohitajika.\nJibu = (_)'

class Phy121_multi(Phy121):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个质点在水平圆周上作匀速圆周运动。\n相关数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يتحرك جسيم بحركة دائرية منتظمة في دائرة أفقية.\nالقيم المعطاة موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक कण क्षैतिज वृत्त में एकसमान वृत्ताकार गति से गति करता है।\nसंबंधित मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Бөлшек горизонтал шеңбер бойымен бірқалыпты қозғалады.\nТиісті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Chembe inasonga kwa mwendo wa duara sare (uniform circular motion) katika duara mlalo. Thamani husika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy122_multi(Phy122):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个质点作匀速圆周运动。\n如图所示，它在时间间隔 Δt 内从位置 A 移动到位置 B。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يتحرك جسيم بحركة دائرية منتظمة.\nينتقل من الموضع A إلى الموضع B خلال زمن Δt كما هو موضح في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक कण एकसमान वृत्ताकार गति से गति करता है।\nयह चित्र में दिखाए गए समय अंतराल Δt में स्थिति A से स्थिति B तक जाता है।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Бөлшек шеңбер бойымен бірқалыпты қозғалады.\nОл көрсетілгендей Δt уақыт аралығында А нүктесінен (орнынан) В нүктесіне ауысады.\nБелгісіз шаманы анықтаңыз.\nЖауапты тиісті түрде көрсетіңіз.'
        self.description_swahili = 'Chembe inasonga kwa mwendo wa duara sare (uniform circular motion). Inasonga kutoka nafasi A hadi nafasi B katika muda Δt, kama inavyoonyeshwa.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy123_multi(Phy123):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个转盘以恒定速率旋转。\n相关数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يدور قرص بمعدل ثابت.\nالقيم المعطاة موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक टर्नटेबल स्थिर गति से घूमता है।\nसंबंधित मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Айналмалы диск тұрақты жылдамдықпен айналады.\nТиісті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Meza inayozunguka (turntable) inazunguka kwa kiwango thabiti (constant rate). Thamani husika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy124_multi(Phy124):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个质点在水平圆周上以恒定速率运动。\n相关数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يتحرك جسيم بسرعة ثابتة في دائرة أفقية.\nالقيم المعطاة موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक कण क्षैतिज वृत्त में स्थिर गति से गति करता है।\nसंबंधित मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Бөлшек горизонтал шеңбер бойымен тұрақты жылдамдықпен қозғалады.\nТиісті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Chembe inasonga kwa kasi thabiti (constant speed) katika duara mlalo. Thamani husika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy125_multi(Phy125):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个质点作匀速圆周运动。\n相关数值在图中显示。\n求缺失的物理量。\n请以适当的形式给出答案。'
        self.description_arabic = 'يتحرك جسيم بحركة دائرية منتظمة.\nالقيم المعطاة موضحة في الشكل.\nأوجد الكمية المجهولة.\nأعطِ إجابتك بالشكل المناسب.'
        self.description_hindi = 'एक कण एकसमान वृत्ताकार गति से गति करता है।\nसंबंधित मान आरेख में दर्शाए गए हैं।\nलुप्त मात्रा ज्ञात कीजिए।\nअपना उत्तर उचित रूप में दीजिए।'
        self.description_kazakh = 'Бөлшек бірқалыпты шеңбер бойымен қозғалады.\nТиісті мәндер диаграммада көрсетілген.\nЖетіспейтін шаманы анықтаңыз.\nЖауабыңызды сәйкес формада беріңіз.'
        self.description_swahili = 'Chembe inasonga kwa mwendo wa duara sare (uniform circular motion). Thamani husika zimeonyeshwa kwenye mchoro.\nBainisha kiwango kinachokosekana. Toa jibu lako katika muundo unaofaa.'

class Phy126_multi(Phy126):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一辆汽车在倾斜道路的弯道部分行驶。道路有倾角，因此转弯不需要摩擦力。根据图中提供的参数，计算作用在汽车上的向心力。(_) N (示例格式：1250.0)'
        self.description_arabic = 'تسير سيارة في مسار منحني لطريق مائل. صُمم ميل الطريق بحيث لا يلزم احتكاك لإتمام الانعطاف.\nبناءً على المعطيات في الشكل، احسب القوة الجاذبة المركزية المؤثرة على السيارة.\n(_) N (مثال: 1250.0)'
        self.description_hindi = 'एक कार ढलान वाली सड़क के घुमावदार हिस्से पर चल रही है। सड़क को इस प्रकार ढलान दिया गया है कि मोड़ के लिए घर्षण की आवश्यकता नहीं होती है। चित्र में दिए गए मापदंडों के आधार पर, कार पर लगने वाले अभिकेन्द्र बल की गणना कीजिए। (_) N (उदाहरण प्रारूप: 1250.0)'
        self.description_kazakh = 'Автомобиль еңіс жолдың қисық бөлігімен қозғалады. Жол бұрылу үшін үйкеліс қажет болмайтындай еңіспен жасалған. Диаграммада берілген параметрлер негізінде автомобильге әсер ететін центрге тартқыш күшті есептеңіз. (_) N (Мысал форматы: 1250.0)'
        self.description_swahili = 'Gari linasafiri kwenye sehemu iliyopinda ya barabara yenye mwinamo (banked road). Barabara imeinamishwa ili kusiwe na msuguano (friction) unaohitajika kwa mzunguko huo. Kulingana na vigezo vilivyotolewa kwenye mchoro, kokotoa kani ya kuelekea kati (centripetal force) inayofanya kazi kwenye gari. (_) N (Muundo wa mfano: 1250.0)'

class Phy127_multi(Phy127):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据图中提供的质量和万有引力，计算行星和太阳中心之间的距离。(_) m'
        self.description_arabic = 'بناءً على الكتل وقوة الجذب التثاقلي الموضحة في الشكل، احسب المسافة بين مركزي الكوكب والشمس.\n(_) m'
        self.description_hindi = 'आरेख में दिए गए द्रव्यमान और गुरुत्वाकर्षण बल के आधार पर, ग्रह और सूर्य के केंद्र के बीच की दूरी की गणना कीजिए। (_) m'
        self.description_kazakh = 'Диаграммада берілген массалар мен гравитациялық тартылыс күші негізінде планета мен Күннің центрлері арасындағы қашықтықты есептеңіз. (_) m'
        self.description_swahili = 'Kulingana na masi (masses) na kani ya gidatisho (gravitational force) iliyotolewa kwenye mchoro, kokotoa umbali kati ya vitovu vya sayari na jua. (_) m'

class Phy128_multi(Phy128):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一颗卫星在行星表面上方某高度的圆轨道上运行。使用图中提供的参数，计算行星的质量。(_) kg (示例格式：5.97E+24)'
        self.description_arabic = 'قمر صناعي في مدار دائري على ارتفاع فوق سطح كوكب كما هو موضح.\nباستخدام المعطيات في الشكل، احسب كتلة الكوكب.\n(_) kg (مثال: 5.97E+24)'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक उपग्रह ग्रह की सतह से ऊपर एक निश्चित ऊंचाई पर वृत्ताकार कक्षा में है। आरेख में दिए गए मापदंडों का उपयोग करके ग्रह का द्रव्यमान ज्ञात कीजिए। (_) kg (उदाहरण प्रारूप: 5.97E+24)'
        self.description_kazakh = 'Көрсетілгендей, спутник планета бетінен белгілі бір биіктіктегі шеңберлік орбитада орналасқан. Диаграммада берілген параметрлерді пайдаланып, планетаның массасын есептеңіз. (_) kg (Мысал форматы: 5.97E+24)'
        self.description_swahili = 'Satelaiti ipo kwenye obiti duara (circular orbit) katika kimo (altitude) juu ya uso wa sayari kama inavyoonyeshwa. Kwa kutumia vigezo vilivyotolewa kwenye mchoro, kokotoa masi ya sayari. (_) kg (Muundo wa mfano: 5.97E+24)'

class Phy129_multi(Phy129):
    def __init__(self):
        super().__init__()
        self.description_chinese = '使用图中提供的相对密度和引力场强度数据，求月球半径 $r_M$ 与地球半径 $r_E$ 的比值。(_) (示例格式：1 : 4)'
        self.description_arabic = 'باستخدام بيانات الكثافة النسبية وشدة مجال الجاذبية الموضحة في الشكل، أوجد نسبة نصف قطر القمر $r_M$ إلى نصف قطر الأرض $r_E$.\n(_) (مثال: 1 : 4)'
        self.description_hindi = 'आरेख में दिए गए सापेक्ष घनत्व और गुरुत्वाकर्षण क्षेत्र की तीव्रता के आंकड़ों का उपयोग करते हुए, चंद्रमा की त्रिज्या $r_M$ और पृथ्वी की त्रिज्या $r_E$ के अनुपात का पता लगाएं। (_) (उदाहरण प्रारूप: 1 : 4)'
        self.description_kazakh = 'Диаграммада берілген салыстырмалы тығыздық пен гравитациялық өріс кернеулігі мәліметтерін пайдаланып, Ай радиусының $r_M$ Жер радиусына $r_E$ қатынасын анықтаңыз. (_) (Мысал форматы: 1 : 4)'
        self.description_swahili = 'Kwa kutumia data ya msongamano linganishi (relative density) na ukali wa uga wa gidatisho (gravitational field strength) iliyotolewa kwenye mchoro, bainisha uwiano wa rediasi ya Mwezi $r_M$ kwa rediasi ya Dunia $r_E$. (_) (Muundo wa mfano: 1 : 4)'

class Phy130_multi(Phy130):
    def __init__(self):
        super().__init__()
        self.description_chinese = "如图所示，一块岩石位于行星表面上方一定距离处。使用图中提供的行星质量、直径和高度数据，计算此处的引力势。(_) J kg^-1 (示例格式：-4.56E+07)"
        self.description_arabic = 'صخرة تقع على مسافة فوق سطح كوكب كما هو موضح.\nباستخدام بيانات كتلة الكوكب وقطره والارتفاع، احسب جهد الجاذبية عند هذه النقطة.\n(_) J kg^-1 (مثال: -4.56E+07)'
        self.description_hindi = "चित्र में दर्शाए अनुसार एक चट्टान ग्रह की सतह से कुछ दूरी पर स्थित है। चित्र में दिए गए ग्रह के द्रव्यमान, व्यास और ऊँचाई के आंकड़ों का उपयोग करके, इस बिंदु पर गुरुत्वाकर्षण विभव की गणना कीजिए। (_) J kg^-1 (उदाहरण प्रारूप: -4.56E+07)"
        self.description_kazakh = "Көрсетілгендей, тас планета бетінен белгілі бір қашықтықта орналасқан. Диаграммада берілген планетаның массасы, диаметрі және биіктік мәліметтерін пайдаланып, осы нүктедегі гравитациялық потенциалды есептеңіз. (_) J kg^-1 (Мысал форматы: -4.56E+07)"
        self.description_swahili = "Jiwe lipo katika kimo juu ya uso wa sayari kama inavyoonyeshwa. Kwa kutumia data ya masi ya sayari, kipenyo, na kimo iliyotolewa kwenye mchoro, kokotoa potenshalo ya gidatisho (gravitational potential) katika nukta hii. (_) J kg^-1 (Muundo wa mfano: -4.56E+07)"

class Phy131_multi(Phy131):
    def __init__(self):
        super().__init__()
        self.description_chinese = "如图所示，一块岩石位于行星表面上方特定高度。根据图中提供的数据，计算岩石所在位置的引力势。(_) J kg^-1 (示例格式：-7577106.41087628)"
        self.description_arabic = 'صخرة تقع على ارتفاع محدد فوق سطح كوكب كما هو موضح.\nبناءً على المعطيات، احسب جهد الجاذبية عند موضع الصخرة.\n(_) J kg^-1 (مثال: -7577106.41087628)'
        self.description_hindi = "चित्र में दिखाए अनुसार एक चट्टान ग्रह की सतह से एक निश्चित ऊँचाई पर स्थित है। आरेख में दिए गए आंकड़ों के आधार पर, चट्टान की स्थिति पर गुरुत्वाकर्षण विभव की गणना कीजिए। (_) J kg^-1 (उदाहरण प्रारूप: -7577106.41087628)"
        self.description_kazakh = "Көрсетілгендей, тас планета бетінен белгілі бір биіктікте орналасқан. Диаграммада берілген мәліметтер негізінде тас орналасқан нүктедегі гравитациялық потенциалды есептеңіз. (_) J kg^-1 (Мысал форматы: -7577106.41087628)"
        self.description_swahili = "Jiwe lipo kwenye kimo maalum juu ya uso wa sayari kama inavyoonyeshwa. Kulingana na data iliyotolewa kwenye mchoro, kokotoa potenshalo ya gidatisho (gravitational potential) katika nafasi ya jiwe. (_) J kg^-1 (Muundo wa mfano: -7577106.41087628)"

class Phy132_multi(Phy132):
    def __init__(self):
        super().__init__()
        self.description_chinese = "将行星建模为一个孤立的球体。一个物体从行星表面竖直向上抛出，直到达到一定高度。使用图中提供的行星数据，计算此运动过程中引力势的变化量。(_) J kg^-1 (示例格式：44676095.446139514)"
        self.description_arabic = 'يُمثَّل كوكب على أنه كرة معزولة. يُقذف جسم عموديًا من سطح الكوكب حتى يصل إلى ارتفاع معين.\nباستخدام المعطيات في الشكل، احسب التغير في جهد الجاذبية.\n(_) J kg^-1 (مثال: 44676095.446139514)'
        self.description_hindi = "एक ग्रह को पृथक गोले के रूप में दर्शाया गया है। एक वस्तु को ग्रह की सतह से लंबवत रूप से तब तक प्रक्षेपित किया जाता है जब तक वह एक निश्चित ऊँचाई तक नहीं पहुँच जाती। आरेख में दिए गए ग्रह के डेटा का उपयोग करके, इस गति के लिए गुरुत्वाकर्षण स्थितिज में परिवर्तन की गणना कीजिए। (_) J kg^-1 (उदाहरण प्रारूप: 44676095.446139514)"
        self.description_kazakh = "Планета оқшауланған шар ретінде модельденген. Дене планета бетінен белгілі бір биіктікке жеткенше вертикаль жоғары лақтырылады. Диаграммада берілген планета мәліметтерін пайдаланып, осы қозғалыс үшін гравитациялық потенциалдың өзгеруін есептеңіз. (_) J kg^-1 (Мысал форматы: 44676095.446139514)"
        self.description_swahili = "Sayari inachukuliwa kama tufe lililojitenga (isolated sphere). Gimba linarushwa kiwima (vertically) kutoka kwenye uso wa sayari hadi lifikie kimo fulani. Kwa kutumia data ya sayari iliyotolewa kwenye mchoro, kokotoa mabadiliko ya potenshalo ya gidatisho (change in gravitational potential) kwa msogeo huu. (_) J kg^-1 (Muundo wa mfano: 44676095.446139514)"

class Phy133_multi(Phy133):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个刚硬容器内装有氦-4气体。假设氦气表现为理想气体，使用图中所示的参数计算氦原子的方均根 (r.m.s.) 速率。(_) m s^-1 (示例格式：1365.234)'
        self.description_arabic = 'وعاء صلب يحتوي على غاز الهيليوم-4. بافتراض أنه غاز مثالي، استخدم المعطيات في الشكل لحساب سرعة الجذر التربيعي لمتوسط المربعات (r.m.s.) لذرات الهيليوم.\n(_) m s^-1 (مثال: 1365.234)'
        self.description_hindi = 'एक कठोर पात्र में हीलियम-4 गैस भरी है। यह मानते हुए कि हीलियम एक आदर्श गैस की तरह व्यवहार करती है, आरेख में दर्शाए गए मापदंडों का उपयोग करके हीलियम परमाणुओं की वर्गमूल गति (r.m.s.) की गणना कीजिए। (_) m s^-1 (उदाहरण प्रारूप: 1365.234)'
        self.description_kazakh = 'Қатты ыдыста Гелий-4 газы бар. Гелийді идеал газ ретінде қарастырып, диаграммада көрсетілген параметрлерді пайдаланып гелий атомдарының орташа квадраттық (r.m.s.) жылдамдығын есептеңіз. (_) m s^-1 (Мысал форматы: 1365.234)'
        self.description_swahili = 'Chombo kigumu kina gesi ya Heliamu-4 (Helium-4). Kwa kudhani Heliamu inatenda kama gesi bora (ideal gas), tumia vigezo vilivyoonyeshwa kwenye mchoro kukokotoa kasi ya mzizi-wastani wa mraba (r.m.s. speed) ya atomi za heliamu. (_) m s^-1 (Muundo wa mfano: 1365.234)'

class Phy134_multi(Phy134):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个固定体积的刚硬容器内装有理想气体。气体被加热到一个新的温度。根据图中所示的初始和最终状态，计算气体的最终压强。(_) Pa (示例格式：346869.46954977704)'
        self.description_arabic = 'حاوية صلبة ذات حجم ثابت تحتوي على غاز مثالي.\nيُسخَّن الغاز إلى درجة حرارة جديدة. باستخدام الحالتين الابتدائية والنهائية، احسب الضغط النهائي.\n(_) Pa (مثال: 346869.46954977704)'
        self.description_hindi = 'एक स्थिर आयतन वाले कठोर पात्र में आदर्श गैस भरी हुई है। गैस को एक नए तापमान तक गर्म किया जाता है। चित्र में दर्शाई गई प्रारंभिक और अंतिम अवस्थाओं के आधार पर, गैस का अंतिम दाब ज्ञात कीजिए। (_) Pa (उदाहरण प्रारूप: 346869.46954977704)'
        self.description_kazakh = 'Тұрақты көлемді қатты ыдыста идеал газ бар. Газ жаңа температураға дейін қыздырылады. Диаграммада көрсетілген бастапқы және соңғы күйлер негізінде газдың соңғы қысымын есептеңіз. (_) Pa (Мысал форматы: 346869.46954977704)'
        self.description_swahili = 'Chombo kigumu (rigid container) chenye ujazo thabiti (fixed volume) kina gesi bora (ideal gas). Gesi inapashwa moto hadi kufikia halijoto mpya. Kulingana na hali ya awali na ya mwisho iliyoonyeshwa kwenye mchoro, kokotoa kanieneo (pressure) ya mwisho ya gesi. (_) Pa (Muundo wa mfano: 346869.46954977704)'

class Phy135_multi(Phy135):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中显示了两个刚性圆柱形容器 A 和 B，它们由体积可忽略且带有闭合阀门的管子连接。使用图中提供的初始参数，计算打开阀门并在恒温下达到平衡后系统的最终压强。(_) Pa (示例格式：291784.95446401695)'
        self.description_arabic = 'يوضح الشكل أسطوانتين صلبتين A و B متصلتين بأنبوب مهمل الحجم مع صمام مغلق.\nباستخدام المعطيات الابتدائية، احسب الضغط النهائي بعد فتح الصمام والوصول إلى الاتزان عند درجة حرارة ثابتة.\n(_) Pa (مثال: 291784.95446401695)'
        self.description_hindi = 'चित्र में दो कठोर सिलेंडर, A और B, एक बंद वाल्व वाली नगण्य आयतन की नली से जुड़े हुए दिखाए गए हैं। चित्र में दिए गए प्रारंभिक मापदंडों का उपयोग करके, वाल्व खुलने और स्थिर तापमान पर संतुलन स्थापित होने के बाद सिस्टम के अंतिम दबाव की गणना करें। (_) Pa (उदाहरण प्रारूप: 291784.95446401695)'
        self.description_kazakh = 'Диаграммада жабық клапаны бар көлемі ескерілмейтін түтікпен жалғанған екі қатты А және В цилиндрлері көрсетілген. Диаграммада берілген бастапқы параметрлерді пайдаланып, клапан ашылып, тұрақты температурада тепе-теңдік орнағаннан кейінгі жүйенің соңғы қысымын есептеңіз. (_) Pa (Мысал форматы: 291784.95446401695)'
        self.description_swahili = 'Mchoro unaonyesha silinda mbili ngumu, A na B, zilizounganishwa na mrija wenye ujazo unaoweza kupuuzwa ukiwa na vali iliyofungwa. Kwa kutumia vigezo vya awali vilivyotolewa kwenye mchoro, kokotoa kanieneo ya mwisho ya mfumo baada ya vali kufunguliwa na msawazo (equilibrium) kufikiwa katika halijoto thabiti. (_) Pa (Muundo wa mfano: 291784.95446401695)'

class Phy136_multi(Phy136):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个刚硬容器内保持着一定量的理想气体样本。根据图中提供的状态参数，计算气体原子的方均根 (r.m.s.) 速率。(_) m s^-1 (示例格式：709.5655501001263)'
        self.description_arabic = 'تُحفظ عينة من غاز مثالي في حاوية صلبة.\nباستخدام معلمات الحالة، احسب سرعة الجذر التربيعي لمتوسط المربعات (r.m.s.) لذرات الغاز.\n(_) m s^-1 (مثال: 709.5655501001263)'
        self.description_hindi = 'एक आदर्श गैस का नमूना एक कठोर पात्र में रखा गया है। आरेख में दिए गए अवस्था मापदंडों के आधार पर, गैस के परमाणुओं की वर्गमूल औसत का वर्ग (r.m.s.) की गणना कीजिए। (_) m s^-1 (उदाहरण प्रारूप: 709.5655501001263)'
        self.description_kazakh = 'Идеал газ үлгісі қатты ыдыста сақталады. Диаграммада берілген күй параметрлері негізінде газ атомдарының орташа квадраттық (r.m.s.) жылдамдығын есептеңіз. (_) m s^-1 (Мысал форматы: 709.5655501001263)'
        self.description_swahili = 'Sampuli ya gesi bora imewekwa kwenye chombo kigumu. Kulingana na vigezo vya hali vilivyotolewa kwenye mchoro, kokotoa kasi ya mzizi-wastani wa mraba (r.m.s.) ya atomi za gesi. (_) m s^-1 (Muundo wa mfano: 709.5655501001263)'

class Phy137_multi(Phy137):
    def __init__(self):
        super().__init__()
        self.description_chinese = '氦气表现为理想气体。根据图中显示的初始参数和最终温度，计算加热后分子的最终方均根 (r.m.s.) 速率。(_) m s^-1 (示例格式：1234.56)'
        self.description_arabic = 'يتصرف الهيليوم كغاز مثالي.\nباستخدام المعطيات الابتدائية ودرجة الحرارة النهائية، احسب السرعة النهائية للجذر التربيعي لمتوسط المربعات (r.m.s.) للجزيئات بعد التسخين.\n(_) m s^-1 (مثال: 1234.56)'
        self.description_hindi = 'हीलियम एक आदर्श गैस की तरह व्यवहार करती है। आरेख में दर्शाए गए प्रारंभिक मापदंडों और अंतिम तापमान के आधार पर, गर्म करने के बाद अणुओं की अंतिम वर्गमूल औसत का वर्ग (r.m.s.) गति की गणना कीजिए। (_) m s^-1 (उदाहरण प्रारूप: 1234.56)'
        self.description_kazakh = 'Гелий идеал газ ретінде қарастырылады. Диаграммада көрсетілген бастапқы параметрлер мен соңғы температура негізінде қыздырылғаннан кейінгі молекулалардың соңғы орташа квадраттық (r.m.s.) жылдамдығын есептеңіз. (_) m s^-1 (Мысал форматы: 1234.56)'
        self.description_swahili = 'Heliamu inatenda kama gesi bora. Kulingana na vigezo vya awali na halijoto ya mwisho iliyoonyeshwa kwenye mchoro, kokotoa kasi ya mwisho ya mzizi-wastani wa mraba (r.m.s.) ya molekuli baada ya kupashwa joto. (_) m s^-1 (Muundo wa mfano: 1234.56)'

class Phy138_multi(Phy138):
    def __init__(self):
        super().__init__()
        self.description_chinese = '所提供的图像说明了氧气在两个不同温度下的分子速率分布。识别分布的特征并计算气体在较高温度 T_2 下的最概然速率 (v_p)。(_) m s^-1 (示例格式：734.9489778209097)'
        self.description_arabic = 'يوضح الشكل توزيع سرعات جزيئات غاز الأكسجين عند درجتي حرارة مختلفتين.\nحدد خصائص التوزيع واحسب السرعة الأكثر احتمالًا $v_p$ عند درجة الحرارة الأعلى $T_2$.\n(_) m s^-1 (مثال: 734.9489778209097)'
        self.description_hindi = 'दिए गए ग्राफ में दो अलग-अलग तापमानों पर ऑक्सीजन गैस की आणविक गति का वितरण दर्शाया गया है। वितरण की विशेषताओं को पहचानें और उच्च तापमान T_2 पर गैस की सबसे संभावित गति (v_p) की गणना करें। (_) m s^-1 (उदाहरण प्रारूप: 734.9489778209097)'
        self.description_kazakh = 'Берілген графикте оттегі газының екі түрлі температурадағы молекулалық жылдамдықтарының таралуы көрсетілген. Таралудың сипаттамаларын анықтап, жоғарырақ T_2 температурасындағы газ үшін ең ықтимал жылдамдықты (v_p) есептеңіз. (_) m s^-1 (Мысал форматы: 734.9489778209097)'
        self.description_swahili = 'Grafu iliyotolewa inaonyesha usambaaji wa kasi za molekuli kwa gesi ya oksijeni katika halijoto mbili tofauti. Bainisha sifa za usambaaji huu na ukokotoe kasi inayoelekea kutokea zaidi (v_p) kwa gesi katika halijoto ya juu T_2. (_) m s^-1 (Muundo wa mfano: 734.9489778209097)'

class Phy139_multi(Phy139):
    def __init__(self):
        super().__init__()
        self.description_chinese = '单原子气体包含在一个柔性气球中。根据图中提供的热力学数值，计算所做功的大小。(_) kJ (示例格式：-25.08634304946299)'
        self.description_arabic = 'غاز أحادي الذرة داخل بالون مرن.\nباستخدام القيم الديناميكية الحرارية، احسب مقدار الشغل المبذول.\n(_) kJ (مثال: -25.08634304946299)'
        self.description_hindi = 'एक एकपरमाण्विक गैस एक लचीले गुब्बारे में समाहित है। आरेख में दिए गए ऊष्मागतिक मानों के आधार पर किए गए कार्य का परिमाण ज्ञात कीजिए। (_) kJ (उदाहरण प्रारूप: -25.08634304946299)'
        self.description_kazakh = 'Иілгіш шарда бір атомды газ бар. Диаграммада берілген термодинамикалық мәндер негізінде жасалған жұмыстың модулін есептеңіз. (_) kJ (Мысал форматы: -25.08634304946299)'
        self.description_swahili = 'Gesi ya kiatomi-kimoja (monatomic gas) ipo ndani ya puto linalonyumbulika. Kulingana na thamani za termodinamika zilizotolewa kwenye mchoro, kokotoa ukubwa wa kazi iliyofanywa. (_) kJ (Muundo wa mfano: -25.08634304946299)'

class Phy140_multi(Phy140):
    def __init__(self):
        super().__init__()
        self.description_chinese = '理想气体保存在气缸中并在恒定压强下膨胀。使用图中显示的热力学数值，计算气体体积变化的大小。(_) m^3 (示例格式：0.150464677)'
        self.description_arabic = 'غاز مثالي داخل أسطوانة يتمدد عند ضغط ثابت.\nباستخدام القيم المعطاة، احسب مقدار التغير في الحجم.\n(_) m^3 (مثال: 0.150464677)'
        self.description_hindi = 'एक आदर्श गैस को सिलेंडर में रखा गया है और यह स्थिर दाब पर फैलती है। आरेख में दर्शाए गए ऊष्मागतिकीय मानों का उपयोग करके, गैस के आयतन में परिवर्तन का परिमाण ज्ञात कीजिए। (_) m^3 (उदाहरण प्रारूप: 0.150464677)'
        self.description_kazakh = 'Идеал газ цилиндрде ұсталады және тұрақты қысымда ұлғаяды. Диаграммада көрсетілген термодинамикалық мәндерді пайдаланып, газ көлемі өзгерісінің модулін есептеңіз. (_) m^3 (Мысал форматы: 0.150464677)'
        self.description_swahili = 'Gesi bora imehifadhiwa kwenye silinda na inapanuka katika kanieneo thabiti. Kwa kutumia thamani za termodinamika zilizoonyeshwa kwenye mchoro, kokotoa ukubwa wa mabadiliko ya ujazo wa gesi. (_) m^3 (Muundo wa mfano: 0.150464677)'

class Phy141_multi(Phy141):
    def __init__(self):
        super().__init__()
        self.description_chinese = '100°C 的液态水在相同温度下完全转化为蒸汽。根据图中提供的具体数据，计算系统内能的增加量。(_) J (示例格式：734566.9489778209097)'
        self.description_arabic = 'يتحول الماء السائل عند 100°C بالكامل إلى بخار عند نفس درجة الحرارة.\nباستخدام المعطيات، احسب الزيادة في الطاقة الداخلية.\n(_) J (مثال: 734566.9489778209097)'
        self.description_hindi = '100°C पर तरल जल उसी तापमान पर पूर्णतः भाप में परिवर्तित हो जाता है। आरेख में दिए गए विशिष्ट आंकड़ों के आधार पर, प्रणाली की आंतरिक ऊर्जा में वृद्धि की गणना कीजिए। (_) J (उदाहरण प्रारूप: 734566.9489778209097)'
        self.description_kazakh = '100°C-тағы сұйық су сол температурада толығымен буға айналады. Диаграммада берілген арнайы мәліметтер негізінде жүйенің ішкі энергиясының артуын есептеңіз. (_) J (Мысал форматы: 734566.9489778209097)'
        self.description_swahili = 'Maji ya kimiminika katika 100°C yanabadilishwa kabisa kuwa mvuke katika halijoto hiyo hiyo. Kulingana na data iliyotolewa kwenye mchoro, kokotoa ongezeko la nishati ya ndani ya mfumo. (_) J (Muundo wa mfano: 734566.9489778209097)'

class Phy142_multi(Phy142):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个单摆由系在细线上的一小球组成。单摆从图中所示位置由静止释放。假设该运动为简谐运动，计算小球在摆动过程中的最大速率。(取 g = {self.g_str} m s⁻²)。(_) m s^-1 (示例格式：0.126778903)'
        self.description_arabic = f'يتكون بندول بسيط من ثقل صغير معلق بخيط. يُترك من السكون من الموضع الموضح.\nبافتراض حركة توافقية بسيطة، احسب السرعة العظمى للثقل.\n(استخدم g = {self.g_str} m s⁻²)\n(_) m s^-1 (مثال: 0.126778903)'
        self.description_hindi = f'एक सरल पेंडुलम में एक डोरी से बंधी एक छोटी सी बॉब होती है। पेंडुलम को चित्र में दर्शाई गई स्थिति से विराम अवस्था से छोड़ा जाता है। यह मानते हुए कि गति सरल आवर्त गति है, बॉब के दोलन के दौरान उसकी अधिकतम गति की गणना कीजिए। (g = {self.g_str} m s⁻²) सूत्र का प्रयोग करें। (_) m s^-1 (उदाहरण प्रारूप: 0.126778903)'
        self.description_kazakh = f'Математикалық маятник жіпке бекітілген кішкентай шардан тұрады. Маятник диаграммада көрсетілген күйден тыныштықтан босатылады. Қозғалысты гармоникалық деп есептеп, тербеліс кезіндегі шардың максималды жылдамдығын есептеңіз. (g = {self.g_str} m s⁻² деп алыңыз). (_) m s^-1 (Мысал форматы: 0.126778903)'
        self.description_swahili = f'Pendulamu rahisi ina bura ndogo iliyounganishwa kwenye kamba. Pendulamu inaachiwa kutoka hali tuli katika nafasi iliyoonyeshwa kwenye mchoro. Kwa kudhani huu ni mwendo rahisi wa sinusoidi (simple harmonic motion), kokotoa kasi ya juu zaidi ya bura wakati wa msuso wake. (Tumia g = {self.g_str} m s⁻²). (_) m s^-1 (Muundo wa mfano: 0.126778903)'

class Phy143_multi(Phy143):
    def __init__(self):
        super().__init__()
        self.description_chinese = '观察到一个单摆正在进行小角度振动。一名学生使用秒表测量了特定次数的完整振动所需的时间。使用图中的测量数据，求振动的频率。(_) Hz (示例格式：9.7194876492)'
        self.description_arabic = 'بندول بسيط يخضع لتذبذبات صغيرة.\nباستخدام قياسات الزمن لعدد من الذبذبات، أوجد تردد التذبذب.\n(_) Hz (مثال: 9.7194876492)'
        self.description_hindi = 'एक सरल पेंडुलम को छोटे कोण पर दोलन करते हुए देखा जाता है। एक छात्र स्टॉपवॉच का उपयोग करके एक निश्चित संख्या में पूर्ण दोलनों में लगने वाले समय को मापता है। आरेख से प्राप्त मापन डेटा का उपयोग करके दोलन की आवृत्ति ज्ञात कीजिए। (_) Hz (उदाहरण प्रारूप: 9.7194876492)'
        self.description_kazakh = 'Математикалық маятниктің кіші бұрыштық тербелістері бақыланады. Оқушы белгілі бір толық тербелістер санына кеткен уақытты өлшеу үшін секундомерді пайдаланады. Диаграммадағы өлшеу деректерін пайдаланып, тербеліс жиілігін анықтаңыз. (_) Hz (Мысал форматы: 9.7194876492)'
        self.description_swahili = 'Pendulamu rahisi inaonekana ikipitia misuso ya pembe ndogo. Mwanafunzi anatumia saa-kipima-muda kupima muda uliotumika kwa idadi maalum ya misuso kamili. Kwa kutumia data ya vipimo kutoka kwenye mchoro, bainisha frikwensi ya msuso huo. (_) Hz (Muundo wa mfano: 9.7194876492)'

class Phy144_multi(Phy144):
    def __init__(self):
        super().__init__()
        self.description_chinese = '质量为 $m$ 的物块连接在水平弹簧上，做简谐运动。图中显示了物块处于最大位移状态。利用给出的瞬时参数，计算振动的角频率 $\\omega$。（单位：rad s^-1）（示例格式：2.345）'
        self.description_arabic = 'كتلة $m$ متصلة بنابض أفقي وتخضع لحركة توافقية بسيطة.\nيوضح الشكل الكتلة عند أقصى إزاحة. باستخدام المعطيات، احسب التردد الزاوي $\\omega$.\n(_) rad s^-1 (مثال: 2.345)'
        self.description_hindi = 'द्रव्यमान $m$ का एक ब्लॉक एक क्षैतिज स्प्रिंग से जुड़ा है और सरल आवर्त गति करता है। चित्र में ब्लॉक का अधिकतम विस्थापन दिखाया गया है। दिए गए तात्कालिक मापदंडों का उपयोग करके, दोलन की कोणीय आवृत्ति $\\omega$ की गणना कीजिए। (_) rad s^-1 (उदाहरण प्रारूप: 2.345)'
        self.description_kazakh = 'Массасы $m$ жүк горизонталь серіппеге бекітілген және гармоникалық тербеліс жасайды. Сызбада жүктің максималды ығысу (амплитуда) кезіндегі күйі көрсетілген. Берілген лездік параметрлерді пайдаланып, тербелістің циклдік (бұрыштық) жиілігін $\\omega$ есептеңіз. (_) рад с^-1 (Мысалы: 2.345)'
        self.description_swahili = 'gimba chenye masi $m$ kimeunganishwa kwenye kichemchemi (springi) mlalo na kufanya mwendo rahisi wa sinusoidi. Mchoro unaonyesha kitalu kikiwa katika mshindo wake wa juu zaidi. Kwa kutumia vigezo vya muda mfupi vilivyotolewa, kokotoa frikwensi ya pembe $\\omega$ ya msuso huo. (_) rad s^-1 (Muundo wa mfano: 2.345)'

class Phy145_multi(Phy145):
    def __init__(self):
        super().__init__()
        self.description_chinese = "一个单摆小球作简谐运动。其动能 $E_k$ 随时间 $t$ 的变化显示在图中。使用连续最大值的时间坐标，求单摆振动的周期 $T$。(_) s (示例格式：2.6430486321164166)"
        self.description_arabic = 'يتذبذب ثقل بندول بحركة توافقية بسيطة.\nيوضح الرسم البياني تغير طاقته الحركية $E_k$ مع الزمن $t$.\nباستخدام أزمنة القمم المتتالية، أوجد الزمن الدوري $T$.\n(_) s (مثال: 2.6430486321164166)'
        self.description_hindi = "एक पेंडुलम बॉब सरल आवर्त गति से दोलन करता है। समय $t$ के साथ इसकी गतिज ऊर्जा $E_k$ का परिवर्तन ग्राफ में दर्शाया गया है। क्रमिक अधिकतम मानों के समय निर्देशांकों का उपयोग करके, पेंडुलम के दोलन की आवर्तकाल $T$ ज्ञात कीजिए। (_) s (उदाहरण प्रारूप: 2.6430486321164166)"
        self.description_kazakh = "Маятник шары гармоникалық тербеліс жасайды. Оның $E_k$ кинетикалық энергиясының $t$ уақытқа тәуелділігі графикте көрсетілген. Тізбекті максимумдардың уақыт координаталарын пайдаланып, маятник тербелісінің $T$ периодын анықтаңыз. (_) s Мысал форматы: 2.6430486321164166)"
        self.description_swahili = "Bura ya pendulamu inasusa kwa mwendo rahisi wa sinusoidi. Mabadiliko ya nishati yake ya mwendo $E_k$ kulingana na muda $t$ yanaonyeshwa kwenye grafu. Kwa kutumia viwianishi vya muda vya vilele mfululizo, bainisha kipindi $T$ cha msuso wa pendulamu. (_) s (Muundo wa mfano: 2.6430486321164166)"

class Phy146_multi(Phy146):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个单摆小球作简谐运动。根据图中所显示的物理约束，计算单摆小球在运动过程中的最大速率。(_) m s^-1 (示例格式：0.1234)'
        self.description_arabic = 'يتذبذب ثقل بندول بحركة توافقية بسيطة.\nبناءً على المعطيات في الشكل، احسب السرعة العظمى لثقل البندول أثناء حركته.\n(_) m s^-1 (مثال: 0.1234)'
        self.description_hindi = 'एक पेंडुलम बॉब सरल आवर्त गति से दोलन करता है। चित्र में दर्शाई गई भौतिक बाधाओं के आधार पर, गति के दौरान पेंडुलम बॉब की अधिकतम गति की गणना कीजिए। (_) m s^-1 (उदाहरण प्रारूप: 0.1234)'
        self.description_kazakh = 'Маятник шары гармоникалық тербеліс жасайды. Диаграммада көрсетілген физикалық шектеулер негізінде қозғалыс кезіндегі маятник шарының максималды жылдамдығын есептеңіз. (_) m s^-1 (Мысал форматы: 0.1234)'
        self.description_swahili = 'Bura ya pendulamu inasusa kwa mwendo rahisi wa sinusoidi. Kulingana na vigezo vya kifizikia vilivyoonyeshwa kwenye mchoro, kokotoa kasi ya juu zaidi ya bura ya pendulamu wakati wa mwendo wake. (_) m s^-1 (Muundo wa mfano: 0.1234)'

class Phy147_multi(Phy147):
    def __init__(self):
        super().__init__()
        self.description_chinese = '该图显示了一个阻尼振动系统的位移-时间图像。使用图中嵌入的参数和峰值坐标，求振动的频率。(_) Hz (示例格式：1.979976539513881)'
        self.description_arabic = 'يوضح الشكل منحنى الإزاحة–الزمن لنظام متذبذب متخامد.\nباستخدام المعطيات وإحداثيات القمم، أوجد تردد التذبذب.\n(_) Hz (مثال: 1.979976539513881)'
        self.description_hindi = 'चित्र में अवमंदित दोलन प्रणाली का विस्थापन-समय ग्राफ दर्शाया गया है। आरेख में दिए गए मापदंडों और शिखर निर्देशांकों का उपयोग करके दोलन की आवृत्ति ज्ञात कीजिए। (_) Hz (उदाहरण प्रारूप: 1.979976539513881)'
        self.description_kazakh = 'Суретте өшетін тербелмелі жүйенің ығысу-уақыт графигі көрсетілген. Диаграммада енгізілген параметрлер мен шың координаталарын пайдаланып, тербеліс жиілігін анықтаңыз. (_) Hz (Мысал форматы: 1.979976539513881)'
        self.description_swahili = 'Kielelezo kinaonyesha grafu ya mshindo na muda kwa mfumo wa msuso unaofifia (damped oscillation). Kwa kutumia vigezo vilivyopachikwa kwenye mchoro na viwianishi vya vilele, bainisha frikwensi ya msuso huo. (_) Hz (Muundo wa mfano: 1.979976539513881)'

class Phy148_multi(Phy148):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个物块连接在两个相同的弹簧之间并进行阻尼振动。根据位移-时间图像和图中提供的参数，求阻尼角频率 $\\omega_d$。(_) rad s^-1 (示例格式：6.90700120734646)'
        self.description_arabic = 'كتلة متصلة بين نابضين متماثلين وتخضع لتذبذبات متخامدة.\nباستخدام منحنى الإزاحة–الزمن والمعطيات، أوجد التردد الزاوي المتخامد $\\omega_d$.\n(_) rad s^-1 (مثال: 6.90700120734646)'
        self.description_hindi = 'एक ब्लॉक दो समान स्प्रिंगों के बीच जुड़ा हुआ है और अवमंद दोलन करता है। विस्थापन-समय ग्राफ और आरेख में दिए गए मापदंडों के आधार पर, अवमंद कोणीय आवृत्ति $\\omega_d$ ज्ञात कीजिए। (_) rad s^-1 (उदाहरण प्रारूप: 6.90700120734646)'
        self.description_kazakh = 'Блок екі бірдей серіппе арасында жалғанған және өшетін тербелістер жасайды. Ығысу-уақыт графигі мен диаграммада берілген параметрлер негізінде өшетін $\\omega_d$ циклдік жиілігін анықтаңыз. (_) rad s^-1 (Мысал форматы: 6.90700120734646)'
        self.description_swahili = 'Kitalu kimeunganishwa kati ya kichemchemi (springi) mbili zinazofanana na kufanya misuso inayofifia. Kulingana na grafu ya mshindo na muda pamoja na vigezo vilivyotolewa kwenye mchoro, bainisha frikwensi ya pembe inayofifia $\\omega_d$. (_) rad s^-1 (Muundo wa mfano: 6.90700120734646)'

class Phy149_multi(Phy149):
    def __init__(self):
        super().__init__()
        self.description_chinese = '真空中固定有两个相同的正点电荷 $+Q$。A点位于连接它们的直线上。根据图中显示的合电场强度和距离，计算电荷 $Q$ 的大小。(_) C (示例格式：8.095898412410912e-08)'
        self.description_arabic = 'شحنتان نقطيتان موجبتان متماثلتان $+Q$ ثابتتان في فراغ.\nتقع النقطة $A$ على الخط الواصل بينهما. باستخدام شدة المجال الكهربائي المحصلة والمسافات، احسب مقدار الشحنة $Q$.\n(_) C (مثال: 8.095898412410912e-08)'
        self.description_hindi = 'दो समान धनात्मक बिंदु चार्ज $+Q$ निर्वात में स्थिर हैं। बिंदु $A$ उन्हें जोड़ने वाली रेखा पर स्थित है। चित्र में दर्शाए गए परिणामी विद्युत क्षेत्र की तीव्रता और दूरियों के आधार पर चार्ज $Q$ का परिमाण ज्ञात कीजिए। (_) C (उदाहरण प्रारूप: 8.095898412410912e-08)'
        self.description_kazakh = 'Екі бірдей оң $+Q$ нүктелік заряды вакуумде бекітілген. $A$ нүктесі оларды қосатын сызықта орналасқан. Диаграммада көрсетілген қорытқы электр өрісінің кернеулігі мен қашықтықтар негізінде $Q$ зарядының шамасын есептеңіз. (_) C (Мысал форматы: 8.095898412410912e-08)'
        self.description_swahili = 'Chaji mbili chanya zinazofanana za nukta $+Q$ zimewekwa tuli kwenye ombwe. Nukta $A$ ipo kwenye mstari unaoziunganisha. Kulingana na ukali tokeo wa uga wa umeme na umbali ulioonyeshwa kwenye mchoro, kokotoa ukubwa wa chaji $Q$. (_) C (Muundo wa mfano: 8.095898412410912e-08)'

class Phy150_multi(Phy150):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个电子被放置在匀强电场中。使用图中提供的参数，计算电子加速度的大小。(_) m s⁻² (示例格式：0.4319030554713497)'
        self.description_arabic = 'يوضع إلكترون في مجال كهربائي منتظم.\nباستخدام المعطيات، احسب مقدار تسارع الإلكترون.\n(_) m s⁻² (مثال: 0.4319030554713497)'
        self.description_hindi = 'एक इलेक्ट्रॉन को एकसमान विद्युत क्षेत्र में रखा गया है। आरेख में दिए गए मापदंडों का उपयोग करके, इलेक्ट्रॉन के त्वरण का परिमाण ज्ञात कीजिए। ( _ ) m s⁻² (उदाहरण प्रारूप: 0.4319030554713497)'
        self.description_kazakh = 'Электрон біртекті электр өрісіне орналастырылған. Диаграммада берілген параметрлерді пайдаланып, электрон үдеуінің модулін есептеңіз. ( _ ) m s⁻² (Мысал форматы:  0.4319030554713497)'
        self.description_swahili = 'Elektroni imewekwa kwenye uga sawia wa umeme. Kwa kutumia vigezo vilivyotolewa kwenye mchoro, kokotoa ukubwa wa mchapuko wa elektroni. ( _ ) m s⁻² (Muundo wa mfano: 0.4319030554713497)'

class Phy151_multi(Phy151):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中展示了连接到直流电源的两块平行金属板。两板之间产生匀强电场。计算两板之间的电场强度。(示例格式：3.546e+10)。'
        self.description_arabic = 'يوضح الشكل لوحين معدنيين متوازيين متصلين بمصدر تيار مستمر (DC).\nينشأ مجال كهربائي منتظم بين اللوحين. احسب شدة المجال الكهربائي.\n(مثال: 3.546e+10)'
        self.description_hindi = 'चित्र में दो समानांतर धातु की प्लेटें एक d.c. विद्युत आपूर्ति से जुड़ी हुई दिखाई गई हैं। प्लेटों के बीच एक समान विद्युत क्षेत्र उत्पन्न होता है। प्लेटों के बीच विद्युत क्षेत्र की तीव्रता की गणना कीजिए। (उदाहरण प्रारूप: 3.546e+10)।'
        self.description_kazakh = 'Диаграммада тұрақты ток көзіне қосылған екі параллель металл пластина көрсетілген. Пластиналар арасында біртекті электр өрісі пайда болады. Пластиналар арасындағы электр өрісінің кернеулігін есептеңіз. (Мысал форматы: 3.546e+10).'
        self.description_swahili = 'Mchoro unaonyesha sahani mbili sambamba za metali zilizounganishwa kwenye chanzo cha umeme cha d.c. Uga sawia wa umeme unazalishwa kati ya sahani hizo. Kokotoa ukali wa uga wa umeme kati ya sahani hizo. (Mfano wa Muundo: 3.546e+10).'

class Phy152_multi(Phy152):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中显示了一个带电的聚苯乙烯小球悬挂在连接到直流电源的两块平行金属板之间。两板之间存在匀强电场。计算作用在电荷上的电场力的大小。(示例格式：3.546e-05)。'
        self.description_arabic = 'يوضح الشكل كرة بوليسترين صغيرة مشحونة معلقة بين لوحين معدنيين متوازيين متصلين بمصدر تيار مستمر (DC).\nيوجد مجال كهربائي منتظم بين اللوحين. احسب مقدار القوة الكهربائية المؤثرة.\n(مثال: 3.546e-05)'
        self.description_hindi = 'चित्र में एक छोटा आवेशित पॉलीस्टायरीन गोला दो समानांतर धातु प्लेटों के बीच लटका हुआ दिखाया गया है, जो एक d.c. विद्युत आपूर्ति से जुड़े हैं। प्लेटों के बीच एक समान विद्युत क्षेत्र मौजूद है। चार्ज पर लगने वाले विद्युत बल का परिमाण ज्ञात कीजिए। (उदाहरण प्रारूप: 3.546e-05)।'
        self.description_kazakh = 'Диаграммада тұрақты ток көзіне қосылған екі параллель металл пластина арасында ілініп тұрған кішкентай зарядталған полистирол шары көрсетілген. Пластиналар арасында біртекті электр өрісі бар. Зарядқа әсер ететін электр күшінің модулін есептеңіз. (Мысал форматы: 3.546e-05).'
        self.description_swahili = 'Mchoro unaonyesha mpira mdogo wa polistairini wenye chaji uliositishwa kati ya sahani mbili sambamba za metali zilizounganishwa kwenye chanzo cha umeme cha d.c. Uga sawia wa umeme upo kati ya sahani hizo. Kokotoa ukubwa wa kani ya umeme inayokaimu chaji hiyo. (Mfano wa Muundo: 3.546e-05).'

class Phy153_multi(Phy153):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，真空中相隔一定距离有两个点电荷A和B。求两电荷之间的静电力大小。请以科学记数法提供您的答案 (示例格式：3.54E-05)。不要包含单位。'
        self.description_arabic = f'شحنتان نقطيتان A و B مفصولتان في فراغ كما هو موضح.\nأوجد مقدار القوة الكهروستاتيكية بينهما.\nأعطِ الإجابة بالتدوين العلمي دون وحدات.\n(مثال: 3.54E-05)'
        self.description_hindi = f'चित्र में दर्शाए अनुसार दो बिंदु चार्ज A और B निर्वात में अलग-अलग रखे गए हैं। दोनों चार्ज के बीच लगने वाले स्थिरवैद्युत बल का परिमाण ज्ञात कीजिए। अपना उत्तर वैज्ञानिक संकेतन में दीजिए (उदाहरण प्रारूप: 3.54E-05)। इकाई शामिल न करें।'
        self.description_kazakh = f'Екі нүктелік А және В заряды суретте көрсетілгендей вакуумде бір-бірінен қашықтықта орналасқан. Екі заряд арасындағы электростатикалық күштің модулін анықтаңыз. Жауабыңызды стандартты түрде беріңіз (Мысал форматы: 3.54E-05). Өлшем бірліктерін қоспаңыз.'
        self.description_swahili = f'Chaji mbili za nukta A na B zimetenganishwa kwenye ombwe kama inavyoonyeshwa kwenye picha. Bainisha ukubwa wa kani ya kielektrostatiki kati ya chaji hizo mbili. Toa jibu lako katika itirafu ya kisayansi (Muundo wa mfano: 3.54E-05). Usijumuishe vizio.'

class Phy154_multi(Phy154):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'如图所示，真空中相隔一定距离有两个点电荷A和B。计算作用在每个电荷上的电场力大小。请以科学记数法提供您的答案 (示例格式：3.54E-05)。'
        self.description_arabic = f'شحنتان نقطيتان A و B مفصولتان في فراغ كما هو موضح.\nاحسب مقدار القوة الكهربائية المؤثرة على كل شحنة.\nأعطِ الإجابة بالتدوين العلمي.\n(مثال: 3.54E-05)'
        self.description_hindi = f'चित्र में दर्शाए अनुसार दो बिंदु आवेश A और B निर्वात में एक दूसरे से अलग-अलग रखे गए हैं। प्रत्येक चार्ज पर लगने वाले विद्युत बल का परिमाण ज्ञात कीजिए। अपना उत्तर वैज्ञानिक संकेतन में दीजिए (उदाहरण प्रारूप: 3.54E-05)।'
        self.description_kazakh = f'Екі нүктелік А және В заряды суретте көрсетілгендей вакуумде бір-бірінен қашықтықта орналасқан. Әр зарядқа әсер ететін электр күшінің модулін есептеңіз. Жауабыңызды стандартты түрде беріңіз (Мысал форматы: 3.54E-05).'
        self.description_swahili = f'Chaji mbili za nukta A na B zimetenganishwa kwenye ombwe kama inavyoonyeshwa kwenye picha. Kokotoa ukubwa wa kani ya umeme inayokaimu kila chaji. Toa jibu lako katika itirafu ya kisayansi (Muundo wa mfano: 3.54E-05).'

class Phy155_multi(Phy155):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中显示了两个带电导体球 A 和 B，以及它们各自的表面电场强度。如果储存在球 B 表面的电荷为 {self.QB_microC:.1f} μC，它的半径为 ... cm (示例格式：3.544E-05)'
        self.description_arabic = f'توضح الصورة كرتين موصلتين مشحونتين A و B، مع شدة المجال الكهربائي السطحي لكل منهما.\nإذا كانت الشحنة على سطح الكرة B تساوي {self.QB_microC:.1f} μC، فأوجد نصف قطرها.\n... cm (مثال: 3.544E-05)'
        self.description_hindi = f'चित्र में दो आवेशित चालक गोले A और B दर्शाए गए हैं, साथ ही उनकी सतही विद्युत क्षेत्र की तीव्रता भी दर्शाई गई है। यदि गोले B की सतह पर संचित आवेश {self.QB_microC:.1f} μC है, तो इसकी त्रिज्या ... cm है। (उदाहरण प्रारूप: 3.544E-05)'
        self.description_kazakh = f'Суретте екі зарядталған өткізгіш А және В сфералары олардың беттік электр өрісінің кернеулігімен көрсетілген. Егер В сферасының бетінде сақталған заряд {self.QB_microC:.1f} μC болса, оның радиусы ... cm (Мысал форматы: 3.544E-05)'
        self.description_swahili = f'Picha inaonyesha tufe mbili kondakta zenye chaji, A na B, pamoja na ukali wa nyuga zao za umeme kwenye uso. Ikiwa chaji iliyohifadhiwa kwenye uso wa tufe B ni {self.QB_microC:.1f} μC, nusukipenyo chake ni ... cm (Muundo wa mfano: 3.544E-05)'

class Phy156_multi(Phy156):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'图中展示了一个α粒子 (α) 正面对着一个金属原子核靠近。如果α粒子以图示速度运动，且该金属原子核的质子数为 Z = {self.Z}，计算最近距离 r_min。(示例格式：1.34)'
        self.description_arabic = f'توضح الصورة جسيم ألفا (α) يقترب مباشرة من نواة معدنية.\nإذا كانت سرعته كما هو موضح وعدد البروتونات Z = {self.Z}، احسب أقرب مسافة اقتراب $r_{{min}}$.\n(مثال: 1.34)'
        self.description_hindi = f'चित्र में एक अल्फा कण (α) को धातु के नाभिक की ओर सीधे अग्रगामी गति से आते हुए दर्शाया गया है। यदि अल्फा कण दर्शाई गई गति से यात्रा करता है और धातु के नाभिक में प्रोटॉन की संख्या Z = {self.Z} है, तो निकटतम निकटवर्ती दूरी r_min की गणना कीजिए। (उदाहरण प्रारूप: 1.34)'
        self.description_kazakh = f'Суретте металл ядросына тікелей жақындап келе жатқан альфа бөлшегі (α) көрсетілген. Егер альфа бөлшегі көрсетілген жылдамдықпен қозғалса және металл ядросының протон саны Z = {self.Z} болса, ең жақын жақындау қашықтығын, r_min есептеңіз. (Мысал форматы: 1.34)'
        self.description_swahili = f'Picha inaonyesha chembe ya alpha (α) ikikaribia kiini cha metali uso kwa uso (head-on). Ikiwa chembe ya alpha inasafiri kwa kasi iliyoonyeshwa na kiini cha metali kina namba ya protoni Z = {self.Z}, kokotoa umbali wa karibu zaidi wa kukaribia, r_min. (Muundo wa mfano: 1.34)'

class Phy157_multi(Phy157):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中显示了一个α粒子正在靠近一个静止的金原子核。在图示距离处，α粒子瞬间静止。计算此时系统的电势能 (U)，以焦耳为单位。(示例格式：3.543E-10)'
        self.description_arabic = 'توضح الصورة جسيم α يقترب من نواة ذهب ساكنة.\nعند المسافة الموضحة، يتوقف الجسيم لحظيًا. احسب طاقة الوضع الكهربائية $U$.\n(مثال: 3.543E-10)'
        self.description_hindi = 'चित्र में एक α-कण स्थिर स्वर्ण नाभिक की ओर अग्रसर दिखाया गया है। दर्शाई गई दूरी पर, α-कण क्षण भर के लिए विराम अवस्था में आ जाता है। इस क्षण पर प्रणाली की विद्युत स्थितिज ऊर्जा (U) की गणना Joules में कीजिए। (उदाहरण प्रारूप: 3.543E-10)'
        self.description_kazakh = 'Суретте тыныштықтағы алтын ядросына жақындап келе жатқан α-бөлшегі көрсетілген. Көрсетілген қашықтықта α-бөлшегі бір сәтке тоқтайды. Осы сәттегі жүйенің электрлік потенциалдық энергиясын (U) Джоульмен есептеңіз. (Мысал форматы: 3.543E-10)'
        self.description_swahili = 'Picha inaonyesha chembe ya α ikikaribia kiini tuli cha dhahabu. Katika umbali ulioonyeshwa, chembe ya α inatulia kwa muda mfupi. Kokotoa nishati ya potensheli ya umeme (U) ya mfumo katika wakati huu kwa vizio vya Chauli (J). (Muundo wa mfano: 3.543E-10)'

class Phy158_multi(Phy158):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中显示了一个以恒定速率运动的α粒子 ($^4_2$He$^{2+}$)。使用图中提供的物理常数和参数，计算α粒子的动能，以焦耳 (J) 为单位。(示例格式：3.54E-12)。'
        self.description_arabic = 'توضح الصورة جسيم α ($^4_2$He$^{2+}$) يتحرك بسرعة ثابتة.\nباستخدام المعطيات، احسب طاقته الحركية.\n(مثال: 3.54E-12)'
        self.description_hindi = 'चित्र में एक α-कण ($^4_2$He$^{2+}$) स्थिर गति से गतिमान दिखाया गया है। चित्र में दिए गए भौतिक स्थिरांकों और मापदंडों का उपयोग करके, α-कण की गतिज ऊर्जा को Joules (J) में ज्ञात कीजिए। (उदाहरण प्रारूप: 3.54E-12)।'
        self.description_kazakh = 'Суретте тұрақты жылдамдықпен қозғалып келе жатқан α-бөлшегі ($^4_2$He$^{2+}$) көрсетілген. Суретте берілген физикалық тұрақтылар мен параметрлерді пайдаланып, α-бөлшегінің кинетикалық энергиясын Джоульмен (J) есептеңіз. (Мысал форматы: 3.54E-12).'
        self.description_swahili = 'Picha inaonyesha chembe ya α ($^4_2$He$^{2+}$) ikisonga kwa kasi thabiti. Kwa kutumia namba thabiti za kifizikia na vigezo vilivyotolewa kwenye picha, kokotoa nishati ya mwendo ya chembe hiyo ya α katika vizio vya Chauli (J). (Muundo wa mfano: 3.54E-12).'

class Phy159_multi(Phy159):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，两个电容器和一个电阻连接在一起。计算这两个电容器的组合电容。(_) µF。(示例格式：12.3664)'
        self.description_arabic = 'مكثفان ومقاومة موصولون كما في الشكل.\nاحسب السعة المكافئة للمكثفين.\n(_) µF (مثال: 12.3664)'
        self.description_hindi = 'चित्र में दिखाए अनुसार दो संधारित्र और एक प्रतिरोधक जुड़े हुए हैं। दोनों संधारित्रों की संयुक्त धारिता ज्ञात कीजिए। (_) µF। (उदाहरण प्रारूप: 12.3664)'
        self.description_kazakh = 'Екі конденсатор мен резистор көрсетілгендей жалғанған. Екі конденсатордың жалпы сыйымдылығын есептеңіз. (_) µF. (Мысал форматы: 12.3664)'
        self.description_swahili = 'Kapasita mbili na kinza vimeunganishwa kama inavyoonyeshwa. Kokotoa uwezo (capacitance) tokeo wa kapasita hizo mbili. (_) µF. (Muundo wa mfano: 12.3664)'

class Phy160_multi(Phy160):
    def __init__(self):
        super().__init__()
        self.description_chinese = '两个电容器 X 和 Y 并联连接到一个电池上。使用图中显示的值，计算电容器 X 上的电荷量。(_) C。(示例格式：1.234e-4)'
        self.description_arabic = 'مكثفان X و Y موصولان على التوازي ببطارية.\nباستخدام القيم المعطاة، احسب الشحنة على المكثف X.\n(_) C (مثال: 1.234e-4)'
        self.description_hindi = 'दो संधारित्र X और Y एक बैटरी से समानांतर क्रम में जुड़े हैं। आरेख में दर्शाए गए मानों का उपयोग करके संधारित्र X पर चार्ज की गणना कीजिए। (_) C। (उदाहरण प्रारूप: 1.234e-4)'
        self.description_kazakh = 'Екі X және Y конденсаторы батареяға параллель жалғанған. Диаграммада көрсетілген мәндерді пайдаланып, X конденсаторындағы зарядты есептеңіз. (_) C. (Мысал форматы: 1.234e-4)'
        self.description_swahili = 'Kapasita mbili, X na Y, zimeunganishwa sambamba kwenye betri. Kwa kutumia thamani zilizoonyeshwa kwenye mchoro, kokotoa chaji iliyo kwenye kapasita X. (_) C. (Muundo wa mfano: 1.234e-4)'

class Phy161_multi(Phy161):
    def __init__(self):
        super().__init__()
        self.description_chinese = '两个电容器 A 和 B 并联连接到一个直流电源上。使用图中显示的值，计算电容器 A 中储存的能量。(_) J (示例格式：0.123)'
        self.description_arabic = 'مكثفان A و B موصولان على التوازي بمصدر تيار مستمر.\nاحسب الطاقة المخزنة في المكثف A.\n(_) J (مثال: 0.123)'
        self.description_hindi = 'दो संधारित्र A और B समानांतर क्रम में एक DC आपूर्ति से जुड़े हैं। आरेख में दर्शाए गए मानों का उपयोग करके संधारित्र A में संग्रहित ऊर्जा की गणना कीजिए। (_) J (उदाहरण प्रारूप: 0.123)'
        self.description_kazakh = 'Екі А және В конденсаторы тұрақты ток көзіне параллель жалғанған. Диаграммада көрсетілген мәндерді пайдаланып, А конденсаторында жинақталған энергияны есептеңіз. (_) J (Мысал форматы: 0.123)'
        self.description_swahili = 'Kapasita mbili, A na B, zimeunganishwa sambamba kwenye chanzo cha DC. Kwa kutumia thamani zilizoonyeshwa kwenye mchoro, kokotoa nishati iliyohifadhiwa kwenye kapasita A. (_) J (Muundo wa mfano: 0.123)'

class Phy162_multi(Phy162):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，两个电容器和一个电阻连接在一起。求这两个电容器中储存的总能量。(_) J。(示例格式：1.234e-4)'
        self.description_arabic = 'مكثفان ومقاومة موصولون كما في الشكل.\nأوجد الطاقة الكلية المخزنة في المكثفين.\n(_) J (مثال: 1.234e-4)'
        self.description_hindi = 'चित्र में दिखाए अनुसार दो संधारित्र और एक प्रतिरोधक जुड़े हुए हैं। दोनों संधारित्रों में संग्रहित कुल ऊर्जा ज्ञात कीजिए। (_) J (उदाहरण प्रारूप: 1.234e-4)'
        self.description_kazakh = 'Екі конденсатор мен резистор көрсетілгендей жалғанған. Екі конденсаторда жинақталған жалпы энергияны анықтаңыз. (_) J. (Мысал форматы: 1.234e-4)'
        self.description_swahili = 'Kapasita mbili na kinza vimeunganishwa kama inavyoonyeshwa. Bainisha jumla ya nishati iliyohifadhiwa kwenye kapasita hizo mbili. (_) J. (Muundo wa mfano: 1.234e-4)'

class Phy163_multi(Phy163):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个电容器通过一个固定电阻放电。该图显示了电容器两端的电势差 V 随时间 t 的变化。使用图中的数值，计算在所示时间间隔内电容器损失的能量占其初始储存能量的百分比。(_) % (示例格式：45.67)'
        self.description_arabic = 'يُفرَّغ مكثف عبر مقاومة ثابتة.\nيوضح الشكل تغير فرق الجهد مع الزمن.\nاحسب نسبة الطاقة المفقودة من الطاقة الابتدائية.\n(_) % (مثال: 45.67)'
        self.description_hindi = 'एक संधारित्र एक स्थिर प्रतिरोधक के माध्यम से निर्वहन करता है। ग्राफ संधारित्र के सिरों पर विभवांतर V के समय t के साथ परिवर्तन को दर्शाता है। ग्राफ में दिए गए मानों का उपयोग करके, दर्शाए गए समय अंतराल के दौरान संधारित्र द्वारा खोई गई ऊर्जा की गणना प्रारंभिक संचित ऊर्जा के प्रतिशत के रूप में करें। (_) % (उदाहरण प्रारूप: 45.67)'
        self.description_kazakh = 'Конденсатор тұрақты резистор арқылы разрядталады. Графикте конденсатордағы V потенциалдар айырымының t уақытқа тәуелділігі көрсетілген. Графиктегі мәндерді пайдаланып, көрсетілген уақыт аралығында конденсатор жоғалтқан энергияны жинақталған бастапқы энергияның пайызы ретінде есептеңіз. (_) %(Мысал форматы: 45.67)'
        self.description_swahili = 'Kapasita inatoa chaji kupitia kinza thabiti. Grafu inaonyesha badiliko la tofauti ya potensheli V dhidi ya muda t kwenye kapasita. Kwa kutumia thamani kutoka kwenye grafu, kokotoa nishati iliyopotea kwenye kapasita katika kipindi cha muda kilichoonyeshwa kama asilimia ya nishati ya awali iliyohifadhiwa. (_) % (Muundo wa mfano: 45.67)'

class Phy164_multi(Phy164):
    def __init__(self):
        super().__init__()
        self.description_chinese = '图中显示了用于研究电容器放电的电路。使用图中显示的数值，计算此电路的时间常数。(_) s。(示例格式：0.01250)'
        self.description_arabic = 'يوضح الشكل دائرة لدراسة تفريغ مكثف.\nباستخدام القيم المعطاة، احسب الثابت الزمني للدائرة.\n(_) s (مثال: 0.01250)'
        self.description_hindi = 'चित्र में संधारित्र के निर्वहन की जांच के लिए प्रयुक्त परिपथ दर्शाया गया है। चित्र में दर्शाए गए मानों का उपयोग करके, इस परिपथ का आवर्तकाल (_) s में ज्ञात कीजिए। (उदाहरण प्रारूप: 0.01250)'
        self.description_kazakh = 'Диаграммада конденсатордың разрядталуын зерттеу үшін қолданылатын тізбек көрсетілген. Диаграммада көрсетілген мәндерді пайдаланып, осы тізбектің уақыт тұрақтысын есептеңіз. (_) s. (Мысал форматы: 0.01250)'
        self.description_swahili = 'Mchoro unaonyesha mzunguko wa umeme unaotumiwa kuchunguza utoaji wa chaji wa kapasita. Kwa kutumia thamani zilizoonyeshwa kwenye mchoro, kokotoa namba thabiti ya muda ya mzunguko huu. (_) s. (Muundo wa mfano: 0.01250)'

class Phy165_multi(Phy165):
    def __init__(self):
        super().__init__()
        self.description_chinese = '通过将开关移至位置 A，电容器通过电阻 P 充电。使用图中显示的电路数值，计算电容器完全充满电时储存的能量。(_) J。(示例格式：8.100e-03)'
        self.description_arabic = 'يُشحن مكثف عبر المقاومة P عند وضع المفتاح في الموضع A.\nاحسب الطاقة المخزنة عند اكتمال الشحن.\n(_) J (مثال: 8.100e-03)'
        self.description_hindi = 'स्विच को स्थिति A पर ले जाने से प्रतिरोधक P के माध्यम से संधारित्र आवेशित होता है। आरेख में दर्शाए गए परिपथ मानों का उपयोग करके, पूर्णतः चार्ज होने पर संधारित्र में संग्रहित ऊर्जा की गणना कीजिए। (_) J। (उदाहरण प्रारूप: 8.100e-03)'
        self.description_kazakh = 'Қосқышты А күйіне ауыстыру арқылы конденсатор P резисторы арқылы зарядталады. Диаграммада көрсетілген тізбек мәндерін пайдаланып, конденсатор толық зарядталған кезде онда жинақталған энергияны есептеңіз. (_) J. (Мысал форматы: 8.100e-03)'
        self.description_swahili = 'Kapasita inachajiwa kupitia kinza P kwa kusogeza swichi hadi nafasi A. Kwa kutumia thamani za mzunguko zilizoonyeshwa kwenye mchoro, kokotoa nishati iliyohifadhiwa kwenye kapasita inapokuwa imejaa chaji kikamilifu. (_) J. (Muundo wa mfano: 8.100e-03)'

class Phy166_multi(Phy166):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一根直导体放置在匀强磁场中。使用图中提供的值，计算作用在导体上的磁场力。(_) N。(示例格式：0.012)'
        self.description_arabic = 'يوضع موصل مستقيم في مجال مغناطيسي منتظم كما هو موضح.\nباستخدام القيم المعطاة، احسب القوة المغناطيسية المؤثرة على الموصل.\n(_) N (مثال: 0.012)'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक सीधा चालक एकसमान चुंबकीय क्षेत्र में रखा गया है। आरेख में दिए गए मानों का उपयोग करके चालक पर लगने वाले चुंबकीय बल की गणना करें। (_) N। (उदाहरण प्रारूप: 0.012)'
        self.description_kazakh = 'Түзу өткізгіш көрсетілгендей біртекті магнит өрісіне орналастырылған. Диаграммада берілген мәндерді пайдаланып, өткізгішке әсер ететін магнит күшін есептеңіз. (_) N. (Мысал форматы: 0.012)'
        self.description_swahili = 'Kipitishio kilichonyooka kimewekwa kwenye uga sawia wa sumaku kama inavyoonyeshwa. Kwa kutumia thamani zilizotolewa kwenye mchoro, kokotoa kani ya sumaku inayokaimu kipitishio hicho. (_) N. (Muundo wa mfano: 0.012)'

class Phy167_multi(Phy167):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根载流导体被放置在与匀强磁场成直角的位置。根据图中显示的数值，作用在导体上的磁场力是多少？(_) N (示例格式：0.06789)'
        self.description_arabic = 'يوضع موصل يمر فيه تيار بزاوية قائمة على مجال مغناطيسي منتظم.\nبناءً على القيم الموضحة في الشكل، احسب القوة المغناطيسية المؤثرة على الموصل.\n(_) N (مثال: 0.06789)'
        self.description_hindi = 'एक धारावाही चालक को एकसमान चुंबकीय क्षेत्र के समकोण पर रखा गया है। चित्र में दर्शाए गए मानों के आधार पर, चालक पर लगने वाला चुंबकीय बल क्या है? (_) N (उदाहरण प्रारूप: 0.06789)'
        self.description_kazakh = 'Тогы бар өткізгіш біртекті магнит өрісіне тік бұрышпен орналастырылған. Диаграммада көрсетілген мәндер негізінде өткізгішке әсер ететін магнит күші қандай? (_) N (Мысал форматы: 0.06789)'
        self.description_swahili = 'Kipitishio kinachobeba mkondo kimewekwa pembe mraba (perpendicular) kwenye uga sawia wa sumaku. Kulingana na thamani zilizoonyeshwa kwenye mchoro, ni ipi kani ya sumaku inayokaimu kipitishio hicho? (_) N (Muundo wa mfano: 0.06789)'

class Phy168_multi(Phy168):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一根载流导体被放置在匀强磁场中。根据图中提供的值，计算作用在导体上的磁场力。(_) N (示例格式：0.07890)'
        self.description_arabic = 'يوضع موصل يمر فيه تيار في مجال مغناطيسي منتظم كما هو موضح.\nباستخدام القيم المعطاة، احسب القوة المغناطيسية المؤثرة على الموصل.\n(_) N (مثال: 0.07890)'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक धारावाही चालक को एकसमान चुंबकीय क्षेत्र में रखा गया है। आरेख में दिए गए मानों के आधार पर चालक पर लगने वाले चुंबकीय बल की गणना कीजिए। (_) N (उदाहरण प्रारूप: 0.07890)'
        self.description_kazakh = 'Тогы бар өткізгіш көрсетілгендей біртекті магнит өрісіне орналастырылған. Диаграммада берілген мәндер негізінде өткізгішке әсер ететін магнит күшін есептеңіз. (_) N (Мысал форматы: 0.07890)'
        self.description_swahili = f'Kipitishio kinachobeba mkondo kimewekwa kwenye uga sawia wa sumaku kama inavyoonyeshwa. Kulingana na thamani zilizotolewa kwenye mchoro, kokotoa kani ya sumaku inayokaimu kipitishio hicho. (_) N (Muundo wa mfano: 0.07890)'

class Phy169_multi(Phy169):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个矩形线圈 ABCD 放置在匀强磁场中。使用图中提供的值，计算作用在边 AB 上的磁场力的大小。(_) N (示例格式：0.1234)'
        self.description_arabic = 'توضع حلقة سلكية مستطيلة ABCD في مجال مغناطيسي منتظم كما هو موضح.\nباستخدام القيم المعطاة، احسب مقدار القوة المغناطيسية المؤثرة على الضلع AB.\n(_) N (مثال: 0.1234)'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक आयताकार तार का लूप ABCD एकसमान चुंबकीय क्षेत्र में रखा गया है। आरेख में दिए गए मानों का उपयोग करके, भुजा AB पर लगने वाले चुंबकीय बल का परिमाण ज्ञात कीजिए। (_) N (उदाहरण प्रारूप: 0.1234)'
        self.description_kazakh = 'ABCD тікбұрышты сым контуры көрсетілгендей біртекті магнит өрісіне орналастырылған. Диаграммада берілген мәндерді пайдаланып, АВ қабырғасына әсер ететін магнит күшінің модулін есептеңіз. (_) N (Мысал форматы: 0.1234)'
        self.description_swahili = 'Kitanzi cha mstatili cha waya ABCD kimewekwa kwenye uga sawia wa sumaku kama inavyoonyeshwa. Kwa kutumia thamani zilizotolewa kwenye mchoro, kokotoa ukubwa wa kani ya sumaku inayokaimu upande wa AB. (_) N (Muundo wa mfano: 0.1234)'

class Phy170_multi(Phy170):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个电子进入均匀磁场。根据图中给出的数值，计算电子圆周运动的半径。（单位：米）（示例格式：0.00123）'
        self.description_arabic = 'يدخل إلكترون مجالًا مغناطيسيًا منتظمًا كما هو موضح.\nباستخدام القيم المعطاة، احسب نصف قطر المسار الدائري للإلكترون.\n(_) m (مثال: 0.00123)'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक इलेक्ट्रॉन एकसमान चुंबकीय क्षेत्र में प्रवेश करता है। आरेख में दिए गए मानों के आधार पर, इलेक्ट्रॉन के वृत्ताकार पथ की त्रिज्या की गणना कीजिए। (_) m (उदाहरण प्रारूप: 0.00123)'
        self.description_kazakh = 'Электрон көрсетілгендей біртекті магнит өрісіне енеді. Сызбада берілген мәндерге сүйене отырып, электронның шеңберлік траекториясының радиусын есептеңіз. (_) м (Мысалы: 0.00123)'
        self.description_swahili = 'Elektroni inaingia kwenye uga sawia wa sumaku kama inavyoonyeshwa. Kulingana na thamani zilizotolewa kwenye mchoro, kokotoa nusukipenyo cha njia ya duara ya elektroni hiyo. (_) m (Muundo wa mfano: 0.00123)'

class Phy171_multi(Phy171):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个点电荷放置在真空中。根据图中提供的值，计算 P 点的电场强度 E。(_) V m^-1 (示例格式：1234.2345)'
        self.description_arabic = 'توضع شحنة نقطية في فراغ كما هو موضح.\nباستخدام القيم المعطاة، احسب شدة المجال الكهربائي $E$ عند النقطة P.\n(_) V m^-1 (مثال: 1234.2345)'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक बिंदु चार्ज को निर्वात में रखा गया है। आरेख में दिए गए मानों के आधार पर, बिंदु P पर विद्युत क्षेत्र की तीव्रता E की गणना कीजिए। (_) V m^-1 (उदाहरण प्रारूप: 1234.2345)'
        self.description_kazakh = 'Нүктелік заряд көрсетілгендей вакуумге орналастырылған. Диаграммада берілген мәндер негізінде P нүктесіндегі электр өрісінің E кернеулігін есептеңіз. (_) V m^-1 (Мысал форматы: 1234.2345)'
        self.description_swahili = 'Chaji ya nukta imewekwa kwenye ombwe kama inavyoonyeshwa. Kulingana na thamani zilizotolewa kwenye mchoro, kokotoa ukali wa uga wa umeme E katika nukta P. (_) V m^-1 (Muundo wa mfano: 1234.2345)'

class Phy172_multi(Phy172):
    def __init__(self):
        super().__init__()
        self.description_chinese = "如图所示，两个点电荷，一个为 +Q，一个为 -Q，它们相隔一定距离。根据图中提供的值，计算两电荷中点处净电场强度的大小。假设库仑常数为 8.99 × 10^9 N m^2 C^-2。(_) V m^-1 (示例格式：12345.2)"
        self.description_arabic = "شحنتان نقطيتان، إحداهما +Q والأخرى -Q، تفصل بينهما مسافة كما هو موضح.\nباستخدام القيم المعطاة، احسب مقدار شدة المجال الكهربائي المحصل عند نقطة المنتصف.\nافترض أن ثابت كولوم يساوي $8.99 \\times 10^9$ N m$^2$ C$^{-2}$.\n(_) V m^-1 (مثال: 12345.2)"
        self.description_hindi = "दो बिंदु चार्ज, एक +Q और एक -Q, चित्र में दर्शाई गई दूरी पर अलग-अलग रखे गए हैं। आरेख में दिए गए मानों के आधार पर, चार्ज के मध्यबिंदु पर कुल विद्युत क्षेत्र की तीव्रता का परिमाण ज्ञात कीजिए। मान लीजिए कि कूलम्ब (Coulomb) का स्थिरांक 8.99 × 10^9 N m^2 C^-2 है। (_) V m^-1 (उदाहरण प्रारूप: 12345.2)"
        self.description_kazakh = "Екі нүктелік заряд, біреуі +Q және біреуі -Q, көрсетілгендей қашықтықта орналасқан. Диаграммада берілген мәндер негізінде зарядтар арасындағы ортаңғы нүктедегі қорытқы электр өрісінің кернеулігінің модулін есептеңіз. Кулон тұрақтысын 8.99 × 10^9 N m^2 C^-2 деп алыңыз. (_) V m^-1 (Мысал форматы: 12345.2)"
        self.description_swahili = "Chaji mbili za nukta, moja +Q na moja -Q, zimetenganishwa kwa umbali kama inavyoonyeshwa. Kulingana na thamani zilizotolewa kwenye mchoro, kokotoa ukubwa wa ukali wa uga wa umeme tokeo katika nukta ya katikati ya chaji hizo. Tumia namba thabiti ya Coulomb kama 8.99 × 10^9 N m^2 C^-2. (_) V m^-1 (Muundo wa mfano: 12345.2)"

class Phy173_multi(Phy173):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个带电量为 q 的粒子以速度 v 进入匀强磁场 B 中。根据图中提供的值，计算作用在粒子上的磁场力的大小。(_) N (示例格式：1.23E-16)'
        self.description_arabic = 'يدخل جسيم بشحنة $q$ مجالًا مغناطيسيًا منتظمًا $B$ بسرعة $v$ كما هو موضح.\nباستخدام القيم المعطاة، احسب مقدار القوة المغناطيسية المؤثرة على الجسيم.\n(_) N (مثال: 1.23E-16)'
        self.description_hindi = 'चित्र में दिखाए अनुसार चार्ज q वाला एक कण एकसमान चुंबकीय क्षेत्र B में वेग v से प्रवेश करता है। आरेख में दिए गए मानों के आधार पर कण पर लगने वाले चुंबकीय बल का परिमाण ज्ञात कीजिए। (_) N (उदाहरण प्रारूप: 1.23E-16)'
        self.description_kazakh = 'q заряды бар бөлшек v жылдамдығымен көрсетілгендей біртекті В магнит өрісіне енеді. Диаграммада берілген мәндер негізінде бөлшекке әсер ететін магнит күшінің модулін есептеңіз. (_) N (Мысал форматы: 1.23E-16)'
        self.description_swahili = 'Chembe yenye chaji q inaingia kwenye uga sawia wa sumaku B kwa kasi v kama inavyoonyeshwa. Kulingana na thamani zilizotolewa kwenye mchoro, kokotoa ukubwa wa kani ya sumaku inayokaimu chembe hiyo. (_) N (Muundo wa mfano: 1.23E-16)'

class Phy174_multi(Phy174):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一根导体以垂直于磁场 B 的速度运动。计算感应电动势。(_) V (示例格式：11.234)'
        self.description_arabic = 'يتحرك موصل طوله $l$ بسرعة عمودية على مجال مغناطيسي $B$.\nاحسب القوة الدافعة الكهربائية المستحثة.\n(_) V (مثال: 11.234)'
        self.description_hindi = 'लंबाई का एक चालक चुंबकीय क्षेत्र B के लंबवत गति से गति करता है। प्रेरित emf की गणना कीजिए। (_) V (उदाहरण प्रारूप: 11.234)'
        self.description_kazakh = 'Ұзындығы бар өткізгіш В магнит өрісіне перпендикуляр жылдамдықпен қозғалады. Индукцияланған ЭҚК-ін есептеңіз. (_) V (Мысал форматы: 11.234)'
        self.description_swahili = 'Kipitishio chenye urefu L kinasonga kwa kasi v perpendicular (kwenye pembe mraba) na uga wa sumaku B. Kokotoa Nguvu Mwendo-Umeme (N.M.U) kishawishi. (_) V (Muundo wa mfano: 11.234)'

class Phy175_multi(Phy175):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个 N 匝的线圈放置在变化的磁场中。使用图中提供的值，计算感应电动势的大小。(_) V (示例格式：11.234)'
        self.description_arabic = 'يوضع ملف مكون من $N$ لفة في مجال مغناطيسي متغير كما هو موضح.\nباستخدام القيم المعطاة، احسب مقدار القوة الدافعة الكهربائية المستحثة.\n(_) V (مثال: 11.234)'
        self.description_hindi = 'चित्र में दिखाए अनुसार, N फेरों वाली एक कएल को बदलते हुए चुंबकीय क्षेत्र में रखा गया है। आरेख में दिए गए मानों का उपयोग करके प्रेरित विद्युत e.m.f का परिमाण ज्ञात कीजिए। (_) V (उदाहरण प्रारूप: 11.234)'
        self.description_kazakh = 'N орамды катушка көрсетілгендей айнымалы магнит өрісіне орналастырылған. Диаграммада берілген мәндерді пайдаланып, индукцияланған ЭҚК-інің модулін есептеңіз. (_) V (Мысал форматы: 11.234)'
        self.description_swahili = 'Koili yenye mizunguko N imewekwa kwenye uga wa sumaku unaobadilika kama inavyoonyeshwa. Kwa kutumia thamani zilizotolewa kwenye mchoro, kokotoa ukubwa wa Nguvu Mwendo-Umeme (N.M.U) kishawishi. (_) V (Muundo wa mfano: 11.234)'

class Phy176_multi(Phy176):
    def __init__(self):
        super().__init__()
        self.description_chinese ='如图所示，一个矩形线圈在均匀磁场中旋转。根据图中给出的数值，计算感应电动势峰值（单位：V）。'
        self.description_arabic = 'يدور ملف مستطيل في مجال مغناطيسي منتظم كما هو موضح.\nباستخدام القيم المعطاة، احسب القيمة العظمى للقوة الدافعة الكهربائية المستحثة.\n(_) V'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक आयताकार कएल एकसमान चुंबकीय क्षेत्र में घूमती है। आरेख में दिए गए मानों के आधार पर, अधिकतम प्रेरित विद्युत बल e.m.f की गणना कीजिए। (_) V'
        self.description_kazakh = 'Тіктөртбұрышты катушка көрсетілгендей біртекті магнит өрісінде айналады. Сызбада берілген мәндерге сүйене отырып, максималды индукциялық ЭҚК-ні есептеңіз. (_) В'
        self.description_swahili = 'Koili ya mstatili inazunguka kwenye uga sawia wa sumaku kama inavyoonyeshwa. Kulingana na thamani zilizotolewa kwenye mchoro, kokotoa kilele cha Nguvu Mwendo-Umeme (N.M.U) kishawishi. (_) V'

class Phy177_multi(Phy177):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一个交流电压的峰值为 V。计算其有效值电压。(_) V（示例格式：123.45）'
        self.description_arabic = f'جهد متردد له قيمة عظمى $V$.\nاحسب قيمة الجذر التربيعي لمتوسط المربعات (RMS).\n(_) V (مثال: 123.45)'
        self.description_hindi = f'एक प्रत्यावर्ती वोल्टेज का अधिकतम मान V है। इसका वास्तविक प्रतिवर्ती वोल्टेज (RMS) ज्ञात कीजिए। (_) V (उदाहरण प्रारूप: 123.45)'
        self.description_kazakh = f'Айнымалы кернеудің максималды (шыңдық) мәні V-ға тең. Кернеудің әсерлік (RMS) мәнін есептеңіз. (_) В (Мысалы: 123.45)'
        self.description_swahili = 'Voltaji geugeu ina thamani ya kilele ya V. Kokotoa voltaji ya RMS. (_) V (Muundo wa mfano: 123.45)'

class Phy178_multi(Phy178):
    def __init__(self):
        super().__init__()
        self.description_chinese = f'一交变电流的有效值 (RMS) 为 {self.I_rms} A。计算峰值电流。(_) A (示例格式：12.34)'
        self.description_arabic = f'تيار متردد له قيمة فعالة (RMS) مقدارها {self.I_rms} A.\nاحسب قيمة تيار الذروة.\n(_) A (مثال: 12.34)'
        self.description_hindi = f'एक प्रत्यावर्ती धारा का RMS मान {self.I_rms} A है। शिखर धारा की गणना कीजिए। (_) A (उदाहरण प्रारूप: 12.34)'
        self.description_kazakh = f'Айнымалы токтың әсерлік мәні {self.I_rms} А. Максимал токты есептеңіз. (_) A (Мысал форматы: 12.34)'
        self.description_swahili = f'Mkondo geugeu una thamani ya RMS ya {self.I_rms} A. Kokotoa thamani ya kilele ya mkondo huo. (_) A (Muundo wa mfano: 12.34)'

class Phy179_multi(Phy179):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，一个平滑电容器连接在桥式整流器的输出端。使用图中提供的参数，求输出的纹波电压。(_) V (示例格式：12.34)'
        self.description_arabic = 'مكثف تنعيم موصول بمخرج مقوم قنطري كما هو موضح.\nباستخدام المعطيات، أوجد جهد التموج عند الخرج.\n(_) V (مثال: 12.34)'
        self.description_hindi = 'चित्र में दिखाए अनुसार एक स्मूथिंग कैपेसिटर को ब्रिज रेक्टिफायर के आउटपुट से जोड़ा गया है। आरेख में दिए गए मापदंडों का उपयोग करके आउटपुट के रिपल वोल्टेज का निर्धारण करें। (_) V (उदाहरण प्रारूप: 12.34)'
        self.description_kazakh = 'Тегістеуші конденсатор көрсетілгендей көпірлік түзеткіштің шығысына қосылған. Диаграммада берілген параметрлерді пайдаланып, шығыстағы пульсация кернеуін анықтаңыз. (_) V (Мысал форматы: 12.34)'
        self.description_swahili = 'Kapasita kichujio imeunganishwa kwenye pato la kirekebishaji daraja kama inavyoonyeshwa. Kwa kutumia vigezo vilivyotolewa kwenye mchoro, ainisha voltaji ya mparuzano (ripple voltage) ya pato hilo. (_) V (Muundo wa mfano: 12.34)'

class Phy180_multi(Phy180):
    def __init__(self):
        super().__init__()
        self.description_chinese = "计算图中所示的光子的能量。取普朗克常量 $h = 6.63 \\times 10^{-34}$ J s。(_) J (示例格式：2.652e-19)"
        self.description_arabic = "احسب طاقة الفوتون الموضح في الشكل.\nخذ ثابت بلانك $h = 6.63 \\times 10^{-34}$ J s.\n(_) J (مثال: 2.652e-19)"
        self.description_hindi = "चित्र में दर्शाए गए फोटॉन की ऊर्जा की गणना कीजिए। प्लैंक (Planck) स्थिरांक $h = 6.63 \\times 10^{-34}$ J s। (_) J (उदाहरण प्रारूप: 2.652e-19)"
        self.description_kazakh = "Диаграммада көрсетілген фотонның энергиясын есептеңіз. Планк тұрақтысын $h = 6.63 \\times 10^{-34}$ J s деп алыңыз. (_) J (Мысал форматы: 2.652e-19)"
        self.description_swahili = "Kokotoa nishati ya fotoni iliyoonyeshwa kwenye mchoro. Tumia namba thabiti ya Planck $h = 6.63 \\times 10^{-34}$ J s. (_) J (Muundo wa mfano: 2.652e-19)"

class Phy181_multi(Phy181):
    def __init__(self):
        super().__init__()
        self.description_chinese = "计算图中所示波长的光子的动量。取普朗克常量 h = 6.63 × 10^{-34} J s。(_) kg m s^-1 (示例格式：1.6575e-27)"
        self.description_arabic = "احسب زخم الفوتون ذي الطول الموجي الموضح في الشكل.\nخذ ثابت بلانك $h = 6.63 \\times 10^{-34}$ J s.\n(_) kg m s^-1 (مثال: 1.6575e-27)"
        self.description_hindi = "आरेख में दर्शाई गई तरंगदैर्ध्य वाले फोटॉन के संवेग की गणना कीजिए। प्लांक (Planck) स्थिरांक h = 6.63 × 10^{-34} J s लीजिए। (_) kg m s^-1 (उदाहरण प्रारूप: 1.6575e-27)"
        self.description_kazakh = "Диаграммада көрсетілген толқын ұзындығына ие фотонның импульсін есептеңіз. Планк тұрақтысын h = 6.63 × 10^{-34} J s деп алыңыз. (_) kg m s^-1 (Мысал форматы: 1.6575e-27)"
        self.description_swahili = "Kokotoa momenta ya fotoni yenye urefu wa wimbi ulioonyeshwa kwenye mchoro. Tumia namba thabiti ya Planck h = 6.63 × 10^{-34} J s. (_) kg m s^-1 (Muundo wa mfano: 1.6575e-27)"

class Phy182_multi(Phy182):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，光照射在金属表面上。计算发射的光电子的最大动能。(_) J (示例格式：1.318e-19)'
        self.description_arabic = 'يسقط الضوء على سطح معدني كما هو موضح.\nاحسب أقصى طاقة حركية للإلكترونات المنبعثة.\n(_) J (مثال: 1.318e-19)'
        self.description_hindi = 'चित्र में दर्शाए अनुसार प्रकाश एक धातु की सतह पर पड़ता है। उत्सर्जित फोटोइलेक्ट्रॉनों की अधिकतम गतिज ऊर्जा की गणना कीजिए। (_) J (उदाहरण प्रारूप: 1.318e-19)'
        self.description_kazakh = 'Жарық диаграммада көрсетілгендей металл бетіне түседі. Ұшып шыққан фотоэлектрондардың максимал кинетикалық энергиясын есептеңіз. (_) J (Мысал форматы: 1.318e-19)'
        self.description_swahili = 'Mwanga unaangaza kwenye uso wa metali kama inavyoonyeshwa kwenye mchoro. Kokotoa nishati ya mwendo ya juu zaidi (maximum kinetic energy) ya fotoelektroni zilizotolewa. (_) J (Muundo wa mfano: 1.318e-19)'

class Phy183_multi(Phy183):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据图中提供的实验数据，求使光电流降为零所需的截止电压 $V_s$。(_) V (示例格式：1.25)'
        self.description_arabic = 'بناءً على البيانات التجريبية الموضحة، أوجد جهد الإيقاف $V_s$ الذي يجعل التيار الكهروضوئي يساوي صفرًا.\n(_) V (مثال: 1.25)'
        self.description_hindi = 'आरेखों में दिए गए प्रायोगिक आंकड़ों के आधार पर, फोटोकरंट को शून्य तक कम करने के लिए आवश्यक स्टॉपिंग पोटेंशियल $V_s$ ज्ञात कीजिए। (_) V (उदाहरण प्रारूप: 1.25)'
        self.description_kazakh = 'Диаграммаларда берілген эксперименттік мәліметтер негізінде фототокты нөлге дейін төмендету үшін қажетті тежеуші потенциалды $V_s$ анықтаңыз. (_) V (Мысал форматы: 1.25)'
        self.description_swahili = 'Kulingana na data ya majaribio iliyotolewa kwenye michoro, ainisha potensheli ya kuzuia $V_s$ inayohitajika kupunguza fotomkondo kuwa sifuri. (_) V (Muundo wa mfano: 1.25)'

class Phy184_multi(Phy184):
    def __init__(self):
        super().__init__()
        self.description_chinese = '计算与图中所示电子相关的德布罗意波长。(_) m (示例格式：1.455e-10)'
        self.description_arabic = 'احسب طول موجة دي برولي المرتبطة بالإلكترون الموضح في الشكل.\n(_) m (مثال: 1.455e-10)'
        self.description_hindi = 'चित्र में दर्शाए गए इलेक्ट्रॉन से संबंधित डी ब्रोगली (Broglie) तरंगदैर्घ्य की गणना कीजिए। (_) m (उदाहरण प्रारूप: 1.455e-10)'
        self.description_kazakh = 'Диаграммада көрсетілген электронға сәйкес де Бройль толқын ұзындығын есептеңіз. (_) m (Мысал форматы: 1.455e-10)'
        self.description_swahili = 'Kokotoa urefu wa wimbi la de Broglie unaohusishwa na elektroni iliyoonyeshwa kwenye mchoro. (_) m (Muundo wa mfano: 1.455e-10)'

class Phy185_multi(Phy185):
    def __init__(self):
        super().__init__()
        self.description_chinese = '如图所示，原子中两个能级之间的电子跃迁导致光子的发射。计算这两个能级之间的能量差 $\\Delta E$。(_) J (示例格式：3.315e-19)'
        self.description_arabic = 'يؤدي انتقال إلكترون بين مستويي طاقة إلى انبعاث فوتون كما هو موضح.\nاحسب فرق الطاقة $\\Delta E$.\n(_) J (مثال: 3.315e-19)'
        self.description_hindi = 'परमाणु में दो ऊर्जा स्तरों के बीच इलेक्ट्रॉन संक्रमण के परिणामस्वरूप एक फोटॉन का उत्सर्जन होता है, जैसा कि चित्र में दिखाया गया है। इन दो स्तरों के बीच ऊर्जा अंतर $\\Delta E$ की गणना कीजिए। (_) J (उदाहरण प्रारूप: 3.315e-19)'
        self.description_kazakh = 'Атомдағы екі энергетикалық деңгей арасындағы электрон ауысуы диаграммада көрсетілгендей фотонның шығарылуына әкеледі. Осы екі деңгей арасындағы энергия айырымын $\\Delta E$ есептеңіз. (_) J (Мысал форматы: 3.315e-19)'
        self.description_swahili = 'Mpito wa elektroni kati ya viwango viwili vya nishati katika atomi unasababisha utoaji wa fotoni kama inavyoonyeshwa kwenye mchoro. Kokotoa tofauti ya nishati $\\Delta E$ kati ya viwango hivi viwili. (_) J (Muundo wa mfano: 3.315e-19)'

class Phy186_multi(Phy186):
    def __init__(self):
        super().__init__()
        self.description_chinese = '氢原子中的电子跃迁释放了如图所示的能量。计算发射光谱线的波长 $\\lambda$。(_) m (示例格式：4.567e-07)'
        self.description_arabic = 'يؤدي انتقال إلكترون في ذرة الهيدروجين إلى انبعاث طاقة كما هو موضح.\nاحسب الطول الموجي $\\lambda$ للخط الطيفي المنبعث.\n(_) m (مثال: 4.567e-07)'
        self.description_hindi = 'चित्र में दर्शाए अनुसार हाइड्रोजन परमाणु में इलेक्ट्रॉन संक्रमण से ऊर्जा मुक्त होती है। उत्सर्जित वर्णक्रमीय रेखा की तरंगदैर्घ्य $\\lambda$ की गणना कीजिए। (_) m (उदाहरण प्रारूप: 4.567e-07)'
        self.description_kazakh = 'Сутегі атомындағы электрон ауысуы диаграммада көрсетілгендей энергия бөледі. Шығарылған спектрлік сызықтың толқын ұзындығын $\\lambda$ есептеңіз. (_) m (Мысал форматы: 4.567e-07)'
        self.description_swahili = 'Mpito wa elektroni katika atomi ya haidrojeni unatoa nishati kama inavyoonyeshwa kwenye mchoro. Kokotoa urefu wa wimbi $\\lambda$ wa mstari wa spektra uliotolewa. (_) m (Muundo wa mfano: 4.567e-07)'

class Phy187_multi(Phy187):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据图中提供的数据，计算原子核的质量亏损。(_) kg (示例格式：3.45e-29)'
        self.description_arabic = 'بناءً على البيانات الموضحة، احسب النقص في الكتلة للنواة.\n(_) kg (مثال: 3.45e-29)'
        self.description_hindi = 'आरेख में दिए गए आंकड़ों के आधार पर, नाभिक के द्रव्यमान दोष की गणना कीजिए। (_) kg (उदाहरण प्रारूप: 3.45e-29)'
        self.description_kazakh = 'Диаграммада берілген мәліметтер негізінде ядроның масса ақауын есептеңіз. (_) kg (Мысал форматы: 3.45e-29)'
        self.description_swahili = 'Kulingana na data iliyotolewa kwenye mchoro, kokotoa hitilafu ya masi (mass defect) ya nyukliasi hiyo. (_) kg (Muundo wa mfano: 3.45e-29)'

class Phy188_multi(Phy188):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据图中显示的质量亏损和常数，计算原子核的结合能。(_) J (示例格式：1.23e-11)'
        self.description_arabic = 'بناءً على النقص في الكتلة والثوابت الموضحة في الشكل، احسب طاقة الربط النووي.\n(_) J (مثال: 1.23e-11)'
        self.description_hindi = 'आरेख में दर्शाए गए द्रव्यमान दोष और स्थिरांकों के आधार पर, नाभिकीय बंधन ऊर्जा की गणना कीजिए। (_) J (उदाहरण प्रारूप: 1.23e-11)'
        self.description_kazakh = 'Диаграммада көрсетілген масса ақауы мен тұрақтылар негізінде ядроның байланыс энергиясын есептеңіз. (_) J (Мысал форматы: 1.23e-11)'
        self.description_swahili = 'Kulingana na hitilafu ya masi na namba thabiti zilizoonyeshwa kwenye mchoro, kokotoa nishati ya muungano wa nyuklia (nuclear binding energy). (_) J (Muundo wa mfano: 1.23e-11)'

class Phy189_multi(Phy189):
    def __init__(self):
        super().__init__()
        self.description_chinese = '一个放射性样本随时间衰变。根据图中提供的数据，计算在指示的目标时间剩余的原子核的确切数量。(_) 原子核 (示例格式：125.00)'
        self.description_arabic = 'تتحلل عينة مشعة بمرور الزمن.\nباستخدام البيانات من الشكل، احسب العدد الدقيق للأنوية المتبقية عند الزمن المحدد.\n(_) (مثال: 125.00)'
        self.description_hindi = 'एक रेडियोधर्मी नमूना समय के साथ क्षय होता है। ग्राफ में दिए गए आंकड़ों के आधार पर, निर्दिष्ट समय पर शेष नाभिकों की सटीक संख्या की गणना करें। (_) nuclei (उदाहरण प्रारूप: 125.00)'
        self.description_kazakh = 'Радиоактивті үлгі уақыт өте келе ыдырайды. Графикте берілген мәліметтер негізінде көрсетілген мақсатты уақытта қалған ядролардың нақты санын есептеңіз. (_) ядро (Мысал форматы: 125.00)'
        self.description_swahili = 'Sampuli ya redioaktivi inamomonyoka kadri muda unavyopita. Kulingana na data iliyotolewa kwenye grafu, kokotoa idadi kamili ya nyukliasi zilizosalia katika muda lengwa ulioonyeshwa. (_) nyukliasi (Muundo wa mfano: 125.00)'

class Phy190_multi(Phy190):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据图中显示的实验装置数据，计算放射性样本的活度，以贝克勒尔 (Bq) 为单位。(_) Bq (示例格式：5.99e+10)'
        self.description_arabic = 'بناءً على بيانات الإعداد التجريبي الموضحة في الشكل، احسب نشاط العينة المشعة بوحدة البيكريل (Bq).\n(_) Bq (مثال: 5.99e+10)'
        self.description_hindi = 'आरेख में दर्शाए गए प्रायोगिक सेटअप डेटा के आधार पर, रेडियोधर्मी नमूने की सक्रियता को Becquerels (Bq) में ज्ञात कीजिए। (_) Bq (उदाहरण प्रारूप: 5.99e+10)'
        self.description_kazakh = 'Диаграммада көрсетілген эксперименталды қондырғы мәліметтері негізінде радиоактивті үлгінің активтілігін Беккерельмен (Bq) есептеңіз. (_) Bq (Мысал форматы: 5.99e+10)'
        self.description_swahili = 'Kulingana na data ya mipangilio ya jaribio iliyoonyeshwa kwenye mchoro, kokotoa utendaji (activity) wa sampuli ya redioaktivi katika Becquerels (Bq). (_) Bq (Muundo wa mfano: 5.99e+10)'

class Phy191_multi(Phy191):
    def __init__(self):
        super().__init__()
        self.description_chinese = '超声波脉冲被发射到软组织中。根据图中提供的回声时间和声速，计算反射体的深度。(_) m (示例格式：0.63987)'
        self.description_arabic = 'تُرسل نبضة موجات فوق صوتية داخل الأنسجة الرخوة.\nباستخدام زمن الصدى وسرعة الصوت، احسب عمق السطح العاكس.\n(_) m (مثال: 0.63987)'
        self.description_hindi = 'नरम ऊतक में अल्ट्रासाउंड तरंग उत्सर्जित की जाती है। आरेख में दिए गए प्रतिध्वनि समय और ध्वनि की गति के आधार पर परावर्तक की गहराई की गणना कीजिए। (_) m (उदाहरण प्रारूप: 0.63987)'
        self.description_kazakh = 'Ультрадыбыстық импульс жұмсақ тінге жіберіледі. Диаграммада берілген жаңғырық уақыты мен дыбыс жылдамдығы негізінде шағылдырғыштың тереңдігін есептеңіз. (_) m (Мысал форматы: 0.63987)'
        self.description_swahili = 'Mpwito wa altrasauti unatumwa kwenye tishu laini. Kulingana na muda wa mwangwi na kasi ya sauti iliyotolewa kwenye mchoro, kokotoa kina cha kiakisio. (_) m (Muundo wa mfano: 0.63987)'

class Phy192_multi(Phy192):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据图中换能器的频率和超声波速度，计算组织中波的波长 $\\lambda$。(_) m (示例格式：0.00385)'
        self.description_arabic = 'باستخدام تردد المحول وسرعة الموجات فوق الصوتية في الشكل، احسب الطول الموجي $\\lambda$.\n(_) m (مثال: 0.00385)'
        self.description_hindi = 'आरेख में ट्रांसड्यूसर की आवृत्ति और अल्ट्रासाउंड की गति के आधार पर, ऊतक में तरंगों की तरंगदैर्घ्य $\\lambda$ की गणना कीजिए। (_) m (उदाहरण प्रारूप: 0.00385)'
        self.description_kazakh = 'Диаграммадағы түрлендіргіш жиілігі мен ультрадыбыстың жылдамдығы негізінде тіндегі толқындардың толқын ұзындығын $\\lambda$ есептеңіз. (_) m (Мысал форматы: 0.00385)'
        self.description_swahili = 'Kulingana na marudio (frequency) ya transdyusa na kasi ya altrasauti kwenye mchoro, kokotoa urefu wa wimbi $\\lambda$ wa mawimbi hayo ndani ya tishu. (_) m (Muundo wa mfano: 0.00385)'

class Phy193_multi(Phy193):
    def __init__(self):
        super().__init__()
        self.description_chinese = '计算图中发射的X射线光子的能量。(_) J (示例格式：1.23e-15)'
        self.description_arabic = 'احسب طاقة فوتون الأشعة السينية الموضح في الشكل.\n(_) J (مثال: 1.23e-15)'
        self.description_hindi = 'चित्र में उत्सर्जित X-ray फोटॉन की ऊर्जा की गणना कीजिए। (_) J (उदाहरण प्रारूप: 1.23e-15)'
        self.description_kazakh = 'Диаграммада шығарылған рентген фотонының энергиясын есептеңіз. (_) J (Мысал форматы: 1.23e-15)'
        self.description_swahili = 'Kokotoa nishati ya fotoni ya eksirei (X-ray) iliyotolewa kwenye mchoro. (_) J (Muundo wa mfano: 1.23e-15)'

class Phy194_multi(Phy194):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据X射线光谱图中提供的加速电势，计算发射的X射线的最小波长 $\\lambda_{min}$。(_) m (示例格式：1.24e-11)'
        self.description_arabic = 'باستخدام جهد التسريع في طيف الأشعة السينية، احسب الطول الموجي الأدنى $\\lambda_{min}$.\n(_) m (مثال: 1.24e-11)'
        self.description_hindi = 'X-ray स्पेक्ट्रम आरेख में दिए गए त्वरण विभव के आधार पर, उत्सर्जित X-ray की न्यूनतम तरंगदैर्ध्य $\\lambda_{min}$ की गणना कीजिए। (_) m (उदाहरण प्रारूप: 1.24e-11)'
        self.description_kazakh = 'Рентген спектрі диаграммасында берілген үдетуші потенциал негізінде шығарылған рентген сәулелерінің минимал толқын ұзындығын $\\lambda_{min}$ есептеңіз. (_) m (Мысал форматы: 1.24e-11)'
        self.description_swahili = 'Kulingana na potensheli ya mchapuko iliyotolewa kwenye mchoro wa spektra ya eksirei, kokotoa urefu wa wimbi wa chini zaidi $\\lambda_{min}$ wa eksirei zilizotolewa. (_) m (Muundo wa mfano: 1.24e-11)'

class Phy195_multi(Phy195):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据图中提供的天文数据，计算到该恒星的距离 $d$。(_) m (示例格式：1.23e+17)'
        self.description_arabic = 'بناءً على البيانات الفلكية في الشكل، احسب المسافة $d$ إلى النجم.\n(_) m (مثال: 1.23e+17)'
        self.description_hindi = 'आरेख में दिए गए खगोलीय आंकड़ों के आधार पर, तारे की दूरी $d$ की गणना कीजिए। (_) m (उदाहरण प्रारूप: 1.23e+17)'
        self.description_kazakh = 'Диаграммада берілген астрономиялық мәліметтер негізінде жұлдызға дейінгі қашықтықты $d$ есептеңіз. (_) m (Мысал форматы: 1.23e+17)'
        self.description_swahili = 'Kulingana na data ya astronomia iliyotolewa kwenye mchoro, kokotoa umbali $d$ hadi kwenye nyota hiyo. (_) m (Muundo wa mfano: 1.23e+17)'

class Phy196_multi(Phy196):
    def __init__(self):
        super().__init__()
        self.description_chinese = "使用图中提供的恒星的光度和表面温度，求该恒星的半径 $R$。(_) m (示例格式：4.81e+10)"
        self.description_arabic = 'باستخدام سطوع النجم ودرجة حرارة سطحه، احسب نصف القطر $R$.\n(_) m (مثال: 4.81e+10)'
        self.description_hindi = "आरेख में दी गई तारे की चमक और सतह के तापमान का उपयोग करके, उसकी त्रिज्या $R$ ज्ञात कीजिए। (_) m (उदाहरण प्रारूप: 4.81e+10)"
        self.description_kazakh = "Диаграммада берілген жұлдыздың жарқырауы мен беттік температурасын пайдаланып, оның радиусын $R$ анықтаңыз. (_) m (Мысал форматы: 4.81e+10)"
        self.description_swahili = "Kwa kutumia luminositi ya nyota na halijoto ya uso iliyotolewa kwenye mchoro, ainisha rediasi yake $R$. (_) m (Muundo wa mfano: 4.81e+10)"

class Phy197_multi(Phy197):
    def __init__(self):
        super().__init__()
        self.description_chinese = "使用维恩位移定律和恒星发射光谱中提供的表面温度，计算峰值波长 $\\lambda_{max}$。(_) m (示例格式：5.89e-07)"
        self.description_arabic = 'باستخدام قانون إزاحة فين ودرجة حرارة السطح، احسب الطول الموجي الأعظمي $\\lambda_{max}$.\n(_) m (مثال: 5.89e-07)'
        self.description_hindi = "वीन (Wien) के विस्थापन नियम और तारकीय उत्सर्जन स्पेक्ट्रम में दिए गए सतही तापमान का उपयोग करके, शिखर तरंगदैर्ध्य $\\lambda_{max}$ की गणना करें। (_) m (उदाहरण प्रारूप: 5.89e-07)"
        self.description_kazakh = "Виннің ығысу заңы мен жұлдыздық сәулелену спектрінде берілген беттік температураны пайдаланып, ең жоғарғы толқын ұзындығын $\\lambda_{max}$ есептеңіз. (_) m (Мысал форматы: 5.89e-07)"
        self.description_swahili = "Kwa kutumia sheria ya mjongeo ya Wien na halijoto ya uso iliyotolewa kwenye spektra ya utoaji ya nyota, kokotoa urefu wa wimbi wa kilele $\\lambda_{max}$. (_) m (Muundo wa mfano: 5.89e-07)"

class Phy198_multi(Phy198):
    def __init__(self):
        super().__init__()
        self.description_chinese = "一个遥远星系的光谱发生红移。使用图中的红移值，计算该星系的退行速度 $v$。(_) m s^-1 (示例格式：5820000.00)"
        self.description_arabic = 'ينزاح طيف مجرة بعيدة نحو الأحمر.\nباستخدام قيمة الانزياح، احسب سرعة التراجع $v$.\n(_) m s^-1 (مثال: 5820000.00)'
        self.description_hindi = "एक दूरस्थ आकाशगंगा का स्पेक्ट्रम रेडशिफ्टेड है। आरेख में दिए गए रेडशिफ्ट मान का उपयोग करके, इस आकाशगंगा के प्रतिगमन वेग $v$ की गणना कीजिए। (_) m s^-1 (उदाहरण प्रारूप: 5820000.00)"
        self.description_kazakh = "Алыстағы галактиканың спектрі қызылға ығысқан. Диаграммадағы қызылға ығысу мәнін пайдаланып, осы галактиканың алыстау жылдамдығын $v$ есептеңіз. (_) m s^-1 (Мысал форматы: 5820000.00)"
        self.description_swahili = "Spektra ya galaksi ya mbali inaonyesha mjongeo nyekundu (redshift). Kwa kutumia thamani ya mjongeo nyekundu kwenye mchoro, kokotoa kasi ya kurudi nyuma $v$ ya galaksi hii. (_) m s^-1 (Muundo wa mfano: 5820000.00)"

class Phy199_multi(Phy199):
    def __init__(self):
        super().__init__()
        self.description_chinese = '根据图中提供的退行速度和哈勃常数，计算到该星系的距离 $d$。(_) m (示例格式：4.84e+24)'
        self.description_arabic = 'باستخدام سرعة التراجع وثابت هابل، احسب المسافة $d$ إلى المجرة.\n(_) m (مثال: 4.84e+24)'
        self.description_hindi = 'आरेख में दी गई प्रतिगमन गति और हबल स्थिरांक के आधार पर, आकाशगंगा की दूरी $d$ की गणना कीजिए। (_) m (उदाहरण प्रारूप: 4.84e+24)'
        self.description_kazakh = 'Диаграммада берілген алыстау жылдамдығы мен Хаббл тұрақтысы негізінде галактикаға дейінгі қашықтықты $d$ есептеңіз. (_) m (Мысал форматы: 4.84e+24)'
        self.description_swahili = 'Kulingana na kasi ya kurudi nyuma na namba thabiti ya Hubble iliyotolewa kwenye mchoro, kokotoa umbali $d$ hadi kwenye galaksi hiyo. (_) m (Muundo wa mfano: 4.84e+24)'

class Phy200_multi(Phy200):
    def __init__(self):
        super().__init__()
        self.description_chinese = '使用图中提供的参数计算该恒星的总光度 $L$。(_) W (示例格式：1.35e+27)'
        self.description_arabic = 'احسب السطوع الكلي $L$ للنجم باستخدام المعطيات.\n(_) W (مثال: 1.35e+27)'
        self.description_hindi = 'आरेख में दिए गए मापदंडों का उपयोग करके तारे की कुल चमक $L$ की गणना करें। (_) W (उदाहरण प्रारूप: 1.35e+27)'
        self.description_kazakh = 'Диаграммада берілген параметрлерді пайдаланып, жұлдыздың жалпы жарқырауын $L$ есептеңіз. (_) W (Мысал форматы: 1.35e+27)'
        self.description_swahili = 'Kokotoa jumla ya mng\'ao (luminosity) $L$ wa nyota kwa kutumia vigezo vilivyotolewa kwenye mchoro. (_) W (Mfano wa muundo: 1.35e+27)'

