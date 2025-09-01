import datetime
import hashlib
import json
import re
from typing import Any, Dict, List, Optional, Union
import streamlit as st

class DateUtils:
    """Utility functions for date and time operations"""
    
    @staticmethod
    def get_turkish_date(date_obj: datetime.date = None) -> str:
        """Get date in Turkish format"""
        if date_obj is None:
            date_obj = datetime.date.today()
        
        turkish_months = {
            1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan",
            5: "Mayıs", 6: "Haziran", 7: "Temmuz", 8: "Ağustos",
            9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık"
        }
        
        turkish_days = {
            0: "Pazartesi", 1: "Salı", 2: "Çarşamba", 3: "Perşembe",
            4: "Cuma", 5: "Cumartesi", 6: "Pazar"
        }
        
        day_name = turkish_days[date_obj.weekday()]
        month_name = turkish_months[date_obj.month]
        
        return f"{day_name}, {date_obj.day} {month_name} {date_obj.year}"
    
    @staticmethod
    def get_study_week_info() -> Dict[str, Any]:
        """Get current study week information"""
        today = datetime.date.today()
        week_start = today - datetime.timedelta(days=today.weekday())
        week_end = week_start + datetime.timedelta(days=6)
        
        # Calculate LGS countdown
        lgs_date = datetime.date(2026, 6, 15)  # Estimated LGS date
        days_to_lgs = (lgs_date - today).days
        
        return {
            "week_number": today.isocalendar()[1],
            "week_start": week_start,
            "week_end": week_end,
            "days_to_lgs": days_to_lgs,
            "is_weekend": today.weekday() >= 5,
            "turkish_date": DateUtils.get_turkish_date(today)
        }

class TextUtils:
    """Utility functions for text processing"""
    
    @staticmethod
    def clean_text_for_display(text: str) -> str:
        """Clean text for better display"""
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Fix Turkish character encoding issues
        replacements = {
            'Ä±': 'ı', 'Ä°': 'İ', 'Å': 'ş', 'Åž': 'ş',
            'Ã§': 'ç', 'Ã': 'ğ', 'Ã¼': 'ü', 'Ã¶': 'ö'
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return text.strip()
    
    @staticmethod
    def format_duration(minutes: int) -> str:
        """Format duration in minutes to human readable format"""
        if minutes < 60:
            return f"{minutes} dakika"
        
        hours = minutes // 60
        remaining_minutes = minutes % 60
        
        if remaining_minutes == 0:
            return f"{hours} saat"
        else:
            return f"{hours} saat {remaining_minutes} dakika"
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 100) -> str:
        """Truncate text to maximum length with ellipsis"""
        if len(text) <= max_length:
            return text
        
        return text[:max_length-3] + "..."
    
    @staticmethod
    def highlight_keywords(text: str, keywords: List[str]) -> str:
        """Highlight keywords in text with HTML"""
        for keyword in keywords:
            text = re.sub(
                f'({re.escape(keyword)})',
                r'<mark style="background-color: #FFDC00; color: #1F2A44;">\1</mark>',
                text,
                flags=re.IGNORECASE
            )
        
        return text

class MathUtils:
    """Utility functions for mathematical operations and formatting"""
    
    @staticmethod
    def calculate_percentage(part: float, total: float) -> float:
        """Calculate percentage with safety check"""
        if total == 0:
            return 0.0
        return round((part / total) * 100, 1)
    
    @staticmethod
    def calculate_average(numbers: List[float]) -> float:
        """Calculate average with safety check"""
        if not numbers:
            return 0.0
        return round(sum(numbers) / len(numbers), 1)
    
    @staticmethod
    def format_score(score: float) -> str:
        """Format LGS score for display"""
        return f"{score:.1f}"
    
    @staticmethod
    def calculate_grade(percentage: float) -> str:
        """Calculate letter grade from percentage"""
        if percentage >= 90:
            return "A+ Mükemmel"
        elif percentage >= 80:
            return "A İyi"
        elif percentage >= 70:
            return "B Orta"
        elif percentage >= 60:
            return "C Geçer"
        else:
            return "D Gelişim Gerekli"

class UIUtils:
    """Utility functions for UI components and styling"""
    
    @staticmethod
    def create_metric_card(title: str, value: str, delta: str = None, delta_color: str = "normal") -> str:
        """Create a metric card with Fenerbahçe styling"""
        delta_html = ""
        if delta:
            color = "#28a745" if delta_color == "normal" else "#dc3545" if delta_color == "inverse" else "#6c757d"
            delta_html = f'<div style="color: {color}; font-size: 14px; margin-top: 5px;">{delta}</div>'
        
        return f"""
        <div style="
            background: white;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #FFDC00;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">
            <div style="color: #6c757d; font-size: 14px; margin-bottom: 5px;">{title}</div>
            <div style="color: #1F2A44; font-size: 24px; font-weight: bold;">{value}</div>
            {delta_html}
        </div>
        """
    
    @staticmethod
    def create_progress_bar(percentage: float, color: str = "#FFDC00") -> str:
        """Create a custom progress bar"""
        return f"""
        <div style="
            width: 100%;
            background-color: #e9ecef;
            border-radius: 10px;
            overflow: hidden;
            margin: 10px 0;
        ">
            <div style="
                width: {percentage}%;
                background-color: {color};
                height: 20px;
                transition: width 0.3s ease;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #1F2A44;
                font-weight: bold;
                font-size: 12px;
            ">
                {percentage:.1f}%
            </div>
        </div>
        """
    
    @staticmethod
    def create_achievement_badge(name: str, description: str = "", earned: bool = True) -> str:
        """Create achievement badge"""
        opacity = "1.0" if earned else "0.5"
        background = "linear-gradient(45deg, #FFDC00, #1F2A44)" if earned else "#6c757d"
        
        return f"""
        <div style="
            background: {background};
            color: white;
            padding: 8px 12px;
            border-radius: 20px;
            margin: 5px;
            display: inline-block;
            opacity: {opacity};
            font-size: 12px;
            font-weight: bold;
        ">
            {'🏆' if earned else '🔒'} {name}
            {f'<br><small>{description}</small>' if description else ''}
        </div>
        """
    
    @staticmethod
    def create_fenerbahce_header(title: str) -> str:
        """Create Fenerbahçe-themed header"""
        return f"""
        <div style="
            background: linear-gradient(90deg, #FFDC00, #1F2A44);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 24px;
        ">
            {title}
            <div style="height: 5px; background: linear-gradient(90deg, #FFDC00 50%, #1F2A44 50%); margin-top: 10px;"></div>
        </div>
        """

class DataValidation:
    """Utility functions for data validation"""
    
    @staticmethod
    def validate_study_time(minutes: int) -> bool:
        """Validate study time input"""
        return 0 <= minutes <= 480  # Max 8 hours per day
    
    @staticmethod
    def validate_accuracy(percentage: float) -> bool:
        """Validate accuracy percentage"""
        return 0.0 <= percentage <= 100.0
    
    @staticmethod
    def validate_username(username: str) -> bool:
        """Validate username"""
        return len(username) >= 2 and username.isalnum()
    
    @staticmethod
    def sanitize_input(text: str) -> str:
        """Sanitize user input"""
        # Remove potentially dangerous characters
        text = re.sub(r'[<>\"\'&]', '', text)
        return text.strip()

class CacheUtils:
    """Utility functions for caching and performance"""
    
    @staticmethod
    def generate_cache_key(*args) -> str:
        """Generate cache key from arguments"""
        key_string = "_".join(str(arg) for arg in args)
        return hashlib.md5(key_string.encode()).hexdigest()[:10]
    
    @staticmethod
    def cache_with_ttl(func, ttl_seconds: int = 300):
        """Simple cache decorator with TTL"""
        cache = {}
        
        def wrapper(*args, **kwargs):
            key = CacheUtils.generate_cache_key(*args, **kwargs)
            now = datetime.datetime.now()
            
            if key in cache:
                result, timestamp = cache[key]
                if (now - timestamp).seconds < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        
        return wrapper

class NotificationUtils:
    """Utility functions for notifications and alerts"""
    
    @staticmethod
    def show_success(message: str):
        """Show success notification"""
        st.success(f"✅ {message}")
    
    @staticmethod
    def show_error(message: str):
        """Show error notification"""
        st.error(f"❌ {message}")
    
    @staticmethod
    def show_warning(message: str):
        """Show warning notification"""
        st.warning(f"⚠️ {message}")
    
    @staticmethod
    def show_info(message: str):
        """Show info notification"""
        st.info(f"ℹ️ {message}")
    
    @staticmethod
    def show_fenerbahce_celebration():
        """Show Fenerbahçe celebration"""
        st.balloons()
        st.success("🎉⚽ FORZA FENERBAHÇE! Harika iş çıkardın! 💛💙")

class ConfigUtils:
    """Utility functions for configuration and settings"""
    
    @staticmethod
    def load_config(config_path: str = "config.json") -> Dict[str, Any]:
        """Load configuration from file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "app_name": "Alex LGS Koçu",
                "version": "1.0.0",
                "theme": "fenerbahce",
                "language": "tr",
                "features": {
                    "voice_synthesis": True,
                    "fenerbahce_integration": True,
                    "gamification": True
                }
            }
    
    @staticmethod
    def get_theme_colors() -> Dict[str, str]:
        """Get Fenerbahçe theme colors"""
        return {
            "primary": "#FFDC00",      # Fenerbahçe yellow
            "secondary": "#1F2A44",    # Fenerbahçe navy
            "success": "#28a745",
            "warning": "#ffc107",
            "error": "#dc3545",
            "info": "#17a2b8",
            "light": "#f8f9fa",
            "dark": "#343a40"
        }

class ExportUtils:
    """Utility functions for data export"""
    
    @staticmethod
    def export_progress_data(data: Dict[str, Any]) -> str:
        """Export progress data to formatted text"""
        export_text = f"""
ALEX LGS KOÇU - İLERLEME RAPORU
{'='*50}
Tarih: {DateUtils.get_turkish_date()}

GENEL İSTATİSTİKLER:
- Toplam Çalışma Süresi: {data.get('total_study_time', 0)} saat
- Çözülen Soru: {data.get('questions_solved', 0)}
- Doğruluk Oranı: %{data.get('accuracy', 0)}
- Kazanılan Puan: {data.get('points_earned', 0)}

DERS BAZINDA PERFORMANS:
"""
        
        for subject, accuracy in data.get('subject_breakdown', {}).items():
            export_text += f"- {subject}: %{accuracy}\n"
        
        export_text += f"\nZAYIF ALANLAR:\n"
        
        for area in data.get('weak_areas', []):
            export_text += f"- {area['subject']} - {area['topic']}: %{area['accuracy']}\n"
        
        return export_text
    
    @staticmethod
    def create_download_button(data: str, filename: str, button_text: str = "📥 İndir"):
        """Create download button for data"""
        st.download_button(
            label=button_text,
            data=data,
            file_name=filename,
            mime="text/plain"
        )

# Global utility instances
date_utils = DateUtils()
text_utils = TextUtils()
math_utils = MathUtils()
ui_utils = UIUtils()
validation = DataValidation()
cache_utils = CacheUtils()
notifications = NotificationUtils()
config_utils = ConfigUtils()
export_utils = ExportUtils()
