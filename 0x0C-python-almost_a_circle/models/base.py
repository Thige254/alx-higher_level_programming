#!/usr/bin/python3
import json
"""Module for Base class."""

class Base:
    """Base class to manage id attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dicts = []

        json_str = Base.to_json_string(list_dicts)

        with open(cls.__name__ + ".json", 'w') as file:
            file.write(json_str)


    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation `json_string`."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with set attributes."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square
        dummy.update(**dictionary)  # Update the dummy instance
        return dummy


    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"

        # Check if file exists
        try:
            with open(filename, 'r') as file:
                list_of_dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        # Use list comprehension and the create method
        # to convert dictionaries to instances
        return [cls.create(**d) for d in list_of_dicts]
