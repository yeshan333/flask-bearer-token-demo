'''
@Author: yeshan333
@Date: 2020-03-14 12:10:11
@GitHub: https://github.com/yeshan333
@Contact: yeshan1329441308@gmail.com
@License:
@LastEditTime: 2020-03-14 12:24:21
@Description: analysis flask session
'''

import base64

def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result

def int_to_bytes(value, length):
    result = []

    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)

    result.reverse()

    return result



# payload.timestamp.signature
# eyJ1c2VyX2lkIjoiaGkifQ.XmxX9w.Vjic-HJ3Wjy2lK2pO7O86UBE_dE

payload = base64.urlsafe_b64decode(b'eyJ1c2VyX2lkIjoiaGkifQ==')  # b'{"user_id":"hi"}'

print(payload)

timestamp = base64.urlsafe_b64decode(b'XmxX9w==')

print(bytes_to_int(timestamp))


