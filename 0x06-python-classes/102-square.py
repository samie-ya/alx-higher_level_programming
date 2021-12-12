#!/usr/bin/python3
"""Defining Square in class"""


class Square:
    """This is class is to compute area of a square"""
    def __init__(self, size=0):
        """Class is initialized with a field named size.

        Args:
            size (int): size is a new field it has been initialized to 0.
        """
        self.__size = size
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

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

    def __eq__(self, other):
        """This function is used to check if area of
           instances is equal

           Args:
               self: represents one instance Square
               other: represents other instance of Square
           Returns:
               if they are equal true, else false
        """
        if (self.area() == other.area()):
            return True
        return False

    def __ne__(self, other):
        """This function is used to check if area of
           instances is not equal

           Args:
               self: represents one instance Square
               other: represents other instance of Square
           Returns:
               if they are not equal true, else false
        """
        if (self.area() != other.area()):
            return True
        return False

    def __lt__(self, other):
        """This function is used to check if area of
           first instances is less than the other

           Args:
               self: represents one instance Square
               other: represents other instance of Square
           Returns:
               if first is less, then true, else false
        """
        if (self.area() < other.area()):
            return True
        return False

    def __gt__(self, other):
        """This function is used to check if area of
           first instances is greater than the other

           Args:
               self: represents one instance Square
               other: represents other instance of Square
           Returns:
               if first is greater, then true, else false
        """
        if (self.area() > other.area()):
            return True
        return False

    def __le__(self, other):
        """This function is used to check if area of
           first instances is less than or equal to
           other

           Args:
               self: represents one instance Square
               other: represents other instance of Square
           Returns:
               if first is less than or equal, then true,
               else false
        """
        if (self.area() <= other.area()):
            return True
        return False

    def __ge__(self, other):
        """This function is used to check if area of
           first instances is greater than or equal to
           other

           Args:
               self: represents one instance Square
               other: represents other instance of Square
           Returns:
               if first is greater than or equal to then, true,
               else false
        """
        if (self.area() >= other.area()):
            return True
        return False
