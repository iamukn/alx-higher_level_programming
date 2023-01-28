#!/usr/bin/python3
# ukn_himself
import os

"""A module that writes a string to a text file"""


def write_file(filename="", text=""):
    """Defining the write_file module"""

    with open(filename, mode='w', encoding="utf-8") as f:
         return f.write(text)
