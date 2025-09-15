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
            ValueError: If size is < 0"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)
