from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
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
    user_id = db.Column(db.Integer, db.ForeignKey('user_fav.id'), nullable=False)
    planets = db.Column(db.String(250), unique=True, nullable=False)
    characters = db.relationship('Characters', backref='characters_fav', nullable=False)

    def to_dict(self):
        return {}
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fav_id = db.Column(db.Integer, db.ForeignKey('characters_fav.id'), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    bithyear = db.Column(db.Integer)
    eye_color = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.olumn(db.String(250))
    gender = db.Column(db.String(250))

    def to_dict(self):
        return {}
    
    class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fav_id = db.Column(db.Integer, ForeignKey('favorites.id'))
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250))
    diameter = db.Column(db.Integer)
    terrain = db.Column(db.String(250))
    population = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    

    def to_dict(self):
        return {}