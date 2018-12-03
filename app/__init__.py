
from flask import Flask, Blueprint
from .api.v1 import version_one as v1
from .api.v2 import version_two as v2
from .config import app_config
from .api.v2.models import db

def launcher():
    app = Flask(__name__)
    app.config.from_object(app_config['development'])
    db.init_app(app)
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app