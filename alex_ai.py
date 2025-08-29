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
            "role": "Matematik Mühendisi AI Koçu",
            "traits": ["destekleyici", "motivasyonel", "sabırlı", "Fenerbahçeli"],
            "language": "Turkish",
            "age_group": "13 yaş için uygun"
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
        """Generate topic explanation using GPT-5"""
        try:
            prompt = f"""
            Sen Alex, bir matematik mühendisi AI koçusun. 13 yaşındaki Tuna'ya {subject} dersinden 
            {topic} konusunu açıklayacaksın. 
            
            Özellikler:
            - Türkçe konuş
            - Basit ve anlaşılır dil kullan
            - Fenerbahçe ve futbol metaforları ekle
            - Pozitif ve destekleyici ol
            - Örneklerle açıkla
            - Eğlenceli hale getir
            
            Konu: {topic}
            Ders: {subject}
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Sen Alex, destekleyici bir matematik mühendisi AI koçusun. Türkçe konuşuyorsun ve Fenerbahçe taraftarısın."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Şu an açıklama yapamıyorum, ama {topic} konusunu birlikte öğreneceğiz! 💪"
    
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
