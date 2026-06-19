import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Environment, FileSystemLoader
import re
import io
import zipfile
import os

# --- GÖRSEL KLASÖRÜ KONTROLÜ ---
# Uygulama çalıştığında 'assets' klasörü yoksa otomatik oluşturur.
if not os.path.exists("assets"):
    os.makedirs("assets")

# Sayfa Ayarları
st.set_page_config(page_title="EBA SCORM Üretici", page_icon="📦", layout="wide")

# Oturum Hafızasını (Session State) Başlatma
if 'sorular' not in st.session_state:
    st.session_state.sorular = []

# Sol Menü (Sidebar) - Ayarlar
st.sidebar.title("📚 Etkinlik Bilgileri")
unite_adi = st.sidebar.text_input("Ünite Adı:", placeholder="Örn: Madde ve Doğası")
konu_adi = st.sidebar.text_input("Konu Adı:", placeholder="Örn: Saf Maddeler")

st.sidebar.markdown("---")
st.sidebar.title("⚙️ SCORM Ayarları")
question_type = st.sidebar.radio(
    "Soru Tipi Ekle:",
    ("Çoktan Seçmeli", "Doğru/Yanlış", "Boşluk Doldurma", "Sürükle-Bırak")
)

st.sidebar.markdown("---")
lms_tracking = st.sidebar.toggle("LMS Puan Takibi", value=True)

if lms_tracking:
    st.sidebar.success("Durum: Aktif (EBA'ya not gönderilecek)")
else:
    st.sidebar.warning("Durum: Pasif (Sadece 'Tamamlandı' gidecek)")

# Ana Ekran
st.title("EBA SCORM İçerik Üretici 📦")
st.subheader(f"Yeni Soru Ekle: {question_type}")

# Dinamik Veri Giriş Formu
with st.form("soru_formu", clear_on_submit=True):
    # Ortak Görsel Yükleme Alanı
    gorsel_dosya = st.file_uploader("🖼️ Soru Görseli Ekle (İsteğe Bağlı):", type=["png", "jpg", "jpeg"])
    st.markdown("---")
    
    if question_type == "Çoktan Seçmeli":
        soru_metni = st.text_area("Soru Metni:", placeholder="Örn: Sabit süratle giden bir aracın zamanla aldığı yol nasıl değişir?")
        col1, col2 = st.columns(2)
        with col1:
            sec_a = st.text_input("A Şıkkı:")
            sec_b = st.text_input("B Şıkkı:")
        with col2:
            sec_c = st.text_input("C Şıkkı:")
            sec_d = st.text_input("D Şıkkı:")
        dogru_cevap = st.selectbox("Doğru Cevap:", ["A", "B", "C", "D"])
        
    elif question_type == "Doğru/Yanlış":
        soru_metni = st.text_area("İfadeyi Yazın:", placeholder="Örn: Kuvvet ve enerji aynı kavramlardır.")
        dogru_cevap = st.radio("Cevap Anahtarı:", ["Doğru", "Yanlış"])
        
    elif question_type == "Boşluk Doldurma":
        soru_metni = st.text_area("Metni Yazın:", placeholder="Örn: Alınan yolun geçen zamana bölümüne [sürat] denir.")
        st.info("İpucu: Öğrencinin doldurmasını istediğiniz kelimeleri köşeli parantez [ ] içine alarak metni yazın.")
        
    elif question_type == "Sürükle-Bırak":
        soru_metni = st.text_area("Yönergeyi Yazın:", placeholder="Örn: Aşağıdaki kavramları doğru tanımlarla eşleştirin.")
        st.info("Sürüklenecek öğeler ile bırakılacak hedefleri sırasıyla ve aralarına virgül koyarak yazın. (1. öğe 1. hedefe eşleşecek şekilde)")
        col1, col2 = st.columns(2)
        with col1:
            suruklenecekler = st.text_area("Sürüklenecek Öğeler (Virgülle ayırın):", placeholder="Örn: Sürat, Yol, Zaman")
        with col2:
            hedefler = st.text_area("Bırakılacak Hedefler / Tanımlar (Virgülle ayırın):", placeholder="Örn: Birim zamandaki yer değiştirme, Hareketlinin izlediği yörünge uzunluğu, Geçen süre")

    submit_btn = st.form_submit_button("Sisteme Ekle ➕")

# Ekleme Butonuna Basıldığında
if submit_btn:
    if not soru_metni.strip():
        st.error("Lütfen bir soru metni veya yönerge girin!")
    else:
        yeni_soru = {
            "soru_tipi": question_type,
            "soru_metni": soru_metni
        }
        
        # --- GÖRSEL KAYDETME İŞLEMİ ---
        if gorsel_dosya is not None:
            # Çakışmaları önlemek için dosya adına soru numarasını ekliyoruz
            dosya_adi = f"q{len(st.session_state.sorular)+1}_{gorsel_dosya.name}"
            dosya_yolu = os.path.join("assets", dosya_adi)
            
            # Resmi fiziksel olarak assets klasörüne yaz
            with open(dosya_yolu, "wb") as f:
                f.write(gorsel_dosya.getbuffer())
                
            # Sadece dosya adını sözlüğe kaydet
            yeni_soru["resim_yolu"] = dosya_adi
        
        if question_type == "Çoktan Seçmeli":
            yeni_soru["secenekler"] = {"A": sec_a, "B": sec_b, "C": sec_c, "D": sec_d}
            yeni_soru["dogru_cevap"] = dogru_cevap
        elif question_type == "Doğru/Yanlış":
            yeni_soru["dogru_cevap"] = dogru_cevap
        elif question_type == "Boşluk Doldurma":
            cevaplar = re.findall(r'\[(.*?)\]', soru_metni)
            if not cevaplar:
                st.error("Lütfen en az bir kelimeyi köşeli parantez [ ] içine alın!")
                st.stop()
            html_metin = re.sub(r'\[(.*?)\]', r'<input type="text" class="blank-input" data-answer="\1">', soru_metni)
            yeni_soru["html_metin"] = html_metin
            yeni_soru["cevaplar"] = cevaplar
        elif question_type == "Sürükle-Bırak":
            s_list = [s.strip() for s in suruklenecekler.split(",") if s.strip()]
            h_list = [h.strip() for h in hedefler.split(",") if h.strip()]
            if len(s_list) != len(h_list) or len(s_list) == 0:
                st.error("Sürüklenecek öğe sayısı ile hedef sayısı eşit olmalı ve boş bırakılmamalıdır!")
                st.stop()
            yeni_soru["suruklenecekler"] = s_list
            yeni_soru["hedefler"] = h_list

        st.session_state.sorular.append(yeni_soru)
        st.success(f"{question_type} başarıyla eklendi! Toplam soru: {len(st.session_state.sorular)}")
        st.rerun()

st.markdown("---")

# Eklenen Soruları Listeleme, Silme ve Sıralama İşlemleri
if len(st.session_state.sorular) > 0:
    st.header(f"📋 Eklenen Sorular ({len(st.session_state.sorular)})")
    
    for i, soru in enumerate(st.session_state.sorular):
        col1, col2, col3, col4 = st.columns([8, 1, 1, 1])
        
        with col1:
            with st.expander(f"Soru {i+1} - {soru['soru_tipi']}"):
                st.write(f"**Metin:** {soru['soru_metni']}")
                if "resim_yolu" in soru:
                    st.info(f"🖼️ Ekli Görsel: {soru['resim_yolu']}")
        
        with col2:
            if st.button("⬆️", key=f"up_{i}", disabled=(i == 0), help="Soruyu yukarı taşı"):
                st.session_state.sorular[i], st.session_state.sorular[i-1] = st.session_state.sorular[i-1], st.session_state.sorular[i]
                st.rerun()
                
        with col3:
            if st.button("⬇️", key=f"down_{i}", disabled=(i == len(st.session_state.sorular) - 1), help="Soruyu aşağı taşı"):
                st.session_state.sorular[i], st.session_state.sorular[i+1] = st.session_state.sorular[i+1], st.session_state.sorular[i]
                st.rerun()
                
        with col4:
            if st.button("🗑️", key=f"del_{i}", help="Soruyu sil"):
                st.session_state.sorular.pop(i)
                st.rerun()
            
    st.markdown("### 📦 Paketi Dışa Aktar")
    if st.button("Tüm Soruları SCORM Olarak Hazırla", type="primary"):
        try:
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template('template.html')
            
            # Form verilerini, LMS ayarını ve Etkinlik Bilgilerini şablona gönder
            html_cikti = template.render(
                unite_adi=unite_adi if unite_adi else "Değerlendirme Etkinliği",
                konu_adi=konu_adi if konu_adi else "Konu Testi",
                sorular=st.session_state.sorular, 
                lms_tracking="true" if lms_tracking else "false"
            )
            
            st.success("HTML başarıyla derlendi! Arayüz önizlemesi aşağıdadır:")
            st.info("Önizleme ekranında yerel klasördeki resimler Streamlit güvenlik politikası gereği görünmeyebilir, ancak indirdiğiniz ZIP dosyasında sorunsuz çalışacaktır.")
            components.html(html_cikti, height=600, scrolling=True)
            
            manifest_xml = """<?xml version="1.0" encoding="utf-8"?>
<manifest identifier="EBA_SCORM_01" version="1.2" xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="default_org">
    <organization identifier="default_org">
      <title>EBA Etkileşimli İçerik</title>
      <item identifier="item_1" identifierref="resource_1">
        <title>Değerlendirme Modülü</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="resource_1" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
    </resource>
  </resources>
</manifest>"""

            # Bellekte ZIP Oluşturma ve Klasörleri Ekleme
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
                zip_file.writestr("imsmanifest.xml", manifest_xml)
                zip_file.writestr("index.html", html_cikti)
                
                # --- FİZİKSEL RESİMLERİ ZIP'E EKLEME ---
                eklenen_resimler = set()
                for s in st.session_state.sorular:
                    if "resim_yolu" in s and s["resim_yolu"]:
                        r_yol = s["resim_yolu"]
                        if r_yol not in eklenen_resimler:
                            yerel_dosya_yolu = os.path.join("assets", r_yol)
                            if os.path.exists(yerel_dosya_yolu):
                                # ZIP'in içine 'assets/dosya_adi.jpg' olarak ekler
                                zip_file.write(yerel_dosya_yolu, f"assets/{r_yol}")
                            eklenen_resimler.add(r_yol)
            
            st.download_button(
                label="⬇️ SCORM Paketini İndir (.zip)",
                data=zip_buffer.getvalue(),
                file_name="eba_scorm_paketi.zip",
                mime="application/zip"
            )
            
        except Exception as e:
            st.error(f"Şablon derlenirken bir hata oluştu: {e}")
            st.info("Lütfen 'template.html' dosyasının app.py ile aynı klasörde olduğundan emin olun.")
else:
    st.info("Henüz hiç soru eklemediniz. Formu kullanarak etkinlik hazırlamaya başlayabilirsiniz.")