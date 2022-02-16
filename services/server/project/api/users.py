import os
from sqlalchemy import exc
from flask import Blueprint, jsonify, request
from project.api.models import User
from project import db
from werkzeug.security import generate_password_hash, check_password_hash

users_blueprint = Blueprint('users', __name__)



@users_blueprint.route('/users', methods=['GET', 'POST'])
def all_users():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    if request.method == 'POST':
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')
        #Hashing the password
        hashed_password = generate_password_hash(password, method='sha256')
        db.session.add(User(email=email, password=hashed_password))
        db.session.commit()
        response_object['message'] = 'User added!'
        
    else:
        response_object['users'] = [user.to_json() for user in User.query.all()]
    return jsonify(response_object)

@users_blueprint.route('/users/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })


if __name__ == '__main__':
    app.run()
