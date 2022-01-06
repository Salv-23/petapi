from flask import Blueprint, request
from flask_restx import Resource, Api, fields
from src import db
from src.api.models import *

cards_blueprint = Blueprint('cards', __name__)
api = Api(cards_blueprint)

card = api.model('Card', {
    'id': fields.Integer(readOnly=True),
    'pet_name': fields.String(required=True),
    'pet_race': fields.String(required=True),
    'pet_gender': fields.String(required=True),
    'birthday': fields.DateTime(dt_format='iso8601'),
    'notes': fields.String,
    'owner': fields.Integer(readOnly=True),
})


class PostCard(Resource):

    @api.expect(card, validate=True)
    def post(self):
        post_data = request.get_json()
        pet_name = post_data.get('pet_name')
        pet_race = post_data.get('pet_race')
        pet_gender = post_data.get('pet_gender')
        birthday = post_data.get('birthday')
        notes = post_data.get('notes')
        owner = post_data.get('owner')
        response_object = {}

        # guard clause to check if owner exists
        owner_id = User.query.filter_by(id=owner).first()
        if not owner_id:
            response_object['message'] = 'This owner does not exist'
            return response_object, 400
            
        # guard clause to check for duplicate pet
        pet = Cards.query.filter_by(owner=owner, pet_name=pet_name).first()
        if pet:
            response_object['message'] = f'{pet_name} is already linked as a pet to the userId:{owner}'
            return response_object, 400
        
        
        card = Cards(
            pet_name=pet_name,
            pet_race=pet_race,
            pet_gender=pet_gender,
            birthday=birthday,
            notes=notes,
            owner=owner
        )
        db.session.add(card)
        db.session.commit()

        response_object['message'] = f'Successfully created a card for {pet_name} and it is linked to the user id:{owner}'
        return response_object, 201


api.add_resource(PostCard, '/cards/create')