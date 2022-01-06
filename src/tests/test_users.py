import json
from src.api.models import *


# POST TESTS
def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users/create',
        data=json.dumps({
            'name': 'Salvador',
            'last_name': 'Estrella',
            'email': 'seodentforever@gmail.com',
            'user_type': 'owner',
            'address': 'Calle primavera #369 Col. Luz',
            'city': 'Santiago de Queretaro',
            'country': 'Mexico',
            'zip_code': '76147',
            'number': '442 253 8197',
            'number_type': 'mobile',
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'seodentforever@gmail.com was successfully added' in data['message']


def test_add_user_duplicate_email(test_app, test_database, add_user):
    client = test_app.test_client()
    add_user(
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
    resp = client.post(
        '/users/create',
        data=json.dumps({
            'name': 'Hector',
            'last_name': 'Sanchez',
            'email': 'hector-san-bb@hotmail.com',
            'user_type': 'veterinarian',
            'address': 'Calle de la amargura #13 Col. Primavera',
            'city': 'Santiago de Queretaro',
            'country': 'Mexico',
            'zip_code': '76145',
            'number': '446 100 7788',
            'number_type': 'mobile'
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'This email is already registered to a user.' in data['message']

    
def test_add_user_empty_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users/create',
        data=json.dumps({}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


def test_add_user_incomplete_json_keys(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users/create',
        data=json.dumps({'email': 'peatpi@gmail.com'}),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert 'Input payload validation failed' in data['message']


# GET TESTS
def test_get_single_user(test_app, test_database, add_user):
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
    client = test_app.test_client()
    resp = client.get(f'/users/read/{user.id}')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'Hector' in data['name']
    assert 'hector-san-bb@hotmail.com' in data['email']
    assert 'Calle de la amargura #13 Col. Primavera' in data['address']
    assert 'Santiago de Queretaro' in data['city']
    assert '446 100 7788' in data['number']
    assert 'mobile' in data['number_type']


def test_get_single_user_invalid_id(test_app, test_database):
    client = test_app.test_client()
    resp = client.get('/users/read/666')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert 'The user with the id:666 does not exist' in data['message']


def test_get_all_users(test_app, test_database, add_user):
    test_database.session.query(UserAddress).delete()
    test_database.session.query(PhoneNumbers).delete()
    test_database.session.query(User).delete()
    add_user(
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
    add_user(
        name='Salvador',
        last_name='Estrella',
        email='seodentforever@gmail.com',
        user_type='owner',
        address='Josafat F Marquez 23 Col. Constituyentes',
        city='Santiago de Queretaro',
        country='Mexico',
        zip_code='76147',
        number='446 233 7788',
        number_type='mobile'
        )
    client = test_app.test_client()
    resp = client.get('/users/read')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data) == 2
    assert 'Hector' in data[0]['name']
    assert 'Salvador' in data[1]['name']
    assert 'hector-san-bb@hotmail.com' in data[0]['email']
    assert 'seodentforever@gmail.com' in data[1]['email']
