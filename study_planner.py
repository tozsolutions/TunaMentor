import datetime
import json
from typing import Dict, List, Any, Optional
from database import Database

class StudyPlanner:
    def __init__(self, database: Database):
        self.db = database
        self.pomodoro_duration = 25  # minutes
        self.short_break = 5  # minutes
        self.long_break = 15  # minutes
        self.sessions_before_long_break = 4
        
        # LGS exam weights for prioritizing subjects
        self.subject_weights = {
            "Matematik": 4,
            "Türkçe": 4,
            "Fen Bilimleri": 4,
            "T.C. İnkılap Tarihi": 1,
            "Din Kültürü": 1,
            "İngilizce": 1
        }
    
    def create_daily_plan(self, username: str, available_hours: float = 2.5) -> Dict[str, Any]:
        """Create optimized daily study plan"""
        
        # Get user's weak areas and progress
        weak_areas = self._analyze_weak_areas(username)
        recent_performance = self._get_recent_performance(username)
        
        # Calculate time allocation based on subject weights and weaknesses
        time_allocation = self._calculate_time_allocation(weak_areas, available_hours)
        
        # Create session schedule
        sessions = self._create_study_sessions(time_allocation)
        
        # Add Fenerbahçe integration
        fenerbahce_adjustment = self._adjust_for_fenerbahce_schedule()
        
        daily_plan = {
            "date": datetime.date.today().strftime("%Y-%m-%d"),
            "total_time_minutes": int(available_hours * 60),
            "sessions": sessions,
            "breaks": self._calculate_breaks(len(sessions)),
            "fenerbahce_info": fenerbahce_adjustment,
            "priority_subjects": self._get_priority_subjects(weak_areas),
            "goals": self._set_daily_goals(sessions),
            "motivational_message": self._get_daily_motivation()
        }
        
        return daily_plan
    
    def get_daily_plan(self, username: str) -> List[Dict[str, Any]]:
        """Get today's study plan for display"""
        plan = self.create_daily_plan(username)
        
        # Convert to display format
        display_tasks = []
        for session in plan["sessions"]:
            display_tasks.append({
                "subject": session["subject"],
                "topic": session.get("topic", "Genel Tekrar"),
                "duration": session["duration"],
                "type": session.get("type", "study"),
                "completed": self._is_session_completed(username, session),
                "priority": session.get("priority", "normal")
            })
        
        return display_tasks
    
    def _analyze_weak_areas(self, username: str) -> List[Dict[str, Any]]:
        """Analyze user's weak areas from recent performance"""
        # This would analyze the database for patterns
        # For now, return sample weak areas based on common LGS challenges
        return [
            {
                "subject": "Matematik",
                "topic": "Cebirsel İfadeler",
                "accuracy": 65,
                "importance": "high",
                "recent_mistakes": 8
            },
            {
                "subject": "Türkçe",
                "topic": "Paragrafta Anlam",
                "accuracy": 70,
                "importance": "high",
                "recent_mistakes": 6
            },
            {
                "subject": "Fen Bilimleri",
                "topic": "DNA ve Genetik Kod",
                "accuracy": 58,
                "importance": "medium",
                "recent_mistakes": 10
            }
        ]
    
    def _get_recent_performance(self, username: str) -> Dict[str, float]:
        """Get recent performance metrics"""
        return {
            "overall_accuracy": 75.5,
            "study_consistency": 85.0,
            "improvement_rate": 12.3,
            "motivation_level": 80.0
        }
    
    def _calculate_time_allocation(self, weak_areas: List[Dict], total_hours: float) -> Dict[str, int]:
        """Calculate optimal time allocation for each subject"""
        total_minutes = int(total_hours * 60)
        
        # Base allocation according to LGS weights
        base_allocation = {}
        total_weight = sum(self.subject_weights.values())
        
        for subject, weight in self.subject_weights.items():
            base_minutes = int((weight / total_weight) * total_minutes * 0.7)  # 70% for base
            base_allocation[subject] = base_minutes
        
        # Additional time for weak areas (30% of total time)
        weak_area_time = int(total_minutes * 0.3)
        weak_subjects = [area["subject"] for area in weak_areas[:3]]  # Top 3 weak areas
        
        if weak_subjects:
            additional_per_subject = weak_area_time // len(weak_subjects)
            for subject in weak_subjects:
                base_allocation[subject] += additional_per_subject
        
        return base_allocation
    
    def _create_study_sessions(self, time_allocation: Dict[str, int]) -> List[Dict[str, Any]]:
        """Create Pomodoro-based study sessions"""
        sessions = []
        session_id = 1
        
        for subject, minutes in time_allocation.items():
            if minutes >= self.pomodoro_duration:
                # Create full Pomodoro sessions
                full_sessions = minutes // self.pomodoro_duration
                remaining_minutes = minutes % self.pomodoro_duration
                
                for i in range(full_sessions):
                    sessions.append({
                        "id": session_id,
                        "subject": subject,
                        "duration": self.pomodoro_duration,
                        "type": "pomodoro",
                        "priority": self._get_subject_priority(subject),
                        "techniques": self._get_study_techniques(subject),
                        "break_after": self.short_break if session_id % self.sessions_before_long_break != 0 else self.long_break
                    })
                    session_id += 1
                
                # Add remaining time as a shorter session if significant
                if remaining_minutes >= 15:
                    sessions.append({
                        "id": session_id,
                        "subject": subject,
                        "duration": remaining_minutes,
                        "type": "review",
                        "priority": "low",
                        "techniques": ["hızlı tekrar", "soru çözme"],
                        "break_after": self.short_break
                    })
                    session_id += 1
            
            elif minutes >= 15:  # Minimum 15 minutes for a session
                sessions.append({
                    "id": session_id,
                    "subject": subject,
                    "duration": minutes,
                    "type": "mini_session",
                    "priority": "medium",
                    "techniques": ["konu özeti", "hızlı soru"],
                    "break_after": self.short_break
                })
                session_id += 1
        
        return sessions
    
    def _get_subject_priority(self, subject: str) -> str:
        """Get priority level for subject"""
        if self.subject_weights.get(subject, 1) >= 4:
            return "high"
        elif self.subject_weights.get(subject, 1) >= 2:
            return "medium"
        else:
            return "low"
    
    def _get_study_techniques(self, subject: str) -> List[str]:
        """Get recommended study techniques for each subject"""
        techniques = {
            "Matematik": ["problem çözme", "formül tekrarı", "adım adım çözüm", "hata analizi"],
            "Türkçe": ["metin analizi", "kelime çalışması", "paragraf özetleme", "soru teknikleri"],
            "Fen Bilimleri": ["kavram haritası", "deney analizi", "görsel öğrenme", "formül uygulaması"],
            "T.C. İnkılap Tarihi": ["kronoloji", "neden-sonuç", "önemli kişiler", "tarih analizi"],
            "Din Kültürü": ["kavram öğrenme", "ayet-hadis", "örneklerle pekiştirme", "değerler"],
            "İngilizce": ["kelime çalışması", "dilbilgisi", "okuma-anlama", "dinleme"]
        }
        
        return techniques.get(subject, ["genel çalışma", "soru çözme"])
    
    def _calculate_breaks(self, session_count: int) -> List[Dict[str, Any]]:
        """Calculate break schedule"""
        breaks = []
        
        for i in range(session_count - 1):  # No break after last session
            break_duration = self.long_break if (i + 1) % self.sessions_before_long_break == 0 else self.short_break
            
            breaks.append({
                "after_session": i + 1,
                "duration": break_duration,
                "type": "long" if break_duration == self.long_break else "short",
                "activity_suggestions": self._get_break_activities(break_duration)
            })
        
        return breaks
    
    def _get_break_activities(self, duration: int) -> List[str]:
        """Get suggested break activities"""
        if duration >= 15:  # Long break
            return [
                "🚶‍♂️ Kısa yürüyüş yap",
                "💧 Su iç ve hafif atıştır",
                "🧘‍♂️ Nefes egzersizi yap",
                "⚽ Fenerbahçe haberlerini kontrol et",
                "📱 Arkadaşlarınla kısa sohbet"
            ]
        else:  # Short break
            return [
                "💧 Su iç",
                "👀 Gözlerini dinlendir",
                "🤸‍♂️ Hafif germe hareketleri",
                "🎵 Sevdiğin müziği dinle",
                "🌬️ Derin nefes al"
            ]
    
    def _adjust_for_fenerbahce_schedule(self) -> Dict[str, Any]:
        """Adjust study plan for Fenerbahçe matches"""
        # This would integrate with FenerbahceIntegration
        today = datetime.date.today()
        
        # Sample adjustment - would be real data in production
        return {
            "is_match_day": False,  # This would check actual fixtures
            "match_time": None,
            "adjustment": "normal",
            "motivation": "💛💙 Fenerbahçe ruhuyla çalışma zamanı! Her soru bir gol! ⚽"
        }
    
    def _get_priority_subjects(self, weak_areas: List[Dict]) -> List[str]:
        """Get today's priority subjects"""
        priority_subjects = []
        
        # High weight subjects always priority
        for subject, weight in self.subject_weights.items():
            if weight >= 4:
                priority_subjects.append(subject)
        
        # Add weak area subjects
        for area in weak_areas[:2]:  # Top 2 weak areas
            if area["subject"] not in priority_subjects:
                priority_subjects.append(area["subject"])
        
        return priority_subjects[:3]  # Maximum 3 priority subjects
    
    def _set_daily_goals(self, sessions: List[Dict]) -> Dict[str, Any]:
        """Set achievable daily goals"""
        total_study_time = sum(session["duration"] for session in sessions)
        session_count = len(sessions)
        
        return {
            "study_time": f"{total_study_time} dakika",
            "pomodoro_sessions": session_count,
            "subjects_covered": len(set(session["subject"] for session in sessions)),
            "accuracy_target": "75% ve üzeri",
            "bonus_goal": "Tüm görevleri tamamla → Fenerbahçe maçı izleme hakkı! ⚽"
        }
    
    def _get_daily_motivation(self) -> str:
        """Get daily motivational message"""
        motivations = [
            "🎯 Bugün bir adım daha LGS hedefine yaklaş! Alex seninle!",
            "⚽ Fenerbahçe sahada nasıl mücadele ediyorsa, sen de derslerinde öyle mücadele et!",
            "💪 Her Pomodoro seansı bir antrenman! Şampiyonlar böyle doğar!",
            "🌟 Bugün öğreneceklerin yarının gücün olacak! Forza Tuna!",
            "🏆 LGS 2026 yolunda bir gün daha! Hedefine odaklan!"
        ]
        
        import random
        return random.choice(motivations)
    
    def _is_session_completed(self, username: str, session: Dict) -> bool:
        """Check if a session is completed (from database)"""
        # This would check the database for completed sessions
        # For demo, randomly return some sessions as completed
        import random
        return random.random() < 0.3  # 30% completion rate for demo
    
    def create_weekly_plan(self, username: str) -> Dict[str, Any]:
        """Create comprehensive weekly study plan"""
        weekly_plan = {
            "week_start": datetime.date.today().strftime("%Y-%m-%d"),
            "total_study_hours": 17.5,  # 2.5 hours/day average
            "daily_plans": {},
            "weekly_goals": self._set_weekly_goals(),
            "spaced_repetition": self._schedule_spaced_repetition(username),
            "exam_preparation": self._schedule_exam_prep(),
            "fenerbahce_integration": self._plan_fenerbahce_week()
        }
        
        # Generate daily plans for the week
        for i in range(7):
            date = datetime.date.today() + datetime.timedelta(days=i)
            day_name = date.strftime("%A")
            
            # Adjust study time for weekends
            study_hours = 3.0 if day_name in ["Saturday", "Sunday"] else 2.5
            
            daily_plan = self.create_daily_plan(username, study_hours)
            weekly_plan["daily_plans"][date.strftime("%Y-%m-%d")] = daily_plan
        
        return weekly_plan
    
    def _set_weekly_goals(self) -> Dict[str, Any]:
        """Set weekly study goals"""
        return {
            "study_hours": {"target": 17.5, "minimum": 15.0},
            "pomodoro_sessions": {"target": 42, "minimum": 36},
            "questions_solved": {"target": 100, "minimum": 80},
            "accuracy_rate": {"target": 80, "minimum": 75},
            "subjects_covered": {"target": 6, "minimum": 4},
            "future_lessons": {"target": 1, "minimum": 1}
        }
    
    def _schedule_spaced_repetition(self, username: str) -> List[Dict[str, Any]]:
        """Schedule spaced repetition sessions"""
        # This would query the spaced_repetition table
        return [
            {"subject": "Matematik", "topic": "Üslü İfadeler", "due_date": "2025-08-30"},
            {"subject": "Türkçe", "topic": "Cümle Öğeleri", "due_date": "2025-08-31"},
            {"subject": "Fen Bilimleri", "topic": "Basınç", "due_date": "2025-09-01"}
        ]
    
    def _schedule_exam_prep(self) -> Dict[str, Any]:
        """Schedule exam preparation sessions"""
        return {
            "mock_exams": [
                {"date": "2025-09-01", "type": "LGS Deneme", "duration": 180}
            ],
            "intensive_reviews": [
                {"date": "2025-08-30", "subjects": ["Matematik", "Türkçe"], "duration": 120}
            ]
        }
    
    def _plan_fenerbahce_week(self) -> Dict[str, Any]:
        """Plan week considering Fenerbahçe matches"""
        return {
            "matches_this_week": 1,
            "match_day_adjustments": "Hafif çalışma, maç sonrası motivasyon artışı",
            "motivation_theme": "Bu hafta Fenerbahçe ruhuyla çalışıyoruz! 💛💙"
        }
    
    def get_study_recommendations(self, username: str) -> List[str]:
        """Get personalized study recommendations"""
        recommendations = [
            "🎯 Matematik'te cebirsel ifadeler konusuna extra odaklan",
            "📚 Türkçe paragraf sorularında hızını artır",
            "⏰ Pomodoro tekniğiyle odaklanmayı sürdür",
            "🔄 Geçen haftaki yanlış sorularını tekrar çöz",
            "⚽ Fenerbahçe maç günü motivasyonunu kullan"
        ]
        
        return recommendations
    
    def update_plan_progress(self, username: str, session_id: int, completed: bool, performance_score: float):
        """Update progress for a specific study session"""
        # This would update the database with session completion
        # Log the completion in study_sessions table
        self.db.log_study_time(
            username=username,
            subject="Plan Update",
            duration=25 if completed else 0,
            topic=f"Session {session_id}"
        )
        
        # Update user points if session completed successfully
        if completed and performance_score >= 0.7:  # 70% success threshold
            from gamification import Gamification
            gamification = Gamification(self.db)
            gamification.add_points(username, 15, "study_session_completed")
