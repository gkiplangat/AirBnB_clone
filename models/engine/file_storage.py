#!/usr/bin/python3
"""This module contains the definition of a FileStorage class"""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """..."""

    __file_path: str = "file.json"
    __objects: dict = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State,
    }

    def all(self) -> dict:
        """..."""
        return type(self).__objects

    def new(self, obj: object) -> None:
        """..."""
        obj_name = obj.__class__.__name__
        key: str = f"{obj_name}.{obj.id}"
        type(self).__objects[key] = obj

    def save(self) -> None:
        """..."""
        objs = {
            key: value.to_dict() for key, value in type(self).__objects.items()
        }
        with open(type(self).__file_path, mode="w", encoding="utf-8") as file:
            json.dump(objs, file)

    def reload(self) -> None:
        """..."""
        if os.path.exists(type(self).__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                new_obj_dict = json.load(file)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value["__class__"]](**value)
                self.__objects[key] = obj