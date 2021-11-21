#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    new_list = my_list
    if idx < 0:
        return new_list
    elif idx >= len(new_list):
        return new_list
    else:
        for i in range(len(new_list)):
            if i == idx:
                del new_list[i]
                return new_list
