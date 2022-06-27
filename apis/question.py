from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from modules.auth.token import token_required

# TODO: Add actions module for questions

api = Namespace('question', description='Question related operations')

question_model = api.model('question', {
    "guid": fields.String(required=True, description='System event GUID'),
    "relatedCategory": fields.String(required=True, description='Category GUID'),
    "headLine": fields.String(required=True, description='Question headline', example='How spicy is it?'),
    "detail": fields.String(description='Question details', example='0=mild, 5=too much'),
    "responses": fields.List(fields.String(example="3b6598c6-6d4f-4293-ac66-9f564dc302e8"))
})

question_example = {
    "guid": "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
    "relatedCategory": "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
    "headLine": "This is the first question",
    "detail": "A much longer version of the question",
    "responses": ["3b6598c6-6d4f-4293-ac66-9f564dc302e8", "3b6598c6-6d4f-4293-ac66-9f564dc302e8",
                  "3b6598c6-6d4f-4293-ac66-9f564dc302e8"]
}

@api.route('/')
class Question(Resource):
    """Create / update question"""

    @api.response(403, "Forbidden")
    @api.response(500, 'Internal Server error')
    @api.response(201, 'Event updated successfully')
    @api.marshal_with(question_model)
    @api.expect(question_model)
    def post(self):
        """Create a new question"""
        return 'Success', 201
