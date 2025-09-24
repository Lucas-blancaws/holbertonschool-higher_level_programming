#!/usr/bin/python3
"""Module 8-rectangle: defines class Rectangle that inherits BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inherits BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialize a Rectangle with validated width and height.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
