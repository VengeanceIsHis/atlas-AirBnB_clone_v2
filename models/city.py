#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
import uuid

class City(BaseModel):
    """ The city class, contains state ID and name """
    def __init__(self):
        self.id = str(uuid.uuid4())
    state_id = ""
    name = ""
