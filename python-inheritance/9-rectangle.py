#!/usr/bin/python3
"""
Module that defines the Rectangle class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
