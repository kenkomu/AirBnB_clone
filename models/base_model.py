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
        """Returns a dictionary representation of an instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )
