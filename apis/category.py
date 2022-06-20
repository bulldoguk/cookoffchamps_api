from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from modules.auth.token import token_required

# TODO: Add actions module for categories

api = Namespace('category', description='Category related operations')

category_model = api.model('category', {
    "guid": fields.String(required=True, description='System event GUID'),
    "relatedEvent": fields.String(required=True, description='Related event GUID'),
    "title": fields.String(required=True, description='Category title', example='Texas Chili'),
    "questions": fields.List(fields.String(example="3b6598c6-6d4f-4293-ac66-9f564dc302e8"))
})

category_example = {
    "guid": "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
    "title": "This is the first category",
    "questions": ["3b6598c6-6d4f-4293-ac66-9f564dc302e8", "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
                  "3b6598c6-6d4f-4293-ac66-9f564dc302e8"]
}


@api.route('/')
class Category(Resource):
    """Create / update category"""

    @api.response(403, "Forbidden")
    @api.response(500, 'Internal Server error')
    @api.response(201, 'Event updated successfully')
    @api.marshal_with(category_model)
    @api.expect(category_model)
    def post(self):
        """Create a new category"""
        return 'Success', 201
