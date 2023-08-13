#!/usr/bin/python3
import json


class FileStorage:
    """
        serializes instances to a JSON file and 
        deserializes JSON file to instances
        
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value['__class__']
                    cls = globals()[cls_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
