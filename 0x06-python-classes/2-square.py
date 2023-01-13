#!/usr/bin/python3
# UKN himself
""" Creating a square """


class Square:
    def __init__(self, size=0):
        """ square defined """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
