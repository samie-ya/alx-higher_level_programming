#!/usr/bin/python3
"""Defining the class MyInt"""


class MyInt(int):
    """This is MyInt class"""

    def __init__(self, value):
        """This function initilizes MyInt"""
        super().__init__()
        self.value = value

    def __eq__(self, other):
        """This function reverses the meaning of equality.

           Args:
               self (int): the value of the class
               other (int): value of the other class

           Returns:
               False if they are equal else True
        """
        if (self.value == other):
            return False
        return True

    def __ne__(self, other):
        """This function reverses the meaning of inequality.

           Args:
               self (int): the value of the class
               other (int): value of the other class

           Returns:
               False if they are inequal else True
        """
        if (self.value != other):
            return False
        return True
