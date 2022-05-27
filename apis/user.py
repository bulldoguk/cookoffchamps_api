from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

api = Namespace('user', description='User related operations')

user_model = api.model('user', {
    "sub": fields.String(required=True, description='oAuth provider ID'),
    "name": fields.String(required=False, description='oAuth provided'),
    "given_name": fields.String(required=False, description='oAuth provided'),
    "family_name": fields.String(required=False, description='oAuth provided'),
    "profile": fields.String(required=False, description='oAuth profile link'),
    "picture": fields.String(required=False, description='oAuth provided'),
    "email": fields.String(required=True, description='Unique identifier for our system'),
    "email_verified": fields.Boolean(required=False),
    "gender": fields.String(required=False),
    "locale": fields.String(required=False, description='Used in i18n, defaults to en'),
    "hd": fields.String(required=False, description='Used to identify superusers, must have email_verified')
})

user_example = {
    "sub": "106226106196704017887",
    "name": "Gary Bailey",
    "given_name": "Gary",
    "family_name": "Bailey",
    "profile": "https://plus.google.com/106226106196704017887",
    "picture": "https://lh3.googleusercontent.com/a-/AOh14GhuErhFmR0i2t-vF8aSdLtI1LP4aR65Os2oioYXKJc=s96-c",
    "email": "gary@myhmbiz.com",
    "email_verified": True,
    "gender": "male",
    "locale": "en",
    "hd": "myhmbiz.com"
}


@api.route('/')
class User(Resource):
    """Get user info or create/update user"""

    @api.response(400, 'User with the given name already exists')
    @api.response(500, 'Internal Server error')
    @api.marshal_with(user_model)
    @api.expect(user_model)
    def post(self):
        """Create a new entity"""
        print(request.json)
        return request.json, 201


@api.route('/user/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(user_model)
    @api.response(500, 'Internal Server error')
    def get(self, id):
        """Fetch a user given its identifier"""
        return user_example, 200

    def post(self, id):
        """Update user details"""
        return "User updated", 201
