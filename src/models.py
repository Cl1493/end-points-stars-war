from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80), unique=False)
    is_active = db.Column(db.Boolean())
    user_id = db.relationship('Favorites', backref='user.id')
    fav_id = db.Column(db.Integer, db.ForeignKey('fav.id'))

    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.is_active = True

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fav_id = db.relationship('User', backref='fav.id')
    planets = db.relationship('Planets', backref='planets.id')
    characters = db.relationship('Characters', backref='characters.id')

    def __repr__(self):
        return '<Favorites %r>' % self.id
    
    def serialize(self):
        return {
            "planets": self.planets,
            "characters": self.characters
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fav_id = db.Column(db.Integer, db.ForeignKey('fav.id'))
    name = db.Column(db.String(250), unique=False)
    bithyear = db.Column(db.Integer)
    eye_color = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    gender = db.Column(db.String(250))

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
    fav_id = db.Column(db.Integer, db.ForeignKey('fav.id'))
    name = db.Column(db.String(250), unique=True)
    climate = db.Column(db.String(250))
    diameter = db.Column(db.Integer)
    terrain = db.Column(db.String(250))
    population = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    

    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "terrain": self.terrain,
            "skin_color": self.skin_color,
            "population": self.population,
            "orbital_period": self.orbital_period
        }