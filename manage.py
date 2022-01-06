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
    user_one = User(
        name='Salvador',
        last_name='Estrella',
        email='seodentforver@gmail.com',
        user_type='veterinarian'
    )
    db.session.add(user_one)
    db.session.commit()
    user_one_address = UserAddress(
        address='Josafat F. Marquez 48',
        city='Queretaro',
        country='Mexico',
        zip_code='76145',
        user_address=user_one.id
    )
    user_one_number = PhoneNumbers(
        number='442 112 7471',
        number_type='mobile',
        owner=user_one.id
    )
    user_two = User(
        name='Hector',
        last_name='Sanchez',
        email='hector-san-bb@gmail.com',
        user_type='owner'
    )
    db.session.add(user_two)
    db.session.commit()
    user_two_address = UserAddress(
        address='Calle primavera privada amargura 13',
        city='Queretaro',
        country='Mexico',
        zip_code='76152',
        user_address=user_two.id
    )
    user_two_number = PhoneNumbers(
        number='442 147 3416',
        number_type='mobile',
        owner=user_two.id
    )
    db.session.add(user_one_address)
    db.session.add(user_one_number)
    db.session.add(user_two_address)
    db.session.add(user_two_number)
    db.session.commit()

        
if __name__ == '__main__':
    cli()