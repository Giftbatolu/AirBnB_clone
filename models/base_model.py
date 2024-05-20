""" Thiss module define a base calss for all other future classes"""
#!/usr/bin/python3
import uuid
from datetime import datetime
#from models.__init__ import storage

class BaseModel():
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:

            # Delete the '__class__' key from kwargs if present 
            # it can't be in the loop cause size of dict chANGES
            # WHILE LOOPING and gives a runtime error
            if "__class__" in kwargs:
                del kwargs["__class__"]
            
            # updating the str time found in dictionary into time obj
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

            # Set the attribute value(tho we have made them objects
            # they arent instances yet & zis sets other attributes too like id.
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
    '''
    this is also possible
    def __init__(self, *args, **kwargs):
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    '''
    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """ updates the time of update_at with the curent time """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
    def to_dict(self):
        """
        converts instances to a dictionary
        we could have simply return self.__dict__ if we were
        not expected creat  a key and also modify exising keys
        """
        #creating an empty dictionary object
        dict_obj = {}
        #iterating though all the instances
        for key, value in self.__dict__.items():
            #checking if they are times/datetime (created and updated AT) and put them in isofromat
            if isinstance(value, datetime):
                dict_obj[key] = value.isoformat()
            else:           
                dict_obj[key] = value 
        # adding a new key "__class_" with the class name of the objectfor better identifcation (for fututre)
        dict_obj["__class__"] = type(self).__name__
        return dict_obj

