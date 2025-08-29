# Alex LGS Koçu - Kişiselleştirilmiş Eğitim Asistanı

## Overview

Alex LGS Koçu, 13 yaşındaki Tuna'nın 2025-2026 LGS sınavına hazırlanması için tasarlanmış kapsamlı bir eğitim platformudur. Uygulama, yapay zeka destekli kişiselleştirilmiş öğretmen Alex ile hibrit bir öğrenme deneyimi sunar. Alex, hem öğretmen rolünde konu anlatımı ve soru çözümü yapar, hem de mentor rolünde motivasyon ve yönlendirme sağlar.

Platform, MEB 8. sınıf müfredatını kapsar ve özellikle Matematik ve Türkçe derslerine odaklanır. Fenerbahçe temasıyla futbol metaforları kullanarak öğrenmeyi eğlenceli hale getirir. Hedef, öğrenciyi Türkiye genelinde %2'lik dilime sokacak 450-475 puan hedefine ulaştırmaktır.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
Streamlit tabanlı web uygulaması, modern ve etkileşimli kullanıcı arayüzü sunar. Fenerbahçe renkleri (sarı-lacivert) ile özelleştirilmiş CSS tema uygulanmıştır. Responsive tasarım ile farklı cihazlarda kullanılabilir.

### AI Integration
OpenAI GPT-5 modeli kullanılarak Alex karakteri hayata geçirilmiştir. AlexAI sınıfı, kişiselleştirilmiş konu anlatımı, motivasyonel mesajlar ve Türkçe dil desteği sağlar. AI, öğrencinin seviyesine uygun açıklamalar yapar ve futbol metaforları kullanır.

### Data Storage
SQLite veritabanı kullanılarak kullanıcı verileri, çalışma seansları, soru çözüm geçmişi ve ilerleme bilgileri saklanır. Database sınıfı ile ORM benzeri bir yapı kurgulanmıştır.

### Gamification System
Puan sistemi, rozet sistemi ve seviye mekanizması ile öğrenme motivasyonu artırılır. Gamification sınıfı, çeşitli başarılar için puan hesaplamaları ve ödül sistemini yönetir.

### Curriculum Management
MEB 8. sınıf müfredatına uygun konu organizasyonu. Curriculum sınıfı, derslerin yapılandırılması ve soru bankası yönetimi sağlar. Her ders için ayrıntılı konu başlıkları tanımlanmıştır.

### Progress Tracking
Detaylı ilerleme takibi ve analitik raporlama sistemi. ProgressTracker sınıfı, öğrencinin performansını analiz eder ve zayıf alanları belirler.

### Study Planning
Akıllı çalışma planı oluşturma sistemi. StudyPlanner sınıfı, Pomodoro tekniği kullanarak günlük ve haftalık çalışma programları oluşturur.

### Voice Synthesis
Sesli etkileşim için VoiceSynthesis sınıfı, Web Speech API kullanarak Alex'in sesli yanıtlar vermesini sağlar. Türkçe telaffuz optimizasyonları uygulanmıştır.

### Parent Dashboard
Veli paneli ile haftalık raporlama ve performans analizi. ParentDashboard sınıfı, ailelerin çocuklarının ilerlemesini takip etmesini sağlar.

## External Dependencies

### AI Services
- **OpenAI GPT-5**: Kişiselleştirilmiş öğretim içeriği ve Alex karakterinin yanıtları için kullanılır
- **Web Speech API**: Tarayıcı tabanlı sesli etkileşim için kullanılır

### Web Framework
- **Streamlit**: Ana web uygulaması framework'ü olarak kullanılır
- **Streamlit Components**: Özelleştirilmiş HTML ve JavaScript entegrasyonu için

### Data Analysis
- **Pandas**: Veri analizi ve raporlama için kullanılır
- **Plotly**: İnteraktif grafikler ve görselleştirme için

### Database
- **SQLite**: Yerel veri depolama çözümü olarak kullanılır
- Gelecekte PostgreSQL'e geçiş planlanabilir

### Fenerbahçe Integration
- **Fikstür API'leri**: 2025-2026 sezon fikstür bilgileri için harici spor API'leri kullanılabilir
- Şu an için simüle edilmiş veri kullanılmaktadır

### Multimedia Support
- **Lottie/MP4**: Animasyonlu ders içerikleri için kullanılacak
- **ElevenLabs veya benzeri**: Gelişmiş ses sentezi için potansiyel entegrasyon