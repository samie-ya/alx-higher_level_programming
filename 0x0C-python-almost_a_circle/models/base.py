#!/usr/bin/python3
"""Defining the class Base"""


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
