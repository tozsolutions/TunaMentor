
#!/usr/bin/env python3
"""
Alex LGS Koçu Final Kontrol Sistemi
Tüm sistemlerin çalıştığını doğrular
"""

import os
import sys
import importlib
import sqlite3
from pathlib import Path

def check_all_systems():
    """Tüm sistemleri kontrol et"""
    print("🔍 Alex LGS Koçu Final Kontrol Başlıyor...\n")
    
    checks = []
    
    # 1. Dosya Kontrolleri
    print("📁 Dosya Kontrolleri:")
    required_files = [
        "app.py", "alex_ai.py", "database.py", "curriculum.py",
        "gamification.py", "memory_techniques.py", "voice_synthesis.py",
        "progress_tracker.py", "parent_dashboard.py", "study_planner.py",
        "fenerbahce_integration.py", "utils.py", "manifest.json"
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
            checks.append(True)
        else:
            print(f"❌ {file} EKSIK!")
            checks.append(False)
    
    # 2. Python Modül Kontrolleri
    print("\n🐍 Python Modül Kontrolleri:")
    try:
        import streamlit
        print("✅ Streamlit")
        checks.append(True)
    except ImportError:
        print("❌ Streamlit EKSIK!")
        checks.append(False)
    
    try:
        import openai
        print("✅ OpenAI")
        checks.append(True)
    except ImportError:
        print("❌ OpenAI EKSIK!")
        checks.append(False)
    
    try:
        import pandas
        print("✅ Pandas")
        checks.append(True)
    except ImportError:
        print("❌ Pandas EKSIK!")
        checks.append(False)
    
    # 3. Veritabanı Kontrolü
    print("\n🗄️ Veritabanı Kontrolü:")
    try:
        if os.path.exists("alex_lgs.db"):
            conn = sqlite3.connect("alex_lgs.db")
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            conn.close()
            print(f"✅ Veritabanı OK - {len(tables)} tablo")
            checks.append(True)
        else:
            print("⚠️ Veritabanı yok, ilk çalıştırmada oluşturulacak")
            checks.append(True)
    except Exception as e:
        print(f"❌ Veritabanı hatası: {e}")
        checks.append(False)
    
    # 4. Özellik Kontrolleri
    print("\n🎯 Özellik Kontrolleri:")
    
    # Alex AI kontrolü
    try:
        from alex_ai import AlexAI
        alex = AlexAI()
        if hasattr(alex, 'learning_techniques') and 'mind_mapping' in alex.learning_techniques:
            print("✅ Alex AI - Gelişmiş öğrenme teknikleri")
            checks.append(True)
        else:
            print("❌ Alex AI - Öğrenme teknikleri eksik")
            checks.append(False)
    except Exception as e:
        print(f"❌ Alex AI hatası: {e}")
        checks.append(False)
    
    # Hafıza teknikleri kontrolü
    try:
        from memory_techniques import MemoryTechniques
        memory = MemoryTechniques()
        if hasattr(memory, 'create_color_coded_mind_map'):
            print("✅ Hafıza Teknikleri - Zihin haritaları")
            checks.append(True)
        else:
            print("❌ Hafıza Teknikleri - Zihin haritaları eksik")
            checks.append(False)
    except Exception as e:
        print(f"❌ Hafıza Teknikleri hatası: {e}")
        checks.append(False)
    
    # Ses sistemi kontrolü
    try:
        from voice_synthesis import VoiceSynthesis
        voice = VoiceSynthesis()
        if hasattr(voice, 'speak'):
            print("✅ Ses Sistemi")
            checks.append(True)
        else:
            print("❌ Ses Sistemi eksik")
            checks.append(False)
    except Exception as e:
        print(f"❌ Ses Sistemi hatası: {e}")
        checks.append(False)
    
    # 5. Sonuç
    print("\n" + "="*50)
    success_rate = (sum(checks) / len(checks)) * 100
    print(f"📊 Başarı Oranı: {success_rate:.1f}%")
    
    if success_rate >= 95:
        print("🎉 SİSTEM HAZIR! APK oluşturulabilir.")
        return True
    elif success_rate >= 80:
        print("⚠️ Sistem çoğunlukla hazır, küçük sorunlar var.")
        return False
    else:
        print("❌ Sistem henüz hazır değil, eksikler giderilmeli.")
        return False

if __name__ == "__main__":
    if check_all_systems():
        print("\n🚀 APK oluşturmak için 'python build_apk.py' komutunu çalıştırabilirsiniz.")
    else:
        print("\n🔧 Lütfen eksikleri giderdikten sonra tekrar kontrol edin.")
