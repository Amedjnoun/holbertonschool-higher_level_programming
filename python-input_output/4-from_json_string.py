#!/usr/bin/python3
"""
Module that defines the from_json_string function.
"""

import json

def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to an object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
