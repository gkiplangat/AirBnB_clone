#!/usr/bin/python3
""" 
    Task: 9. More classes!
    Create the Review Module
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """ 
        Review class inherits from BaseModel
        Manage review objects
    """

    place_id = ""
    user_id = ""
    text = ""