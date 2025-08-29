import os
import tempfile
import streamlit as st
from typing import Optional
import base64

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
