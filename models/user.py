#!/usr/bin/python3
""" module containing User class """
from models.base_model import BaseModel


class User(BaseModel):
    """Creating the User Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
