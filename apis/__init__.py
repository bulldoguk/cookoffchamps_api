from flask_restx import Api

from .namespace1 import api as ns1
from .user import api as user

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1, path='/prefix/of/ns1')
api.add_namespace(user, path='/user')
