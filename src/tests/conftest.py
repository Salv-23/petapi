import pytest
from src.api.models import *
from src import create_app, db  


@pytest.fixture(scope='module')
def test_app():
    app = create_app()  
    app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app  


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='function')
def add_user():
    def _add_user(
        name, last_name, email,
        user_type, address, city,
        country, zip_code, number,
        number_type):
        user = User(
            name=name, 
            last_name=last_name,
            email=email, 
            user_type=user_type)
        db.session.add(user)
        db.session.commit()
        user_address = UserAddress(
            address=address, 
            city=city, 
            country=country, 
            zip_code=zip_code, 
            user_address=user.id)
        user_number = PhoneNumbers(
            number=number, 
            number_type=number_type, 
            owner=user.id)
        db.session.add(user_address)
        db.session.add(user_number)
        db.session.commit()
        return user
    return _add_user


@pytest.fixture(scope='function')
def add_card():
    def _add_card(pet_name, pet_race, pet_gender, birthday, notes, owner):
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
    return _add_card
    