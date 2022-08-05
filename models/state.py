#!/usr/bin/python3
"""A module containing the State model"""
from models.base_model import BaseModel


class State(BaseModel):
    """Implements the State model for any state object"""
    def __init__(self, name="", *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        return f'State({self.name})'
