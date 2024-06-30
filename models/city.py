#!/usr/bin/python3
""" City Module for HBNB project """


from models.base_model import BaseModel, Base
import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities' 
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.name = kwargs.get('name', None)
        self.state_id = kwargs.get('state_id', None)
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def to_dict(self):
        dictionary = {
            '__class__': type(self).__name__,
            'id': self.id,
            'name': self.name,
            'state_id': self.state_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        return dictionary
