"""
This file receives and serves requests as api endpoints.
"""
from flask import request
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
             return self.get_incidences()
        return self.get_incidence_by_id(identifier)
    def put(self,identifier):
        """Implements update to an entry"""
        return self.database.update_entry(identifier,request.get_json())         
    def post(self):
        """Sets new data to database(Dict)"""
        flags = RedFlagSchema().load(request.get_json())
        self.database.add_incidence(flags.data)
        return 'OK', 204
    def delete(self, identifier):
        """Basically removes a single entry provided by the id as identify"""
        return self.database.remove_entry(identifier)     
class User(Resource):
    """User view handler"""
    def __init__(self):
        self.runs = "Waiting for name.."
    def get(self, name):
        """Retrieves the available entry identified by name"""
        return name