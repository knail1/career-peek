from flask import Flask, jsonify
from flask_cors import CORS
import os

# Import extensions
from extensions import db, migrate

def create_app(config_name='default'):
    """Application factory function."""
    # Import config module
    from config import config
    
    # Create Flask app
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Enable CORS for frontend
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import models to ensure they are registered with SQLAlchemy
    from models import Profile, JobHistory, Education, ProfileTag, ProfileVersion
    
    # Register blueprints
    
    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint to verify API and database status."""
        db_status = "disconnected"
        
        try:
            # Check database connection
            db.session.execute('SELECT 1')
            db_status = "connected"
        except Exception as e:
            app.logger.error(f"Database connection error: {str(e)}")
        
        return jsonify({
            "status": "healthy",
            "database": db_status
        })
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"error": "Server error"}), 500
    
    return app

if __name__ == '__main__':
    # Get environment from environment variable or default to development
    env = os.environ.get('FLASK_ENV', 'development')
    
    # Create app with appropriate configuration
    app = create_app(env)
    
    # Run the app
    app.run(host='0.0.0.0', port=5000)