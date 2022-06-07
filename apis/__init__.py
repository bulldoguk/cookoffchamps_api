from flask_restx import Api

from .user import api as user
from .event import api as event

api = Api(
    title='Cook Off Champs API documentation',
    version='1.0',
    description='APIs used to manage cookoffchamps.  Requires Google authentication token.',
    # All API metadatas
)

api.add_namespace(user, path='/user')
api.add_namespace(event, path='/event')
