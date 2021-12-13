#!/usr/bin/python3
"""Defining Rectangle"""


class Rectangle:
    """This is used to create an instance Rectangle"""

    def __init__(self, width=0, height=0):
        """This function is used to initialize the instance.

           Args:
               width (int): the width of rectangle
               height (int): the height of rectangle
        """
        if not(isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        elif not(isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This function is used to change the value of
           private attribute width to value given in setter
           function.

           Args:
               value (int): the new value of width

           Returns:
               the new value
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This function is used to change the value of
           private attribute height to value given in setter
           function.

           Args:
               value (int): the new value of height

           Returns:
               the new value
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This function is used to return the product
           of height and width
        """
        return self.__width * self.__height

    def perimeter(self):
        """This function is used to return the sum
           of all sides of the rectangle
        """
        if ((self.__width == 0) or (self.__height == 0)):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """This function is used to return the string
           representation of the rectangle in the form
           of '#'
        """
        new_string = ""
        if ((self.__width == 0) or (self.__height == 0)):
            return new_string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new_string += "#"
                new_string += "\n"
            return new_string.rstrip()
