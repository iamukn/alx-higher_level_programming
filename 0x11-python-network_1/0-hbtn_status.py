#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/statis"""
from urllib import request


if __name__ == "__main__":
    """ assigns the urls to a variable url
    """
    url = "https://alx-intranet.hbtn.io/status"
    """ sends a urlopen api request to fetch the
        information from the website """
    res = request.Request(url)
    result = request.urlopen(res)
    with result as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print(f"\t- content: {data}")
        print("\t- utf8 content: {}".format(data.decode("utf8")))
