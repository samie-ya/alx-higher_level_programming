#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    for i in list(a_dictionary):
        if i is key:
            del a_dictionary[i]
    return a_dictionary
