#!/usr/bin/python3

import urllib.request
import urllib.error
from sys import argv
""" Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the response
(decoded in utf-8) Prevents the script from running when its imported """

if __name__ == "__main__":

        url = argv[1]
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        try:
            with res as f:
                print(f.read().decode('ascii'))
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")
