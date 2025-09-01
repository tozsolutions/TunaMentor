"""
Configuration management for TunaMentor application
"""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration class"""
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Application Configuration
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///alex_lgs.db")
    DATABASE_BACKUP_ENABLED: bool = os.getenv("DATABASE_BACKUP_ENABLED", "true").lower() == "true"
    
    # Security Configuration
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default-secret-key-please-change")
    SESSION_TIMEOUT: int = int(os.getenv("SESSION_TIMEOUT", "3600"))
    
    # Application Settings
    MAX_UPLOAD_SIZE_MB: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", "200"))
    DEFAULT_LANGUAGE: str = os.getenv("DEFAULT_LANGUAGE", "tr-TR")
    VOICE_SYNTHESIS_ENABLED: bool = os.getenv("VOICE_SYNTHESIS_ENABLED", "true").lower() == "true"
    
    # Streamlit Configuration
    STREAMLIT_SERVER_PORT: int = int(os.getenv("STREAMLIT_SERVER_PORT", "8501"))
    STREAMLIT_SERVER_ADDRESS: str = os.getenv("STREAMLIT_SERVER_ADDRESS", "0.0.0.0")
    STREAMLIT_SERVER_HEADLESS: bool = os.getenv("STREAMLIT_SERVER_HEADLESS", "true").lower() == "true"
    
    @classmethod
    def validate_config(cls) -> list[str]:
        """Validate configuration and return list of errors"""
        errors = []
        
        if not cls.OPENAI_API_KEY:
            errors.append("OPENAI_API_KEY is required but not set")
        
        if cls.SECRET_KEY == "default-secret-key-please-change" and cls.ENVIRONMENT == "production":
            errors.append("SECRET_KEY must be changed for production environment")
        
        return errors
    
    @classmethod
    def is_production(cls) -> bool:
        """Check if running in production environment"""
        return cls.ENVIRONMENT.lower() == "production"
    
    @classmethod
    def is_development(cls) -> bool:
        """Check if running in development environment"""
        return cls.ENVIRONMENT.lower() == "development"

# Create config instance
config = Config()

# Validate configuration on import
config_errors = config.validate_config()
if config_errors and config.is_production():
    raise ValueError(f"Configuration errors: {', '.join(config_errors)}")
elif config_errors:
    print(f"⚠️ Configuration warnings: {', '.join(config_errors)}")