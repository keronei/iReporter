"""
This file receives and serves requests as api endpoints.
"""
from flask import request, jsonify, Response
from flask_restful import Resource
import json
from ..models.user_model import UserModel
from ..models.incidence import Incidence, IncidenceSchema
from ..models.red_flags import RedFlagSchema, RedFlag
from ..models.incidence_type import IncidenceType 

incidence_s = IncidenceSchema(many=True)
incidence = RedFlagSchema()


class UserView(Resource):

    """
    This class receives and serves requests as api endpoints.
    """
    def __init__(self):
        """Instantiate the db as the database"""
        self.database = "ker"
        self.model = UserModel()
    def get(self, identifier=None):
        """
        Serves the GET request, But checks if any param is given in order to determine
        if its a single entry request or all
        """
        self.add_user(request.get_json()) 
        return incidence.dump(raw_single)
        #return result
               
    def post(self):
        """Sets new data to database(Dict)"""
        
        result = self.model.add_user(request.get_json())
        
        return self.custom_response({"data": result}, 200)
        
    def custom_response(self,res, status_code):
        """
        Custom Response Function
        """
        return Response(
          mimetype="application/json",
          response=json.dumps(res),
          status=status_code
        )
class User(Resource):
    """User view handler"""
    def __init__(self):
        self.runs = "Waiting for name.."
    def get(self, name):
        """Retrieves the available entry identified by name"""
        return name