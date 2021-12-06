#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        errormessage = "Exception: Unknown format code 'd'\
 for object of type 'str'"
        print(errormessage, file=sys.stderr)
        return False
    else:
        return True
