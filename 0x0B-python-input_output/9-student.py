#!/usr/bin/python3
"""
Module 9-student
Defines a student by public instance attributes:
- first_name
- last_name
- age
"""

class Student:
    """Representation of a student."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
