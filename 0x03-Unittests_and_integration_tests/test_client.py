#!/usr/bin/env python3
"""
Parameterize and patch as decorators.
Mocking a property.
"""

import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ A Test class for test_org method. """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, input, result, mock_get_json):
        """
        A test_org method with two arguments that is extended from
        TestGithubOrgClient class with input, expect are the arguments.
        """
        mock_get_json.return_value = result
        self.assertEqual(GithubOrgClient(input).org, result)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{input}")

    def test_public_repos_url(self):
        """ Test the result of public_repos_url """
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "World"}
            test_class = GithubOrgClient('check')
            result = test_class._public_repos_url
            self.assertEqual(result, mock.return_value["repos_url"])
