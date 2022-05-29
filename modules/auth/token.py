from flask import request, jsonify
import requests


def token_required(headers):
    token = None

    if headers:
        token = headers

    if not token:
        print(f'Kicking back token {token}')
        return jsonify({'result': False, 'message': 'a valid token is missing'})

    try:
        encoded = token.split()[1]
        uri = 'https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=' + encoded
        print(f'Calling {uri}')
        validate = requests.get(uri).content
        print(f'validation {validate}')
        return jsonify({'result': True, 'message': 'success'})
    except:
        print('Failed to decode')
        return jsonify({'result': False, 'message': 'token is invalid'})


class AccessToken:
    pass
