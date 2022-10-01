#!/usr/bin/python3
""" This module contain the file storage for the models"""
from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:
    """ This class serializes instances to a JSON file and
    deserializes JSON file to instances

    Attributes:
        __file_path: string - file path to JSON file
        __objects:  dictionary - empty but will store all objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ return the all the dictionary object """
        if cls:
            obj_same_type = {}
            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    obj_same_type[key] = obj
            return obj_same_type
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.update({key: obj})
            self.save()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict.update({key: value.to_dict()})
            #value.to_dict converts the value to json
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                data = (json.load(f))
                if data:
                    for key, value in data.items():
                        #convert back to class
                        value = eval(value["__class__"])(**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass
