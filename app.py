# app.py
from flask import Flask
from api import blueprint as api

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(api)

if __name__ == "__main__":
    app.run()