#!/usr/bin/python3
"""Define a locked class."""

class LockedClass:
    """
    Prevent the user making new LockedClass attributes
    for anything else but 'first_name' attributes.
    """

    __slots__ = ["first_name"]
