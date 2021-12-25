import json


def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({
            'name': 'Hector',
            'last_name': 'Sanchez',
            'email': 'hector-san-bb@hotmail.com',
            'user_type': 'owner'
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'hector-san-bb@hotmail.com was successfully added!' in data['message']
