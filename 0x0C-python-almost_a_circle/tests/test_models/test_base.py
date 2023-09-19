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
