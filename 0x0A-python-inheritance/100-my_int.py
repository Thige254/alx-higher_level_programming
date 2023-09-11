#!/usr/bin/python3
"""Defines a class MyInt.It inherits from int."""


class MyInt(int):
    """A rebel version of int, inverts == and !=."""

    def __eq__(self, value):
        """OVERWRITE '==' with '!=' ."""
        return self.real != value

    def __ne__(self, value):
        """OVERWRITE '!=' with '==' ."""
        return self.real == value
