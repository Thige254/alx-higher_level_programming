#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    that inherited (directly or indirectly)
    from a specified class.

    Args:
        obj: The object to check.
        a_class: The base class to check against.

    Returns:
        True if obj is an instance of a subclass of
        a_class; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
