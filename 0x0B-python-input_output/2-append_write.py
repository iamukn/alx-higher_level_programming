#!/usr/bin/python3
# ukn_himself


""" defining an append-write module"""


def append_write(filename="", text=""):
    """declaring an append_write module"""

    with open(filename, 'a', encoding="utf-8") as ukn:
        return ukn.write(text)
