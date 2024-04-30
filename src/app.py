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

# TODOS LOS GET DE 1: user, planet, character y favorite

@app.route('/users/<int:id>', methods=['GET'])
def handle_get_one_user(id):

    user = User.query.get(id)
           

    response_body = {
        "msg": "The user: ",
        "user": user.serialize()
    }

    return jsonify(response_body), 200

# TODOS LOS POST DE 1: user, planet, character

@app.route('/users', methods=['POST'])
def handle_create_user():

    email : request.json.get('email')
    password : request.json.get('password')

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.comit()      

    response_body = {
        "msg": "The user was created ",
        "user": user.serialize()
    }

    return jsonify(response_body), 200

# TODOS LOS PUT DE 1: user, planet, character

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

# TODOS LOS DELETE DE 1: user, planet, character

@app.route('/users/<int:id>', methods=['DELETE'])
def handle_delete_user(id):

    user = User.query.get(id)

    db.session.delete(user)   
    db.session.commit()    

    response_body = {
        "msg": "The user was deleted "
    }

    return jsonify(response_body), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
