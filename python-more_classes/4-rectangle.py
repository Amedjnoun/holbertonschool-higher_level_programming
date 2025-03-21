#!/usr/bin/python3
"""
This module defines the Rectangle class, which represents a rectangle
with attributes for width and height. It includes a __repr__ method
to provide a string representation for recreating the instance.
"""


class Rectangle:
    # ...existing code...

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
