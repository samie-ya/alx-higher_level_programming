#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password) id"""

if __name__ == "__main__":
    import requests
    import sys
    resp = requests.get('https://api.github.com/user', auth=(sys.argv[1],
                        sys.argv[2]))
    json_resp = resp.json()
    print(json_resp['id'])
