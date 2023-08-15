#!/usr/bin/python3

""" 
    Task: 8. First User
    User Module
"""

from models.base_model import BaseModel

class User(BaseModel):
    """ User class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
