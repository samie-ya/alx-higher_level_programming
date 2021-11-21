#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list) - 1
    if len(my_list) == 0:
        return
    while length > 0:
        i = 0
        while i < length:
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
            i += 1
        return my_list[length]
        length -= 1
