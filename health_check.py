#!/usr/bin/env python3
"""
Health check script for TunaMentor application
"""
import sys
import sqlite3
import requests
from pathlib import Path
from config import config
from logger import get_logger

def check_database():
    """Check database connectivity"""
    try:
        db_path = config.DATABASE_URL.replace('sqlite:///', '')
        if Path(db_path).exists():
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            conn.close()
            return True, f"Database OK ({len(tables)} tables)"
        else:
            return False, "Database file not found"
    except Exception as e:
        return False, f"Database error: {e}"

def check_openai():
    """Check OpenAI API configuration"""
    if not config.OPENAI_API_KEY:
        return False, "OpenAI API key not configured"
    elif config.OPENAI_API_KEY.startswith('sk-'):
        return True, "OpenAI API key configured"
    else:
        return False, "Invalid OpenAI API key format"

def check_streamlit_server():
    """Check if Streamlit server is running"""
    try:
        url = f"http://{config.STREAMLIT_SERVER_ADDRESS}:{config.STREAMLIT_SERVER_PORT}/_stcore/health"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True, "Streamlit server running"
        else:
            return False, f"Streamlit server returned {response.status_code}"
    except Exception as e:
        return False, f"Streamlit server not reachable: {e}"

def check_logs_directory():
    """Check logs directory"""
    logs_dir = Path("logs")
    if logs_dir.exists() and logs_dir.is_dir():
        log_files = list(logs_dir.glob("*.log"))
        return True, f"Logs directory OK ({len(log_files)} files)"
    else:
        return False, "Logs directory not found"

def main():
    """Run all health checks"""
    logger = get_logger(__name__)
    logger.info("Starting health checks...")
    
    checks = [
        ("Database", check_database),
        ("OpenAI API", check_openai),
        ("Logs Directory", check_logs_directory),
        ("Streamlit Server", check_streamlit_server),
    ]
    
    results = []
    all_passed = True
    
    for name, check_func in checks:
        try:
            passed, message = check_func()
            status = "✅ PASS" if passed else "❌ FAIL"
            results.append(f"{status} {name}: {message}")
            
            if not passed:
                all_passed = False
                logger.error(f"Health check failed - {name}: {message}")
            else:
                logger.info(f"Health check passed - {name}: {message}")
                
        except Exception as e:
            status = "❌ ERROR"
            message = str(e)
            results.append(f"{status} {name}: {message}")
            all_passed = False
            logger.error(f"Health check error - {name}: {message}")
    
    # Print results
    print("\n🏥 TunaMentor Health Check Results")
    print("=" * 40)
    for result in results:
        print(result)
    
    print("=" * 40)
    if all_passed:
        print("🎉 All health checks passed!")
        logger.info("All health checks passed")
        sys.exit(0)
    else:
        print("⚠️ Some health checks failed!")
        logger.warning("Some health checks failed")
        sys.exit(1)

if __name__ == "__main__":
    main()