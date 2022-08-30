#!/usr/bin/python3
import uuid import 
from datetime import datetime

class BaseModel:
    def __init__(self):
       self.id = str(uuid.uuid4())
       self.created_at = datetime.now()
       self.updated_at = datetime.now()

    def __str__(self):
        string_representation = f"[{self.__class__}] ({self.id}) {self.__dict__}"
        return string_representation
       
