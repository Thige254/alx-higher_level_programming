#!/usr/bin/python3
"""Define a class to represent a Square."""


class Square:
    """Class that represents a geometric square."""

    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size (int): The edge length of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current edge length of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
