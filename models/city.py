#!/usr/bin/python3
"""Contains the City model"""
from models.base_model import BaseModel


class City(BaseModel):
    """Implements the City class"""
    def __init__(self, state_id = "", name = "", *args, **kwargs):
        super(City, self).__init__(*args, **kwargs)
        self.state_id = state_id
        self.name = name

    def __str__(self):
        return f'City({self.state_id},{self.name})'
