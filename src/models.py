from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)
    user_id = db.relationship('Favorites', backref='user_fav', nullable=False)

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
    user_id = db.Column(db.Integer, db.ForeignKey('user_fav.id'), nullable=True)
    planets = db.relationship('Planets', backref='planets_fav', nullable=True)
    characters = db.relationship('Characters', backref='characters_fav', nullable=True)

    def __repr__(self):
        return '<Favorites %r>' % self.id
    
    def serialize(self):
        return {
            "planets": self.planets,
            "characters": self.characters
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fav_id = db.Column(db.Integer, db.ForeignKey('characters_fav.id'), nullable=False)
    name = db.Column(db.String(250), unique=False, nullable=False)
    bithyear = db.Column(db.Integer, nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.olumn(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)

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
    fav_id = db.Column(db.Integer, db.ForeignKey('planets_fav.id'), nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    

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