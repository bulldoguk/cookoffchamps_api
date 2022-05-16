from flask_restx import Api

from api.cats import api as cats

api = Api(
    title='CookOffChampsAPIs',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(cats, path='/api/cats')
