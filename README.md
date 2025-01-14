# Yapay Zeka ile Edebi Eserlerin Betimlemelerini Görselleştirme

## Amaç
Bu projede, seçilen edebi eserlerdeki betimlemelerin yapay zeka yardımıyla görselleştirilmesi ve elde edilen görsellerin insanların zihnindeki canlanan görsellerle ne kadar tutarlı olduğunun ölçülmesi hedeflenmiştir.

## Yöntem
Proje iki temel aşamada gerçekleştirilmiştir: metin analizi ve görsel üretim.

### 1. Metin Analizi
Metinlerin analizinde, Hugging Face platformunda açık kaynak olarak sunulan **Meta-llama/Llama-3.3-70B-Instruct** modeli kullanılmıştır. Transformer mimarisine dayalı bu model, metinlerdeki kelime ilişkilerini, bağlamı ve duygu tonlarını etkili bir şekilde analiz edebilme yeteneğine sahiptir. 

Bu aşamanın önemli adımları şunlardır:
- **Alt Metin ve Tema Analizi:** Metinlerin derinlemesine kavranması için duygu tonu, atmosfer ve tematik unsurlar belirlenmiştir.
- **Prompt Oluşturulması:** Eserlerin her bir sayfasına özgü yaratıcı promptlar tasarlanmış ve bunlar, görsel içeriklerin üretimi için temel girdi olarak kullanılmıştır.

Bu aşamada **Python** programlama dili kullanılmış ve aşağıdaki kütüphanelerden yararlanılmıştır:
- **Transformers:** Doğal dil işleme modellerinin yürütülmesi.
- **PyPDF2:** PDF formatındaki metinlerin okunması ve işlenmesi.

### 2. Görsel Üretim
Metin analizi sonucunda oluşturulan promptlar, difüzyon tabanlı bir görsel üretim modeli olan **Stable Diffusion** kullanılarak görsele dökülmüştür. Stable Diffusion modeli, rastgele gürültü ile başlayarak bu gürültüyü adım adım azaltır ve sonunda anlamlı görseller üretir.

Bu aşamanın ana adımları:
- **Prompt Kullanımı:** Metinlerin duygusal ve tematik özelliklerini yansıtan promptlar ile modelin girdi verilmesi.
- **Görsel İşleme:** Elde edilen görsellerin projenin hedeflerine uygun şekilde düzenlenmesi ve değerlendirilmesi.

Bu süreçte kullanılan Python kütüphaneleri:
- **Diffusers:** Stable Diffusion modelinin kullanımı.
- **Pillow ve NumPy:** Görsel işleme ve düzenleme için.

### Değerlendirme
Proje ekibi, üretilen görselleri aşağıdaki kriterlere göre değerlendirmiştir:
- **Metinlerle Uyumluluk:** Betimlemelerin içerik ve duygu tonlarıyla uyumu.
- **Atmosferin Doğruluğu:** Hedeflenen tematik özelliklerin yansıtılması.
- **Sanatsal ve Anlatısal Katkı:** Görsellerin, metinlerin anlatısal etkisini zenginleştirme potansiyeli.

Seçilen görseller, eserin anlatısal etkisini destekleyerek okuyucunun anlatıya daha fazla dahil olmasını sağlamıştır.

## Sonuç
Proje, yapay zeka destekli betimleme analizi ve görsel üretim süreçlerinin birleştirilmesiyle, edebi eserlerin görsel bir forma dönüştürülmesine olanak tanımıştır. Elde edilen görseller, metinlerin sanatsal ve duygusal derinliğini güçlendirmiş ve yeni bir anlatı deneyimi sunmuştur.

# Google Drive Linki: https://drive.google.com/drive/folders/1WpuEI018BAJDyLpLdNXhO86RuGjOz5NI?usp=sharing
