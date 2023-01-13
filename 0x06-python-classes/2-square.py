#!/usr/bin/python3
# UKN himself
""" Creating a square """


class Square:
    def __init__(self, size=0):
        """ square defined """

        if size.isdigit():
            pass
        else:
            raise TypeError("size must be an integer")

    """ The above determined if size is an int """

    if size < 0:
        raise ValueError("size must be >= 0")
