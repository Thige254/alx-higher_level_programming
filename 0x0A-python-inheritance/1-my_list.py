#!/usr/bin/python3
"""Defines MyList class which inherits from list."""


class MyList(list):'l'
    """A class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
