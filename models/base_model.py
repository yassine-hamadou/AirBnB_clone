#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
       self.id = str(uuid4())
       self.created_at = datetime.now()
       self.updated_at = datetime.now()

    def __str__(self):
        self.string_representation = f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
        return self.string_representation

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__


