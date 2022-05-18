from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

api = Namespace('blank', description='Very simple example')

blank_model = api.model('Blank', {
    'blankId': fields.String(),
    'firstName': fields.String(),
    'lastName': fields.String()
})

blank_model_example = {
    'blankId': '12345',
    'firstName': 'MyFirstName',
    'lastName': 'MyLastName'
}

blanks = [blank_model_example]

@api.route('/')
class BlankList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(blank_model)
    def get(self):
        """List with all the users"""
        return blanks
