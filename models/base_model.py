#!/usr/bin/python3

import uuid
from datetime import datetime

""" Defines a base class that other class inherit from. """


class BaseModel:
    """ The base class """

    def __init__(self, *args, **kwargs):
        """ The class constructors that initialise instance """

        if kwargs:

            dfmt = "%Y-%m-%dT%H:%M:%S.%f"

            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], dfmt)

                if key != '__class__':
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            The print function of the class.

        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            Update "updated_at" with the current datetime.

        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all keys/value of
            __dict__ of the instance.
        """
        obj_dict = {}
        for key, value in self.__dict__.items():

            if key == "created_at" or key == "updated_at":
                obj_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")

            else:
                obj_dict[key] = value
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict
