#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 3, 2]), 3)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.2]), 3.3)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)
