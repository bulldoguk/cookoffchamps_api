from flask import Flask, request
from apis import api
from flask_cors import CORS

app = Flask(__name__)
api.init_app(app)

# enable CORS
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
