#!/usr/bin/python3
"""This script handles errors"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys
    try:
        request = urlopen(sys.argv[1])
        response = request.read()
    except HTTPError as e:
        print("Error: ", e.code)
    else:
        print(response.decode("utf-8"))
