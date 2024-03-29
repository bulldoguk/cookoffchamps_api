from flask_restx import Api

from .user import api as user
from .event import api as event
from .category import api as category
from .question import api as question
from .response import api as response

api = Api(
    title='Cook Off Champs API documentation',
    version='1.0',
    description='APIs used to manage cookoffchamps.  Requires Google authentication token.',
    # All API metadatas
)

api.add_namespace(user, path='/user')
api.add_namespace(event, path='/event')
api.add_namespace(category, path='/category')
api.add_namespace(question, path='/question')
api.add_namespace(response, path='/response')
