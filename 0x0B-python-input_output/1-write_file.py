#!/usr/bin/python3

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

# This function will overwrite existing content or create a new file if it doesn't exist.
