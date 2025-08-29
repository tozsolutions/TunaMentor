import streamlit as st
import json
import datetime
from alex_ai import AlexAI
from database import Database
from curriculum import Curriculum
from gamification import Gamification
from fenerbahce_integration import FenerbahceIntegration
from progress_tracker import ProgressTracker
from parent_dashboard import ParentDashboard
from study_planner import StudyPlanner
from voice_synthesis import VoiceSynthesis
import time
import pandas as pd

# Initialize session state with advanced learning systems
if 'db' not in st.session_state:
    st.session_state.db = Database()
    st.session_state.alex = AlexAI()
    st.session_state.curriculum = Curriculum()
    st.session_state.gamification = Gamification(st.session_state.db)
    st.session_state.fenerbahce = FenerbahceIntegration()
    st.session_state.progress = ProgressTracker(st.session_state.db)
    st.session_state.parent_dash = ParentDashboard(st.session_state.db)
    st.session_state.planner = StudyPlanner(st.session_state.db)
    st.session_state.voice = VoiceSynthesis()
    
    # Gelişmiş öğrenme sistemleri
    from memory_techniques import MemoryTechniques
    st.session_state.memory = MemoryTechniques()
    
    st.session_state.user_authenticated = False
    st.session_state.current_session = None
    st.session_state.current_memory_palace = None
    st.session_state.active_mind_map = None
    st.session_state.spaced_repetition_queue = []

# Custom CSS for Fenerbahçe theme with background images
st.markdown("""
<style>
    /* Ana sayfa arka planı - Fenerbahçe temalı */
    .main > div {
        background: 
            linear-gradient(135deg, rgba(31,42,68,0.95), rgba(255,220,0,0.25)),
            radial-gradient(circle at 20% 30%, rgba(255,220,0,0.3) 0%, transparent 60%),
            radial-gradient(circle at 80% 70%, rgba(31,42,68,0.4) 0%, transparent 60%),
            url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><pattern id="fbpattern" x="0" y="0" width="150" height="150" patternUnits="userSpaceOnUse"><circle cx="75" cy="75" r="30" fill="none" stroke="%23FFDC00" stroke-width="3" opacity="0.2"/><polygon points="75,45 85,70 75,95 65,70" fill="%23FFDC00" opacity="0.15"/></pattern></defs><rect width="100%" height="100%" fill="url(%23fbpattern)"/></svg>');
        background-size: cover, auto, auto, 300px 300px;
        background-position: center, 0 0, 100% 100%, 0 0;
        background-attachment: fixed;
        min-height: 100vh;
        position: relative;
    }
    
    .main > div::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(255,220,0,0.2) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(31,42,68,0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(255,220,0,0.1) 0%, transparent 50%),
            url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" fill="none" stroke="%23FFDC00" stroke-width="1" opacity="0.1"/><circle cx="50" cy="50" r="15" fill="none" stroke="%231F2A44" stroke-width="0.5" opacity="0.2"/></svg>');
        background-size: auto, auto, auto, 300px 300px;
        z-index: -1;
        pointer-events: none;
        animation: float 10s infinite ease-in-out;
    }
    
    @keyframes float {
        0%, 100% { 
            transform: translateY(0px) rotate(0deg); 
        }
        50% { 
            transform: translateY(-20px) rotate(180deg); 
        }
    }
    
    /* Sayfa özel arka planları */
    .study-page-bg {
        background: linear-gradient(135deg, rgba(255,220,0,0.1), rgba(31,42,68,0.9));
    }
    
    .games-page-bg {
        background: linear-gradient(135deg, rgba(31,42,68,0.9), rgba(255,220,0,0.2));
    }
    
    .fenerbahce-page-bg {
        background: linear-gradient(45deg, rgba(255,220,0,0.3), rgba(31,42,68,0.8));
    }
    
    .progress-page-bg {
        background: linear-gradient(135deg, rgba(31,42,68,0.8), rgba(255,220,0,0.1));
    }
    
    .main-header {
        background: linear-gradient(135deg, rgba(255,220,0,0.95), rgba(31,42,68,0.95));
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        color: white;
        font-weight: bold;
        box-shadow: 0 8px 32px rgba(255,220,0,0.3);
        border: 2px solid rgba(255,220,0,0.4);
    }
    .alex-avatar {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 5px solid #FFDC00;
        background: 
            radial-gradient(circle at 30% 30%, #87CEEB 0%, #4169E1 100%),
            linear-gradient(135deg, #1F2A44, #FFDC00);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px auto;
        box-shadow: 
            0 0 30px rgba(255,220,0,0.8),
            inset 0 0 30px rgba(255,255,255,0.2),
            0 8px 16px rgba(0,0,0,0.3);
        animation: alex3d 3s infinite ease-in-out;
        position: relative;
        overflow: visible;
        font-size: 0;
        z-index: 10;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    
    .alex-avatar:hover {
        transform: scale(1.1) rotateY(10deg);
    }
    
    .alex-avatar::before {
        content: '👨‍🏫';
        position: absolute;
        font-size: 80px;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 12;
        text-shadow: 
            3px 3px 6px rgba(0,0,0,0.5),
            0 0 15px rgba(255,220,0,0.8);
        animation: alexBlink 4s infinite;
    }
    
    .alex-avatar::after {
        content: 'ALEX';
        position: absolute;
        bottom: -35px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 16px;
        font-weight: bold;
        color: #FFDC00;
        background: rgba(31,42,68,0.9);
        padding: 5px 15px;
        border-radius: 20px;
        border: 2px solid #FFDC00;
        letter-spacing: 3px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        z-index: 11;
    }
    
    @keyframes alex3d {
        0%, 100% { 
            transform: translateY(0px) rotateX(0deg) rotateY(0deg);
            box-shadow: 
                0 0 30px rgba(255,220,0,0.8),
                inset 0 0 30px rgba(255,255,255,0.2),
                0 8px 16px rgba(0,0,0,0.3);
        }
        25% { 
            transform: translateY(-10px) rotateX(5deg) rotateY(5deg);
            box-shadow: 
                0 0 40px rgba(255,220,0,1),
                inset 0 0 40px rgba(255,255,255,0.3),
                0 12px 20px rgba(0,0,0,0.4);
        }
        50% { 
            transform: translateY(-5px) rotateX(-2deg) rotateY(-2deg);
            box-shadow: 
                0 0 35px rgba(255,220,0,0.9),
                inset 0 0 35px rgba(255,255,255,0.25),
                0 10px 18px rgba(0,0,0,0.35);
        }
        75% { 
            transform: translateY(-8px) rotateX(3deg) rotateY(-3deg);
            box-shadow: 
                0 0 38px rgba(255,220,0,0.95),
                inset 0 0 38px rgba(255,255,255,0.28),
                0 11px 19px rgba(0,0,0,0.37);
        }
    }
    
    @keyframes alexBlink {
        0%, 90%, 100% { 
            content: '👨‍🏫';
        }
        93%, 97% { 
            content: '😊';
        }
    }
    
    .alex-avatar::before {
        content: 'ALEX';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 11;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
        letter-spacing: 2px;
        text-shadow: 
            2px 2px 4px rgba(0,0,0,0.8),
            0 0 10px rgba(255,220,0,0.6);
    }
    
    .alex-avatar::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: shine 3s infinite;
        z-index: 1;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes shine {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .alex-speech-bubble {
        background: rgba(255,255,255,0.95);
        border: 2px solid #FFDC00;
        border-radius: 20px;
        padding: 15px;
        margin: 10px;
        position: relative;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        backdrop-filter: blur(5px);
    }
    
    .alex-speech-bubble::before {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 30px;
        width: 0;
        height: 0;
        border-left: 15px solid transparent;
        border-right: 15px solid transparent;
        border-top: 15px solid #FFDC00;
    }
    .progress-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FFDC00;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .achievement-badge {
        background: linear-gradient(45deg, #FFDC00, #1F2A44);
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        margin: 2px;
        display: inline-block;
    }
    .fenerbahce-colors {
        background: linear-gradient(90deg, #FFDC00 50%, #1F2A44 50%);
        height: 5px;
        width: 100%;
        margin: 10px 0;
    }
    .study-button {
        background: #FFDC00;
        color: #1F2A44;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

def authenticate_user():
    """Simple authentication for Tuna"""
    st.markdown('<div class="main-header"><h1>🎯 ALEX LGS KOÇUM - 2026 HAZIRLIK SİSTEMİ</h1></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="alex-avatar">ALEX</div>', unsafe_allow_html=True)
        st.markdown("### 👋 Merhaba! Ben Alex, senin matematik mühendisi koçun!")
        
        name = st.text_input("📝 Adını gir:", placeholder="Tuna")
        password = st.text_input("🔐 Şifren:", type="password", placeholder="Şifreni gir")
        
        if st.button("🚀 Çalışmaya Başla!", key="login"):
            if name.lower() == "tuna" and password:
                st.session_state.user_authenticated = True
                st.session_state.current_user = name
                st.session_state.db.create_user_session(name)
                st.rerun()
            else:
                st.error("❌ Hatalı bilgi! Sadece Tuna giriş yapabilir.")

def main_app():
    """Main application interface"""
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown('<div class="alex-avatar">ALEX</div>', unsafe_allow_html=True)
        st.markdown("### 🎯 Matematik Mühendisi Koçun")
        
        # User stats
        user_stats = st.session_state.progress.get_user_stats("tuna")
        st.metric("📊 Toplam Puan", user_stats.get('total_points', 0))
        st.metric("🔥 Seri", user_stats.get('streak', 0))
        st.metric("⭐ Seviye", user_stats.get('level', 1))
        
        # Navigation
        page = st.selectbox("📚 Bölümler", [
            "🏠 Ana Sayfa",
            "📖 Ders Çalış",
            "🎮 Oyunlar",
            "⚽ Fenerbahçe",
            "📊 İlerleme",
            "🚀 Gelecek Dersleri",
            "👨‍👩‍👧‍👦 Aile Paneli"
        ])
    
    # Main content area
    if page == "🏠 Ana Sayfa":
        show_home_page()
    elif page == "📖 Ders Çalış":
        show_study_page()
    elif page == "🎮 Oyunlar":
        show_games_page()
    elif page == "⚽ Fenerbahçe":
        show_fenerbahce_page()
    elif page == "📊 İlerleme":
        show_progress_page()
    elif page == "🚀 Gelecek Dersleri":
        show_future_lessons_page()
    elif page == "👨‍👩‍👧‍👦 Aile Paneli":
        show_parent_dashboard()

def show_home_page():
    """Home page with daily overview"""
    st.markdown('<div class="main-header"><h2>🏠 Hoş Geldin Tuna!</h2></div>', unsafe_allow_html=True)
    
    # Alex greeting with auto-speech
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="alex-avatar"></div>', unsafe_allow_html=True)
    with col2:
        greeting = st.session_state.alex.get_daily_greeting()
        st.markdown(f'<div class="alex-speech-bubble">{greeting}</div>', unsafe_allow_html=True)
        
        # Auto-speak on page load
        if 'home_greeted' not in st.session_state:
            st.session_state.home_greeted = True
            # Trigger auto-speech
            auto_speech_js = f"""
            <script>
            setTimeout(function() {{
                if ('speechSynthesis' in window) {{
                    var utterance = new SpeechSynthesisUtterance('{greeting}');
                    utterance.lang = 'tr-TR';
                    utterance.rate = 0.9;
                    utterance.pitch = 1.1;
                    window.speechSynthesis.speak(utterance);
                }}
            }}, 1000);
            </script>
            """
            st.components.v1.html(auto_speech_js, height=0)
    
    st.markdown('<div class="fenerbahce-colors"></div>', unsafe_allow_html=True)
    
    # Daily plan
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="progress-card"><h4>📅 Bugünkü Plan</h4>', unsafe_allow_html=True)
        daily_plan = st.session_state.planner.get_daily_plan("tuna")
        for task in daily_plan:
            status = "✅" if task['completed'] else "⏳"
            st.markdown(f"{status} {task['subject']} - {task['duration']} dk")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="progress-card"><h4>⚽ Fenerbahçe</h4>', unsafe_allow_html=True)
        next_match = st.session_state.fenerbahce.get_next_match()
        if next_match:
            st.markdown(f"🏆 **Sonraki Maç:** {next_match['opponent']}")
            st.markdown(f"📅 **Tarih:** {next_match['date']}")
            st.markdown(f"⏰ **Saat:** {next_match['time']}")
            
            # Match reward status
            if st.session_state.gamification.can_watch_full_match("tuna"):
                st.markdown("🎉 **Tam maç izleme hakkın var!**")
            else:
                st.markdown("⚠️ **Görevlerini tamamla, maçı tam izle!**")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="progress-card"><h4>🏆 Başarılarım</h4>', unsafe_allow_html=True)
        achievements = st.session_state.gamification.get_achievements("tuna")
        for achievement in achievements[-3:]:  # Show last 3 achievements
            st.markdown(f'<div class="achievement-badge">{achievement["name"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick study buttons
    st.markdown("### 🚀 Hızlı Çalışma")
    col1, col2, col3, col4 = st.columns(4)
    
    subjects = ["Matematik", "Türkçe", "Fen", "İnkılap"]
    for i, subject in enumerate(subjects):
        with [col1, col2, col3, col4][i]:
            if st.button(f"📚 {subject}", key=f"quick_{subject}"):
                st.session_state.current_subject = subject
                st.rerun()

def show_study_page():
    """Advanced study page with memory techniques"""
    st.markdown('<div class="study-page-bg"></div>', unsafe_allow_html=True)
    st.markdown('<div class="main-header"><h2>🧠 Süper Öğrenme Laboratuvarı!</h2></div>', unsafe_allow_html=True)
    
    # Alex'in gelişmiş önerileri
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="alex-avatar"></div>', unsafe_allow_html=True)
    with col2:
        alex_tip = st.session_state.alex.get_advanced_learning_tip()
        st.markdown(f'<div class="alex-speech-bubble">{alex_tip}</div>', unsafe_allow_html=True)
        
        if st.button("🔊 Alex'i Dinle"):
            st.session_state.voice.speak(alex_tip, emotion="explaining")
    
    # Öğrenme tekniği seçimi
    st.markdown("### 🎯 Öğrenme Tekniği Seç")
    learning_method = st.selectbox("🧠 Nasıl öğrenmek istiyorsun?", [
        "🏰 Zihin Sarayı ile Öğren",
        "🗺️ Zihin Haritası Oluştur", 
        "⚡ Aktif Geri Getirme",
        "🔄 Aralıklı Tekrar",
        "🎴 Görsel Flash Kartlar",
        "📚 Klasik Ders Çalışma"
    ])
    
    # Subject selection
    subject = st.selectbox("📚 Ders Seç:", [
        "Matematik", "Türkçe", "Fen Bilimleri", "T.C. İnkılap Tarihi", 
        "Din Kültürü", "İngilizce"
    ])
    
    # Get topics for selected subject
    topics = st.session_state.curriculum.get_topics(subject)
    topic = st.selectbox("📝 Konu Seç:", topics)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"### 🎯 {topic}")
        
        # Lesson content
        lesson_content = st.session_state.curriculum.get_lesson_content(subject, topic)
        st.markdown(lesson_content)
        
        # Alex explanation
        if st.button("🤖 Alex'ten Açıklama İste"):
            explanation = st.session_state.alex.explain_topic(subject, topic)
            st.markdown(f"**Alex açıklıyor:** {explanation}")
            
            if st.button("🔊 Sesli Dinle", key="explanation_audio"):
                st.session_state.voice.speak(explanation)
    
    with col2:
        st.markdown("### 🎮 Çalışma Araçları")
        
        # Persistent question state
        if f"current_question_{subject}_{topic}" not in st.session_state:
            st.session_state[f"current_question_{subject}_{topic}"] = None
            st.session_state[f"answered_{subject}_{topic}"] = False
            st.session_state[f"score_{subject}_{topic}"] = 0
            st.session_state[f"total_questions_{subject}_{topic}"] = 0
        
        current_q_key = f"current_question_{subject}_{topic}"
        answered_key = f"answered_{subject}_{topic}"
        score_key = f"score_{subject}_{topic}"
        total_key = f"total_questions_{subject}_{topic}"
        
        # Show current stats
        if st.session_state[total_key] > 0:
            st.markdown(f"**📊 Bu Konudaki Performansın:** {st.session_state[score_key]}/{st.session_state[total_key]} doğru")
        
        if st.button("❓ Yeni Soru Getir") or st.session_state[current_q_key] is None:
            question = st.session_state.curriculum.get_question(subject, topic)
            st.session_state[current_q_key] = question
            st.session_state[answered_key] = False
            
            # Alex auto-speaks the question
            if question:
                question_speech = f"Yeni soru geliyor! {question['text']}"
                auto_speech_js = f"""
                <script>
                setTimeout(function() {{
                    if ('speechSynthesis' in window) {{
                        var utterance = new SpeechSynthesisUtterance('{question_speech}');
                        utterance.lang = 'tr-TR';
                        utterance.rate = 0.8;
                        window.speechSynthesis.speak(utterance);
                    }}
                }}, 500);
                </script>
                """
                st.components.v1.html(auto_speech_js, height=0)
        
        current_question = st.session_state[current_q_key]
        if current_question and not st.session_state[answered_key]:
            st.markdown("#### 📝 Soru:")
            st.markdown(current_question['text'])
            
            # Multiple choice options
            user_answer = st.radio("Cevabını seç:", current_question['options'], key=f"answer_{current_q_key}")
            
            if st.button("✅ Cevapla", key=f"submit_{current_q_key}"):
                st.session_state[answered_key] = True
                st.session_state[total_key] += 1
                
                is_correct = st.session_state.curriculum.check_answer(current_question['id'], user_answer)
                
                if is_correct:
                    st.session_state[score_key] += 1
                    st.success("🎉 Doğru! Harika iş!")
                    points_earned = st.session_state.gamification.add_points("tuna", 10)
                    st.info(f"🏆 +10 puan kazandın! Toplam: {points_earned}")
                    
                    # Alex congratulation speech
                    congrats = "Tebrikler! Doğru cevap! Böyle devam et şampiyon!"
                    success_speech_js = f"""
                    <script>
                    setTimeout(function() {{
                        if ('speechSynthesis' in window) {{
                            var utterance = new SpeechSynthesisUtterance('{congrats}');
                            utterance.lang = 'tr-TR';
                            utterance.rate = 0.9;
                            utterance.pitch = 1.2;
                            window.speechSynthesis.speak(utterance);
                        }}
                    }}, 500);
                    </script>
                    """
                    st.components.v1.html(success_speech_js, height=0)
                else:
                    st.error(f"❌ Yanlış. Doğru cevap: {current_question['correct_answer']}")
                    st.session_state.db.log_mistake("tuna", subject, topic, current_question['id'])
                    
                    # Alex encouragement with auto-speech
                    encouragement = st.session_state.alex.get_encouragement()
                    st.info(f"🤖 Alex: {encouragement}")
                    
                    encouragement_speech_js = f"""
                    <script>
                    setTimeout(function() {{
                        if ('speechSynthesis' in window) {{
                            var utterance = new SpeechSynthesisUtterance('{encouragement}');
                            utterance.lang = 'tr-TR';
                            utterance.rate = 0.8;
                            window.speechSynthesis.speak(utterance);
                        }}
                    }}, 500);
                    </script>
                    """
                    st.components.v1.html(encouragement_speech_js, height=0)
        
        elif st.session_state[answered_key]:
            st.info("✅ Bu soruyu cevapladın! Yeni soru için 'Yeni Soru Getir' butonuna tıkla.")
        
        if st.button("🔄 Tekrar Et"):
            st.info("🎯 Bu konuyu aralıklı tekrar listesine eklendi!")
            st.session_state.db.add_to_spaced_repetition("tuna", subject, topic)
        
        if st.button("🎯 Pomodoro Başlat"):
            st.session_state.current_pomodoro = {
                'subject': subject,
                'topic': topic,
                'start_time': datetime.datetime.now(),
                'duration': 25
            }
            st.success("⏰ 25 dakikalık çalışma başladı!")

def show_games_page():
    """Gamification page with rewards and challenges"""
    st.markdown('<div class="games-page-bg"></div>', unsafe_allow_html=True)
    st.markdown('<div class="main-header"><h2>🎮 Oyunlar ve Ödüller</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏆 Puan Durumu")
        user_stats = st.session_state.gamification.get_user_stats("tuna")
        
        st.metric("💰 Toplam Puanın", user_stats['total_points'])
        st.metric("🔥 Günlük Seri", user_stats['streak'])
        st.metric("⭐ Seviye", user_stats['level'])
        
        # Progress bar to next level
        current_xp = user_stats['total_points']
        next_level_xp = user_stats['level'] * 100
        progress = min(100, (current_xp % 100))
        st.progress(progress / 100)
        st.caption(f"Sonraki seviyeye {100 - progress} puan kaldı!")
        
        # Daily challenges
        st.markdown("### 🎯 Günlük Görevler")
        challenges = st.session_state.gamification.get_daily_challenges("tuna")
        
        for challenge in challenges:
            status = "✅" if challenge['completed'] else "⏳"
            st.markdown(f"{status} {challenge['description']} - {challenge['reward']} puan")
    
    with col2:
        st.markdown("### 🛍️ Ödül Mağazası")
        
        # Alex customization
        st.markdown("#### 🤖 Alex'i Özelleştir")
        alex_items = [
            {"name": "Fenerbahçe Forması", "cost": 50, "type": "outfit"},
            {"name": "Matematik Kaskı", "cost": 30, "type": "accessory"},
            {"name": "Özel Ses Paketi", "cost": 100, "type": "voice"},
        ]
        
        for item in alex_items:
            col_item, col_buy = st.columns([3, 1])
            with col_item:
                st.markdown(f"👕 {item['name']} - {item['cost']} puan")
            with col_buy:
                if st.button("Satın Al", key=f"buy_{item['name']}"):
                    if st.session_state.gamification.spend_points("tuna", item['cost']):
                        st.success(f"🎉 {item['name']} satın alındı!")
                    else:
                        st.error("💸 Yeterli puanın yok!")
        
        # Game time rewards
        st.markdown("#### 🎮 Oyun Zamanı")
        if st.button("🕹️ Serbest Oyun Saati (100 puan)"):
            if st.session_state.gamification.spend_points("tuna", 100):
                st.success("🎉 1 saat serbest oyun hakkın açıldı!")
                st.balloons()
            else:
                st.error("💸 Yeterli puanın yok!")

def show_fenerbahce_page():
    """Fenerbahçe integration page"""
    st.markdown('<div class="fenerbahce-page-bg"></div>', unsafe_allow_html=True)
    st.markdown('<div class="main-header"><h2>⚽ FENERBAHÇE - FORZA FB! 💛💙</h2></div>', unsafe_allow_html=True)
    
    # Team colors
    st.markdown('<div class="fenerbahce-colors"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📅 Maç Takvimi")
        fixtures = st.session_state.fenerbahce.get_fixtures()
        
        for match in fixtures[:5]:  # Show next 5 matches
            match_date = datetime.datetime.strptime(match['date'], "%Y-%m-%d")
            is_today = match_date.date() == datetime.date.today()
            
            if is_today:
                st.markdown(f"🔥 **BUGÜN:** {match['opponent']}")
            else:
                st.markdown(f"📅 {match['date']} - {match['opponent']}")
            
            st.markdown(f"⏰ {match['time']} | 🏟️ {match['venue']}")
            
            # Watch permission
            can_watch = st.session_state.gamification.can_watch_full_match("tuna")
            if can_watch:
                st.success("✅ Tam maç izleme hakkın var!")
            else:
                remaining_tasks = st.session_state.gamification.get_remaining_tasks("tuna")
                st.warning(f"⚠️ {remaining_tasks} görev daha tamamla!")
            
            st.markdown("---")
    
    with col2:
        st.markdown("### 🏆 Fenerbahçe Motivasyonu")
        
        fb_motivation = st.session_state.alex.get_fenerbahce_motivation()
        st.markdown(f"💛💙 **Alex:** {fb_motivation}")
        
        if st.button("🔊 Motivasyon Konuşması"):
            st.session_state.voice.speak(fb_motivation)
        
        # FB themed challenges
        st.markdown("### ⚽ Fenerbahçe Görevleri")
        fb_challenges = [
            "⚽ Matematik'te 10 gol at (10 soru çöz)",
            "🥅 Türkçe defansını geç (5 paragraf oku)",
            "🏃‍♂️ Fen'de hızlı koş (15 dk çalış)",
            "👥 Takım oyunu: Tüm dersleri tamamla"
        ]
        
        for challenge in fb_challenges:
            st.markdown(f"• {challenge}")
        
        # Match day special
        if st.session_state.fenerbahce.is_match_day():
            st.markdown("### 🔥 MAÇ GÜNÜ ÖZEL!")
            st.markdown("Bugün tüm görevleri tamamlarsan:")
            st.markdown("🎁 Çifte puan kazanırsın!")
            st.markdown("🍿 Maç öncesi özel atıştırma hakkı!")

def show_progress_page():
    """Progress tracking and analytics"""
    st.markdown('<div class="progress-page-bg"></div>', unsafe_allow_html=True)
    st.markdown('<div class="main-header"><h2>📊 İlerleme Raporum</h2></div>', unsafe_allow_html=True)
    
    # Time period selection
    period = st.selectbox("📅 Zaman Aralığı:", ["Bu Hafta", "Bu Ay", "Tüm Zamanlar"])
    
    # Get progress data
    progress_data = st.session_state.progress.get_progress_data("tuna", period.lower().replace(" ", "_"))
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Genel İstatistikler")
        
        # Key metrics
        st.metric("📚 Toplam Çalışma", f"{progress_data['total_study_time']} saat")
        st.metric("✅ Çözülen Soru", progress_data['questions_solved'])
        st.metric("🎯 Doğruluk Oranı", f"{progress_data['accuracy']}%")
        st.metric("🏆 Kazanılan Puan", progress_data['points_earned'])
        
        # Subject breakdown
        st.markdown("### 📊 Ders Bazında Performans")
        subject_data = progress_data['subject_breakdown']
        
        df = pd.DataFrame(list(subject_data.items()), columns=['Ders', 'Doğruluk'])
        st.bar_chart(df.set_index('Ders'))
    
    with col2:
        st.markdown("### 🎯 Hedef Takibi")
        
        # LGS target
        current_score = progress_data['estimated_lgs_score']
        target_score = 475
        
        st.metric("🎯 LGS Tahmini Puanım", current_score)
        st.metric("🏆 Hedef Puan", target_score)
        
        score_progress = min(100, (current_score / target_score) * 100)
        st.progress(score_progress / 100)
        st.caption(f"Hedefe {target_score - current_score} puan kaldı!")
        
        # Weak areas
        st.markdown("### 🔧 Gelişim Alanları")
        weak_areas = progress_data['weak_areas']
        
        for area in weak_areas:
            st.markdown(f"📝 **{area['subject']}** - {area['topic']}")
            st.caption(f"Doğruluk: {area['accuracy']}% | Öneri: {area['suggestion']}")
        
        # Study recommendations
        if st.button("🤖 Alex'ten Çalışma Önerisi"):
            recommendation = st.session_state.alex.get_study_recommendation(progress_data)
            st.info(f"💡 **Alex önerileri:** {recommendation}")

def show_future_lessons_page():
    """Future skills and career mentoring"""
    st.markdown('<div class="main-header"><h2>🚀 Gelecek Dersleri - Ufuk Açıyoruz!</h2></div>', unsafe_allow_html=True)
    
    # Weekly future lesson
    st.markdown("### 📅 Bu Haftanın Gelecek Dersi")
    
    future_topics = [
        {"title": "🐍 Python Programlama", "duration": "15 dk", "level": "Başlangıç"},
        {"title": "🎮 Oyun Geliştirme", "duration": "15 dk", "level": "Başlangıç"},
        {"title": "🤖 Yapay Zeka Nedir?", "duration": "15 dk", "level": "Keşif"},
        {"title": "📊 Veri Bilimi", "duration": "15 dk", "level": "Keşif"},
        {"title": "🌍 Geleceğin Meslekleri", "duration": "15 dk", "level": "Keşif"}
    ]
    
    current_week = datetime.datetime.now().isocalendar()[1]
    current_topic = future_topics[current_week % len(future_topics)]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"#### {current_topic['title']}")
        st.markdown(f"⏱️ **Süre:** {current_topic['duration']}")
        st.markdown(f"📊 **Seviye:** {current_topic['level']}")
        
        # Lesson content based on topic
        if "Python" in current_topic['title']:
            st.markdown("""
            **Bu hafta Python ile tanışıyoruz!**
            
            Python, dünyanın en popüler programlama dillerinden biri. Neden?
            - 🐍 Kolay öğrenilir
            - 🌍 Her yerde kullanılır (Instagram, YouTube, Netflix)
            - 🤖 Yapay zeka için birinci seçim
            - 📊 Veri analizi için mükemmel
            
            **İlk Python kodum:**
            ```python
            print("Merhaba, ben Tuna!")
            print("LGS'yi kazanacağım!")
            ```
            """)
        
        elif "Oyun" in current_topic['title']:
            st.markdown("""
            **Oyun nasıl yapılır?**
            
            Sevdiğin oyunlar nasıl yapılıyor merak ettin mi?
            - 🎨 Grafik tasarımı
            - 🎵 Ses ve müzik
            - 💻 Programlama
            - 🎮 Oyun mekaniği
            
            **Basit oyun örneği:**
            - Tahmin oyunu
            - Matematik yarışması
            - Kelime bulmaca
            """)
        
        elif "Yapay Zeka" in current_topic['title']:
            st.markdown("""
            **Yapay Zeka - AI nedir?**
            
            Ben Alex de bir yapay zeka örneğiyim! 🤖
            - 🧠 Bilgisayarlar nasıl "düşünür"?
            - 📱 Telefonundaki Siri, Google Assistant
            - 🚗 Otonom arabalar
            - 🎯 Kişiselleştirilmiş öneriler
            
            **Yapay zeka kullandığın yerler:**
            - YouTube önerileri
            - Harita uygulamaları
            - Fotoğraf tanıma
            - Çeviri uygulamaları
            """)
    
    with col2:
        st.markdown("### 🎯 Gelecek Hedefleri")
        
        if st.button("▶️ Dersi Başlat"):
            st.success("🎉 Gelecek dersi başladı!")
            # Add 15 minutes to study time
            st.session_state.db.log_study_time("tuna", "Gelecek Dersleri", 15)
            st.session_state.gamification.add_points("tuna", 20)
        
        st.markdown("### 📚 Tamamlanan Dersler")
        completed_lessons = st.session_state.db.get_completed_future_lessons("tuna")
        
        for lesson in completed_lessons:
            st.markdown(f"✅ {lesson['title']}")
        
        st.markdown("### 🌟 Gelecek Vizyonu")
        st.markdown("""
        **LGS sonrası yolculuk:**
        - 🏫 İyi bir lise
        - 💻 Teknoloji becerileri
        - 🌍 Global perspektif
        - 🚀 Hayal gücün sınırsız!
        """)

def show_parent_dashboard():
    """Parent dashboard and reports"""
    st.markdown('<div class="main-header"><h2>👨‍👩‍👧‍👦 Aile Paneli</h2></div>', unsafe_allow_html=True)
    
    # Authentication for parents
    parent_auth = st.text_input("Ebeveyn Şifresi:", type="password")
    
    if parent_auth == "ebeveyn2026":  # Simple password for demo
        
        # Weekly report
        st.markdown("### 📊 Haftalık Rapor")
        
        weekly_data = st.session_state.parent_dash.get_weekly_report("tuna")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("⏱️ Toplam Çalışma", f"{weekly_data['study_hours']} saat")
        with col2:
            st.metric("✅ Başarı Oranı", f"{weekly_data['success_rate']}%")
        with col3:
            st.metric("🎯 Tamamlanan Görev", weekly_data['completed_tasks'])
        with col4:
            st.metric("🏆 Kazanılan Puan", weekly_data['points_earned'])
        
        # Detailed breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📈 Günlük Çalışma Grafiği")
            daily_study = weekly_data['daily_breakdown']
            df_daily = pd.DataFrame(list(daily_study.items()), columns=['Gün', 'Dakika'])
            st.line_chart(df_daily.set_index('Gün'))
            
            st.markdown("### 🎯 Ders Bazında Performans")
            subject_performance = weekly_data['subject_performance']
            df_subjects = pd.DataFrame(list(subject_performance.items()), columns=['Ders', 'Doğruluk %'])
            st.bar_chart(df_subjects.set_index('Ders'))
        
        with col2:
            st.markdown("### 📝 Hata Analizi")
            mistakes = weekly_data['common_mistakes']
            
            for mistake in mistakes:
                st.markdown(f"**{mistake['subject']} - {mistake['topic']}**")
                st.caption(f"Hata sayısı: {mistake['count']} | Öneri: {mistake['suggestion']}")
                st.markdown("---")
            
            st.markdown("### 🔮 Alex'in Değerlendirmesi")
            alex_evaluation = st.session_state.alex.get_parent_report("tuna", weekly_data)
            st.info(alex_evaluation)
        
        # Recommendations
        st.markdown("### 💡 Öneriler")
        recommendations = st.session_state.parent_dash.get_recommendations("tuna")
        
        for rec in recommendations:
            st.markdown(f"• **{rec['area']}:** {rec['suggestion']}")
        
        # Download report
        if st.button("📥 Raporu İndir"):
            report_text = st.session_state.parent_dash.generate_report_text("tuna", weekly_data)
            st.download_button(
                label="📄 PDF Rapor",
                data=report_text,
                file_name=f"tuna_haftalik_rapor_{datetime.date.today()}.txt",
                mime="text/plain"
            )
    
    else:
        st.warning("🔐 Ebeveyn paneline erişim için şifre gereklidir.")

# Main app logic
def main():
    st.set_page_config(
        page_title="Alex LGS Koçum",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # PWA meta tags
    st.markdown("""
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <meta name="theme-color" content="#FFDC00">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="Alex LGS">
        <link rel="manifest" href="/manifest.json">
        <link rel="apple-touch-icon" href="/icon-192.png">
        <script>
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.register('/service-worker.js');
            }
        </script>
    </head>
    """, unsafe_allow_html=True)
    
    if not st.session_state.user_authenticated:
        authenticate_user()
    else:
        main_app()

if __name__ == "__main__":
    main()
