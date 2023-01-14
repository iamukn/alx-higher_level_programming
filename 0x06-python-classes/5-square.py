#!/usr/bin/python3
# Ukn_himself

"""Defining a Square"""


class Square:
    """Defining a Square Class"""

    def __init__(self, size=0):
        """ Assigning a size variable
        Args:
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
        """ retrieving the size data"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculates the area
        Returns: The square of the size value
        """

        return self.__size ** 2

    def my_print(self):
        """print the square in #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
