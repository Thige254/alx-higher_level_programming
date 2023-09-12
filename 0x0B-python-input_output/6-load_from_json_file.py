#!/usr/bin/python3
"""Defines a function to create an object from a JSON file."""

def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.
    Returns:
        any: The Python data structure represented in the file.
    """
    import json

    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
