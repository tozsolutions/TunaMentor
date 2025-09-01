"""
Logging configuration for TunaMentor application
"""
import logging
import logging.handlers
import os
from datetime import datetime
from config import config

def setup_logging():
    """Setup logging configuration"""
    
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    # Set logging level based on config
    log_level = getattr(logging, config.LOG_LEVEL.upper(), logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Create root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    # Remove existing handlers to avoid duplication
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    
    # File handler (rotating)
    log_filename = f"logs/alex_lgs_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.handlers.RotatingFileHandler(
        log_filename,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    
    # Error handler (separate file for errors)
    error_filename = f"logs/alex_lgs_errors_{datetime.now().strftime('%Y%m%d')}.log"
    error_handler = logging.handlers.RotatingFileHandler(
        error_filename,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    root_logger.addHandler(error_handler)
    
    # Application logger
    app_logger = logging.getLogger("alex_lgs")
    app_logger.info(f"Logging initialized - Level: {config.LOG_LEVEL} - Environment: {config.ENVIRONMENT}")
    
    return app_logger

def get_logger(name: str = "alex_lgs") -> logging.Logger:
    """Get logger instance"""
    return logging.getLogger(name)

# Initialize logging on import
if not logging.getLogger().handlers:
    setup_logging()