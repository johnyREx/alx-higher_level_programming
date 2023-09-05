#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """The unittest class
    """
    def test_len_cannot_be_called_on_argument(self):
        """Test that the argument passed to the function does not support the len function"""
        self.assertRaises(TypeError, max_integer, 3)
