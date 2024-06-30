#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
import uuid
from datetime import datetime
class City(BaseModel):
    """ The city class, contains state ID and name """
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.name = kwargs.get('name', None)
        self.state_id = kwargs.get('state_id', None)
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())
