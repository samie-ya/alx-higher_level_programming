#!/usr/bin/python3
"""Defining MagicClass"""
import math


class MagicClass:
    """MagicClass is used to show circle circuma nd area"""
    def __init__(self, radius=0):
        """This function is used to initilize MagicClass
           Args:
                radius (int): radius of a circle"""
        self.__radius = radius
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError("radius must be a number")

    def area(self):
        """This funcnction is used to find area
           of a circle"""
        return (math.pi * self.__radius**2)

    def circumference(self):
        """This function is used to find circumference"""
        return ((2 * math.pi) * self.__radius)
