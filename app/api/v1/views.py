from flask_restful import Api,Resource
from .models import IncidenceModel, incidence
from .red_flags import RedFlag, RedFlagSchema
from flask import jsonify, request
from .incidence_type import IncidenceType

class iReporter(Resource, IncidenceModel):
    def __init__(self):
        self.database = IncidenceModel()
        
    def get(self):
       
        return self.getIncidences()
        
    def post(self):
        flags = RedFlagSchema().load(request.get_json())
        self.database.addIncidence(flags.data)
        return 'OK',204
        