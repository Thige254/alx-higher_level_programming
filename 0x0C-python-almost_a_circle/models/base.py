#!/usr/bin/python3
import json
import csv
import turtle

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None or len(list_objs) == 0:
                return

            if cls.__name__ == "Rectangle":
                attributes = ["id", "width", "height", "x", "y"]
            else:  # Square
                attributes = ["id", "size", "x", "y"]

            writer = csv.DictWriter(csvfile, fieldnames=attributes)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        instances = []

        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Convert each value to int since CSV handles data in strings
                    for key, value in row.items():
                        row[key] = int(value)
                    instances.append(cls.create(**row))
        except FileNotFoundError:
            pass

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Use Turtle graphics module to drawlist of rectangles and squares."""

        # Create new turtle screen
        window = turtle.Screen()
        window.bgcolor("white")  # Set background color

        # Create new turtle object
        t = turtle.Turtle()
        t.speed(1)  # Slowest speed

        # Draw a given rectangle or square
        def draw_shape(obj):
            t.penup()
            t.goto(obj.x, obj.y)
            t.pendown()
            for _ in range(2):
                if isinstance(obj, Rectangle):
                    t.forward(obj.width)
                else:  # it's a square
                    t.forward(obj.size)
                t.right(90)
                if isinstance(obj, Rectangle):
                    t.forward(obj.height)
                else:  # it's a square
                    t.forward(obj.size)
                t.right(90)

        # Draw each rectangle
        for rect in list_rectangles:
            draw_shape(rect)

        # Draw each square
        for square in list_squares:
            draw_shape(square)

        # Close the turtle graphics window
        window.mainloop()
