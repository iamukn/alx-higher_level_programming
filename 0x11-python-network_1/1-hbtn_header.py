#!/usr/bin/python3
""" Sends a url request using the url passed as argument """

from sys import argv
from urllib import request
if __name__ == "__main__":
    if len(argv) > 1:
        url = argv[1]
        res = request.urlopen(url)
        with res as result:
            print(result.headers.get("X-Request-Id"))
    else:
        print("You didn't pass any argument")
