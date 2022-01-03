#!/usr/bin/python3
"""Defining the class Base"""
import json
from pathlib import Path


class Base:
    """This is a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This function is used to initialize a class.

           Args:
               id (int): id value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function sreturns the json string of list
           of dictionaries.

           Args:
               list_dictionaries (list): The dictionary used

           Returns:
               the json string
        """
        if (list_dictionaries is None) or (list_dictionaries is []):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This function write the json representation of list_obj
           to file

           Args:
               list_objs (list): the list of instances
        """
        new_list = []
        for i in list_objs:
            new_list.append(i.to_dictionary())
            file_name = type(i).__name__ + ".json"
        with open(file_name, "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """This function returns the list of json representation
           in json_string

           Args:
               json_string (str): string representation of list of
               dictionaries

           Returns:
               list of json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This function returns an instance with all attributes already set.

           Args:
               dictionary (dict): double pointer to dictionary

           Returns:
               returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            instance = cls(2, 3)
        if cls.__name__ == "Square":
            instance = cls(2)
        instance.update(**dictionary)
        return instance
