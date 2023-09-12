#!/usr/bin/python3
"""Defines a function to write an object to a file using its JSON representation."""

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj (any): The Python object to write.
        filename (str): The name of the file to write to.
    """
    import json

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
