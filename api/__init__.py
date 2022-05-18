# blueprints/api/__init__.py
from flask import Blueprint
from flask_restx import Api
# from api.user import api as user_ns
from api.blank import api as blank_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='Flask RESTx setup for CookOffChamps.com',
    version='1.0',
    description='Backend, self documenting API blocks for cookoffchamps',
    doc='/doc'
)

# api_extension.add_namespace(user_ns)
api_extension.add_namespace(blank_ns)
