#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] is search:
            new_list.remove(new_list[i])
            new_list.insert(i, replace)
    return new_list
