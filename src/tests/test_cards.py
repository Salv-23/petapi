import json
from src.api.models import *


# POST TESTS
def test_add_card(test_app, test_database, add_user):
    # Creating a new user to link it to the card
    test_database.session.query(UserAddress).delete()
    test_database.session.query(PhoneNumbers).delete()
    test_database.session.query(User).delete()
    user = add_user(
        name='Hector',
        last_name='Sanchez',
        email='hector-san-bb@hotmail.com',
        user_type='veterinarian',
        address='Calle de la amargura #13 Col. Primavera',
        city='Santiago de Queretaro',
        country='Mexico',
        zip_code='76145',
        number='446 100 7788',
        number_type='mobile'
        )
    # Creating a card
    client = test_app.test_client()
    resp = client.post(
        '/cards/create',
        data=json.dumps({
            'pet_name': 'Apollo',
            'pet_race': 'Husky',
            'pet_gender': 'Undecided',
            'birthday': '2021-03-23T10:00:00',
            'notes': 'A good boy',
            'owner': user.id,
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert f'Successfully created a card for Apollo and it is linked to the user id:{user.id}' in data['message']


def test_add_card_invalid_user_id(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/cards/create',
        data=json.dumps({
            'pet_name': 'Apollo',
            'pet_race': 'Husky',
            'pet_gender': 'Undecided',
            'birthday': '2021-03-23T10:00:00',
            'notes': 'A good boy',
            'owner': 666,
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'This owner does not exist' in data['message']


def test_add_duplicate_card_to_user(test_app, test_database, add_user, add_card):
    # Creating a new user and a linked card with pet_name=Nero
    test_database.session.query(Cards).delete()
    test_database.session.query(UserAddress).delete()
    test_database.session.query(PhoneNumbers).delete()
    test_database.session.query(User).delete()
    user = add_user(
        name='Hector',
        last_name='Sanchez',
        email='hector-san-bb@hotmail.com',
        user_type='veterinarian',
        address='Calle de la amargura #13 Col. Primavera',
        city='Santiago de Queretaro',
        country='Mexico',
        zip_code='76145',
        number='446 100 7788',
        number_type='mobile'
        )
    add_card(
        pet_name='Nero',
        pet_race='Schnauzer',
        pet_gender='Male',
        birthday='2016-01-23T03:03:03',
        notes='Does not shut up',
        owner=user.id
    )
    # Trying to link a new card to user with the same pet_name
    client = test_app.test_client()
    resp = client.post(
        '/cards/create',
        data=json.dumps({
            'pet_name': 'Nero',
            'pet_race': 'Schnauzer',
            'pet_gender': 'Male',
            'birthday': '2016-01-23T03:03:03',
            'notes': 'Does not shut up',
            'owner':user.id
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert f'Nero is already linked as a pet to the userId:{user.id}'


def test_add_card_empty_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        'cards/create',
        data=json.dumps({}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


def test_add_card_incomplete_json_keys(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        'cards/create',
        data=json.dumps({'pet_name': 'Firulais'}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


# GET TESTS
def test_get_single_card(test_app, test_database, add_user, add_card):
    test_database.session.query(Cards).delete()
    test_database.session.query(UserAddress).delete()
    test_database.session.query(PhoneNumbers).delete()
    test_database.session.query(User).delete()
    user = add_user(
        name='Hector',
        last_name='Sanchez',
        email='hector-san-bb@hotmail.com',
        user_type='veterinarian',
        address='Calle de la amargura #13 Col. Primavera',
        city='Santiago de Queretaro',
        country='Mexico',
        zip_code='76145',
        number='446 100 7788',
        number_type='mobile'
        )
    add_card(
        pet_name='Nero',
        pet_race='Schnauzer',
        pet_gender='Male',
        birthday='2016-01-23T03:03:03',
        notes='Does not shut up',
        owner=user.id
    )
    client = test_app.test_client()
    resp = client.get(f'/cards/read/{user.id}')
    data = json.loads(resp.data.decode())
    
