#!/usr/bin/python3


def uppercase(str):

    for i in range(0, len(str)):

        str1 = ord(str[i])

        if ((str1 >= 97) and (str1 <= 122)):
            str1 = str1 - 32
            print("{:c}".format(str1), end="")

    print()
