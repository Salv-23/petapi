from flask import Flask, jsonify
from flask_restx import Resource, Api


# instantiate the app
app = Flask(__name__)
# instantiate the api
api = Api(app)
# set config
app.config.from_object('src.config.DevelopmentConfig')


# first endpoint 
class Test(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'It works!'
        }

# Add resource to the api
api.add_resource(Test, '/test')

