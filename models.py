from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    education = db.Column(db.Text)
    
    # Relationships
    skills = db.relationship('Skill', backref='profile', lazy=True)
    projects = db.relationship('Project', backref='profile', lazy=True)
    work_experiences = db.relationship('WorkExperience', backref='profile', lazy=True)
    links = db.relationship('Link', backref='profile', lazy=True)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    skills_str = db.Column(db.String(200))
    links = db.Column(db.String(200))

class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50))
    description = db.Column(db.Text)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)