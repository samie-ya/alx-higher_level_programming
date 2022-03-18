#!/usr/bin/python3
"""This script handles errors"""

if __name__ == "__main__":
    from urllib import request, error
    import sys
    try:
        req = request.urlopen(sys.argv[1])
        response = req.read()
    except error.HTTPError as e:
        print("Error: ", e.code)
    else:
        print(response.decode("utf-8"))
