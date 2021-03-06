import datetime as dt
from marshmallow import Schema, fields

class Incidence():
    
    def __init__(self,id,CreatedBy,location,status,Images,Videos,comment,type):
          
        self.CreatedOn = dt.datetime.today().strftime("%d %B %Y %H:%M")
        self.CreatedBy = CreatedBy
        self.type = type
        self.id = id
        self.location = location
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment
        
class IncidenceSchema(Schema):
    
    CreatedBy = fields.Integer()
    CreatedOn = fields.Str()
    location = fields.Str()
    status = fields.Str()
    Images = fields.List(fields.String, attribute='Images')
    Videos = fields.List(fields.String, attribute='Videos')
    comment = fields.Str()
    type = fields.Str()
    id = fields.Integer()