#!/usr/bin/python3

"""
    Task: 9. More classes!
    Create the Place Module
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
        Place class inherits from BaseModel
        Manage place objects
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    