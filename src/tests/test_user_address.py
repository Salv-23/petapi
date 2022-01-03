# import json
# from src.api.models import *


# # POST
# def test_add_user_address(test_app, test_database, add_user):
#     test_database.session.query(User).delete()
#     add_user(
#         name='Hector',
#         last_name='Sanchez',
#         email='hector-san-bb@hotmail.com',
#         user_type='owner'
#     )
#     client = test_app.test_client()
#     resp = client.post(
#         '/users/1/address',
#         data=json.dumps({
#             'address': 'calle amargura 13',
#             'city': 'santiago de queretaro',
#             'country': 'mexico',
#             'zip_code': 76145,
#             'user_address': 1
#         }),
#         content_type='application/json',
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 201
#     assert 'Address information for user 1 successfully added' in data['message']
#     assert 'Hector' in data['user']['name']




# # user_address = api.model('UserAddress', {
# #     'id': fields.Integer(readOnly=True),
# #     'address': fields.String(required=True),
# #     'city': fields.String(required=True),
# #     'country': fields.String(required=True),
# #     'zip_code': fields.Integer(required=True),
# #     'user_address': fields.Integer(required=True)
# # })