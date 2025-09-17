#!/usr/bin/python3
"""Defines a class Rectangle with size validation"""


class Rectangle:
    """An empty class that defines a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):

        """Returns the width"""

        return self.__width

    @property
    def height(self):
        """Returns the width"""

        return self.__height

    @width.setter
    def width(self, value):

        """
        Set the width of the rectangle.

        Args:
            value (int): the new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):

        """
        Set the height of the rectangle.

        Args:
            value (int): the new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle as a string of #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        linesR = []
        symbol = str(self.print_symbol)
        for i in range(self.__height):
            linesR.append(symbol * self.__width)
        return "\n".join(linesR)

    def __repr__(self):
        """Return a string to recreate the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
