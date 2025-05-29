import pytest
import json
from datetime import datetime, date, timedelta
from app import create_app
from extensions import db
from models import Profile, JobHistory, Education, ProfileTag, ProfileVersion

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app('testing')
    
    # Create all tables
    with app.app_context():
        db.create_all()
    
    yield app
    
    # Clean up after test
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test CLI runner for the app."""
    return app.test_cli_runner()

@pytest.fixture
def sample_profile(app):
    """Create a sample profile for testing."""
    with app.app_context():
        profile = Profile(
            name="John Doe",
            linkedin_url="https://www.linkedin.com/in/johndoe",
            engagement_score=85.5
        )
        db.session.add(profile)
        db.session.commit()
        
        # Get a fresh instance from the database to avoid detached instance errors
        profile_id = profile.id
        fresh_profile = Profile.query.get(profile_id)
        return fresh_profile

def test_profile_creation(app):
    """Test that a profile can be created."""
    with app.app_context():
        profile = Profile(
            name="Jane Smith",
            linkedin_url="https://www.linkedin.com/in/janesmith",
            engagement_score=92.3
        )
        db.session.add(profile)
        db.session.commit()
        
        saved_profile = Profile.query.filter_by(name="Jane Smith").first()
        assert saved_profile is not None
        assert saved_profile.name == "Jane Smith"
        assert saved_profile.linkedin_url == "https://www.linkedin.com/in/janesmith"
        assert saved_profile.engagement_score == 92.3
        assert saved_profile.created_at is not None
        assert saved_profile.updated_at is not None

def test_profile_linkedin_url_validation(app):
    """Test that LinkedIn URL validation works."""
    with app.app_context():
        # Test valid URLs
        valid_urls = [
            "https://www.linkedin.com/in/validuser",
            "http://www.linkedin.com/in/validuser",
            "https://linkedin.com/in/validuser",
            "http://linkedin.com/in/validuser"
        ]
        
        for url in valid_urls:
            profile = Profile(name="Test User", linkedin_url=url)
            db.session.add(profile)
            db.session.commit()
            db.session.delete(profile)
            db.session.commit()
        
        # Test invalid URLs
        invalid_urls = [
            "",
            "https://facebook.com/user",
            "linkedin.com/in/invaliduser",
            "www.linkedin.com/in/invaliduser"
        ]
        
        for url in invalid_urls:
            with pytest.raises(ValueError):
                profile = Profile(name="Test User", linkedin_url=url)

def test_job_history_creation(app, sample_profile):
    """Test that job history can be created and linked to a profile."""
    with app.app_context():
        job = JobHistory(
            profile_id=sample_profile.id,
            company_name="Tech Corp",
            company_url="https://techcorp.com",
            company_size="1001-5000",
            role="Senior Developer",
            role_type="Full-time",
            start_date=date(2020, 1, 15),
            end_date=date(2023, 6, 30),
            is_current=False,
            description="Led development of key features"
        )
        db.session.add(job)
        db.session.commit()
        
        saved_job = JobHistory.query.filter_by(company_name="Tech Corp").first()
        assert saved_job is not None
        assert saved_job.role == "Senior Developer"
        assert saved_job.start_date == date(2020, 1, 15)
        assert saved_job.profile_id == sample_profile.id
        
        # Test relationship
        profile = Profile.query.get(sample_profile.id)
        assert len(profile.jobs) == 1
        assert profile.jobs[0].company_name == "Tech Corp"

def test_education_creation(app, sample_profile):
    """Test that education can be created and linked to a profile."""
    with app.app_context():
        education = Education(
            profile_id=sample_profile.id,
            institution="University of Technology",
            degree="Bachelor of Science",
            field_of_study="Computer Science",
            start_date=date(2016, 9, 1),
            end_date=date(2020, 5, 31)
        )
        db.session.add(education)
        db.session.commit()
        
        saved_education = Education.query.filter_by(institution="University of Technology").first()
        assert saved_education is not None
        assert saved_education.degree == "Bachelor of Science"
        assert saved_education.field_of_study == "Computer Science"
        
        # Test relationship
        profile = Profile.query.get(sample_profile.id)
        assert len(profile.education) == 1
        assert profile.education[0].institution == "University of Technology"

def test_profile_tag_creation(app, sample_profile):
    """Test that profile tags can be created and linked to a profile."""
    with app.app_context():
        tag1 = ProfileTag(
            profile_id=sample_profile.id,
            tag_name="python"
        )
        tag2 = ProfileTag(
            profile_id=sample_profile.id,
            tag_name="machine-learning"
        )
        db.session.add_all([tag1, tag2])
        db.session.commit()
        
        saved_tags = ProfileTag.query.filter_by(profile_id=sample_profile.id).all()
        assert len(saved_tags) == 2
        tag_names = [tag.tag_name for tag in saved_tags]
        assert "python" in tag_names
        assert "machine-learning" in tag_names
        
        # Test relationship
        profile = Profile.query.get(sample_profile.id)
        assert len(profile.tags) == 2

def test_profile_version_creation(app, sample_profile):
    """Test that profile versions can be created and linked to a profile."""
    with app.app_context():
        # Create a snapshot of the profile data
        profile_data = {
            "name": sample_profile.name,
            "linkedin_url": sample_profile.linkedin_url,
            "engagement_score": sample_profile.engagement_score
        }
        
        version = ProfileVersion(
            profile_id=sample_profile.id,
            version_number=1,
            data_snapshot=json.dumps(profile_data),
            valid_from=datetime.utcnow()
        )
        db.session.add(version)
        db.session.commit()
        
        saved_version = ProfileVersion.query.filter_by(profile_id=sample_profile.id).first()
        assert saved_version is not None
        assert saved_version.version_number == 1
        
        # Test data serialization/deserialization
        data = saved_version.get_data()
        assert data["name"] == sample_profile.name
        assert data["linkedin_url"] == sample_profile.linkedin_url
        
        # Test relationship
        profile = Profile.query.get(sample_profile.id)
        assert len(profile.versions) == 1
        assert profile.versions[0].version_number == 1

def test_timestamps_automation(app):
    """Test that timestamps are automatically set and updated."""
    with app.app_context():
        # Create a profile
        profile = Profile(
            name="Auto Timestamp User",
            linkedin_url="https://www.linkedin.com/in/autotimestamp"
        )
        db.session.add(profile)
        db.session.commit()
        
        # Check that created_at and updated_at are set
        assert profile.created_at is not None
        assert profile.updated_at is not None
        initial_updated_at = profile.updated_at
        
        # Wait a moment to ensure timestamp difference
        import time
        time.sleep(1)
        
        # Update the profile
        profile.name = "Updated Timestamp User"
        db.session.commit()
        
        # Check that updated_at has changed
        assert profile.updated_at > initial_updated_at

def test_cascade_delete(app):
    """Test that deleting a profile cascades to related entities."""
    with app.app_context():
        # Create a profile with related entities
        profile = Profile(
            name="Cascade Test User",
            linkedin_url="https://www.linkedin.com/in/cascadetest"
        )
        db.session.add(profile)
        db.session.flush()
        
        # Add job history
        job = JobHistory(
            profile_id=profile.id,
            company_name="Cascade Corp",
            role="Developer",
            start_date=date(2020, 1, 1),
            is_current=True
        )
        
        # Add education
        education = Education(
            profile_id=profile.id,
            institution="Cascade University",
            degree="Bachelor's"
        )
        
        # Add tag
        tag = ProfileTag(
            profile_id=profile.id,
            tag_name="cascade-test"
        )
        
        # Add version
        version = ProfileVersion(
            profile_id=profile.id,
            version_number=1,
            data_snapshot=json.dumps({"name": profile.name}),
            valid_from=datetime.utcnow()
        )
        
        db.session.add_all([job, education, tag, version])
        db.session.commit()
        
        # Verify all related entities exist
        assert JobHistory.query.count() == 1
        assert Education.query.count() == 1
        assert ProfileTag.query.count() == 1
        assert ProfileVersion.query.count() == 1
        
        # Delete the profile
        db.session.delete(profile)
        db.session.commit()
        
        # Verify all related entities are deleted
        assert Profile.query.count() == 0
        assert JobHistory.query.count() == 0
        assert Education.query.count() == 0
        assert ProfileTag.query.count() == 0
        assert ProfileVersion.query.count() == 0