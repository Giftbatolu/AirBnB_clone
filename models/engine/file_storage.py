""" This module defines a class FIlestorage that uses for storing and retiving data """
#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os

class FileStorage:
    def __init__(self, file_path = "file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self.__objects
        #self.__dict__.__objects
    def new(self, obj):
        #for eac_obj in self.objects:
            #setattr(self, each_obj, obj)
            self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj
    def save(self):
        """ serlialize the dictionary __object to Json file  """
        #json.dump(__object, my_jsonfile.json)
        with open(self.__file_path, 'w') as f:
            temp_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(temp_dict, f)
    def reload(self):
        """ decerilize the json string from the json file if a path is given """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:    
                    loaded_objects = json.load(f)
                    for key, val in loaded_objects.items():
                        #self.new(v)
                        class_name = val["__class__"]
                        cls = globals().get(class_name, None)
                        if cls:
                            self.__objects[key] = cls(**val)
                except json.JSONDecodeError:
                    pass


#my_file_storage = FileStorage(file_path="/path/to/file", objects={})
#print(my_file_storage._file_path)  # Accessing private variable
#print(my_file_storage._objects)  # Accessing private variable
