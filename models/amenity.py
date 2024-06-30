#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel
import uuid


class Amenity(BaseModel):
    def __init__(self):
        self.id = str(uuid.uuid4())
    name = ""
