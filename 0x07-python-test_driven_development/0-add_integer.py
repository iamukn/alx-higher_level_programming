#!/usr/bin/python3
# Ukn_himself
""" Defining an integer function"""


def add_integer(a, b=98):
    """ defined an integer func
    Args:
        a = the first argument
        b = the second argument which has a default value of 98
    Raises:
        if a and be is not an int or a float, raise a TypeError
        with the message a must be an integer or b must be an integer
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
