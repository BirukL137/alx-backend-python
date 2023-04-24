#!/usr/bin/env python3
"""
Parameterize and patch as decorators.
Mocking a property.
More patching.
Parameterize.
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
                    'client.GithubOrgClient.org',
                    new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "World"}
            test_class = GithubOrgClient('check')
            result = test_class._public_repos_url
            self.assertEqual(result, mock.return_value["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, json_mock):
        """
        A method that tests the public repos
        """
        json_mock.return_value = [{"name": "Github"}, {"name": "Instagram"}]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos:

            mock_repos.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            test = []
            for i in [{"name": "Github"}, {"name": "Instagram"}]:
                test.append(i["name"])

            self.assertEqual(result, test)

            mock_repos.assert_called_once()
            json_mock.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, result):
        """ A method that tests has_license function from client file. """
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), result)
