#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    lists = my_list[:]
    if idx < 0:
        return lists
    elif idx >= len(lists):
        return lists
    else:
        for i in range(len(lists)):
            if i == idx:
                lists.pop(i)
                lists.insert(i, element)
                return lists
