#!/usr/bin/python3
"""Defining a locked class"""


class LockedClass:
    """This class is used to create a dynamic creation
       of attributes. only those mentioned in list can be
       created"""
    __slots__ = ['first_name']

    def __init__(self, name=None):
        """This function is used to initialize the class

           Args:
                name (str): the value of first name"""
        self.first_name = name
