from flask import Blueprint, request
from flask_restx import Resource, Api
from src import db
from src.api.models import *

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UsersPost(Resource):

    def post(self):
        post_data = request.get_json()
        name = post_data.get('name')
        last_name = post_data.get('last_name')
        email = post_data.get('email')
        user_type = post_data.get('user_type')
        address = post_data.get('address')
        city = post_data.get('city')
        country = post_data.get('country')
        zip_code = post_data.get('zip_code')
        number = post_data.get('number')
        number_type = post_data.get('number_type')


        db.session.add(User(
            name=name,
            last_name=last_name,
            email=email,
            user_type=user_type
        ))
        db.session.commit()

        user_id = db.session.query(User.id).filter_by(email=email)
        db.session.add(UserAddress(
            address=address,
            city=city,
            country=country,
            zip_code=zip_code,
            user_address=user_id
        ))
        db.session.add(PhoneNumbers(
            number=number,
            number_type=number_type,
            owner=user_id
        ))

        response_object = {
            'message': f'{email} was successfully added'
        }
        return response_object, 201
    
api.add_resource(UsersPost, '/users/create')


















# from flask import Blueprint, request
# from flask_restx import Resource, Api, fields
# from src import db
# from src.api.models import *

# users_blueprint = Blueprint('users', __name__)
# api = Api(users_blueprint)


# user = api.model('User', {
#     'id': fields.Integer(readOnly=True),
#     'name': fields.String(required=True),
#     'last_name': fields.String(required=True),
#     'email': fields.String(required=True),
#     'user_type': fields.String(required=True),
# })


# class UserList(Resource):

#     @api.expect(user, validate=True)
#     def post(self):
#         post_data = request.get_json()
#         name = post_data.get('name')
#         last_name = post_data.get('last_name')
#         email = post_data.get('email')
#         user_type = post_data.get('user_type')
#         response_object = {}

#         user = User.query.filter_by(email=email).first()
#         if user:
#             response_object['message'] = 'Sorry. That email already exists.'
#             return response_object, 400

#         db.session.add(User(
#             name=name,
#             last_name=last_name,
#             email=email,
#             user_type=user_type
#         ))
#         db.session.commit()


#         response_object = {
#             'message': f'{email} was successfully added!'
#         }
#         return response_object, 201
    

#     @api.marshal_with(user, as_list=True)
#     def get(self):
#         return User.query.all(), 200


# class Users(Resource):

#     @api.marshal_with(user)
#     def get(self, user_id):
#         user = User.query.filter_by(id=user_id).first()
#         if not user:
#             api.abort(404, f'User {user_id} does not exist')
#         return user, 200


# api.add_resource(UserList, '/users')
# api.add_resource(Users, '/users/<int:user_id>')
