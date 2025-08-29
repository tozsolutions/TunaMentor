import datetime
import pandas as pd
from typing import Dict, List, Any
from database import Database

class ProgressTracker:
    def __init__(self, database: Database):
        self.db = database
        self.learning_algorithms = {
            "spaced_repetition": self._calculate_spaced_intervals,
            "forgetting_curve": self._analyze_forgetting_pattern,
            "optimal_difficulty": self._find_optimal_difficulty,
            "learning_velocity": self._calculate_learning_speed
        }

    def get_user_stats(self, username: str) -> Dict[str, Any]:
        """Get comprehensive user statistics"""
        stats = self.db.get_study_stats(username, "all")

        # Calculate additional metrics
        total_points = self.db.get_user_points(username)
        level = max(1, total_points // 100)

        return {
            'total_points': total_points,
            'level': level,
            'streak': self._calculate_streak(username),
            'total_study_hours': stats['total_study_time'],
            'questions_solved': stats['questions_solved'],
            'accuracy': stats['accuracy']
        }

    def get_progress_data(self, username: str, period: str) -> Dict[str, Any]:
        """Get comprehensive progress data with advanced analytics"""
        stats = self.db.get_study_stats(username, period)
        user_data = self.db.get_user_data(username) # Assuming this retrieves all relevant user data for analytics

        # Estimate LGS score based on performance
        estimated_score = self._estimate_lgs_score(username, stats)

        # Identify weak areas
        weak_areas = self._analyze_weak_areas(username)

        # Calculate subject breakdown
        subject_breakdown = self._calculate_subject_accuracy(username, period)

        # Apply learning algorithms
        spaced_repetition_intervals = self.learning_algorithms["spaced_repetition"](stats)
        forgetting_pattern_analysis = self.learning_algorithms["forgetting_curve"](user_data)
        optimal_difficulty_level = self.learning_algorithms["optimal_difficulty"](stats) # Assuming stats contains performance_history equivalent
        learning_speed_data = self.learning_algorithms["learning_velocity"](user_data.get("recent_sessions", [])) # Assuming user_data contains recent_sessions


        return {
            'total_study_time': stats['total_study_time'],
            'questions_solved': stats['questions_solved'],
            'accuracy': stats['accuracy'],
            'points_earned': self._calculate_points_earned(username, period),
            'estimated_lgs_score': estimated_score,
            'weak_areas': weak_areas,
            'subject_breakdown': subject_breakdown,
            'daily_breakdown': self._get_daily_breakdown(username, period),
            'progress_trend': self._calculate_progress_trend(username),
            'learning_analytics': {
                "spaced_repetition_intervals": spaced_repetition_intervals,
                "forgetting_pattern_analysis": forgetting_pattern_analysis,
                "optimal_difficulty_level": optimal_difficulty_level,
                "learning_speed_data": learning_speed_data
            }
        }

    def _calculate_streak(self, username: str) -> int:
        """Calculate current study streak in days"""
        # This would query the database for consecutive study days
        # For demo, return a reasonable value
        return 5

    def _estimate_lgs_score(self, username: str, stats: Dict[str, Any]) -> int:
        """Estimate LGS score based on current performance"""
        base_score = 300  # Minimum LGS score

        # Factors affecting score estimation
        accuracy_factor = stats['accuracy'] / 100  # 0-1
        study_time_factor = min(1.0, stats['total_study_time'] / 100)  # Normalize study time
        question_factor = min(1.0, stats['questions_solved'] / 1000)  # Normalize questions

        # Weight the factors
        performance_score = (
            accuracy_factor * 0.5 +
            study_time_factor * 0.3 +
            question_factor * 0.2
        )

        # Calculate estimated score (300-500 range)
        estimated_score = base_score + (performance_score * 200)

        return min(500, max(300, int(estimated_score)))

    def _analyze_weak_areas(self, username: str) -> List[Dict[str, Any]]:
        """Analyze areas where student needs improvement"""
        # This would analyze mistake patterns from database
        # For demo, return sample weak areas
        sample_weak_areas = [
            {
                "subject": "Matematik",
                "topic": "Cebirsel İfadeler",
                "accuracy": 65,
                "mistake_count": 8,
                "suggestion": "Daha fazla pratik yap ve temel kuralları tekrar et"
            },
            {
                "subject": "Türkçe", 
                "topic": "Paragrafta Anlam",
                "accuracy": 70,
                "mistake_count": 6,
                "suggestion": "Uzun metinleri parçalara bölerek oku"
            },
            {
                "subject": "Fen Bilimleri",
                "topic": "DNA ve Genetik Kod",
                "accuracy": 58,
                "mistake_count": 10,
                "suggestion": "Görsel materyallerle konuyu pekiştir"
            }
        ]

        return sample_weak_areas

    def _calculate_subject_accuracy(self, username: str, period: str) -> Dict[str, float]:
        """Calculate accuracy percentage for each subject"""
        # This would query question_attempts table
        # For demo, return sample data
        return {
            "Matematik": 78.5,
            "Türkçe": 82.0,
            "Fen Bilimleri": 71.2,
            "T.C. İnkılap Tarihi": 85.5,
            "Din Kültürü": 88.0,
            "İngilizce": 76.8
        }

    def _calculate_points_earned(self, username: str, period: str) -> int:
        """Calculate points earned in specified period"""
        # This would sum points from achievements table
        # For demo, return reasonable value based on period
        if period == "bu_hafta":
            return 245
        elif period == "bu_ay":
            return 980
        else:
            return 2450

    def _get_daily_breakdown(self, username: str, period: str) -> Dict[str, int]:
        """Get daily study time breakdown"""
        # Generate sample daily data for the last 7 days
        daily_data = {}
        for i in range(7):
            date = datetime.date.today() - datetime.timedelta(days=i)
            day_name = date.strftime("%A")
            # Convert to Turkish day names
            day_turkish = {
                "Monday": "Pazartesi",
                "Tuesday": "Salı", 
                "Wednesday": "Çarşamba",
                "Thursday": "Perşembe",
                "Friday": "Cuma",
                "Saturday": "Cumartesi",
                "Sunday": "Pazar"
            }.get(day_name, day_name)

            # Sample study minutes (higher on weekends)
            if day_name in ["Saturday", "Sunday"]:
                daily_data[day_turkish] = 90 + (i * 10)
            else:
                daily_data[day_turkish] = 60 + (i * 5)

        return daily_data

    def _calculate_progress_trend(self, username: str) -> str:
        """Calculate overall progress trend"""
        # This would analyze historical data to determine trend
        # For demo, return positive trend
        return "improving"  # "improving", "stable", "declining"

    def get_weekly_summary(self, username: str) -> Dict[str, Any]:
        """Get comprehensive weekly summary"""
        return {
            "study_hours": 12.5,
            "questions_solved": 85,
            "accuracy_improvement": 3.2,  # percentage points
            "goals_completed": 4,
            "total_goals": 5,
            "points_earned": 425,
            "new_achievements": 2,
            "streak_days": 6,
            "favorite_subject": "Matematik",
            "needs_attention": ["Fen Bilimleri", "İngilizce"]
        }

    def get_monthly_report(self, username: str) -> Dict[str, Any]:
        """Generate comprehensive monthly report"""
        return {
            "total_study_hours": 48.0,
            "avg_daily_study": 1.6,
            "questions_solved": 340,
            "overall_accuracy": 76.8,
            "improvement_rate": 8.5,  # percentage
            "lgs_readiness": 72,  # percentage
            "strong_subjects": ["T.C. İnkılap Tarihi", "Din Kültürü"],
            "improvement_needed": ["Fen Bilimleri", "İngilizce"],
            "achievements_earned": 5,
            "fenerbahce_matches_watched": 3,
            "future_lessons_completed": 4,
            "parent_satisfaction": 85  # percentage
        }

    def get_lgs_prediction(self, username: str) -> Dict[str, Any]:
        """Predict LGS performance based on current progress"""
        current_stats = self.get_user_stats(username)
        estimated_score = self._estimate_lgs_score(username, current_stats)

        # Calculate ranking estimation
        if estimated_score >= 475:
            ranking_estimate = "Top 500"
            success_probability = 95
        elif estimated_score >= 450:
            ranking_estimate = "Top 1000"
            success_probability = 85
        elif estimated_score >= 425:
            ranking_estimate = "Top 2000"
            success_probability = 75
        else:
            ranking_estimate = "Top 5000"
            success_probability = 60

        return {
            "estimated_score": estimated_score,
            "target_score": 475,
            "score_gap": max(0, 475 - estimated_score),
            "ranking_estimate": ranking_estimate,
            "success_probability": success_probability,
            "recommendation": self._get_score_improvement_plan(estimated_score),
            "time_to_target": self._calculate_time_to_target(estimated_score)
        }

    def _get_score_improvement_plan(self, current_score: int) -> str:
        """Get specific improvement plan based on current score"""
        if current_score >= 450:
            return "Mükemmel! Son rötuşlar için zayıf konuları tekrar et."
        elif current_score >= 400:
            return "İyi durumdasın! Matematik ve Türkçe'ye daha fazla odaklan."
        else:
            return "Daha çok çalışma gerekiyor. Günlük çalışma süresini artır ve Alex'ten yardım al!"

    def _calculate_time_to_target(self, current_score: int) -> str:
        """Calculate estimated time to reach target score"""
        score_gap = max(0, 475 - current_score)

        if score_gap == 0:
            return "Hedefe ulaştın! 🎯"
        elif score_gap <= 25:
            return "2-3 hafta yoğun çalışma"
        elif score_gap <= 50:
            return "1-2 ay düzenli çalışma"
        else:
            return "3-4 ay sistemli çalışma"

    def _calculate_spaced_intervals(self, performance_data):
        """Performansa göre aralıklı tekrar hesapla"""
        if performance_data['accuracy'] >= 90:
            return [1, 4, 10, 20, 40, 90]  # Daha uzun aralıklar
        elif performance_data['accuracy'] >= 70:
            return [1, 2, 5, 10, 20, 45]  # Orta aralıklar  
        else:
            return [1, 1, 2, 4, 8, 15]   # Kısa aralıklar

    def _analyze_forgetting_pattern(self, user_data):
        """Unutma eğrisi analizi"""
        # Ebbinghaus unutma eğrisine göre analiz
        retention_rates = []
        if 'recent_sessions' in user_data:
            for session in user_data['recent_sessions']:
                time_diff = (datetime.datetime.now() - session['date']).days
                predicted_retention = 100 * (0.6 ** (time_diff / 7))  # 7 günde %60 unutma
                actual_retention = session['accuracy']
                retention_rates.append({
                    'predicted': predicted_retention,
                    'actual': actual_retention,
                    'difference': actual_retention - predicted_retention
                })
        return retention_rates

    def _find_optimal_difficulty(self, performance_history):
        """Optimal zorluk seviyesi bul"""
        # Vygotsky'nin Yakınsal Gelişim Alanı teorisine göre
        # For simplicity, using accuracy from stats as a proxy for current_level
        current_level = performance_history.get('accuracy', 0) 

        if current_level >= 85:
            return "challenge_mode"  # Zorluğu artır
        elif current_level >= 65:
            return "optimal_zone"    # Mevcut seviyeyi koru
        else:
            return "support_mode"    # Daha kolay sorular

    def _calculate_learning_speed(self, user_sessions):
        """Öğrenme hızı hesapla"""
        if len(user_sessions) < 3:
            return {"speed": "insufficient_data"}

        accuracy_improvements = []
        for i in range(1, len(user_sessions)):
            improvement = user_sessions[i]['accuracy'] - user_sessions[i-1]['accuracy']
            accuracy_improvements.append(improvement)

        avg_improvement = sum(accuracy_improvements) / len(accuracy_improvements)

        if avg_improvement > 5:
            return {"speed": "fast", "rate": avg_improvement}
        elif avg_improvement > 2:
            return {"speed": "normal", "rate": avg_improvement}
        else:
            return {"speed": "slow", "rate": avg_improvement, "suggestion": "review_methods"}