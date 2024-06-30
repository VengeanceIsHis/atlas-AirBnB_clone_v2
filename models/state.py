#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import uuid

class State(BaseModel):
    """ State class """
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.name = kwargs.get('name', None)
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())