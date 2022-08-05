#!/usr/bin/python3
"""Contains the Place model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implements the Place model
    Args:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """
    def __init__(self, city_id="", user_id="", name="", description="",
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0,
                 amenity_ids=[], *args, **kwargs):
        super(Place, self).__init__(*args, **kwargs)
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.lattitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids

    def __str__(self):
        return f'Place({self.city_id}, {self.user_id}, {self.name},\
             {self.description}, {self.number_rooms}, {self.number_bathrooms},\
                {self.max_guest}, {self.price_by_night}, {self.lattitude},\
                     {self.longitude}, {self.amenity_ids})'
