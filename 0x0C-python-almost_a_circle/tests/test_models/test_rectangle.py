#!/usr/bin/python3
"""Module to test the Rectangle class"""

from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_basic_instance(self):
        """Basic test for rectangle instance creation"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 5, 6, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 6)
        self.assertEqual(r2.id, 12)

    def test_type_errors(self):
        """Test type validation in Rectangle class"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0")
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0")

    def test_value_errors(self):
        """Test value validation in Rectangle class"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area_method(self):
        """Test area calculation of Rectangle class"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(5, 3)
        self.assertEqual(r2.area(), 15)

class TestRectangleDisplay(unittest.TestCase):
    """Test cases for the display method of the Rectangle class"""

    def setUp(self):
        """Set up method to redirect stdout to a StringIO object"""
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """Tear down method to close and delete the StringIO object"""
        self.held_output.close()
        del self.held_output
        sys.stdout = sys.__stdout__

    def test_display_basic(self):
        """Tests the basic display method without x and y offsets."""
        r = Rectangle(3, 2)
        r.display()
        self.assertEqual(self.held_output.getvalue(), "###\n" * 2)

        self.held_output.truncate(0)
        self.held_output.seek(0)

        r = Rectangle(2, 4)
        r.display()
        self.assertEqual(self.held_output.getvalue(), "##\n" * 4)

    def test_display_with_xy(self):
        """Tests the display method with x and y offsets."""
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        self.assertEqual(self.held_output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        self.held_output.truncate(0)
        self.held_output.seek(0)

        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        self.assertEqual(self.held_output.getvalue(), " ###\n" * 2)


    def test_update_args(self):
        """Tests updating attributes using *args."""
        r1 = Rectangle(10, 10, 10, 10, 1)

        r1.update(12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(13, 5)
        self.assertEqual(r1.id, 13)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(14, 6, 7)
        self.assertEqual(r1.id, 14)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(15, 8, 9, 2)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 8)
        self.assertEqual(r1.height, 9)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 10)

        r1.update(16, 11, 12, 3, 4)
        self.assertEqual(r1.id, 16)
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_update_no_args(self):
        """Tests update method with no arguments passed."""
        r2 = Rectangle(5, 5, 1, 1, 2)

        r2.update()
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
    def test_update_kwargs(self):
        """Tests updating attributes using **kwargs."""
        r1 = Rectangle(10, 10, 10, 10, 1)

        r1.update(height=2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

        r1.update(width=3, x=4)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

        r1.update(id=5, y=6)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.y, 6)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)

    def test_update_args_and_kwargs(self):
        """Tests updating attributes using both *args and **kwargs."""
        r2 = Rectangle(5, 5, 1, 1, 2)

        r2.update(10, 10, x=1, y=2)
        self.assertEqual(r2.id, 10)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)


    def test_update_no_args_no_kwargs(self):
        """Tests update method with no arguments or kwargs passed."""
        r3 = Rectangle(5, 5, 1, 1, 2)

        r3.update()
        self.assertEqual(r3.id, 2)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 1)

    def test_update_invalid_kwargs(self):
        """Tests update method with invalid kwargs."""
        r4 = Rectangle(5, 5, 1, 1, 2)

        r4.update(color="red")
        self.assertEqual(r4.id, 2)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 5)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 1)
        with self.assertRaises(AttributeError):
            r4.color
