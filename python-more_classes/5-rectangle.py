#!/usr/bin/python3
"""
This module defines the Rectangle class, which represents a rectangle
with attributes for width and height. It includes a destructor method
that prints a message upon instance deletion.
"""


class Rectangle:
    # ...existing code...

    def __del__(self):
        print("Bye rectangle...")
