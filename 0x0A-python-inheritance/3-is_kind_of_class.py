#!/usr/bin/python3
"""Defines a class & its inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of,
    or if it has inherited from, a specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance or subclass
        instance of a_class; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
