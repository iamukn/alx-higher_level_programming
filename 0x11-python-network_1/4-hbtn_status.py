#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """


import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        req = requests.get(url)
        with req as res:
            print("Body response:")
            print(f"\t- type: {type(req.text)}")
            print(f"\t- content: {res.text}")
    except requests.exceptions.HTTPError as e:
        print(e.errno)
