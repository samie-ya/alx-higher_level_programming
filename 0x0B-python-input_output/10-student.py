#!/usr/bin/python3
"""Defining class Student"""


class Student:
    """This is a class called Student"""

    def __init__(self, first_name, last_name, age):
        """This is function initilizes the class Student.

           Args:
               first_name (str): the first name
               last_name (str): the last name
               age (int): the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function is used to retreive the dictionary
           representation of student instance

           Args:
               attrs (str): attributes

           Returns: those attributes in attrs only
        """
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i not in self.__dict__:
                    attrs.remove(i)
                    if (attrs is None):
                        return {}
                    return {i: self.__dict__[i] for i in attrs}
                else:
                    return {i: self.__dict__[i] for i in attrs}
