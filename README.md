# 📦 EBA SCORM İçerik Üretici

Bu proje, eğitimcilerin ve içerik geliştiricilerin **EBA (Eğitim Bilişim Ağı)** platformu için kodlama bilgisine ihtiyaç duymadan hızlı ve etkileşimli **SCORM 1.2** paketleri hazırlamasını sağlayan Python tabanlı bir web uygulamasıdır.

Özellikle fen bilimleri müfredatındaki "Kuvvet ve Enerji" gibi soyut konuları veya "Şehrimiz Malatya" tarzı yerel eğitim içeriklerini dijitalleştirirken; öğretmenlere zaman kazandırmak ve öğrencilere pedagojik olarak doğru geri bildirimler sunmak amacıyla geliştirilmiştir.

## ✨ Özellikler

* **4 Farklı Soru Tipi:** Çoktan Seçmeli, Doğru/Yanlış, Boşluk Doldurma (Regex destekli) ve HTML5 Drag & Drop (Sürükle-Bırak) eşleştirme formatlarında sorular hazırlama.
* **Pedagojik Geri Bildirim Sistemi:** Etkileşimli sorularda öğrenciyi anında cezalandırmak yerine **3 deneme hakkı** sunan, yanlışların eski yerine dönmesini sağlayan "formative" (biçimlendirici) değerlendirme altyapısı.
* **Yerel Medya Yönetimi:** Eklenen soru görsellerini Base64 ile şişirmek yerine, otomatik olarak fiziksel `assets/` klasörüne kopyalayıp dışa aktarılan paketin içine izole bir şekilde entegre etme yeteneği.
* **LMS Puan Takibi:** Etkinlik sonu başarı yüzdesini SCORM API Wrapper aracılığıyla EBA'nın not sistemine (`cmi.core.score.raw`) işleme veya sadece etkinlik `completed` (tamamlandı) bilgisi gönderme seçenekleri.
* **Dinamik Şablon Motoru:** Jinja2 kullanarak girilen verileri modern, responsive ve animasyonlu HTML şablonlarına anında enjekte etme.
* **Otomatik Paketleme:** SCORM zorunluluğu olan `imsmanifest.xml` bildirgesini hatasız oluşturup, tüm HTML, JS, CSS ve resim klasörlerini EBA'ya yüklenmeye hazır tek bir `.zip` dosyası haline getirme.

## 🛠️ Kurulum ve Gereksinimler

Uygulamanın çalışması için bilgisayarınızda **Python 3.x** kurulu olmalıdır.

1. Projeyi bilgisayarınıza indirin veya klonlayın:
```bash
git clone [https://github.com/KULLANICI_ADINIZ/eba-scorm-uretici.git](https://github.com/KULLANICI_ADINIZ/eba-scorm-uretici.git)
cd eba-scorm-uretici
