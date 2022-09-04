#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A base class for other classes
    defines all attributes/method
    all subclasses could inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        A class constructor
        initializes the private instance variables
        assigns new values to the variables
        if no kwargs was passed
        sets the **kwargs if it exists
        using iteration
        self.kwargs[key] = value
        """

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
        string = "[{}] ({}) {}".format(
                type(self).__name__,
                self.id, self.__dict__)
        return string

    def save(self):
        """
        A base class that updates the "self.updated_at"
        to the current time when the object was saved
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        A method that returns a dictionary
        containing all keys/values of __dict__ instance
        with some added parameters
        A key __class__ added
        Created_at and Updated_at:
            converted to string object in ISO format using .isoformat()
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
