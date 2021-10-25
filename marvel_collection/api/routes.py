from flask import Blueprint, request, jsonify
from marvel_collection.helpers import token_required
from marvel_collection.models import Character, db, character_schema, characters_schema

api = Blueprint('api', __name__, url_prefix='/api')

# CRUD functionality below

# CREATE ENDPOINT
@api.route('/characters', methods=['POST'])
@token_required
def create_character(current_user_token):
    name = request.json['name']
    description = request.json['description']
    token = current_user_token.token

    print(f'TEST: {current_user_token.token}')

    character = Character(name,description,user_token = token)

    db.session.add(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)

# RETRIEVE ROUTES
# Retrive all characters associated w/ user token
@api.route('/characters', methods = ['GET'])
@token_required
def get_characters(current_user_token):
    owner = current_user_token.token
    characters = Character.query.filter_by(user_token = owner).all()
    response = characters_schema.dump(characters)
    return jsonify(response)

# Retrieve 1 character (by ID) associated w/ user token
@api.route('/characters/<id>', methods = ['GET'])
@token_required
def get_character(current_user_token, id):
    character = Character.query.get(id)
    if character:
        print(f'Here is your character: {character.name}')
        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That character does not exist!'})


# Update a single Drone by ID
@api.route('/characters/<id>', methods = ['POST', 'PUT'])
@token_required
def update_character(current_user_token, id):
    character = Character.query.get(id)
    print(character)
    if character:
        character.name = request.json['name']
        character.description = request.json['description']
        character.user_token = current_user_token.token
        db.session.commit()

        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That character does not exist!'})


# DELETE ROUTE
@api.route('/characters/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    if character:
        db.session.delete(character)
        db.session.commit()
        return jsonify({'Success': f'Character ID #{character.id} has been deleted'})
    else:
        return jsonify({'Error': 'That character does not exist!'})
