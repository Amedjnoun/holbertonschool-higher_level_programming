#!/usr/bin/python3
"""
Module that defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of or inherited from a_class or  False.
    """
    return isinstance(obj, a_class)
