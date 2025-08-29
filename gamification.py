import random
import datetime
from typing import Dict, List, Any
from database import Database

class Gamification:
    def __init__(self, database: Database):
        self.db = database
        self.point_values = {
            'correct_answer': 10,
            'study_session': 5,
            'daily_goal': 50,
            'weekly_goal': 200,
            'streak_bonus': 25,
            'future_lesson': 20
        }
        
        self.achievement_definitions = [
            {"id": "first_steps", "name": "İlk Adımlar", "description": "İlk soruyu çözdün!", "points": 25},
            {"id": "math_lover", "name": "Matematik Aşığı", "description": "Matematik'te 100 puan kazandın!", "points": 50},
            {"id": "fenerbahce_fan", "name": "Fenerbahçe Ruhlu", "description": "Maç günü çalışmayı unutmadın!", "points": 75},
            {"id": "week_warrior", "name": "Hafta Şampiyonu", "description": "Haftalık hedefini tamamladın!", "points": 100},
            {"id": "streak_master", "name": "Seri Ustası", "description": "7 gün üst üste çalıştın!", "points": 150},
            {"id": "lgs_ready", "name": "LGS'ye Hazır", "description": "1000 puan kazandın!", "points": 200}
        ]
    
    def add_points(self, username: str, points: int, reason: str = "") -> int:
        """Add points to user and return total points"""
        self.db.update_user_points(username, points)
        
        # Check for achievements
        self._check_achievements(username)
        
        return self.db.get_user_points(username)
    
    def spend_points(self, username: str, points: int) -> bool:
        """Spend points if user has enough"""
        current_points = self.db.get_user_points(username)
        
        if current_points >= points:
            self.db.update_user_points(username, -points)
            return True
        return False
    
    def get_user_stats(self, username: str) -> Dict[str, Any]:
        """Get comprehensive user statistics"""
        total_points = self.db.get_user_points(username)
        level = self._calculate_level(total_points)
        streak = self._calculate_streak(username)
        
        return {
            'total_points': total_points,
            'level': level,
            'streak': streak,
            'next_level_points': (level * 100) - (total_points % 100)
        }
    
    def _calculate_level(self, total_points: int) -> int:
        """Calculate user level based on total points"""
        return max(1, total_points // 100)
    
    def _calculate_streak(self, username: str) -> int:
        """Calculate current study streak"""
        # This would check consecutive days of study from database
        # For demo, return a sample value
        return random.randint(0, 10)
    
    def get_daily_challenges(self, username: str) -> List[Dict[str, Any]]:
        """Generate daily challenges for user"""
        today = datetime.date.today()
        
        # Sample challenges - in real app these would be personalized
        base_challenges = [
            {
                "id": "daily_math",
                "description": "Matematik'te 5 soru çöz",
                "reward": 25,
                "progress": 0,
                "target": 5,
                "completed": False
            },
            {
                "id": "daily_study",
                "description": "30 dakika çalış",
                "reward": 30,
                "progress": 0,
                "target": 30,
                "completed": False
            },
            {
                "id": "daily_topic",
                "description": "Yeni bir konu öğren",
                "reward": 20,
                "progress": 0,
                "target": 1,
                "completed": False
            },
            {
                "id": "daily_review",
                "description": "Eski konuları tekrar et",
                "reward": 15,
                "progress": 0,
                "target": 1,
                "completed": False
            }
        ]
        
        # Add Fenerbahçe special challenge if it's match day
        if self._is_match_day():
            base_challenges.append({
                "id": "match_day",
                "description": "Maç öncesi tüm görevleri tamamla!",
                "reward": 100,
                "progress": 0,
                "target": 4,
                "completed": False
            })
        
        return base_challenges
    
    def _is_match_day(self) -> bool:
        """Check if today is a Fenerbahçe match day"""
        # This would check against actual fixture data
        # For demo, randomly return True ~20% of the time
        return random.random() < 0.2
    
    def get_achievements(self, username: str) -> List[Dict[str, Any]]:
        """Get user's earned achievements"""
        # This would fetch from database
        # For demo, return some sample achievements
        sample_achievements = [
            {"name": "İlk Adımlar", "date": "2025-08-20", "points": 25},
            {"name": "Matematik Aşığı", "date": "2025-08-25", "points": 50},
            {"name": "Fenerbahçe Ruhlu", "date": "2025-08-28", "points": 75}
        ]
        return sample_achievements
    
    def _check_achievements(self, username: str):
        """Check and award new achievements"""
        total_points = self.db.get_user_points(username)
        
        # Simple achievement check - in real app this would be more sophisticated
        if total_points >= 1000:
            # Award "LGS Ready" achievement if not already earned
            pass
    
    def can_watch_full_match(self, username: str) -> bool:
        """Check if user completed enough tasks to watch full match"""
        # Check today's completed challenges
        daily_progress = self._get_daily_progress(username)
        completed_challenges = sum(1 for challenge in daily_progress if challenge['completed'])
        
        # Need to complete at least 3 out of 4 daily challenges
        return completed_challenges >= 3
    
    def get_remaining_tasks(self, username: str) -> int:
        """Get number of tasks remaining for match watching privilege"""
        daily_progress = self._get_daily_progress(username)
        completed_challenges = sum(1 for challenge in daily_progress if challenge['completed'])
        
        return max(0, 3 - completed_challenges)
    
    def _get_daily_progress(self, username: str) -> List[Dict[str, Any]]:
        """Get today's challenge progress"""
        # This would fetch real progress from database
        # For demo, return sample progress
        return [
            {"completed": True},
            {"completed": True},
            {"completed": False},
            {"completed": False}
        ]
    
    def get_leaderboard(self, period: str = "week") -> List[Dict[str, Any]]:
        """Get leaderboard for specified period"""
        # For demo purposes - in real app this would query database
        sample_leaderboard = [
            {"rank": 1, "username": "Tuna", "points": 450, "streak": 7},
            {"rank": 2, "username": "Demo User 1", "points": 380, "streak": 5},
            {"rank": 3, "username": "Demo User 2", "points": 320, "streak": 3}
        ]
        return sample_leaderboard
    
    def get_weekly_goals(self, username: str) -> Dict[str, Any]:
        """Get weekly goals and progress"""
        return {
            "study_hours": {"target": 15, "current": 8.5, "completed": False},
            "questions_solved": {"target": 100, "current": 67, "completed": False}, 
            "topics_learned": {"target": 5, "current": 3, "completed": False},
            "accuracy_rate": {"target": 80, "current": 75, "completed": False}
        }
    
    def award_special_bonus(self, username: str, bonus_type: str, points: int):
        """Award special bonus points"""
        bonus_messages = {
            "match_day": f"⚽ Maç günü bonusu! +{points} puan!",
            "perfect_score": f"🎯 Mükemmel skor! +{points} puan!",
            "streak_bonus": f"🔥 {points} günlük seri bonusu!",
            "subject_master": f"📚 Konu uzmanı bonusu! +{points} puan!"
        }
        
        self.add_points(username, points, bonus_messages.get(bonus_type, "Özel bonus!"))
