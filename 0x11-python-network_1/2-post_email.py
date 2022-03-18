#!/usr/bin/python3
"""This script will use POST to add a data to a url"""

if __name__ == "__main__":
    from urllib import request, parse
    import sys
    url = sys.argv[1]
    value = sys.argv[2]
    email = parse.urlencode(value.encode("utf-8"))
    req = request.Request(url, data=email)
    with request.urlopen(req) as resp:
        page = response.read()
        print(page.decode("utf-8")
