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


# custom command to populate the db with some initial data
@cli.command('seed_db')
def seed_db():
    db.session.add(User(
        name='Salvador',
        last_name='Estrella',
        email='seodentforever@gmail.com',
        user_type='veterinarian'
    ))
    db.session.add(User(
        name='Hector',
        last_name='Sanchez',
        email='hector-san-bb@hotmail.com',
        user_type='owner'
    ))
    db.session.commit()

        
if __name__ == '__main__':
    cli()