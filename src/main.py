import os
from flask import Flask, jsonify
from flask.cli import FlaskGroup
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# Instantiate the app
app = Flask(__name__)

# Instantiate the api
api = Api(app)

# Set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# Instantiate the db
db = SQLAlchemy(app)

# Extending the Flask CLI with our own
cli = FlaskGroup(app)

# custom command to create and commit to db
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
