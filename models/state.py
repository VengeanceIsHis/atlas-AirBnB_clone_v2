#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import uuid
from datetime import datetime
class State(BaseModel):
    """ State class """
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.name = kwargs.get('name', None)
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {
            '__class__': type(self).__name__,
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        return dictionary