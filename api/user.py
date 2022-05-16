from argparse import Namespace
from xmlrpc.client import Boolean
from flask_restx import api, Resource, fields
from http import HTTPStatus

api = Namespace('user', description='User related operations')

oAuthId = api.model('oAuth', {
    'provider': fields.String(required=True, description='oAuth provider, such as Google, etc'),
    'providerId': fields.String(required=True, description='UserID from provider'),
    'tenantId': fields.String(required=True, description='Tenant ID from oAuth provider')
})

oAuthId_example = {
    'provider': 'google',
    'providerId': 'asda-sdfsdf-123123-sdf',
    'tenantId': 'dfgsdgdfg-fgsdfg-fgsdfg'
}

email = api.model('email', {
    'id': fields.String(required=True, description='Unique email address identifier'),
    'emailAddress': fields.String(required=True, description='Email address'),
    'oAuth': fields.Boolean(value=False),
    'primary': fields.Boolean(value=False)
})

email_example = {
    'id': 'abc-123-dfsf',
    'emailAddress': 'something@example.com',
    'oAuth': True,
    'primary': True
}

user = api.model('User', {
    'id': fields.String(required=True, description='Unique user identifier'),
    'oAuthConnections': fields.Nested(oAuthId, as_list=True),
    'cellPhone': fields.String(required=False, description='Single cellphone number'),
    'emailAddress': fields.Nested(email, as_list=True)
})

user_example = {
    'id': '234-24-234-234',
    'oAuthConnections': [oAuthId_example],
    'cellPhone': '1234567980',
    'emailAddress': [email_example]
}


@api.route('')
class userList(Resource):
    '''Get users list and create new users'''

    @api.response(500, 'Internal Server error')
    @api.marshal_list_with(user_list)
    def get(self):
        '''List with all the users'''
        user_list = [user_example]

        return {
            'entities': user_list,
            'total_records': len(user_list)
        }

    @api.response(400, 'User with the given name already exists')
    @api.response(500, 'Internal Server error')
    @api.expect(user)
    @api.marshal_with(user, code=HTTPStatus.CREATED)
    def post(self):
        '''Create a new entity'''

        if request.json['name'] == 'User name':
            api.abort(400, 'User with the given name already exists')

        return user_list_example, 201


@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class user(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        '''Fetch a user given its identifier'''
        for user in user_list:
            if user['id'] == id:
                return user
        api.abort(404)
