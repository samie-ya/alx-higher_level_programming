#!/usr/bin/python3


def uppercase(str):

    for i in str:

        str1 = ord(i)

        if ((str1 >= 97) and (str1 <= 122)):
            str1 = str1 - 32
        else:
            str1 = ord(i)
        print("{:c}".format(str1), end="")

    print()
