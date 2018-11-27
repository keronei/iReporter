from .views import iReporter

from flask_restful import Api, Resource

from flask import Blueprint

version_one = Blueprint('api_v1',__name__, url_prefix = '/api/v1/red-flags/')

api = Api(version_one)

api.add_resource(iReporter,'/')