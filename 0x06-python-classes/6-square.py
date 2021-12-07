#!/usr/bin/python3
"""Defining Square in class"""


class Square:
    """This is class is to compute area of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Class is initialized with a field named size and position.

        Args:
            size (int): size is a new field it has been initialized to 0.
            position (int): position is a new tuple field it has been
            initialized to 0
        """
        self.__size = size
        self.__position = position
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if ((position[0] < 0) or (position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This funtion is used to find the area of square.

        Returns:
            size squared
        """
        return self.__size**2

    @property
    def size(self):
        """This function is used to return  the value that
           was changed by the size setter function.
        Args:
            value (int): the value to be changed
        Returns:
            the new size
        """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """This function is used to return the value that
           was changed by position setter function.

        Args:
            value (int): the value of tuple to be changed.
        Returns:
            the new tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if ((position[0] < 0) or (position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """This function is used to print a square in form
        of # using the value given.
        """
        if (self.__size == 0):
            print()
        else:
            for l in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
