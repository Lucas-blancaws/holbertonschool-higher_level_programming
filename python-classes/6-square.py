#!/usr/bin/python3
"""Defines a class Square with size validation"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional private size attribute
        Args:
            size (int): The size of the square (default = 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is < 0"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):

        """Returns position"""

        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):

        """
        Set the position of the square.

        Args:
            value (tuple of int): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """

        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for x in range(self.position[1]):
                print()
            for y in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
