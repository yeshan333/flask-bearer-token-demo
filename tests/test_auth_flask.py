'''
@Author: yeshan333
@Date: 2020-03-16 09:54:26
@GitHub: https://github.com/yeshan333
@Contact: yeshan1329441308@gmail.com
@License:
@LastEditTime: 2020-03-16 10:43:58
@Description: api test, https://flask.palletsprojects.com/en/1.1.x/testing/#testing
'''

import unittest

from app import app

class Flask_APP_Test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        self.app.testing = True

    # /oauth/token
    # Httpie: http --form :5000/oauth/token grant_type=password username=shansan password=123456
    def test_token(self):
        result = self.app.post('/oauth/token', \
            data={"grant_type": "password", "username": "shansan", "password": "123456"}, \
            content_type='multipart/form-data')
        data = result.get_json()
        self.assertEqual(data['token_type'], "Bearer")

    # Httpie: http :5000/protect Authorization:"Bearer eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NDMyNDgzOSwiZXhwIjoxNTg0MzI4NDM5fQ.eyJpZCI6IjEyMzQ1NiJ9.pOFYk4-e-LX3tbpvDOp9wXs1JE5mbPfJQ7y7xm06evEx8Su-hsmYSRH8p_P-RLO48GTG43sBDcBvUZJAXZGy-A"
    def test_visit_by_token(self):
        get_token_response  = self.app.post('/oauth/token', \
            data={"grant_type": "password", "username": "shansan", "password": "123456"}, \
            content_type='multipart/form-data')

        rep_json = get_token_response.get_json()
        token = rep_json['access_token']

        result = self.app.get('/protect', \
            headers={'Authorization': 'Bearer {}'.format(token)})

        self.assertEqual(result.status_code, 200)
