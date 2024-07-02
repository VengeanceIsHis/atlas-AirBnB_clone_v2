#!/usr/bin/python3
""" Review module for the HBNB project """


from models.base_model import BaseModel, Base
import uuid
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __table__ == 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    def __init__(self):
        self.id = str(uuid.uuid4())
    place_id = ""
    user_id = ""
    text = ""
