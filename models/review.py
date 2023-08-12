#!/usr/bin/python3
""" Module containing a Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """creating the class"""

    place_id = ""
    user_id = ""
    text = ""
