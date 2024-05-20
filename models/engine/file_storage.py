""" This module defines a class FileStorage that
uses for storing and retrieving data."""

# !/usr/bin/python3
from models.base_model import BaseModel
import json
import os


class FileStorage:
    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        """Return all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize the dictionary __objects to a JSON file."""
        with open(self.__file_path, 'w') as f:
            temp_dict = {
                    key: obj.to_dict() for key, obj in self.__objects.items()
                }
            json.dump(temp_dict, f)

    def reload(self):
        """ Deserialize the JSON string from the
        JSON file if a path is given. """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    loaded_objects = json.load(f)
                    for key, val in loaded_objects.items():
                        class_name = val["__class__"]
                        cls = globals().get(class_name, None)
                        if cls:
                            self.__objects[key] = cls(**val)
                except json.JSONDecodeError:
                    pass
