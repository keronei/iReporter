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
        
        
    def __repr__(self):
        #return '<Incidence(id={self.id!r})>'.format(self=self)
        return '<Status %r>'%self.status
    
class IncidenceUpdate():
    
    def __init__(self,id,CreatedBy,location,status,Images,Videos,comment,CreatedOn,type):
        self.CreatedOn = CreatedOn
        self.CreatedBy = CreatedBy
        self.type = type
        self.id = id
        self.location = location
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment
        
        
    def __repr__(self):
        #return '<Incidence(id={self.id!r})>'.format(self=self)
        return '<Status %r>'%self.status
    def id_gen():
        fake_id += 1
        
        return fake_id
    
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