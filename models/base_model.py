#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
       self.id = str(uuid4())
       self.created_at = datetime.now()
       self.updated_at = datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat(timespec='microseconds')
        self.updated_at = self.updated_at.isoformat(timespec='microseconds')
        return self.__dict__

