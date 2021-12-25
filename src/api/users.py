from flask import Blueprint, request
from flask_restx import Resource, Api
from src import db
from src.api.models import User

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

class UserList(Resource):

    def post(self):
        post_data = request.get_json()
        name = post_data.get('name')
        last_name = post_data.get('last_name')
        email = post_data.get('email')
        user_type = post_data.get('user_type')

        db.session.add(User(name=name, last_name=last_name, email=email, user_type=user_type))
        db.session.commit()

        response_object = {
            'message': f'{email} was successfully added!'
        }
        return response_object, 201


api.add_resource(UserList, '/users')
