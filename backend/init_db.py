#!/usr/bin/env python3
"""
Database initialization script.
This script creates the database if it doesn't exist and runs migrations.
"""
import os
import sys
import time
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from flask_migrate import upgrade

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def wait_for_db(db_uri, max_retries=30, retry_interval=2):
    """Wait for the database to be available."""
    # For SQLite, we don't need to wait
    if db_uri.startswith('sqlite'):
        return True
    
    # Extract connection details from PostgreSQL URI
    # Format: postgresql://username:password@host:port/dbname
    db_uri_parts = db_uri.replace('postgresql://', '').split('/')
    db_name = db_uri_parts[-1]
    connection_string = db_uri_parts[0].split('@')
    credentials = connection_string[0].split(':')
    username = credentials[0]
    password = credentials[1] if len(credentials) > 1 else ''
    host_port = connection_string[1].split(':')
    host = host_port[0]
    port = host_port[1] if len(host_port) > 1 else '5432'
    
    # Create a connection string to the postgres database (exists by default)
    postgres_uri = f"postgresql://{username}:{password}@{host}:{port}/postgres"
    engine = create_engine(postgres_uri)
    
    # Try to connect to the database
    for attempt in range(max_retries):
        try:
            logger.info(f"Attempting to connect to database (attempt {attempt + 1}/{max_retries})...")
            connection = engine.connect()
            logger.info("Successfully connected to database server")
            connection.close()
            return True
        except OperationalError as e:
            logger.warning(f"Database connection failed: {e}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_interval} seconds...")
                time.sleep(retry_interval)
            else:
                logger.error("Max retries reached. Could not connect to database.")
                return False
    
    return False

def create_database_if_not_exists(db_uri):
    """Create the database if it doesn't exist."""
    # For SQLite, the database is created automatically
    if db_uri.startswith('sqlite'):
        logger.info("Using SQLite database, no need to create it explicitly")
        return True
    
    # Extract connection details from PostgreSQL URI
    db_uri_parts = db_uri.replace('postgresql://', '').split('/')
    db_name = db_uri_parts[-1]
    connection_string = db_uri_parts[0].split('@')
    credentials = connection_string[0].split(':')
    username = credentials[0]
    password = credentials[1] if len(credentials) > 1 else ''
    host_port = connection_string[1].split(':')
    host = host_port[0]
    port = host_port[1] if len(host_port) > 1 else '5432'
    
    # Create a connection string to the postgres database (exists by default)
    postgres_uri = f"postgresql://{username}:{password}@{host}:{port}/postgres"
    
    try:
        # Connect to the postgres database
        engine = create_engine(postgres_uri)
        conn = engine.connect()
        
        # Check if our database exists
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'"))
        exists = result.scalar() == 1
        
        # Create the database if it doesn't exist
        if not exists:
            # Close the connection to postgres before creating the database
            conn.execute(text("COMMIT"))
            conn.close()
            
            # Reconnect to postgres
            conn = engine.connect()
            conn.execute(text("COMMIT"))
            
            # Create the database
            logger.info(f"Creating database '{db_name}'...")
            conn.execute(text(f"CREATE DATABASE {db_name}"))
            logger.info(f"Database '{db_name}' created successfully")
        else:
            logger.info(f"Database '{db_name}' already exists")
        
        # Close the connection
        conn.close()
        return True
    
    except Exception as e:
        logger.error(f"Error creating database: {e}")
        return False

def run_migrations(app):
    """Run database migrations."""
    try:
        logger.info("Running database migrations...")
        with app.app_context():
            upgrade()
        logger.info("Migrations completed successfully")
        return True
    except Exception as e:
        logger.error(f"Error running migrations: {e}")
        return False

def init_db():
    """Initialize the database."""
    # Import app here to avoid circular imports
    from app import create_app
    from config import Config
    
    # Get database URI from config
    db_uri = Config.SQLALCHEMY_DATABASE_URI
    logger.info(f"Using database URI: {db_uri}")
    
    # Wait for the database to be available
    if not wait_for_db(db_uri):
        logger.error("Could not connect to database. Exiting.")
        return False
    
    # Create the database if it doesn't exist
    if not create_database_if_not_exists(db_uri):
        logger.error("Could not create database. Exiting.")
        return False
    
    # Create the Flask app
    app = create_app()
    
    # Run migrations
    if not run_migrations(app):
        logger.error("Could not run migrations. Exiting.")
        return False
    
    logger.info("Database initialization completed successfully")
    return True

if __name__ == "__main__":
    success = init_db()
    sys.exit(0 if success else 1)