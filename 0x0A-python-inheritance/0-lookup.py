#!/usr/bin/python3
"""defines an object attribute function."""


def lookup(obj):
    """returns list of an object's available attributes."""
    return (dir(obj))
