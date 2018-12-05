from marshmallow import post_load
from .incidence import Incidence, IncidenceSchema
from .incidence_type import IncidenceType 

class RedFlag(Incidence):
    def __init__(self,id,CreatedBy,location,status,Images,Videos,comment):
        super(RedFlag,self).__init__(id,CreatedBy,location,status,Images,Videos,comment,IncidenceType.REDFLAG)
        


class RedFlagUpdate():
    def __init__(self,id,CreatedBy,CreatedOn,location,status,Images,Videos,comment,type):
        self.CreatedOn = CreatedOn
        self.CreatedBy = CreatedBy
        self.type = type
        self.id = id
        self.location = location
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment
           
    
class RedFlagSchema(IncidenceSchema):
    @post_load
    def make_red_flag(self,data):
        return RedFlag(**data)
    
class RedFlagSchemaUpdate(IncidenceSchema):
    @post_load
    def make_red_flag(self,data):
        return RedFlagUpdate(**data)    