#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Defines a TestAccessNestedMap class that inherits from unittest.TestCase.
    It then defines a test_access_nested_map method that uses decorator
    called @parameterized.expand, to test the access_nested_map function
    for different inputs.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        This method takes 3 arguments: nested_map, nested_map, path and
        expexted output. Then uses the assertEqual to test that function
        returns the expected output for each input
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         exception_type):
        """
        Test method for the access_nested_map_function with exception handling
        """
        with self.assertRaises(exception_type) as context:
            access_nested_map(nested_map, path)
        self.assertTrue(str(context.exception).startswith("KeyError"))
