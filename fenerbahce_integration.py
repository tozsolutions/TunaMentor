import datetime
import random
from typing import Dict, List, Any

class FenerbahceIntegration:
    def __init__(self):
        # Sample 2025-2026 season fixture data
        self.fixtures = self._generate_sample_fixtures()
        self.motivational_quotes = [
            "Futbolda en güzel zafer, hak edilen zaferdir! Sen de çalışarak hak et! ⚽",
            "Fenerbahçe ruhu demek, asla vazgeçmemek demek! LGS'de de vazgeçme! 💛💙",
            "Her maçtan önce hazırlık, her sınavdan önce çalışma! Forza FB! 🏆",
            "Takım oyunu önemli! Sen de derslerinle takım halinde çalış! ⚽",
            "Kadıköy'ün coşkusu, senin çalışma enerjin olsun! 🔥"
        ]
    
    def _generate_sample_fixtures(self) -> List[Dict[str, Any]]:
        """Generate sample Fenerbahçe fixtures for 2025-2026 season"""
        opponents = [
            "Galatasaray", "Beşiktaş", "Trabzonspor", "Başakşehir", 
            "Alanyaspor", "Antalyaspor", "Kasımpaşa", "Konyaspor",
            "Sivasspor", "Gaziantep FK", "Adana Demirspor", "Kayserispor"
        ]
        
        fixtures = []
        start_date = datetime.date(2025, 9, 1)  # Season start
        
        for i in range(20):  # Generate 20 fixtures
            match_date = start_date + datetime.timedelta(days=i*7 + random.randint(0, 6))
            opponent = random.choice(opponents)
            home_away = random.choice(["H", "A"])
            venue = "Ülker Stadyumu" if home_away == "H" else f"{opponent} Stadyumu"
            
            fixtures.append({
                "date": match_date.strftime("%Y-%m-%d"),
                "time": f"{random.randint(16, 21)}:{random.choice(['00', '30'])}",
                "opponent": opponent,
                "home_away": home_away,
                "venue": venue,
                "competition": random.choice(["Süper Lig", "Türkiye Kupası", "UEFA"])
            })
        
        return sorted(fixtures, key=lambda x: x['date'])
    
    def get_next_match(self) -> Dict[str, Any]:
        """Get the next upcoming Fenerbahçe match"""
        today = datetime.date.today()
        
        for match in self.fixtures:
            match_date = datetime.datetime.strptime(match['date'], "%Y-%m-%d").date()
            if match_date >= today:
                return match
        
        # If no future matches found, return the last one for demo
        return self.fixtures[-1] if self.fixtures else None
    
    def get_fixtures(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get upcoming fixtures"""
        today = datetime.date.today()
        upcoming_fixtures = []
        
        for match in self.fixtures:
            match_date = datetime.datetime.strptime(match['date'], "%Y-%m-%d").date()
            if match_date >= today:
                upcoming_fixtures.append(match)
                if len(upcoming_fixtures) >= limit:
                    break
        
        return upcoming_fixtures
    
    def is_match_day(self) -> bool:
        """Check if today is a match day"""
        today = datetime.date.today().strftime("%Y-%m-%d")
        
        for match in self.fixtures:
            if match['date'] == today:
                return True
        
        return False
    
    def get_match_day_motivation(self) -> str:
        """Get special motivation message for match days"""
        match_day_quotes = [
            "🔥 BUGÜN MAÇ GÜNÜ! Önce görevlerini tamamla, sonra coşkuyla maçı izle! ⚽",
            "💛💙 Fenerbahçe ruhuyla bugün çalış! Maç öncesi hazırlığını tamamla! 🏆",
            "⚡ FORZA FENERBAHÇE! Sen de sahada olduğun gibi çalışmada da şampiyon ol! 🎯",
            "🎉 Maç günü enerjisi! Görevlerini bitir, maçı hak ederek izle! ⚽"
        ]
        
        return random.choice(match_day_quotes)
    
    def get_motivation_quote(self) -> str:
        """Get a random Fenerbahçe-themed motivational quote"""
        return random.choice(self.motivational_quotes)
    
    def get_match_week_schedule(self) -> Dict[str, Any]:
        """Get study schedule adjusted for match week"""
        next_match = self.get_next_match()
        
        if not next_match:
            return {"has_match": False}
        
        match_date = datetime.datetime.strptime(next_match['date'], "%Y-%m-%d").date()
        days_until_match = (match_date - datetime.date.today()).days
        
        # Adjust study intensity based on match proximity
        if days_until_match <= 1:
            intensity = "light"  # Light study on match day
            study_time = 60  # 1 hour
            message = "Maç günü! Hafif çalışma, sonra maç keyfi! ⚽"
        elif days_until_match <= 3:
            intensity = "normal"
            study_time = 120  # 2 hours
            message = "Maç yaklaşıyor! Normal tempoda çalışmaya devam! 💛💙"
        else:
            intensity = "intensive"
            study_time = 150  # 2.5 hours
            message = "Maça uzun var! Yoğun çalışma zamanı! 🔥"
        
        return {
            "has_match": True,
            "match_date": next_match['date'],
            "opponent": next_match['opponent'],
            "days_until_match": days_until_match,
            "intensity": intensity,
            "recommended_study_time": study_time,
            "message": message
        }
    
    def get_post_match_motivation(self, match_result: str = "win") -> str:
        """Get motivation message after match"""
        if match_result == "win":
            return "🎉 FENERBAHÇE KAZANDI! Bu coşkuyla çalışmalarına devam et! Şampiyonluk yolunda! 🏆"
        elif match_result == "draw":
            return "⚖️ Berabere bitti ama mücadele devam ediyor! Sen de çalışmada mücadeleni sürdür! 💪"
        else:
            return "😔 Bugün olmadı ama Fenerbahçe ruhu asla pes etmez! Sen de çalışmanda pes etme! 💛💙"
    
    def get_season_progress(self) -> Dict[str, Any]:
        """Get season progress and statistics"""
        # Sample season statistics
        return {
            "matches_played": 12,
            "wins": 8,
            "draws": 2,
            "losses": 2,
            "goals_for": 24,
            "goals_against": 10,
            "points": 26,
            "league_position": 2,
            "next_target": "Şampiyonluk! 🏆"
        }
    
    def get_player_spotlight(self) -> Dict[str, Any]:
        """Get featured player for motivation"""
        players = [
            {
                "name": "Edin Džeko",
                "position": "Forvet",
                "motivation": "Tecrübe ve çalışkanlik! Džeko gibi sabırla çalış! ⚽"
            },
            {
                "name": "İrfan Can Kahveci",
                "position": "Orta Saha", 
                "motivation": "Yaratıcılık ve teknik! İrfan Can gibi zeki ol! 🎯"
            },
            {
                "name": "Dominik Livakovic",
                "position": "Kaleci",
                "motivation": "Konsantrasyon ve odaklanma! Livakovic gibi odaklan! 🥅"
            }
        ]
        
        return random.choice(players)
    
    def calculate_match_bonus(self, daily_tasks_completed: int, total_tasks: int) -> Dict[str, Any]:
        """Calculate match watching bonus based on completed tasks"""
        completion_rate = daily_tasks_completed / total_tasks if total_tasks > 0 else 0
        
        if completion_rate >= 0.8:  # 80% completion
            return {
                "can_watch_full": True,
                "watch_time": "Full match",
                "bonus_message": "🎉 Harika! Tam maç izleme hakkın var!",
                "bonus_points": 50
            }
        elif completion_rate >= 0.5:  # 50% completion
            return {
                "can_watch_full": False,
                "watch_time": "Second half only",
                "bonus_message": "⚽ İyi! İkinci yarıyı izleyebilirsin!",
                "bonus_points": 25
            }
        else:
            return {
                "can_watch_full": False,
                "watch_time": "30 minutes only",
                "bonus_message": "⏰ Görevlerini tamamla, daha fazla izle!",
                "bonus_points": 10
            }
