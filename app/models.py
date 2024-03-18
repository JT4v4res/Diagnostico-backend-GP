# app/models.py

from app import db

class Anamnesis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    profession = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum('male', 'female', 'other'), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    symptoms = db.Column(db.ARRAY(db.String(100)), nullable=False)
    complaint_duration = db.Column(db.Integer, nullable=False)
    childhood_diseases = db.Column(db.ARRAY(db.String(100)), nullable=False)
    allergies = db.Column(db.ARRAY(db.String(100)), nullable=False)
    family_history = db.Column(db.ARRAY(db.String(100)), nullable=False)
    meal_frequency = db.Column(db.String(100), nullable=False)
    power_type = db.Column(db.String(100), nullable=False)
    water_consumption = db.Column(db.String(100), nullable=False)
    food_preferences = db.Column(db.ARRAY(db.String(100)), nullable=False)
    

    def __repr__(self):
        return '<Anamnesis %r>' % self.id
