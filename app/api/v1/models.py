
from .red_flags import RedFlag, RedFlagSchema
from .incidence_type import IncidenceType

incidence = [
    #RedFlag(32,"7770,-452","pending",['image.png','face.jpg'],['movie.mp4','clip.mov'],"Waiting")
]

class IncidenceModel():
    def __init__(self):
        self.database = incidence
        
    def addIncidence(self,data):
        
        self.database.append(data)
        return "Saved",201
    
    def getIncidences(self):
        schema = RedFlagSchema(many=True)
        
        flags = schema.dump(
            filter(lambda i: i.type == IncidenceType.REDFLAG,incidence)
        )
        return { "Status":200,"Data":flags.data }
    
    def getSingleIncidence(self,id):
        return id, "request received"
    
    def updateEntry(id):
        return id ,"Updating"
    