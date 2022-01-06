import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  


# instantiate the db
db = SQLAlchemy()


# factory pattern
def create_app(scritp_info=None):
    """
    Factory to create the Flask application
    :return: A `Flask` application instance.
    """

    # instantiate the  app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from src.api.route import route_blueprint
    app.register_blueprint(route_blueprint)
    from src.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    from src.api.cards import cards_blueprint
    app.register_blueprint(cards_blueprint)


    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        """Creates a shell context that adds the database
        and model to the shell session"""
        return {'app': app, 'db': db}

    return app



