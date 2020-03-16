'''
@Author: yeshan333
@Date: 2020-03-14 17:58:23
@GitHub: https://github.com/yeshan333
@Contact: yeshan1329441308@gmail.com
@License:
@LastEditTime: 2020-03-14 20:22:33
@Description:
'''

from itsdangerous.serializer import Serializer
from itsdangerous import JSONWebSignatureSerializer
s = Serializer("secret-key")

print(s.dumps([1, 2, 3, 4]))

# itsdangerous.exc.BadSignature: Signature b'r7R9RhGgDPvvWl3iNzLuIIfELmo' does not match
# print(s.loads('[1, 2, 3].r7R9RhGgDPvvWl3iNzLuIIfELmo'))

jws = JSONWebSignatureSerializer("secret-key")

print(jws.dumps(0, header_fields={"v": 1}))

print(jws.loads("eyJ2IjoxLCJhbGciOiJIUzUxMiJ9.MA.JO6MA9EEyQPvf_IbRuP6zT9Sa2KjKOxub2ssCpgHCj_ZqsOkCxlFvp1QebNuDHhz8UHiO1EbAG80HrQQyJD7CA"
      , return_header=True))