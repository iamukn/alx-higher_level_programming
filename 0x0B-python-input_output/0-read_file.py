#!/usr/bin/python3
# Ukn himself
""" This moducle defines a text file reading func"""


def read_file(filename=""):
    """prints the content of the UTF text file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
