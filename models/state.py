#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if models.storage_selection == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")

    if models.storage_selection == 'file':
        @property
        def cities(self):
            from models import storage
            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return (city_list)

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
