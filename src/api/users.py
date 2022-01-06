from flask import Blueprint, request
from flask_restx import Resource, Api, fields
from src import db
from src.api.models import *


users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

user = api.model('User', {
    'id': fields.Integer(readOnly=True),
    'name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'user_type': fields.String(required=True),
    'address': fields.String(required=True),
    'city': fields.String(required=True),
    'country': fields.String(required=True),
    'zip_code': fields.String(required=True),
    'number': fields.String(required=True),
    'number_type': fields.String(required=True),
})

users = api.model('Users', {
    'id': fields.Integer(readOnly=True),
    'name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'user_type': fields.String(required=True),
})


class PostUser(Resource):

    @api.expect(user, validate=True)
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
        response_object = {}

        # guard clause to check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            response_object['message'] = 'This email is already registered to a user.'
            return response_object, 400


        user = User(
            name=name,
            last_name=last_name,
            email=email,
            user_type=user_type)
        db.session.add(user)
        db.session.commit()

        db.session.add(UserAddress(
            address=address,
            city=city,
            country=country,
            zip_code=zip_code,
            user_address=user.id
        ))

        db.session.add(PhoneNumbers(
            number=number,
            number_type=number_type,
            owner=user.id
        ))
        db.session.commit()

        response_object['message'] =  f'{email} was successfully added'
        return response_object, 201


class GetUser(Resource):

    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        
        # guard clause that checks if user exists
        if user:
            user_address = UserAddress.query.filter_by(user_address=user_id).first()
            user_number = PhoneNumbers.query.filter_by(owner=user_id).first()
            response_object = {
                'id': user.id,
                'name': user.name,
                'last_name': user.last_name,
                'email': user.email,
                'user_type': user.user_type,
                'address': user_address.address,
                'city': user_address.city,
                'country': user_address.country,
                'zip_code': user_address.zip_code,
                'number': user_number.number,
                'number_type': user_number.number_type,
            }
            return response_object, 200
        else:    
            api.abort(404, f'The user with the id:{user_id} does not exist')


class GetUsers(Resource):

    @api.marshal_with(users, as_list=True)
    def get(self):
        return User.query.all(), 200

    
api.add_resource(PostUser, '/users/create')
api.add_resource(GetUser, '/users/read/<int:user_id>')
api.add_resource(GetUsers, '/users/read')