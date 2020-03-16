## flask-bearer-token-demo-in-restful-apis

```shell
pip install virtualenv
virtualenv env
# actviate virtual environment
source env/Scripts/activate
# install dependencies
pip install -r requirements.txt
# start test
nose2
```

```python
# test_auth_flask.py
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
```

other: test by Httpie

```shell
http --form :5000/oauth/token grant_type=password username=shansan password=123456

http :5000/protect Authorization:"Bearer eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NDMyNDgzOSwiZXhwIjoxNTg0MzI4NDM5fQ.eyJpZCI6IjEyMzQ1NiJ9.pOFYk4-e-LX3tbpvDOp9wXs1JE5mbPfJQ7y7xm06evEx8Su-hsmYSRH8p_P-RLO48GTG43sBDcBvUZJAXZGy-A"
```
