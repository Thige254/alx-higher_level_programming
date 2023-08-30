#!/usr/bin/python3

class Node:
    """Represents a single node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the node with data and next reference."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize the list with a head set to None."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""
        values = []
        node = self.__head
        while node:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a value into the correct position to keep list sorted."""
        new_node = Node(value)
        if not self.__head or self.__head.data > value:
            new_node.next_node, self.__head = self.__head, new_node
            return
        node = self.__head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node, node.next_node = node.next_node, new_node
