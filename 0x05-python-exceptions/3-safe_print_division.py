#!/usr/bin/python3


def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    finally:
        if (b > 0):
            print("Inside result: {}".format(div))
            return div
