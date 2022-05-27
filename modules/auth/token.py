from flask import request, jsonify
from google.auth import crypt
from google.auth import jwt


def token_required(headers):
    token = None

    if headers:
        token = headers

    print(f'Got token {token}')
    if not token:
        print(f'Kicking back token {token}')
        return jsonify({'result': False, 'message': 'a valid token is missing'})

    try:
        # data = jwt.decode(token.split()[1], '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', algorithms=["HS256"])
        # encoded = token.split()
        # print(encoded)
        data = jwt.decode(encoded, verify=False)
        print(f'Decoded data {data}')
        return jsonify({'result': True, 'message': 'success'})
    except:
        print('Failed to decode')
        return jsonify({'result': False, 'message': 'token is invalid'})


class AccessToken:
    pass
