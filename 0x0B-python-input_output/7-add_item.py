#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and then saves them to a file.
"""

import sys  # To access command line arguments
from os import path  # To check if a file exists

# Import the functions from the provided modules
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Check if the file exists. If it does, load its content.
# Otherwise, initialize an empty list.
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add the command line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
