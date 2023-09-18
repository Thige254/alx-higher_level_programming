#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Width getter and setter
    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        # To later include validations here
        self.__width = value

    # Height getter and setter
    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        # To later include validations here
        self.__height = value

    # x getter and setter
    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        # To later include validations here
        self.__x = value

    # y getter and setter
    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        # To later include validations here
        self.__y = value
