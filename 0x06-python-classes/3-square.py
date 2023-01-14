#!/usr/bin/python3
# UKN_himself

"""defining a square"""


class Square:
    def __init__(self, size=0):
        """ initializing the square class
        Arg:
            self: this represents the object
            size: represents the attribute required
        Raises: raises an error if size is not a digit
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculating the area
        Return: Size raised to power 2
        """

        return (self.__size ** 2)
