#!/usr/bin/python3
"""Defining the function inherits_from"""


def inherits_from(obj, a_class):
    """This function checks if obj is instance or
       inheritance of a_class directly or indirectly

       Args:
           obj (class): the class instane
           a_class (class): the class to compare to

       Returns:
           if obj is an instance then true else false
    """
    if (isinstance(obj, a_class) and type(obj) != a_class):
        return True
    return False
