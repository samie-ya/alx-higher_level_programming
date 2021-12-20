#!/usr/bin/python3
"""Defining a look up"""


def lookup(obj):
    """This function returns all the list of available
       attributes and methods of object"""
    return list(dir(obj))
