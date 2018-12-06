"""
This file receives and serves requests as api endpoints.
"""
from flask import request, jsonify, Response
from flask_restful import Resource
from validate_email import validate_email
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
        received_data = request.get_json()
        count = 0
        for entry in received_data:
            count += 1
        if count < 6:
            return self.custom_response({'status': 200, 'data': 'Less params.'}, 200)
        if self.validator(received_data):
            result = self.model.add_user(received_data)
            return Helper.custom_response({"data": result}, 200)
        return self.custom_response({'status': 200, 'data': 'Your credentials were invalid.'}, 200)
     
        
    def validator(self, json_data):
        """Check all the values in json and assign back to error,
        Finally, the result would remain in error as bool"""
        formated = json.dumps(json_data)
        string_formatted = json.loads(formated)

        error_firstname = isinstance(string_formatted["firstname"], str)
        error_secondname = isinstance(string_formatted["secondname"], str)
        error_phone = isinstance(string_formatted["phoneNumber"], str)
        error_username = isinstance(string_formatted["username"], str)        
        is_valid = validate_email('example@example.com')
        
        if False in {error_firstname, error_secondname, error_phone, error_username, is_valid} :
           return False
        return True
        
class Helper():
    
    def custom_response(res, status_code):
        """
        Custom Response Function
        """
        return Response(
          mimetype="application/json",
          response=json.dumps(res),
          status=status_code
        )
    
