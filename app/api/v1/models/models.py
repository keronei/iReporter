"""This file is the model that handle requests from views. Manipulates the Dict accordingly"""
from .red_flags import RedFlagSchema, RedFlagSchemaUpdate
from .incidence_type import IncidenceType

INCIDENCE = []

class IncidenceModel():
    """Handles the requests from exposed endpoints"""
    def __init__(self):
        self.database = INCIDENCE
    def add_incidence(self, data):
        """Adds a new entry of flag"""
        self.database.append(data)
        return "Saved", 201
    def get_incidences(self):
        """Returns all flag entries"""
        schema = RedFlagSchema(many=True)
        flags = schema.dump(
            filter(lambda i: i.type == IncidenceType.REDFLAG, INCIDENCE)
        )
        return {"Status":200, "Data":schema.dump(INCIDENCE)}
    def get_incidence_by_id(self, identifier):
        """Gets a single entry of of flag recognized by id"""
        flags = self.get_entry_helper(identifier)
        return {"Status":200, "Data":flags} 
    def update_entry(self, identifier, data):
        """Ofcourse updates a single entry identified by id"""
        hack = self.get_entry_helper(identifier)
        final = hack[0]
        #first merge to get one bit
        schema = RedFlagSchema(many=True)
        updated_dict = self.manual_update_helper(final, data)
        #remove the old entry
        old_entry = RedFlagSchemaUpdate().load(final)
        #determine the index...
        flags = schema.dump(INCIDENCE)
        old_ = schema.dump(old_entry).data[0]
        index = flags.data.index(old_)
        #add the new & updated dict!
        objected = RedFlagSchemaUpdate().load(updated_dict)
        #flags.data.pop(index)
        INCIDENCE.pop(index)
        #self.database = flags.data
        INCIDENCE.append(objected.data)
        return updated_dict, 200
    def manual_update_helper(self, dict_one, dict_two):
        """Manually updates the dictionary by flipping and re-assigning"""
        fin = dict_one.copy()
        fin.update(dict_two)
        return fin
    #need to dry-run this code!
    def find_index(self, identifier):
        """Takes in an id of an entry in dict, then returns its location in the list as Index"""
        hack = self.get_entry_helper(identifier)
        final = hack[0]
        #first merge to get one bit
        schema = RedFlagSchema(many=True)
        #determine the index...
        flags = schema.dump(INCIDENCE)
        index = flags.data.index(final)
        return index
    def get_entry_helper(self,identifier):
        """Dumps the dicts and gets the required entry identified by id"""
        schema = RedFlagSchema(many=True)
        flags = schema.dump(
            filter(lambda i: i.id == int(identifier), INCIDENCE)
        )
        return flags.data
    def remove_entry(self, identifier):
        """Removes a single entry identifieid by id"""
        INCIDENCE.pop(self.find_index(identifier))
        return "OK", 200
    