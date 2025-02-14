#!/usr/bin/python3
"""
Module that defines the class_to_json function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: The object to convert to a dictionary.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
