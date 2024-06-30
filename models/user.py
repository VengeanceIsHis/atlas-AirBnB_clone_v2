#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
class User(BaseModel):
    """This class defines a user by various attributes"""
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.password = kwargs.get('password', None)
        self.email = kwargs.get('email', None)
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def to_dict(self):
        dictionary = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        return dictionary