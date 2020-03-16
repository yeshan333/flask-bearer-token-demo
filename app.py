'''
@Author: yeshan333
@Date: 2020-03-14 12:02:56
@GitHub: https://github.com/yeshan333
@Contact: yeshan1329441308@gmail.com
@License:
@LastEditTime: 2020-03-16 10:13:48
@Description: Auth 机制
'''

from flask import Flask, session, jsonify, request
from flask.views import MethodView

from auth.get_token import generate_token, auth_required
from auth.errors import api_abort
from auth.fake_user import User, validate_password

app = Flask(__name__)

app.secret_key = '23333'

@app.route('/')
def hello():
    session[User['id']] = "hi"
    return jsonify({"hi": "xxxx"})

# payload.timestamp.signature
# eyJ1c2VyX2lkIjoiaGkifQ.XmxX9w.Vjic-HJ3Wjy2lK2pO7O86UBE_dE

# https://flask.palletsprojects.com/en/1.1.x/api/?highlight=jsonify#flask.json.jsonify
# https://flask.palletsprojects.com/en/1.1.x/api/?highlight=jsonify#flask.Response

# /protect
class ProtectSource(MethodView):

    decorators = [auth_required]

    def get(self):
        return jsonify({"Page": "Protect"})


# get token, /oauth/token
class AuthTokenAPI(MethodView):

    def post(self):
        grant_type = request.form.get('grant_type')
        username = request.form.get('username')
        password = request.form.get('password')

        if grant_type is None or grant_type.lower() != 'password':
            return api_abort(code=400, message='The grant type must be password.')

        # TODO: find user in database by username
        # user = User.query.filter_by(username=username).first()
        user = {}
        if User['username'] == username:
            user['id'] = User['id']
            user['username'] = username
        # validate_password func in fake_user, bind with User
        if user is None or not validate_password(password):
            return api_abort(code=400, message='Either the username or password was invalid.')

        token, expiration = generate_token(user)

        response = jsonify({
            'access_token': token,
            'token_type': 'Bearer',
            'expires_in': expiration
        })
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response


app.add_url_rule('/oauth/token', view_func=AuthTokenAPI.as_view('token'), methods=['POST'])
app.add_url_rule('/protect', view_func=ProtectSource.as_view('protect'), methods=['GET'])


