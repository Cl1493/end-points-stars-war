from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='user')


    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
    
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.id
    
    def serialize(self):
        return {
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    bithyear = db.Column(db.Integer, unique=False, nullable=False)
    eye_color = db.Column(db.String(250), unique=False, nullable=False)
    hair_color = db.Column(db.String(250), unique=False, nullable=False)
    skin_color = db.Column(db.String(250), unique=False, nullable=False)
    gender = db.Column(db.String(250), unique=False, nullable=False)
    favorite = db.relationship('Favorites', backref='characters')

    def __repr__(self):
        return '<Characters %r>' % self.name
    
    def serialize(self):
        return {
            "name": self.name,
            "birthyear": self.birthyear,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "gender": self.gender
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    climate = db.Column(db.String(250), unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    terrain = db.Column(db.String(250), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)
    favorite = db.relationship('Favorites', backref='planets')
    

    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "terrain": self.terrain,
            "population": self.population,
            "orbital_period": self.orbital_period
        }