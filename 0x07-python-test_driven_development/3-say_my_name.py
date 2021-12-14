#!/usr/bin/python3
"""Defining say_my_name"""


def say_my_name(first_name, last_name=""):
    """This function is used to take the parameters given
       and uses them to create a first name and last name.

       Args:
           first_name (str): the first name to be used
           last_name (str): the last name to be used
    """
    if not(type(first_name) is str):
        raise TypeError("first_name must be a string")
    if not(type(last_name) is str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
