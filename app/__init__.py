from flask import Flask, Blueprint
from .api.v1 import version_one as v1
from .config import app_config
def launcher(config=None):
    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    app.register_blueprint(v1)
    return app

