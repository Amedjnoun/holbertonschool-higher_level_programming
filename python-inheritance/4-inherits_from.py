#!/usr/bin/python3
"""
Module that defines the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is instance of a class that inherited from a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
