#!/usr/bin/python3
"""This script will get the value of X-Request-Id"""

if __name__ == "__main__":

    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
