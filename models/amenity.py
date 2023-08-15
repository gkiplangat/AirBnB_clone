#!/usr/bin/python3

"""
    Task: 9. More classes!
    Create the Amenity Module
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity class inherits from BaseModel
        Manage amenity objects
    """
    name = ""
    