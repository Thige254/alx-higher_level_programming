#!/usr/bin/python3

def write_file(filename="", text=""):
    """Write a string in a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): Text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
