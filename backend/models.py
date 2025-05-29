from datetime import datetime
import json
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy

# Import db from a separate module to avoid circular imports
from extensions import db

class Profile(db.Model):
    """Profile model representing a LinkedIn user profile."""
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    linkedin_url = db.Column(db.String(255), nullable=False, unique=True, index=True)
    last_updated = db.Column(db.DateTime, nullable=True)
    engagement_score = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    jobs = db.relationship('JobHistory', back_populates='profile', cascade='all, delete-orphan')
    education = db.relationship('Education', back_populates='profile', cascade='all, delete-orphan')
    tags = db.relationship('ProfileTag', back_populates='profile', cascade='all, delete-orphan')
    versions = db.relationship('ProfileVersion', back_populates='profile', cascade='all, delete-orphan')
    
    @validates('linkedin_url')
    def validate_linkedin_url(self, key, url):
        """Validate that the LinkedIn URL is properly formatted."""
        if not url:
            raise ValueError("LinkedIn URL cannot be empty")
        
        if not url.startswith(('https://www.linkedin.com/', 'http://www.linkedin.com/', 
                              'https://linkedin.com/', 'http://linkedin.com/')):
            raise ValueError("Invalid LinkedIn URL format")
        
        return url
    
    def __repr__(self):
        return f"<Profile {self.name} ({self.id})>"


class JobHistory(db.Model):
    """JobHistory model representing a job in a user's career history."""
    __tablename__ = 'job_history'
    
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False, index=True)
    company_name = db.Column(db.String(255), nullable=False)
    company_url = db.Column(db.String(255), nullable=True)
    company_size = db.Column(db.String(50), nullable=True)
    role = db.Column(db.String(255), nullable=False)
    role_type = db.Column(db.String(100), nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    is_current = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    profile = db.relationship('Profile', back_populates='jobs')
    
    def __repr__(self):
        return f"<JobHistory {self.role} at {self.company_name} ({self.id})>"


class Education(db.Model):
    """Education model representing educational background of a profile."""
    __tablename__ = 'education'
    
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False, index=True)
    institution = db.Column(db.String(255), nullable=False)
    degree = db.Column(db.String(255), nullable=True)
    field_of_study = db.Column(db.String(255), nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    profile = db.relationship('Profile', back_populates='education')
    
    def __repr__(self):
        return f"<Education {self.degree} at {self.institution} ({self.id})>"


class ProfileTag(db.Model):
    """ProfileTag model for tagging and categorizing profiles."""
    __tablename__ = 'profile_tags'
    
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False, index=True)
    tag_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    profile = db.relationship('Profile', back_populates='tags')
    
    # Composite unique constraint
    __table_args__ = (
        db.UniqueConstraint('profile_id', 'tag_name', name='uix_profile_tag'),
    )
    
    def __repr__(self):
        return f"<ProfileTag {self.tag_name} for profile {self.profile_id}>"


class ProfileVersion(db.Model):
    """ProfileVersion model for Slowly Changing Dimension (SCD) tracking."""
    __tablename__ = 'profile_versions'
    
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False, index=True)
    version_number = db.Column(db.Integer, nullable=False)
    data_snapshot = db.Column(db.Text, nullable=False)  # JSON serialized data
    valid_from = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    valid_to = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    profile = db.relationship('Profile', back_populates='versions')
    
    # Composite unique constraint
    __table_args__ = (
        db.UniqueConstraint('profile_id', 'version_number', name='uix_profile_version'),
    )
    
    def get_data(self):
        """Deserialize the JSON data snapshot."""
        return json.loads(self.data_snapshot)
    
    def set_data(self, data):
        """Serialize data to JSON for storage."""
        self.data_snapshot = json.dumps(data)
    
    def __repr__(self):
        return f"<ProfileVersion {self.version_number} for profile {self.profile_id}>"