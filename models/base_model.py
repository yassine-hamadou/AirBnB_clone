#!/usr/bin/python3
"""
This module contains the BaseModel class that defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    BaseModel that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        This is the object initializer
        """

        self.created_at = datetime.now()     
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key in kwargs.keys():
                if key != "__class__":
                    if (key == "created_at") or (key == "updated_at"):
                        print(f"hey {kwargs[key]}")
                        self.__dict__[f"{key}"] = datetime.fromisoformat(kwargs[key])
                    else:
                        self.__dict__[f"{key}"] = kwargs[key]       
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            
    def __str__(self):
        """
        This method is called whenever a the print function is called on an object of this class
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the time of the of the object""" 
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        return a dictionary containing all keys/values of the instance
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat(timespec='microseconds')
        self.updated_at = self.updated_at.isoformat(timespec='microseconds')
        return self.__dict__

