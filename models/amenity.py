#!/usr/bin/python3
"""Contains the Amenity model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Implements the Amenity model"""
    def __init__(self, name="", *args, **kwargs):
        super(Amenity, self).__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        return f'Amenity({self.name})'
