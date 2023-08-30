#!/usr/bin/python3
"""Module that defines a Square with position and size attributes."""

class Square:
    """A representation of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructs a new Square with optional size and position.

        Args:
            size (int): Length of the square's sides.
            position (tuple): Coordinates of the square in 2D space.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve or assign the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size while validating its type and value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve or assign the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position while validating its type and value."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Display the square using the # character, respecting its position."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            print("")

    def __str__(self):
        """Generate a string representation of the square suitable for printing."""
        result = ""
        if self.__size != 0:
            result += "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            if i != self.__size - 1:
                result += "\n"
        return result
