import sys
from flask.cli import FlaskGroup
from src import create_app, db
from src.api.models import *


app = create_app()

# extending the Flask CLI with our own 
cli = FlaskGroup(create_app=create_app)


# custom command to create and commit to db
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()