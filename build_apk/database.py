import sqlite3
import json
import datetime
from typing import Dict, List, Any

class Database:
    def __init__(self, db_path="alex_lgs.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_points INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1,
                streak INTEGER DEFAULT 0
            )
        ''')
        
        # Study sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS study_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                subject TEXT NOT NULL,
                topic TEXT,
                duration_minutes INTEGER NOT NULL,
                session_date DATE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        
        # Questions and answers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS question_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                subject TEXT NOT NULL,
                topic TEXT NOT NULL,
                question_id TEXT NOT NULL,
                user_answer TEXT,
                correct_answer TEXT,
                is_correct BOOLEAN NOT NULL,
                attempt_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        
        # Mistakes tracking table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mistakes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                subject TEXT NOT NULL,
                topic TEXT NOT NULL,
                question_id TEXT NOT NULL,
                mistake_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                reviewed BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        
        # Spaced repetition table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS spaced_repetition (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                subject TEXT NOT NULL,
                topic TEXT NOT NULL,
                next_review_date DATE NOT NULL,
                review_count INTEGER DEFAULT 0,
                difficulty_level INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        
        # Achievements table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS achievements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                achievement_name TEXT NOT NULL,
                achievement_description TEXT,
                points_awarded INTEGER DEFAULT 0,
                achieved_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        
        # Daily goals table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                goal_date DATE NOT NULL,
                subject TEXT NOT NULL,
                target_minutes INTEGER NOT NULL,
                completed_minutes INTEGER DEFAULT 0,
                completed BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        
        # Future lessons progress
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS future_lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                lesson_title TEXT NOT NULL,
                lesson_type TEXT NOT NULL,
                completion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (username) REFERENCES users (username)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_user_session(self, username: str):
        """Create or update user session"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR IGNORE INTO users (username) VALUES (?)
        ''', (username,))
        
        conn.commit()
        conn.close()
    
    def log_study_time(self, username: str, subject: str, duration: int, topic: str = None):
        """Log study session"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        today = datetime.date.today()
        
        cursor.execute('''
            INSERT INTO study_sessions (username, subject, topic, duration_minutes, session_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, subject, topic, duration, today))
        
        conn.commit()
        conn.close()
    
    def log_question_attempt(self, username: str, subject: str, topic: str, 
                           question_id: str, user_answer: str, correct_answer: str, is_correct: bool):
        """Log question attempt"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO question_attempts 
            (username, subject, topic, question_id, user_answer, correct_answer, is_correct)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (username, subject, topic, question_id, user_answer, correct_answer, is_correct))
        
        conn.commit()
        conn.close()
    
    def log_mistake(self, username: str, subject: str, topic: str, question_id: str):
        """Log a mistake for spaced repetition"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO mistakes (username, subject, topic, question_id)
            VALUES (?, ?, ?, ?)
        ''', (username, subject, topic, question_id))
        
        conn.commit()
        conn.close()
    
    def add_to_spaced_repetition(self, username: str, subject: str, topic: str):
        """Add topic to spaced repetition schedule"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Calculate next review date (start with 1 day)
        next_review = datetime.date.today() + datetime.timedelta(days=1)
        
        cursor.execute('''
            INSERT OR REPLACE INTO spaced_repetition 
            (username, subject, topic, next_review_date)
            VALUES (?, ?, ?, ?)
        ''', (username, subject, topic, next_review))
        
        conn.commit()
        conn.close()
    
    def get_study_stats(self, username: str, period: str = "week") -> Dict[str, Any]:
        """Get study statistics for a user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Calculate date range
        today = datetime.date.today()
        if period == "week":
            start_date = today - datetime.timedelta(days=7)
        elif period == "month":
            start_date = today - datetime.timedelta(days=30)
        else:
            start_date = datetime.date(2025, 1, 1)  # All time
        
        # Total study time
        cursor.execute('''
            SELECT SUM(duration_minutes) FROM study_sessions 
            WHERE username = ? AND session_date >= ?
        ''', (username, start_date))
        
        total_minutes = cursor.fetchone()[0] or 0
        
        # Subject breakdown
        cursor.execute('''
            SELECT subject, SUM(duration_minutes) FROM study_sessions 
            WHERE username = ? AND session_date >= ?
            GROUP BY subject
        ''', (username, start_date))
        
        subject_breakdown = dict(cursor.fetchall())
        
        # Question accuracy
        cursor.execute('''
            SELECT COUNT(*), SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) 
            FROM question_attempts 
            WHERE username = ? AND DATE(attempt_date) >= ?
        ''', (username, start_date))
        
        total_questions, correct_answers = cursor.fetchone()
        accuracy = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        
        conn.close()
        
        return {
            'total_study_time': round(total_minutes / 60, 1),  # Convert to hours
            'subject_breakdown': subject_breakdown,
            'questions_solved': total_questions or 0,
            'accuracy': round(accuracy, 1),
            'total_minutes': total_minutes
        }
    
    def get_user_points(self, username: str) -> int:
        """Get user's total points"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT total_points FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        
        conn.close()
        return result[0] if result else 0
    
    def update_user_points(self, username: str, points: int):
        """Update user's points"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE users SET total_points = total_points + ? WHERE username = ?
        ''', (points, username))
        
        conn.commit()
        conn.close()
    
    def get_completed_future_lessons(self, username: str) -> List[Dict[str, Any]]:
        """Get completed future lessons"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT lesson_title, lesson_type, completion_date 
            FROM future_lessons 
            WHERE username = ?
            ORDER BY completion_date DESC
        ''', (username,))
        
        lessons = []
        for row in cursor.fetchall():
            lessons.append({
                'title': row[0],
                'type': row[1],
                'completion_date': row[2]
            })
        
        conn.close()
        return lessons
    
    def add_future_lesson_completion(self, username: str, lesson_title: str, lesson_type: str):
        """Add completed future lesson"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO future_lessons (username, lesson_title, lesson_type)
            VALUES (?, ?, ?)
        ''', (username, lesson_title, lesson_type))
        
        conn.commit()
        conn.close()
