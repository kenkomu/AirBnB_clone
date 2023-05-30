#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes:
"""

import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    def update(self):
        self.updated_at = datetime.now()
    def save(self):
        self.update()
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
base_model = BaseModel()
base_model.save()
obj_dict = base_model.to_dict()
print(obj_dict)