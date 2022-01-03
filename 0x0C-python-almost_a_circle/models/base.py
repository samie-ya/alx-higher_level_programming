#!/usr/bin/python3
"""Defining the class Base"""
import json


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
        new_list = []
        for i in list_objs:
            new_list.append(i.to_dictionary())
            file_name = type(i).__name__ + ".json"
        with open(file_name, "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(new_list))
