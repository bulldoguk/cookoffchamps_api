from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from modules.auth.token import token_required

# TODO: Add actions module for responses

api = Namespace('response', description='Response related operations')

response_model = api.model('response', {
    "guid": fields.String(example='xyz'),
    "relatedQuestion": fields.String(description='Related question GUID'),
    "score": fields.Integer(example='1'),
    "description": fields.String(example='No flavor')
})

response_example = {
    "guid": "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
    "relatedQuestion": "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
    "score": "Numeric value of this response",
    "description": "A description of what makes this score",
}


@api.route('/')
class Response(Resource):
    """Create / update response"""

    @api.response(403, "Forbidden")
    @api.response(500, 'Internal Server error')
    @api.response(201, 'Event updated successfully')
    @api.marshal_with(response_model)
    @api.expect(response_model)
    def post(self):
        """Create a new response"""
        return 'Success', 201
