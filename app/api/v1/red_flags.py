from marshmallow import post_load
from .incidence import Incidence, IncidenceSchema
from .incidence_type import IncidenceType 

class RedFlag(Incidence):
    def __init__(self,CreatedBy,location,status,Images,Videos,comment):
        super(RedFlag,self).__init__(CreatedBy,location,status,Images,Videos,comment,IncidenceType.REDFLAG)
        
    def __repr__(self):
        return '<RedFlag(CreatedBy={self.CreatedBy!r})>'.format(self=self)
    
    
class RedFlagSchema(IncidenceSchema):
    @post_load
    def make_red_flag(self,data):
        return RedFlag(**data)