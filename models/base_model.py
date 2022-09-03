#!/usr/bin/python3
"""
This module contains the BaseModel class that defines all common
attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel"""

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Prints a string representaion of object."""
        string = "[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__)
        return string

    def save(self):
        """Save method updates the public instance attribute `updated_at` """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns diction representation of the object
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1

