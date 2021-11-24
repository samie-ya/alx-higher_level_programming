#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    for i in zip(set_1, set_2):
        return set_1 ^ set_2
