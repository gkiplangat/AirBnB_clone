#!/usr/bin/python3
"""
This module contains the BaseModel class that defines all common
attributes/methods for other classes.
"""
from datetime import datetime
import uuid


class BaseModel:
    """This defines a BaseModel class"""

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(
                        self,
                        key,
                        datetime.strptime(str(value), "%Y-%m-%dT%H:%M:%S.%f"),
                    )
                else:
                    setattr(self, key, value)
        else:
            self.id: str = str(uuid.uuid4())
            self.created_at: datetime = datetime.now()

        self.save()

    def __str__(self) -> str:
        return f"{[self.__class__.__name__]} ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        Save the object by updating the `updated_at` attribute with
        the current datetime. This function does not take any
        parameters and does not return anything.
        """
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Converts the object to a dictionary representation.
        Returns:
            dict: A dictionary representation of the object, including
            the class name, created_at, and updated_at attributes.
        """
        form: str = "%Y-%m-%dT%H:%M:%S.%f"
        properties: dict = self.__dict__
        properties["__class__"] = self.__class__.__name__
        properties["created_at"] = self.created_at.strftime(form)
        properties["updated_at"] = self.updated_at.strftime(form)
        # properties["created_at"] = datetime.isoformat(self.updated_at, form)
        # properties["updated_at"] = datetime.isoformat(self.updated_at, form)

        return properties
