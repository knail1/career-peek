import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-please-change-in-production')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Use SQLite for local development and PostgreSQL in Docker
    if os.environ.get('DOCKER_ENV') == 'true':
        SQLALCHEMY_DATABASE_URI = os.environ.get(
            'DATABASE_URL',
            'postgresql://postgres:postgres@db:5432/career_peek'
        )
    else:
        # Use SQLite for local development
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = os.environ.get(
            'DATABASE_URL',
            f'sqlite:///{os.path.join(basedir, "career_peek_dev.sqlite")}'
        )

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    
    # Use in-memory SQLite for testing when not in Docker
    if os.environ.get('DOCKER_ENV') == 'true':
        SQLALCHEMY_DATABASE_URI = os.environ.get(
            'TEST_DATABASE_URL',
            'postgresql://postgres:postgres@db:5432/career_peek_test'
        )
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False

# Dictionary with different configuration environments
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}