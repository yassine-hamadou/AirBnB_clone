#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
       self.id = str(uuid4())
       self.created_at = datetime.now()
       self.updated_at = datetime.now()

    def __str__(self):
        string_representation = f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
        return string_representation

if __name__ == '__main__':
    my_model = BaseModel()
    print(my_model)
       
