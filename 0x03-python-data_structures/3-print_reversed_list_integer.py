#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if len(my_list) != 0:
        length = (len(my_list) - 1)
        while(length >= 0):
            print("{:d}".format(my_list[length]))
            length -= 1
