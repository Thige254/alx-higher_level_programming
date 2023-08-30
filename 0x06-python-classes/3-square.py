#!/usr/bin/python3
"""Define a class Square with a method to compute its area."""

class Square:
    """Represent a square.
    
    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the new square. Defaults to 0.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square's area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
