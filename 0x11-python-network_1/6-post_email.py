#!/usr/bin/python3
"""This script will use POST to add a data to a url"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
