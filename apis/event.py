from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from modules.auth.token import token_required

api = Namespace('event', description='User related operations')

event_model = api.model('event', {
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
    "hd": fields.String(required=False, description='Used to identify superusers, must have email_verified'),
    "extended_info": fields.Boolean(required=False, description='Added by system as flag that we have extended data on this user'),
    "some_new_data": fields.String(required=False, description='Test field to show passing extended data back')
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
    "hd": "myhmbiz.com",
    "extended_info": True
}


@api.route('/')
class User(Resource):
    """Create/update user"""

    @api.response(403, "Forbidden")
    @api.response(400, 'User with the given name already exists')
    @api.response(500, 'Internal Server error')
    @api.response(201, 'User updated successfully')
    @api.marshal_with(user_model)
    @api.expect(user_model)
    def post(self):
        """Create a new entity"""
        token_test = token_required(request.headers.get("Authorization")).get_json()
        if not token_test.get('result'):
            return token_test.get('message'), 403
        try:
            result = add_or_update(request.json)
            return result, 201
        except:
            return 'Failed user update', 500


@api.route('/<id>')
class UserUpdate(Resource):
    @api.param('id', 'The user identifier')
    @api.response(404, 'User not found')
    @api.doc('get_user')
    @api.marshal_with(user_model)
    @api.response(500, 'Internal Server error')
    def get(self, id):
        """Fetch a user given its identifier"""
        return user_example, 200

    def patch(self, id):
        """Update user details"""
        return "User updated", 201
