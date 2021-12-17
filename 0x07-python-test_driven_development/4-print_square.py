#!/usr/bin/python3
"""Defining the function print_square"""


def print_square(size):
    """This function is used to take the parameter
       and make a square using #

       Args:
           size (int): the height and width of square
    """
    if not(type(size) is int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif (not(type(size) is float) and size < 0):
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
