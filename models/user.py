#!/usr/bin/python3
"""Implements the user's model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from the BaseModel class and add user's functionalities
    Args:
        email (str): the email of the user
        password (str): the password of the user
        first_name (str): the first name of the user
        last_name (str): the last name of the user
    """
    def __init__(self, email="", password="",
                 first_name="", last_name="", *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'User({self.email}, {self.password},\
            {self.first_name}, {self.last_name})'
