#!/usr/bin/python3
"""This script will get the value of X-Request-Id"""

if __name__ == "__main__":

    from urllib.request import urlopen
    import sys

    with urlopen(sys.argv[1]) as res:
        print(res.getheader("X-Request-Id"))
