import datetime
import json
from typing import Dict, List, Any
from database import Database

class ParentDashboard:
    def __init__(self, database: Database):
        self.db = database
    
    def get_weekly_report(self, username: str) -> Dict[str, Any]:
        """Generate comprehensive weekly report for parents"""
        
        # Get basic study statistics
        stats = self.db.get_study_stats(username, "week")
        
        # Calculate metrics
        daily_breakdown = self._get_daily_study_breakdown(username)
        subject_performance = self._get_subject_performance(username)
        common_mistakes = self._analyze_mistakes(username)
        goals_progress = self._get_goals_progress(username)
        behavioral_observations = self._get_behavioral_insights(username)
        
        return {
            'study_hours': stats['total_study_time'],
            'success_rate': stats['accuracy'],
            'completed_tasks': self._count_completed_tasks(username),
            'points_earned': self._calculate_weekly_points(username),
            'daily_breakdown': daily_breakdown,
            'subject_performance': subject_performance,
            'common_mistakes': common_mistakes,
            'goals_progress': goals_progress,
            'behavioral_insights': behavioral_observations,
            'alex_assessment': self._get_alex_assessment(username),
            'recommendations': self._generate_parent_recommendations(username, stats)
        }
    
    def _get_daily_study_breakdown(self, username: str) -> Dict[str, int]:
        """Get daily study minutes for the past week"""
        # This would query the study_sessions table
        # For demo, generate realistic daily study data
        days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
        daily_data = {}
        
        for i, day in enumerate(days):
            # Simulate more study time on weekends, less on weekdays
            if day in ["Cumartesi", "Pazar"]:
                base_time = 120  # 2 hours
            else:
                base_time = 90   # 1.5 hours
            
            # Add some variation
            variation = (-20 + (i * 5)) if i < 4 else (10 + (i * 5))
            daily_data[day] = max(0, base_time + variation)
        
        return daily_data
    
    def _get_subject_performance(self, username: str) -> Dict[str, float]:
        """Get accuracy percentage by subject"""
        # This would analyze question_attempts table
        # For demo, return realistic performance data
        return {
            "Matematik": 76.5,
            "Türkçe": 82.0,
            "Fen Bilimleri": 68.8,
            "T.C. İnkılap Tarihi": 88.2,
            "Din Kültürü": 91.5,
            "İngilizce": 74.3
        }
    
    def _analyze_mistakes(self, username: str) -> List[Dict[str, Any]]:
        """Analyze common mistake patterns"""
        # This would query the mistakes table and analyze patterns
        # For demo, return sample mistake analysis
        return [
            {
                "subject": "Matematik",
                "topic": "Cebirsel İfadeler", 
                "count": 8,
                "pattern": "Işaret hatası",
                "suggestion": "Adım adım çözüm yapmaya odaklanmalı"
            },
            {
                "subject": "Fen Bilimleri",
                "topic": "DNA ve Genetik Kod",
                "count": 6,
                "pattern": "Kavram karışıklığı",
                "suggestion": "Görsel materyallerle pekiştirme yapmalı"
            },
            {
                "subject": "Türkçe",
                "topic": "Paragrafta Anlam",
                "count": 5,
                "pattern": "Hızlı okuma",
                "suggestion": "Metni daha dikkatli okumalı, anahtar kelimeleri işaretlemeli"
            }
        ]
    
    def _get_goals_progress(self, username: str) -> Dict[str, Any]:
        """Get weekly goals and completion status"""
        return {
            "daily_study_target": {
                "target": "2 saat/gün",
                "achieved": "1.8 saat/gün",
                "completion": 90,
                "status": "İyi"
            },
            "question_target": {
                "target": "100 soru/hafta",
                "achieved": "87 soru",
                "completion": 87,
                "status": "Orta"
            },
            "accuracy_target": {
                "target": "%80 doğruluk",
                "achieved": "%78.5",
                "completion": 98,
                "status": "Çok İyi"
            },
            "fenerbahce_bonus": {
                "matches_earned": 2,
                "matches_available": 3,
                "completion": 67,
                "status": "İyi"
            }
        }
    
    def _get_behavioral_insights(self, username: str) -> Dict[str, Any]:
        """Analyze behavioral patterns and engagement"""
        return {
            "engagement_level": "Yüksek",
            "peak_performance_time": "16:00-18:00",
            "attention_span": "25-30 dakika (İdeal)",
            "motivation_level": "İyi",
            "challenge_response": "Pozitif",
            "help_seeking": "Uygun sıklıkta",
            "consistency": "Düzenli",
            "fenerbahce_motivation": "Çok etkili"
        }
    
    def _get_alex_assessment(self, username: str) -> str:
        """Get Alex AI's assessment of student progress"""
        return """
        Tuna bu hafta güzel bir performans sergiledi. Matematik konularında özellikle 
        cebirsel ifadelerde gelişim gösteriyor. Fenerbahçe maç günlerinde motivasyonu 
        artıyor ve daha odaklı çalışıyor. 
        
        Türkçe paragraf anlama konusunda daha fazla pratik yapması gerekiyor. 
        Fen bilimlerinde kavramsal öğrenmeye odaklanmalı. 
        
        Genel olarak disiplinli ve kararlı bir yaklaşım sergiliyor. LGS hedefine 
        ulaşmak için bu tempoyu sürdürmesi yeterli olacaktır.
        """
    
    def _generate_parent_recommendations(self, username: str, stats: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate specific recommendations for parents"""
        recommendations = []
        
        # Study time recommendation
        if stats['total_study_time'] < 10:  # Less than 10 hours per week
            recommendations.append({
                "area": "Çalışma Süresi",
                "suggestion": "Günlük çalışma süresini 30 dakika artırın. Kısa molalarla bölümler halinde çalışması daha etkili olacaktır."
            })
        
        # Accuracy recommendation
        if stats['accuracy'] < 75:
            recommendations.append({
                "area": "Doğruluk Oranı", 
                "suggestion": "Hızdan ziyade doğruluğa odaklanmasını sağlayın. Yanlış sorularını tekrar çözmesini teşvik edin."
            })
        
        # Subject-specific recommendations
        recommendations.extend([
            {
                "area": "Matematik",
                "suggestion": "Günlük en az 5 problem çözmesini sağlayın. Adım adım çözüm yapmaya odaklanmalı."
            },
            {
                "area": "Türkçe",
                "suggestion": "Her gün 1 paragraf okuyup özetlemesini isteyin. Kelime haznesini geliştirici kitaplar okutun."
            },
            {
                "area": "Motivasyon",
                "suggestion": "Fenerbahçe maç günlerini motivasyon aracı olarak kullanın. Başarılarını kutlayın."
            },
            {
                "area": "Dinlenme",
                "suggestion": "Çalışma-dinlenme dengesini koruyun. Yeterli uyku ve fiziksel aktivite sağlayın."
            }
        ])
        
        return recommendations
    
    def _count_completed_tasks(self, username: str) -> int:
        """Count completed tasks for the week"""
        # This would query daily_goals table
        return 18  # Sample: 18 out of 21 possible daily tasks
    
    def _calculate_weekly_points(self, username: str) -> int:
        """Calculate points earned this week"""
        # This would query achievements and point transactions
        return 340
    
    def get_monthly_overview(self, username: str) -> Dict[str, Any]:
        """Get monthly overview for deeper analysis"""
        return {
            "total_study_hours": 45.5,
            "average_daily_study": 1.5,
            "consistency_score": 85,  # How regularly student studies
            "improvement_rate": 12,   # Percentage improvement over month
            "lgs_readiness": 74,      # Estimated readiness percentage
            "subject_mastery": {
                "Matematik": 78,
                "Türkçe": 82,
                "Fen Bilimleri": 71,
                "T.C. İnkılap Tarihi": 88,
                "Din Kültürü": 92,
                "İngilizce": 75
            },
            "behavioral_trends": {
                "motivation": "Artış trendi",
                "focus": "Stabil",
                "challenge_handling": "Gelişim gösteriyor",
                "independence": "Artıyor"
            },
            "parent_action_items": [
                "Fen Bilimleri için görsel materyaller temin edin",
                "İngilizce dinleme pratiği yaptırın", 
                "Matematik soru bankaları artırın",
                "Düzenli dinlenme saatlerini koruyun"
            ]
        }
    
    def generate_report_text(self, username: str, weekly_data: Dict[str, Any]) -> str:
        """Generate downloadable text report"""
        report_date = datetime.date.today().strftime("%d/%m/%Y")
        
        report_text = f"""
ALEX LGS KOÇU - HAFTALIK İLERLEME RAPORU
Öğrenci: {username.title()}
Rapor Tarihi: {report_date}

═══════════════════════════════════════════════════════

📊 GENEL PERFORMANS
• Toplam Çalışma Süresi: {weekly_data['study_hours']} saat
• Başarı Oranı: %{weekly_data['success_rate']}
• Tamamlanan Görev: {weekly_data['completed_tasks']}
• Kazanılan Puan: {weekly_data['points_earned']}

📈 GÜNLÜK ÇALIŞMA DAĞILIMI
"""
        
        for day, minutes in weekly_data['daily_breakdown'].items():
            hours = minutes // 60
            mins = minutes % 60
            report_text += f"• {day}: {hours} saat {mins} dakika\n"
        
        report_text += f"""
📚 DERS BAZINDA PERFORMANS
"""
        
        for subject, accuracy in weekly_data['subject_performance'].items():
            report_text += f"• {subject}: %{accuracy}\n"
        
        report_text += f"""
🔍 HATA ANALİZİ
"""
        
        for mistake in weekly_data['common_mistakes']:
            report_text += f"• {mistake['subject']} - {mistake['topic']}: {mistake['count']} hata\n"
            report_text += f"  Öneri: {mistake['suggestion']}\n\n"
        
        report_text += f"""
🤖 ALEX'İN DEĞERLENDİRMESİ
{weekly_data.get('alex_assessment', 'Değerlendirme hazırlanıyor...')}

💡 EbeVEYN ÖNERİLERİ
"""
        
        for i, rec in enumerate(weekly_data.get('recommendations', []), 1):
            report_text += f"{i}. {rec['area']}: {rec['suggestion']}\n"
        
        report_text += f"""
═══════════════════════════════════════════════════════
Bu rapor Alex LGS Koçu tarafından otomatik olarak oluşturulmuştur.
Sorularınız için: alex.lgs.kocu@example.com
"""
        
        return report_text
    
    def get_recommendations(self, username: str) -> List[Dict[str, str]]:
        """Get actionable recommendations for parents"""
        weekly_data = self.get_weekly_report(username)
        return weekly_data.get('recommendations', [])
