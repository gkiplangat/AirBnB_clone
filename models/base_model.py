#!/usr/bin/python3

import uuid
from datetime import datetime

from models import storage
import models


class BaseModel:
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

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def from_dict(cls, data_dict):
        if "__class__" in data_dict:
            class_name = data_dict.pop("__class__")
            if class_name == cls.__name__:
                return cls(**data_dict)
        return None
