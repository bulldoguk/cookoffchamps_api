from flask import Flask
from apis import api
from flask_cors import CORS
from flask_cors import logging

logging.getLogger('flask_cors').level = logging.DEBUG

app = Flask(__name__)
api.init_app(app)

# enable CORS
CORS(app)

app.run(debug=True)