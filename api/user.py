from flask import request
from flask_restx import Namespace, Resource, fields
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
    'firstName': fields.String(description='User first name'),
    'lastName': fields.String(description='User last name'),
    'oAuthConnections': fields.Nested(oAuthId, as_list=True),
    'cellPhone': fields.String(required=False, description='Single cellphone number'),
    'emailAddress': fields.Nested(email, as_list=True)
})

user_example = {
    'id': '234-24-234-234',
    'firstName': 'FirstName',
    'lastName': 'LastName',
    'oAuthConnections': [oAuthId_example],
    'cellPhone': '1234567980',
    'emailAddress': [email_example]
}


@api.route('')
class UserList(Resource):
    """Get users list and create new users"""

    @api.response(500, 'Internal Server error')
    @api.marshal_list_with(user)
    def get(self):
        """List with all the users"""
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
        """Create a new entity"""

        if request.json['name'] == 'User name':
            api.abort(400, 'User with the given name already exists')
        user_list = [user_example]

        return user_list, 201


@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        """Fetch a user given its identifier"""
        for thisUser in UserList:
            if thisUser['id'] == id:
                return thisUser
        api.abort(404)
