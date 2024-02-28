#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances."""

    __filepath = "file.json"
    __objects = {}

    @property
    def objects(self):
        return FileStorage.__objects
    
    @objects.setter
    def objects(self, value):
        FileStorage.__objects = value

    @property
    def filepath(self):
        return FileStorage.__filepath
    
    @filepath.setter
    def filepath(self, value):
        FileStorage.__filepath = value

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        with open(FileStorage.__filepath, "w") as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            """with open(FileStorage.__file_path, "r") as file:
                serialized = json.load(file)
                for key, value in serialized.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)"""
            with open(FileStorage.__filepath) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
