#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password) id"""

if __name__ == "__main__":
    import requests
    import sys
    resp = requests.get('https://api.github.com/repos/' + sys.argv[2] +
                        '/' + sys.argv[1] + '/commits')
    json_resp = resp.json()
    new_list = json_resp[:10]
    for i in new_list:
        print("{}: {}".format(i["sha"], i["commit"]["author"]["name"]))
