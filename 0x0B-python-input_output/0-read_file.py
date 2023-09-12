#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """Read a text file and print its content to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
