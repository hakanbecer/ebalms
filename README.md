📦 EBA SCORM İçerik Üretici
Bu proje, eğitimcilerin ve içerik geliştiricilerin EBA (Eğitim Bilişim Ağı) platformu için kodlama bilgisine ihtiyaç duymadan hızlı ve etkileşimli SCORM 1.2 paketleri hazırlamasını sağlayan Python tabanlı bir web uygulamasıdır.

Özellikle fen bilimleri müfredatındaki "Kuvvet ve Enerji" gibi soyut konuları veya "Şehrimiz Malatya" tarzı yerel eğitim içeriklerini dijitalleştirirken; öğretmenlere zaman kazandırmak ve öğrencilere pedagojik olarak doğru geri bildirimler sunmak amacıyla geliştirilmiştir.

✨ Özellikler
4 Farklı Soru Tipi: Çoktan Seçmeli, Doğru/Yanlış, Boşluk Doldurma (Regex destekli) ve HTML5 Drag & Drop (Sürükle-Bırak) eşleştirme formatlarında sorular hazırlama.

Pedagojik Geri Bildirim Sistemi: Etkileşimli sorularda öğrenciyi anında cezalandırmak yerine 3 deneme hakkı sunan, yanlışların eski yerine dönmesini sağlayan "formative" (biçimlendirici) değerlendirme altyapısı.

Yerel Medya Yönetimi: Eklenen soru görsellerini Base64 ile şişirmek yerine, otomatik olarak fiziksel assets/ klasörüne kopyalayıp dışa aktarılan paketin içine izole bir şekilde entegre etme yeteneği.

LMS Puan Takibi: Etkinlik sonu başarı yüzdesini SCORM API Wrapper aracılığıyla EBA'nın not sistemine (cmi.core.score.raw) işleme veya sadece etkinlik completed (tamamlandı) bilgisi gönderme seçenekleri.

Dinamik Şablon Motoru: Jinja2 kullanarak girilen verileri modern, responsive ve animasyonlu HTML şablonlarına anında enjekte etme.

Otomatik Paketleme: SCORM zorunluluğu olan imsmanifest.xml bildirgesini hatasız oluşturup, tüm HTML, JS, CSS ve resim klasörlerini EBA'ya yüklenmeye hazır tek bir .zip dosyası haline getirme.

🛠️ Kurulum ve Gereksinimler
Uygulamanın çalışması için bilgisayarınızda Python 3.x kurulu olmalıdır.

Projeyi bilgisayarınıza indirin veya klonlayın:

Bash
git clone https://github.com/KULLANICI_ADINIZ/eba-scorm-uretici.git
cd eba-scorm-uretici
Terminal (veya PowerShell) üzerinden gerekli kütüphaneleri yükleyin:

Bash
pip install streamlit jinja2
🚀 Kullanım
Streamlit arayüzünü ayağa kaldırmak için proje dizininde şu komutu çalıştırın:

Bash
python -m streamlit run app.py
(Uygulama otomatik olarak varsayılan tarayıcınızda http://localhost:8501 adresinde açılacaktır.)

İçerik Geliştirme Adımları:
Sol menüden ünitenin ve konunun adını belirleyin.

EBA'ya not gönderilip gönderilmeyeceğini "LMS Puan Takibi" butonundan (Aktif/Pasif) ayarlayın.

İlgili soru tipini seçin, metinleri girin ve varsa bilgisayarınızdan soru görselini seçerek listeye ekleyin.

Tüm işlemleriniz bittiğinde ekranın altındaki "Tüm Soruları SCORM Olarak Hazırla" butonuna tıklayın.

İndirilen .zip dosyasını EBA platformuna "Etkileşimli İçerik / SCORM Paketi" olarak doğrudan yükleyebilirsiniz.

📂 Proje Klasör Yapısı
Plaintext
eba-scorm-uretici/
│
├── app.py              # Streamlit arayüzü ve Python arka plan işlemleri
├── template.html       # Öğrenci arayüzü, CSS tasarımları ve SCORM API JS kodları
├── assets/             # (Uygulama çalıştığında otomatik oluşur) Yüklenen fiziksel resimler
└── README.md           # Proje dokümantasyonu
⚠️ Bilinen Durumlar (Önizleme Güvenliği)
Uygulama içindeki "Önizleme" (Preview) penceresinde, tarayıcıların yerel dosya güvenlik politikaları (Iframe kısıtlamaları) gereğince assets/ klasörüne yüklediğiniz resimler kırık bir ikon olarak görünebilir. Bu durum bir hata değildir. Oluşturduğunuz SCORM paketi (.zip) EBA sunucularına yüklendiğinde resimleriniz sorunsuz ve eksiksiz olarak çalışacaktır.

🤝 Katkıda Bulunma
Bu araç, açık kaynak felsefesiyle eğitimcilerin hayatını kolaylaştırmak için tasarlanmıştır. Yeni soru tipleri eklemek veya arayüzü geliştirmek isterseniz Pull Request (PR) göndermekten çekinmeyin.
