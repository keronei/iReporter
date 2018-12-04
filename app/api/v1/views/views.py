"""
This file receives and serves requests as api endpoints.
"""
from flask import request, json, Response
from flask_restful import Resource
from ..models.models import IncidenceModel
from ..models.red_flags import RedFlagSchema

class iReporterFlags(Resource, IncidenceModel):
    """
    This class receives and serves requests as api endpoints.
    """
    def __init__(self):
        """Instantiate the dict as the database"""
        self.database = IncidenceModel()
    def get(self, identifier=None):
        """
        Serves the GET request, But checks if any param is given in order to determine
        if its a single entry request or all
        """
        if identifier is None:
             
             return self.custom_response({'data': self.get_incidences(), 'status':200}, 200) 
        
        return self.custom_response({'data': self.get_incidence_by_id(identifier) ,'status':200}, 200)
    def put(self,identifier=None):
        """Implements update to an entry"""
        if identifier is None:
            return self.custom_response({'status': 200, 'data': 'Identifier required <id>'}, 200)
        self.database.update_entry(identifier,request.get_json())
        return self.custom_response({'status': 200, 'data': 'Updated'}, 200)
    def post(self):
        """Sets new data to database(Dict)"""
        received_data = request.get_json()
        print(received_data)
        count = 0
        for entry in received_data:
            count += 1
        if count < 7:
            return self.custom_response({'status': 200, 'data': 'Less params.'}, 200)
            
        flags = RedFlagSchema().load(received_data)
     
        self.database.add_incidence(flags.data)
        return self.custom_response({'status': 204, 'data': 'Created'}, 200)
        
    def delete(self, identifier=None):
        """Basically removes a single entry provided by the id as identify"""
        if identifier is None:    
            return self.custom_response({'status': 200, 'data': 'Identifier required <id>'}, 200)
        self.database.remove_entry(identifier)
        return self.custom_response({'status': 200, 'data': 'Deleted'}, 200)
    
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
    def get(self, identifier):
        """Retrieves the available entry identified by name"""
        return identifier