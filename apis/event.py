from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from modules.auth.token import token_required
from modules.event.actions import add_or_update

api = Namespace('event', description='Event related operations')

event_model = api.model('event', {
    "guid": fields.String(required=True, description='System event GUID'),
    "address_street_number": fields.String(required=True, description='Street number'),
    "address_route": fields.String(required=True, description='Street'),
    "address_locality": fields.String(required=True, description='City'),
    "address_administrative_area_level_1": fields.String(required=True, description='State'),
    "address_administrative_area_level_2": fields.String(required=False, description='County'),
    "address_country": fields.String(required=True, description='Country'),
    "address_postal_code": fields.String(required=True, description='Postal code'),
    "address_postal_code_suffix": fields.String(required=False, description='Extended postal code suffix'),
    "address_lat": fields.Float(required=False, description='Latitude'),
    "address_lng": fields.Float(required=False, description='Longtitude')
})

event_example = {
    "guid": "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
    "address_street_number": "9771",
    "address_route": "Some Street",
    "address_locality": "Ubersville",
    "address_administrative_area_level_1": "Texas",
    "address_administrative_area_level_2": "Some county",
    "address_country": "Country",
    "address_postal_code": "77443",
    "address_postal_code_suffix": "1234",
    "address_lat": 39.1234,
    "address_lng": 10.5432
}


@api.route('/')
class Event(Resource):
    """Create/update event"""

    @api.response(403, "Forbidden")
    @api.response(500, 'Internal Server error')
    @api.response(201, 'Event updated successfully')
    @api.marshal_with(event_model)
    @api.expect(event_model)
    def post(self):
        """Create a new entity"""
        token_test = token_required(request.headers.get("Authorization")).get_json()
        if not token_test.get('result'):
            return token_test.get('message'), 403
        try:
            result = add_or_update(request.json)
            return result, 201
        except:
            return 'Failed event update', 500
