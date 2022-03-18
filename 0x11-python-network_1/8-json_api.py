#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to"""

if __name__ == "__main__":
    import requests
    import sys
    value = {}
    if (len(sys.argv[1]) < 2):
        value = {'q', ""}
    value = {'q', sys.argv[1]}
    try:
        resp = requests.post('http://0.0.0.0:5000/search_user', data=value)
        res = resp.json()
    except Exception as e:
        print("Not a valid JSON")
    else:
        if (res == {}):
            print("No result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
