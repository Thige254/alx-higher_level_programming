#!/usr/bin/python3
"""Defines a function to deserialize a JSON string to an object."""


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): A JSON string representation.
    Returns:
        any: The Python data structure represented by my_str.
    """
    import json
    return json.loads(my_str)
