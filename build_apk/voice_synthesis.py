import os
import tempfile
import streamlit as st
from typing import Optional
import base64
import json
import requests
from datetime import datetime

class VoiceSynthesis:
    def __init__(self):
        self.voice_settings = {
            "alex_voice": {
                "rate": 1.0,
                "pitch": 1.1,
                "volume": 0.8,
                "voice_type": "friendly_teacher"
            },
            "languages": {
                "turkish": "tr-TR",
                "english": "en-US"
            },
            "emotion_modes": {
                "encouraging": {"pitch": 1.2, "rate": 0.9},
                "explaining": {"pitch": 1.0, "rate": 0.8},
                "celebrating": {"pitch": 1.3, "rate": 1.1},
                "comforting": {"pitch": 0.9, "rate": 0.7}
            }
        }
        
        self.alex_personality_voices = {
            "greeting": "🎵 Merhaba Tuna! Ben Alex, senin süper zeki matematik mentöörün!",
            "encouragement": [
                "💪 Harika gidiyorsun! Beynin şu anda güçleniyor!",
                "⭐ Sen gerçekten yeteneklisin! Devam et!",
                "🚀 Her doğru cevap seni hedefe yaklaştırıyor!",
                "🎯 Mükemmel! Zihnin çok hızlı çalışıyor!"
            ],
            "mistake_support": [
                "😊 Hiç sorun değil! Hatalar öğrenmenin en önemli parçası!",
                "💡 Bu hata sana yeni bir şey öğretti! Harika!", 
                "🎈 Yanılmak cesaret gerektirir! Sen çok cesursun!",
                "🌟 Her hata seni daha güçlü yapıyor!"
            ],
            "learning_tips": [
                "🧠 Şimdi gözlerini kapat ve konuyu zihninde canlandır!",
                "🏠 Bu bilgiyi evinin hangi odasına yerleştirirsin?",
                "🎨 Bu konuyu resim yaparak hatırlar mısın?",
                "🎵 Bu formülü şarkı haline getirebilir miyiz?"
            ]
        }
    
    def speak(self, text: str, emotion: str = "explaining", language: str = "turkish"):
        """Alex'in gelişmiş ses sentezi"""
        # Emotion ayarlarını uygula
        emotion_settings = self.voice_settings["emotion_modes"].get(emotion, {})
        
        # HTML5 Web Speech API kullanarak ses çıkışı
        speech_html = f"""
        <script>
        function speakText() {{
            if ('speechSynthesis' in window) {{
                var utterance = new SpeechSynthesisUtterance("{text}");
                utterance.lang = "{self.voice_settings['languages'][language]}";
                utterance.rate = {emotion_settings.get('rate', 1.0)};
                utterance.pitch = {emotion_settings.get('pitch', 1.0)};
                utterance.volume = {self.voice_settings['alex_voice']['volume']};
                
                // Alex'in özel karakteristiklerini ekle
                utterance.onstart = function() {{
                    console.log('Alex konuşuyor...');
                }};
                
                utterance.onend = function() {{
                    console.log('Alex konuşmasını bitirdi.');
                }};
                
                speechSynthesis.speak(utterance);
            }} else {{
                alert('Tarayıcınız ses özelliğini desteklemiyor.');
            }}
        }}
        speakText();
        </script>
        """
        
        st.components.v1.html(speech_html, height=0)
        
        # Konuşma logunu kaydet
        self._log_speech_interaction(text, emotion, language)
    
    def get_alex_response(self, context: str, user_performance: dict) -> str:
        """Kullanıcı performansına göre Alex'in yanıtını oluştur"""
        if user_performance.get("is_correct", False):
            if user_performance.get("streak", 0) >= 5:
                response = "🔥 İnanılmaz! 5 doğru üst üste! Sen gerçek bir matematik ninjasısın! "
                response += "Beynin şu anda nöral bağlantıları güçlendiriyor!"
            elif user_performance.get("accuracy", 0) >= 90:
                response = "⭐ Mükemmel! %90 üzeri başarı! Zihnin süper hızda çalışıyor!"
            else:
                response = random.choice(self.alex_personality_voices["encouragement"])
        else:
            response = random.choice(self.alex_personality_voices["mistake_support"])
            
            # Hafıza tekniği önerisi ekle
            if context == "study_session":
                response += " " + random.choice(self.alex_personality_voices["learning_tips"])
        
        return response
    
    def create_personalized_audio_lesson(self, subject: str, topic: str, user_level: str) -> dict:
        """Kişiselleştirilmiş sesli ders oluştur"""
        lesson_script = self._generate_lesson_script(subject, topic, user_level)
        
        audio_lesson = {
            "lesson_id": f"audio_{subject}_{topic}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "subject": subject,
            "topic": topic,
            "duration": len(lesson_script.split()) * 0.5,  # Yaklaşık konuşma süresi
            "script": lesson_script,
            "interactive_points": self._create_interactive_points(lesson_script),
            "voice_settings": {
                "emotion": "explaining",
                "pace": "moderate",
                "emphasis_words": self._identify_key_terms(lesson_script)
            }
        }
        
        return audio_lesson
    
    def _generate_lesson_script(self, subject: str, topic: str, user_level: str) -> str:
        """Ders için ses script'i oluştur"""
        scripts = {
            "Matematik": {
                "beginner": f"""
                Merhaba Tuna! Ben Alex. Bugün {topic} konusunu birlikte öğreneceğiz.
                
                Önce nefes alalım ve zihnimizi rahatlatalalım. Hazır mısın?
                
                {topic} aslında çok basit. Şimdi gözlerini kapat ve hayal et...
                
                Bu konuyu öğrenmek için zihin sarayı tekniğini kullanacağız.
                Evinin salonunu hayal et. Bu salon bizim {topic} öğrenme merkezimiz olacak.
                
                Şimdi bu bilgileri görsel olarak yerleştirelim...
                """,
                "intermediate": f"""
                Selam Tuna! Alex burada. {topic} konusunda ilerliyorsun!
                
                Bugün daha derinlemesine gideceğiz. Hazırlanacağın zaman!
                
                Aralıklı tekrar prensibini hatırlıyor musun? Bu konuyu 1-3-7 gün sonra tekrar edeceğiz.
                
                Şimdi aktif geri getirme yapacağız. Dinleme, sadece hatırlamaya çalış...
                """
            }
        }
        
        return scripts.get(subject, {}).get(user_level, f"{topic} konusunu öğreniyoruz...")
    
    def _create_interactive_points(self, script: str) -> list:
        """Script'te etkileşimli noktalar oluştur"""
        return [
            {"time": 30, "action": "pause", "message": "Şimdi dur ve düşün..."},
            {"time": 60, "action": "question", "message": "Bu kısmı anladın mı?"},
            {"time": 90, "action": "visualization", "message": "Gözlerini kapat ve hayal et..."}
        ]
    
    def _identify_key_terms(self, script: str) -> list:
        """Script'teki anahtar kelimeleri belirle"""
        key_terms = ["formül", "kural", "örnek", "çözüm", "yöntem", "teknik"]
        found_terms = []
        
        for term in key_terms:
            if term in script.lower():
                found_terms.append(term)
        
        return found_terms
    
    def _log_speech_interaction(self, text: str, emotion: str, language: str):
        """Ses etkileşimini logla"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "text_length": len(text),
            "emotion": emotion,
            "language": language,
            "interaction_type": "speech_synthesis"
        }
        
        # Session state'e kaydet
        if 'speech_logs' not in st.session_state:
            st.session_state.speech_logs = []
        
        st.session_state.speech_logs.append(log_entry)

class VoiceSynthesis:
    def __init__(self):
        # Alex's voice characteristics
        self.voice_config = {
            "language": "tr-TR",  # Turkish
            "gender": "male",
            "age": "young_adult",
            "personality": "friendly",
            "speed": "normal",
            "pitch": "medium"
        }
        
        # Turkish phonetic adjustments for better pronunciation
        self.pronunciation_map = {
            "Alex": "Aleks",
            "Tuna": "Tuna",
            "Fenerbahçe": "Fenerbahçe",
            "matematik": "matematik",
            "Pomodoro": "Pomodoro",
            "LGS": "L-G-S"
        }
    
    def speak(self, text: str, voice_type: str = "default") -> bool:
        """
        Convert text to speech using browser's Web Speech API
        Returns True if successful, False otherwise
        """
        try:
            # Clean and prepare text for speech
            clean_text = self._prepare_text_for_speech(text)
            
            # Use Streamlit's HTML component to trigger browser speech
            speech_html = self._generate_speech_html(clean_text, voice_type)
            st.components.v1.html(speech_html, height=0)
            
            return True
            
        except Exception as e:
            st.error(f"🔊 Ses çalma hatası: {str(e)}")
            return False
    
    def _prepare_text_for_speech(self, text: str) -> str:
        """Prepare text for better Turkish pronunciation"""
        # Remove markdown and HTML tags
        import re
        clean_text = re.sub(r'[*_#`]', '', text)
        clean_text = re.sub(r'<[^>]+>', '', clean_text)
        
        # Apply pronunciation corrections
        for original, corrected in self.pronunciation_map.items():
            clean_text = clean_text.replace(original, corrected)
        
        # Handle mathematical expressions
        clean_text = clean_text.replace('×', ' çarpı ')
        clean_text = clean_text.replace('÷', ' bölü ')
        clean_text = clean_text.replace('=', ' eşittir ')
        clean_text = clean_text.replace('+', ' artı ')
        clean_text = clean_text.replace('-', ' eksi ')
        
        # Handle special Turkish characters properly
        clean_text = clean_text.replace('ğ', 'ğ')
        clean_text = clean_text.replace('ı', 'ı')
        clean_text = clean_text.replace('ş', 'ş')
        clean_text = clean_text.replace('ç', 'ç')
        clean_text = clean_text.replace('ö', 'ö')
        clean_text = clean_text.replace('ü', 'ü')
        
        # Remove excessive punctuation for smoother speech
        clean_text = re.sub(r'[!]{2,}', '!', clean_text)
        clean_text = re.sub(r'[?]{2,}', '?', clean_text)
        clean_text = re.sub(r'[.]{2,}', '.', clean_text)
        
        return clean_text.strip()
    
    def _generate_speech_html(self, text: str, voice_type: str) -> str:
        """Generate HTML with JavaScript for text-to-speech"""
        
        # Adjust voice settings based on type
        voice_settings = self._get_voice_settings(voice_type)
        
        html_template = f"""
        <script>
        function speakText() {{
            if ('speechSynthesis' in window) {{
                // Cancel any ongoing speech
                speechSynthesis.cancel();
                
                const utterance = new SpeechSynthesisUtterance(`{text}`);
                
                // Configure voice settings
                utterance.lang = '{voice_settings['language']}';
                utterance.rate = {voice_settings['rate']};
                utterance.pitch = {voice_settings['pitch']};
                utterance.volume = {voice_settings['volume']};
                
                // Try to find a Turkish voice
                const voices = speechSynthesis.getVoices();
                const turkishVoice = voices.find(voice => 
                    voice.lang.startsWith('tr') || 
                    voice.lang.startsWith('TR')
                );
                
                if (turkishVoice) {{
                    utterance.voice = turkishVoice;
                }}
                
                // Add event listeners
                utterance.onstart = function() {{
                    console.log('Alex konuşmaya başladı');
                }};
                
                utterance.onend = function() {{
                    console.log('Alex konuşmayı bitirdi');
                }};
                
                utterance.onerror = function(event) {{
                    console.error('Konuşma hatası:', event.error);
                }};
                
                // Speak the text
                speechSynthesis.speak(utterance);
            }} else {{
                console.error('Tarayıcı ses sentezini desteklemiyor');
                alert('Tarayıcınız ses özelliğini desteklemiyor.');
            }}
        }}
        
        // Auto-trigger speech when component loads
        setTimeout(speakText, 100);
        </script>
        """
        
        return html_template
    
    def _get_voice_settings(self, voice_type: str) -> dict:
        """Get voice configuration based on context"""
        base_settings = {
            "language": "tr-TR",
            "rate": 0.9,    # Slightly slower for clarity
            "pitch": 1.1,   # Slightly higher for friendliness
            "volume": 0.8   # Not too loud
        }
        
        # Adjust settings based on voice type
        if voice_type == "explanation":
            base_settings.update({
                "rate": 0.8,    # Slower for explanations
                "pitch": 1.0    # Normal pitch for serious content
            })
        elif voice_type == "motivation":
            base_settings.update({
                "rate": 1.0,    # Normal speed for motivation
                "pitch": 1.2    # Higher pitch for excitement
            })
        elif voice_type == "encouragement":
            base_settings.update({
                "rate": 0.9,    # Gentle pace
                "pitch": 1.1    # Warm and supportive
            })
        
        return base_settings
    
    def speak_explanation(self, text: str) -> bool:
        """Speak educational explanation with appropriate tone"""
        return self.speak(text, "explanation")
    
    def speak_motivation(self, text: str) -> bool:
        """Speak motivational message with energetic tone"""
        return self.speak(text, "motivation")
    
    def speak_encouragement(self, text: str) -> bool:
        """Speak encouragement with supportive tone"""
        return self.speak(text, "encouragement")
    
    def create_audio_button(self, text: str, button_text: str = "🔊 Sesli Dinle", key: str = None) -> bool:
        """Create a button that speaks text when clicked"""
        button_key = key or f"audio_{hash(text) % 10000}"
        
        if st.button(button_text, key=button_key):
            return self.speak(text)
        
        return False
    
    def get_voice_status(self) -> dict:
        """Get current voice synthesis status and capabilities"""
        status_html = """
        <script>
        if ('speechSynthesis' in window) {
            const voices = speechSynthesis.getVoices();
            const turkishVoices = voices.filter(voice => 
                voice.lang.startsWith('tr') || voice.lang.startsWith('TR')
            );
            
            console.log('Toplam ses sayısı:', voices.length);
            console.log('Türkçe ses sayısı:', turkishVoices.length);
            
            document.write('<div style="color: green;">✅ Ses desteği aktif</div>');
            if (turkishVoices.length > 0) {
                document.write('<div style="color: green;">🇹🇷 Türkçe ses mevcut</div>');
            } else {
                document.write('<div style="color: orange;">⚠️ Türkçe ses bulunamadı, varsayılan ses kullanılacak</div>');
            }
        } else {
            document.write('<div style="color: red;">❌ Ses desteği yok</div>');
        }
        </script>
        """
        
        st.components.v1.html(status_html, height=100)
        
        return {
            "supported": True,  # Assume supported for modern browsers
            "turkish_available": True,  # Most browsers have Turkish TTS
            "quality": "browser_native"
        }
    
    def create_interactive_lesson(self, lesson_content: dict) -> None:
        """Create an interactive lesson with speech narration"""
        st.markdown("### 🎧 İnteraktif Ders")
        
        # Title and introduction
        if st.button("▶️ Dersi Başlat", key="start_lesson"):
            intro_text = f"Merhaba! Ben Alex, senin matematik mühendisi koçun. Bugün {lesson_content.get('title', 'bu konuyu')} öğreneceğiz."
            self.speak_motivation(intro_text)
        
        # Main content with audio segments
        for i, section in enumerate(lesson_content.get('sections', [])):
            st.markdown(f"#### {section.get('title', f'Bölüm {i+1}')}")
            st.markdown(section.get('content', ''))
            
            if st.button(f"🔊 Bölüm {i+1} Dinle", key=f"section_{i}"):
                section_text = f"{section.get('title', '')}: {section.get('content', '')}"
                self.speak_explanation(section_text)
        
        # Conclusion
        if st.button("🎯 Ders Özeti", key="lesson_summary"):
            summary_text = f"Harika! {lesson_content.get('title', 'Bu konuyu')} başarıyla tamamladın. Artık pratik yapmaya hazırsın!"
            self.speak_encouragement(summary_text)
    
    def create_question_narration(self, question_text: str, options: list) -> None:
        """Create narrated question reading"""
        if st.button("📖 Soruyu Oku", key=f"read_question_{hash(question_text) % 1000}"):
            full_text = f"Soru: {question_text} Seçenekler: "
            for option in options:
                full_text += f"{option}. "
            
            self.speak_explanation(full_text)
    
    def create_pronunciation_helper(self, word: str, pronunciation: str = None) -> None:
        """Help with pronunciation of difficult words"""
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{word}**")
            if pronunciation:
                st.caption(f"Telaffuz: {pronunciation}")
        
        with col2:
            if st.button("🔊", key=f"pronounce_{word}"):
                self.speak(pronunciation or word)
    
    def create_fenerbahce_cheer(self, text: str) -> None:
        """Create Fenerbahçe-themed motivational speech"""
        cheer_button_html = """
        <style>
        .fenerbahce-button {
            background: linear-gradient(45deg, #FFDC00, #1F2A44);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        </style>
        """
        
        st.markdown(cheer_button_html, unsafe_allow_html=True)
        
        if st.button("⚽ FORZA FENERBAHÇE! 💛💙", key="fb_cheer"):
            fenerbahce_text = f"Forza Fenerbahçe! {text} Hadi Tuna, şampiyonlar gibi çalış!"
            self.speak_motivation(fenerbahce_text)
