#!/usr/bin/python3
"""creates an obj from json"""


import json

# Ukn_himself


def load_from_json_file(filename):
    """defined a LFJ function"""

    with open(filename) as ukn:
        return json.load(ukn)
