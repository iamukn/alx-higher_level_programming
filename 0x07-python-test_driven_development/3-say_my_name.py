#!/usr/bin/python3
# Ukn_himself

""" Defining a function"""


def say_my_name(first_name, last_name=""):
    """ Defined a say_my_name function
    Args:
        first_name: first arg
        last_name: second arg
    Raises:
        TypeError: if first and second arg are not strings,
        raise exception with message first name must be a string or
        last name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    message = "My name is {} {}"
    print(message.format(first_name, last_name))
