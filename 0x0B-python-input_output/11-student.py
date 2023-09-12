#!/usr/bin/python3
"""
This module contains a class Student that defines a
student by certain attributes.
"""


class Student:
    """Defines a student.

    Attributes:
        first_name (str): First name of the student.
        last_name (str): Last name of the student.
        age (int): Age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize the student object.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of strings representin
            attribute names. Defaults to None.

        Returns:
            dict: Dictionary representation of the Student.
        """
        if attrs is not None and isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary representing a Student's attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
