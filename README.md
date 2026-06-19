# 📦 EBA SCORM İçerik Üretici

Bu proje, eğitimcilerin ve içerik geliştiricilerin **EBA (Eğitim Bilişim Ağı)** platformu için kodlama bilgisine ihtiyaç duymadan hızlı ve etkileşimli **SCORM 1.2** paketleri hazırlamasını sağlayan Python tabanlı bir web uygulamasıdır.

Özellikle fen bilimleri müfredatındaki "Kuvvet ve Enerji" gibi soyut konuları veya "Şehrimiz Malatya" tarzı yerel eğitim içeriklerini dijitalleştirirken; öğretmenlere zaman kazandırmak ve öğrencilere pedagojik olarak doğru geri bildirimler sunmak amacıyla geliştirilmiştir.

## ✨ Özellikler

* **Tek Dosya Mimarisi:** Tüm sistem HTML, CSS, JS ve SCORM API kodları dahil olmak üzere tek bir `app.py` dosyası üzerinden çalışır. Kurulumu ve taşıması son derece kolaydır.
* **4 Farklı Soru Tipi:** Çoktan Seçmeli, Doğru/Yanlış, Boşluk Doldurma (Regex destekli) ve HTML5 Drag & Drop (Sürükle-Bırak) eşleştirme formatlarında sorular hazırlama.
* **Pedagojik Geri Bildirim Sistemi:** Etkileşimli sorularda öğrenciyi anında cezalandırmak yerine **3 deneme hakkı** sunan, yanlışların eski yerine dönmesini sağlayan "formative" (biçimlendirici) değerlendirme altyapısı.
* **Yerel Medya Yönetimi:** Eklenen soru görsellerini Base64 ile şişirmek yerine, otomatik olarak fiziksel `assets/` klasörüne kopyalayıp dışa aktarılan paketin içine izole bir şekilde entegre etme yeteneği.
* **LMS Puan Takibi:** Etkinlik sonu başarı yüzdesini SCORM API Wrapper aracılığıyla EBA'nın not sistemine (`cmi.core.score.raw`) işleme veya sadece etkinlik `completed` (tamamlandı) bilgisi gönderme seçenekleri.
* **Otomatik Paketleme:** SCORM zorunluluğu olan `imsmanifest.xml` bildirgesini hatasız oluşturup, tüm dosyaları ve resim klasörlerini EBA'ya yüklenmeye hazır tek bir `.zip` dosyası haline getirme.

## 🛠️ Kurulum Adımları ve Gereksinimler

Uygulamanın çalışması için bilgisayarınızda **Python 3.x** kurulu olmalıdır. 

**Adım 1: Proje Klasörünü Hazırlayın**
Bilgisayarınızda boş bir klasör oluşturun (örneğin `eba-scorm-uretici`) ve indirdiğiniz `app.py` dosyasını bu klasörün içine koyun.

**Adım 2: Gerekli Kütüphaneleri Yükleyin**
Windows PowerShell veya komut satırında proje klasörünün içindeyken şu komutu çalıştırarak gerekli paketleri kurun:
```powershell
pip install streamlit jinja2


🚀 Kullanım
Kurulum tamamlandıktan sonra arayüzü ayağa kaldırmak için aynı dizinde şu komutu çalıştırın:
python -m streamlit run app.py

(Uygulama otomatik olarak varsayılan tarayıcınızda http://localhost:8501 adresinde açılacaktır.)

İçerik Geliştirme Adımları:
Sol menüden ünitenin ve konunun adını belirleyin.

EBA'ya not gönderilip gönderilmeyeceğini "LMS Puan Takibi" butonundan (Aktif/Pasif) ayarlayın.

İlgili soru tipini seçin, metinleri girin ve varsa bilgisayarınızdan soru görselini seçerek listeye ekleyin. (Sistem görseli otomatik olarak assets klasörüne kopyalayacaktır.)

Tüm işlemleriniz bittiğinde ekranın altındaki "Tüm Soruları SCORM Olarak Hazırla" butonuna tıklayın.

İndirilen .zip dosyasını EBA platformuna "Etkileşimli İçerik / SCORM Paketi" olarak doğrudan yükleyebilirsiniz.

📂 Proje Klasör Yapısı
Sistemi çalıştırdığınızda ve resim eklediğinizde klasör yapısı otomatik olarak şu hali alacaktır:
eba-scorm-uretici/
│
├── app.py              # Tüm Streamlit arayüzü, HTML şablonu ve arka plan işlemleri
├── assets/             # (Otomatik oluşur) Yüklenen fiziksel resimler
└── README.md           # Bu dokümantasyon dosyası

⚠️ Bilinen Durumlar (Önizleme Güvenliği)
Uygulama içindeki "Önizleme" (Preview) penceresinde, tarayıcıların yerel dosya güvenlik politikaları (Iframe kısıtlamaları) gereğince assets/ klasörüne yüklediğiniz resimler kırık bir ikon olarak görünebilir. Bu durum bir hata değildir. Oluşturduğunuz SCORM paketi (.zip) EBA sunucularına yüklendiğinde resimleriniz sorunsuz ve eksiksiz olarak çalışacaktır.
