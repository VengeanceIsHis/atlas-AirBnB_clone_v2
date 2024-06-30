#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import uuid

class State(BaseModel):
    """ State class """
    def __init__(self, *args):
        self.id = str(uuid.uuid4())
        self.name = find_name(args[2])
def find_name(string):
        parts = string.split('=')
        if len(parts) >= 2:
            return parts[1].strip()
