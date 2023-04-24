#!/usr/bin/python3
"""
Parameterize and patch as decorators.
"""

import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    """ A Test class for test_org method. """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, inp, expect, mock_get_json):
        """
        A test_org method with two arguments that is extended from
        TestGithubOrgClient class with input, expect are the arguments.
        """
        mock_get_json.return_value = expect
        client = GithubOrgClient(inp)
        self.assertEqual(client.org, expect)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{inp}")