#!/usr/bin/python3
"""Defining the class Base"""
import json
from pathlib import Path


class Base:
    """This is the class base

       Args:
           __nb_objects (int): private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This function will initialize the class Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function takes a list of ictionaries
           and returns the json representation

           Args:
               list_dictionaries (list): list of dictionaries

           Returns:
               json represenation
        """
        if list_dictionaries is None or list_dictionaries is []:
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
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                new_list = []
                for i in list_objs:
                    new_list.append(i.to_dictionary())
                f.write(Base.to_json_string(new_list))

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

    @classmethod
    def load_from_file(cls):
        """This file returns list of instance depending on the class"""

        file_name = cls.__name__ + ".json"
        path = Path(file_name)
        if path.is_file():
            with open(file_name, "r", encoding='utf-8') as f:
                list_of_dict = cls.from_json_string(f.read())
                new_list = []
                for i in list_of_dict:
                    new_list.append(cls.create(**i))
            return new_list
        else:
            return []
