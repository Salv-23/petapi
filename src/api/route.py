from flask import Blueprint
from flask_restx import Resource, Api


route_blueprint = Blueprint('route', __name__)
api = Api(route_blueprint)


# first endpoint 
class Route(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'It works!'
        }
        

# Add resource to the api
api.add_resource(Route, '/route')