#!/usr/bin/python3
"""Define a class Square with validations for its size attribute."""

class Square:
    """Represent a square with validations.
    
    Attributes:
        __size (int): The size of the square, validated to be an
        integer and 
                      greater than or equal to 0.
    """

    def __init__(self, size=0):
        """Initialize a new Square with validations.

        Args:
            size (int, optional): The size of the new square.
            Defaults to 0.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
