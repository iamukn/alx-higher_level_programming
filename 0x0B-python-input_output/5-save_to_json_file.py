#!/usr/bin/python3
"""declaring a json function"""


import json


def save_to_json_file(my_obj, filename):
    """the json function is defined"""

    with open(filename, 'w', encoding="utf-8") as ukn:
        ukn.write(json.dumps(my_obj))
