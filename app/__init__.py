
from flask import Flask, Blueprint
from .api.v1 import version_one as v1
from .config import app_config

def launcher():
    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    app.register_blueprint(v1)
<<<<<<< HEAD
    return app
=======
    return app
>>>>>>> 3b255b5c37a95a6d2c78cf52dd281a686ea26a0e
