#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = 0
    i = 0
    my_list = []
    while (i < list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            my_list.append(result)
        i += 1
    return my_list
