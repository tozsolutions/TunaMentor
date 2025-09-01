import json
import random
from typing import Dict, List, Any

class Curriculum:
    def __init__(self):
        self.meb_curriculum = self._load_meb_curriculum()
        self.question_bank = self._load_question_bank()
    
    def _load_meb_curriculum(self) -> Dict[str, Any]:
        """Load MEB 8th grade curriculum structure"""
        return {
            "Matematik": [
                "Çarpanlar ve Katlar",
                "Üslü İfadeler", 
                "Kareköklü İfadeler",
                "Cebirsel İfadeler",
                "Doğrusal Denklemler ve Eşitsizlikler",
                "Üçgenler",
                "Dönüşüm Geometrisi",
                "Eşlik ve Benzerlik",
                "Geometrik Cisimler",
                "Veri Analizi ve İstatistik"
            ],
            "Türkçe": [
                "Erdemler (zorunlu)",
                "Millî Kültürümüz (zorunlu)",
                "Millî Mücadele ve Atatürk (zorunlu)",
                "Birey ve Toplum",
                "Okuma Kültürü",
                "Kişisel Gelişim",
                "Bilim ve Teknoloji",
                "Çocuk Dünyası"
            ],
            "Fen Bilimleri": [
                "DNA ve Genetik Kod",
                "Basit Makineler",
                "Enerji Dönüşümleri ve Çevre Bilimi",
                "Basınç",
                "Madde ve Endüstri"
            ],
            "T.C. İnkılap Tarihi": [
                "Bir Kahraman Doğuyor",
                "Millî Uyanış: Yurdumuzun İşgaline Tepkiler",
                "Ya İstiklal Ya Ölüm!",
                "Çağdaş Türkiye Yolunda Adımlar",
                "Atatürkçülük ve Çağdaşlaşan Türkiye",
                "Demokratikleşme Çabaları",
                "Atatürkün Ölümü ve Sonrası"
            ],
            "Din Kültürü": [
                "Kader İnancı",
                "Zekât ve Sadaka",
                "Din ve Hayat",
                "Hz. Muhammedin Örnekliği",
                "Kuran-ı Kerim ve Özellikleri"
            ],
            "İngilizce": [
                "Friendship",
                "Teen Life",
                "In the Kitchen",
                "On the Phone",
                "The Internet",
                "Adventures",
                "Tourism",
                "Chores",
                "Science",
                "Natural Forces"
            ]
        }
    
    def _load_question_bank(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load sample question bank for each subject"""
        return {
            "Matematik": [
                {
                    "id": "mat_001",
                    "topic": "Çarpanlar ve Katlar",
                    "text": "12 sayısının pozitif bölenlerinin toplamı kaçtır?",
                    "options": ["A) 24", "B) 28", "C) 30", "D) 32"],
                    "correct_answer": "B) 28",
                    "explanation": "12'nin pozitif bölenleri: 1, 2, 3, 4, 6, 12. Toplamları: 1+2+3+4+6+12 = 28"
                },
                {
                    "id": "mat_002", 
                    "topic": "Üslü İfadeler",
                    "text": "2⁴ × 2³ işleminin sonucu kaçtır?",
                    "options": ["A) 2⁷", "B) 2¹²", "C) 4⁷", "D) 4¹²"],
                    "correct_answer": "A) 2⁷",
                    "explanation": "Aynı tabanlı sayıların çarpımında üsler toplanır: 2⁴ × 2³ = 2⁴⁺³ = 2⁷"
                },
                {
                    "id": "mat_003",
                    "topic": "Cebirsel İfadeler", 
                    "text": "3x + 2 = 14 denkleminde x kaçtır?",
                    "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
                    "correct_answer": "B) 4",
                    "explanation": "3x + 2 = 14 → 3x = 12 → x = 4"
                }
            ],
            "Türkçe": [
                {
                    "id": "tur_001",
                    "topic": "Sözcükte Anlam",
                    "text": "'Kitabı masanın üzerine koydu.' cümlesinde 'üzerine' sözcüğü hangi anlamda kullanılmıştır?",
                    "options": ["A) Zaman", "B) Yer", "C) Sebep", "D) Amaç"],
                    "correct_answer": "B) Yer",
                    "explanation": "'Üzerine' sözcüğü burada yer bildiren bir edat olarak kullanılmıştır."
                },
                {
                    "id": "tur_002",
                    "topic": "Cümlenin Öğeleri",
                    "text": "'Çocuklar parkta top oynuyor.' cümlesinde özne hangisidir?",
                    "options": ["A) Çocuklar", "B) parkta", "C) top", "D) oynuyor"],
                    "correct_answer": "A) Çocuklar",
                    "explanation": "'Kim?' sorusunun cevabı olan 'Çocuklar' sözcüğü öznedir."
                }
            ],
            "Fen Bilimleri": [
                {
                    "id": "fen_001",
                    "topic": "DNA ve Genetik Kod",
                    "text": "DNA'nın açılımı nedir?",
                    "options": ["A) Deoksiribonükleik Asit", "B) Ribonükleik Asit", "C) Amino Asit", "D) Yağ Asidi"],
                    "correct_answer": "A) Deoksiribonükleik Asit",
                    "explanation": "DNA, Deoksiribonükleik Asitin kısaltmasıdır ve kalıtsal bilgileri taşır."
                }
            ],
            "T.C. İnkılap Tarihi": [
                {
                    "id": "ink_001",
                    "topic": "Bir Kahraman Doğuyor",
                    "text": "Mustafa Kemal Atatürk hangi yılda doğmuştur?",
                    "options": ["A) 1880", "B) 1881", "C) 1882", "D) 1883"],
                    "correct_answer": "B) 1881",
                    "explanation": "Mustafa Kemal Atatürk 1881 yılında Selanik'te doğmuştur."
                }
            ]
        }
    
    def get_topics(self, subject: str) -> List[str]:
        """Get topics for a given subject"""
        return self.meb_curriculum.get(subject, [])
    
    def get_lesson_content(self, subject: str, topic: str) -> str:
        """Get lesson content for a topic"""
        
        # Sample lesson content - in real app this would come from comprehensive database
        lesson_templates = {
            "Matematik": {
                "Çarpanlar ve Katlar": """
                ## 🔢 Çarpanlar ve Katlar
                
                **Çarpan Nedir?**
                Bir sayıyı tam olarak bölen sayılara o sayının çarpanı denir.
                
                **Örnek:** 12 sayısının çarpanları
                - 12 ÷ 1 = 12 ✅
                - 12 ÷ 2 = 6 ✅  
                - 12 ÷ 3 = 4 ✅
                - 12 ÷ 4 = 3 ✅
                - 12 ÷ 6 = 2 ✅
                - 12 ÷ 12 = 1 ✅
                
                Yani 12'nin çarpanları: 1, 2, 3, 4, 6, 12
                
                **Kat Nedir?**
                Bir sayının pozitif tam sayılarla çarpımına o sayının katı denir.
                
                **Örnek:** 3'ün katları
                3 × 1 = 3, 3 × 2 = 6, 3 × 3 = 9, 3 × 4 = 12...
                Yani 3'ün katları: 3, 6, 9, 12, 15, 18...
                """,
                
                "Üslü İfadeler": """
                ## ⚡ Üslü İfadeler
                
                **Üs Nedir?**
                Bir sayının kaç kez kendisiyle çarpıldığını gösteren küçük rakam.
                
                **Örnek:** 2⁴ = 2 × 2 × 2 × 2 = 16
                - 2: taban
                - 4: üs
                - 16: değer
                
                **Üslü Sayılarda İşlemler:**
                - Çarpma: aᵐ × aⁿ = aᵐ⁺ⁿ
                - Bölme: aᵐ ÷ aⁿ = aᵐ⁻ⁿ
                - Üssün üssü: (aᵐ)ⁿ = aᵐˣⁿ
                
                **Fenerbahçe Örneği:** ⚽
                Fenerbahçe 2² = 4 gol attı, sonra 2³ = 8 gol daha attı.
                Toplam: 2² + 2³ = 4 + 8 = 12 gol! 💛💙
                """
            },
            "Türkçe": {
                "Sözcükte Anlam": """
                ## 📚 Sözcükte Anlam
                
                **Anlam Türleri:**
                
                **1. Temel Anlam (Gerçek Anlam)**
                Sözcüğün sözlükteki ilk anlamı
                Örnek: Aslan → Büyük, yeleli vahşi hayvan
                
                **2. Yan Anlam (Mecaz Anlam)**  
                Sözcüğün benzetme yoluyla kazandığı anlam
                Örnek: Aslan → Cesur, güçlü kişi
                
                **3. Çağrışım Anlam**
                Sözcüğün zihnimizde uyandırdığı duygular
                Örnek: Fenerbahçe → Başarı, tutku, mücadele 💛💙
                
                **Çok Anlamlılık:**
                Bir sözcüğün birden fazla anlamı olması
                Örnek: 
                - Yüz: Vücut organı / Sayı
                - Saray: Padişah evi / Saha kenarı
                """
            }
        }
        
        subject_content = lesson_templates.get(subject, {})
        return subject_content.get(topic, f"**{topic}** konusu için içerik hazırlanıyor... 📚")
    
    def get_question(self, subject: str, topic: str) -> Dict[str, Any]:
        """Get a random question for the given subject and topic"""
        subject_questions = self.question_bank.get(subject, [])
        
        # Filter questions by topic if available
        topic_questions = [q for q in subject_questions if q.get('topic') == topic]
        
        if not topic_questions:
            # If no specific topic questions, get any from subject
            topic_questions = subject_questions
        
        if topic_questions:
            return random.choice(topic_questions)
        
        # Fallback question if no questions available
        return {
            "id": f"fallback_{subject}_{topic}",
            "topic": topic,
            "text": f"{topic} konusundan bir soru hazırlanıyor...",
            "options": ["A) Seçenek 1", "B) Seçenek 2", "C) Seçenek 3", "D) Seçenek 4"],
            "correct_answer": "A) Seçenek 1",
            "explanation": "Bu bir örnek sorudur."
        }
    
    def check_answer(self, question_id: str, user_answer: str) -> bool:
        """Check if user's answer is correct"""
        # Find the question by ID
        for subject_questions in self.question_bank.values():
            for question in subject_questions:
                if question['id'] == question_id:
                    return question['correct_answer'] == user_answer
        
        return False
    
    def get_lgs_practice_questions(self, subject: str, count: int = 5) -> List[Dict[str, Any]]:
        """Get LGS-style practice questions"""
        subject_questions = self.question_bank.get(subject, [])
        
        if len(subject_questions) >= count:
            return random.sample(subject_questions, count)
        else:
            return subject_questions
    
    def get_weak_topics(self, username: str, subject: str) -> List[str]:
        """Get topics where student makes most mistakes"""
        # This would connect to database to analyze mistakes
        # For demo, return some sample weak topics
        weak_topics_sample = {
            "Matematik": ["Cebirsel İfadeler", "Dönüşüm Geometrisi"],
            "Türkçe": ["Paragrafta Anlam", "Söz Sanatları"],
            "Fen Bilimleri": ["DNA ve Genetik Kod"],
            "T.C. İnkılap Tarihi": ["Demokratikleşme Çabaları"]
        }
        
        return weak_topics_sample.get(subject, [])
    
    def get_topic_priority(self, subject: str, topic: str) -> int:
        """Get priority level for LGS exam (1-5, 5 being highest)"""
        # Based on historical LGS question frequency
        priority_map = {
            "Matematik": {
                "Çarpanlar ve Katlar": 5,
                "Cebirsel İfadeler": 5,
                "Doğrusal Denklemler ve Eşitsizlikler": 4,
                "Üçgenler": 4,
                "Veri Analizi ve İstatistik": 3
            },
            "Türkçe": {
                "Paragrafta Anlam": 5,
                "Sözcükte Anlam": 4,
                "Cümlenin Öğeleri": 4,
                "Söz Sanatları": 3
            }
        }
        
        return priority_map.get(subject, {}).get(topic, 3)
