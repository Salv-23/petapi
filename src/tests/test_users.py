import json


def test_add_user_owner(test_app, test_database):
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
















# import json
# from src.api.models import *

# # POST 
# def test_add_user(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.post(
#         '/users',
#         data=json.dumps({
#             'name': 'Hector',
#             'last_name': 'Sanchez',
#             'email': 'hector-san-bb@hotmail.com',
#             'user_type': 'owner'
#         }),
#         content_type='application/json',
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 201
#     assert 'hector-san-bb@hotmail.com was successfully added!' in data['message']


# def test_add_user_invalid_json(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.post(
#         '/users',
#         data=json.dumps({}),
#         content_type='application/json',
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert 'Input payload validation failed' in data['message']


# def test_add_user_invalid_json_keys(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.post(
#         '/users',
#         data=json.dumps({'email': 'hector-san-bb@hotmail.com'}),
#         content_type='applicaton/json',
#     )    
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert 'Input payload validation failed' in data['message']


# def test_add_user_duplicate_email(test_app, test_database):
#     client = test_app.test_client()
#     client.post(
#         '/users',
#         data=json.dumps({
#             'name': 'Hector',
#             'last_name': 'Sanchez',
#             'email': 'hector-san-bb@hotmail.com',
#             'user_type': 'owner'
#         }),
#         content_type='application/json',
#     )
#     resp = client.post(
#         '/users',
#         data=json.dumps({
#             'name': 'Hector',
#             'last_name': 'Sanchez',
#             'email': 'hector-san-bb@hotmail.com',
#             'user_type': 'owner'
#         }),
#         content_type='application/json',
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert 'Sorry. That email already exists.' in data['message']

# # GET
# def test_single_user(test_app, test_database, add_user):
#     user = add_user(
#         name='Salvador', 
#         last_name='Estrella', 
#         email='seodentforever@gmail.com', 
#         user_type='owner'
#     )
#     client = test_app.test_client()
#     resp = client.get(f'/users/{user.id}')
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 200
#     assert 'Salvador' in data['name']
#     assert 'Estrella' in data['last_name']
#     assert 'seodentforever@gmail.com' in data['email']
#     assert 'owner' in data['user_type']


# def test_single_user_incorrect_id(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.get('/users/333')
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 404
#     assert 'User 333 does not exist' in data['message']

# def test_all_users(test_app, test_database, add_user):
#     test_database.session.query(User).delete()
#     add_user(
#         name='Hector',
#         last_name='Sanchez',
#         email='hector-san-bb@hotmail.com',
#         user_type='owner'
#     )
#     add_user(
#         name='Salvador',
#         last_name='Estrella',
#         email='seodentforever@gmail.com',
#         user_type='veterinarian'
#     )
#     client = test_app.test_client()
#     resp = client.get('/users')
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 200
#     assert len(data) == 2
#     assert 'Hector' in data[0]['name']
#     assert 'Salvador' in data[1]['name']
#     assert 'hector-san-bb@hotmail.com' in data[0]['email']
#     assert 'seodentforever@gmail.com' in data[1]['email']
#     assert 'Sanchez' in data[0]['last_name']
#     assert 'Estrella' in data[1]['last_name']
#     assert 'owner' in data[0]['user_type']
#     assert 'veterinarian' in data[1]['user_type']



