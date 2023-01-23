#!/usr/bin/python3
# Ukn himself

"""Creating a class MyList"""


class MyList(list):
    """ Mylist class"""

    def print_sorted(self):
        """prints sorted list
        Args:
        self: object itself
        """
        print(sorted(self))
