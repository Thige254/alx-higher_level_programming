#!/usr/bin/python3
"""Module that defines a Square class with comparators based on area."""

class Square:
    """Represents a square with methods for calculating area and comparisons."""

    def __init__(self, size=0):
        """
        Constructs a Square instance.

        Args:
            size (float or int): Length of the square's sides.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size while validating its type and value."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

    # Comparator methods based on the square's area
    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if current square has an area less than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if current square has an area less than or equal to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if current square has an area greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if current square has an area greater than or equal to the other."""
        return self.area() >= other.area()
