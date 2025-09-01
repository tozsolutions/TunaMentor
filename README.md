# 🎯 Alex LGS Koçu - TunaMentor

Alex LGS Koçu, Türkiye'deki öğrencilerin LGS (Liselere Geçiş Sistemi) sınavına hazırlanması için geliştirilen AI destekli kişisel öğretim sistemidir.

## 🌟 Özellikler

### 🤖 Alex AI Mentör
- **Yapay Zeka Destekli Öğrenme**: GPT-5 ile güçlendirilmiş kişiselleştirilmiş eğitim
- **Sesli Etkileşim**: Türkçe text-to-speech desteği
- **Motivasyonel Destek**: Fenerbahçe temalı motivasyon sistemi

### 📚 Gelişmiş Öğrenme Teknikleri
- **Zihin Sarayı (Memory Palace)**: Görsel hafıza teknikleri
- **Aralıklı Tekrar (Spaced Repetition)**: Bilimsel tekrar sistemi
- **Aktif Geri Getirme (Active Recall)**: Etkili öğrenme yöntemi
- **Çift Kodlama**: Görsel ve sözel hafıza kombinasyonu

### 🎮 Gamification Sistemi
- **Puan ve Rozetler**: Başarı odaklı ödül sistemi
- **Günlük Görevler**: Motivasyonel hedefler
- **Seviye Sistemi**: İlerleme takibi
- **Fenerbahçe Entegrasyonu**: Maç izleme ödülleri

### 📊 İlerleme Takibi
- **Detaylı Analytics**: Konu bazında performans analizi
- **Ebeveyn Paneli**: Haftalık ilerleme raporları
- **Zayıf Alan Tespiti**: Kişiselleştirilmiş çalışma önerileri
- **LGS Puan Tahmini**: Gerçekçi hedef belirleme

### 📱 Çok Platform Desteği
- **Web Uygulaması**: Streamlit tabanlı responsive tasarım
- **PWA Desteği**: Mobil cihazlarda app-like deneyim
- **Cross-platform**: Windows, Mac, Linux desteği

## 🚀 Kurulum

### Gereksinimler
- Python 3.11+
- OpenAI API Key
- Modern web tarayıcısı

### Hızlı Başlangıç

1. **Repository'yi klonlayın:**
```bash
git clone https://github.com/tozsolutions/TunaMentor.git
cd TunaMentor
```

2. **Sanal ortam oluşturun:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Ortam değişkenlerini ayarlayın:**
```bash
cp .env.example .env
# .env dosyasını düzenleyerek OPENAI_API_KEY'i ayarlayın
```

5. **Uygulamayı başlatın:**
```bash
streamlit run app.py
```

### Docker ile Kurulum

1. **Docker image oluşturun:**
```bash
docker build -t tutor-app .
```

2. **Container'ı çalıştırın:**
```bash
docker-compose up -d
```

## 🔧 Konfigürasyon

### Ortam Değişkenleri

| Değişken | Açıklama | Varsayılan |
|----------|----------|------------|
| `OPENAI_API_KEY` | OpenAI API anahtarı | - |
| `ENVIRONMENT` | Çalışma ortamı (development/production) | development |
| `DEBUG` | Debug modu | false |
| `LOG_LEVEL` | Log seviyesi | INFO |
| `DATABASE_URL` | Veritabanı URL'i | sqlite:///alex_lgs.db |
| `STREAMLIT_SERVER_PORT` | Port numarası | 8501 |

### Streamlit Konfigürasyonu

`.streamlit/config.toml` dosyasında tema ve sunucu ayarları bulunur:

```toml
[theme]
primaryColor = "#FFDC00"  # Fenerbahçe sarısı
backgroundColor = "#1F2A44"  # Fenerbahçe mavisi
```

## 📖 Kullanım

### Öğrenci Girişi
1. Ana sayfada adını gir (varsayılan: "tuna")
2. Şifreni gir
3. "Çalışmaya Başla" butonuna tıkla

### Ana Özellikler
- **📖 Ders Çalış**: Konu bazında interaktif eğitim
- **🎮 Oyunlar**: Gamification ve ödül sistemi
- **⚽ Fenerbahçe**: Motivasyonel içerik ve maç entegrasyonu
- **📊 İlerleme**: Detaylı performans analizi
- **🚀 Gelecek Dersleri**: Teknoloji ve kariyer odaklı ek eğitim

### Ebeveyn Paneli
- Şifre: `ebeveyn2026`
- Haftalık ilerleme raporları
- Detaylı performans analizi
- PDF rapor indirme

## 🏗️ Mimari

```
TunaMentor/
├── app.py                 # Ana Streamlit uygulaması
├── alex_ai.py            # AI mentor sınıfı
├── database.py           # Veritabanı yönetimi
├── config.py             # Konfigürasyon yönetimi
├── logger.py             # Log sistemi
├── curriculum.py         # Müfredat yönetimi
├── gamification.py       # Oyunlaştırma sistemi
├── progress_tracker.py   # İlerleme takibi
├── voice_synthesis.py    # Sesli etkileşim
├── memory_techniques.py  # Hafıza teknikleri
├── fenerbahce_integration.py # FB entegrasyonu
├── study_planner.py      # Çalışma planlayıcısı
├── parent_dashboard.py   # Ebeveyn paneli
├── utils.py              # Yardımcı fonksiyonlar
└── requirements.txt      # Python bağımlılıkları
```

## 🛡️ Güvenlik

- ✅ API anahtarları environment variables ile yönetilir
- ✅ Input validation ve sanitization
- ✅ Session management
- ✅ XSS/CSRF koruması
- ✅ Rate limiting (üretim ortamında)

## 📊 Monitoring ve Logs

### Log Dosyaları
- `logs/alex_lgs_YYYYMMDD.log` - Genel uygulama logları
- `logs/alex_lgs_errors_YYYYMMDD.log` - Hata logları

### Health Check
```bash
curl http://localhost:8501/_stcore/health
```

## 🚀 Deployment

### Streamlit Community Cloud
1. GitHub repository oluşturun
2. [share.streamlit.io](https://share.streamlit.io) adresinde hesap açın
3. Repository'yi bağlayın
4. Secrets bölümünde API anahtarlarını ekleyin

### Heroku
```bash
heroku create alex-lgs-kocu
heroku config:set OPENAI_API_KEY=your_key_here
git push heroku main
```

### VPS/Dedicated Server
1. Sistem gereksinimlerini yükleyin
2. Repository'yi klonlayın
3. Systemd service oluşturun
4. Nginx reverse proxy kurun
5. SSL sertifikası ekleyin

Detaylı deployment talimatları için `deployment_instructions.txt` dosyasına bakın.

## 🧪 Testing

```bash
# Unit testleri çalıştır
python -m pytest tests/

# Syntax kontrolü
python -m py_compile *.py

# Linting
flake8 .
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 📞 Destek

- **E-posta**: support@tozsolutions.com
- **GitHub Issues**: [Issues sayfası](https://github.com/tozsolutions/TunaMentor/issues)
- **Dokumentasyon**: [Wiki sayfası](https://github.com/tozsolutions/TunaMentor/wiki)

## 🎯 Hedefler 2026

- [ ] Mobil uygulama (React Native)
- [ ] Çok kullanıcılı sistem
- [ ] Sınıf yönetimi
- [ ] Öğretmen paneli
- [ ] API entegrasyonları
- [ ] Machine learning tabanlı kişiselleştirme

---

⚽ **Fenerbahçe ruhuyla, eğitimde başarıya!** 💛💙

**Alex ile 2026 LGS'de zirvede olun!** 🏆