#!/usr/bin/python3
"""
class BaseModel that defines
"""


import uuid
from datetime import datetime
from models import storage

from models.__init__ import storage


class BaseModel:
    def save(self):
        """Updates the public instance attribute updated_at with the current datetime and calls save() method of storage."""
        self.updated_at = datetime.now()
        storage.save()

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel. If not from a dictionary representation, calls new() method on storage."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
