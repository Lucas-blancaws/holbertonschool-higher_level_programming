#!/usr/bin/python3

"""
Module construct class shape
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):

        """rectangle"""

        self.width = width
        self.height = height

    def area(self):

        """area"""

        return self.width * self.height

    def perimeter(self):

        """perimeter """

        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of any shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
