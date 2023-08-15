#!/usr/bin/python3

"""
    Task: 8. First User
    Create the User Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        User class inherits from BaseModel.
        Manage user objects.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    