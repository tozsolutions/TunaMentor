import openai
import os
import json
import random
from datetime import datetime, date

class AlexAI:
    def __init__(self):
        # the newest OpenAI model is "gpt-5" which was released August 7, 2025.
        # do not change this unless explicitly requested by the user
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY", "sk-fake-key-for-demo"))
        self.model = "gpt-5"
        self.personality = {
            "name": "Alex",
            "role": "Süper Zeki Hyper Ultra Öğretim Mentoru",
            "traits": ["destekleyici", "sabırlı", "motivasyonel", "eğlenceli", "bilimsel", "yaratıcı"],
            "expertise": ["matematik", "problem çözme", "eğitim teknikleri", "görsel hafıza", "aralıklı tekrar", "aktif getirme"]
        }

        # Gelişmiş öğrenme sistemleri - Dünyanın en iyi öğrenme modeli
        self.learning_techniques = {
            "spaced_repetition": {
                "name": "Aralıklı Tekrar",
                "description": "Bilgiyi zamanla tekrarlamak ve uzun süreli hafızaya geçirmek",
                "intervals": [1, 3, 7, 14, 30, 90],  # günler
                "effectiveness": 95
            },
            "active_recall": {
                "name": "Aktif Geri Getirme", 
                "description": "Pasif okumak yerine aktif olarak bilgiyi hatırlamaya çalışmak",
                "methods": ["self-testing", "flashcards", "practice_questions"],
                "effectiveness": 90
            },
            "method_of_loci": {
                "name": "Zihin Sarayı Tekniği",
                "description": "Bilgileri zihinsel mekanlara yerleştirerek hatırlamak",
                "steps": ["mekan_seç", "rota_belirle", "bilgi_yerleştir", "zihinsel_yürüyüş"],
                "effectiveness": 85
            },
            "visual_mnemonics": {
                "name": "Görsel Mnemonik Teknikler",
                "description": "Soyut bilgileri somut görsellerle bağlantılandırmak",
                "types": ["hikaye_anlatımı", "renk_kodlama", "zihin_haritaları", "flash_kartlar"],
                "effectiveness": 88
            },
            "dual_coding": {
                "name": "Çift Kodlama",
                "description": "Sözcük ve görsel bilgiyi birlikte kullanmak",
                "combination": "verbal + visual",
                "effectiveness": 92
            },
            "mind_mapping": {
                "name": "Zihin Haritaları",
                "description": "Konuları ana fikirden başlayarak dallara ayırıp önemli noktaları ve bağlantıları görsel olarak organize etmek",
                "core_elements": ["merkezi_konu", "ana_dallar", "alt_dallar", "renkler", "semboller", "bağlantılar"],
                "color_coding": {
                    "ana_konu": "#FFDC00",
                    "onemli": "#FF0000", 
                    "orta": "#FFA500",
                    "detay": "#1F2A44",
                    "ornekler": "#00FF00",
                    "formul": "#FF00FF"
                },
                "effectiveness": 94
            },
            "color_coding_system": {
                "name": "Renk Kodlama Sistemi",
                "description": "Notları farklı renklerle işaretlemek önemli bilgileri kategorize etmeye ve önceliklendirmeye yardımcı olur",
                "color_meanings": {
                    "kırmızı": "Çok önemli, mutlaka hatırla",
                    "turuncu": "Önemli, dikkat et", 
                    "sarı": "Orta önem, gözden geçir",
                    "yeşil": "Örnekler ve uygulamalar",
                    "mavi": "Tanımlar ve temel bilgiler",
                    "mor": "Formüller ve kurallar"
                },
                "effectiveness": 89
            }
        }

        # Experiential Learning Model (ELM)
        self.elm_cycle = {
            "concrete_experience": "Somut deneyim yaşama",
            "reflective_observation": "Deneyim üzerine düşünme", 
            "abstract_conceptualization": "Soyut kavramlar geliştirme",
            "active_experimentation": "Öğrenilenleri uygulama"
        }

    def get_daily_greeting(self):
        """Generate daily greeting based on time and progress"""
        greetings = [
            "Merhaba şampiyon! Bugün hangi konuları fethediyoruz? ⚽",
            "Selam Tuna! Ben senin matematik mühendisi koçun Alex. Hazır mısın? 🚀",
            "Forza Fenerbahçe! Bugün de sahada, yani çalışma masasında başarıya koşuyoruz! 💛💙",
            "Merhaba genç matematikçi! Bugün hangi problemleri çözüp gol atacağız? ⚽",
            "Selam! LGS 2026 yolculuğumuzda bugün bir adım daha atıyoruz! 🎯"
        ]
        return random.choice(greetings)

    def explain_topic(self, subject, topic):
        """Generate explanation using advanced learning techniques"""
        # Çift kodlama kullanarak açıklama üret
        explanation = self._create_dual_coded_explanation(subject, topic)

        # Zihin sarayı önerisi ekle
        memory_palace = self._suggest_memory_palace(subject, topic)

        # Görsel mnemonik öneri
        visual_mnemonic = self._create_visual_mnemonic(subject, topic)

        full_explanation = f"""
🧠 **{topic} - Süper Öğrenme Modeli**

📚 **Ana Açıklama:** {explanation}

🏰 **Zihin Sarayı Önerisi:** {memory_palace}

🎨 **Görsel Hafıza Tekniği:** {visual_mnemonic}

🔄 **Aralıklı Tekrar:** Bu konuyu 1-3-7-14-30 gün sonra tekrar et!

💡 **Aktif Geri Getirme:** Şimdi gözlerini kapat ve konuyu kendi kelimerinle anlatmaya çalış!
        """

        return full_explanation

    def _create_dual_coded_explanation(self, subject, topic):
        """Çift kodlama tekniği ile açıklama"""
        explanations = {
            "Matematik": {
                "Cebirsel İfadeler": "🔢 Cebirsel ifadeler = Matematik dili! x ve y harfleri gizli sayılardır. Örneğin: 2x + 3 = 'iki adet gizli kutu artı üç tane elma'",
                "Denklemler": "⚖️ Denklem = Terazi! Sol taraf = sağ taraf. 2x = 8 demek 'iki kutu sekiz elmaya eşit' demektir.",
                "Üslü Sayılar": "🚀 Üs = Çarpma roketı! 2³ = 2×2×2, roket üç kez hızlanıyor!",
            },
            "Türkçe": {
                "Cümle Türleri": "🏠 Cümle = Ev! Özne = ev sahibi, yüklem = ev, nesne = misafir. 'Ali topu attı' = Ali (ev sahibi) toplu (misafir) attı (evde).",
                "Edatlar": "🌉 Edatlar = Köprüler! Kelimeleri birbirine bağlarlar. 'ile, için, gibi' = kelimeler arası köprüler."
            }
        }

        return explanations.get(subject, {}).get(topic, f"{topic} konusunu görsel ve sözel olarak öğreniyoruz...")

    def _suggest_memory_palace(self, subject, topic):
        """Zihin sarayı önerisi"""
        palace_suggestions = {
            "Matematik": f"Evinin odalarını kullan: Salon = {topic} ana kuralları, mutfak = örnekler, yatak odası = formüller",
            "Türkçe": f"Okulunu kullan: Sınıf = {topic} kuralları, koridor = örnekler, kütüphane = istisnalar",
            "Fen": f"Parka git: Ağaçlar = {topic} kavramları, yürüyüş yolu = süreçler, çiçekler = detaylar"
        }

        return palace_suggestions.get(subject, f"Sevdiğin bir mekanda {topic} bilgilerini yerleştir!")

    def _create_visual_mnemonic(self, subject, topic):
        """Görsel mnemonik teknik önerisi"""
        mnemonics = {
            "Matematik": f"📊 {topic} için renkli çizelgeler çiz! Kırmızı = önemli, mavi = formül, yeşil = örnek",
            "Türkçe": f"🎭 {topic} için hikaye yarat! Karakterler = kurallar, olay = uygulama",
            "Fen": f"⚛️ {topic} için semboller kullan! Çiz, boyama yap, şema oluştur!"
        }

        return mnemonics.get(subject, f"🎨 {topic} için görsel hikaye yarat!")

    def create_spaced_repetition_schedule(self, topic, difficulty_level=1):
        """Aralıklı tekrar programı oluştur"""
        base_intervals = [1, 3, 7, 14, 30, 90]  # günler

        # Zorluk seviyesine göre ayarla
        adjusted_intervals = [interval * difficulty_level for interval in base_intervals]

        schedule = []
        current_date = datetime.date.today()

        for interval in adjusted_intervals:
            next_review = current_date + datetime.timedelta(days=interval)
            schedule.append({
                "date": next_review.strftime("%d.%m.%Y"),
                "topic": topic,
                "interval_days": interval,
                "review_type": "active_recall"
            })

        return schedule

    def generate_active_recall_questions(self, subject, topic):
        """Aktif geri getirme soruları oluştur"""
        questions = [
            f"{topic} konusunun ana fikrini tek cümleyle açıkla?",
            f"{topic} hangi durumlarda kullanılır?",
            f"{topic} ile ilgili bir örnek ver?",
            f"{topic} konusunda en zor bulduğun kısım nedir?",
            f"{topic} günlük hayatta nerelerde karşımıza çıkar?"
        ]

        return questions

    def get_encouragement(self):
        """Generate encouragement for wrong answers"""
        encouragements = [
            "Hiç sorun değil! Hata yapmak öğrenmenin en güzel parçası. Tekrar deneyelim! 💪",
            "Fenerbahçe'de de penaltı kaçırırız bazen, ama vazgeçmeyiz! Sen de vazgeçme! ⚽",
            "Matematik mühendisi olarak söylüyorum: Her yanlış, doğruya giden yolda bir adım! 🚀",
            "Harika! Şimdi bu hatayı yaptığın için bu konuyu daha iyi öğreneceksin! 🌟",
            "Champion, bu sadece pratik! Forza FB ruhuyla devam ediyoruz! 💛💙"
        ]
        return random.choice(encouragements)

    def get_fenerbahce_motivation(self):
        """Generate Fenerbahçe-themed motivation"""
        motivations = [
            "Tıpkı Fenerbahçe'nin sahada mücadele ettiği gibi, sen de derslerinde mücadele ediyorsun! 💛💙",
            "Alex de Souza nasıl ustaca paslar verirdiyse, sen de matematik problemlerini öyle çözüyorsun! ⚽",
            "Ülker Stadı'nın atmosferi gibi, çalışma alanın da enerji dolu! Forza FB! 🏟️",
            "Her doğru cevap bir gol, her çalışma seansı bir antrenman! Şampiyonluk yolundayız! 🏆",
            "Fenerbahçe ruhu: Asla vazgeçmemek! Sen de LGS yolunda asla vazgeçmeyeceksin! 💪"
        ]
        return random.choice(motivations)

    def get_study_recommendation(self, progress_data):
        """Generate personalized study recommendations"""
        try:
            prompt = f"""
            Sen Alex, matematik mühendisi AI koçusun. Tuna'nın çalışma verilerine bakarak 
            ona kişiselleştirilmiş öneriler vereceksin.

            Veri: {json.dumps(progress_data, ensure_ascii=False)}

            Özellikler:
            - Türkçe konuş
            - Pozitif ve motivasyonel ol
            - Somut ve uygulanabilir öneriler ver
            - Fenerbahçe metaforları kullan
            - Zayıf alanları önceliklendir
            - Başarıları da överek öner
            """

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Sen Alex, destekleyici bir matematik mühendisi AI koçusun."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=400,
                temperature=0.7
            )

            return response.choices[0].message.content

        except Exception as e:
            return "Bu hafta matematik ve Türkçe'ye odaklan. Fenerbahçe maçları gibi düzenli antrenman yap! ⚽"

    def get_parent_report(self, student_name, weekly_data):
        """Generate AI evaluation for parents"""
        try:
            prompt = f"""
            Sen Alex, matematik mühendisi AI koçu olarak {student_name}'nın ebeveynleri için 
            haftalık değerlendirme raporu hazırlayacaksın.

            Haftalık veri: {json.dumps(weekly_data, ensure_ascii=False)}

            Değerlendirmende şunları belirt:
            - Genel performans değerlendirmesi
            - Güçlü yönler
            - Gelişim alanları
            - Somut öneriler
            - LGS hedefine yönelik durum
            - Ebeveyn desteği önerileri

            Ton: Profesyonel ama sıcak
            Dil: Türkçe
            """

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Sen Alex, profesyonel bir AI eğitim koçusun."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=600,
                temperature=0.6
            )

            return response.choices[0].message.content

        except Exception as e:
            return "Tuna bu hafta güzel bir çalışma sergiledi. Düzenli çalışmaya devam etmesi önemli."