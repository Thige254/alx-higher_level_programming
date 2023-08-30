import math

class MagicClass:

    def __init__(self, radius=0):
        """Initialize a new MagicClass."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Compute the area of a circle with the current radius."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Compute the circumference of a circle with the current radius."""
        return 2 * math.pi * self.__radius
