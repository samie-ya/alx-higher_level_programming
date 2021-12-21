#!/usr/bin/python3
"""Defining the class BaseGeometry"""


class BaseGeometry:
    """This is a BaseGeometry class"""

    def area(self):
        """This function is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function is used to validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is a Rectangle class"""

    def __init__(self, width, height):
        BaseGeometry.__init__(self)
        """This class is used to initiate the class rectangle.

           Args:
               width (int): the width of rectangle
               height (int): teh height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
