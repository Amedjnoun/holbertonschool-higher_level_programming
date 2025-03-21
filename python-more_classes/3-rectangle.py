#!/usr/bin/python3
"""
This module defines the Rectangle class, which represents a rectangle
with attributes for width and height. It includes a __str__ method
to provide a string representation of the rectangle using the '#' character.
"""


class Rectangle:
    """Represents a rectangle with string representation using '#'."""
    # ...existing code...

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])
