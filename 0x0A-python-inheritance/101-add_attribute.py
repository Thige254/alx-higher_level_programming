#!/usr/bin/python3
"""Defines a function that adds a new
attribute to an object if possible."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): Object to add an attribute to.
        att (str): Name of attribute to add.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
