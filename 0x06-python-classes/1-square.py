#!/usr/bin/python3
"""Defining Square in class"""


class Square:
    """This is class is to compute area of a square"""
    def __init__(self, size=0):
        """Class is initialized with a field named size.

        Args:
            size (float): size is a new field it has been initialized to 0.
        """
        self.__size = size
