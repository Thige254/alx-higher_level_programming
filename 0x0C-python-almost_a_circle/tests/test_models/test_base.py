#!/usr/bin/python3
""" Module for testing the Base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ TestBase class """

    def test_id(self):
        """ Test id functionality """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()

    def test_to_json_string_None(self):
        """ Test to_json_string with None """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_None(self):
        """ Test to_json_string with None """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """ Test to_json_string with an empty list """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list_of_dictionaries(self):
        """ Test to_json_string with a list containing a dictionary """
        self.assertEqual(Base.to_json_string([{'id': 12}]),
                         '[{"id": 12}]')

    def test_to_json_string_returns_string(self):
        """ Test that to_json_string returns a string """
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_from_json_string_None(self):
        """ Test from_json_string with None """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        """ Test from_json_string with an empty string """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_string_of_list_of_dictionaries(self):
        """ Test from_json_string with a string representing a list of dictionaries """
        self.assertEqual(Base.from_json_string('[{"id": 89}]'),
                         [{"id": 89}])

    def test_from_json_string_returns_list(self):
        """ Test that from_json_string returns a list """
        self.assertIsInstance(Base.from_json_string('[{"id": 89}]'), list)
