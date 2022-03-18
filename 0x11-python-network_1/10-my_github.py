#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password) id"""

if __name__ == "__main__":
    import requests
    import sys
    resp = requests.get('https://api.github.com/user',
                        auth=requests.auth.HTTPBasicAuth(sys.argv[1],
                                                         sys.argv[2]))
    if (resp.status_code == 200):
        json_resp = resp.json()
        print(json_resp['id'])
    else:
        print(None)
