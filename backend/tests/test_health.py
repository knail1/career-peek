import pytest
from app import create_app, db

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app('testing')
    
    # Create a test client using the Flask application
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_health_check(client):
    """Test that the health check endpoint returns 200 and correct JSON."""
    response = client.get('/health')
    
    # Check status code
    assert response.status_code == 200
    
    # Check response data
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['database'] in ['connected', 'disconnected']