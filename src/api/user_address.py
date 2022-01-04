# from flask import Blueprint, request
# from flask_restx import Resource, Api, fields
# from src import db
# from src.api.models import *
# from src.api.users import user


# user_address_blueprint = Blueprint('user_address', __name__)
# api = Api(user_address_blueprint)

# address = api.model('UserAddress', {
#     'id': fields.Integer(readOnly=True),
#     'address': fields.String(required=True),
#     'city': fields.String(required=True),
#     'country': fields.String(required=True),
#     'zip_code': fields.Integer(required=True),
#     'user_address': fields.Integer(required=True)
# })


# class AddressList(Resource):

#     def post(self):
#         post_data = request.get_json()
#         address = post_data.get('address')
#         city = post_data.get('city')
#         country = post_data.get('country')
#         zip_code = post_data.get('zip_code')
#         user_address = post_data.get('user_address')
#         response_object = {}

#         db.session.add(UserAddress(
#             address=address,
#             city=city,
#             country=country,
#             zip_code=zip_code,
#             user_address=user_address
#         ))
#         db.session.commit()

#         response_object = {
#             'message': f'Address information for user {user_address} successfully added'
#         }
#         return response_object, 201


# api.add_resource(AddressList, '/users/<int:user_address>/address')