#!/usr/bin/python3
"""Define a MagicClass exactly like the given bytecode"""

import math


class MagicClass:
    """Class that encapsulates a circle's behavior and properties"""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Compute and return the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Compute and return the circumference of the circle."""
        return (2 * math.pi * self.__radius)