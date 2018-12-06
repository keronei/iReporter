"""
This file receives and serves requests as api endpoints.
"""
from flask import request, jsonify, Response
from flask_restful import Resource
import json
from ..models.user_model import UserModel

class UserView(Resource):

    """
    This class receives and serves requests as api endpoints.
    """
    def __init__(self):
        """Instantiate the db as the database"""
        self.model = UserModel()
               
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
