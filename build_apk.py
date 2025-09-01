
#!/usr/bin/env python3
"""
Alex LGS Koçu APK Builder
Bu script web uygulamasını APK formatına dönüştürür
"""

import os
import subprocess
import shutil
from pathlib import Path

def build_apk():
    print("🚀 Alex LGS Koçu APK Build Başlıyor...")
    
    # Build directory oluştur
    build_dir = Path("build_apk")
    if build_dir.exists():
        shutil.rmtree(build_dir)
    build_dir.mkdir()
    
    print("📦 Gerekli dosyalar kopyalanıyor...")
    
    # Ana dosyaları kopyala
    files_to_copy = [
        "app.py", "alex_ai.py", "database.py", "curriculum.py",
        "gamification.py", "memory_techniques.py", "voice_synthesis.py",
        "manifest.json", "service-worker.js"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, build_dir / file)
    
    # Cordova projesi oluştur
    cordova_dir = build_dir / "cordova_app"
    cordova_dir.mkdir()
    
    print("📱 Cordova projesi oluşturuluyor...")
    
    # config.xml oluştur
    config_xml = cordova_dir / "config.xml"
    config_xml.write_text("""<?xml version='1.0' encoding='utf-8'?>
<widget id="com.tuna.alexlgs" version="1.0.0" xmlns="http://www.w3.org/ns/widgets">
    <name>Alex LGS Koçu</name>
    <description>Tuna için özel LGS 2026 hazırlık sistemi</description>
    <author email="tuna@alexlgs.com" href="">Alex AI Team</author>
    <content src="index.html" />
    <access origin="*" />
    <allow-intent href="http://*/*" />
    <allow-intent href="https://*/*" />
    <platform name="android">
        <allow-intent href="market:*" />
        <icon density="ldpi" src="res/icon/android/ldpi.png" />
        <icon density="mdpi" src="res/icon/android/mdpi.png" />
        <icon density="hdpi" src="res/icon/android/hdpi.png" />
        <icon density="xhdpi" src="res/icon/android/xhdpi.png" />
        <icon density="xxhdpi" src="res/icon/android/xxhdpi.png" />
        <icon density="xxxhdpi" src="res/icon/android/xxxhdpi.png" />
    </platform>
    <plugin name="cordova-plugin-statusbar" spec="^3.0.0" />
    <plugin name="cordova-plugin-device" spec="^2.0.3" />
    <plugin name="cordova-plugin-splashscreen" spec="^6.0.0" />
</widget>""")
    
    print("✅ APK build dosyaları hazırlandı!")
    print(f"📁 Build dizini: {build_dir.absolute()}")
    print("🔧 APK oluşturmak için Android Studio veya Cordova CLI kullanabilirsiniz.")
    
    return True

if __name__ == "__main__":
    build_apk()
