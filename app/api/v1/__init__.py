from .views.views import IreporterFlags, User

from flask_restful import Api, Resource

from flask import Blueprint


version_one = Blueprint('api_v1',__name__)#url_prefix = '/api/v1/')

api = Api(version_one)

api.add_resource(IreporterFlags,'/','/api/v1/red-flag','/api/v1/red-flag/<identifier>')
api.add_resource(User,'/api/v1/user/<identifier>')

