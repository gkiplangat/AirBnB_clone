#!/usr/bin/python3
"""
This module contains the BaseModel class that defines all common
attributes/methods for other classes.
"""
from datetime import datetime
import uuid

import models


class BaseModel:
    """This defines a BaseModel class"""

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        """..."""
        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    val = datetime.strptime(str(value), "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

        # self.save()

    def save(self) -> None:
        """
        Save the object by updating the `updated_at` attribute with
        the current datetime. This function does not take any
        parameters and does not return anything.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object, including
            the class name, created_at, and updated_at attributes.
        """
        # date_format: str = "%Y-%m-%dT%H:%M:%S.%f"
        properties: dict = self.__dict__.copy()
        properties["__class__"] = self.__class__.__name__
        # properties["created_at"] = self.created_at.strftime(date_format)
        # properties["updated_at"] = self.updated_at.strftime(date_format)
        properties["created_at"] = self.created_at.isoformat()
        properties["updated_at"] = self.updated_at.isoformat()

        return properties

    def __str__(self) -> str:
        """..."""
        classname = self.__class__.__name__
        return f"[{classname}] ({self.id}) {self.__dict__}"