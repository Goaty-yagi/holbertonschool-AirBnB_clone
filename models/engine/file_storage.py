#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """Initialize class FileStorage"""

    @property
    def objects(self):
        return self.__objects
    
    @objects.setter
    def objects(self, value):
        self.__objects = value

    @property
    def filepath(self):
        return self.__file_path
    
    @filepath.setter
    def filepath(self, value):
        self.__file_path = value

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            """with open(FileStorage.__file_path, "r") as file:
                serialized = json.load(file)
                for key, value in serialized.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)"""
            with open(self.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
