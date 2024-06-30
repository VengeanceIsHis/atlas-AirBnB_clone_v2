#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
import uuid

class Place(BaseModel):
    """ A place to stay """
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.city_id = kwargs.get('city_id', None)
        self.user_id = kwargs.get('user_id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.number_rooms = kwargs.get('number_rooms', None)
        self.number_bathrooms = kwargs.get('number_bathrooms', None)
        self.max_guest = kwargs.get('max_guest')
        self.price_by_night = kwargs.get('price_by_night')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude', None)
    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {
            '__class__': type(self).__name__,
            'id': self.id,
            'city_id': self.city_id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'number_rooms': self.number_rooms,
            'number_bathrooms': self.number_bathrooms,
            'max_guest': self.max_guest,
            'price_by_night': self.price_by_night,
            'latitude': self.latitude,
            'longitude': self.longitude
                }
        return dictionary