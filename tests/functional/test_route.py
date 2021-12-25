import json

def test_route(test_app):
    """
    GIVEN a flask test client application
    WHEN a get request is sent to /test route
    THEN a proper response code and data is returned
    """
    client = test_app.test_client()
    resp = client.get('/test')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'success' in data['status']
    assert 'It works!' in data['message']
    