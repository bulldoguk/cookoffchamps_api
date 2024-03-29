from flask import request, jsonify
from flask_restx import Namespace, Resource, fields, reqparse
from modules.auth.token import token_required
from modules.event.actions import add_or_update, list_events, get_event

api = Namespace('event', description='Event related operations')

event_model = api.model('event', {
    "guid": fields.String(required=True, description='System event GUID'),
    "title": fields.String(required=True, description='Event title'),
    "seTitle": fields.String(required=False, description="SE title for use in URLs"),
    "address_street_number": fields.String(required=True, description='Street number'),
    "address_route": fields.String(required=True, description='Street'),
    "address_locality": fields.String(required=True, description='City'),
    "address_administrative_area_level_1": fields.String(required=True, description='State'),
    "address_administrative_area_level_2": fields.String(required=False, description='County'),
    "address_country": fields.String(required=True, description='Country'),
    "address_postal_code": fields.String(required=True, description='Postal code'),
    "address_postal_code_suffix": fields.String(required=False, description='Extended postal code suffix'),
    "address_lat": fields.Float(required=False, description='Latitude'),
    "address_lng": fields.Float(required=False, description='Longitude'),
    "categories": fields.List(fields.String(example="3b6598c6-6d4f-4293-ac66-9f564dc302e8"))
})

event_example = {
    "guid": "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
    "title": "This is going to be a great event",
    "seTitle": "This_is_going_to_be_a_great_event",
    "address_street_number": "9771",
    "address_route": "Some Street",
    "address_locality": "Ubersville",
    "address_administrative_area_level_1": "Texas",
    "address_administrative_area_level_2": "Some county",
    "address_country": "Country",
    "address_postal_code": "77443",
    "address_postal_code_suffix": "1234",
    "address_lat": 39.1234,
    "address_lng": 10.5432,
    "categories": ["3b6598c6-6d4f-4293-ac66-9f564dc302e8", "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
                   "3b6598c6-6d4f-4293-ac66-9f564dc302e8"]
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
        """Create a new event"""
        token_test = token_required(request.headers.get("Authorization")).get_json()
        if not token_test.get('result'):
            return token_test.get('message'), 403
        try:
            result = add_or_update(request.json)
            return result, 201
        except:
            return 'Failed event add or update', 500


@api.route('/list')
class EventList(Resource):
    """Pull list of events public or for a user"""

    # TODO Will need a way to filter or paginate this
    @api.response(500, 'Internal server error')
    @api.response(200, 'Success')
    @api.marshal_list_with(event_model)
    def get(self):
        """Pull list of all events"""
        userguid = str(request.args.get('userguid'))
        try:
            result = list_events(userguid)
            return result, 200
        except Exception as e:
            return e, 500


@api.route('/detail/<se_name>')
class EventDetail(Resource):
    """Pull event details for a given seName"""

    @api.response(500, 'Internal server error')
    @api.response(200, 'Success')
    @api.marshal_with(event_model)
    def get(self, se_name):
        try:
            result = get_event(se_name)
            return result, 200
        except Exception as e:
            return e, 500
