#!/usr/bin/python3
"""Define classes for representing a singly-linked list."""


class Node:
    """Defines a node in a singly-linked list."""

    def __init__(self, content, next_reference=None):
        """Initialize a Node instance.

        Parameters:
            content (int): The content/data of the node.
            next_reference (Node): Reference to the next node in the list.
        """
        self.content = content
        self.next_reference = next_reference

    @property
    def content(self):
        """Get/set the content/data of the Node."""
        return (self.__content)

    @content.setter
    def content(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__content = value

    @property
    def next_reference(self):
        """Get/set the next node reference of this Node."""
        return (self.__next_reference)

    @next_reference.setter
    def next_reference(self, reference):
        if not isinstance(reference, Node) and reference is not None:
            raise TypeError("next_reference must be a Node object")
        self.__next_reference = reference


class SinglyLinkedList:
    """Represents a singly-linked list structure."""

    def __init__(self):
        """Initialize a SinglyLinkedList instance with no head node."""
        self.__starter_node = None

    def ordered_insert(self, value):
        """Insert a new Node in the correct position of the SinglyLinkedList.

        The node's position is determined by the numerical value 
        to ensure the list remains sorted.

        Parameters:
            value (int): The content/data for the new Node.
        """
        new_node = Node(value)
        if self.__starter_node is None:
            self.__starter_node = new_node
        elif self.__starter_node.content > value:
            new_node.next_reference = self.__starter_node
            self.__starter_node = new_node
        else:
            current = self.__starter_node
            while (current.next_reference is not None and
                    current.next_reference.content < value):
                current = current.next_reference
            new_node.next_reference = current.next_reference
            current.next_reference = new_node

    def __str__(self):
        """Provide a string representation of the SinglyLinkedList content."""
        nodes_content = []
        current = self.__starter_node
        while current is not None:
            nodes_content.append(str(current.content))
            current = current.next_reference
        return ('\n'.join(nodes_content))
