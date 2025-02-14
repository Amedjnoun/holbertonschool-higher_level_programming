#!/usr/bin/python3
"""
Module that defines the CustomObject class with serialization and
deserialization using pickle.
"""

import pickle


class CustomObject:
    """
    A custom class with attributes name, age, and is_student.
    """

    def __init__(self, name, age, is_student):
        """
        __init__ method to initialize the CustomObject attributes.

        Args:
            name (string): name of the user
            age (int): age of the user
            is_student (bool): true / false if is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object to a file using pickle.

        Args:
            filename (str): The filename to save the serialized object.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file using pickle.

        Args:
            filename (str): The filename to load the serialized object from.

        Returns:
            object: The deserialized object or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
