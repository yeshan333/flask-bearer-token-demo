'''
@Author: yeshan333
@Date: 2020-03-16 09:18:56
@GitHub: https://github.com/yeshan333
@Contact: yeshan1329441308@gmail.com
@License:
@LastEditTime: 2020-03-16 09:28:01
@Description:
'''

User = {
    'id': "123456",
    'username': "shansan",
    'password': "123456"
}

def validate_password(password):
    if password == User['password']:
        return True
    return False
