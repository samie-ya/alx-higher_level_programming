#!/usr/bin/python3


def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except ZeroDivisionError:
        return None
    finally:
        if (b > 0):
            print("Inside result: {}".format(div))
            return div
        else:
            print("Inside result: None")
