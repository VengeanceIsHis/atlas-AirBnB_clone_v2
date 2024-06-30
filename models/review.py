#!/usr/bin/python3
""" Review module for the HBNB project """


from models.base_model import BaseModel
import uuid


class Review(BaseModel):
    """ Review classto store review information """
    def __init__(self):
        self.id = str(uuid.uuid4())
    place_id = ""
    user_id = ""
    text = ""
