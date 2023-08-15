#!/usr/bin/python3

""" 
    Task: 9. More classes!
    Create the City Module
"""

from models.base_model import BaseModel

class City(BaseModel):
    """ 
        City class inherits from BaseModel
        Manage city objects
    """
    state_id = ""
    name = ""