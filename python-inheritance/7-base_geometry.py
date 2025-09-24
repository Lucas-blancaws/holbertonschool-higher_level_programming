#!/usr/bin/python3
"""Module 6-base_geometry: class BaseGeometry with area method"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """
        Raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is an integer greater than 0.

        Args:
            name (str): the name of the value (always a string)
            value (any): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
