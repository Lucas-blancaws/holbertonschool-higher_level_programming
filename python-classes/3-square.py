#!/usr/bin/python3
"""Defines a class Square with size validation"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Initialize the square with an optional private size attribute
        Args:
            size (int): The size of the square (default = 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
