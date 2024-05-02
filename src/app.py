"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Favorites, Characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# TODOS LOS GET ALL: users, planets, characters y favorites

@app.route('/users', methods=['GET'])
def handle_get_users():

    users = User.query.all()
    users_serialized = []
    for user in users:
        users_serialized.append(user.serialize())
    print(users)        

    response_body = {
        "msg": "The users: ",
        "users": users_serialized
    }

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def handle_get_planets():

    planets = Planets.query.all()
    planets_serialized = []
    for planet in planets:
        planets_serialized.append(planet.serialize())
    print(planets)        

    response_body = {
        "msg": "The planets: ",
        "planets": planets_serialized
    }

    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def handle_get_characters():

    characters = Characters.query.all()
    characters_serialized = []
    for character in characters:
        characters_serialized.append(character.serialize())
    print(characters)        

    response_body = {
        "msg": "The characters: ",
        "characters": characters_serialized
    }

    return jsonify(response_body), 200

@app.route('/users/favorites', methods=['GET'])
def handle_get_favorites():

    favorites = Favorites.query.all()
    favorites_serialized = []
    for favorite in favorites:
        favorites_serialized.append(favorite.serialize())
    print(favorites)        

    response_body = {
        "msg": "The favorites: ",
        "favorites": favorites_serialized
    }

    return jsonify(response_body), 200

# TODOS LOS GET DE 1: user, planet, character

@app.route('/users/<int:id>', methods=['GET'])
def handle_get_one_user(id):

    user = User.query.get(id)
           

    response_body = {
        "msg": "The user: ",
        "user": user.serialize()
    }

    return jsonify(response_body), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def handle_get_one_planet(id):

    planet = Planets.query.get(id)
           

    response_body = {
        "msg": "The planet: ",
        "planet": planet.serialize()
    }

    return jsonify(response_body), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def handle_get_one_character(id):

    character = Characters.query.get(id)
           

    response_body = {
        "msg": "The character: ",
        "character": character.serialize()
    }

    return jsonify(response_body), 200

# TODOS LOS POST DE 1: user, fav-planet, fav-character

@app.route('/users', methods=['POST'])
def handle_create_user():

    email : request.json.get('email')
    password : request.json.get('password')

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()      

    response_body = {
        "msg": "The user was created ",
        "user": user.serialize()
    }

    return jsonify(response_body), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def handle_fav_planet():

    name : request.json.get('name')
    climate : request.json.get('climate')
    diameter : request.json.get('diameter')
    terrain : request.json.get('terrain')
    population : request.json.get('population')
    orbital_period : request.json.get('orbital_period')

    planet = Planets(name=name, climate=climate, diameter=diameter, terrain=terrain, population=population, orbital_period=orbital_period)

    db.session.add(planet)
    db.session.commit()      

    response_body = {
        "msg": "The planet was created ",
        "planet": planet.serialize()
    }

    return jsonify(response_body), 200

@app.route('/favorite/character/<int:character_id>', methods=['POST'])
def handle_fav_character():

    name : request.json.get('name')
    bithyear : request.json.get('bithyear')
    eye_color : request.json.get('eye_color')
    hair_color : request.json.get('hair_color')
    skin_color : request.json.get('skin_color')
    gender : request.json.get('gender')

    character = Characters(name=name, bithyear=bithyear, eye_color=eye_color, hair_color=hair_color, skin_color=skin_color, gender=gender)

    db.session.add(character)
    db.session.commit()      

    response_body = {
        "msg": "The character was created ",
        "characters": characters.serialize()
    }

    return jsonify(response_body), 200

# TODOS LOS PUT DE 1: user

@app.route('/users/<int:id>', methods=['PUT'])
def handle_edit_user(id):

    email : request.json.get('email')
    password : request.json.get('password')
    
    user = User.query.get(id)
           
    user.email = email
    user.password = password
    db.session.commit()

    response_body = {
        "msg": "The user was modified ",
        "user": user.serialize()
    }

    return jsonify(response_body), 200

# TODOS LOS DELETE DE 1: user, fav-planet, fav-character

@app.route('/users/<int:id>', methods=['DELETE'])
def handle_delete_user(id):

    user = User.query.get(id)

    db.session.delete(user)   
    db.session.commit()    

    response_body = {
        "msg": "The user was deleted "
    }

    return jsonify(response_body), 200

@app.route('/favorite/character/<int:character_id>', methods=['DELETE'])
def handle_delete_fav_character(character_id):

    favorite = Favorites.query.get(character_id)

    db.session.delete(favorite)   
    db.session.commit()    

    response_body = {
        "msg": "The character was deleted "
    }

    return jsonify(response_body), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def handle_delete_fav_planet(planet_id):

    favorite = Favorites.query.get(planet_id)

    db.session.delete(favorite)   
    db.session.commit()    

    response_body = {
        "msg": "The planet was deleted "
    }

    return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
