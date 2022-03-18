#!/usr/bin/python3
"""This script will fetch a url"""

if __name__ == "__main__":
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- utf8 content: {}".format(r.text))
