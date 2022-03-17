#!/usr/bin/python3
"""This finds the largest number"""


def find_peak(list_of_integers):
    """This function finds largest number"""
    if list_of_integers:
        large = 0
        for n in list_of_integers:
            if n > large:
                large = n
        return large
    return None
