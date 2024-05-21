#!/usr/bin/python3

""" Defines the FileStorage class """

from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
        The FileStorage class that serialize and deserialize the json file.

        Attributes:
                __file_path (str) - The path to the json file.
                __object (dict) - Dictionary that store the object.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return all objects. """
        return FileStorage.__objects

    def new(self, obj):
        """
            Add new object to the storage sets obj with key <obj class name>.id

        """
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """
            Serialize the dictionary __objects to a JSON file.
        """
        with open(FileStorage.__file_path, 'w') as obj_f:
            temp_dict = {
                    key: obj.to_dict() for key, obj in self.__objects.items()
                }
            json.dump(temp_dict, obj_f)

    def reload(self):
        """
            Deserialize the JSON string from the JSON file if a path is given.

        """
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, 'r') as obj_f:
                try:
                    loaded_objects = json.load(obj_f)
                    for key, val in loaded_objects.items():
                        class_name = val["__class__"]
                        cls = globals().get(class_name, None)
                        if cls:
                            self.__objects[key] = cls(**val)
                except json.JSONDecodeError:
                    pass
