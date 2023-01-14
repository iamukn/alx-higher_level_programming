#!/usr/bin/python3
# Ukn_himself

"""Defining a Square"""


class Square:
    """Defining a Square Class"""

    def __init__(self, size=0):
        """ Assigning a size variable
        Args:
            self: This represents the Square object
            size: This reps the attribute
        Raises:
            TypeError: if size is not an interger
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """ Retrieving size using the getter"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the square of the size"""
        return (self.__size ** 2)
