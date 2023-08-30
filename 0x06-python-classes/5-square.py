#!/usr/bin/python3
"""Define a class Square with properties and methods to manipulate it."""

class Square:
    """Represent a square with properties to retrieve and set its size, 
    a method to compute its area, and another to print it.
    """

    def __init__(self, size=0):
        """Initialize a new square with a given size.

        Args:
            size (int, optional): The size of the new square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
            
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square's area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#'.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
