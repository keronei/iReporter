
from .models.user_model import UserModel
from .views.user_view import UserView, UserLogin
from flask_restful import Api, Resource

from flask import Blueprint


version_two = Blueprint('api_v2',__name__)

api = Api(version_two)

api.add_resource(UserView,'/','/api/v2/auth/signup')
api.add_resource(UserLogin,'/','/api/v2/auth/signin')



