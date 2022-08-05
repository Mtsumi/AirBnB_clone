#!/usr/bin/python3
"""Contains the Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implements the Review model"""
    def __init__(self, place_id="", user_id="", text="", *args, **kwargs):
        super(Review, self).__init__(*args, **kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

    def __str__(self):
        return f'Review({self.place_id}, {self.user_id}, {self.text})'
