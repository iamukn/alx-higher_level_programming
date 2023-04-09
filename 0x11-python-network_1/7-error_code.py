#!/usr/bin/python3
""" Script that takes a URL and sendis a
request to the URL and displays the body of the response """

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if res.status_code > 200:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
