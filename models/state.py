#!/usr/bin/python3

"""
    Task: 9. 9. More classes!
    Create the State Module
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
        State class inherits from BaseModel
        Manage state objects
    """
    name = ""
    