#!/usr/bin/python3
"""Module 10-square: defines class Square that inherits Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits Rectangle"""

    def __init__(self, size):
        """
        Initialize a Square with validated size.

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
