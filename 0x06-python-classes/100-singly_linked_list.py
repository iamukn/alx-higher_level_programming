#!/usr/bin/python3
# Ukn himself

"""Defining a Node class"""


class Node:
    """Defined an empty node class"""
    def __init__(self, data, next_node=None):
        """created a node object
        Args:
            data: the data object
            next_node: the node holder
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ retrieves data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """ Sets data attribute"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ Retrieve the next_node attribute"""

        return (self.__next_node = next_node)

    @next_node.setter
    def next_node(self, value):
        """set the next_node value"""

        if (value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value

""" Defining a singly linked class"""


class SinglyLinkedList:
    """Defined a SLL class"""
    def __init__(self):
        """defined a sll object with head attr
        """

        self.head = None

    def __str__(self):
        """make list printable"""

        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
        return printsll[:-1]

    def sorted_insert(self, value):
        """ insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """

        new = Node(value)
        if not self.head:
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
