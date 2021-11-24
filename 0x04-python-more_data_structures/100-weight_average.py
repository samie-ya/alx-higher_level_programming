#!/usr/bin/python3


def weight_average(my_list=[]):
    total = 0
    div = 0
    if my_list != []:
        for score in my_list:
            total += (score[0] * score[1])
            div += score[1]
        average = total / div
        return average
    return 0
