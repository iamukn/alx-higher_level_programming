#!/usr/bin/python3
# Ukn_himself

"""Defining a Rectangle"""


class Rectangle:
    """Defining an empty rectangle"""

    pass

    def __init__(self, width=0, height=0):
        """Defining a new object
        Args:
            width: The first attribute
            height: The second attribute
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieving the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setting the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retrieving the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value