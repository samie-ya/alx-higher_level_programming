#!/usr/bin/python3


def best_score(a_dictionary):
    best = 0
    if a_dictionary:
        for i in a_dictionary:
            dic = a_dictionary[i]
            if dic > best:
                best = dic
                scorer = i
        return scorer
    return
