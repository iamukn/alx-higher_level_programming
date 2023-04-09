#!/usr/bin/python3
""" script that takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header """


from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) > 1:
        url = argv[1]
        req = requests.get(url)
        Id = req.headers.get('X-Request-Id')
        print(Id)
    else:
        pass
