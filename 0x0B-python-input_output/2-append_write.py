#!/usr/bin/python3
"""
This module provides functions to append to text files.
"""

def append_write(filename="", text=""):
    """Append a string to a UTF8 text file and return
    the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
