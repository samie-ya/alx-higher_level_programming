#!/usr/bin/python3
"""This script handles errors"""

if __name__ == "__main__":
    from urllib import request, error
    import sys
    try:
        with request.urlopen(sys.argv[1]) as res:
            response = res.read()
    except error.HTTPError as e:
        print("Error code:", e.code)
    else:
        print(response.decode("utf-8"))
